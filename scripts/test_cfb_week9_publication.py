"""Authentic retained source with explicitly synthetic decision/replay clocks.

No test packet is a production review, current quote or earned decision.
"""
import copy
import json
import os
import unittest
from pathlib import Path
import cfb_neutral_publication_gate as gate
import cfb_week9_publication as week
import cfb_week9_frozen_field_invariant as frozen
import cfb_hot_sheet_readiness as readiness
from cfb_cbs_full_board_normalizer import normalize, WEEK9_URL
from cfb_neutral_publication_legacy_replay import historical, packet

ROOT = Path(__file__).resolve().parents[1]
AT = '2026-10-25T15:55:00Z'
BY = week.FIRST_SOURCE['recovered_by']
CYCLE = 'CFB_PRESENTATION_RECONCILIATION_20261025T154819Z'


class Week9Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.market = historical(ROOT / 'evidence/operational/CFB_MARKET_MONITOR_STATE.md', week.MARKET_PARENT)
        cls.decision = historical(ROOT / 'evidence/operational/CFB_DECISION_WAIT_LEDGER.md', week.DECISION_PARENT)
        cls.lineage = (ROOT / 'evidence/scheduler_qa/CFB_WEEK9_ORIGINAL_ANCESTRY_RECOVERY_20261025.json').read_text()
        cls.capture = (ROOT / week.FIRST_SOURCE['path']).read_text()
        cls.rows = [{'game_id': r['game_id'], 'state': 'INCONCLUSIVE',
                     'reason': 'SYNTHETIC QA ONLY pending independent material review',
                     'reconciliation_utc': '2026-10-26T18:00:00Z', 'planning_cutoff_utc': None,
                     'cutoff_authority': 'UNVERIFIED', 'acceptable_number': None, 'execution_window': None}
                    for r in json.loads(cls.lineage)['rows']]
        cls.pm, cls.pd = cls.build()
        cls.sheet = gate.render(cls.pm, cls.pd, 'execution fixture', 'scorecard fixture', cls.lineage, AT, 'WEEK9')

    @classmethod
    def build(cls, **changes):
        values = dict(market=cls.market, decision=cls.decision, capture=cls.capture,
                      lineage=cls.lineage, cycle=CYCLE, as_of=AT, recovered_by=BY,
                      decision_rows=cls.rows)
        values.update(changes)
        return week.compile(**values)

    def test_complete_source_and_exact_directed_census(self):
        r = normalize(self.capture, self.lineage, BY, source_url=WEEK9_URL, profile='WEEK9')
        self.assertEqual(r['coverage']['matched_games'], 56)
        self.assertEqual(r['coverage']['source_team_rows'], 112)
        self.assertEqual(r['coverage']['future_games'], 56)
        self.assertEqual(r['consensus'], 'CONSENSUS_UNAVAILABLE')
        self.assertEqual(r['caesars'], 'UNVERIFIED')

    def test_history_and_first_observations_preserved(self):
        self.assertTrue(self.pm.startswith(self.market))
        self.assertTrue(self.pd.startswith(self.decision))
        r = gate.inputs(self.pm, self.pd, self.lineage, AT, 'WEEK9')
        for gid, expected in week.first_rows(self.lineage).items():
            self.assertEqual(r[3][gid]['first'], expected['first'])
        self.assertEqual(week.bootstrap_check(self.pm, self.pd, self.lineage), 'PASS_WEEK9_ORIGINAL_AND_FIRST_SOURCE_BOOTSTRAP_ONLY')

    def test_whole_render_and_exactly_once_with_exclusion_separators(self):
        gate.audit(self.sheet, self.pm, self.pd, 'execution fixture', 'scorecard fixture', self.lineage, AT, 'WEEK9')
        self.assertEqual(sum(l.startswith('| ') and ' @ ' in l for l in self.sheet.splitlines()), 56)
        self.assertIn('Nebraska', self.sheet)
        self.assertIn('45 predictions and 11 exclusions', self.sheet)

    def test_research_debt_is_visible(self):
        r = readiness.audit(self.pm, self.pd, self.lineage, AT, 'WEEK9')
        self.assertEqual(r['games'], 56)
        self.assertEqual(r['evaluation_coverage']['counts']['ORIGINAL_EXCLUSION'], 11)
        self.assertEqual(r['evaluation_coverage']['counts']['NOT_CERTIFIED'], 45)

    def test_original_archive_field_invariant(self):
        archive = os.environ.get('CFB_ACCEPTED_FREEZE_ARCHIVE')
        if not archive:
            self.skipTest('accepted original archive path required')
        result = frozen.audit(self.sheet, self.lineage, Path(archive))
        self.assertEqual(result['numeric_fields'], 135)
        with self.assertRaises(ValueError):
            frozen.audit(self.sheet.replace('45 predictions and 11 exclusions', '46 predictions and 10 exclusions'), self.lineage, Path(archive))

    def test_bad_parent_or_lineage_rejected(self):
        for changes in ({'market': self.market + '\n'}, {'decision': self.decision + '\n'}, {'lineage': self.lineage + '\n'}):
            with self.subTest(changes=list(changes)), self.assertRaises(ValueError):
                self.build(**changes)

    def test_incomplete_source_or_decision_union_rejected(self):
        lines = self.capture.splitlines(keepends=True)
        first_team = next(i for i, line in enumerate(lines) if line.startswith('| [Delaware]'))
        with self.assertRaises(ValueError):
            self.build(capture=''.join(lines[:first_team] + lines[first_team + 1:]))
        with self.assertRaises(ValueError):
            self.build(decision_rows=self.rows[:-1])

    def test_source_page_and_unqualified_profile_rejected(self):
        with self.assertRaises(ValueError):
            normalize(self.capture, self.lineage, BY, source_url=WEEK9_URL.replace('week-9', 'week-8'), profile='WEEK9')
        with self.assertRaises(ValueError):
            gate.profile_config('WEEK10')

    def test_stale_or_future_source_rejected(self):
        for at in ('2026-10-25T16:10:00Z', '2026-10-25T15:40:00Z'):
            with self.subTest(at=at), self.assertRaisesRegex(ValueError, 'fresh source'):
                self.build(as_of=at)

    def test_no_initial_elapsed_decision_reconstruction(self):
        with self.assertRaisesRegex(ValueError, 'elapsed decisions'):
            self.build(as_of='2026-11-01T15:55:00Z', recovered_by='2026-11-01T15:54:00Z')

    def test_root_first_capture_or_untyped_tail_cannot_change(self):
        with self.assertRaises(ValueError):
            week.bootstrap_check(self.pm.replace(week.FIRST_SOURCE['blob'], '0' * 40, 1), self.pd, self.lineage)
        with self.assertRaisesRegex(ValueError, 'untyped'):
            week.bootstrap_check(self.pm + 'Unqualified publication tail\n', self.pd, self.lineage)

    def test_earliest_quote_cannot_be_deleted(self):
        m = gate.selected_block(self.pm, week.MARKET_TAG, gate.WEEKLY_MARKET_SCHEMA, gate.clock(AT))
        next(r for r in m['rows'] if r['first'])['first'] = None
        prefix = self.pm[:self.pm.rfind('```' + week.MARKET_TAG)]
        with self.assertRaisesRegex(ValueError, 'earliest observation'):
            week.bootstrap_check(prefix + packet(m, week.MARKET_TAG).lstrip('\n'), self.pd, self.lineage)

    def test_richer_earned_state_not_silently_downgraded(self):
        rows = copy.deepcopy(self.rows)
        rows[0]['state'] = 'CONDITIONAL'
        with self.assertRaisesRegex(ValueError, 'richer decision'):
            self.build(decision_rows=rows)

    def test_overdue_decision_and_unchanged_source_advance_rejected(self):
        rows = copy.deepcopy(self.rows)
        rows[0]['reconciliation_utc'] = '2026-10-25T15:50:00Z'
        with self.assertRaises(ValueError):
            self.build(decision_rows=rows)
        with self.assertRaisesRegex(ValueError, 'advance current boundary'):
            self.build(market=self.pm, decision=self.pd)


if __name__ == '__main__':
    unittest.main()
