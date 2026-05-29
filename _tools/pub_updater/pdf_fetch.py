"""Best-effort open-access PDF retrieval.

Given a DOI, try a few open sources and save a PDF to downloads/pubs/. This is
strictly best-effort: every failure is swallowed and reported as "no PDF", so a
paywalled paper never breaks a run. Network access is required, so this only
does anything on a GitHub Actions runner, not in the restricted sandbox.

Uses only the standard library to avoid extra dependencies.
"""

from __future__ import annotations

import json
import os
import urllib.parse
import urllib.request
from typing import Optional

_UA = "neuroconn-pub-updater/1.0 (mailto:%s)"
_TIMEOUT = 30


def fetch_pdf(doi: str, dest_path: str, unpaywall_email: str) -> bool:
    """Try to download an OA PDF for ``doi`` to ``dest_path``. Returns success."""
    if not doi:
        return False
    for url in _candidate_urls(doi, unpaywall_email):
        if url and _download_if_pdf(url, dest_path, unpaywall_email):
            return True
    return False


def _candidate_urls(doi: str, email: str):
    """Yield candidate PDF URLs, cheapest/most-likely first."""
    doi_l = doi.lower()
    # Cold Spring Harbor preprints (bioRxiv / medRxiv) expose a direct PDF.
    if doi_l.startswith("10.1101/"):
        suffix = doi.split("/", 1)[1]
        yield f"https://www.biorxiv.org/content/{doi}v1.full.pdf"
        yield f"https://www.medrxiv.org/content/{doi}v1.full.pdf"
        del suffix
    # Unpaywall knows the best OA location for most published DOIs.
    yield _unpaywall_pdf_url(doi, email)


def _unpaywall_pdf_url(doi: str, email: str) -> Optional[str]:
    try:
        api = f"https://api.unpaywall.org/v2/{urllib.parse.quote(doi)}?email={urllib.parse.quote(email)}"
        with urllib.request.urlopen(_req(api, email), timeout=_TIMEOUT) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        loc = data.get("best_oa_location") or {}
        return loc.get("url_for_pdf")
    except Exception:
        return None


def _download_if_pdf(url: str, dest_path: str, email: str) -> bool:
    try:
        with urllib.request.urlopen(_req(url, email), timeout=_TIMEOUT) as resp:
            head = resp.read(5)
            if head[:4] != b"%PDF":
                return False
            os.makedirs(os.path.dirname(dest_path) or ".", exist_ok=True)
            with open(dest_path, "wb") as fh:
                fh.write(head)
                fh.write(resp.read())
        return os.path.getsize(dest_path) > 1024
    except Exception:
        return False


def _req(url: str, email: str) -> urllib.request.Request:
    return urllib.request.Request(url, headers={"User-Agent": _UA % email})
