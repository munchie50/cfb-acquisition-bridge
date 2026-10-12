import copy,os,unittest
from pathlib import Path
import cfb_accepted_refresh_field_adapter as gate
ROOT=Path(__file__).resolve().parents[1]
class RefreshTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        local=os.environ.get('CFB_REFRESH_FIELD_FIXTURE_DIR')
        if local:
            base=Path(local);cls.pointer=(base/'pointer.json').read_text();cls.acceptance=(base/'acceptance.md').read_text();cls.lineage=(Path('frozen_invariant_qa')/'lineage.json').read_text()
        else:
            from test_cfb_week7_opening_display_gate import snapshot
            cls.pointer=snapshot('evidence/operational/CFB_ACCEPTED_PREDICTION_SOURCE_STATE.json',gate.POINTER_SHA)
            cls.acceptance=snapshot('evidence/CFB_QA_WEEKLY_REFRESH_ACCEPTANCE_2026-10-07.md',gate.ACCEPTANCE_SHA)
            cls.lineage=(ROOT/'evidence/operational/CFB_WEEK7_ORIGINAL_FIRST_FROZEN_LINEAGE_2026-10-11.json').read_text()
        cls.z=Path(os.environ['CFB_ACCEPTED_REFRESH_ARCHIVE']);cls.package=gate.prepare(cls.z,cls.pointer,cls.acceptance,cls.lineage)
    def check(self,package=None,pointer=None,acceptance=None,lineage=None):
        return gate.audit(self.package if package is None else package,self.z,self.pointer if pointer is None else pointer,self.acceptance if acceptance is None else acceptance,self.lineage if lineage is None else lineage)
    def bad(self,change):
        x=copy.deepcopy(self.package);change(x)
        with self.assertRaises(ValueError):self.check(package=x)
    def test_actual(self):
        r=self.check();self.assertEqual((r['refresh_predictions'],r['refresh_exclusions'],r['later_eligible_original_exclusions']),(61,1,10))
    def test_original_preserved(self):
        before=self.lineage;self.check();self.assertEqual(self.lineage,before)
        self.assertEqual(sum(r['original_first_frozen_status']=='EXCLUDED' for r in self.package['records']),11)
    def test_not_first_frozen(self):self.bad(lambda x:x.update(source_type='FIRST_FROZEN'))
    def test_unaccepted_candidate_pointer(self):
        with self.assertRaises(ValueError):self.check(pointer=self.pointer.replace('ACCEPTED_PREDICTION_SOURCE_STATE','WEEKLY_CANDIDATE_BOUNDARY_NOT_ACCEPTED'))
    def test_acceptance_absent(self):
        with self.assertRaises(ValueError):self.check(acceptance='workflow success')
    def test_acceptance_changed(self):
        with self.assertRaises(ValueError):self.check(acceptance=self.acceptance+'\n')
    def test_unknown_boundary(self):
        with self.assertRaises(ValueError):self.check(pointer=self.pointer.replace('2026-10-06','2026-10-13'))
    def test_census_changed(self):
        with self.assertRaises(ValueError):self.check(lineage=self.lineage+'\n')
    def test_wrong_cutoff(self):self.bad(lambda x:x.update(cutoff_utc='2026-10-13T15:00:00Z'))
    def test_operational_selection_not_earned(self):self.bad(lambda x:x.update(scope='PRODUCTION_SELECTED'))
    def test_missing_id(self):self.bad(lambda x:x['records'].pop())
    def test_duplicate_id(self):self.bad(lambda x:x['records'].__setitem__(1,x['records'][0]))
    def test_row_reordering(self):
        x=copy.deepcopy(self.package);x['records'].reverse();self.check(x)
    def test_unknown_id(self):self.bad(lambda x:x['records'][0].update(game_id='999'))
    def test_directed_identity(self):self.bad(lambda x:x['records'][0].update(home_team='Delaware'))
    def test_value_rewrite(self):self.bad(lambda x:x['records'][0].update(refresh_field='REFRESH_SNAPSHOT: Delaware -99 / 90 / .9 home'))
    def test_type_relabel(self):self.bad(lambda x:x['records'][0].update(snapshot_type='FIRST_FROZEN'))
    def test_original_exclusion_backfill(self):self.bad(lambda x:next(r for r in x['records'] if r['original_first_frozen_status']=='EXCLUDED').update(original_first_frozen_status='PREDICTION'))
    def test_original_numeric_rewrite(self):self.bad(lambda x:x['records'][0].update(original_first_frozen_field=x['records'][0]['refresh_field']))
    def test_refresh_exclusion_filled(self):self.bad(lambda x:next(r for r in x['records'] if r['refresh_status']=='EXCLUDED').update(refresh_status='PREDICTION'))
    def test_outcome_column(self):self.bad(lambda x:x['records'][0].update(final_home_score=40))
    def test_market_column(self):self.bad(lambda x:x['records'][0].update(caesars_line=-4))
    def test_unscoped_extra_fields(self):self.bad(lambda x:x.update(accepted=True))
    def test_independent_numeric_csv(self):
        import csv,io,zipfile
        with zipfile.ZipFile(self.z) as z:
            rows={r['game_id']:r for r in csv.DictReader(io.StringIO(z.read('s0/challenger_b_2026_refresh_fair_predictions_v1_246.csv').decode()))}
        checked=0
        for r in self.package['records']:
            if r['refresh_status']!='PREDICTION':continue
            source=rows[r['game_id']];m=float(source['pred_margin']);favorite=source['home_team'] if m>=0 else source['away_team']
            expected='REFRESH_SNAPSHOT: '+favorite+' -'+format(abs(m),'.1f')+' / '+format(float(source['pred_total']),'.1f')+' / '+format(float(source['pred_win']),'.3f')+' home'
            self.assertEqual(r['refresh_field'],expected);checked+=1
        self.assertEqual(checked,61)
if __name__=='__main__':unittest.main()
