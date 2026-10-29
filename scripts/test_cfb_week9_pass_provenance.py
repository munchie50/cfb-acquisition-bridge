"""Retained source replay with synthetic changed judgments, never live research."""
import copy
import json
from pathlib import Path
import unittest
import cfb_week9_publication as week
import cfb_neutral_publication_gate as gate

ROOT = Path(__file__).resolve().parents[1]
AT = '2026-10-29T18:09:30Z'
CYCLE = 'CFB_MARKET_MONITOR_20261029T180930Z'


class PassProvenanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.market = (ROOT / 'evidence/operational/CFB_MARKET_MONITOR_STATE.md').read_text()
        cls.decision = (ROOT / 'evidence/operational/CFB_DECISION_WAIT_LEDGER.md').read_text()
        cls.capture = (ROOT / 'evidence/operational/CFB_CBS_WEEK9_TEXT_TABLE_CAPTURE_20261029T180541Z.md').read_text()
        cls.lineage = (ROOT / 'evidence/scheduler_qa/CFB_WEEK9_ORIGINAL_ANCESTRY_RECOVERY_20261025.json').read_text()
        cls.old = gate.inputs(cls.market, cls.decision, cls.lineage, AT, 'WEEK9')[4]

    def compile(self, change=None):
        rows = [{k: v for k, v in row.items() if k not in ('state_recorded_at_utc', 'state_evidence')}
                for row in copy.deepcopy(self.old).values()]
        if change:
            change(rows)
        # Retained capture with explicit synthetic replay clocks; never publish.
        return week.compile(self.market, self.decision, self.capture, self.lineage,
                            CYCLE, AT, AT, rows)

    def test_future_reassessment_keeps_original_state_origin_and_new_packet_reason(self):
        gid = '401869963'  # Troy @ JMU, future at retained boundary
        def change(rows):
            next(r for r in rows if r['game_id'] == gid)['reason'] = 'SYNTHETIC QA ONLY changed prospective PASS assessment'
        m, d = self.compile(change)
        new = gate.inputs(m, d, self.lineage, AT, 'WEEK9')[4]
        self.assertEqual(new[gid]['state_evidence'], self.old[gid]['state_evidence'])
        self.assertEqual(new[gid]['state_recorded_at_utc'], self.old[gid]['state_recorded_at_utc'])
        self.assertEqual(new[gid]['reason'], 'SYNTHETIC QA ONLY changed prospective PASS assessment')
        packet = gate.selected_block(d, week.DECISION_TAG, gate.WEEKLY_DECISION_SCHEMAS, gate.clock(AT))
        self.assertEqual(packet['cycle_id'], CYCLE)
        self.assertTrue(m.startswith(self.market))
        self.assertTrue(d.startswith(self.decision))
        other = next(k for k, v in self.old.items() if k != gid and v['state'] == 'PASS')
        self.assertEqual(new[other], self.old[other])

    def test_exact_carry_does_not_claim_new_review_clock(self):
        m, d = self.compile()
        self.assertEqual(gate.inputs(m, d, self.lineage, AT, 'WEEK9')[4], self.old)

    def test_changed_elapsed_pass_cannot_borrow_pregame_origin(self):
        source = gate.inputs(self.market, self.decision, self.lineage, AT, 'WEEK9')[3]
        gid = next(k for k, v in self.old.items()
                   if v['state'] == 'PASS' and gate.clock(source[k]['kickoff_utc']) < gate.clock(AT))
        def change(rows):
            next(r for r in rows if r['game_id'] == gid)['reason'] = 'SYNTHETIC QA ONLY postkickoff rewrite'
        with self.assertRaisesRegex(ValueError, 'postkickoff|elapsed'):
            self.compile(change)


if __name__ == '__main__':
    unittest.main()
