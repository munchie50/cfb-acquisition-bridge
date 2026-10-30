import unittest
from cfb_incident_ledger_qa import reconcile
T="2026-10-30T17:00:00Z"
FAIL={"incident_key":"abc","path":"weekly.yml","status":"WORKFLOW_FAILURE","action_required":True}
PASS={"incident_key":"xyz","path":"weekly.yml","status":"GITHUB_WORKFLOW_PASS_ONLY","action_required":False}
class LedgerTests(unittest.TestCase):
    def test_first_failure_opens(self):
        rows,events=reconcile([],[FAIL],T)
        self.assertEqual(rows[0]["status"],"OPEN")
        self.assertEqual(events[0]["event"],"OPENED")
    def test_repeat_is_not_duplicate(self):
        rows,_=reconcile([],[FAIL],T)
        rows,events=reconcile(rows,[FAIL],T)
        self.assertEqual(len(rows),1)
        self.assertEqual(rows[0]["observations"],2)
        self.assertEqual(events[0]["event"],"OBSERVED_EXISTING")
    def test_green_not_producer_closure(self):
        rows,_=reconcile([],[FAIL],T)
        rows,events=reconcile(rows,[PASS],T)
        self.assertEqual(rows[0]["status"],"AWAITING_PRODUCER_VERIFICATION")
        self.assertEqual(events[0]["event"],"WORKFLOW_GREEN_NOT_CLOSED")
    def test_no_automatic_recovery(self):
        rows,_=reconcile([],[FAIL],T)
        self.assertEqual(rows[0]["recovery_attempts"],0)
    def test_unrelated_pass_no_change(self):
        rows,events=reconcile([],[PASS],T)
        self.assertEqual(rows,[])
        self.assertEqual(events,[])
if __name__=="__main__":
    unittest.main()
