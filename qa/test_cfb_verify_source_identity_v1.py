#!/usr/bin/env python3
"""Negative-path QA for identity verifier; does not certify real market data."""
import json
import tempfile
from pathlib import Path
from cfb_verify_source_identity_v1 import git_blob, verify

def check(condition, message):
    if not condition:
        raise RuntimeError("QA_FAILURE: " + message)

AS_OF = "2026-11-20T22:00:00Z"
with tempfile.TemporaryDirectory() as td:
    root = Path(td)
    data = root / "quote.txt"
    data.write_bytes(b"synthetic quote")
    row = {
        "event_id": "synthetic1", "observed_at": "2026-11-20T18:00:00Z",
        "decision_deadline": "2026-11-20T19:00:00Z", "status": "PASS",
        "source_kind": "CERTIFIED_MARKET", "market": "spread", "side": "home",
        "book": "SYNTHETIC_BOOK", "price_unit": "points", "quote_type": "spread",
        "price": -3.5, "source_path": "quote.txt",
        "source_blob": git_blob(data.read_bytes()),
    }
    inp = root / "input.jsonl"
    inp.write_text(json.dumps(row) + "\n")
    ok = verify(root, inp, AS_OF)
    check(ok["status"] == "UNVERIFIED_SOURCE_ATTESTATION", "identity match cannot certify")
    check(not ok["eligible_for_production_learning"], "must not learn")
    check(ok["market_rows_examined"] == 1, "market row count")
    data.write_bytes(b"tampered")
    check(verify(root, inp, AS_OF)["status"] == "INCOMPLETE", "tampering must fail")
    inp.write_text("")
    check(verify(root, inp, AS_OF)["status"] == "INCOMPLETE", "empty must fail")
    decision = dict(row)
    decision["source_kind"] = "ENGINE_DECISION"
    decision["decision_at"] = "2026-11-20T18:30:00Z"
    inp.write_text(json.dumps(decision) + "\n")
    no_market = verify(root, inp, AS_OF)
    check(no_market["status"] == "INCOMPLETE", "no market records must fail")
    check("NO_MARKET_ROWS_TO_VERIFY" in no_market["missing_or_invalid"], "missing reason")
print("QA_PASS: identity verifier negative paths")
