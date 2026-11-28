"""QA-only Monitor continuation replay using the verified Nov. 28 captures."""
import json
from pathlib import Path
import subprocess
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

import cfb_conditional_recommendation_profile as recommendations
import cfb_week13_publication as week
from cfb_cbs_full_board_normalizer import WEEK13_LINEAGE_PATH, normalize, WEEK13_URL
from cfb_saved_publication_audit import audit

BASE = '6620ef3ad0e67e60dae020544897fd630e0497e3'
CAPTURE = 'evidence/operational/CFB_WEEK13_CBS_FBS_TABLES_20261128T143135Z_MANUAL.md'
RECOVERED = '2026-11-28T14:31:35Z'
AT = '2026-11-28T14:36:43Z'
CYCLE = 'CFB_MARKET_MONITOR_20261128T143643Z'
TARGET = '401856877'
GATE = week.gate


class Week13ReassessmentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        operational = Path('evidence/operational')
        cls.market, cls.decision = [
            subprocess.check_output(['git', 'show', f'{BASE}:{operational / name}']).decode()
            for name in ('CFB_MARKET_MONITOR_STATE.md', 'CFB_DECISION_WAIT_LEDGER.md')
        ]
        cls.execution = (operational / 'CFB_EXECUTION_LEDGER.md').read_text()
        cls.scorecard = (operational / 'CFB_POSTGAME_FIRST_FROZEN_SCORECARD.md').read_text()
        cls.lineage = Path(WEEK13_LINEAGE_PATH).read_text()
        cls.prior = GATE.inputs(cls.market, cls.decision, cls.lineage, AT, week.PROFILE)[4]
        cls.source = dict(path=CAPTURE, blob=GATE.blob(Path(CAPTURE).read_text()),
                          recovered_by=RECOVERED)

    def rows(self):
        return [{k: v for k, v in row.items() if k not in ('state_recorded_at_utc', 'state_evidence')}
                for row in self.prior.values()]

    def check_draft(self, market, decision):
        args = (market, decision, self.execution, self.scorecard, self.lineage, AT, week.PROFILE)
        sheet = GATE.render(*args)
        with TemporaryDirectory() as temp:
            path = Path(temp) / 'qa-only.md'
            path.write_text(sheet)
            self.assertEqual(audit(path.read_text(), *args)['integrity']['games'], 69)
        self.assertTrue(market.startswith(self.market))
        self.assertTrue(decision.startswith(self.decision))
        return sheet

    def test_capture_resume_and_no_play(self):
        raw = Path(CAPTURE).read_text()
        board = normalize(raw, self.lineage, RECOVERED, WEEK13_URL, profile=week.PROFILE)
        self.assertEqual(board['coverage']['source_team_rows'], 138)
        # Restart from the persisted capture binding. An expired capture must
        # be refused before replaying with the qualified replacement.
        stale = dict(path='evidence/operational/CFB_WEEK13_CBS_FBS_TABLES_20261128T141240Z_MANUAL.md',
                     recovered_by='2026-11-28T14:12:40Z')
        stale['blob'] = GATE.blob(Path(stale['path']).read_text())
        with self.assertRaisesRegex(ValueError, 'fresh Week13 capture'):
            week.compile(self.market, self.decision, stale, self.lineage, CYCLE, AT, self.rows())
        resumed_source = json.loads(json.dumps(self.source))
        market, decision = week.compile(self.market, self.decision, resumed_source,
                                        self.lineage, CYCLE, AT, self.rows())
        self.assertNotIn('| CONDITIONAL |', self.check_draft(market, decision))

    def test_conditional_preserves_historical_gaps(self):
        rows = self.rows()
        target = next(row for row in rows if row['game_id'] == TARGET)
        review = self.review()
        target.update({key: review[key] for key in
                       ('state', 'acceptable_number', 'reconciliation_utc',
                        'planning_cutoff_utc', 'execution_window')},
                      reason=review['rationale'], cutoff_authority='REVIEW_EVIDENCED',
                      review_ref=dict(path='evidence/operational/recommendation_reviews/QA_ONLY.json',
                                      commit='a' * 40, blob='b' * 40))
        with patch.object(recommendations, 'load_review',
                          return_value=(json.dumps(review), '2026-11-28T14:36:35Z')), \
             patch.object(week, 'load_review', recommendations.load_review):
            market, decision = week.compile(self.market, self.decision, self.source,
                                            self.lineage, CYCLE, AT, rows)
            sheet = self.check_draft(market, decision)
            self.assertEqual(sheet.count('| CONDITIONAL |'), 1)
            self.assertEqual(sheet.count('| HISTORICAL_GAP |'), 3)

    def review(self):
        capture = Path('evidence/operational/CFB_WEEK13_NOV28_SATURDAY_ESPN_DK_BENCHMARKS.json')
        benchmark = json.loads(capture.read_text())['observations']['Kansas']
        quote_at = '2026-11-28T14:35:56Z'
        kickoff = '2026-11-28T23:15:00Z'
        official = 'https://kuathletics.com/news/2026/11/23/football-jayhawks-travel-to-stillwater-to-take-on-cowboys'
        selection = dict(game_id=TARGET, market='TOTAL', selection='under',
                         period='PREGAME_FULL_GAME')
        quote = dict(selection, book='DraftKings', operator='DraftKings',
                     source_url=benchmark['source'], operator_evidence_url=benchmark['operator_link'],
                     retrieved_at=quote_at, offer_updated_at=None, line=65.5, price=-115)
        previous = json.dumps(self.prior[TARGET], sort_keys=True, separators=(',', ':'))
        return dict(schema=recommendations.RECONSIDERATION_REVIEW_SCHEMA,
                    game_id=TARGET, state='CONDITIONAL', recorded_at_utc='2026-11-28T14:36:30Z',
                    original_lineage_blob=week.WEEK13_LINEAGE_SHA, maturity='CONTROLLED_BETA_RECOMMENDATION',
                    market='TOTAL', selection='under', rationale='QA fixture only',
                    model_review='QA model assumption', uncertainty='QA uncertainty',
                    decision_rule='QA decision rule', source_qualification='QA source boundary',
                    cutoff_basis='QA-only hypothetical cutoff',
                    material_sources=[dict(url=official, retrieved_at=quote_at, finding='QA source binding')],
                    market_reference=dict(selection, kickoff_utc=kickoff, kickoff_source_url=official,
                                          collection_start=quote_at, collection_end=quote_at,
                                          quotes=[quote], clock_semantics='RESPONSE_RECOVERED_BY'),
                    reconsideration=dict(prior_row_blob=GATE.blob(previous), reason='QA reconsideration'),
                    acceptable_number=dict(market='TOTAL', selection='under', line=65.5,
                                           minimum_price=-115, direction='AT_LEAST'),
                    reconciliation_utc='2026-11-28T15:00:00Z',
                    planning_cutoff_utc='2026-11-28T22:00:00Z',
                    execution_window=dict(start_utc='2026-11-28T14:36:40Z', end_utc='2026-11-28T22:00:00Z'))


if __name__ == '__main__':
    unittest.main()
