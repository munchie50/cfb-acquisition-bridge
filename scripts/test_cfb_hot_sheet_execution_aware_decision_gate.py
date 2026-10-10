import unittest
from pathlib import Path
import cfb_hot_sheet_execution_aware_decision_gate as gate

ROOT=Path(__file__).resolve().parents[1]
SHEET='evidence/operational/CFB_WEEK6_HOT_SHEET_2026-10-10_1312CT.md'
DECISION='evidence/operational/CFB_DECISION_WAIT_LEDGER.md'
EXECUTION='evidence/operational/CFB_EXECUTION_LEDGER.md'
BASELINE='evidence/operational/CFB_WEEK6_HOT_SHEET_2026-10-09_1538CT.md'

class ExecutionProjectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sheet=(ROOT/SHEET).read_bytes().decode()
        cls.decision=(ROOT/DECISION).read_bytes().decode()
        cls.execution=(ROOT/EXECUTION).read_bytes().decode()
        cls.baseline=(ROOT/BASELINE).read_bytes().decode()
    def check(self, sheet=None, decision=None, execution=None):
        return gate.audit(self.sheet if sheet is None else sheet, self.baseline,
                          self.decision if decision is None else decision,
                          self.execution if execution is None else execution)
    def row(self,game):
        return next(l for l in self.sheet.splitlines() if l.startswith('| Sat') and gate.cells(l)[1]==game)
    def alter(self,game,column,value):
        row=self.row(game); cols=gate.cells(row); cols[column]=value
        return self.sheet.replace(row,'| '+' | '.join(cols)+' |')
    def test_actual_current(self):
        r=self.check()
        self.assertEqual((r['matched_games'],r['matched_market_verdicts'],r['actual_tickets'],r['stake_usd']),(38,76,4,20))
    def test_jmu_cannot_be_retroactively_recommended(self):
        with self.assertRaisesRegex(ValueError,'prospective PASS'):
            self.check(self.alter('James Madison @ Georgia Southern',5,'BET NOW CONDITIONAL — EXECUTED / TOTAL PASS'))
    def test_completed_fresno_cannot_be_reopened(self):
        with self.assertRaisesRegex(ValueError,'reopened'):
            self.check(self.alter('Boise State @ Fresno State',5,'BET NOW CONDITIONAL / TOTAL PASS'))
    def test_completed_app_cannot_gain_new_execution_window(self):
        with self.assertRaisesRegex(ValueError,'reopened'):
            self.check(self.alter('Old Dominion @ App State',8,'Bet another $5 tonight'))
    def test_ordinary_pass_cannot_be_changed(self):
        with self.assertRaisesRegex(ValueError,'disposition changed'):
            self.check(self.alter('Texas vs Oklahoma',5,'BET NOW / TOTAL PASS'))
    def test_total_pass_cannot_be_changed(self):
        with self.assertRaises(ValueError):self.check(self.alter('UCLA @ Oregon',5,'PASS / TOTAL BET NOW'))
    def test_wait_cannot_return(self):
        with self.assertRaises(ValueError):self.check(self.alter('UCLA @ Oregon',5,'WAIT / TOTAL PASS'))
    def test_wrong_ticket_price_rejected(self):
        row=self.row('Boise State @ Fresno State')
        with self.assertRaisesRegex(ValueError,'execution facts'):
            self.check(self.sheet.replace(row,row.replace('Fresno +7 (-113), $5','Fresno +7 (-110), $5')))
    def test_wrong_ticket_line_rejected(self):
        row=self.row('James Madison @ Georgia Southern')
        with self.assertRaisesRegex(ValueError,'execution facts'):
            self.check(self.sheet.replace(row,row.replace('JMU -7.5 (-107), $5','JMU -8 (-107), $5')))
    def test_missing_actual_qualifier_rejected(self):
        row=self.row('Old Dominion @ App State')
        with self.assertRaisesRegex(ValueError,'execution facts'):
            self.check(self.sheet.replace(row,row.replace('actual Caesars execution','current Caesars offer')))
    def test_missing_jmu_pass_qualifier(self):
        with self.assertRaisesRegex(ValueError,'prospective PASS'):
            self.check(self.alter('James Madison @ Georgia Southern',6,'Recommendation confirmed'))
    def test_stale_execution_binding(self):
        with self.assertRaisesRegex(ValueError,'binding'):
            self.check(execution=self.execution+'\n')
    def test_stale_decision_binding(self):
        with self.assertRaisesRegex(ValueError,'binding'):
            self.check(decision=self.decision+'\n')
    def test_duplicate_ticket(self):
        row=next(l for l in self.execution.splitlines() if l.startswith('| CFB_OCT09-01'))
        execution=self.execution+'\n'+row+'\n'
        sheet=self.sheet.replace(gate.blob(self.execution),gate.blob(execution))
        with self.assertRaisesRegex(ValueError,'duplicate current ticket'):self.check(sheet,execution=execution)
    def test_missing_ticket(self):
        row=next(l for l in self.execution.splitlines() if l.startswith('| CFB_OCT09-04'))
        execution=self.execution.replace(row,'')
        sheet=self.sheet.replace(gate.blob(self.execution),gate.blob(execution))
        with self.assertRaisesRegex(ValueError,'four established'):self.check(sheet,execution=execution)
    def test_unknown_new_cycle(self):
        with self.assertRaisesRegex(ValueError,'unsupported'):
            self.check(self.sheet.replace(gate.CYCLE,'CFB_MARKET_MONITOR_NEW'))
    def test_later_decision_block_requires_qualification(self):
        decision=self.decision+'\n## Later state\n'
        sheet=self.sheet.replace(gate.blob(self.decision),gate.blob(decision))
        with self.assertRaisesRegex(ValueError,'requires qualification'):self.check(sheet,decision=decision)
    def test_missing_saturday_game(self):
        with self.assertRaisesRegex(ValueError,'identity'):
            self.check(self.sheet.replace(self.row('Texas vs Oklahoma'),''))
    def test_duplicate_saturday_game(self):
        with self.assertRaisesRegex(ValueError,'identity'):
            self.check(self.sheet+'\n'+self.row('Texas vs Oklahoma')+'\n')
    def test_wrong_summary_exposure(self):
        with self.assertRaisesRegex(ValueError,'summary'):
            self.check(self.sheet.replace('Four established October 9 tickets total $20','Four established October 9 tickets total $25'))

if __name__=='__main__':unittest.main()
