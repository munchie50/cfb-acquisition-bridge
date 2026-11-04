"""Authentic retained Week10 sources with explicitly hypothetical QA clocks.

Synthetic pending decisions never represent production research or new offers.
"""
import copy
import json
import os
import unittest
from pathlib import Path

import cfb_hot_sheet_readiness as readiness
import cfb_neutral_publication_gate as gate
import cfb_week10_frozen_field_invariant as frozen
import cfb_week10_publication as week
from cfb_neutral_publication_legacy_replay import historical, packet

ROOT = Path(__file__).resolve().parents[1]
AT = '2026-11-04T17:56:00Z'
BY = '2026-11-04T17:55:30Z'
CYCLE = 'CFB_PRESENTATION_RECONCILIATION_20261104T175530Z'


class Week10Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.market = historical(ROOT / 'evidence/operational/CFB_MARKET_MONITOR_STATE.md', week.MARKET_PARENT)
        cls.decision = historical(ROOT / 'evidence/operational/CFB_DECISION_WAIT_LEDGER.md', week.DECISION_PARENT)
        cls.lineage = (ROOT / 'evidence/scheduler_qa/CFB_WEEK10_ORIGINAL_ANCESTRY_RECOVERY_20261104.json').read_text()
        cls.capture = (ROOT / week.FIRST_SOURCE['path']).read_text()
        cls.rows = [dict(game_id=r['game_id'],
                         state='HISTORICAL_GAP' if r['game_id'] in week.RECOVERY_GAPS else 'INCONCLUSIVE',
                         reason='SYNTHETIC QA ONLY missing historical decision' if r['game_id'] in week.RECOVERY_GAPS else 'SYNTHETIC QA ONLY pending independent review',
                         reconciliation_utc=None if r['game_id'] in week.RECOVERY_GAPS else '2026-11-04T23:00:00Z',
                         planning_cutoff_utc=None, cutoff_authority='UNVERIFIED',
                         acceptable_number=None, execution_window=None)
                    for r in json.loads(cls.lineage)['rows']]
        cls.pm, cls.pd = cls.build()
        cls.sheet = gate.render(cls.pm, cls.pd, 'execution fixture', 'scorecard fixture', cls.lineage, AT, 'WEEK10')

    @classmethod
    def build(cls, **changes):
        values = dict(market=cls.market, decision=cls.decision, capture=cls.capture,
                      lineage=cls.lineage, cycle=CYCLE, as_of=AT, recovered_by=BY,
                      decision_rows=cls.rows)
        values.update(changes)
        return week.compile(**values)

    @classmethod
    def advance(cls, **changes):
        values = dict(market=cls.pm, decision=cls.pd, cycle='CFB_PRESENTATION_RECONCILIATION_20261104T175700Z',
                      as_of='2026-11-04T17:58:00Z', recovered_by='2026-11-04T17:57:00Z')
        values.update(changes)
        return cls.build(**values)

    def test_all_dated_retained_sources_supply_earliest_observations(self):
        rows = week.first_rows(self.lineage)
        by_clock = {}
        for row in rows.values():
            if row['first'] is not None:
                stamp = row['first']['retrieved_at']
                by_clock[stamp] = by_clock.get(stamp, 0) + 1
        self.assertEqual(sum(by_clock.values()), 60)
        self.assertEqual(by_clock[week.FIRST_SOURCE['recovered_by']], 17)
        self.assertEqual(by_clock[week.RETAINED_SOURCES[-1]['recovered_by']], 43)
        changed = copy.deepcopy(week.RETAINED_SOURCES)
        changed[-1]['blob'] = '0' * 40
        from unittest.mock import patch
        with patch.object(week, 'RETAINED_SOURCES', changed), self.assertRaises(ValueError):
            week.first_rows(self.lineage)

    def test_exact_original_identity_and_whole_render(self):
        result = gate.audit(self.sheet, self.pm, self.pd, 'execution fixture', 'scorecard fixture', self.lineage, AT, 'WEEK10')
        self.assertIn('PASS', result['verdict'])
        self.assertEqual(sum(line.startswith('| ') and ' @ ' in line for line in self.sheet.splitlines()), 63)
        self.assertIn('55 predictions and 8 exclusions', self.sheet)
        self.assertIn('Merrimack @ Wake Forest', self.sheet)
        self.assertIn('2 HISTORICAL_GAP', self.sheet)

    def test_original_archive_field_invariant(self):
        first = os.environ.get('CFB_ACCEPTED_FREEZE_ARCHIVE')
        if not first:
            self.skipTest('accepted original archive path required')
        result = frozen.audit(self.sheet, self.lineage, Path(first))
        self.assertEqual(result['numeric_fields'], 165)
        with self.assertRaises(ValueError):
            frozen.audit(self.sheet.replace('55 predictions and 8 exclusions', '63 predictions and 0 exclusions'), self.lineage, Path(first))

    def test_prior_history_and_retained_first_observations(self):
        self.assertTrue(self.pm.startswith(self.market))
        self.assertTrue(self.pd.startswith(self.decision))
        self.assertEqual(week.bootstrap_check(self.pm, self.pd, self.lineage), 'PASS_WEEK10_ORIGINAL_AND_FIRST_SOURCE_BOOTSTRAP_ONLY')
        current = gate.inputs(self.pm, self.pd, self.lineage, AT, 'WEEK10')
        for gid, row in week.first_rows(self.lineage).items():
            self.assertEqual(current[3][gid]['first'], row['first'])

    def test_readiness_exposes_unfinished_review_and_gaps(self):
        result = readiness.audit(self.pm, self.pd, self.lineage, AT, 'WEEK10')
        self.assertEqual(result['games'], 63)
        self.assertEqual(sum(r['state'] == 'HISTORICAL_GAP' for r in result['rows']), 2)
        self.assertEqual(result['evaluation_coverage']['counts']['HISTORICAL_GAP'], 2)
        self.assertEqual(result['evaluation_coverage']['counts']['ORIGINAL_EXCLUSION'], 8)

    def test_wrong_parent_and_lineage_rejected(self):
        for changes in ({'market': self.market + '\n'}, {'decision': self.decision + '\n'}, {'lineage': self.lineage + '\n'}):
            with self.subTest(changes=list(changes)), self.assertRaises(ValueError):
                self.build(**changes)

    def test_missing_duplicate_decision_or_source_rejected(self):
        for rows in (self.rows[:-1], self.rows[:-1] + [self.rows[0]]):
            with self.subTest(rows=len(rows)), self.assertRaises(ValueError):
                self.build(decision_rows=rows)
        lines = self.capture.splitlines(keepends=True)
        team = next(i for i, line in enumerate(lines) if line.startswith('|') and '[Ohio](https://www.cbssports.com/college-football/teams/OHIO/' in line)
        with self.assertRaises(ValueError):
            self.build(capture=''.join(lines[:team] + lines[team + 1:]))

    def test_stale_future_and_backdated_recovery_rejected(self):
        for changes in ({'as_of': '2026-11-04T18:11:00Z'}, {'as_of': '2026-11-04T17:55:00Z'},
                        {'as_of': '2026-11-04T17:55:05Z', 'recovered_by': '2026-11-04T17:55:04Z', 'cycle': 'CFB_PRESENTATION_RECONCILIATION_20261104T175504Z'}):
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                self.build(**changes)

    def test_gap_cannot_be_pass_or_future_game_gap(self):
        for gid, state in [('401866453', 'PASS'), ('401866455', 'HISTORICAL_GAP')]:
            rows = copy.deepcopy(self.rows)
            row = next(r for r in rows if r['game_id'] == gid)
            row['state'] = state
            row['reconciliation_utc'] = None
            with self.subTest(game=gid), self.assertRaises(ValueError):
                self.build(decision_rows=rows)

    def test_gap_cannot_claim_limit_deadline_or_execution(self):
        for field, value in [('planning_cutoff_utc', '2026-11-04T23:00:00Z'),
                             ('reconciliation_utc', '2026-11-04T23:00:00Z'),
                             ('acceptable_number', 1.5), ('execution_window', 'invented'),
                             ('cutoff_authority', 'VERIFIED')]:
            rows = copy.deepcopy(self.rows)
            next(r for r in rows if r['game_id'] == '401866453')[field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                self.build(decision_rows=rows)

    def test_gap_history_exactly_preserved_on_advance(self):
        pm, pd = self.advance()
        before = gate.inputs(self.pm, self.pd, self.lineage, AT, 'WEEK10')
        after = gate.inputs(pm, pd, self.lineage, '2026-11-04T17:58:00Z', 'WEEK10')
        for gid in week.RECOVERY_GAPS:
            self.assertEqual(before[4][gid], after[4][gid])
        self.assertEqual(week.recovery_context(pm, pd, self.lineage), week.recovery_context(self.pm, self.pd, self.lineage))

    def test_gap_cannot_change_reopen_or_expand_on_advance(self):
        for gid, field, value in [('401866453', 'reason', 'Changed missing history'),
                                  ('401866453', 'state', 'PASS'),
                                  ('401866455', 'state', 'HISTORICAL_GAP')]:
            rows = copy.deepcopy(self.rows)
            row = next(r for r in rows if r['game_id'] == gid)
            row[field] = value
            if value == 'HISTORICAL_GAP':
                row['reconciliation_utc'] = None
            with self.subTest(field=field, value=value), self.assertRaises(ValueError):
                self.advance(decision_rows=rows)

    def test_recovery_declaration_cannot_reset_backdate_or_expand(self):
        for mutation in ('reset', 'backdate', 'expand'):
            pm, pd = self.pm, self.pd
            if mutation == 'reset':
                pm = pm.replace(AT, '2026-11-04T17:57:00Z')
            elif mutation == 'backdate':
                pm = pm.replace('"as_of_utc": "' + AT + '"', '"as_of_utc": "2026-11-04T17:55:05Z"', 1)
                pd = pd.replace('"as_of_utc": "' + AT + '"', '"as_of_utc": "2026-11-04T17:55:05Z"', 1)
            else:
                pm = pm.replace('"401866454"\n', '"401866454", "401866455"\n', 1)
                pd = pd.replace('"401866454"\n', '"401866454", "401866455"\n', 1)
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                week.bootstrap_check(pm, pd, self.lineage)

    def test_earliest_observation_and_untyped_tail_cannot_change(self):
        m = gate.selected_block(self.pm, week.MARKET_TAG, gate.WEEKLY_MARKET_SCHEMA, gate.clock(AT))
        next(r for r in m['rows'] if r['first'])['first'] = None
        prefix = self.pm[:self.pm.rfind('```' + week.MARKET_TAG)]
        bad = prefix + packet(m, week.MARKET_TAG).lstrip('\n')
        with self.assertRaises(ValueError):
            week.bootstrap_check(bad, self.pd, self.lineage)
        with self.assertRaises(ValueError):
            week.bootstrap_check(self.pm + 'Unqualified publication tail\n', self.pd, self.lineage)

    def test_conditional_missing_or_invalid_review_rejected(self):
        for ref in (None, {'commit': '0' * 40, 'blob': '0' * 40, 'path': 'evidence/absent.json'}):
            rows = copy.deepcopy(self.rows)
            row = next(r for r in rows if r['game_id'] == '401866455')
            row.update(state='CONDITIONAL', review_ref=ref)
            with self.subTest(ref=ref), self.assertRaises((ValueError, TypeError)):
                self.build(decision_rows=rows)

    def test_initial_recovery_cannot_expand_after_another_kickoff(self):
        with self.assertRaises(ValueError):
            self.build(as_of='2026-11-05T00:01:00Z', recovered_by='2026-11-05T00:00:30Z',
                       cycle='CFB_PRESENTATION_RECONCILIATION_20261105T000030Z')


if __name__ == '__main__':
    unittest.main()
