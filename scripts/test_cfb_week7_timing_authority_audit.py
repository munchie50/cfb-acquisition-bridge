import unittest
from pathlib import Path
import cfb_week7_timing_authority_audit as gate
from test_cfb_week7_opening_display_gate import snapshot
ROOT=Path(__file__).resolve().parents[1]
class TimingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s=(ROOT/'evidence/operational/CFB_WEEK7_HOT_SHEET_2026-10-11_1305CT.md').read_bytes().decode()
        cls.l=snapshot('evidence/operational/CFB_DECISION_WAIT_LEDGER.md',gate.LEDGER)
        cls.c=snapshot('evidence/CFB_ENGINE_EARLY_EXPOSURE_AND_LEARNING_CADENCE_CONTROL_v1_237.md',gate.CADENCE)
        cls.p=(ROOT/'evidence/CFB_HOT_SHEET_DETERMINISTIC_KICKOFF_SECTIONING_CONTRACT_2026-09-30.md').read_bytes().decode()
    def check(self,s=None,l=None,c=None,p=None,at='2026-10-11T18:57:10Z'):
        return gate.audit(self.s if s is None else s,self.l if l is None else l,self.c if c is None else c,self.p if p is None else p,at)
    def test_real_findings(self):
        r=self.check();self.assertEqual(r['status'],'TIMING_AUTHORITY_UNRESOLVED_NOT_OPERATIONAL_ACCEPTANCE')
        self.assertEqual(r['counts']['games'],62);self.assertEqual(r['counts']['cutoffs_60_minutes_before_saved_kickoff'],62)
        self.assertEqual(r['counts']['independently_qualified_cutoffs'],0)
    def test_default_matches_not_effective_acceptance(self):
        r=self.check();self.assertEqual(r['counts']['deadline_class']['EXPLICIT_DEFAULT_CLOCK_MATCH_ONLY'],42)
        self.assertTrue(all(x['effective_game_deadline']=='NOT_CERTIFIED' for x in r['rows']))
    def test_earlyweek_not_default_inheritance(self):
        self.assertEqual(self.check()['counts']['deadline_class']['GAME_SPECIFIC_ASSIGNED_NOT_INDEPENDENTLY_QUALIFIED'],4)
    def test_thursday_practical_access_conditional(self):
        self.assertEqual(self.check()['counts']['deadline_class']['DEFAULT_MATCH_CONDITIONAL_ON_PRACTICAL_ACCESS'],3)
    def test_flexible_event_not_guaranteed_completion(self):
        self.assertEqual(self.check()['counts']['deadline_class']['NOMINAL_FLEXIBLE_EVENT_TIME_NOT_COMPLETION_DEADLINE'],13)
    def test_current_no_due_claim(self):self.assertEqual(self.check()['counts']['saved_clock_status'],{'FUTURE':62})
    def test_later_clock_not_false_overdue_acceptance(self):
        r=self.check(at='2026-10-13T18:01:00Z')
        self.assertEqual(r['counts']['saved_clock_status']['SAVED_CLOCK_REACHED_NOT_EFFECTIVE_DEADLINE_CERTIFICATION'],2)
    def test_naive_asof(self):
        with self.assertRaises(ValueError):self.check(at='2026-10-11T13:57:10')
    def test_stale_ledger(self):
        with self.assertRaises(ValueError):self.check(l=self.l+'\n')
    def test_changed_authority(self):
        with self.assertRaises(ValueError):self.check(c=self.c.replace('Saturday 07:00','Saturday 08:00'))
    def test_missing_earlyweek_ancestry(self):
        with self.assertRaises(ValueError):self.check(p='No earlyweek contract')
    def test_unknown_cycle(self):
        with self.assertRaises(ValueError):self.check(s=self.s.replace(gate.CYCLE,'LATER_CYCLE'))
    def test_duplicate_game(self):
        row=next(l for l in self.s.splitlines() if l.startswith('| Tue Oct'));s=self.s.replace(row,row+'\n'+row)
        with self.assertRaises(ValueError):self.check(s)
    def test_missing_game(self):
        row=next(l for l in self.s.splitlines() if l.startswith('| Tue Oct'))
        with self.assertRaises(ValueError):self.check(s=self.s.replace(row,''))
    def test_atkickoff_cutoff_not_practical(self):
        with self.assertRaises(ValueError):self.check(s=self.s.replace('final cutoff Tue Oct 13 5:00 PM CT','final cutoff Tue Oct 13 6:00 PM CT',1))
    def test_clock_weekday(self):
        with self.assertRaises(ValueError):gate.clock('Fri Oct 17 7:30 PM CT')
    def test_invalid_clock_hour(self):
        with self.assertRaises(ValueError):gate.clock('Sat Oct 17 13:30 PM CT')
if __name__=='__main__':unittest.main()
