#!/usr/bin/env python3
"""Update publications: query PubMed -> append new entries -> sync year sections.

Typical CI usage (needs open network for the PubMed query):

    python _tools/pub_updater/update.py --repo-root .

Offline development (no NCBI access), using a saved efetch XML fixture:

    python _tools/pub_updater/update.py --from-xml tests/fixtures/sample_efetch.xml

Skip PDF downloads (e.g. for a quick metadata-only run):

    python _tools/pub_updater/update.py --no-pdf

A machine-readable summary of what changed is written with --summary, which the
GitHub Action turns into the body of the pull request.
"""

from __future__ import annotations

import argparse
import os
import sys

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import bibstore
import pages


def load_config(path: str) -> dict:
    with open(path, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Update the publications bibliography.")
    parser.add_argument("--config", default=os.path.join(os.path.dirname(__file__), "config.yml"))
    parser.add_argument("--repo-root", default=os.getcwd())
    parser.add_argument("--from-xml", metavar="FILE", help="Parse saved efetch XML instead of querying NCBI.")
    parser.add_argument("--no-pdf", action="store_true", help="Do not attempt PDF downloads.")
    parser.add_argument("--summary", metavar="FILE", help="Write a Markdown change summary here.")
    args = parser.parse_args(argv)

    cfg = load_config(args.config)
    root = args.repo_root
    bib_path = os.path.join(root, cfg["paths"]["bib"])
    page_path = os.path.join(root, cfg["paths"]["page"])
    pdf_dir = os.path.join(root, cfg["paths"]["pdf_dir"])

    # 1. Gather candidate publications.
    candidates = _gather(args, cfg)
    print(f"Retrieved {len(candidates)} candidate record(s).")

    # 2. Drop ones already present (by DOI / PMID / title).
    identities, citekeys = bibstore.load_identities(bib_path)
    new_pubs = [p for p in candidates if p.identity() not in identities]
    # Guard against duplicates within this same batch.
    seen, deduped = set(), []
    for p in new_pubs:
        if p.identity() not in seen:
            seen.add(p.identity())
            deduped.append(p)
    new_pubs = deduped
    print(f"{len(new_pubs)} new publication(s) after dedup.")

    # 3. Format entries, downloading OA PDFs where possible.
    pdf_enabled = cfg.get("pdf", {}).get("enabled", False) and not args.no_pdf
    added, needs_pdf, blocks = [], [], []
    for pub in sorted(new_pubs, key=lambda p: (p.year or 0, p.first_author_last())):
        key = bibstore.make_citekey(pub, citekeys)
        pdf_rel = ""
        if pdf_enabled and pub.doi:
            import pdf_fetch

            dest = os.path.join(pdf_dir, f"{key}.pdf")
            if pdf_fetch.fetch_pdf(pub.doi, dest, cfg["pdf"]["unpaywall_email"]):
                pdf_rel = f"../downloads/pubs/{key}.pdf"
                print(f"  PDF saved: {key}.pdf")
        if not pdf_rel:
            needs_pdf.append((key, pub))
        blocks.append(bibstore.format_entry(pub, key, pdf_rel))
        added.append((key, pub))

    # 4. Persist: append entries, then ensure the page has the right years.
    bibstore.append_entries(bib_path, blocks)
    article_years = {p.year for k, p in added if not p.is_preprint and p.year}
    years_added = pages.ensure_years(page_path, article_years) if article_years else []

    # 5. Report.
    print(f"Appended {len(added)} entry(ies); added year section(s): {years_added or 'none'}")
    if args.summary:
        _write_summary(args.summary, added, needs_pdf, years_added)
    return 0


def _gather(args, cfg):
    if args.from_xml:
        import fetch_pubmed

        with open(args.from_xml, "rb") as fh:
            return fetch_pubmed.parse_efetch_xml(fh.read())

    import fetch_pubmed

    ent, q = cfg.get("entrez", {}), cfg.get("query", {})
    fetch_pubmed.configure(
        email=os.environ.get("NCBI_EMAIL", ent.get("email", "")),
        tool=ent.get("tool", "neuroconn-pub-updater"),
        api_key=os.environ.get("NCBI_API_KEY", ent.get("api_key", "")),
    )
    pmids = fetch_pubmed.search_pmids(q["raw_query"], retmax=int(q.get("retmax", 1000)))
    print(f"PubMed query matched {len(pmids)} PMID(s).")
    return fetch_pubmed.fetch_records(pmids)


def _write_summary(path, added, needs_pdf, years_added):
    lines = [f"## Publications update\n", f"Added **{len(added)}** new publication(s).\n"]
    if years_added:
        lines.append(f"New year section(s) on the page: {', '.join(map(str, years_added))}\n")
    if added:
        lines.append("### New entries")
        for key, pub in added:
            kind = "preprint" if pub.is_preprint else "article"
            doi = f" — doi:{pub.doi}" if pub.doi else ""
            lines.append(f"- `{key}` ({pub.year}, {kind}): {pub.title}{doi}")
        lines.append("")
    if needs_pdf:
        lines.append("### PDFs needed (no open-access copy found)")
        for key, _ in needs_pdf:
            lines.append(f"- [ ] `downloads/pubs/{key}.pdf`")
        lines.append("")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))


if __name__ == "__main__":
    raise SystemExit(main())
