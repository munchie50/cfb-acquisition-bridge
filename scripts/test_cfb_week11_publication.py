"""Exercise Week 11 with retained source and synthetic decision fixtures."""
import unittest
from datetime import timedelta

import cfb_neutral_publication_gate as gate
import cfb_week11_publication as week


class Week11PublicationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        evidence = week.ROOT / 'evidence'
        cls.lineage = (evidence / 'audits/CFB_WEEK11_ORIGINAL_ANCESTRY_RECOVERY_20261109.json').read_text()
        root = '```' + week.SOURCE_TAG + '\n'
        cls.market = (evidence / 'operational/CFB_MARKET_MONITOR_STATE.md').read_text().split(root, 1)[0]
        cls.decision = (evidence / 'operational/CFB_DECISION_WAIT_LEDGER.md').read_text().split(root, 1)[0]
        cls.capture = (week.ROOT / week.FIRST_SOURCE['path']).read_text()
        cls.as_of = week.FIRST_SOURCE['recovered_by']
        clock = gate.clock(cls.as_of)
        cls.cycle = clock.strftime('CFB_MARKET_MONITOR_%Y%m%dT%H%M%SZ')
        cls.rows = [{
            'game_id': gid, 'state': 'INCONCLUSIVE', 'reason': 'Synthetic test only',
            'reconciliation_utc': (clock + timedelta(hours=1)).isoformat(),
            'planning_cutoff_utc': None, 'cutoff_authority': 'UNVERIFIED',
            'acceptable_number': None, 'execution_window': None,
        } for gid in week.first_rows(cls.lineage)]

    def proposal(self, market=None, recovered_by=None):
        return week.compile(
            self.market if market is None else market, self.decision, self.capture,
            self.lineage, self.cycle, self.as_of, recovered_by or self.as_of, self.rows,
        )

    def test_bootstrap_render_and_readback(self):
        market, decision = self.proposal()
        self.assertTrue(market.startswith(self.market))
        self.assertTrue(decision.startswith(self.decision))
        self.assertEqual(gate.bootstrap(market, decision, self.lineage, 'WEEK11'),
                         'PASS_WEEK11_ORIGINAL_AND_FIRST_SOURCE_BOOTSTRAP_ONLY')
        args = (market, decision, '', '', self.lineage, self.as_of, 'WEEK11')
        self.assertEqual(gate.audit(gate.render(*args), *args)['games'], 67)

    def test_parent_and_source_age_fail_closed(self):
        with self.assertRaisesRegex(ValueError, 'parent'):
            self.proposal(market=self.market + '\n')
        stale = (gate.clock(self.as_of) - timedelta(seconds=901)).isoformat()
        with self.assertRaisesRegex(ValueError, 'fifteen minutes'):
            self.proposal(recovered_by=stale)

    def test_changed_lineage_and_incomplete_source_fail_closed(self):
        with self.assertRaisesRegex(ValueError, 'identity baseline'):
            week.board(self.capture, self.lineage + '\n', self.as_of)
        incomplete = '\n'.join(self.capture.splitlines()[:-4])
        with self.assertRaisesRegex(ValueError, 'incomplete source'):
            week.board(incomplete, self.lineage, self.as_of)
