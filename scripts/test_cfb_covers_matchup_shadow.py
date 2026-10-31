import unittest
from cfb_covers_matchup_shadow import inspect

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

    def test_fail_closed_identity_and_clock(self):
        with self.assertRaises(ValueError):
            inspect(SAMPLE, "https://example.com/odds", CLOCK)
        with self.assertRaises(ValueError):
            inspect(SAMPLE, URL, "unknown")
        with self.assertRaises(ValueError):
            inspect("No matchup", URL, CLOCK)

if __name__ == "__main__":
    unittest.main()
