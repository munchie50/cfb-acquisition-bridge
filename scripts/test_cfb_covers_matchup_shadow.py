import unittest
from cfb_covers_matchup_shadow import inspect, match_canonical_pair

URL = "https://www.covers.com/sport/football/ncaaf/matchup/378696/odds"
CLOCK = "2026-10-31T19:00:00Z"
SAMPLE = """Texas vs Missouri Odds
| Texas | - | - | -172![FanDuel logo](https://img.covers.com/betting/sportsbooks/818/fanduel_icon.svg) |
| Missouri | - | - | +142![FanDuel logo](https://img.covers.com/betting/sportsbooks/818/fanduel_icon.svg) |
"""

class CoversShadowTest(unittest.TestCase):
    def test_extract_without_authorizing(self):
        r = inspect(SAMPLE, URL, CLOCK)
        self.assertEqual([x["displayed_moneyline"] for x in r["displayed_moneyline_rows"]], [-172, 142])
        self.assertFalse(r["decision_authorized"])
        self.assertFalse(r["executable_offer_verified"])
        self.assertIsNone(r["independent_price_clock"])

    def test_repeated_summary_rows_are_not_new_offers(self):
        result = inspect(SAMPLE + SAMPLE, URL, CLOCK)
        self.assertEqual(len(result["displayed_moneyline_rows"]), 2)
        self.assertEqual([x["displayed_moneyline"] for x in result["displayed_moneyline_rows"]], [-172, 142])

    def test_exact_canonical_join_and_ambiguity_rejection(self):
        result = inspect(SAMPLE, URL, CLOCK)
        baseline = {"rows": [{"game_id": "401856743", "away_team": "Texas",
                              "home_team": "Missouri"}]}
        matched = match_canonical_pair(result, baseline)
        self.assertEqual(matched["game_id"], "401856743")
        self.assertFalse(matched["decision_authorized"])
        self.assertFalse(matched["kickoff_independently_verified"])
        self.assertIsNone(match_canonical_pair(result, {"rows": []})["game_id"])
        self.assertIsNone(match_canonical_pair(result, {"rows": baseline["rows"] * 2})["game_id"])

    def test_fail_closed_identity_and_clock(self):
        with self.assertRaises(ValueError):
            inspect(SAMPLE, "https://example.com/odds", CLOCK)
        with self.assertRaises(ValueError):
            inspect(SAMPLE, URL, "unknown")
        with self.assertRaises(ValueError):
            inspect("No matchup", URL, CLOCK)

if __name__ == "__main__":
    unittest.main()
