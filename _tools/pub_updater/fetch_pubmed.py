"""Fetch publications from PubMed via NCBI E-utilities (Biopython Entrez).

Network note: NCBI is only reachable from environments with open outbound
access (e.g. GitHub Actions runners), not from the restricted Claude Code web
sandbox. To develop and test parsing offline, save an efetch XML response and
feed it through :func:`parse_efetch_xml` (see update.py ``--from-xml``).
"""

from __future__ import annotations

import time
from io import BytesIO
from typing import List, Optional

from Bio import Entrez  # type: ignore

from model import Publication

# Journal/source names that mark a record as a preprint rather than a
# peer-reviewed article (case-insensitive substring match).
_PREPRINT_SOURCES = ("biorxiv", "medrxiv", "arxiv", "research square", "preprints.org", "ssrn")


def configure(email: str, tool: str = "neuroconn-pub-updater", api_key: str = "") -> None:
    """Set the Entrez globals NCBI requires before any request."""
    Entrez.email = email
    Entrez.tool = tool
    if api_key:
        Entrez.api_key = api_key


def search_pmids(raw_query: str, retmax: int = 1000) -> List[str]:
    """Run the raw PubMed query verbatim and return the matching PMIDs."""
    handle = Entrez.esearch(db="pubmed", term=raw_query, retmax=retmax)
    record = Entrez.read(handle)
    handle.close()
    return list(record.get("IdList", []))


def fetch_records(pmids: List[str], batch_size: int = 100) -> List[Publication]:
    """efetch the given PMIDs in batches and parse them to Publications."""
    pubs: List[Publication] = []
    for start in range(0, len(pmids), batch_size):
        batch = pmids[start : start + batch_size]
        handle = Entrez.efetch(db="pubmed", id=",".join(batch), rettype="xml", retmode="xml")
        xml = handle.read()
        handle.close()
        pubs.extend(parse_efetch_xml(xml))
        time.sleep(0.34)  # be polite to NCBI between batches
    return pubs


def parse_efetch_xml(xml) -> List[Publication]:
    """Parse a raw efetch XML response (bytes, str or file-like) to records."""
    if hasattr(xml, "read"):
        record = Entrez.read(xml)
    else:
        if isinstance(xml, str):
            xml = xml.encode("utf-8")
        record = Entrez.read(BytesIO(xml))
    return [_parse_article(a) for a in record.get("PubmedArticle", [])]


def _parse_article(article) -> Publication:
    medline = article["MedlineCitation"]
    art = medline["Article"]

    title = _strip(art.get("ArticleTitle", "")).rstrip(".")

    authors = []
    for a in art.get("AuthorList", []):
        last = a.get("LastName")
        if last:
            fore = a.get("ForeName") or a.get("Initials") or ""
            authors.append(f"{last}, {fore}".strip().rstrip(","))
        elif a.get("CollectiveName"):
            authors.append(str(a["CollectiveName"]))

    journal = _strip(art.get("Journal", {}).get("Title", ""))
    issue_info = art.get("Journal", {}).get("JournalIssue", {})

    pub = Publication(
        title=title,
        authors=authors,
        journal=journal,
        year=_extract_year(art),
        month=_extract_month(art),
        volume=str(issue_info.get("Volume", "")),
        issue=str(issue_info.get("Issue", "")),
        pages=str(art.get("Pagination", {}).get("MedlinePgn", "")),
        pmid=str(medline.get("PMID", "")),
        doi=_extract_doi(article),
        is_preprint=_is_preprint(art, journal),
    )
    pub.url = pub.doi_url()
    return pub


def _is_preprint(art, journal: str) -> bool:
    journal_l = journal.lower()
    if any(src in journal_l for src in _PREPRINT_SOURCES):
        return True
    for pt in art.get("PublicationTypeList", []):
        if str(pt).strip().lower() == "preprint":
            return True
    return False


def _extract_year(art) -> Optional[int]:
    pubdate = art.get("Journal", {}).get("JournalIssue", {}).get("PubDate", {})
    if "Year" in pubdate:
        try:
            return int(str(pubdate["Year"])[:4])
        except ValueError:
            pass
    for token in str(pubdate.get("MedlineDate", "")).split():
        if token[:4].isdigit():
            return int(token[:4])
    return None


def _extract_month(art) -> str:
    pubdate = art.get("Journal", {}).get("JournalIssue", {}).get("PubDate", {})
    return str(pubdate.get("Month", "")).strip()


def _extract_doi(article) -> str:
    for eid in article["MedlineCitation"]["Article"].get("ELocationID", []):
        if eid.attributes.get("EIdType") == "doi":
            return str(eid)
    for aid in article.get("PubmedData", {}).get("ArticleIdList", []):
        if aid.attributes.get("IdType") == "doi":
            return str(aid)
    return ""


def _strip(value) -> str:
    """Flatten Biopython's StringElement / list quirks to a plain string."""
    if isinstance(value, list):
        return " ".join(_strip(v) for v in value)
    return str(value).strip()
