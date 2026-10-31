"""Coverage contract: preserve missing games as actionable acquisition work."""
import unittest
from cfb_week10_fallback_branch_inventory import inventory, BRANCHES

class Week10InventoryCoverageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.board = inventory()

    def test_full_slate_and_branch_reconciliation(self):
        b = self.board
        self.assertEqual(b["games"], 63)
        self.assertEqual(len(b["rows"]), 63)
        self.assertEqual(b["possible_branches"], 378)
        self.assertEqual(sum(b["displayed_by_branch"].values()), b["displayed_branches"])
        self.assertEqual(b["displayed_branches"], 102)
        self.assertEqual(set(b["displayed_by_branch"]), set(BRANCHES))

    def test_missing_games_are_explicit_and_not_passes(self):
        b = self.board
        self.assertEqual(b["unpriced_games"], 46)
        self.assertEqual(len(b["unpriced_game_ids"]), 46)
        self.assertEqual(len(set(b["unpriced_game_ids"])), 46)
        self.assertEqual(b["partially_priced_game_ids"], [])
        self.assertFalse(b["source_coverage_complete"])
        self.assertFalse(b["decision_authorized"])
        self.assertEqual(b["executability"], "UNVERIFIED")
        self.assertEqual(b["consensus"], "UNAVAILABLE")
        by_id = {r["game_id"]: r for r in b["rows"]}
        for game_id in b["unpriced_game_ids"]:
            self.assertIn(game_id, by_id)
            self.assertTrue(all(x["availability"] != "DISPLAYED"
                                for x in by_id[game_id]["branches"].values()))

if __name__ == "__main__":
    unittest.main()
