import unittest
from pathlib import Path
import cfb_saved_publication_audit as saved
from cfb_neutral_publication_legacy_replay import historical


class SavedPublicationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        root = Path('evidence/operational')
        cls.args = [(root / 'CFB_WEEK7_HOT_SHEET_2026-10-16_1301CT.md').read_text(),
            historical(root / 'CFB_MARKET_MONITOR_STATE.md', 'f96df574ef69a6d1e21139c9c721bd1804295501'),
            historical(root / 'CFB_DECISION_WAIT_LEDGER.md', '579ee3d16c76663428b3a00e49d4861a8ed512f1'),
            historical(root / 'CFB_EXECUTION_LEDGER.md', '75caee4052e02ea7d2453d1d37fd3866e13ecc07'),
            historical(root / 'CFB_POSTGAME_FIRST_FROZEN_SCORECARD.md', '4380a04b9ce285288861e910fc7b754f977529d1'),
            (root / 'CFB_WEEK7_ORIGINAL_FIRST_FROZEN_LINEAGE_2026-10-11.json').read_text()]

    def test_live_gate_still_rejects_stale_pregame(self):
        with self.assertRaisesRegex(ValueError, 'elapsed game'):
            saved.gate.audit(*self.args, '2026-10-17T00:00:00Z')

    def test_saved_integrity_and_stale_exception_are_separate(self):
        r = saved.audit(*self.args, '2026-10-17T00:31:00Z')
        self.assertEqual(r['verdict'], 'PASS_SAVED_PUBLICATION_INTEGRITY_ONLY')
        self.assertEqual(len(r['elapsed_current_quote_game_ids']), 3)
        self.assertEqual(len(r['overdue_open_decision_game_ids']), 13)
        self.assertEqual(r['current_operational_acceptance'], 'NOT_CERTIFIED')

    def test_saved_header_cannot_retime_source_boundary(self):
        args = self.args.copy()
        args[0] = args[0].replace('2026-10-16T18:01:27Z', '2026-10-16T18:01:28Z')
        with self.assertRaises(ValueError): saved.audit(*args, '2026-10-17T00:00:00Z')

    def test_future_boundary_and_missing_boundary_rejected(self):
        with self.assertRaises(ValueError): saved.audit(*self.args, '2026-10-16T17:00:00Z')
        args = self.args.copy(); args[0] = args[0].replace('**Publication boundary:**', '**Missing:**')
        with self.assertRaises(ValueError): saved.audit(*args, '2026-10-17T00:00:00Z')

    def test_source_binding_and_sheet_tamper_rejected(self):
        for index, value in ((0, self.args[0].replace('52 INCONCLUSIVE', '51 INCONCLUSIVE')),
                             (3, self.args[3] + '\nChanged execution')):
            args = self.args.copy(); args[index] = value
            with self.assertRaises(ValueError): saved.audit(*args, '2026-10-17T00:00:00Z')


if __name__ == '__main__': unittest.main()
