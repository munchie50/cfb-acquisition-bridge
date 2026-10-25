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

    def test_authentic_retained_diagnostic_covers_all_qualified_states(self):
        root = Path('evidence/operational')
        from cfb_neutral_publication_legacy_replay import historical
        m = historical(root / 'CFB_MARKET_MONITOR_STATE.md', '87d735251e328226087daa9aa1519c22c702a762')
        d = historical(root / 'CFB_DECISION_WAIT_LEDGER.md', '65b87247a18060069402d9814692ab57ce97dcf3')
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


class EvaluationCoverageTests(unittest.TestCase):
    def setUp(self):
        self.census = {str(i): {'first_frozen_status': 'PREDICTION'} for i in range(6)}
        self.census['4']['first_frozen_status'] = 'EXCLUDED'
        states = ['PASS', 'INCONCLUSIVE', 'CONDITIONAL', 'HISTORICAL_GAP', 'PASS', 'PASS']
        self.decisions = {str(i): {'state': state, 'reason': 'Saved original reason',
                                  'review_ref': {'blob': 'saved'} if state == 'CONDITIONAL' else None}
                          for i, state in enumerate(states)}
        self.rows = [{'game_id': str(i), 'review_window': {
                      'review_required': i not in (3, 5),
                      'review_due_by_utc': '2026-10-17T23:00:00Z' if i != 1 else None,
                      'timing_issue': 'KICKOFF_REQUIRES_QUALIFICATION' if i == 1 else None}}
                     for i in range(6)]

    def test_full_identity_accounting_does_not_certify_pass(self):
        r = readiness.evaluation_coverage(self.census, self.decisions, self.rows)
        self.assertEqual(sum(r['counts'].values()), 6)
        self.assertEqual(r['game_ids']['NOT_CERTIFIED'], ['0', '1', '5'])
        self.assertEqual(r['counts']['CONDITIONAL_REVIEW_REFERENCE'], 1)
        self.assertEqual(r['counts']['ORIGINAL_EXCLUSION'], 1)
        self.assertEqual(r['counts']['HISTORICAL_GAP'], 1)
        self.assertFalse(r['historical_backfill_authorized'])

    def test_pending_queue_preserves_unknown_timing_and_drops_closed_games(self):
        r = readiness.evaluation_coverage(self.census, self.decisions, self.rows)
        self.assertEqual([x['game_id'] for x in r['uncertified_open_review_queue']], ['1', '0'])
        self.assertEqual(self.rows[5]['evaluation_coverage'], 'NOT_CERTIFIED')

    def test_deadlines_are_sorted_as_clocks_not_offset_text(self):
        self.rows[0]['review_window']['review_due_by_utc'] = '2026-10-17T18:00:00-05:00'
        self.rows[1]['review_window']['review_due_by_utc'] = '2026-10-17T22:00:00Z'
        r = readiness.evaluation_coverage(self.census, self.decisions, self.rows)
        self.assertEqual([x['game_id'] for x in r['uncertified_open_review_queue']], ['1', '0'])

    def test_original_exclusion_cannot_be_promoted_by_a_conditional_label(self):
        self.decisions['4'].update(state='CONDITIONAL', review_ref={'blob': 'saved'})
        r = readiness.evaluation_coverage(self.census, self.decisions, self.rows)
        self.assertIn('4', r['game_ids']['ORIGINAL_EXCLUSION'])
        self.assertNotIn('4', r['game_ids']['CONDITIONAL_REVIEW_REFERENCE'])

    def test_missing_duplicate_or_mismatched_identities_rejected(self):
        for kind in ('missing', 'duplicate', 'decision'):
            rows = copy.deepcopy(self.rows)
            decisions = copy.deepcopy(self.decisions)
            if kind == 'missing': rows.pop()
            elif kind == 'duplicate': rows[-1]['game_id'] = '0'
            else: decisions.pop('0')
            with self.assertRaises(ValueError):
                readiness.evaluation_coverage(self.census, decisions, rows)

    def test_saved_reasons_and_decisions_are_not_rewritten(self):
        before = copy.deepcopy(self.decisions)
        readiness.evaluation_coverage(self.census, self.decisions, self.rows)
        self.assertEqual(before, self.decisions)
        self.assertEqual(self.rows[0]['saved_reason'], 'Saved original reason')


if __name__ == '__main__': unittest.main()
