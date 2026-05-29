# Publications updater

Automatically keeps the lab's publication list current. It queries PubMed,
appends any newly-found publications to the jekyll-scholar bibliography, and
makes sure the publications page has a section for every year present — then
opens a pull request for review.

## How it fits the existing site

The site renders publications with **jekyll-scholar**, so there is no
hand-written HTML per paper:

- `_bibliography/publications.bib` is the **source of truth**. The updater only
  ever *appends* to it; existing entries, hand edits and section comments are
  left untouched.
- `research/publications.md` lists journal articles under one `##### YYYY`
  heading per year. When a new year appears, the updater inserts the missing
  heading + `{% bibliography ... year=YYYY %}` block in descending order.
- Per-entry links (PDF, Link/DOI, …) come from `.bib` fields, formatted by
  `_layouts/bib_small.html`. New entries get `doi`/`link`/`url`, and a `pdf`
  field only when an open-access PDF was successfully downloaded.

## Files

| File | Purpose |
|------|---------|
| `config.yml` | PubMed query, paths, email/PDF settings |
| `fetch_pubmed.py` | Query + parse PubMed via Biopython Entrez |
| `bibstore.py` | Read for dedup; format and append entries in the house style |
| `pages.py` | Insert missing `##### YYYY` sections into the page |
| `pdf_fetch.py` | Best-effort open-access PDF download (bioRxiv/medRxiv, Unpaywall) |
| `update.py` | Orchestrator / CLI |

## Running

The PubMed query needs open internet, so it runs on a **GitHub Actions
runner**, not in restricted sandboxes. Trigger it from the **Actions tab →
"Update publications" → "Run workflow"**, or wait for the monthly schedule. It
opens/updates the `auto/pub-updates` PR against `staging`.

### Local / offline

```bash
pip install -r _tools/pub_updater/requirements.txt

# Live run (needs network to NCBI):
python _tools/pub_updater/update.py --repo-root .

# Offline, against a saved efetch XML fixture (no network):
python _tools/pub_updater/update.py --repo-root . \
    --from-xml tests/fixtures/sample_efetch.xml --no-pdf

# Tests:
python -m unittest discover -s tests
```

## Dedup & safety

- A publication is skipped if its DOI, PMID, or normalized title already
  appears in the bibliography, so re-runs are idempotent.
- The query in `config.yml` is passed to PubMed verbatim; edit it there to
  refine what counts as "ours".
- Papers with no open-access PDF are added without a `pdf` field and listed in
  the PR body under "PDFs needed" for a manual upload to `downloads/pubs/`.
