"""Read-only Week10 observed-census regression, including persisted capture."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from cfb_week10_source_census_readonly import census, URL


class CensusTests(unittest.TestCase):
    def setUp(self):
        self.capture = (ROOT / "evidence/operational/CFB_CBS_WEEK10_LIVE_MARKDOWN_CAPTURE_20261031.md").read_text()

    def test_real_persisted_capture_census(self):
        r = census(self.capture)
        self.assertEqual(r["observed_games"], 63)
        self.assertEqual(r["observed_team_rows"], 126)
        self.assertFalse(r["independent_identity_baseline_verified"])
        self.assertFalse(r["publication_authorized"])
        self.assertTrue(all(x["game_id"] is None for x in r["games"]))

    def test_rejects_partial_game(self):
        rows = self.capture.splitlines()
        team = next(i for i, x in enumerate(rows) if x.startswith("| [![team logo]"))
        rows.pop(team)
        with self.assertRaises(ValueError):
            census("\n".join(rows))

    def test_rejects_wrong_source_and_missing_heading(self):
        with self.assertRaises(ValueError):
            census(self.capture, source_url=URL.replace("week-10", "week-9"))
        with self.assertRaises(ValueError):
            census(self.capture.replace("# Odds - Week 10", "# Odds - Week 9"))


if __name__ == "__main__":
    unittest.main()
