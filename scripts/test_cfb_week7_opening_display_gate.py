import re, subprocess, unittest
from pathlib import Path
import cfb_week7_opening_display_gate as gate
ROOT=Path(__file__).resolve().parents[1]
SHEET='evidence/operational/CFB_WEEK7_HOT_SHEET_2026-10-11_0708CT.md'
def snapshot(path,sha):
    raw=(ROOT/path).read_bytes().decode()
    if gate.blob(raw)==sha:return raw
    objects=subprocess.run(['git','rev-list','--objects','--all','--',path],check=True,capture_output=True,text=True).stdout.splitlines()
    if sha+' '+path not in objects:raise ValueError('historical source not recovered at canonical path')
    return subprocess.run(['git','cat-file','blob',sha],check=True,capture_output=True).stdout.decode()
class OpeningTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sheet=(ROOT/SHEET).read_bytes().decode()
        market,decision=re.findall(r'^Canonical inputs: market ([0-9a-f]{40}); decision ([0-9a-f]{40})\.$',cls.sheet,re.M)[0]
        cls.market=snapshot('evidence/operational/CFB_MARKET_MONITOR_STATE.md',market)
        cls.decision=snapshot('evidence/operational/CFB_DECISION_WAIT_LEDGER.md',decision)
    def check(self,sheet=None,market=None,decision=None):
        return gate.audit(self.sheet if sheet is None else sheet,self.market if market is None else market,self.decision if decision is None else decision)
    def test_real(self):self.assertEqual(self.check()['games'],62)
    def test_duplicate(self):
        row=next(l for l in self.sheet.splitlines() if l.startswith('| Tue Oct'))
        with self.assertRaises(ValueError):self.check(self.sheet.replace(row,row+'\n'+row))
    def test_missing(self):
        row=next(l for l in self.sheet.splitlines() if l.startswith('| Tue Oct'))
        with self.assertRaises(ValueError):self.check(self.sheet.replace(row,''))
    def test_invented_prediction(self):
        with self.assertRaises(ValueError):self.check(self.sheet.replace('NOT YET EARNED — Week 7 Monday readiness pending; Tuesday candidate is not acceptance','Delaware -8 / 52 / .8',1))
    def test_invented_action(self):
        with self.assertRaises(ValueError):self.check(self.sheet.replace('INCONCLUSIVE — pre-freeze opening capture','BET NOW',1))
    def test_wrong_quote(self):
        with self.assertRaises(ValueError):self.check(self.sheet.replace('Delaware -1.5 -115','Delaware -2.5 -115',1))
    def test_false_consensus(self):
        with self.assertRaises(ValueError):self.check(self.sheet.replace('CONSENSUS_UNAVAILABLE; Caesars UNVERIFIED; CBS mixed-book fallback 07:08 CT — Delaware','CONSENSUS_VERIFIED; Caesars UNVERIFIED; CBS mixed-book fallback 07:08 CT — Delaware',1))
    def test_changed_deadline(self):
        with self.assertRaises(ValueError):self.check(self.sheet.replace('Tue Oct 13 1:00 PM CT; final cutoff','Tue Oct 13 2:00 PM CT; final cutoff',1))
    def test_changed_cutoff(self):
        with self.assertRaises(ValueError):self.check(self.sheet.replace('final cutoff Tue Oct 13 5:00 PM CT','final cutoff Tue Oct 13 6:00 PM CT',1))
    def test_invented_execution(self):
        with self.assertRaises(ValueError):self.check(self.sheet.replace('Not established; no execution before accepted frozen prediction and qualified offer','Bet $5',1))
    def test_unavailable_market_preserved(self):
        with self.assertRaises(ValueError):self.check(self.sheet.replace('No qualified observation; CBS showed no market','First qualified observation; movement 0',1))
    def test_source_open_not_observation(self):
        with self.assertRaises(ValueError):self.check(self.sheet.replace('Source-displayed Open reference:','Observed earlier quote:',1))
    def test_wrong_section(self):
        with self.assertRaises(ValueError):self.check(self.sheet.replace('## TUESDAY','## FRIDAY',1))
    def test_wrong_source(self):
        with self.assertRaises(ValueError):self.check(market=self.market+'\n')
    def test_unknown_later_source(self):
        d=self.decision+'\n## Later decisions\n';s=self.sheet.replace(gate.blob(self.decision),gate.blob(d))
        with self.assertRaisesRegex(ValueError,'qualification'):self.check(s,decision=d)
    def test_unknown_phase(self):
        with self.assertRaises(ValueError):self.check(self.sheet.replace('OPENING-BOARD CAPTURE / PRE-FREEZE','LIVE FROZEN',1))
if __name__=='__main__':unittest.main()
