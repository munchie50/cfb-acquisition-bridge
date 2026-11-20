"""Read-only content-addressed overlay publication feasibility probe.

Never mutates canonical surfaces or grants publication acceptance.
"""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path


def git_blob_sha(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\\0" + raw).hexdigest()


def checked_blob(repo, sha):
    if len(sha) != 40 or any(c not in "0123456789abcdef" for c in sha):
        raise ValueError("invalid blob sha")
    raw = subprocess.check_output(["git", "-C", str(repo), "cat-file", "blob", sha])
    if git_blob_sha(raw) != sha:
        raise ValueError("blob identity mismatch")
    return raw


def reconstruct(repo, manifest):
    if manifest.get("schema") != "cfb-overlay-probe-v1":
        raise ValueError("unsupported manifest")
    if set(manifest) != {"schema", "cycle_id", "as_of_utc", "market", "decision"}:
        raise ValueError("unexpected manifest fields")
    outputs = {}
    for surface in ("market", "decision"):
        entry = manifest[surface]
        if set(entry) != {"base", "delta", "expected_blob"}:
            raise ValueError("invalid surface entry")
        base = checked_blob(repo, entry["base"])
        delta = checked_blob(repo, entry["delta"])
        if not delta.startswith(("\\x60" * 3 + "cfb-week12-" + surface + "-v1\\n").encode()):
            raise ValueError("wrong packet type")
        raw = base + delta
        if git_blob_sha(raw) != entry["expected_blob"]:
            raise ValueError("reconstruction digest mismatch")
        outputs[surface] = raw.decode("utf-8")
    return outputs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path, required=True)
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--lineage", type=Path, required=True)
    args = ap.parse_args()
    manifest = json.loads(args.manifest.read_text())
    outputs = reconstruct(args.repo, manifest)
    import sys
    sys.path.insert(0, str(args.repo / "scripts"))
    import cfb_week12_publication as week
    result = week.bootstrap_check(outputs["market"], outputs["decision"], args.lineage.read_text())
    print(json.dumps({"status": "READ_ONLY_PROBE_ONLY", "bootstrap": result,
                      "cycle_id": manifest["cycle_id"], "as_of_utc": manifest["as_of_utc"]}, sort_keys=True))


if __name__ == "__main__":
    main()
