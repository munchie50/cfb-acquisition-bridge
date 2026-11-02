"""Read-only regression tests for runtime diagnostic classification."""
import unittest
from cfb_runtime_failure_trace_readonly import classify, trace

class DiagnosticTests(unittest.TestCase):
    def test_dns(self):
        self.assertEqual(classify("checkout", "fatal: Could not resolve host: github.com"), "DNS_RESOLUTION")

    def test_distinguishes_failure_boundaries(self):
        self.assertEqual(classify("compiler", "process exited 1"), "COMPILER")
        self.assertEqual(classify("publication", "validation failed"), "PUBLICATION")
        self.assertEqual(classify("connector", "API unavailable"), "CONNECTOR")
        self.assertEqual(classify("checkout", "shallow repository"), "GIT_ANCESTRY")

    def test_trace_is_not_acceptance(self):
        record = trace("checkout", "BLOCKED", "Could not resolve host: github.com", "CFB-TEST", "2026-11-02T20:00:00Z")
        self.assertEqual(record["failure_category"], "DNS_RESOLUTION")
        self.assertEqual(record["scope"], "DIAGNOSTIC_ONLY_NO_PRODUCTION_ACCEPTANCE")

    def test_redacts_credentials(self):
        record = trace("connector", "FAIL", "token=abc123 https://someone:secret@github.com")
        self.assertNotIn("abc123", record["error_excerpt"])
        self.assertNotIn("someone:secret", record["error_excerpt"])

    def test_rejects_bad_correlation(self):
        with self.assertRaises(ValueError):
            trace("checkout", "FAIL", correlation_id="../../unsafe")

if __name__ == "__main__":
    unittest.main()
