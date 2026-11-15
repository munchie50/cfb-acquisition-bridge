"""Read-only, file-only checkout probe for an authenticated Actions bundle ZIP."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
from zipfile import ZipFile


REQUIRED = (
    "cfb_runtime_checkout.py", "cfb_neutral_publication_gate.py",
    "cfb_hot_sheet_readiness.py", "cfb_recovery_consumer_preflight.py",
    "cfb_monitor_collection.py",
)


def validate_reviews(repo):
    sys.path.insert(0, str(repo / "scripts"))
    from cfb_conditional_recommendation_profile import load_review

    ledger = (repo / "evidence/operational/CFB_DECISION_WAIT_LEDGER.md").read_text()
    refs = {}
    for body in re.findall(r"^\x60\x60\x60cfb-[^\n]+\n(.*?)^\x60\x60\x60\s*$", ledger, re.M | re.S):
        for row in json.loads(body).get("rows", []):
            ref = row.get("review_ref")
            if ref:
                refs[(ref["commit"], ref["path"], ref["blob"])] = ref
    if not refs:
        raise ValueError("no immutable review references")
    for ref in refs.values():
        load_review(ref)
    return len(refs)


def probe(archive, archive_digest, expected_head, destination, profile_script):
    result = {"status": "RUN_INCOMPLETE", "head_expected": expected_head}
    stage = "ARCHIVE_INTEGRITY"
    try:
        if not re.fullmatch("[0-9a-f]{40}", expected_head):
            raise ValueError("authenticated exact main pin required")
        with archive.open("rb") as source:
            digest = hashlib.file_digest(source, "sha256").hexdigest()
        if digest != archive_digest:
            raise ValueError("archive digest mismatch")
        result.update(archive_bytes=archive.stat().st_size, archive_sha256=digest)
        stage = "BINARY_MATERIALIZATION"
        destination = destination.resolve()
        destination.mkdir()
        bundle = destination / "engine.bundle"
        with ZipFile(archive) as package:
            if package.namelist() != ["engine.bundle"]:
                raise ValueError("unexpected archive member set")
            with package.open("engine.bundle") as source, bundle.open("xb") as target:
                shutil.copyfileobj(source, target)
        result["bundle_bytes"] = bundle.stat().st_size
        if not result["bundle_bytes"]:
            raise ValueError("empty Git bundle")

        env = dict(os.environ, GIT_ALLOW_PROTOCOL="file", GIT_TERMINAL_PROMPT="0")
        def git(*args):
            return subprocess.check_output(["git", *args], env=env, stderr=subprocess.PIPE,
                                           timeout=120, text=True).strip()

        stage = "PIN_VALIDATION"
        heads = git("bundle", "list-heads", str(bundle)).splitlines()
        if heads != [f"{expected_head} refs/heads/offline-engine"]:
            raise ValueError("bundle pin differs from authenticated exact main")
        stage = "FILE_ONLY_CHECKOUT"
        repo = destination / "repo"
        git("clone", "--branch", "offline-engine", str(bundle), str(repo))
        actual = git("-C", str(repo), "rev-parse", "HEAD")
        if actual != expected_head or git("-C", str(repo), "rev-parse", "--is-shallow-repository") != "false":
            raise ValueError("checkout head or ancestry mismatch")
        result["head_actual"] = actual
        stage = "PROFILE_READINESS"
        if not re.fullmatch(r"cfb_week\d+_publication\.py", profile_script):
            raise ValueError("expected weekly publication script name required")
        result["missing_scripts"] = [
            name for name in (*REQUIRED, profile_script) if not (repo / "scripts" / name).is_file()
        ]
        stage = "IMMUTABLE_REVIEW_VALIDATION"
        result["immutable_reviews"] = validate_reviews(repo)
        result["status"] = "FILE_ONLY_CHECKOUT_VERIFIED"
        result["profile_ready"] = not result["missing_scripts"]
        result["stage"] = "COMPLETE"
    except (ValueError, OSError, RuntimeError, subprocess.SubprocessError, ImportError) as exc:
        result.update(stage=stage, error=type(exc).__name__)
        if isinstance(exc, ValueError):
            result["reason"] = str(exc)[:180]
    finally:
        print(json.dumps(result, sort_keys=True))
    return result["status"] == "FILE_ONLY_CHECKOUT_VERIFIED"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, required=True)
    parser.add_argument("--archive-digest", required=True)
    parser.add_argument("--expected-head", required=True)
    parser.add_argument("--destination", type=Path, required=True)
    parser.add_argument("--profile-script", required=True)
    args = parser.parse_args()
    sys.exit(0 if probe(args.archive, args.archive_digest, args.expected_head,
                        args.destination, args.profile_script) else 1)
