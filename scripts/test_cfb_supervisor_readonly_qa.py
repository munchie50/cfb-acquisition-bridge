import datetime as dt
import unittest
from cfb_supervisor_readonly_qa import classify
NOW=dt.datetime.fromisoformat("2026-10-30T16:30:00+00:00")
BASE={"scheduled_for":"2026-10-30T15:15:24Z","id":"test"}
class ClassifierTests(unittest.TestCase):
    def test_missing(self):
        self.assertEqual(classify(BASE,NOW),"MISSING_START")
    def test_no_update(self):
        self.assertEqual(classify(dict(BASE,started_at="2026-10-30T15:15:44Z",completed_at="2026-10-30T15:15:45Z",recorded_status="no_update"),NOW),"RUN_FAILURE")
    def test_started_no_terminal(self):
        self.assertEqual(classify(dict(BASE,started_at="2026-10-30T15:15:44Z"),NOW),"NO_TERMINAL")
    def test_completed_without_producer(self):
        self.assertEqual(classify(dict(BASE,started_at="2026-10-30T15:15:44Z",completed_at="2026-10-30T15:20:00Z",recorded_status="completed"),NOW),"PRODUCER_UNVERIFIED")
    def test_verified_pass(self):
        self.assertEqual(classify(dict(BASE,started_at="2026-10-30T15:15:44Z",completed_at="2026-10-30T15:20:00Z",recorded_status="completed",producer_artifact_verified=True),NOW),"VERIFIED_PASS")
if __name__=="__main__":
    unittest.main()
