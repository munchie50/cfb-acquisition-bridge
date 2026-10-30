import datetime as dt
import unittest
from cfb_github_watchdog_qa import assess, TARGETS
NOW=dt.datetime.fromisoformat("2026-10-30T16:30:00+00:00")
PATH=next(iter(TARGETS))
def receipt(**kwargs):
    return dict(path=PATH,head_branch="main",event="schedule",created_at="2026-10-27T15:00:00Z",status="completed",conclusion="success",**kwargs)
class WatchdogTests(unittest.TestCase):
    def test_missing(self):
        self.assertEqual(assess([],NOW)[0]["status"],"NO_SCHEDULED_RECEIPT")
    def test_pass(self):
        self.assertEqual(assess([receipt()],NOW)[0]["status"],"GITHUB_WORKFLOW_PASS_ONLY")
    def test_failed(self):
        r=receipt();r["conclusion"]="failure"
        self.assertEqual(assess([r],NOW)[0]["status"],"WORKFLOW_FAILURE")
    def test_stale(self):
        r=receipt();r["created_at"]="2026-10-01T15:00:00Z"
        self.assertEqual(assess([r],NOW)[0]["status"],"STALE_SCHEDULED_RECEIPT")
    def test_not_terminal(self):
        r=receipt();r["status"]="in_progress"
        self.assertEqual(assess([r],NOW)[0]["status"],"RUN_NOT_TERMINAL")
    def test_dedup_key_stable_and_failure_actionable(self):
        r=receipt();r["id"]=123;r["conclusion"]="failure"
        first=assess([r],NOW)[0]
        second=assess([r],NOW)[0]
        self.assertEqual(first["incident_key"],second["incident_key"])
        self.assertTrue(first["action_required"])
        self.assertFalse(assess([receipt()],NOW)[0]["action_required"])
    def test_manual_not_schedule(self):
        r=receipt();r["event"]="workflow_dispatch"
        self.assertEqual(assess([r],NOW)[0]["status"],"NO_SCHEDULED_RECEIPT")
if __name__=="__main__":
    unittest.main()
