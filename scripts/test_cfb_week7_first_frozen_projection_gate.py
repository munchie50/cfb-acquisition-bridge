import os, unittest
from pathlib import Path
import cfb_week7_first_frozen_projection_gate as gate

ROOT=Path(__file__).resolve().parents[1]
class ProjectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        base=Path(os.environ.get('CFB_WEEK7_PROJECTION_FIXTURE_ROOT',ROOT))
        cls.parent=(base/'evidence/operational/CFB_WEEK7_HOT_SHEET_2026-10-11_1305CT.md').read_text()
        if 'CFB_WEEK7_PROJECTION_FIXTURE_ROOT' in os.environ:
            cls.prior=(base/'evidence/operational/CFB_DECISION_WAIT_LEDGER.md').read_text()
        else:
            from test_cfb_week7_opening_display_gate import snapshot
            cls.prior=snapshot('evidence/operational/CFB_DECISION_WAIT_LEDGER.md',gate.DECISION_SHA)
        cls.first=Path(os.environ['CFB_ACCEPTED_FREEZE_ARCHIVE'])
        cls.refresh=Path(os.environ['CFB_ACCEPTED_REFRESH_ARCHIVE'])
        cls.rows=gate.inventory(cls.first,cls.refresh,cls.parent)
        cls.decision,cls.sheet=gate.project(cls.parent,cls.prior,cls.rows)
    def check(self,s=None,d=None,p=None):
        return gate.audit(self.sheet if s is None else s,self.parent if p is None else p,self.decision if d is None else d,self.prior,self.first,self.refresh)
    def reject(self,s):
        with self.assertRaises(ValueError):self.check(s)
    def row(self,g):return next(l for l in self.sheet.splitlines() if l.startswith('| ') and len(l.split('|'))==11 and l.split('|')[2].strip()==g)
    def alter(self,g,n,value):
        old=self.row(g);cells=[c.strip() for c in old.split('|')[1:-1]];cells[n]=value
        return self.sheet.replace(old,'| '+' | '.join(cells)+' |',1)
    def test_actual(self):
        r=self.check();self.assertEqual((r['games'],r['first_frozen_predictions'],r['first_frozen_exclusions']),(62,51,11))
    def test_original_parent_exposes_absence_error(self):self.reject(self.parent)
    def test_original_numeric_source_independent(self):
        import zipfile,csv,io
        with zipfile.ZipFile(self.first) as z:
            records={r['game_id']:r for r in csv.DictReader(io.StringIO(z.read('challenger_b_2026_fair_predictions_v1_206.csv').decode()))}
        for row in self.rows:
            if row['first_frozen_status']!='PREDICTION':continue
            r=records[row['game_id']];m=float(r['pred_margin']);parts=row['display'].removeprefix('FIRST_FROZEN: ').split(' / ')
            self.assertEqual(parts[0],(r['home_team'] if m>=0 else r['away_team'])+' -'+format(abs(m),'.1f'))
            self.assertEqual(parts[1],format(float(r['pred_total']),'.1f'))
            self.assertEqual(parts[2],format(float(r['pred_win']),'.3f')+' home')
    def test_earliest_four_available(self):
        self.assertTrue(all(r['first_frozen_status']=='PREDICTION' for r in self.rows[:4]))
    def test_exclusion_preserved(self):
        e=[r for r in self.rows if r['first_frozen_status']=='EXCLUDED'];self.assertEqual(len(e),11)
        self.assertEqual(sum(r['oct6_refresh_status']=='PREDICTION' for r in e),10)
        self.assertTrue(all('not substituted' in r['display'] for r in e))
    def test_positive_margin_favorite(self):self.assertIn('Home -3.0',gate.fair({'pred_margin':'3','home_team':'Home','away_team':'Away','pred_total':'40','pred_win':'.7'}))
    def test_negative_margin_favorite(self):self.assertIn('Away -3.0',gate.fair({'pred_margin':'-3','home_team':'Home','away_team':'Away','pred_total':'40','pred_win':'.3'}))
    def test_wrong_number(self):self.reject(self.alter('Delaware @ Middle Tenn.',2,'FIRST_FROZEN: Delaware -99.0 / 40.0 / .9 home'))
    def test_false_absence(self):self.reject(self.alter('Delaware @ Middle Tenn.',2,'NOT YET EARNED'))
    def test_refresh_substitution(self):self.reject(self.alter('East Carolina @ UAB',2,'REFRESH: UAB -3.0 / 40.0 / .6 home'))
    def test_lost_exclusion_reason(self):self.reject(self.alter('Elon @ Stanford',2,'EXCLUDED'))
    def test_bet_not_earned(self):self.reject(self.alter('Delaware @ Middle Tenn.',5,'BET NOW'))
    def test_quote_unchanged(self):self.reject(self.alter('Delaware @ Middle Tenn.',3,'New price'))
    def test_movement_unchanged(self):self.reject(self.alter('Delaware @ Middle Tenn.',4,'Movement 0'))
    def test_clock_not_extended(self):self.reject(self.alter('Delaware @ Middle Tenn.',7,'final cutoff kickoff'))
    def test_unverified_clock_not_dropped(self):self.reject(self.sheet.replace('CUTOFF_AUTHORITY_UNVERIFIED','CUTOFF_VERIFIED',1))
    def test_no_execution(self):self.reject(self.alter('Delaware @ Middle Tenn.',8,'Bet $5'))
    def test_duplicate(self):
        r=self.row('Delaware @ Middle Tenn.');self.reject(self.sheet.replace(r,r+'\n'+r))
    def test_missing(self):self.reject(self.sheet.replace(self.row('Elon @ Stanford'),''))
    def test_old_decision_rewrite(self):
        with self.assertRaises(ValueError):self.check(d=self.decision.replace('INCONCLUSIVE','BET NOW',1))
    def test_later_decision_needs_qualification(self):
        with self.assertRaises(ValueError):self.check(d=self.decision+'\nLater disposition\n')
    def test_parent_unqualified(self):
        with self.assertRaises(ValueError):self.check(p=self.parent+'\n')
    def test_bad_archive(self):
        with self.assertRaises(ValueError):gate.inventory(self.refresh,self.refresh,self.parent)

if __name__=='__main__':unittest.main()
