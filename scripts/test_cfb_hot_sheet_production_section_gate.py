import unittest
from pathlib import Path
import cfb_hot_sheet_production_section_gate as gate

class ProductionSectionGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.reference = Path('evidence/operational/CFB_WEEK6_HOT_SHEET_RESEARCH_CANDIDATE_2026-10-07.md').read_text()
        cls.sheet = Path('evidence/operational/CFB_WEEK6_HOT_SHEET_2026-10-09_1538CT.md').read_text()
        cls.expected = gate.reference_ids(cls.reference)

    def check_rejected(self, sheet):
        with self.assertRaises(ValueError): gate.validate(sheet,self.expected)

    def test_real_sheet(self):
        r=gate.validate(self.sheet,self.expected)
        self.assertEqual(r['modeled'],49)
        self.assertEqual(sum(r['counts'].values()),49)

    def test_missing_game(self):
        self.check_rejected('\n'.join(l for l in self.sheet.splitlines() if not l.startswith('| Sat 12:00 PM |')))

    def test_duplicate_game(self):
        row=next(l for l in self.sheet.splitlines() if l.startswith('| Sat 12:00 PM |'))
        self.check_rejected(self.sheet.replace(row,row+'\n'+row))

    def test_substituted_game_same_count(self):
        self.check_rejected(self.sheet.replace('Old Dominion @ App State','Unknown @ App State'))

    def test_wrong_section(self):
        self.check_rejected(self.sheet.replace('| Sat 12:00 PM |','| Sat 11:59 AM |'))

    def test_noon_belongs_afternoon(self):
        gate.validate(self.sheet,self.expected)

    def test_five_pm_belongs_evening(self):
        self.check_rejected(self.sheet.replace('| Sat 5:00 PM |','| Sat 4:59 PM |'))

    def test_invalid_hour(self):
        self.check_rejected(self.sheet.replace('| Sat 12:00 PM |','| Sat 13:00 PM |'))

    def test_invalid_minute(self):
        self.check_rejected(self.sheet.replace('| Sat 12:00 PM |','| Sat 12:60 PM |'))

    def test_bad_day(self):
        self.check_rejected(self.sheet.replace('| Sat 12:00 PM |','| Sun 12:00 PM |'))

    def test_duplicate_section(self):
        self.check_rejected(self.sheet.replace('### SATURDAY MORNING','### SATURDAY MORNING\n### SATURDAY MORNING'))

    def test_unresolved_preserves_identity(self):
        row=next(l for l in self.sheet.splitlines() if l.startswith('| Sat 12:00 PM |'))
        s=self.sheet.replace(row,'')+'\n### UNRESOLVED KICKOFF\n'+row.replace('Sat 12:00 PM','UNRESOLVED')
        self.assertEqual(gate.validate(s,self.expected)['counts']['UNRESOLVED KICKOFF'],1)

    def test_unresolved_in_wrong_bucket(self):
        self.check_rejected(self.sheet.replace('| Sat 12:00 PM |','| UNRESOLVED |'))

    def test_nebraska_missing(self):
        self.check_rejected(self.sheet.replace('Indiana @ Nebraska','Indiana @ Another Team'))

    def test_reference_rewrite(self):
        with self.assertRaises(ValueError): gate.reference_ids(self.reference+'\n')

    def test_unsectioned_game(self):
        self.check_rejected(self.sheet.replace('### SATURDAY AFTERNOON','### OTHER'))

    def test_fiu_alias(self):
        self.assertEqual(gate.identity('New Mexico State @ FIU'),gate.identity('New Mexico State @ Florida International'))

if __name__=='__main__': unittest.main()
