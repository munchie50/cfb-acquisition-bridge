import unittest
from pathlib import Path
import cfb_week6_market_total_display_gate as gate

ROOT = Path(__file__).resolve().parents[1]

class AfternoonTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sheet = (ROOT/'evidence/operational/CFB_WEEK6_HOT_SHEET_2026-10-10_1312CT.md').read_bytes().decode()
        fixture = ROOT/'afternoon_market_fixture.md'
        cls.market = fixture.read_bytes().decode() if fixture.exists() else gate.recovered_market(gate.declared_market(cls.sheet))
    def test_actual_afternoon_partition(self):
        r = gate.audit(self.sheet, self.market)
        self.assertEqual((r['matched_modeled_total_displays'], r['fresh_total_displays'], r['retained_total_displays']), (38, 28, 10))
        self.assertEqual(r['nebraska_quote'], 'WITHHELD_NOT_NUMERICALLY_CERTIFIED')
    def test_fresh_asymmetric_pair_cannot_collapse(self):
        with self.assertRaisesRegex(ValueError, 'omitted total'):
            gate.audit(self.sheet.replace('total 39.5/41.5', 'total 41.5'), self.market)
    def test_retained_pair_cannot_collapse(self):
        with self.assertRaisesRegex(ValueError, 'omitted total'):
            gate.audit(self.sheet.replace('total 60.5/61.5', 'total 61.5'), self.market)
    def test_wrong_fresh_value(self):
        with self.assertRaises(ValueError):
            gate.audit(self.sheet.replace('total 39.5/41.5', 'total 40.5/41.5'), self.market)
    def test_retained_quote_cannot_be_relabelled_fresh(self):
        with self.assertRaisesRegex(ValueError, 'partition'):
            gate.audit(self.sheet.replace('retained pregame fallback:', 'CBS mixed-book fallback ~13:03 CT:', 1), self.market)
    def test_fresh_quote_cannot_be_relabelled_retained(self):
        with self.assertRaisesRegex(ValueError, 'partition'):
            gate.audit(self.sheet.replace('CBS mixed-book fallback ~13:03 CT:', 'retained pregame fallback:', 1), self.market)
    def test_missing_retained_qualifier(self):
        with self.assertRaisesRegex(ValueError, 'partition'):
            gate.audit(self.sheet.replace('no later pregame quote promoted', 'quote refreshed', 1), self.market)
    def test_source_bytes_must_match(self):
        with self.assertRaisesRegex(ValueError, 'declared market blob'):
            gate.audit(self.sheet, self.market+'\n')
    def test_wrong_canonical_cycle(self):
        market=self.market.replace('Run: '+gate.AFTERNOON_CYCLE+'.', 'Run: WRONG.')
        sheet=self.sheet.replace(gate.blob(self.market), gate.blob(market))
        with self.assertRaisesRegex(ValueError, 'cycle mismatch'):gate.audit(sheet, market)
    def test_unknown_cycle(self):
        with self.assertRaisesRegex(ValueError, 'source binding'):
            gate.audit(self.sheet.replace(gate.AFTERNOON_CYCLE, 'CFB_MARKET_MONITOR_UNKNOWN'), self.market)
    def test_duplicate_saturday_row(self):
        row=next(l for l in self.sheet.splitlines() if l.startswith('| Sat'))
        with self.assertRaisesRegex(ValueError, 'duplicate displayed'):
            gate.audit(self.sheet+'\n'+row+'\n', self.market)
    def test_missing_saturday_row(self):
        row=next(l for l in self.sheet.splitlines() if l.startswith('| Sat'))
        with self.assertRaisesRegex(ValueError, 'identity union'):
            gate.audit(self.sheet.replace(row, ''), self.market)
    def test_nebraska_withholding_is_required(self):
        with self.assertRaisesRegex(ValueError, 'Nebraska'):
            gate.audit(self.sheet.replace('no later displayed number is promoted as pregame evidence', 'current quote'), self.market)
    def test_nebraska_numeric_claim_not_silently_certified(self):
        with self.assertRaisesRegex(ValueError, 'numeric Nebraska'):
            gate.audit(self.sheet.replace('Retained public fallback remains historical.', 'Retained public fallback remains historical; total 47.5.'), self.market)

if __name__ == '__main__': unittest.main()
