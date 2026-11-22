"""Read-only Week12 source adapter: fail closed until collection bytes are retained in Git.

This does not publish, re-freeze, or modify any operational ledger. It bridges the
collection manifest to cfb_week12_publication.source_board's retained-file contract.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess

import cfb_week12_publication as week

ROOT = Path(__file__).resolve().parents[1]
OPERATIONS = (ROOT / "evidence/operational").resolve()


def verify(verified_dir, retained_path, as_of):
    verified_dir = Path(verified_dir)
    manifest = json.loads((verified_dir / "manifest.json").read_text())
    if manifest.get("profile") != "WEEK12":
        raise ValueError("not a Week12 verified collection")
    if manifest.get("lineage_blob") != week.WEEK12_LINEAGE_SHA:
        raise ValueError("Week12 lineage mismatch")
    if manifest.get("source_url") != week.WEEK12_URL:
        raise ValueError("Week12 source URL mismatch")
    if not manifest.get("producer_head") or not manifest.get("run_id"):
        raise ValueError("collection provenance incomplete")
    capture = (verified_dir / "capture.md").read_bytes()
    capture_record = manifest.get("files", {}).get("capture.md")
    if (not isinstance(capture_record, dict)
            or capture_record.get("bytes") != len(capture)
            or capture_record.get("sha256") != hashlib.sha256(capture).hexdigest()):
        raise ValueError("collection capture digest or length mismatch")
    path = (ROOT / retained_path).resolve()
    if path.parent != OPERATIONS or path.suffix != ".md":
        raise ValueError("capture must be a retained operational Markdown file")
    if not path.is_file() or path.read_bytes() != capture:
        raise ValueError("retained capture differs from verified collection bytes")
    relative = path.relative_to(ROOT).as_posix()
    committed = subprocess.check_output(
        ["git", "-C", str(ROOT), "show", "HEAD:" + relative])
    if committed != capture:
        raise ValueError("retained capture not identical to committed HEAD blob")
    source = {
        "path": relative,
        "blob": week.gate.blob(capture.decode("utf-8")),
        "recovered_by": manifest["recovered_by"],
    }
    lineage = (ROOT / "evidence/audits/CFB_WEEK12_CBS_ORIGINAL_LINEAGE_PREFLIGHT_20261115.json").read_text()
    board = week.source_board(source, lineage, as_of)
    return {
        "status": "PASS_WEEK12_READ_ONLY_SOURCE_ADAPTER_NOT_PUBLICATION",
        "retained_path": relative,
        "capture_blob": source["blob"],
        "games": len(board["games"]),
        "producer_head": manifest["producer_head"],
        "run_id": manifest["run_id"],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--verified-dir", required=True)
    parser.add_argument("--retained-path", required=True)
    parser.add_argument("--as-of", required=True)
    args = parser.parse_args()
    print(json.dumps(verify(args.verified_dir, args.retained_path, args.as_of), indent=2))


if __name__ == "__main__":
    main()
