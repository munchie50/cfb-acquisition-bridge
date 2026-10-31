"""Isolated, no-network regression for prospective Week10 source preflight."""
import hashlib
import sys
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from cfb_week10_source_preflight_readonly import EXPECTED_URL, check


class Week10SourcePreflightTests(unittest.TestCase):
    def setUp(self):
        self.recovered = "2026-11-01T15:00:00Z"
        self.now = "2026-11-01T15:10:00Z"
        self.capture = "Captured from " + EXPECTED_URL + "\\n| Game | Odds |\\n"

    def validate(self, **overrides):
        args = dict(capture=self.capture, source_url=EXPECTED_URL,
                    recovered_by=self.recovered, as_of=self.now)
        args.update(overrides)
        return check(**args)

    def test_valid_capture_is_preflight_only(self):
        result = self.validate()
        self.assertEqual(result["status"], "WEEK10_SOURCE_PREFLIGHT_ONLY")
        self.assertFalse(result["publication_authorized"])
        self.assertFalse(result["decision_rows_authored"])
        self.assertIsNone(result["qualified_games"])
        raw = self.capture.encode()
        expected = hashlib.sha1(b"blob " + str(len(raw)).encode() + bytes([0]) + raw).hexdigest()
        self.assertEqual(result["capture_git_blob"], expected)

    def test_rejects_stale_future_and_naive_times(self):
        for changed in (dict(as_of="2026-11-01T15:16:00Z"),
                        dict(as_of="2026-11-01T14:59:59Z"),
                        dict(as_of="2026-11-01T15:10:00")):
            with self.subTest(changed=changed), self.assertRaises(ValueError):
                self.validate(**changed)

    def test_rejects_week9_empty_and_wrong_source(self):
        for changed in (dict(capture=""), dict(capture="week-9/ " + self.capture),
                        dict(source_url=EXPECTED_URL.replace("week-10", "week-9")),
                        dict(capture="Capture with no source attribution")):
            with self.subTest(changed=changed), self.assertRaises(ValueError):
                self.validate(**changed)


if __name__ == "__main__":
    unittest.main()
