"""Recommendation blockers must never depend on venue verification."""
import copy
import unittest
from pathlib import Path
import cfb_hot_sheet_readiness as readiness


class ReadinessTests(unittest.TestCase):
    def setUp(self):
        self.review = dict.fromkeys(readiness.REVIEW_FIELDS, 'EARNED')

    def test_unverified_caesars_does_not_block_completed_review(self):
        r = readiness.assess(self.review, False)
        self.assertTrue(r['recommendation_review_complete'])
        self.assertEqual(r['recommendation_blockers'], [])
        self.assertEqual(r['venue_confirmation'], 'PENDING')

    def test_venue_does_not_change_recommendation_eligibility(self):
        a = readiness.assess(self.review, False)
        b = readiness.assess(self.review, True)
        self.assertEqual(a['recommendation_blockers'], b['recommendation_blockers'])
        self.assertEqual(a['recommendation_review_complete'], b['recommendation_review_complete'])

    def test_each_other_prerequisite_still_blocks(self):
        for field in readiness.REVIEW_FIELDS:
            with self.subTest(field=field):
                review = self.review.copy(); review[field] = 'MISSING'
                for venue in (False, True):
                    r = readiness.assess(review, venue)
                    self.assertFalse(r['recommendation_review_complete'])
                    self.assertEqual(r['recommendation_blockers'], [field.upper() + '_MISSING'])

    def test_unreviewed_never_means_earned(self):
        self.review['material_review'] = 'UNREVIEWED'
        self.assertFalse(readiness.assess(self.review)['recommendation_review_complete'])

    def test_missing_extra_and_unknown_fields_rejected(self):
        for change in ('missing', 'extra', 'unknown'):
            r = self.review.copy()
            if change == 'missing': r.pop('model_review')
            elif change == 'extra': r['caesars_required'] = 'EARNED'
            else: r['market_reference'] = 'TRUE'
            with self.assertRaises(ValueError): readiness.assess(r)

    def test_boolean_venue_not_string(self):
        with self.assertRaises(ValueError): readiness.assess(self.review, 'false')

    def test_no_input_mutation_or_automatic_bet(self):
        before = copy.deepcopy(self.review)
        r = readiness.assess(self.review)
        self.assertEqual(self.review, before)
        self.assertNotIn('BET NOW', str(r))
        self.assertNotIn('stake', r)

    def test_authentic_current_diagnostic_covers_all_qualified_states(self):
        root = Path('evidence/operational')
        m = (root / 'CFB_MARKET_MONITOR_STATE.md').read_text()
        d = (root / 'CFB_DECISION_WAIT_LEDGER.md').read_text()
        lineage = (root / 'CFB_WEEK7_ORIGINAL_FIRST_FROZEN_LINEAGE_2026-10-11.json').read_text()
        # Bound replay clock to the canonical packet; not a new observation.
        import cfb_neutral_weekly_reconciliation as repair
        at = repair.latest(m, readiness.gate.MARKET_TAG)['as_of_utc']
        r = readiness.audit(m, d, lineage, at)
        self.assertEqual(r['games'], 62)
        self.assertEqual(len({x['game_id'] for x in r['rows']}), 62)
        self.assertEqual(r['open_games'] + r['preserved_pass'] + r['conditional_recommendations'], 62)
        self.assertFalse(r['caesars_required_for_recommendation'])
        self.assertEqual(r['recommendation_blocker_counts'].get('MARKET_REFERENCE_MISSING', 0), r['open_games'])
        self.assertTrue(all('CAESARS' not in b for b in r['recommendation_blocker_counts']))

    def test_stale_publication_is_diagnosed_not_retimed(self):
        root = Path('evidence/operational')
        from cfb_neutral_publication_legacy_replay import historical
        m = historical(root / 'CFB_MARKET_MONITOR_STATE.md', 'f96df574ef69a6d1e21139c9c721bd1804295501')
        d = historical(root / 'CFB_DECISION_WAIT_LEDGER.md', '579ee3d16c76663428b3a00e49d4861a8ed512f1')
        lineage = (root / 'CFB_WEEK7_ORIGINAL_FIRST_FROZEN_LINEAGE_2026-10-11.json').read_text()
        r = readiness.audit(m, d, lineage, '2026-10-17T00:31:00Z')
        self.assertTrue(r['saved_state_validated_at_own_boundary_only'])
        self.assertNotEqual(r['canonical_as_of_utc'], r['as_of_utc'])
        self.assertGreater(len(r['elapsed_current_quote_game_ids']), 0)
        self.assertGreater(len(r['overdue_open_decision_game_ids']), 0)


class ReviewWindowTests(unittest.TestCase):
    def window(self, state='PASS', kick='2026-10-18T00:00:00Z',
               cutoff='2026-10-17T23:30:00Z', status='QUALIFIED',
               now='2026-10-17T20:00:00Z'):
        return readiness.review_window(
            {'state': state, 'planning_cutoff_utc': cutoff,
             'reconciliation_utc': '2026-10-17T18:00:00Z'},
            {'kickoff_utc': kick, 'kickoff_status': status}, now)

    def test_pass_remains_in_review_after_reconciliation_deadline(self):
        r = self.window()
        self.assertTrue(r['review_required'])
        self.assertEqual(r['disposition'], 'PASS_FOR_NOW_REEVALUATE')
        self.assertEqual(r['review_due_by_utc'], '2026-10-17T23:30:00Z')

    def test_recommendations_and_inconclusives_also_remain_in_review(self):
        for state in ('CONDITIONAL', 'INCONCLUSIVE'):
            self.assertTrue(self.window(state=state)['review_required'])

    def test_exact_cutoff_closes_without_extending_to_kickoff(self):
        r = self.window(now='2026-10-17T23:30:00Z')
        self.assertFalse(r['review_required'])
        self.assertEqual(r['disposition'], 'PREGAME_WINDOW_CLOSED')

    def test_earlier_kickoff_binds(self):
        r = self.window(kick='2026-10-17T19:00:00Z')
        self.assertFalse(r['review_required'])

    def test_missing_cutoff_does_not_silently_drop_pass(self):
        r = self.window(cutoff=None)
        self.assertTrue(r['review_required'])
        self.assertEqual(r['timing_issue'], 'PRACTICAL_CUTOFF_MISSING')

    def test_unknown_or_unqualified_kickoff_is_visible_debt(self):
        for kick, status in ((None, 'UNAVAILABLE'),
                             ('2026-10-17T19:00:00Z', 'RETAINED_UNVERIFIED')):
            r = self.window(kick=kick, status=status, cutoff=None)
            self.assertTrue(r['review_required'])
            self.assertEqual(r['timing_issue'], 'KICKOFF_REQUIRES_QUALIFICATION')

    def test_no_market_inherits_a_pass(self):
        r = self.window()
        self.assertEqual(r['markets_to_review'], list(readiness.MARKETS))
        self.assertIn('OVER', r['markets_to_review'])
        self.assertIn('UNDER', r['markets_to_review'])
        self.assertIn('AWAY_MONEYLINE', r['markets_to_review'])
        self.assertIn('PARLAY_SUITABILITY', r['markets_to_review'])

    def test_review_requirement_does_not_create_a_decision(self):
        r = self.window()
        self.assertNotIn('acceptable_number', r)
        self.assertNotIn('stake', r)
        self.assertIn('NOT_REOPEN_AUTHORITY', r['scope'])


if __name__ == '__main__': unittest.main()
