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


def run(root: Path, index_path: Path, ledger_path: Path, as_of: str, expected_index: str, expected_ledger: str, expected_sheet: str):
    sys.path.insert(0, str(root / "scripts"))
    from cfb_recovery_navigation_reader import read
    from cfb_hot_sheet_current_decision_binding_gate import (
        publication, blob, LEDGER, CURRENT_ROLE,
    )
    index = index_path.read_bytes().decode("utf-8")
    ledger = ledger_path.read_bytes().decode("utf-8")
    for name, digest in [('index', expected_index), ('ledger', expected_ledger), ('sheet', expected_sheet)]:
        if len(digest) != 40 or any(c not in '0123456789abcdef' for c in digest):
            raise ValueError('invalid expected ' + name + ' blob SHA')
    if blob(index) != expected_index or blob(ledger) != expected_ledger:
        raise ValueError('staged index or ledger differs from pinned repository snapshot')
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
    if result["sheet_blob"] != expected_sheet:
        raise ValueError('staged sheet differs from pinned repository snapshot')
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
            "Expected blob SHA values must be sourced from the same verified remote commit; this script cannot prove remote commit provenance",
            "No market/source freshness, offer qualification, scheduled-run, or betting acceptance",
        ],
    }, indent=2))


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo", required=True, type=Path)
    ap.add_argument("--index", required=True, type=Path)
    ap.add_argument("--ledger", required=True, type=Path)
    ap.add_argument("--as-of", required=True)
    ap.add_argument("--expected-index-blob", required=True)
    ap.add_argument("--expected-ledger-blob", required=True)
    ap.add_argument("--expected-sheet-blob", required=True)
    a = ap.parse_args()
    run(a.repo.resolve(), a.index.resolve(), a.ledger.resolve(), a.as_of,
        a.expected_index_blob, a.expected_ledger_blob, a.expected_sheet_blob)
