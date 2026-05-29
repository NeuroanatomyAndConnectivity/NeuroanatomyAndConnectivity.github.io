"""Read the jekyll-scholar BibTeX file and append new entries to it.

The store is deliberately *append-only*: existing entries, their hand edits,
the section comments (``%% Articles:``) and the file ordering are all left
untouched. We only parse the file (read-only) to learn which publications and
citekeys already exist, then format new entries as text in the same style and
append them. jekyll-scholar sorts by year at build time, so file position of
new entries does not matter.
"""

from __future__ import annotations

import re
from typing import List, Set, Tuple

import bibtexparser

from model import Publication

# Order fields the way the existing file does: alphabetical, one-space indent.
_FIELD_ORDER = [
    "abstract", "author", "booktitle", "doi", "journal", "link", "month",
    "number", "pages", "pdf", "pmid", "publisher", "title", "url", "volume", "year",
]


def load_identities(bib_path: str) -> Tuple[Set[str], Set[str]]:
    """Return (existing publication identities, existing citekeys).

    Identities are DOI/PMID/normalized-title strings used to avoid adding a
    paper that is already present in any form.
    """
    identities: Set[str] = set()
    citekeys: Set[str] = set()
    try:
        with open(bib_path, encoding="utf-8") as fh:
            db = bibtexparser.load(fh)
    except FileNotFoundError:
        return identities, citekeys

    for entry in db.entries:
        citekeys.add(entry.get("ID", ""))
        if entry.get("doi"):
            identities.add("doi:" + entry["doi"].lower())
        if entry.get("pmid"):
            identities.add("pmid:" + entry["pmid"])
        if entry.get("title"):
            identities.add("title:" + re.sub(r"[^a-z0-9]", "", entry["title"].lower()))
    return identities, citekeys


def make_citekey(pub: Publication, taken: Set[str]) -> str:
    """Build a unique ``LastnameYEAR`` citekey, suffixing a, b, ... on clash."""
    base = f"{pub.first_author_last()}{pub.year or ''}"
    if base not in taken:
        taken.add(base)
        return base
    for suffix in "abcdefghijklmnopqrstuvwxyz":
        candidate = base + suffix
        if candidate not in taken:
            taken.add(candidate)
            return candidate
    # Extremely unlikely fallback.
    n = 1
    while f"{base}_{n}" in taken:
        n += 1
    taken.add(f"{base}_{n}")
    return f"{base}_{n}"


def format_entry(pub: Publication, citekey: str, pdf_path: str = "") -> str:
    """Render one BibTeX entry as text in the file's existing style."""
    entry_type = "misc" if pub.is_preprint else "article"
    fields = {
        "author": " and ".join(pub.authors),
        "title": pub.title,
        "year": str(pub.year) if pub.year else "",
    }
    if not pub.is_preprint:
        fields["journal"] = pub.journal
    if pub.doi:
        fields["doi"] = pub.doi
        fields["link"] = pub.doi_url()
        fields["url"] = pub.doi_url()
    if pub.volume:
        fields["volume"] = pub.volume
    if pub.issue:
        fields["number"] = pub.issue
    if pub.pages:
        fields["pages"] = pub.pages
    if pub.month:
        fields["month"] = pub.month
    if pub.pmid:
        fields["pmid"] = pub.pmid
    if pdf_path:
        fields["pdf"] = pdf_path

    lines = [f"@{entry_type}{{{citekey},"]
    ordered = [k for k in _FIELD_ORDER if fields.get(k)]
    for i, key in enumerate(ordered):
        value = _escape(fields[key])
        comma = "," if i < len(ordered) - 1 else ""
        lines.append(f" {key} = {{{value}}}{comma}")
    lines.append("}")
    return "\n".join(lines)


def append_entries(bib_path: str, entries: List[str]) -> None:
    """Append formatted entry blocks to the .bib, separated by blank lines."""
    if not entries:
        return
    with open(bib_path, "a", encoding="utf-8") as fh:
        for block in entries:
            fh.write("\n" + block + "\n")


def _escape(value: str) -> str:
    """Minimal BibTeX-safe escaping; braces in values would break parsing."""
    return value.replace("{", "(").replace("}", ")").strip()
