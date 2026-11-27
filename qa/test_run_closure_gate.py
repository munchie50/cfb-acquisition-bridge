"""QA-only evidence gate. Caller must supply independently verified artifacts."""
import re
import unittest
from dataclasses import replace
from cfb_run_failure_classifier_readonly import Evidence, classify

def classify_receipt(receipt: str, *, run_id: str, closure_text: str | None = None,
                     verified_artifacts: dict | None = None) -> str:
    """Fail closed: text alone never proves persistence or production acceptance."""
    if not re.search(r"(?m)^RUN_PASS(?:\s|[;]|$)", receipt):
        return "NOT_CLAIMED_PASS"
    if not run_id or not closure_text or not verified_artifacts:
        return "ACCEPTANCE_PENDING"
    receipt_identity = re.search(r"(?im)^run_id:\s*(\S+)\s*$", receipt)
    if not receipt_identity or receipt_identity.group(1) != run_id:
        return "ACCEPTANCE_PENDING"
    if not re.search(r"\bRUN_CLOSURE\b", closure_text) or not re.search(r"\bRUN_PASS\b", closure_text):
        return "ACCEPTANCE_PENDING"
    # Require exact, separately labeled identity, not substring occurrence.
    match = re.search(r"(?im)^run_id:\s*(\S+)\s*$", closure_text)
    if not match or match.group(1) != run_id:
        return "ACCEPTANCE_PENDING"
    # A closure mentioning an unresolved proof is never acceptance.
    if re.search(r"(?i)\b(?:pending|unverified|not read back|not verified|missing|failed)\b", closure_text):
        return "ACCEPTANCE_PENDING"
    # Evidence must come from caller's independent fetch/readback, not receipt assertions.
    if not all(verified_artifacts.get(k) is True for k in ("canonical", "terminal_candidate", "closure")):
        return "ACCEPTANCE_PENDING"
    if not re.search(r"(?i)\bindependent(?:ly)?\s+read\s*back\b", closure_text):
        return "ACCEPTANCE_PENDING"
    return "EVIDENCE_GATE_PASSED_NOT_PRODUCTION_ACCEPTED"

def classify_legacy_closure(closure_text: str, *, independently_verified_blobs: dict[str, str]) -> str:
    """Historical compatibility check; only independently fetched exact blobs count."""
    if not re.search(r"(?m)^TERMINAL_STATE:\s*RUN_PASS\s*$", closure_text):
        return "ACCEPTANCE_PENDING"
    if re.search(r"(?i)\b(?:pending|unverified|missing|failed)\b", closure_text):
        return "ACCEPTANCE_PENDING"
    if "Independent post-write readback completed" not in closure_text:
        return "ACCEPTANCE_PENDING"
    proofs = re.findall(r"(?m)^-\s+(\S+)\s+blob\s+([0-9a-f]{40})\s+[—-]\s+PASS\s*$", closure_text)
    if not proofs or len(proofs) != len(set(name for name, _ in proofs)):
        return "ACCEPTANCE_PENDING"
    if set(independently_verified_blobs) != {name for name, _ in proofs}:
        return "ACCEPTANCE_PENDING"
    if not all(independently_verified_blobs.get(name) == digest for name, digest in proofs):
        return "ACCEPTANCE_PENDING"
    return "HISTORICAL_EVIDENCE_MATCH_NOT_PRODUCTION_ACCEPTED"

class ClosureGateTests(unittest.TestCase):
    def setUp(self):
        self.good = "RUN_CLOSURE\nrun_id: 20261031T120000Z\nRUN_PASS\nindependently read back"
        self.artifacts = {"canonical": True, "terminal_candidate": True, "closure": True}

    def check(self, closure, artifacts=None, run_id="20261031T120000Z"):
        return classify_receipt("RUN_PASS\nrun_id: " + run_id, run_id=run_id, closure_text=closure,
                                verified_artifacts=self.artifacts if artifacts is None else artifacts)

    def test_historical_false_pass(self):
        self.assertEqual(classify_receipt("RUN_PASS; Sunday Early Board pending; terminal receipt readback pending",
                                          run_id="old"), "ACCEPTANCE_PENDING")

    def test_start_only(self):
        self.assertEqual(classify_receipt("RUN_STARTED", run_id="x"), "NOT_CLAIMED_PASS")

    def test_no_closure(self):
        self.assertEqual(self.check(None), "ACCEPTANCE_PENDING")

    def test_pending_readback(self):
        self.assertEqual(self.check(self.good + "\nterminal receipt readback pending"), "ACCEPTANCE_PENDING")

    def test_wrong_run(self):
        self.assertEqual(self.check(self.good, run_id="different"), "ACCEPTANCE_PENDING")

    def test_missing_artifact(self):
        a = dict(self.artifacts); a["terminal_candidate"] = False
        self.assertEqual(self.check(self.good, artifacts=a), "ACCEPTANCE_PENDING")

    def test_no_independent_readback(self):
        self.assertEqual(self.check(self.good.replace("independently read back", "readback claimed")),
                         "ACCEPTANCE_PENDING")

    def test_positive_still_requires_production_reconciliation(self):
        self.assertEqual(self.check(self.good), "EVIDENCE_GATE_PASSED_NOT_PRODUCTION_ACCEPTED")

    def test_unrelated_receipt_rejected(self):
        self.assertEqual(classify_receipt("RUN_PASS\nrun_id: unrelated", run_id="20261031T120000Z",
                         closure_text=self.good, verified_artifacts=self.artifacts), "ACCEPTANCE_PENDING")

    def test_real_legacy_closure_requires_separate_compatibility_adapter(self):
        legacy = ("# CFB Run Closure — 2026-09-29 20:20 CT — MANUAL MARKET MONITOR RESET\n"
                  "TERMINAL_STATE: RUN_PASS\n"
                  "Independent post-write readback completed after all run artifacts were persisted.\n"
                  "Readback proof: CFB_MARKET_MONITOR_STATE.md blob f0e56a83cf394e0dd9209961b457eb3eeea2647e — PASS")
        # A genuine older closure must not be silently misclassified as conforming
        # to the newer run_id schema. Historical compatibility needs explicit
        # artifact-by-artifact verification and its own governed adapter.
        self.assertEqual(classify_receipt("RUN_PASS", run_id="2026-09-29",
                         closure_text=legacy, verified_artifacts=self.artifacts),
                         "ACCEPTANCE_PENDING")

    def test_legacy_blob_proof_binding(self):
        closure = ("TERMINAL_STATE: RUN_PASS\n"
                   "Independent post-write readback completed after all run artifacts were persisted.\n"
                   "- CFB_MARKET_MONITOR_STATE.md blob f0e56a83cf394e0dd9209961b457eb3eeea2647e — PASS")
        verified = {"CFB_MARKET_MONITOR_STATE.md": "f0e56a83cf394e0dd9209961b457eb3eeea2647e"}
        self.assertEqual(classify_legacy_closure(closure, independently_verified_blobs=verified),
                         "HISTORICAL_EVIDENCE_MATCH_NOT_PRODUCTION_ACCEPTED")
        self.assertEqual(classify_legacy_closure(closure, independently_verified_blobs={
            "CFB_MARKET_MONITOR_STATE.md": "0" * 40}), "ACCEPTANCE_PENDING")

    def test_legacy_requires_all_declared_artifacts(self):
        closure = ("TERMINAL_STATE: RUN_PASS\n"
                   "Independent post-write readback completed after all run artifacts were persisted.\n"
                   "- A.md blob " + "a" * 40 + " — PASS\n"
                   "- B.md blob " + "b" * 40 + " — PASS")
        self.assertEqual(classify_legacy_closure(closure, independently_verified_blobs={
            "A.md": "a" * 40}), "ACCEPTANCE_PENDING")
        self.assertEqual(classify_legacy_closure(closure, independently_verified_blobs={
            "A.md": "a" * 40, "B.md": "0" * 40}), "ACCEPTANCE_PENDING")

    def test_classifier_integration_requires_gate_and_operational_evidence(self):
        baseline = Evidence(producer_started=True, canonical_write_attempted=True,
                            canonical_write_accepted=True, source_complete=True,
                            publication_present=True, independent_publication_verified=True)
        self.assertEqual(classify(baseline), "PUBLISHED_UNVERIFIED")
        gated = self.check(self.good) == "EVIDENCE_GATE_PASSED_NOT_PRODUCTION_ACCEPTED"
        self.assertTrue(gated)
        self.assertEqual(classify(replace(baseline, terminal_closure_verified=gated)), "RUN_PASS")
        self.assertEqual(classify(replace(baseline, source_complete=False,
                                          terminal_closure_verified=gated)), "PARTIAL_SOURCE")
        self.assertEqual(classify(replace(baseline, independent_publication_verified=False,
                                          terminal_closure_verified=gated)), "PUBLISHED_UNVERIFIED")
        self.assertEqual(classify(replace(baseline, terminal_closure_verified=False)),
                         "PUBLISHED_UNVERIFIED")

    def test_prose_mention_of_run_pass_rejected(self):
        self.assertEqual(classify_receipt("Historical RUN_PASS claim was invalid", run_id="x"),
                         "NOT_CLAIMED_PASS")

if __name__ == "__main__":
    unittest.main()
