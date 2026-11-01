"""Regression checks for CFB terminal closure evidence. QA only; no production mutation."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
RECEIPTS = ROOT / "evidence" / "run_receipts"

def classify_receipt(text: str, *, closure_text: str | None = None, surfaces_read_back: bool = False) -> str:
    """Conservative evidence gate: never infer PASS from a receipt's own claim."""
    if not re.search(r"\bRUN_PASS\b", text):
        return "NOT_CLAIMED_PASS"
    if not surfaces_read_back:
        return "ACCEPTANCE_PENDING"
    if closure_text is None:
        return "ACCEPTANCE_PENDING"
    required = ("RUN_CLOSURE", "RUN_PASS", "readback")
    if not all(token.lower() in closure_text.lower() for token in required):
        return "ACCEPTANCE_PENDING"
    return "PASS_EVIDENCE_PRESENT"

class ClosureGateTests(unittest.TestCase):
    def test_historical_false_pass_is_not_accepted(self):
        receipt = "RUN_PASS; Sunday Early Board pending; terminal receipt readback pending"
        self.assertEqual(classify_receipt(receipt), "ACCEPTANCE_PENDING")

    def test_startup_marker_is_not_completion(self):
        self.assertEqual(classify_receipt("RUN_STARTED"), "NOT_CLAIMED_PASS")

    def test_pass_claim_without_independent_closure_is_not_accepted(self):
        self.assertEqual(classify_receipt("RUN_PASS", surfaces_read_back=True), "ACCEPTANCE_PENDING")

    def test_incomplete_closure_is_not_accepted(self):
        self.assertEqual(classify_receipt("RUN_PASS", closure_text="RUN_CLOSURE RUN_PASS", surfaces_read_back=True), "ACCEPTANCE_PENDING")

    def test_minimal_positive_fixture(self):
        self.assertEqual(classify_receipt("RUN_PASS", closure_text="RUN_CLOSURE RUN_PASS independent readback", surfaces_read_back=True), "PASS_EVIDENCE_PRESENT")

if __name__ == "__main__":
    unittest.main()
