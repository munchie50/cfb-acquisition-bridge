#!/usr/bin/env python3
"""Direct binding API must reject explicit nonacceptance before declaring PASS."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from cfb_hot_sheet_current_decision_binding_gate import audit, blob


class DirectBindingProvisionalTests(unittest.TestCase):
    def test_rejects_provisional_with_valid_decision_binding(self):
        ledger = '# canonical ledger\n'
        declaration = f'Canonical inputs: market {"a" * 40}; decision {blob(ledger)}.'
        for label in ('NONCANONICAL', 'NOT ACCEPTED', 'NOT-ACCEPTED',
                      'NOT\nACCEPTED', 'NO ACTIONABLE WAGERS'):
            with self.subTest(label=label), self.assertRaisesRegex(ValueError, 'provisional'):
                audit(declaration + '\n' + label, ledger)

    def test_valid_binding_without_rejection_is_binding_only(self):
        ledger = '# canonical ledger\n'
        sheet = f'Canonical inputs: market {"a" * 40}; decision {blob(ledger)}.'
        self.assertEqual(audit(sheet, ledger)['verdict'], 'PASS_SUPPLIED_CURRENT_DECISION_BINDING_ONLY')


if __name__ == '__main__':
    unittest.main()
