import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import cfb_week6_market_total_display_gate as gate

ROOT = Path(__file__).resolve().parents[1] if Path(__file__).parent.name == 'scripts' else Path(__file__).parent
CURRENT = ROOT/'evidence/operational/CFB_WEEK6_HOT_SHEET_2026-10-09_1538CT.md'
ORIGINAL = ROOT/'evidence/operational/CFB_WEEK6_HOT_SHEET_2026-10-09_1301CT.md'

class DisplayTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sheet = CURRENT.read_text()
        cls.original = ORIGINAL.read_text()
        fixture = ROOT/'total_market_fixture.md'
        cls.market = fixture.read_text() if fixture.exists() else gate.recovered_market(gate.declared_market(cls.sheet))

    def test_current_real_sheet(self):
        r = gate.audit(self.sheet, self.market)
        self.assertEqual((r['matched_modeled_total_displays'],r['matched_unmodeled_total_displays'],r['uncovered_earlier_week_modeled_rows']), (43,1,6))

    def test_original_real_bad_endpoint(self):
        with self.assertRaisesRegex(ValueError,'unsupported or omitted total endpoint'):
            gate.audit(self.original, self.market)

    def test_asymmetric_pair_not_collapsed(self):
        with self.assertRaisesRegex(ValueError,'unsupported or omitted total endpoint'):
            gate.audit(self.sheet.replace('totals 53.5/54.5','total 54.5'), self.market)

    def test_extra_endpoint(self):
        with self.assertRaisesRegex(ValueError,'unsupported or omitted total endpoint'):
            gate.audit(self.sheet.replace('totals 53.5/54.5','totals 53.5/54.5/55.5'), self.market)

    def test_wrong_declared_source(self):
        with self.assertRaisesRegex(ValueError,'declared market blob'):
            gate.audit(self.sheet, self.market+'\n')

    def test_missing_source_reference(self):
        with self.assertRaisesRegex(ValueError,'source binding'):
            gate.audit(self.sheet.replace('Canonical inputs: market','Missing inputs: market'),self.market)

    def test_unknown_future_cycle(self):
        with self.assertRaisesRegex(ValueError,'source binding'):
            gate.audit(self.sheet.replace(gate.CYCLE, 'CFB_MARKET_MONITOR_20261010T120000Z'),self.market)

    def test_duplicate_source_quote(self):
        market=self.market+'\n- Arizona @ West Virginia: Arizona -3; total 61.5.\n'
        sheet=self.sheet.replace(gate.blob(self.market),gate.blob(market))
        with self.assertRaisesRegex(ValueError,'duplicate canonical'):
            gate.audit(sheet,market)

    def test_duplicate_display(self):
        line=next(l for l in self.sheet.splitlines() if l.startswith('| Fri 8:00 PM | Iowa @'))
        with self.assertRaisesRegex(ValueError,'duplicate displayed'):
            gate.audit(self.sheet+'\n'+line+'\n',self.market)

    def test_missing_nebraska(self):
        sheet='\n'.join(l for l in self.sheet.splitlines() if not l.startswith('Indiana @ Nebraska — '))
        with self.assertRaisesRegex(ValueError,'Nebraska'):
            gate.audit(sheet,self.market)

    def test_odds_not_total_endpoints(self):
        self.assertEqual(gate.totals('total 53.5/54.5 (Over -112 / Under -110)'),gate.totals('totals 53.5–54.5'))
        self.assertEqual(gate.totals('displayed totals A o59.5 (-112), B u60.5 (-115). First observation 58.5.'),frozenset([gate.Decimal('59.5'),gate.Decimal('60.5')]))

    def test_duplicate_or_missing_total_fails(self):
        for text in ['totals 53.5/53.5','total UNAVAILABLE','total 53.5; total 54.5']:
            with self.assertRaises(ValueError): gate.totals(text)

    def test_historical_source_resolved_after_later_append(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            def git(*args):
                return subprocess.run(['git','-C',str(root),*args],check=True,capture_output=True,text=True).stdout
            git('init','-q');git('config','user.email','test@example.invalid');git('config','user.name','QA')
            p=root/gate.MARKET_PATH;p.parent.mkdir(parents=True);p.write_text(self.market)
            git('add','.');git('commit','-qm','actual retained canonical fixture')
            p.write_text(self.market+'\nLater independent observation.\n');git('add','.');git('commit','-qm','later append')
            original_run=subprocess.run
            def scoped(args,**kwargs):
                return original_run(args,cwd=root,**kwargs)
            with patch.object(gate.subprocess,'run',side_effect=scoped):
                recovered=gate.recovered_market(gate.declared_market(self.sheet))
            self.assertEqual(recovered,self.market)
            self.assertEqual(gate.audit(self.sheet,recovered)['matched_modeled_total_displays'],43)

    def test_noncanonical_blob_path_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            def git(*args): return subprocess.run(['git','-C',str(root),*args],check=True,capture_output=True,text=True).stdout
            git('init','-q');git('config','user.email','test@example.invalid');git('config','user.name','QA')
            (root/'other.md').write_text(self.market);git('add','.');git('commit','-qm','noncanonical fixture')
            original_run=subprocess.run
            with patch.object(gate.subprocess,'run',side_effect=lambda args,**kwargs:original_run(args,cwd=root,**kwargs)):
                with self.assertRaisesRegex(ValueError,'canonical market path'):
                    gate.recovered_market(gate.blob(self.market))

if __name__=='__main__': unittest.main()
