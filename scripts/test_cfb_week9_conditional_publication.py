"""Synthetic Week9 decisions over authentic retained source; never actual picks."""
import copy
import json
import unittest
from unittest.mock import patch
import cfb_conditional_recommendation_profile as profile
import cfb_neutral_publication_gate as gate
import test_cfb_week9_publication as fixtures
from test_cfb_week9_publication import AT
import test_cfb_conditional_recommendation_profile as conditional_fixtures


class Week9ConditionalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        fixtures.Week9Tests.setUpClass()

    def setUp(self):
        self.rows = copy.deepcopy(fixtures.Week9Tests.rows)
        census = json.loads(fixtures.Week9Tests.lineage)['rows']
        gid = next(r['game_id'] for r in census if r['first_frozen_status'] == 'PREDICTION')
        self.target = next(r for r in self.rows if r['game_id'] == gid)
        self.source = __import__('cfb_week9_publication').first_rows(fixtures.Week9Tests.lineage)[gid]
        fixture = conditional_fixtures.ConditionalTests()
        conditional_fixtures.ConditionalTests.setUpClass()
        fixture.setUp()
        self.review = json.loads(json.dumps(fixture.review).replace('2026-10-17T00:04', '2026-10-25T15:54'))
        self.review.update(game_id=gid, original_lineage_blob=gate.profile_config('WEEK9')['lineage'],
                           reconciliation_utc='2026-10-25T16:20:00Z',
                           planning_cutoff_utc='2026-10-26T17:00:00Z',
                           execution_window={'start_utc': '2026-10-25T15:55:00Z', 'end_utc': '2026-10-26T17:00:00Z'})
        ref = self.review['market_reference']
        ref.update(game_id=gid, kickoff_utc=self.source['kickoff_utc'], kickoff_source_url='https://example.org/official-synthetic-schedule')
        for q in ref['quotes']:
            q['game_id'] = gid
        self.target.update(state='CONDITIONAL', reason=self.review['rationale'], cutoff_authority='REVIEW_EVIDENCED',
                           review_ref=copy.deepcopy(fixture.target['review_ref']))
        for k in ('acceptable_number', 'reconciliation_utc', 'planning_cutoff_utc', 'execution_window'):
            self.target[k] = copy.deepcopy(self.review[k])

    def build(self):
        with patch.object(profile, 'load_review', return_value=(json.dumps(self.review), '2026-10-25T15:54:50Z')):
            return fixtures.Week9Tests.build(decision_rows=self.rows)

    def test_qualified_review_compiles_renders_and_preserves_history(self):
        with patch.object(profile, 'load_review', return_value=(json.dumps(self.review), '2026-10-25T15:54:50Z')):
            m, d = fixtures.Week9Tests.build(decision_rows=self.rows)
            sheet = gate.render(m, d, 'execution fixture', 'scorecard fixture', fixtures.Week9Tests.lineage, AT, 'WEEK9')
            gate.audit(sheet, m, d, 'execution fixture', 'scorecard fixture', fixtures.Week9Tests.lineage, AT, 'WEEK9')
        self.assertTrue(m.startswith(fixtures.Week9Tests.market))
        self.assertTrue(d.startswith(fixtures.Week9Tests.decision))
        self.assertEqual(sheet.count('| CONDITIONAL |'), 1)
        self.assertIn('VENUE_CONFIRMATION_PENDING', sheet)
        self.assertIn('45 predictions and 11 exclusions', sheet)

    def test_missing_review_is_rejected(self):
        self.target['review_ref'] = None
        with self.assertRaises(ValueError):
            fixtures.Week9Tests.build(decision_rows=self.rows)

    def test_cbs_display_cannot_qualify_kickoff(self):
        for url in (__import__('cfb_week9_publication').WEEK9_URL,
                    'https://www.cbssports.com/college-football/odds/FBS/2026/regular/week-9?view=full'):
            self.review['market_reference']['kickoff_source_url'] = url
            with self.subTest(url=url), self.assertRaisesRegex(ValueError, 'display alone'):
                self.build()

    def test_other_game_lineage_or_kickoff_rejected(self):
        original = copy.deepcopy(self.review)
        for key, value in [('game_id', 'wrong'), ('original_lineage_blob', gate.LINEAGE_SHA)]:
            self.review = copy.deepcopy(original)
            self.review[key] = value
            with self.assertRaises(ValueError): self.build()
        self.review = copy.deepcopy(original)
        self.review['market_reference']['kickoff_utc'] = '2026-10-28T23:00:00Z'
        with self.assertRaises(ValueError): self.build()

    def test_exclusions_cannot_be_replaced_by_conditional(self):
        gid = next(r['game_id'] for r in json.loads(fixtures.Week9Tests.lineage)['rows'] if r['first_frozen_status'] == 'EXCLUDED')
        self.target.update(state='INCONCLUSIVE', acceptable_number=None, execution_window=None, cutoff_authority='UNVERIFIED', review_ref=None)
        target = next(r for r in self.rows if r['game_id'] == gid)
        self.target, target_data = target, copy.deepcopy(self.target)
        self.target.update(target_data, game_id=gid, state='CONDITIONAL', reason=self.review['rationale'], cutoff_authority='REVIEW_EVIDENCED', review_ref={'path':'evidence/operational/recommendation_reviews/SYNTHETIC_QA_ONLY.json','commit':'a'*40,'blob':'b'*40})
        for k in ('acceptable_number', 'reconciliation_utc', 'planning_cutoff_utc', 'execution_window'):
            self.target[k] = copy.deepcopy(self.review[k])
        self.review['game_id'] = gid
        reference = self.review['market_reference']
        reference.update(game_id=gid, kickoff_utc=__import__('cfb_week9_publication').first_rows(fixtures.Week9Tests.lineage)[gid]['kickoff_utc'])
        for q in reference['quotes']: q['game_id'] = gid
        with self.assertRaisesRegex(ValueError, 'original model exclusion'):
            self.build()

    def test_expired_review_and_missing_material_are_rejected(self):
        self.review['reconciliation_utc'] = self.target['reconciliation_utc'] = AT
        with self.assertRaises(ValueError): self.build()
        self.setUp()
        self.review['material_sources'] = []
        with self.assertRaisesRegex(ValueError, 'material availability'):
            self.build()

    def test_overdue_neutral_rows_still_block_whole_packet(self):
        next(r for r in self.rows if r is not self.target)['reconciliation_utc'] = AT
        with self.assertRaisesRegex(ValueError, 'overdue'):
            self.build()

    def closed_fixture(self, at):
        for row in self.rows:
            if row is not self.target:
                row.update(state='PASS', reason='SYNTHETIC QA ONLY independently reviewed PASS')
        with patch.object(profile, 'load_review', return_value=(json.dumps(self.review), '2026-10-25T15:54:50Z')):
            m, d = fixtures.Week9Tests.build(decision_rows=self.rows)
            rows = [{k: v for k, v in r.items() if k not in ('state_recorded_at_utc', 'state_evidence')}
                    for r in gate.inputs(m, d, fixtures.Week9Tests.lineage, AT, 'WEEK9')[4].values()]
            import cfb_week9_publication as week
            out = week.compile(m, d, fixtures.Week9Tests.capture, fixtures.Week9Tests.lineage,
                               'CFB_PRESENTATION_RECONCILIATION_' + gate.clock(at).strftime('%Y%m%dT%H%M%SZ'), at, at, rows)
            sheet = gate.render(*out, 'execution fixture', 'scorecard fixture', fixtures.Week9Tests.lineage, at, 'WEEK9')
            gate.audit(sheet, *out, 'execution fixture', 'scorecard fixture', fixtures.Week9Tests.lineage, at, 'WEEK9')
        return m, d, out, sheet

    def test_closed_cutoff_retains_exact_origin_and_removes_opportunity(self):
        m, d, (pm, pd), sheet = self.closed_fixture('2026-10-26T17:01:00Z')
        self.assertTrue(pm.startswith(m)); self.assertTrue(pd.startswith(d))
        self.assertIn('| HISTORICAL CONDITIONAL — WINDOW CLOSED |', sheet)
        self.assertIn('**Primary section:** NONE', sheet)
        self.assertNotIn('Conditional recommendations are shown', sheet)

    def test_postkickoff_retention_is_history_without_current_quote(self):
        from datetime import timedelta
        at = (gate.clock(self.source['kickoff_utc']) + timedelta(minutes=1)).isoformat()
        m, d, (pm, pd), sheet = self.closed_fixture(at)
        with patch.object(profile, 'load_review', return_value=(json.dumps(self.review), '2026-10-25T15:54:50Z')):
            result = gate.inputs(pm, pd, fixtures.Week9Tests.lineage, at, 'WEEK9')
        self.assertIsNone(result[3][self.target['game_id']]['current'])
        self.assertIn('execution tracked separately', sheet)

    def test_changed_closed_origin_rejected(self):
        row = dict(self.target, state_recorded_at_utc=AT, state_evidence='OLD_SYNTHETIC')
        with self.assertRaisesRegex(ValueError, 'origin missing'):
            gate.conditional_boundary(row, {'cycle_id':'NEW_SYNTHETIC', 'as_of_utc':'2026-10-26T17:01:00Z'}, '', '', 'WEEK9')


if __name__ == '__main__': unittest.main()
