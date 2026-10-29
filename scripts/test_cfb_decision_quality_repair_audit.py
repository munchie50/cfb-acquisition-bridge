"""Authentic failure replay plus diagnostic rejection/false-positive controls."""
import copy
import json
from pathlib import Path
import unittest
from cfb_decision_quality_repair_audit import audit

ROOT = Path(__file__).resolve().parents[1] / 'evidence/operational'


class RepairAuditTests(unittest.TestCase):
    def setUp(self):
        self.prior = json.loads((ROOT / 'CFB_MARKET_MONITOR_20261029T115755Z_REVALIDATION.json').read_text())
        self.current = json.loads((ROOT / 'CFB_MARKET_MONITOR_20261029T180541Z_REVALIDATION.json').read_text())

    def test_authentic_stale_reasoning_and_population(self):
        result = audit(self.prior, self.current)
        games = {f['game'] for f in result['findings']}
        self.assertTrue({'Troy @ James Madison', 'Baylor @ UCF', 'Tulane @ Charlotte'} <= games)
        self.assertEqual(sum(result['separated_counts'].values()), 56)
        self.assertEqual(result['separated_counts']['original_exclusion'], 11)
        self.assertEqual(result['separated_counts']['future_pass_recorded_not_semantically_certified'], 36)

    def test_unchanged_prices_are_not_flagged(self):
        current = copy.deepcopy(self.prior)
        current['as_of_utc'] = self.current['as_of_utc']
        self.assertEqual(audit(self.prior, current)['findings'], [])

    def test_reversed_clocks_rejected(self):
        with self.assertRaises(ValueError):
            audit(self.current, self.prior)

    def test_duplicate_identity_rejected(self):
        self.current['cases'].append(copy.deepcopy(self.current['cases'][0]))
        with self.assertRaises(ValueError):
            audit(self.prior, self.current)


if __name__ == '__main__':
    unittest.main()
