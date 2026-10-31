import unittest
from cfb_covers_matchup_shadow import inspect, match_canonical_pair, discover_dated_matchups, reconcile_shadow_moneylines

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

    def test_date_scoped_discovery_excludes_sidebars(self):
        page = """| Oct 31, 12:00<br>/matchup/111 |
| Nov 7, 12:00<br>/matchup/378696 |
| Nov 7, 12:00<br>/matchup/378696 |
| Nov 6, 19:00<br>/matchup/378718 |
| Nov 3, 19:00<br>/matchup/378801 |\n| Nov 4, 19:00<br>/matchup/378802 |\nsidebar /matchup/222
"""
        self.assertEqual([x["matchup_id"] for x in discover_dated_matchups(page)],
                         ["378696", "378718", "378801", "378802"])

    def test_explicit_aliases_not_fuzzy_matching(self):
        baseline = {"rows": [
            {"game_id": "401856741", "away_team": "Georgia", "home_team": "Ole Miss"},
            {"game_id": "401858291", "away_team": "Miami", "home_team": "Notre Dame"}]}
        self.assertEqual(match_canonical_pair(
            {"matchup": "# Georgia vs Mississippi"}, baseline)["game_id"], "401856741")
        self.assertEqual(match_canonical_pair(
            {"matchup": "# Miami (FL) vs Notre Dame"}, baseline)["game_id"], "401858291")
        self.assertIsNone(match_canonical_pair(
            {"matchup": "# Georgia vs Mississippi State"}, baseline)["game_id"])

    def test_reconciliation_only_counts_missing_cbs_moneylines(self):
        result = inspect(SAMPLE, URL, CLOCK)
        match = {"status": "SHADOW_IDENTITY_MATCH_ONLY", "game_id": "401856743"}
        row = {"game_id": "401856743", "branches": {
            "away_ml": {"availability": "DISPLAYED"},
            "home_ml": {"availability": "MISSING"}}}
        reconciled = reconcile_shadow_moneylines(result, match, {"rows": [row]})
        self.assertEqual(reconciled["candidate_branch_names"], ["home_ml"])
        self.assertEqual(reconciled["new_candidate_branches"], 1)
        self.assertFalse(reconciled["decision_authorized"])
        self.assertEqual(reconcile_shadow_moneylines(
            result, {"status": "UNRESOLVED", "game_id": None},
            {"rows": [row]})["new_candidate_branches"], 0)

    def test_repeated_same_side_does_not_qualify_as_pair(self):
        result = inspect(SAMPLE, URL, CLOCK)
        result["displayed_moneyline_rows"] = [
            {"displayed_moneyline": -172}, {"displayed_moneyline": -172}]
        match = {"status": "SHADOW_IDENTITY_MATCH_ONLY", "game_id": "401856743"}
        row = {"game_id": "401856743", "branches": {
            "away_ml": {"availability": "MISSING"},
            "home_ml": {"availability": "MISSING"}}}
        reconciled = reconcile_shadow_moneylines(result, match, {"rows": [row]})
        self.assertEqual(reconciled["status"], "INCOMPLETE_PAIR")
        self.assertEqual(reconciled["new_candidate_branches"], 0)

    def test_fail_closed_identity_and_clock(self):
        with self.assertRaises(ValueError):
            inspect(SAMPLE, "https://example.com/odds", CLOCK)
        with self.assertRaises(ValueError):
            inspect(SAMPLE, URL, "unknown")
        with self.assertRaises(ValueError):
            inspect("No matchup", URL, CLOCK)

if __name__ == "__main__":
    unittest.main()
