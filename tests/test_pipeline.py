"""Offline tests for the publications updater.

These exercise parsing, formatting, dedup and year-section insertion without
touching the network, using the checked-in efetch fixture and temporary copies
of the bibliography/page. Run with: python -m pytest tests/ (or python tests/test_pipeline.py).
"""

import os
import shutil
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "_tools", "pub_updater"))

import bibstore  # noqa: E402
import fetch_pubmed  # noqa: E402
import pages  # noqa: E402

FIXTURE = os.path.join(os.path.dirname(__file__), "fixtures", "sample_efetch.xml")


class FetchTests(unittest.TestCase):
    def setUp(self):
        with open(FIXTURE, "rb") as fh:
            self.pubs = fetch_pubmed.parse_efetch_xml(fh.read())

    def test_parses_all_records(self):
        self.assertEqual(len(self.pubs), 3)

    def test_preprint_detection(self):
        by_title = {p.title: p for p in self.pubs}
        self.assertTrue(by_title["A connectivity atlas of the marmoset prefrontal cortex"].is_preprint)
        self.assertFalse(by_title["Gradients in brain organization"].is_preprint)

    def test_fields_extracted(self):
        art = next(p for p in self.pubs if p.year == 2026)
        self.assertEqual(art.doi, "10.1038/s41593-026-00001-2")
        self.assertEqual(art.volume, "29")
        self.assertEqual(art.issue, "2")
        self.assertEqual(art.pages, "210-225")
        self.assertEqual(art.first_author_last(), "Margulies")


class FormatTests(unittest.TestCase):
    def test_citekey_uniqueness(self):
        taken = {"Margulies2026"}
        art = next(p for p in _load() if p.year == 2026)
        self.assertEqual(bibstore.make_citekey(art, taken), "Margulies2026a")

    def test_entry_type_by_preprint(self):
        pre = next(p for p in _load() if p.is_preprint)
        art = next(p for p in _load() if p.year == 2026)
        self.assertTrue(bibstore.format_entry(pre, "X").startswith("@misc{"))
        self.assertTrue(bibstore.format_entry(art, "Y").startswith("@article{"))

    def test_fields_alphabetical_and_indented(self):
        art = next(p for p in _load() if p.year == 2026)
        body = bibstore.format_entry(art, "Margulies2026").splitlines()[1:-1]
        keys = [ln.strip().split(" =")[0] for ln in body]
        self.assertEqual(keys, sorted(keys))
        self.assertTrue(all(ln.startswith(" ") for ln in body))


class PageTests(unittest.TestCase):
    def test_inserts_missing_year_in_order(self):
        tmp = tempfile.mkdtemp()
        try:
            page = os.path.join(tmp, "publications.md")
            shutil.copy(os.path.join(ROOT, "research", "publications.md"), page)
            added = pages.ensure_years(page, {2026})
            self.assertEqual(added, [2026])
            with open(page, encoding="utf-8") as fh:
                text = fh.read()
            self.assertIn('##### 2026 <a name="2026"></a>', text)
            # 2026 must come before 2025 (descending order preserved).
            self.assertLess(text.index("name=\"2026\""), text.index("name=\"2025\""))
            # No duplicate header line glued to the section title.
            self.assertNotIn('</a>#####', text)
            # Existing years are untouched (re-running adds nothing).
            self.assertEqual(pages.ensure_years(page, {2025, 2024}), [])
        finally:
            shutil.rmtree(tmp)


def _load():
    with open(FIXTURE, "rb") as fh:
        return fetch_pubmed.parse_efetch_xml(fh.read())


if __name__ == "__main__":
    unittest.main(verbosity=2)
