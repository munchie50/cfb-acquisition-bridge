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

    def test_missing_reports_fails_closed(self):
        with self.assertRaises(ValueError):
            analyze({})

if __name__ == "__main__":
    unittest.main()
