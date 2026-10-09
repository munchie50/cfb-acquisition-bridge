#!/usr/bin/env python3
"""Compute content-free metadata for a permitted planned append; never writes."""
import argparse
import hashlib
import json
import re
from pathlib import Path

FIELDS = {"game_identity", "observation_timestamp", "source", "book", "line", "price",
          "availability", "executability", "provenance", "champion_snapshot", "decision_state"}

def git_blob(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def metadata(prior, proposed, expected_sha, inventory):
    if not re.fullmatch(r"[0-9a-f]{40}", expected_sha):
        raise ValueError("invalid expected Git blob SHA")
    if git_blob(prior) != expected_sha:
        raise ValueError("baseline does not match expected Git blob SHA")
    if not proposed.startswith(prior):
        raise ValueError("proposal does not preserve complete prior bytes")
    if not inventory or set(inventory) - FIELDS or len(inventory) != len(set(inventory)):
        raise ValueError("inventory must contain unique approved field names")
    prior_text, proposed_text = prior.decode("utf-8"), proposed.decode("utf-8")
    delta = proposed[len(prior):]
    delta_text = delta.decode("utf-8")
    return {
        "schema": "CFB_PLANNED_APPEND_METADATA_V1",
        "status": "PROPOSED_ONLY_NOT_WRITE_SUCCESS",
        "prior_git_blob_sha": expected_sha,
        "proposed_git_blob_sha": git_blob(proposed),
        "prior_sha256": hashlib.sha256(prior).hexdigest(),
        "proposed_sha256": hashlib.sha256(proposed).hexdigest(),
        "delta_sha256": hashlib.sha256(delta).hexdigest(),
        "prior_bytes": len(prior), "proposed_bytes": len(proposed), "delta_bytes": len(delta),
        "prior_characters": len(prior_text), "proposed_characters": len(proposed_text),
        "delta_characters": len(delta_text),
        "prior_bytes_preserved": True,
        "field_inventory": sorted(inventory),
        "inventory_basis": "CALLER_DECLARED_NOT_SEMANTICALLY_VALIDATED",
        "raw_content_included": False
    }

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prior", type=Path, required=True)
    parser.add_argument("--proposed", type=Path, required=True)
    parser.add_argument("--expected-prior-sha", required=True)
    parser.add_argument("--inventory", required=True, help="comma-separated approved field names")
    args = parser.parse_args()
    # No payload text, file paths or market values are emitted.
    result = metadata(args.prior.read_bytes(), args.proposed.read_bytes(),
                      args.expected_prior_sha, args.inventory.split(","))
    print(json.dumps(result, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
