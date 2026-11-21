"""Read-only data integrity gate regression tests."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from cfb_data_integrity_gate import audit

def review(games):
    return {"reports": {"sat": {"rows": games}}}

def game(gid, state="PASS"):
    return {"game_id": gid, "six_markets": {m: {"state": state} for m in
        ("away_spread", "home_spread", "away_moneyline", "home_moneyline", "over", "under")}}

class DataIntegrityGateTests(unittest.TestCase):
    def test_clean_review_passes(self):
        self.assertEqual(audit(review([game("1")]))["status"], "PASS")

    def test_duplicate_fails(self):
        result = audit(review([game("1"), game("1")]))
        self.assertEqual(result["status"], "FAIL")
        self.assertEqual(result["finding_code_counts"]["DUPLICATE_GAME_ID"], 1)

    def test_quote_unavailable_warns(self):
        result = audit(review([game("1", "QUOTE_UNAVAILABLE")]))
        self.assertEqual(result["status"], "WARN")
        self.assertEqual(result["finding_code_counts"]["QUOTE_UNAVAILABLE"], 6)

    def test_missing_markets_warns(self):
        result = audit(review([{"game_id": "1", "six_markets": {}}]))
        self.assertEqual(result["finding_code_counts"]["MARKET_MISSING"], 6)

    def test_status_conflict_fails(self):
        g = game("1")
        g["six_markets"]["over"]["analytical_status"] = "LEAN"
        self.assertEqual(audit(review([g]))["status"], "FAIL")

    def test_source_ambiguity_fails(self):
        g = game("1")
        g["branches"] = {}
        self.assertEqual(audit(review([g]))["status"], "FAIL")

    def test_unknown_state_warns(self):
        result = audit(review([game("1", "PASS_UNREVIEWED")]))
        self.assertEqual(result["finding_code_counts"]["STATUS_UNRECOGNIZED"], 6)

    def test_empty_reports_fails(self):
        self.assertEqual(audit({"reports": {}})["status"], "FAIL")

if __name__ == "__main__":
    unittest.main()
