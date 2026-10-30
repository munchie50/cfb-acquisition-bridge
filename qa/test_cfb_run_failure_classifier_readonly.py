"""Fixture tests for the read-only QA classifier."""
import unittest
from cfb_run_failure_classifier_readonly import Evidence, classify

class ClassifierFixtures(unittest.TestCase):
    def test_six_states(self):
        cases = {
            "NO_UPDATE": Evidence(scheduler_no_update=True),
            "START_ONLY": Evidence(producer_started=True),
            "WRITE_REJECTED": Evidence(producer_started=True, canonical_write_attempted=True),
            "PARTIAL_SOURCE": Evidence(producer_started=True, canonical_write_attempted=True, canonical_write_accepted=True),
            "PUBLISHED_UNVERIFIED": Evidence(producer_started=True, canonical_write_attempted=True, canonical_write_accepted=True, source_complete=True, publication_present=True),
            "RUN_PASS": Evidence(producer_started=True, canonical_write_attempted=True, canonical_write_accepted=True, source_complete=True, publication_present=True, independent_publication_verified=True),
        }
        for expected, evidence in cases.items():
            with self.subTest(expected=expected):
                self.assertEqual(classify(evidence), expected)

    def test_no_false_success(self):
        e = Evidence(producer_started=True, canonical_write_accepted=True, source_complete=True, publication_present=True)
        self.assertNotEqual(classify(e), "RUN_PASS")

if __name__ == "__main__":
    unittest.main()
