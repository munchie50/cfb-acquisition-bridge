"""Mocked Week10 conditional protocol over retained sources, never actual picks."""
import copy
import json
import unittest
from unittest.mock import patch

import cfb_conditional_recommendation_profile as profile
import cfb_neutral_publication_gate as gate
import cfb_week10_publication as week
import test_cfb_conditional_recommendation_profile as conditional_fixtures
import test_cfb_week10_publication as fixtures
from test_cfb_week10_publication import AT


class Week10ConditionalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        fixtures.Week10Tests.setUpClass()
        conditional_fixtures.ConditionalTests.setUpClass()

    def setUp(self):
        self.rows = copy.deepcopy(fixtures.Week10Tests.rows)
        self.census = {r['game_id']: r for r in json.loads(fixtures.Week10Tests.lineage)['rows']}
        self.target = next(r for r in self.rows if r['game_id'] == '401866455')
        self.source = copy.deepcopy(week.first_rows(fixtures.Week10Tests.lineage)[self.target['game_id']])
        fixture = conditional_fixtures.ConditionalTests()
        fixture.setUp()
        self.review = json.loads(json.dumps(fixture.review).replace('2026-10-17T00:04', '2026-11-04T17:54'))
        self.review.update(game_id=self.target['game_id'], original_lineage_blob=week.WEEK10_LINEAGE_SHA,
                           reconciliation_utc='2026-11-04T18:20:00Z', planning_cutoff_utc='2026-11-04T23:00:00Z',
                           execution_window={'start_utc': '2026-11-04T17:55:00Z', 'end_utc': '2026-11-04T23:00:00Z'})
        ref = self.review['market_reference']
        ref.update(game_id=self.target['game_id'], kickoff_utc=self.source['kickoff_utc'],
                   kickoff_source_url='https://example.org/official-synthetic-week10-schedule')
        for q in ref['quotes']:
            q['game_id'] = self.target['game_id']
        self.source.update(kickoff_status='QUALIFIED', kickoff_source_url=ref['kickoff_source_url'])
        self.target.update(state='CONDITIONAL', reason=self.review['rationale'], cutoff_authority='REVIEW_EVIDENCED',
                           review_ref=copy.deepcopy(fixture.target['review_ref']))
        for key in ('acceptable_number', 'reconciliation_utc', 'planning_cutoff_utc', 'execution_window'):
            self.target[key] = copy.deepcopy(self.review[key])

    def mocked(self):
        return patch.object(profile, 'load_review', return_value=(json.dumps(self.review), '2026-11-04T17:54:50Z'))

    def build(self):
        with self.mocked():
            return fixtures.Week10Tests.build(decision_rows=self.rows)

    def direct(self, **changes):
        row = dict(self.target, state_recorded_at_utc=AT)
        values = dict(row=row, market_row=self.source, model=self.census[row['game_id']],
                      as_of=AT, lineage_sha=week.WEEK10_LINEAGE_SHA)
        values.update(changes)
        with self.mocked():
            return profile.validate(**values)

    def test_valid_week10_conditional_compiles_renders_and_preserves_original_exclusions(self):
        original_exclusions = {gid: copy.deepcopy(r) for gid, r in self.census.items() if r['first_frozen_status'] == 'EXCLUDED'}
        with self.mocked():
            m, d = fixtures.Week10Tests.build(decision_rows=self.rows)
            sheet = gate.render(m, d, 'execution fixture', 'scorecard fixture', fixtures.Week10Tests.lineage, AT, 'WEEK10')
            result = gate.audit(sheet, m, d, 'execution fixture', 'scorecard fixture', fixtures.Week10Tests.lineage, AT, 'WEEK10')
            actual_census = gate.inputs(m, d, fixtures.Week10Tests.lineage, AT, 'WEEK10')[2]
        self.assertTrue(m.startswith(fixtures.Week10Tests.market))
        self.assertTrue(d.startswith(fixtures.Week10Tests.decision))
        self.assertEqual(result['games'], 63)
        self.assertEqual(sheet.count('| CONDITIONAL |'), 1)
        self.assertIn('VENUE_CONFIRMATION_PENDING', sheet)
        self.assertIn('55 predictions and 8 exclusions', sheet)
        self.assertEqual(len(original_exclusions), 8)
        self.assertEqual({gid: r for gid, r in actual_census.items() if r['first_frozen_status'] == 'EXCLUDED'}, original_exclusions)
        self.direct()

    def test_unknown_lineage_and_wrong_review_lineage_rejected(self):
        with self.assertRaisesRegex(ValueError, 'unqualified conditional lineage'):
            self.direct(lineage_sha='0' * 40)
        self.review['original_lineage_blob'] = gate.profile_config('WEEK9')['lineage']
        with self.assertRaisesRegex(ValueError, 'lineage mismatch'):
            self.build()

    def test_expired_review_rejected(self):
        self.review['reconciliation_utc'] = self.target['reconciliation_utc'] = AT
        with self.assertRaisesRegex(ValueError, 'expired|inconsistent'):
            self.build()

    def test_current_or_elapsed_kickoff_rejected(self):
        for kickoff in (AT, '2026-11-04T17:55:00Z'):
            source = dict(self.source, kickoff_utc=kickoff)
            with self.subTest(kickoff=kickoff), self.assertRaisesRegex(ValueError, 'qualified future kickoff'):
                self.direct(market_row=source)

    def test_cbs_display_does_not_qualify_conditional_kickoff(self):
        self.review['market_reference']['kickoff_source_url'] = week.WEEK10_URL
        with self.assertRaisesRegex(ValueError, 'display alone'):
            self.build()

    def test_altered_line_price_cutoff_or_window_rejected(self):
        original = copy.deepcopy(self.target)
        mutations = [('acceptable_number', dict(self.target['acceptable_number'], line=13)),
                     ('acceptable_number', dict(self.target['acceptable_number'], minimum_price=-120)),
                     ('planning_cutoff_utc', '2026-11-04T23:10:00Z'),
                     ('execution_window', {'start_utc': '2026-11-04T17:55:00Z', 'end_utc': '2026-11-04T23:10:00Z'})]
        for field, value in mutations:
            self.target.clear(); self.target.update(copy.deepcopy(original)); self.target[field] = value
            with self.subTest(field=field, value=value), self.assertRaisesRegex(ValueError, 'differs from immutable review'):
                self.build()

    def test_each_original_exclusion_rejects_conditional_substitution(self):
        for model in self.census.values():
            if model['first_frozen_status'] != 'EXCLUDED':
                continue
            with self.subTest(game=model['game_id']), self.assertRaisesRegex(ValueError, 'original model exclusion'):
                self.direct(model=model)

    def test_missing_material_review_still_rejected(self):
        self.review['material_sources'] = []
        with self.assertRaisesRegex(ValueError, 'material availability'):
            self.build()

    def primary_summary_review(self):
        self.review['schema'] = profile.RETRIEVAL_REVIEW_SCHEMA
        reference = self.review['market_reference']
        reference['clock_semantics'] = 'EXACT_RETRIEVAL'
        reference['quotes'] = [reference['quotes'][0]]
        reference['quotes'][0].update(
            book='DraftKings', operator='DraftKings', offer_updated_at=None,
            source_url='https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=' + self.target['game_id'],
            operator_evidence_url='https://sportsbook.draftkings.com/event/synthetic-qa-only/123456?outcomes=7654321')
        return reference['quotes'][0]

    def test_exact_primary_summary_alias_is_retrieval_only_and_compiles(self):
        quote = self.primary_summary_review()
        result = profile.market_reference(self.review, AT)
        self.assertEqual(result['status'], 'IDENTIFIED_RETRIEVAL_ONLY_BENCHMARK')
        self.assertEqual(result['consensus'], 'CONSENSUS_UNAVAILABLE')
        self.assertIsNone(quote['offer_updated_at'])
        with self.mocked():
            market, decision = fixtures.Week10Tests.build(decision_rows=self.rows)
            sheet = gate.render(market, decision, 'execution fixture', 'scorecard fixture', fixtures.Week10Tests.lineage, AT, 'WEEK10')
        self.assertEqual(sheet.count('| CONDITIONAL |'), 1)
        self.assertIn('VENUE_CONFIRMATION_PENDING', sheet)

    def test_primary_summary_rejects_wrong_host_path_event_or_extra_query(self):
        quote = self.primary_summary_review()
        original = quote['source_url']
        invalid = [original.replace('site.api.espn.com', 'site.api.example.org'),
                   original.replace('/summary?', '/scoreboard?'),
                   original.replace('?event=' + self.target['game_id'], '?event=401866456'),
                   original + '&event=' + self.target['game_id'],
                   original + '&limit=100', original.replace('https:', 'http:'),
                   original + '#synthetic', original.replace('site.api.espn.com', 'site.api.espn.com:443')]
        for url in invalid:
            quote['source_url'] = url
            with self.subTest(url=url), self.assertRaises(ValueError):
                profile.market_reference(self.review, AT)

    def test_primary_summary_requires_draftkings_selection_link_and_unknown_update(self):
        quote = self.primary_summary_review()
        original = copy.deepcopy(quote)
        changes = [dict(book='FanDuel', operator='FanDuel', operator_evidence_url='https://sportsbook.fanduel.com/event/123?outcomes=1'),
                   dict(operator_evidence_url='https://sportsbook.draftkings.com/'),
                   dict(operator_evidence_url='https://sportsbook.draftkings.com/event/123'),
                   dict(operator_evidence_url='https://sportsbook.draftkings.com/event/123?outcomes=1&outcomes=2'),
                   dict(offer_updated_at='2026-11-04T17:54:10Z')]
        for change in changes:
            quote.clear(); quote.update(copy.deepcopy(original)); quote.update(change)
            with self.subTest(change=change), self.assertRaises(ValueError):
                profile.market_reference(self.review, AT)


if __name__ == '__main__':
    unittest.main()
