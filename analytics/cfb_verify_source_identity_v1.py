#!/usr/bin/env python3
"""Fail-closed provenance verifier for CFB analytics JSONL; no conversion or source mutation."""
import argparse
import hashlib
import json
from pathlib import Path
from cfb_read_only_analytics_v1 import timestamp, load, analyze

def git_blob(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def verify(root, input_file, as_of):
    rows, errors = load(input_file, timestamp(as_of))
    base = root.resolve()
    checked_market = 0
    for i, row in enumerate(rows, 1):
        if row["source_kind"] != "CERTIFIED_MARKET":
            continue
        checked_market += 1
        rel = Path(row["source_path"])
        if rel.is_absolute() or ".." in rel.parts:
            errors.append("row %d: invalid source path" % i)
            continue
        src = (base / rel).resolve()
        if not src.is_relative_to(base) or not src.is_file():
            errors.append("row %d: source unavailable" % i)
            continue
        if git_blob(src.read_bytes()) != row["source_blob"]:
            errors.append("row %d: source blob mismatch" % i)
    if checked_market == 0:
        errors.append("NO_MARKET_ROWS_TO_VERIFY")
    result = analyze(rows, errors, timestamp(as_of))
    # A blob hash proves byte identity only; it does not certify that the upstream
    # quote is genuine or was captured contemporaneously.
    result["provenance_scope"] = "LOCAL_GIT_BLOB_IDENTITY_ONLY_NOT_UPSTREAM_CERTIFICATION"
    result["status"] = "INCOMPLETE" if errors or not rows else "UNVERIFIED_SOURCE_ATTESTATION"
    result["eligible_for_production_learning"] = False
    result["market_rows_examined"] = checked_market
    return result

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--root", required=True)
    p.add_argument("--input", required=True)
    p.add_argument("--as-of", required=True)
    p.add_argument("--output")
    a = p.parse_args()
    result = verify(Path(a.root), a.input, a.as_of)
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if a.output:
        Path(a.output).write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
    raise SystemExit(2 if result["status"] == "INCOMPLETE" else 3)

if __name__ == "__main__":
    main()
