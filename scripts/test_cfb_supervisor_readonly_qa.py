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
        self.assertEqual(classify(dict(BASE,started_at="2026-10-30T15:15:44Z",completed_at="2026-10-30T15:20:00Z",recorded_status="completed",authority_read_verified=True,startup_run_id="test",closure_run_id="test",readback_run_id="test",qualified_publication=True),NOW),"VERIFIED_PASS")
    def test_legacy_boolean_cannot_pass(self):
        r=dict(BASE,started_at="2026-10-30T15:15:44Z",completed_at="2026-10-30T15:20:00Z",recorded_status="completed",producer_artifact_verified=True)
        self.assertEqual(classify(r,NOW),"PRODUCER_UNVERIFIED")
    def test_cross_run_receipts_cannot_pass(self):
        good=dict(BASE,started_at="2026-10-30T15:15:44Z",completed_at="2026-10-30T15:20:00Z",recorded_status="completed",authority_read_verified=True,startup_run_id="test",closure_run_id="test",readback_run_id="test",qualified_publication=True)
        for field in ("startup_run_id","closure_run_id","readback_run_id"):
            self.assertEqual(classify(dict(good,**{field:"other-run"}),NOW),"PRODUCER_UNVERIFIED")
        for field in ("authority_read_verified","qualified_publication"):
            self.assertEqual(classify(dict(good,**{field:False}),NOW),"PRODUCER_UNVERIFIED")
    def test_failure_overrides_complete_receipts(self):
        good=dict(BASE,started_at="2026-10-30T15:15:44Z",completed_at="2026-10-30T15:20:00Z",authority_read_verified=True,startup_run_id="test",closure_run_id="test",readback_run_id="test",qualified_publication=True)
        for status in ("failed","no_update","cancelled"):
            self.assertEqual(classify(dict(good,recorded_status=status),NOW),"RUN_FAILURE")
    def test_actual_oct31_four_task_no_update_receipts(self):
        # Observed Automations metadata; scheduler start is not producer-start proof.
        receipts=[
            ("bada8a47-b168-832f-ab6c-0f8c3359e8b7","2026-10-31T23:55:23.851701Z","2026-10-31T23:55:34.522483Z","2026-10-31T23:55:37.458922Z"),
            ("07df7505-0e0c-8326-b708-c63bd36a928a","2026-10-31T21:30:00Z","2026-10-31T21:51:58.594546Z","2026-10-31T21:51:59.205276Z"),
            ("988ca83e-87b4-832f-a645-2f40e45d39d4","2026-10-31T14:00:00Z","2026-10-31T14:01:36.670445Z","2026-10-31T14:01:37.372879Z"),
            ("538a2aa6-fd64-832c-91c1-a9ddf5f6d471","2026-10-31T00:30:00Z","2026-10-31T01:19:27.628173Z","2026-10-31T01:19:28.289293Z"),
        ]
        now=dt.datetime.fromisoformat("2026-11-01T01:00:00+00:00")
        for run_id,due,start,end in receipts:
            record=dict(id=run_id,scheduled_for=due,started_at=start,completed_at=end,
                        recorded_status="no_update",chat_ref=None)
            self.assertEqual(classify(record,now),"RUN_FAILURE")
            # Even forged matching receipt booleans must not override scheduler failure.
            record.update(authority_read_verified=True,startup_run_id=run_id,
                          closure_run_id=run_id,readback_run_id=run_id,qualified_publication=True)
            self.assertEqual(classify(record,now),"RUN_FAILURE")
if __name__=="__main__":
    unittest.main()
