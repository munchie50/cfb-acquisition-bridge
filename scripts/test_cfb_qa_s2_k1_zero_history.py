"""Frozen source-context examples; no model, predictions, outcomes or raw inputs."""
import ast
import unittest
from pathlib import Path
import numpy as np

source = Path(__file__).with_name('cfb_qa_prospective_s2_k1_consumer_v1_2026_09_30.py')
tree = ast.parse(source.read_text())
function = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'opponent_residuals')
namespace = {'np': np}
exec(compile(ast.Module(body=[function], type_ignores=[]), str(source), 'exec'), namespace)
residuals = namespace['opponent_residuals']


class FrozenContextExamples(unittest.TestCase):
    def test_zero_history_unavailable_raw_is_zero(self):
        np.testing.assert_array_equal(residuals([0], [np.nan], [7]), [0])

    def test_zero_history_does_not_use_raw(self):
        np.testing.assert_array_equal(residuals([0], [9999], [7]), [0])

    def test_mixed_context_keeps_zero_in_mean(self):
        got = residuals([0, 1, 3], [np.nan, 9, 3], [7, 7, 7])
        np.testing.assert_allclose(got, [0, 1, -3], rtol=0, atol=1e-12)
        self.assertAlmostEqual(got.mean(), -2 / 3)

    def test_positive_history_requires_raw(self):
        with self.assertRaises(ValueError):
            residuals([1], [np.nan], [7])

    def test_zero_history_still_requires_baseline(self):
        with self.assertRaises(ValueError):
            residuals([0], [np.nan], [np.nan])

    def test_invalid_counts_fail_closed(self):
        for count in [-1, 0.5, np.nan, np.inf]:
            with self.subTest(count=count), self.assertRaises(ValueError):
                residuals([count], [9], [7])

    def test_misaligned_arrays_fail_closed(self):
        with self.assertRaises(ValueError):
            residuals([0, 1], [np.nan], [7, 7])


if __name__ == '__main__':
    unittest.main()
