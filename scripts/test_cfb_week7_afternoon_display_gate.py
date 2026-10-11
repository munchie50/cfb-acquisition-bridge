import unittest
from pathlib import Path
import cfb_week7_afternoon_display_gate as gate
from test_cfb_week7_opening_display_gate import snapshot
ROOT=Path(__file__).resolve().parents[1]
SHEET='evidence/operational/CFB_WEEK7_HOT_SHEET_2026-10-11_1305CT.md'
class AfternoonTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s=(ROOT/SHEET).read_bytes().decode()
        cls.m=snapshot('evidence/operational/CFB_MARKET_MONITOR_STATE.md','3d4aa26b8ca2c5ff9bad1e3b5545d41ebfd64c0a')
        cls.d=snapshot('evidence/operational/CFB_DECISION_WAIT_LEDGER.md','4a525667b6ecfbeaf6e74222d18640e91e5d35f2')
        cls.om=snapshot('evidence/operational/CFB_MARKET_MONITOR_STATE.md',gate.OLD_MARKET)
        cls.od=snapshot('evidence/operational/CFB_DECISION_WAIT_LEDGER.md',gate.OLD_DECISION)
        cls.e=snapshot('evidence/operational/CFB_EXECUTION_LEDGER.md','75caee4052e02ea7d2453d1d37fd3866e13ecc07')
        cls.p=snapshot('evidence/operational/CFB_POSTGAME_FIRST_FROZEN_SCORECARD.md','6f7650d340bf63f8f93a2b825e35f8b8e41fa80b')
    def check(self,s=None,m=None,d=None,om=None,e=None,p=None):
        return gate.audit(self.s if s is None else s,self.m if m is None else m,self.d if d is None else d,
                          self.om if om is None else om,self.od,self.e if e is None else e,self.p if p is None else p)
    def reject(self,s):
        with self.assertRaises(ValueError):self.check(s)
    def row(self,g):return next(l for l in self.s.splitlines() if l.startswith('| ') and len(gate.opening.cells(l))==9 and gate.opening.cells(l)[1]==g)
    def alter(self,g,n,value):
        row=self.row(g);r=gate.opening.cells(row);r[n]=value
        return self.s.replace(row,'| '+' | '.join(r)+' |',1)
    def test_actual(self):
        r=self.check();self.assertEqual((r['games'],r['first_price_observations'],r['changed_existing_quotes']),(62,28,34))
    def test_missing_game(self):self.reject(self.s.replace(self.row('Nebraska @ Oregon'),''))
    def test_duplicate_game(self):
        r=self.row('Delaware @ Middle Tenn.');self.reject(self.s.replace(r,r+'\n'+r))
    def test_invented_model(self):self.reject(self.alter('Delaware @ Middle Tenn.',2,'Delaware -9 / 52 / .8'))
    def test_false_action(self):self.reject(self.alter('Delaware @ Middle Tenn.',5,'BET NOW'))
    def test_stale_quote(self):self.reject(self.alter('Delaware @ Middle Tenn.',3,'Old quote'))
    def test_false_consensus(self):self.reject(self.s.replace('CONSENSUS_UNAVAILABLE; Caesars UNVERIFIED; CBS mixed-book fallback 13:05 CT — Delaware','CONSENSUS_VERIFIED; Caesars UNVERIFIED; CBS mixed-book fallback 13:05 CT — Delaware',1))
    def test_first_observation_backfill(self):self.reject(self.alter('East Carolina @ UAB',4,'07:08 CT first: East Carolina -5.5 -110'))
    def test_wrong_first_quote(self):self.reject(self.alter('Delaware @ Middle Tenn.',4,gate.opening.cells(self.row('Delaware @ Middle Tenn.'))[4].replace('-1.5 -115','-2.5 -115')))
    def test_wrong_current_movement(self):self.reject(self.alter('Delaware @ Middle Tenn.',4,gate.opening.cells(self.row('Delaware @ Middle Tenn.'))[4].replace('-2.5 -110','-3.5 -110')))
    def test_wrong_nebraska_kickoff(self):self.reject(self.alter('Nebraska @ Oregon',0,'Sat Oct 17 2:00 PM CT'))
    def test_nebraska_wrong_section(self):self.reject(self.s.replace('## SATURDAY EVENING/NIGHT','## SATURDAY AFTERNOON',1))
    def test_wrong_deadline(self):self.reject(self.alter('Nebraska @ Oregon',7,'Sat Oct 17 2:00 PM CT; final cutoff Sat Oct 17 9:00 PM CT'))
    def test_wrong_cutoff(self):self.reject(self.alter('Nebraska @ Oregon',7,'Sat Oct 17 1:00 PM CT; final cutoff Sat Oct 17 10:00 PM CT'))
    def test_invented_execution(self):self.reject(self.alter('Nebraska @ Oregon',8,'Bet $5'))
    def test_pending_qualifier(self):self.reject(self.alter('Nebraska @ Oregon',6,'Ready'))
    def test_original_market_rewrite(self):
        m=self.m.replace('Delaware -1.5 -115','Delaware -1.5 -110',1);s=self.s.replace(gate.blob(self.m),gate.blob(m))
        with self.assertRaisesRegex(ValueError,'rewritten'):self.check(s,m=m)
    def test_stale_execution(self):
        with self.assertRaises(ValueError):self.check(e=self.e+'\n')
    def test_stale_scorecard(self):
        with self.assertRaises(ValueError):self.check(p=self.p+'\n')
    def test_original_identity_change(self):
        with self.assertRaises(ValueError):self.check(om=self.om+'\n')
    def test_unknown_later_boundary(self):
        m=self.m+'\n## Later market\n';s=self.s.replace(gate.blob(self.m),gate.blob(m))
        with self.assertRaisesRegex(ValueError,'qualification'):self.check(s,m=m)
    def test_unknown_phase(self):self.reject(self.s.replace('AFTERNOON MARKET REFRESH / PRE-FREEZE','LATER LIVE',1))
if __name__=='__main__':unittest.main()
