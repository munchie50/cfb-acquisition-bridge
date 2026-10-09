import unittest
from pathlib import Path
from datetime import datetime,date
import cfb_week6_decision_coverage_audit as gate

class CoverageTests(unittest.TestCase):
    def setUp(self):
        self.s=Path('evidence/operational/CFB_WEEK6_HOT_SHEET_2026-10-09_1538CT.md').read_text()
        self.l=Path('evidence/operational/CFB_DECISION_WAIT_LEDGER.md').read_text()
        self.c=Path('evidence/CFB_ENGINE_EARLY_EXPOSURE_AND_LEARNING_CADENCE_CONTROL_v1_237.md').read_text()
        self.t=datetime.fromisoformat('2026-10-09T18:17:14-05:00')

    def audit(self,s=None,l=None,c=None,t=None):
        return gate.audit(s or self.s,l or self.l,self.t if t is None else t,date(2026,10,6),c or self.c)

    def test_current_history_nine_columns(self):
        r=self.audit(); self.assertEqual(r['counts']['slate'],49); self.assertEqual(r['slate_row_columns'],9)
        self.assertTrue(any(x['named_ledger_occurrences']>1 for x in r['rows']))

    def test_original_eight_column_reference(self):
        s=Path('evidence/operational/CFB_WEEK6_HOT_SHEET_RESEARCH_CANDIDATE_2026-10-07.md').read_text()
        self.assertEqual(self.audit(s=s)['slate_row_columns'],8)

    def test_repeated_references_are_naming_only(self):
        r=self.audit(l=self.l+'\n- Iowa @ Washington — synthetic conflicting state\n')
        row=next(x for x in r['rows'] if x['game']=='Iowa @ Washington')
        self.assertGreater(row['named_ledger_occurrences'],1)
        self.assertEqual(row['decision_validation'],'NOT_CERTIFIED')
        self.assertEqual(row['hard_cutoff'],'NOT_EXTRACTED')

    def test_missing_naming_remains_missing(self):
        r=self.audit(l=gate.MARKER+'\nsynthetic unnamed boundary')
        self.assertEqual(r['counts']['named_records'],0)

    def test_saturday_deadlines_remain_future(self):
        r=self.audit(); later=[x for x in r['rows'] if x['section'] in ('Saturday afternoon','Saturday evening/night')]
        self.assertEqual(len(later),31)
        self.assertTrue(all(x['default_deadline_status']=='DEFAULT_TIME_FUTURE' for x in later))

    def test_timezone_required(self):
        with self.assertRaises(ValueError): self.audit(t=datetime(2026,10,9))

    def test_authority_required(self):
        with self.assertRaises(ValueError): self.audit(c='synthetic missing cadence')

    def test_duplicate_slate_rejected(self):
        row=next(x for x in self.s.splitlines() if x.startswith('| Sat 12:00 PM |'))
        with self.assertRaises(ValueError): self.audit(s=self.s.replace(row,row+'\n'+row))

    def test_wrong_bucket_rejected(self):
        with self.assertRaises(ValueError): self.audit(s=self.s.replace('| Sat 12:00 PM |','| Sat 11:59 AM |'))

    def test_mixed_schema_rejected(self):
        row=next(x for x in self.s.splitlines() if x.startswith('| Sat 12:00 PM |'))
        cells=row.split('|'); altered='|'.join(cells[:-2]+cells[-1:])
        with self.assertRaises(ValueError): self.audit(s=self.s.replace(row,altered))

if __name__=='__main__':unittest.main()
