import os
import subprocess
import tempfile
import unittest
from pathlib import Path
import cfb_week6_production_frozen_gate as gate

class FrozenDisplayTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sheet=Path('evidence/operational/CFB_WEEK6_HOT_SHEET_2026-10-09_1538CT.md').read_text()
        cls.archive=Path(os.environ.get('CFB_ACCEPTED_FREEZE_ARCHIVE','frozen.zip')).resolve()

    def audit(self,content):
        with tempfile.TemporaryDirectory() as temp:
            p=Path(temp)/'synthetic.md'; p.write_text(content)
            return gate.audit_sheet(p,self.archive)

    def rejected(self,content,reason):
        with self.assertRaises(subprocess.CalledProcessError) as cm: self.audit(content)
        self.assertIn(reason,cm.exception.stderr)

    def test_real_147_numeric_values(self):
        r=self.audit(self.sheet); self.assertEqual(r['matched_numeric_fields'],147)
        self.assertEqual(r['matched_favorite_directions'],49)

    def test_spread_change(self):
        self.rejected(self.sheet.replace('Troy -6.4 / 51.9 / .612 home','Troy -6.5 / 51.9 / .612 home'),'fair spread mismatch')

    def test_total_change(self):
        self.rejected(self.sheet.replace('Troy -6.4 / 51.9 / .612 home','Troy -6.4 / 52.0 / .612 home'),'frozen total mismatch')

    def test_probability_change(self):
        self.rejected(self.sheet.replace('Troy -6.4 / 51.9 / .612 home','Troy -6.4 / 51.9 / .613 home'),'probability mismatch')

    def test_favorite_reversal(self):
        self.rejected(self.sheet.replace('Troy -6.4 / 51.9 / .612 home','Southern Miss -6.4 / 51.9 / .612 home'),'favorite direction mismatch')

    def test_wrong_archive(self):
        with tempfile.TemporaryDirectory() as temp:
            p=Path(temp)/'bad.zip'; p.write_bytes(b'synthetic invalid archive')
            with self.assertRaises(subprocess.CalledProcessError) as cm: gate.audit_sheet(Path('evidence/operational/CFB_WEEK6_HOT_SHEET_2026-10-09_1538CT.md'),p)
            self.assertIn('archive does not match accepted',cm.exception.stderr)

    def test_unresolved_kickoff_retains_frozen_values(self):
        r=self.audit(self.sheet.replace('| Sat 12:00 PM |','| UNRESOLVED |'))
        self.assertEqual(r['matched_numeric_fields'],147)

if __name__=='__main__': unittest.main()
