import copy
import unittest
from datetime import datetime, timezone
from cfb_week7_accepted_s0_ancestry_audit import coverage, sheet_rows

class CoverageTests(unittest.TestCase):
    def setUp(self):
        self.target = [{'game_id': '1', 'away_team': 'A', 'home_team': 'B', 'start_date': '2026-10-13T23:00:00+00:00'}]
        self.pred = [{'game_id': '1'}]
        self.rows = [(('A', 'B'), datetime(2026,10,13,23,tzinfo=timezone.utc))]
    def test_prediction(self):
        r=coverage(self.target,self.pred,[],self.rows)
        self.assertEqual(r['s0_predictions'],1)
        self.assertEqual(r['status'],'ANCESTRY_COVERAGE_ONLY_NOT_OPERATIONAL_ACCEPTANCE')
    def test_exclusion(self):
        self.assertEqual(coverage(self.target,[],self.pred,self.rows)['s0_exclusions'],1)
    def test_duplicate_target(self):
        with self.assertRaises(ValueError): coverage(self.target*2,self.pred,[],self.rows)
    def test_duplicate_prediction(self):
        with self.assertRaises(ValueError): coverage(self.target,self.pred*2,[],self.rows)
    def test_duplicate_exclusion(self):
        with self.assertRaises(ValueError): coverage(self.target,[],self.pred*2,self.rows)
    def test_overlap(self):
        with self.assertRaises(ValueError): coverage(self.target,self.pred,self.pred,self.rows)
    def test_missing_partition(self):
        with self.assertRaises(ValueError): coverage(self.target,[],[],self.rows)
    def test_wrong_pair(self):
        with self.assertRaises(ValueError): coverage(self.target,self.pred,[],[(('B','A'),self.rows[0][1])])
    def test_ambiguous_pair(self):
        extra=copy.deepcopy(self.target[0]);extra['game_id']='2'
        with self.assertRaises(ValueError): coverage(self.target+[extra],self.pred+[{'game_id':'2'}],[],self.rows)
    def test_old_week(self):
        self.target[0]['start_date']='2026-10-06T23:00:00+00:00'
        with self.assertRaises(ValueError): coverage(self.target,self.pred,[],self.rows)
    def test_moved_clock_not_rewritten(self):
        self.target[0]['start_date']='2026-10-13T22:00:00+00:00'
        r=coverage(self.target,self.pred,[],self.rows)
        self.assertEqual(r['archive_start_mismatches'],1)
        self.assertEqual(self.target[0]['start_date'],'2026-10-13T22:00:00+00:00')
    def test_incomplete_sheet(self):
        with self.assertRaises(ValueError): sheet_rows('')

if __name__ == '__main__': unittest.main()
