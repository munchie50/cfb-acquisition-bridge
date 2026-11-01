"""Regression coverage for fail-closed Week10 market provenance gate."""
import unittest
from cfb_week10_market_qualification_gate import qualify, BRANCHES


def inventory():
    rows = []
    for i in range(63):
        rows.append({"game_id": str(401800000 + i), "branches": {
            b: {"status": "DISPLAYED_UNQUALIFIED", "price": -110,
                "line": None if b.endswith("_ml") else 7.5} for b in BRANCHES}})
    return {"schema": "CFB_WEEK10_R91_CBS_DIRECTED_SIX_BRANCH_SOURCE_INVENTORY", "rows": rows}


class MarketGateTest(unittest.TestCase):
    def test_unverified_all_wait(self):
        result = qualify(inventory())
        self.assertEqual(result["counts"], {"branches": 378, "qualified": 0, "wait": 378})
        self.assertFalse(any(x["decision_authorized"] for x in result["rows"]))

    def test_exact_offer_qualifies_market_only(self):
        gid = str(401800000)
        quote = {gid: {"away_spread": {"operator": "Book A", "offer_updated_at_utc": "2026-11-02T15:00:00Z",
                                         "venue": "Verified sportsbook", "venue_executable": True, "line": 7.5, "price": -110}}}
        result = qualify(inventory(), quote)
        self.assertEqual(result["counts"], {"branches": 378, "qualified": 1, "wait": 377})
        self.assertFalse(result["rows"][0]["decision_authorized"])

    def test_mismatched_line_and_price_wait(self):
        gid = str(401800000)
        base = {"operator": "Book A", "offer_updated_at_utc": "2026-11-02T15:00:00Z",
                "venue": "Verified sportsbook", "venue_executable": True, "line": 8.5, "price": -110}
        self.assertEqual(qualify(inventory(), {gid: {"away_spread": base}})["counts"]["qualified"], 0)
        base["line"] = 7.5
        base["price"] = -115
        self.assertEqual(qualify(inventory(), {gid: {"away_spread": base}})["counts"]["qualified"], 0)

    def test_unavailable_branch_stays_wait(self):
        source = inventory()
        source["rows"][0]["branches"]["away_spread"]["status"] = "UNAVAILABLE"
        proof = {"operator": "Book A", "offer_updated_at_utc": "2026-11-02T15:00:00Z",
                 "venue": "Verified sportsbook", "venue_executable": True, "line": 7.5, "price": -110}
        self.assertEqual(qualify(source, {str(401800000): {"away_spread": proof}})["counts"]["qualified"], 0)

    def test_duplicate_games_rejected(self):
        source = inventory()
        source["rows"][1]["game_id"] = source["rows"][0]["game_id"]
        with self.assertRaises(ValueError):
            qualify(source)

    def test_missing_branch_rejected(self):
        source = inventory()
        del source["rows"][0]["branches"]["under_total"]
        with self.assertRaises(ValueError):
            qualify(source)


if __name__ == "__main__":
    unittest.main()
