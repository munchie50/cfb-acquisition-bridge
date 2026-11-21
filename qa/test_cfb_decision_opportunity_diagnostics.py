"""Regression coverage for read-only opportunity diagnostics."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from cfb_decision_opportunity_diagnostics import analyze

def review(rows):
    return {"reports": {"sat": {"rows": rows}}}

class DecisionDiagnosticsTests(unittest.TestCase):
    def test_price_factor_does_not_become_price_only_or_bet(self):
        out = analyze(review([{"game_id": "1", "six_markets": {
            "away_spread": {"state": "PASS", "reason": "Good matchup but price -130 is expensive"}}}]))
        row = out["rows"][0]
        self.assertEqual(row["category"], "PASS_WITH_PRICE_FACTOR_NOT_PRICE_ONLY_PROVEN")
        self.assertFalse(row["bet_authorized"])
        self.assertEqual(out["market_slots"], 6)

    def test_conditional_is_not_actionable(self):
        row = analyze(review([{"game_id": "2", "six_markets": {
            "under": {"state": "CONDITIONAL_PROPOSAL", "reason": "Under if lineup confirmed"}}}]))["rows"][-1]
        self.assertEqual(row["category"], "PROPOSAL_REQUIRES_QUALIFICATION")
        self.assertFalse(row["bet_authorized"])

    def test_missing_market_is_visible_not_pass(self):
        out = analyze(review([{"game_id": "3"}]))
        self.assertEqual(out["market_slot_counts"], {"MARKET_REVIEW_NOT_EXTRACTABLE": 6})

    def test_string_review_supported(self):
        row = analyze(review([{"game_id": "4", "six_market_review": {
            "over": "PASS over 50.5 price is too steep"}}]))["rows"][-2]
        self.assertEqual(row["original_state"], "PASS")
        self.assertTrue(row["price_factor_mentioned"])

    def test_duplicate_identity_quarantined_and_reported(self):
        out = analyze(review([{"game_id": "5"}, {"game_id": "5"}]))
        self.assertEqual(out["game_count"], 1)
        self.assertEqual(out["market_slots"], 6)
        self.assertEqual(out["duplicate_identity_conflicts"], [{"game_id": "5", "additional_section": "sat"}])
        self.assertEqual(out["market_slot_counts"], {"DUPLICATE_IDENTITY_CONFLICT": 6})
        self.assertEqual(out["reviewed_nonconflicted_market_slots"], 0)
        self.assertEqual(out["conflicted_market_slots"], 6)

    def test_friday_and_late_branches_are_extracted(self):
        out = analyze(review([{"game_id": "6", "branches": {
            "home_moneyline": {"state": "PASS", "reason": "Price is expensive"},
            "under": "PASS under 40.5: number too low"}}]))
        self.assertEqual(out["rows"][3]["category"], "PASS_WITH_PRICE_FACTOR_NOT_PRICE_ONLY_PROVEN")
        self.assertEqual(out["rows"][5]["original_state"], "PASS")
        self.assertEqual(out["market_slot_counts"]["MARKET_REVIEW_NOT_EXTRACTABLE"], 4)
        self.assertEqual(out["reviewed_nonconflicted_market_slots"], 2)
        self.assertEqual(sum(out["section_market_slot_counts"]["sat"].values()), 6)

    def test_exclusion_analytical_status_is_not_canonical_pass(self):
        out = analyze(review([{"game_id": "7", "six_markets": {
            "away_spread": {"analytical_status": "PASS_CURRENT_REVIEW", "reason": "No edge"},
            "under": {"analytical_status": "SPECIFIC_RECHECK", "reason": "Need QB evidence"}}}]))
        self.assertEqual(out["rows"][0]["category"], "ANALYTICAL_PASS_NOT_CANONICAL_DECISION")
        self.assertEqual(out["rows"][5]["category"], "ANALYTICAL_RECHECK_NOT_CANONICAL_DECISION")
        self.assertFalse(out["rows"][0]["bet_authorized"])

    def test_quote_unavailable_is_separate_and_not_reviewed(self):
        out = analyze(review([{"game_id": "10", "six_markets": {"over": {
            "analytical_status": "QUOTE_UNAVAILABLE", "reason": "No market quote"}}}]))
        self.assertEqual(out["quote_unavailable_market_slots"], 1)
        self.assertEqual(out["reviewed_nonconflicted_market_slots"], 0)
        self.assertEqual(out["missing_market_slots"], 5)
        self.assertFalse(out["rows"][4]["bet_authorized"])

    def test_empty_market_object_does_not_inflate_coverage(self):
        out = analyze(review([{"game_id": "8", "six_markets": {"over": {}}}]))
        self.assertEqual(out["missing_market_slots"], 6)
        self.assertEqual(out["reviewed_nonconflicted_market_slots"], 0)

    def test_ambiguous_review_shapes_fail_closed(self):
        with self.assertRaises(ValueError):
            analyze(review([{"game_id": "13", "six_markets": {}, "branches": {}}]))

    def test_conflicting_moneyline_aliases_fail_closed(self):
        with self.assertRaises(ValueError):
            analyze(review([{"game_id": "14", "six_markets": {
                "away_moneyline": "PASS price too high", "away_ml": "LEAN price fine"}}]))

    def test_missing_review_shape_is_visible(self):
        out = analyze(review([{"game_id": "15"}]))
        self.assertEqual(out["source_review_shapes"]["15"], "MISSING")
        self.assertEqual(out["missing_market_slots"], 6)

    def test_colon_terminated_string_state(self):
        out = analyze(review([{"game_id": "12", "branches": {"over": "PASS: price insufficient"}}]))
        self.assertEqual(out["rows"][4]["original_state"], "PASS")
        self.assertEqual(out["reviewed_nonconflicted_market_slots"], 1)

    def test_section_without_rows_or_games_fails_closed(self):
        with self.assertRaises(ValueError):
            analyze({"reports": {"sat": {"metadata": "no game list"}}})

    def test_no_games_fails_closed(self):
        with self.assertRaises(ValueError):
            analyze({"reports": {"sat": {"rows": []}}})

    def test_unknown_prefix_statuses_are_not_reviewed(self):
        out = analyze(review([{"game_id": "11", "six_markets": {
            "over": {"state": "PASS_FUTURE_UNVERIFIED"},
            "under": {"analytical_status": "ANALYTICAL_FUTURE_UNVERIFIED"}}}]))
        self.assertEqual(out["unclassified_market_slots"], 2)
        self.assertEqual(out["reviewed_nonconflicted_market_slots"], 0)

    def test_unrecognized_market_state_does_not_inflate_coverage(self):
        out = analyze(review([{"game_id": "9", "six_markets": {"over": {"state": "NOT_A_DECISION", "reason": "unknown"}}}]))
        self.assertEqual(out["unclassified_market_slots"], 1)
        self.assertEqual(out["reviewed_nonconflicted_market_slots"], 0)

    def test_malformed_section_fails_closed(self):
        with self.assertRaises(ValueError):
            analyze({"reports": {"sat": None}})

    def test_malformed_rows_fails_closed(self):
        with self.assertRaises(ValueError):
            analyze({"reports": {"sat": {"rows": "not a list"}}})

    def test_unidentified_game_fails_closed(self):
        with self.assertRaises(ValueError):
            analyze(review([{"six_markets": {"over": "PASS"}}]))

    def test_empty_reports_fails_closed(self):
        with self.assertRaises(ValueError):
            analyze({"reports": {}})

    def test_missing_reports_fails_closed(self):
        with self.assertRaises(ValueError):
            analyze({})

if __name__ == "__main__":
    unittest.main()
