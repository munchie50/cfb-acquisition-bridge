"""Bounded source-discovery tests: no source-only game can authorize a wager."""
import unittest
from cfb_betsharp_week10_shadow import discover

class TestBetSharpShadow(unittest.TestCase):
    def test_dedup_and_fail_closed(self):
        page = ("https://betsharp.com/ncaaf/game/2026-11-07-clemson-tigers-at-syracuse-orange\n" * 2
                + "https://betsharp.com/ncaaf/game/2026-11-06-vt-at-smu\n")
        result = discover(page, [{"game_id": "401", "away_team": "Clemson",
                                  "home_team": "Syracuse"}])
        self.assertEqual(result["source_urls_count"], 1)
        self.assertEqual(result["strict_name_candidate_count"], 0)
        self.assertEqual(result["mascot_prefix_candidate_count"], 1)
        self.assertFalse(result["mascot_prefix_candidates"][0]["identity_verified"])
        self.assertFalse(result["canonical_join_authorized"])
        self.assertFalse(result["prices_qualified"])
        self.assertFalse(result["decision_authorized"])
        self.assertFalse(result["unpriced_targets"][0]["identity_verified"])

    def test_exact_full_name_candidate_still_unverified(self):
        page = "https://betsharp.com/ncaaf/game/2026-11-07-clemson-at-syracuse"
        result = discover(page, [{"game_id": "401", "away_team": "Clemson", "home_team": "Syracuse"}])
        self.assertEqual(result["strict_name_candidate_count"], 1)
        self.assertFalse(result["strict_name_candidates"][0]["identity_verified"])
        self.assertFalse(result["canonical_join_authorized"])

    def test_day_scope(self):
        with self.assertRaises(ValueError):
            discover("", [], "2026-11-08")

if __name__ == "__main__":
    unittest.main()
