import os,unittest
from pathlib import Path
import cfb_week7_frozen_field_invariant as gate
ROOT=Path(__file__).resolve().parents[1]
class InvariantTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        local=os.environ.get('CFB_WEEK7_FROZEN_FIXTURE_DIR')
        root=Path(local) if local else ROOT
        cls.s=(root/'current.md').read_text() if local else (ROOT/'evidence/operational/CFB_WEEK7_HOT_SHEET_2026-10-11_1429CT.md').read_text()
        cls.l=(root/'lineage.json').read_text() if local else (ROOT/'evidence/operational/CFB_WEEK7_ORIGINAL_FIRST_FROZEN_LINEAGE_2026-10-11.json').read_text()
        cls.z=Path(os.environ['CFB_ACCEPTED_FREEZE_ARCHIVE'])
    def check(self,s=None,l=None):return gate.audit(self.s if s is None else s,self.z,self.l if l is None else l)
    def row(self,g):return next(l for l in self.s.splitlines() if l.startswith('| ') and len(l.split('|'))==11 and l.split('|')[2].strip()==g)
    def alter(self,g,n,value):
        line=self.row(g);c=[v.strip() for v in line.split('|')[1:-1]];c[n]=value
        return self.s.replace(line,'| '+' | '.join(c)+' |',1)
    def reject(self,s):
        with self.assertRaises(ValueError):self.check(s)
    def test_actual(self):self.assertEqual((self.check()['numeric_fields'],self.check()['exclusions']),(153,11))
    def test_scope_explicit(self):self.assertEqual(self.check()['verdict'],'PASS_ORIGINAL_FROZEN_FIELDS_ONLY')
    def test_title_change_not_model_change(self):self.assertEqual(self.check(self.s.replace(self.s.splitlines()[0],'# DIAGNOSTIC LABEL — not a publication'))['predictions'],51)
    def test_cycle_change_not_model_change(self):self.check(self.s.replace('CFB_MARKET_MONITOR_20261011T180208Z','DIAGNOSTIC_CYCLE_NOT_ACCEPTED'))
    def test_absent_prediction(self):self.reject(self.alter('Delaware @ Middle Tenn.',2,'NOT YET EARNED'))
    def test_wrong_spread(self):self.reject(self.alter('Delaware @ Middle Tenn.',2,'FIRST_FROZEN: Middle Tennessee -9.8 / 50.6 / 0.530 home'))
    def test_wrong_total(self):self.reject(self.alter('Delaware @ Middle Tenn.',2,'FIRST_FROZEN: Middle Tennessee -1.8 / 90.6 / 0.530 home'))
    def test_wrong_probability(self):self.reject(self.alter('Delaware @ Middle Tenn.',2,'FIRST_FROZEN: Middle Tennessee -1.8 / 50.6 / 0.930 home'))
    def test_wrong_favorite(self):self.reject(self.alter('Delaware @ Middle Tenn.',2,'FIRST_FROZEN: Delaware -1.8 / 50.6 / 0.530 home'))
    def test_refresh_substitution(self):self.reject(self.alter('East Carolina @ UAB',2,'REFRESH PREDICTION'))
    def test_exclusion_reason_lost(self):self.reject(self.alter('Elon @ Stanford',2,'FIRST_FROZEN EXCLUDED'))
    def test_exclusion_no_substitution_lost(self):self.reject(self.s.replace('(not substituted)','(substituted)',1))
    def test_duplicate(self):
        r=self.row('Elon @ Stanford');self.reject(self.s.replace(r,r+'\n'+r))
    def test_missing(self):self.reject(self.s.replace(self.row('Elon @ Stanford'),''))
    def test_wrong_directed_pair(self):self.reject(self.alter('Delaware @ Middle Tenn.',1,'Middle Tenn. @ Delaware'))
    def test_unknown_name(self):self.reject(self.alter('Delaware @ Middle Tenn.',1,'Unknown @ Middle Tenn.'))
    def test_unknown_schema(self):self.reject(self.s.replace(self.row('Delaware @ Middle Tenn.'),self.row('Delaware @ Middle Tenn.')+' extra |'))
    def test_wrong_census(self):
        with self.assertRaises(ValueError):self.check(l=self.l+'\n')
    def test_cutoff_declaration(self):self.reject(self.s.replace(gate.CUTOFF,'2026-10-06T15:11:29Z',1))
    def test_duplicate_model_boundary(self):self.reject(self.s+'\n'+next(l for l in self.s.splitlines() if l.startswith('**Frozen-model boundary:**'))+'\n')
    def test_unresolved_clock_can_preserve_frozen_values(self):self.check(self.alter('Delaware @ Middle Tenn.',0,'UNRESOLVED kickoff — no source qualification'))
    def test_summary_is_not_a_governed_game(self):self.check(self.s.replace('| UNRESOLVED KICKOFF | 0 |','| UNRESOLVED KICKOFF | 7 |'))
    def test_summary_shape_cannot_hide_missing_game(self):self.reject(self.s.replace(self.row('Delaware @ Middle Tenn.'),'| UNRESOLVED KICKOFF | 0 |'))
    def full_check(self,s):
        import cfb_week7_first_frozen_projection_gate as full
        base=Path(os.environ.get('CFB_WEEK7_PREDECESSOR_FIXTURE_ROOT',ROOT))
        parent=(base/'evidence/operational/CFB_WEEK7_HOT_SHEET_2026-10-11_1305CT.md').read_text()
        if 'CFB_WEEK7_PREDECESSOR_FIXTURE_ROOT' in os.environ:
            prior=(base/'evidence/operational/CFB_DECISION_WAIT_LEDGER.md').read_text()
        else:
            from test_cfb_week7_opening_display_gate import snapshot
            prior=snapshot('evidence/operational/CFB_DECISION_WAIT_LEDGER.md',full.DECISION_SHA)
        rows=full.inventory(self.z,Path(os.environ['CFB_ACCEPTED_REFRESH_ARCHIVE']),parent)
        decision,_=full.project(parent,prior,rows)
        return full.audit(s,parent,decision,prior,self.z,Path(os.environ['CFB_ACCEPTED_REFRESH_ARCHIVE']))
    def test_new_title_frozen_pass_full_profile_reject(self):
        s=self.s.replace(self.s.splitlines()[0],'# DIAGNOSTIC LABEL — not a publication');self.check(s)
        with self.assertRaises(ValueError):self.full_check(s)
    def test_unqualified_market_not_certified(self):
        s=self.alter('Delaware @ Middle Tenn.',3,'DIAGNOSTIC_UNQUALIFIED_PRICE');self.check(s)
        with self.assertRaises(ValueError):self.full_check(s)
    def test_decision_not_certified(self):
        s=self.alter('Delaware @ Middle Tenn.',5,'DIAGNOSTIC_UNEARNED_ACTION');self.check(s)
        with self.assertRaises(ValueError):self.full_check(s)
if __name__=='__main__':unittest.main()
