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

    def test_authentic_current_neutral_diagnostic(self):
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
        self.assertEqual(r['open_games'] + r['preserved_pass'], 62)
        self.assertFalse(r['caesars_required_for_recommendation'])
        self.assertEqual(r['recommendation_blocker_counts']['MARKET_REFERENCE_MISSING'], r['open_games'])
        self.assertTrue(all('CAESARS' not in b for b in r['recommendation_blocker_counts']))

    def test_stale_publication_is_diagnosed_not_retimed(self):
        root = Path('evidence/operational')
        m = (root / 'CFB_MARKET_MONITOR_STATE.md').read_text()
        d = (root / 'CFB_DECISION_WAIT_LEDGER.md').read_text()
        lineage = (root / 'CFB_WEEK7_ORIGINAL_FIRST_FROZEN_LINEAGE_2026-10-11.json').read_text()
        r = readiness.audit(m, d, lineage, '2026-10-17T00:31:00Z')
        self.assertTrue(r['saved_state_validated_at_own_boundary_only'])
        self.assertNotEqual(r['canonical_as_of_utc'], r['as_of_utc'])
        self.assertGreater(len(r['elapsed_current_quote_game_ids']), 0)
        self.assertGreater(len(r['overdue_open_decision_game_ids']), 0)


if __name__ == '__main__': unittest.main()
