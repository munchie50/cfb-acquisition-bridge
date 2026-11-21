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
        fake_week = SimpleNamespace(bootstrap_check=lambda m, d, l: "PASS_WEEK12_CONDITIONAL_PROPOSAL_ONLY")
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
        base = b"base\n"
        packet = {"cycle_id": "c", "as_of_utc": "2026-11-21T15:00:00Z", "rows": {}}
        delta = ("\x60\x60\x60cfb-week12-market-v1\n" +
                 json.dumps(packet) + "\n\x60\x60\x60").encode()
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

    def test_pair_adapter_rejects_nonpassing_bootstrap(self):
        from types import SimpleNamespace
        with patch.object(probe, "reconstruct", return_value={
                "market": "market", "decision": self.ledger}):
            with patch.dict(sys.modules, {"cfb_week12_publication":
                    SimpleNamespace(bootstrap_check=lambda *args: "RUN_INCOMPLETE")}):
                with self.assertRaisesRegex(ValueError, "bootstrap did not return"):
                    probe.inspect_pair(None, {}, self.sheet, "lineage")

    def test_cli_sheet_option_invokes_paired_consumer(self):
        import json
        from tempfile import TemporaryDirectory
        with TemporaryDirectory() as td:
            root = Path(td)
            manifest = root / "manifest.json"
            lineage = root / "lineage.md"
            sheet = root / "preview.md"
            manifest.write_text(json.dumps({"cycle_id": "cycle", "as_of_utc": "2026-11-21T15:00:00Z"}))
            lineage.write_text("lineage")
            sheet.write_text("preview")
            argv = ["probe", "--repo", td, "--manifest", str(manifest),
                    "--lineage", str(lineage), "--sheet", str(sheet)]
            with patch.object(sys, "argv", argv):
                with patch.object(probe, "inspect_pair", return_value={
                        "status": "READ_ONLY_VERIFIED_PREVIEW", "production_acceptance": False}) as paired:
                    with patch("builtins.print") as printed:
                        probe.main()
            paired.assert_called_once_with(root, json.loads(manifest.read_text()),
                                           "preview", "lineage")
            self.assertFalse(json.loads(printed.call_args.args[0])["production_acceptance"])


    def test_reconstruction_multiple_packets_and_divergent_intermediate_boundary(self):
        import json
        base = b"base\n"
        last = ("c2", "2026-11-21T16:00:00Z")
        def delta(surface, first):
            def packet(boundary):
                return ("\x60\x60\x60cfb-week12-" + surface + "-v1\n" +
                        json.dumps({"cycle_id": boundary[0], "as_of_utc": boundary[1],
                                    "rows": []}) + "\n\x60\x60\x60\n")
            return (packet(first) + packet(last)).encode()
        market = delta("market", ("c1", "2026-11-21T15:00:00Z"))
        decision = delta("decision", ("c1", "2026-11-21T15:00:00Z"))
        def manifest(m, d):
            return {"schema": "cfb-overlay-probe-v1", "cycle_id": last[0],
                    "as_of_utc": last[1],
                    "market": {"base": probe.git_blob_sha(base),
                               "delta": probe.git_blob_sha(m),
                               "expected_blob": probe.git_blob_sha(base + m)},
                    "decision": {"base": probe.git_blob_sha(base),
                                 "delta": probe.git_blob_sha(d),
                                 "expected_blob": probe.git_blob_sha(base + d)}}
        blobs = {probe.git_blob_sha(raw): raw for raw in (base, market, decision)}
        with patch.object(probe, "checked_blob", side_effect=lambda repo, sha: blobs[sha]):
            result = probe.reconstruct(None, manifest(market, decision))
            self.assertEqual(result["market"], (base + market).decode())
            self.assertEqual(result["decision"], (base + decision).decode())
        divergent = delta("decision", ("wrong", "2026-11-21T15:00:00Z"))
        blobs[probe.git_blob_sha(divergent)] = divergent
        with patch.object(probe, "checked_blob", side_effect=lambda repo, sha: blobs[sha]):
            with self.assertRaisesRegex(ValueError, "boundaries disagree"):
                probe.reconstruct(None, manifest(market, divergent))


    def test_duplicate_and_reordered_cycles_rejected_even_if_streams_agree(self):
        import json
        base = b"base\\n"
        def packet(surface, cycle, instant):
            return ("\\x60\\x60\\x60cfb-week12-" + surface + "-v1\\n" +
                    json.dumps({"cycle_id": cycle, "as_of_utc": instant, "rows": []}) +
                    "\\n\\x60\\x60\\x60\\n").encode()
        def check(boundaries, expected):
            market = b"".join(packet("market", *b) for b in boundaries)
            decision = b"".join(packet("decision", *b) for b in boundaries)
            blobs = {probe.git_blob_sha(raw): raw for raw in (base, market, decision)}
            manifest = {"schema": "cfb-overlay-probe-v1",
                        "cycle_id": boundaries[-1][0], "as_of_utc": boundaries[-1][1],
                        "market": {"base": probe.git_blob_sha(base),
                                   "delta": probe.git_blob_sha(market),
                                   "expected_blob": probe.git_blob_sha(base + market)},
                        "decision": {"base": probe.git_blob_sha(base),
                                     "delta": probe.git_blob_sha(decision),
                                     "expected_blob": probe.git_blob_sha(base + decision)}}
            with patch.object(probe, "checked_blob", side_effect=lambda repo, sha: blobs[sha]):
                with self.assertRaisesRegex(ValueError, expected):
                    probe.reconstruct(None, manifest)
        t1 = "2026-11-21T15:00:00Z"
        t2 = "2026-11-21T16:00:00Z"
        check([("c1", t1), ("c1", t2)], "duplicate overlay cycle")
        check([("c1", t2), ("c2", t1)], "reordered or duplicate overlay timestamp")
        check([("c1", t1), ("c2", t1)], "reordered or duplicate overlay timestamp")


if __name__ == "__main__":
    unittest.main()
