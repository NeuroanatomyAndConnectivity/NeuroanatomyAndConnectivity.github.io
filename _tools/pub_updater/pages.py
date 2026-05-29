"""Keep the per-year sections of research/publications.md in sync.

The page lists journal articles under one ``##### YYYY`` heading per year, each
followed by a jekyll-scholar ``{% bibliography ... year=YYYY %}`` block, in
descending order. When a publication appears for a year that has no heading yet
(typically a new current year), we insert the missing heading + block in the
right place. Existing headings are never reordered or rewritten.
"""

from __future__ import annotations

import re
from typing import Iterable, List, Set

# Marks the start and end of the journal-article year list on the page.
_SECTION_START = re.compile(r'^##\s*Journal articles\s*<a name="articles"></a>\s*$', re.M)
_SECTION_END = re.compile(r'^<hr class="style5">\s*$', re.M)
_YEAR_HEADER = re.compile(r'^#####\s*(\d{4})\s*<a name="\d{4}"></a>\s*$', re.M)


def _block_for(year: int) -> str:
    return (
        f'##### {year} <a name="{year}"></a>\n'
        f'{{% bibliography --style /bibcsl/acta.csl '
        f'--query @article[type!=preprint && year={year}] %}}'
    )


def existing_years(page_text: str) -> Set[int]:
    """Years that already have a heading in the journal-article section."""
    region = _article_region(page_text)
    if region is None:
        return set()
    start, end = region
    return {int(m.group(1)) for m in _YEAR_HEADER.finditer(page_text[start:end])}


def ensure_years(page_path: str, years: Iterable[int]) -> List[int]:
    """Ensure the page has a section for each given year. Returns years added.

    Only years strictly greater than the current maximum, or filling a gap
    between existing headings, are inserted; all insertions keep the list in
    descending order.
    """
    with open(page_path, encoding="utf-8") as fh:
        text = fh.read()

    region = _article_region(text)
    if region is None:
        raise ValueError("Could not locate the 'Journal articles' section in the page.")
    start, end = region
    head, body, tail = text[:start], text[start:end], text[end:]

    have = {int(m.group(1)) for m in _YEAR_HEADER.finditer(body)}
    want = {int(y) for y in years if y}
    missing = sorted(want - have, reverse=True)
    if not missing:
        return []

    all_years = sorted(have | want, reverse=True)
    # Preserve existing block text verbatim; generate blocks for missing years.
    existing_blocks = _split_blocks(body)
    rebuilt = []
    for year in all_years:
        rebuilt.append(existing_blocks.get(year, _block_for(year)))
    # Leading newline restores the break after the section header line, which
    # the start-of-section regex stops just short of.
    new_body = "\n" + "\n".join(rebuilt) + "\n"

    with open(page_path, "w", encoding="utf-8") as fh:
        fh.write(head + new_body + tail)
    return missing


def _article_region(text: str):
    start_m = _SECTION_START.search(text)
    if not start_m:
        return None
    end_m = _SECTION_END.search(text, start_m.end())
    body_start = start_m.end()
    body_end = end_m.start() if end_m else len(text)
    return body_start, body_end


def _split_blocks(body: str) -> dict:
    """Map year -> verbatim block text for each existing year heading."""
    headers = list(_YEAR_HEADER.finditer(body))
    blocks = {}
    for i, m in enumerate(headers):
        year = int(m.group(1))
        block_start = m.start()
        block_end = headers[i + 1].start() if i + 1 < len(headers) else len(body)
        blocks[year] = body[block_start:block_end].strip("\n")
    return blocks
