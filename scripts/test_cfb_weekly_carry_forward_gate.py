import json,os,unittest
from pathlib import Path
import cfb_weekly_carry_forward_gate as gate
ROOT=Path(__file__).resolve().parents[1]
class CarryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        fixture=os.environ.get('CFB_WEEKLY_CARRY_FIXTURE_DIR')
        if fixture:
            root=Path(fixture);cls.original=(root/'original.md').read_text();cls.lineage=(root/'lineage.json').read_text()
            cls.health=json.loads((root/'health_source.json').read_text())['content']
        else:
            cls.original=(ROOT/'evidence/CFB_ENGINE_WEEKLY_BETA_LEARNING_REVIEW_2026-10-11_R1.md').read_text()
            cls.lineage=(ROOT/'evidence/operational/CFB_WEEK7_ORIGINAL_FIRST_FROZEN_LINEAGE_2026-10-11.json').read_text()
            cls.health=(ROOT/'evidence/scheduler_qa/CFB_DUAL_ENGINE_HEALTH_20261011T215456Z_AUDIT.md').read_text()
        cls.review=gate.expected(cls.original,cls.lineage,cls.health)
    def check(self,review=None,original=None,lineage=None,health=None):
        return gate.audit(self.review if review is None else review,self.original if original is None else original,self.lineage if lineage is None else lineage,self.health if health is None else health)
    def reject(self,value):
        with self.assertRaises(ValueError):self.check(review=value)
    def test_actual(self):self.assertEqual(self.check()['first_frozen_predictions'],51)
    def test_original_false_absence_rejected(self):self.reject(self.original)
    def test_false_absence_returned(self):self.reject(self.review.replace(gate.NEW_EXEC,gate.OLD_EXEC))
    def test_original_byte_identity(self):
        with self.assertRaises(ValueError):self.check(original=self.original+'\n')
    def test_lineage_byte_identity(self):
        with self.assertRaises(ValueError):self.check(lineage=self.lineage+'\n')
    def test_health_byte_identity(self):
        with self.assertRaises(ValueError):self.check(health=self.health+'\n')
    def test_wrong_first_count(self):self.reject(self.review.replace('51 immutable predictions','61 immutable predictions',1))
    def test_lost_exclusion(self):self.reject(self.review.replace('11 explicit original exclusions','1 explicit original exclusion',1))
    def test_refresh_substitution(self):self.reject(self.review.replace('never substitutes','substitutes',1))
    def test_retro_closed(self):self.reject(self.review.replace('OPEN / NATURAL_PRODUCER_PENDING','CLOSED',1))
    def test_natural_success_reintroduced(self):self.reject(self.review.replace('natural output semantic fidelity UNVERIFIED','natural output semantic fidelity PASS',1))
    def test_week6_stats_unchanged(self):self.reject(self.review.replace('| Margin MAE | 15.13','| Margin MAE | 1.13',1))
    def test_actual_wager_unchanged(self):self.reject(self.review.replace('Appalachian State -10 (-110), $5','Appalachian State -9 (-110), $5',1))
    def test_accounting_unchanged(self):self.reject(self.review.replace('$53.45 stake','$73.45 stake',1))
    def test_threshold_unchanged(self):self.reject(self.review.replace('max -115','max -120',1))
    def test_champion_unchanged(self):self.reject(self.review.replace('v1.193','v2.193',1))
    def test_source_hash_unchanged(self):self.reject(self.review.replace(gate.CURRENT_SHEET_SHA,'0'*40,1))
    def test_49_game_rows_unchanged(self):
        def rows(s):return s.split('## 3. Game-level learning',1)[1].split('Largest absolute margin misses:',1)[0]
        self.assertEqual(rows(self.review),rows(self.original))
        self.assertEqual(sum(l.startswith('| ') and '@' in l for l in rows(self.review).splitlines()),48)
        self.assertIn('| Texas vs Oklahoma |',rows(self.review))
    def test_wager_table_unchanged(self):
        def wager(s):return s.split('### Established Week 6 user wagers only',1)[1].split('## 6. Real-world Beta failures',1)[0]
        self.assertEqual(wager(self.review),wager(self.original))
    def test_extra_claim_rejected(self):self.reject(self.review+'\nRUN_PASS full natural production\n')
    def navigation(self,changes=None):
        p=[{'path':gate.R2,'blob':gate.blob(self.review),'purpose':'CURRENT_WEEKLY_REVIEW: exact manual R2'},
           {'path':'evidence/operational/CFB_WEEK7_ORIGINAL_FIRST_FROZEN_LINEAGE_2026-10-11.json','blob':gate.LINEAGE_SHA,'purpose':'accepted lineage'},
           {'path':'evidence/scheduler_qa/CFB_DUAL_ENGINE_HEALTH_20261011T215456Z_AUDIT.md','blob':gate.HEALTH_SHA,'purpose':'latest incomplete health'}]
        if changes:changes(p)
        f={'schema':'CFB_RECOVERY_NAVIGATION_FRONTIER_V1','as_of_utc':'2026-10-11T23:45:19Z','scope':'NAVIGATION_ONLY_NOT_AUTHORITY','claims':['Navigation only'],'pointers':p}
        return '```cfb-frontier-json\n'+json.dumps(f)+'\n```\n'
    def test_current_binding(self):self.assertEqual(gate.bind(self.navigation(),self.review,self.lineage,self.health,'2026-10-11T23:45:19Z')['current_weekly_review_blob'],gate.blob(self.review))
    def test_missing_current_role(self):
        with self.assertRaises(ValueError):gate.bind(self.navigation(lambda p:p[0].update(purpose='historical')),self.review,self.lineage,self.health,'2026-10-11T23:45:19Z')
    def test_stale_current_blob(self):
        with self.assertRaises(ValueError):gate.bind(self.navigation(lambda p:p[0].update(blob='0'*40)),self.review,self.lineage,self.health,'2026-10-11T23:45:19Z')
    def test_ambiguous_current_role(self):
        with self.assertRaises(ValueError):gate.bind(self.navigation(lambda p:p[1].update(purpose='CURRENT_WEEKLY_REVIEW: competing')),self.review,self.lineage,self.health,'2026-10-11T23:45:19Z')
    def test_stale_health_pointer(self):
        with self.assertRaises(ValueError):gate.bind(self.navigation(lambda p:p[2].update(blob='0'*40)),self.review,self.lineage,self.health,'2026-10-11T23:45:19Z')
    def test_qualified_week7_navigation_retains_historical_review(self):
        def advance(p):
            p[0]['purpose']='HISTORICAL_WEEKLY_REVIEW: retained correction'
            p.append({'path':gate.WEEK7_REVIEW,'blob':gate.WEEK7_REVIEW_SHA,'purpose':'CURRENT_WEEKLY_REVIEW: Week7 closure'})
        result=gate.bind(self.navigation(advance),self.review,self.lineage,self.health,'2026-10-20T01:40:30Z')
        self.assertEqual(result['current_weekly_review_blob'],gate.WEEK7_REVIEW_SHA)
    def test_unqualified_weekly_successor_rejected(self):
        for path,sha in [(gate.WEEK7_REVIEW,'0'*40),('evidence/future_week.md',gate.WEEK7_REVIEW_SHA)]:
            def advance(p):
                p[0]['purpose']='historical'
                p.append({'path':path,'blob':sha,'purpose':'CURRENT_WEEKLY_REVIEW: unsupported'})
            with self.assertRaises(ValueError):
                gate.bind(self.navigation(advance),self.review,self.lineage,self.health,'2026-10-20T01:40:30Z')
    def test_successor_cannot_erase_historical_correction(self):
        def advance(p):
            p[0].update(path=gate.WEEK7_REVIEW,blob=gate.WEEK7_REVIEW_SHA)
        with self.assertRaisesRegex(ValueError,'historical weekly correction'):
            gate.bind(self.navigation(advance),self.review,self.lineage,self.health,'2026-10-20T01:40:30Z')
if __name__=='__main__':unittest.main()
