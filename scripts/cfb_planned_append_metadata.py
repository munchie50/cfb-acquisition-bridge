#!/usr/bin/env python3
"""Compute content-free metadata for a permitted planned append; never writes."""
import argparse
import hashlib
import json
import re
from pathlib import Path

FIELDS = {"game_identity", "observation_timestamp", "source", "book", "line", "price",
          "availability", "executability", "provenance", "champion_snapshot", "decision_state"}
TRANSFER_CHARACTERS = 12000

def git_blob(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def transfer(data, expected_sha, chunk_index=None, chunk_characters=TRANSFER_CHARACTERS):
    """Read exact bounded UTF-8 chunks; never write or certify persistence.

    The receiver must check ordered complete assembly against the manifest's
    byte count and Git blob before calling Contents. A valid local proposal is
    not proof the outgoing tool argument contains those same bytes.
    """
    if not re.fullmatch(r"[0-9a-f]{40}", expected_sha):
        raise ValueError("invalid expected transport Git blob SHA")
    if git_blob(data) != expected_sha:
        raise ValueError("transfer source differs from expected complete Git blob")
    if type(chunk_characters) is not int or not 1 <= chunk_characters <= TRANSFER_CHARACTERS:
        raise ValueError("chunk characters must be between 1 and 12000")
    text = data.decode("utf-8")
    count = max(1, (len(text) + chunk_characters - 1) // chunk_characters)
    result = {"schema": "CFB_EXACT_TEXT_TRANSFER_V1", "status": "TRANSPORT_ONLY_NOT_WRITE_SUCCESS",
              "git_blob": expected_sha, "sha256": hashlib.sha256(data).hexdigest(),
              "bytes": len(data), "characters": len(text),
              "chunk_characters": chunk_characters, "chunk_count": count,
              "raw_content_included": chunk_index is not None}
    if chunk_index is not None:
        if type(chunk_index) is not int or not 0 <= chunk_index < count:
            raise ValueError("chunk index outside complete source")
        piece = text[chunk_index * chunk_characters:(chunk_index + 1) * chunk_characters]
        encoded = piece.encode("utf-8")
        result.update(chunk_index=chunk_index, content=piece,
                      chunk_bytes=len(encoded), chunk_characters_actual=len(piece),
                      chunk_git_blob=git_blob(encoded))
    return result

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
    parser.add_argument("--prior", type=Path)
    parser.add_argument("--proposed", type=Path)
    parser.add_argument("--expected-prior-sha")
    parser.add_argument("--inventory", help="comma-separated approved field names")
    parser.add_argument("--transfer-file", type=Path)
    parser.add_argument("--expected-transport-sha")
    parser.add_argument("--chunk-index", type=int)
    parser.add_argument("--chunk-characters", type=int, default=TRANSFER_CHARACTERS)
    args = parser.parse_args()
    if args.transfer_file is not None:
        if not args.expected_transport_sha or any(v is not None for v in
                (args.prior, args.proposed, args.expected_prior_sha, args.inventory)):
            parser.error('transfer requires expected transport SHA and no append-metadata arguments')
        result = transfer(args.transfer_file.read_bytes(), args.expected_transport_sha,
                          args.chunk_index, args.chunk_characters)
        print(json.dumps(result, ensure_ascii=False))
        return
    if any(v is not None for v in (args.expected_transport_sha, args.chunk_index)):
        parser.error('transport options require --transfer-file')
    if any(v is None for v in (args.prior, args.proposed, args.expected_prior_sha, args.inventory)):
        parser.error('append metadata requires prior, proposed, expected-prior-sha and inventory')
    # No payload text, file paths or market values are emitted.
    result = metadata(args.prior.read_bytes(), args.proposed.read_bytes(),
                      args.expected_prior_sha, args.inventory.split(","))
    print(json.dumps(result, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
