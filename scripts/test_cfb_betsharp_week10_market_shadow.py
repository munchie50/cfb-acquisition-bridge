"""Market extractor regression: moneylines are observations, never bets."""
import unittest
from cfb_betsharp_week10_market_shadow import inspect

class TestBetSharpMarket(unittest.TestCase):
    def test_moneyline_only(self):
        header = "# Clemson Tigers at Syracuse Orange odds\n## Game lines\nUpdated 4:51 PM ET\n"
        rows = []
        for market, side, value in (("ml","away","-144<br>Kalshi"),("ml","home","+100<br>Kalshi"),
                                    ("spread","away","-"),("spread","home","-"),
                                    ("total","over","-"),("total","under","-")):
            rows.append(f"| [History](https://betsharp.com/history?m={market}&s={side}) | {value} | {value} |")
        page = header + "\n".join(rows)
        result = inspect(page, "https://betsharp.com/ncaaf/game/2026-11-07-clemson-tigers-at-syracuse-orange")
        self.assertEqual(sum(x["availability"] == "DISPLAYED_SHADOW" for x in result["branches"].values()),2)
        self.assertIsNone(result["branches"]["away_spread"]["price"])
        self.assertFalse(result["decision_authorized"])
        self.assertTrue(result["date_of_update_unverified"])

    def test_unapproved_url_fails(self):
        with self.assertRaises(ValueError):
            inspect("# Example odds", "https://example.org/ncaaf/game/2026-11-07-test")

    def test_missing_update_fails(self):
        with self.assertRaises(ValueError):
            inspect("# Example odds\n## Game lines", "https://betsharp.com/test")

if __name__ == "__main__":
    unittest.main()
