import unittest
from pathlib import Path
import cfb_week6_market_total_display_gate as gate

ROOT=Path(__file__).resolve().parents[1]

class SaturdayTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sheet=(ROOT/'evidence/operational/CFB_WEEK6_HOT_SHEET_2026-10-10_0708CT.md').read_bytes().decode()
        fixture=ROOT/'saturday_market_fixture.md'
        cls.market=fixture.read_bytes().decode() if fixture.exists() else gate.recovered_market(gate.declared_market(cls.sheet))
    def test_real_saturday(self):
        result=gate.audit(self.sheet,self.market)
        self.assertEqual((result['matched_modeled_total_displays'],result['matched_unmodeled_total_displays'],result['uncovered_earlier_week_modeled_rows']),(38,1,11))
    def test_collapsed_asymmetric_pair(self):
        with self.assertRaisesRegex(ValueError,'unsupported or omitted total endpoint'):
            gate.audit(self.sheet.replace('total 60.5/61.5','total 61.5'),self.market)
    def test_wrong_total(self):
        with self.assertRaisesRegex(ValueError,'unsupported or omitted total endpoint'):
            gate.audit(self.sheet.replace('total 60.5/61.5','total 59.5/61.5'),self.market)
    def test_copied_friday_total_not_accepted(self):
        with self.assertRaisesRegex(ValueError,'unsupported or omitted total endpoint'):
            gate.audit(self.sheet.replace('total 49.5','total 48.5',1),self.market)
    def test_wrong_source_bytes(self):
        with self.assertRaisesRegex(ValueError,'declared market blob'):
            gate.audit(self.sheet,self.market+'\n')
    def test_unknown_future_cycle(self):
        with self.assertRaisesRegex(ValueError,'source binding'):
            gate.audit(self.sheet.replace('CFB_MARKET_MONITOR_20261010T120036Z','CFB_MARKET_MONITOR_20261010T180000Z'),self.market)
    def test_wrong_canonical_cycle(self):
        market=self.market.replace('Run: CFB_MARKET_MONITOR_20261010T120036Z.','Run: WRONG_CYCLE.')
        sheet=self.sheet.replace(gate.blob(self.market),gate.blob(market))
        with self.assertRaisesRegex(ValueError,'cycle mismatch'):gate.audit(sheet,market)
    def test_nebraska_pair_not_collapsed(self):
        line=next(l for l in self.sheet.splitlines() if l.startswith('Indiana @ Nebraska — '))
        with self.assertRaisesRegex(ValueError,'unsupported or omitted total endpoint'):
            gate.audit(self.sheet.replace(line,line.replace('total 47.5/48.5','total 48.5')),self.market)

if __name__=='__main__':unittest.main()
