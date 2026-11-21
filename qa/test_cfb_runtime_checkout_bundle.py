"""Offline bundle checkout guard regression tests; no network or production writes."""
import hashlib
import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "cfb_runtime_checkout.py"
spec = importlib.util.spec_from_file_location("cfb_runtime_checkout", SCRIPT)
checkout = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checkout)


class BundleGuardTests(unittest.TestCase):
    def test_bad_pin_rejected_before_transport(self):
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaisesRegex(ValueError, "exact connector-observed"):
                checkout.prepare(Path(temp) / "new", "not-a-sha")

    def test_digest_required_with_bundle(self):
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaisesRegex(ValueError, "supplied together"):
                checkout.prepare(Path(temp) / "new", "a" * 40, bundle=Path(temp) / "x")

    def test_bundle_digest_mismatch_rejected_before_git(self):
        with tempfile.TemporaryDirectory() as temp:
            bundle = Path(temp) / "x.bundle"
            bundle.write_bytes(b"bundle fixture")
            with patch.object(checkout.subprocess, "check_output", side_effect=AssertionError("git invoked")):
                with self.assertRaisesRegex(ValueError, "SHA-256 differs"):
                    checkout.prepare(Path(temp) / "new", "a" * 40,
                                     bundle=bundle, bundle_sha256="0" * 64)

    def test_stale_main_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            bundle = Path(temp) / "x.bundle"
            bundle.write_bytes(b"fixture")
            digest = hashlib.sha256(bundle.read_bytes()).hexdigest()
            with patch.object(checkout.subprocess, "check_output",
                              return_value=(("b" * 40) + " refs/heads/main\n").encode()):
                with self.assertRaisesRegex(ValueError, "bundle main differs"):
                    checkout.prepare(Path(temp) / "new", "a" * 40,
                                     bundle=bundle, bundle_sha256=digest)

    def test_real_local_bundle_reaches_immutable_review_gate(self):
        # A genuine file-only checkout must reach the original retained-review gate.
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            source = base / "source"
            source.mkdir()
            subprocess.run(["git", "init", "-q", "-b", "main", str(source)], check=True)
            subprocess.run(["git", "-C", str(source), "config", "user.email", "qa@example.invalid"], check=True)
            subprocess.run(["git", "-C", str(source), "config", "user.name", "QA"], check=True)
            (source / "README").write_text("fixture\n")
            subprocess.run(["git", "-C", str(source), "add", "README"], check=True)
            subprocess.run(["git", "-C", str(source), "commit", "-qm", "fixture"], check=True)
            head = subprocess.check_output(["git", "-C", str(source), "rev-parse", "HEAD"], text=True).strip()
            bundle = base / "fixture.bundle"
            subprocess.run(["git", "-C", str(source), "bundle", "create", str(bundle), "--all"], check=True)
            digest = hashlib.sha256(bundle.read_bytes()).hexdigest()
            with self.assertRaisesRegex(ValueError, "missing governed compiler"):
                checkout.prepare(base / "checkout", head, bundle=bundle, bundle_sha256=digest)
            self.assertEqual(subprocess.check_output(
                ["git", "-C", str(base / "checkout"), "rev-parse", "HEAD"], text=True).strip(), head)


if __name__ == "__main__":
    unittest.main()
