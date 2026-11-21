"""Read-only overlay-to-preview binding guard tests."""
import importlib.util
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from cfb_hot_sheet_current_decision_binding_gate import blob

spec = importlib.util.spec_from_file_location("cfb_overlay_publication_probe", ROOT / "scripts" / "cfb_overlay_publication_probe.py")
probe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(probe)


class OverlayBindingTests(unittest.TestCase):
    def setUp(self):
        self.ledger = "governed decision ledger\n"
        self.sha = blob(self.ledger)
        self.sheet = ("**Canonical inputs:** market " + "a" * 40 + "; decision " +
                      self.sha + "; execution " + "b" * 40 + "; scorecard " + "c" * 40 + ".\n")

    def check(self, sheet):
        with patch.object(probe, "reconstruct", return_value={"market": "x", "decision": self.ledger}):
            return probe.inspect_binding(None, {}, sheet)

    def test_matching_preview_stays_noncanonical(self):
        result = self.check("**NONCANONICAL MANUAL RECOVERY PREVIEW**\n" + self.sheet)
        self.assertEqual(result["status"], "OVERLAY_BYTES_MATCH_PREVIEW_ONLY")
        self.assertFalse(result["production_acceptance"])

    def test_matching_nonprovisional_still_unpublished(self):
        result = self.check(self.sheet)
        self.assertEqual(result["status"], "OVERLAY_BYTES_MATCH_NONPROVISIONAL_UNPUBLISHED")
        self.assertFalse(result["production_acceptance"])

    def test_stale_decision_rejected(self):
        with self.assertRaisesRegex(ValueError, "differs from reconstructed"):
            self.check(self.sheet.replace(self.sha, "0" * 40))

    def test_duplicate_declaration_rejected(self):
        with self.assertRaisesRegex(ValueError, "unique sheet"):
            self.check(self.sheet + self.sheet)

    def test_duplicate_overlay_packet_key_rejected(self):
        import hashlib

        def sha(raw):
            return hashlib.sha1(b"blob " + str(len(raw)).encode() + bytes([0]) + raw).hexdigest()

        base = b"base\n"
        delta = (b"```cfb-week12-market-v1\n"
                 b'{"cycle_id":"c1","cycle_id":"c2","as_of_utc":"2026-11-21T15:00:00Z"}'
                 b"\n```")
        manifest = {"schema": "cfb-overlay-probe-v1", "cycle_id": "c1",
                    "as_of_utc": "2026-11-21T15:00:00Z",
                    "market": {"base": sha(base), "delta": sha(delta),
                               "expected_blob": sha(base + delta)},
                    "decision": {"base": sha(base), "delta": sha(delta),
                                 "expected_blob": sha(base + delta)}}
        with patch.object(probe, "checked_blob", side_effect=lambda repo, digest:
                          base if digest == sha(base) else delta):
            with self.assertRaisesRegex(ValueError, "duplicate overlay packet JSON key"):
                probe.reconstruct(None, manifest)

    def test_pair_adapter_rejects_stale_market_declaration(self):
        from types import SimpleNamespace
        from unittest.mock import patch
        market = "market ledger\n"
        decision = self.ledger
        good = ("**Canonical inputs:** market " + blob(market) +
                "; decision " + blob(decision) + "; execution " + "b" * 40 +
                "; scorecard " + "c" * 40 + ".\n")
        fake_week = SimpleNamespace(bootstrap_check=lambda m, d, l: "PASS_PAIR_ONLY")
        with patch.object(probe, "reconstruct", return_value={"market": market, "decision": decision}):
            with patch.dict(sys.modules, {"cfb_week12_publication": fake_week}):
                with self.assertRaisesRegex(ValueError, "canonical pair differs"):
                    probe.inspect_pair(None, {}, good.replace(blob(market), "0" * 40), "lineage")
                result = probe.inspect_pair(None, {}, "NONCANONICAL\n" + good, "lineage")
                self.assertEqual(result["status"], "READ_ONLY_VERIFIED_PREVIEW")
                self.assertFalse(result["production_acceptance"])


    def test_malformed_manifest_and_packet_rows_rejected(self):
        with self.assertRaisesRegex(ValueError, "manifest must be a JSON object"):
            probe.reconstruct(None, [])
        with self.assertRaisesRegex(ValueError, "invalid surface entry"):
            probe.reconstruct(None, {"schema": "cfb-overlay-probe-v1",
                "cycle_id": "c", "as_of_utc": "2026-11-21T15:00:00Z",
                "market": [], "decision": {}})
        import json
        base = b"base\\n"
        packet = {"cycle_id": "c", "as_of_utc": "2026-11-21T15:00:00Z", "rows": {}}
        delta = ("\x60\x60\x60cfb-week12-market-v1\\n" +
                 json.dumps(packet) + "\\n\x60\x60\x60").encode()
        manifest = {"schema": "cfb-overlay-probe-v1", "cycle_id": "c",
                    "as_of_utc": "2026-11-21T15:00:00Z",
                    "market": {"base": probe.git_blob_sha(base),
                               "delta": probe.git_blob_sha(delta),
                               "expected_blob": probe.git_blob_sha(base + delta)},
                    "decision": {}}
        with patch.object(probe, "checked_blob", side_effect=lambda repo, digest:
                          base if digest == probe.git_blob_sha(base) else delta):
            with self.assertRaisesRegex(ValueError, "packet rows must be a list"):
                probe.reconstruct(None, manifest)


if __name__ == "__main__":
    unittest.main()
