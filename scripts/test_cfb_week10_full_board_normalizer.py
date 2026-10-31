"""Bounded Week 10 full-board CBS fallback normalization regression; never betting acceptance."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from cfb_cbs_full_board_normalizer import normalize, WEEK10_URL

CBS = ROOT / "evidence/operational/CFB_CBS_WEEK10_LIVE_MARKDOWN_CAPTURE_20261031.md"
LINEAGE = ROOT / "evidence/operational/CFB_WEEK10_CANDIDATE_CANONICAL_IDENTITY_BASELINE_20261031.json"
RECOVERED_BY = "2026-10-31T20:00:00Z"


class Week10FallbackTest(unittest.TestCase):
    def setUp(self):
        self.markdown = CBS.read_text()
        self.lineage = LINEAGE.read_text()

    def run_capture(self, **kw):
        return normalize(self.markdown, self.lineage, RECOVERED_BY,
                         source_url=WEEK10_URL, profile="WEEK10", **kw)

    def test_complete_63_game_126_team_row_capture(self):
        result = self.run_capture()
        self.assertEqual(result["coverage"]["matched_games"], 63)
        self.assertEqual(result["coverage"]["source_team_rows"], 126)
        self.assertEqual(result["coverage"]["future_games"], 63)
        self.assertEqual(result["coverage"]["missing_game_ids"], [])
        self.assertEqual(len({g["game_id"] for g in result["games"]}), 63)
        self.assertEqual(result["qualification"], "UNIDENTIFIED_FIELD_LEVEL_MIXED_BOOK_FALLBACK_ONLY")
        self.assertEqual(result["executability"], "UNVERIFIED")
        self.assertEqual(result["consensus"], "CONSENSUS_UNAVAILABLE")
        self.assertTrue(all(g["temporal_status"] == "FUTURE_AT_CAPTURE" for g in result["games"]))
        self.assertTrue(all(len(g["team_offers"]) == 2 for g in result["games"]))

    def test_hawaii_is_pinned_to_identity_baseline(self):
        result = self.run_capture()
        row = next(g for g in result["games"] if g["game_id"] == "401864532")
        self.assertEqual((row["away_team"], row["home_team"]), ("Hawaii", "UTEP"))

    def test_reject_modified_lineage(self):
        modified = json.loads(self.lineage)
        modified["rows"][0]["game_id"] = "NOT_ACCEPTED"
        with self.assertRaisesRegex(ValueError, "unqualified original identity baseline"):
            normalize(self.markdown, json.dumps(modified), RECOVERED_BY,
                      source_url=WEEK10_URL, profile="WEEK10")

    def test_reject_reversed_pair(self):
        altered = self.markdown.replace("[OHIO](https://www.cbssports.com/college-football/teams/OHIO/ohio-bobcats/)[Ohio]",
                                        "[OHIO](https://www.cbssports.com/college-football/teams/OHIO/ohio-bobcats/)[Akron]", 1)
        with self.assertRaises(ValueError):
            normalize(altered, self.lineage, RECOVERED_BY,
                      source_url=WEEK10_URL, profile="WEEK10")


if __name__ == "__main__":
    unittest.main()
