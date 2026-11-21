#!/usr/bin/env python3
"""Read-only QA of ACTUAL canonical index/ledger/sheet bytes, not a virtual candidate.

Input files must be staged from one identified repository snapshot and verified
against the corresponding remote Git blob IDs before relying on this result.
This QA does not certify live markets, bets, freshness, or scheduled execution.
"""
import argparse
import json
import sys
from pathlib import Path


def run(root: Path, index_path: Path, ledger_path: Path, as_of: str):
    sys.path.insert(0, str(root / "scripts"))
    from cfb_recovery_navigation_reader import read
    from cfb_hot_sheet_current_decision_binding_gate import (
        publication, blob, LEDGER, CURRENT_ROLE,
    )
    index = index_path.read_bytes().decode("utf-8")
    ledger = ledger_path.read_bytes().decode("utf-8")
    nav = read(index, as_of)
    pointers = nav["frontier"]["pointers"]
    current = [p for p in pointers if p["purpose"].startswith(CURRENT_ROLE)]
    canonical = [p for p in pointers if p["path"] == LEDGER]
    if len(current) != 1 or len(canonical) != 1:
        raise ValueError("exactly one current sheet and canonical ledger pointer required")
    if canonical[0]["blob"] != blob(ledger):
        raise ValueError("actual canonical ledger bytes differ from index pointer")
    path = current[0]["path"]
    def loader(relative_path):
        if relative_path != path:
            raise ValueError("unexpected current publication path")
        resolved = (root / relative_path).resolve()
        if not resolved.is_relative_to(root.resolve()):
            raise ValueError("publication path escapes repository")
        return resolved.read_bytes().decode("utf-8")
    result = publication(index, ledger, loader, as_of)
    if result["sheet_blob"] != current[0]["blob"]:
        raise RuntimeError("actual current sheet blob mismatch")
    print(json.dumps({
        "status": "QA_ACTUAL_CANONICAL_SELECTOR_BINDING_ONLY_NOT_PRODUCTION",
        "index_blob": nav["index_blob"],
        "ledger_blob": blob(ledger),
        "sheet_path": result["sheet_path"],
        "sheet_blob": result["sheet_blob"],
        "verdict": result["verdict"],
        "limitations": [
            "Input staging and remote repository snapshot identity must be verified separately",
            "No market/source freshness, offer qualification, scheduled-run, or betting acceptance",
        ],
    }, indent=2))


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo", required=True, type=Path)
    ap.add_argument("--index", required=True, type=Path)
    ap.add_argument("--ledger", required=True, type=Path)
    ap.add_argument("--as-of", required=True)
    a = ap.parse_args()
    run(a.repo.resolve(), a.index.resolve(), a.ledger.resolve(), a.as_of)
