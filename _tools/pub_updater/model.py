"""Normalized publication record shared across the updater modules.

A single dataclass keeps the PubMed fetcher, the BibTeX store and the page
updater agreed on field names, so changes propagate in one place.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Publication:
    """A single publication, source-agnostic.

    ``authors`` are stored as ("Lastname", "ForeName") tuples flattened to a
    "Last, Fore" string so a CSL style can re-format them however the page
    requires. ``is_preprint`` decides the BibTeX entry type (@misc vs
    @article), which is what keeps preprints out of the journal-article
    sections of the page.
    """

    title: str
    authors: List[str] = field(default_factory=list)
    journal: str = ""
    year: Optional[int] = None
    month: str = ""
    volume: str = ""
    issue: str = ""
    pages: str = ""
    doi: str = ""
    pmid: str = ""
    url: str = ""
    is_preprint: bool = False

    def identity(self) -> str:
        """Stable dedup key. DOI preferred, then PMID, then normalized title."""
        if self.doi:
            return "doi:" + self.doi.lower()
        if self.pmid:
            return "pmid:" + self.pmid
        return "title:" + _normalize_title(self.title)

    def first_author_last(self) -> str:
        if not self.authors:
            return "Anon"
        # "Lastname, Forename" -> "Lastname"; keep letters only for the key.
        last = self.authors[0].split(",")[0]
        return re.sub(r"[^A-Za-z]", "", last) or "Anon"

    def doi_url(self) -> str:
        return f"https://doi.org/{self.doi}" if self.doi else ""


def _normalize_title(title: str) -> str:
    return re.sub(r"[^a-z0-9]", "", title.lower())
