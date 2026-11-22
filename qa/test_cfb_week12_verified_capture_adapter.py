"""Contract tests for Week12 verified-collection adapter (no network or production writes)."""
import hashlib
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

import cfb_week12_verified_capture_adapter as adapter


class AdapterContractTests(unittest.TestCase):
    def test_manifest_nested_digest_and_negative_guards(self):
        capture = b"retained verified board\n"
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            operational = root / "evidence" / "operational"
            operational.mkdir(parents=True)
            lineage = root / "evidence" / "audits"
            lineage.mkdir(parents=True)
            (lineage / "CFB_WEEK12_CBS_ORIGINAL_LINEAGE_PREFLIGHT_20261115.json").write_text("{}")
            retained = operational / "board.md"
            retained.write_bytes(capture)
            verified = root / "verified"
            verified.mkdir()
            (verified / "capture.md").write_bytes(capture)
            manifest = {
                "profile": "WEEK12", "lineage_blob": adapter.week.WEEK12_LINEAGE_SHA,
                "source_url": adapter.week.WEEK12_URL, "producer_head": "abc",
                "run_id": "123", "recovered_by": "2026-11-20T12:00:00Z",
                "files": {"capture.md": {
                    "bytes": len(capture),
                    "sha256": hashlib.sha256(capture).hexdigest(),
                }},
            }
            def save():
                (verified / "manifest.json").write_text(json.dumps(manifest))
            save()
            def committed(*args, **kwargs):
                return capture
            with (patch.object(adapter, "ROOT", root),
                  patch.object(adapter, "OPERATIONS", operational.resolve()),
                  patch.object(adapter.subprocess, "check_output", side_effect=committed),
                  patch.object(adapter.week, "source_board", return_value={"games": [{}] * 70})):
                result = adapter.verify(verified, "evidence/operational/board.md",
                                        "2026-11-20T12:01:00Z")
                self.assertEqual(result["games"], 70)
                manifest["files"]["capture.md"]["sha256"] = "0" * 64
                save()
                with self.assertRaisesRegex(ValueError, "digest or length"):
                    adapter.verify(verified, "evidence/operational/board.md", "2026-11-20T12:01:00Z")
                manifest["files"]["capture.md"]["sha256"] = hashlib.sha256(capture).hexdigest()
                manifest["files"]["capture.md"]["bytes"] += 1
                save()
                with self.assertRaisesRegex(ValueError, "digest or length"):
                    adapter.verify(verified, "evidence/operational/board.md", "2026-11-20T12:01:00Z")
                manifest["files"]["capture.md"]["bytes"] -= 1
                save()
                retained.write_bytes(b"modified")
                with self.assertRaisesRegex(ValueError, "differs"):
                    adapter.verify(verified, "evidence/operational/board.md", "2026-11-20T12:01:00Z")
                retained.write_bytes(capture)
                with patch.object(adapter.subprocess, "check_output", return_value=b"other"):
                    with self.assertRaisesRegex(ValueError, "committed HEAD"):
                        adapter.verify(verified, "evidence/operational/board.md", "2026-11-20T12:01:00Z")
                manifest["profile"] = "WEEK11"
                save()
                with self.assertRaisesRegex(ValueError, "not a Week12"):
                    adapter.verify(verified, "evidence/operational/board.md", "2026-11-20T12:01:00Z")


if __name__ == "__main__":
    unittest.main()
