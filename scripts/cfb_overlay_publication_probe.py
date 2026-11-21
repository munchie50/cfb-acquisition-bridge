"""Read-only content-addressed overlay publication feasibility probe.

Never mutates canonical surfaces or grants publication acceptance.
"""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path


def git_blob_sha(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + bytes([0]) + raw).hexdigest()


def checked_blob(repo, sha):
    if len(sha) != 40 or any(c not in "0123456789abcdef" for c in sha):
        raise ValueError("invalid blob sha")
    raw = subprocess.check_output(["git", "-C", str(repo), "cat-file", "blob", sha])
    if git_blob_sha(raw) != sha:
        raise ValueError("blob identity mismatch")
    return raw


def reconstruct(repo, manifest):
    if not isinstance(manifest, dict):
        raise ValueError("overlay manifest must be a JSON object")
    if manifest.get("schema") != "cfb-overlay-probe-v1":
        raise ValueError("unsupported manifest")
    if set(manifest) != {"schema", "cycle_id", "as_of_utc", "market", "decision"}:
        raise ValueError("unexpected manifest fields")
    outputs = {}
    for surface in ("market", "decision"):
        entry = manifest[surface]
        if not isinstance(entry, dict) or set(entry) != {"base", "delta", "expected_blob"}:
            raise ValueError("invalid surface entry")
        base = checked_blob(repo, entry["base"])
        delta = checked_blob(repo, entry["delta"])
        if not delta.startswith(("`" * 3 + "cfb-week12-" + surface + "-v1" + chr(10)).encode()):
            raise ValueError("wrong packet type")
        raw = base + delta
        if git_blob_sha(raw) != entry["expected_blob"]:
            raise ValueError("reconstruction digest mismatch")
        import re
        text = delta.decode("utf-8")
        tag = "cfb-week12-" + surface + "-v1"
        pattern = r"^```" + tag + chr(10) + r"(.*?)^```[ ]*$"
        matches = list(re.finditer(pattern, text, re.M | re.S))
        if not matches or re.sub(pattern, "", text, flags=re.M | re.S).strip():
            raise ValueError("invalid typed packet framing")
        def reject_duplicate_keys(pairs):
            result = {}
            for key, value in pairs:
                if key in result:
                    raise ValueError("duplicate overlay packet JSON key")
                result[key] = value
            return result
        boundaries = []
        for match in matches:
            packet = json.loads(match.group(1), object_pairs_hook=reject_duplicate_keys)
            if not isinstance(packet, dict):
                raise ValueError("overlay packet must be a JSON object")
            if not isinstance(packet.get("rows"), list):
                raise ValueError("overlay packet rows must be a list")
            boundaries.append((packet.get("cycle_id"), packet.get("as_of_utc")))
        if boundaries[-1] != (manifest["cycle_id"], manifest["as_of_utc"]):
            raise ValueError("packet and manifest boundary mismatch")
        outputs[surface] = raw.decode("utf-8")
    return outputs




def inspect_pair(repo, manifest, sheet, lineage):
    """Reconstruct a pinned pair and verify Week12 parent/sequence and preview binding.

    This is a read-only consumer adapter, not a canonical publication or wager gate.
    """
    outputs = reconstruct(repo, manifest)
    import sys
    scripts = str(Path(__file__).resolve().parent)
    if scripts not in sys.path:
        sys.path.insert(0, scripts)
    import cfb_week12_publication as week
    bootstrap = week.bootstrap_check(outputs["market"], outputs["decision"], lineage)
    if not isinstance(bootstrap, str) or not bootstrap.startswith("PASS_WEEK12_"):
        raise ValueError("Week12 bootstrap did not return an accepted read-only proposal verdict")
    from cfb_hot_sheet_current_decision_binding_gate import audit, blob
    import re
    declarations = [line for line in sheet.splitlines() if "Canonical inputs:" in line]
    if len(declarations) != 1:
        raise ValueError("unique sheet canonical declaration required")
    match = re.search(r"market ([0-9a-f]{40}); decision ([0-9a-f]{40})", declarations[0])
    if not match:
        raise ValueError("malformed sheet canonical declaration")
    market_sha, decision_sha = match.groups()
    if market_sha != blob(outputs["market"]) or decision_sha != blob(outputs["decision"]):
        raise ValueError("sheet canonical pair differs from reconstructed overlay")
    try:
        binding = audit(sheet, outputs["decision"])
    except ValueError as exc:
        if "explicitly provisional publication" not in str(exc):
            raise
        return {"status": "READ_ONLY_VERIFIED_PREVIEW", "bootstrap": bootstrap,
                "market_blob": market_sha, "decision_blob": decision_sha,
                "binding": "REJECTED_PROVISIONAL", "production_acceptance": False}
    return {"status": "READ_ONLY_VERIFIED_UNPUBLISHED", "bootstrap": bootstrap,
            "market_blob": market_sha, "decision_blob": decision_sha,
            "binding": binding["verdict"], "production_acceptance": False}


def inspect_binding(repo, manifest, sheet):
    """Inspect exact overlay-to-sheet binding without granting publication authority.

    The existing audit deliberately rejects explicitly provisional previews.
    Report that gate separately from immutable decision-byte identity.
    """
    outputs = reconstruct(repo, manifest)
    from cfb_hot_sheet_current_decision_binding_gate import audit, blob
    declared = []
    for line in sheet.splitlines():
        if "Canonical inputs:" in line:
            import re
            declared.extend(re.findall(r"decision ([0-9a-f]{40})", line))
    if len(declared) != 1:
        raise ValueError("unique sheet decision declaration required")
    expected = blob(outputs["decision"])
    if declared[0] != expected:
        raise ValueError("sheet declaration differs from reconstructed decision")
    try:
        result = audit(sheet, outputs["decision"])
    except ValueError as exc:
        if "explicitly provisional publication" not in str(exc):
            raise
        return {"status": "OVERLAY_BYTES_MATCH_PREVIEW_ONLY",
                "decision_blob": expected, "canonical_binding": "REJECTED_PROVISIONAL",
                "production_acceptance": False, "canonical_mutation": False}
    return {"status": "OVERLAY_BYTES_MATCH_NONPROVISIONAL_UNPUBLISHED",
            "decision_blob": expected, "canonical_binding": result["verdict"],
            "production_acceptance": False, "canonical_mutation": False}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path, required=True)
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--lineage", type=Path, required=True)
    ap.add_argument("--sheet", type=Path, help="Optional preview sheet for paired market/decision binding")
    args = ap.parse_args()
    manifest = json.loads(args.manifest.read_text())
    lineage = args.lineage.read_text()
    if args.sheet:
        result = inspect_pair(args.repo, manifest, args.sheet.read_text(), lineage)
        print(json.dumps({**result, "cycle_id": manifest["cycle_id"],
                          "as_of_utc": manifest["as_of_utc"]}, sort_keys=True))
        return
    outputs = reconstruct(args.repo, manifest)
    import sys
    sys.path.insert(0, str(args.repo / "scripts"))
    import cfb_week12_publication as week
    result = week.bootstrap_check(outputs["market"], outputs["decision"], lineage)
    print(json.dumps({"status": "READ_ONLY_PROBE_ONLY", "bootstrap": result,
                      "cycle_id": manifest["cycle_id"], "as_of_utc": manifest["as_of_utc"]}, sort_keys=True))


if __name__ == "__main__":
    main()
