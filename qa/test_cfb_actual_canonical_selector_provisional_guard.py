#!/usr/bin/env python3
"""Regression tests for explicit nonacceptance; no production acceptance implied."""
import unittest
from cfb_actual_canonical_selector_readback_qa import assert_not_explicitly_provisional


class ProvisionalGuardTests(unittest.TestCase):
    def test_real_week12_preview_banner(self):
        text = "**NONCANONICAL MANUAL RECOVERY PREVIEW — NOT ACCEPTED PRODUCTION / NO ACTIONABLE WAGERS**"
        with self.assertRaisesRegex(ValueError, "explicitly provisional"):
            assert_not_explicitly_provisional(text)

    def test_padding_cannot_hide_rejection(self):
        text = "# Hot Sheet\n" + ("ordinary line\n" * 40) + "NOT_ACCEPTED"
        with self.assertRaises(ValueError):
            assert_not_explicitly_provisional(text)

    def test_case_insensitive(self):
        with self.assertRaises(ValueError):
            assert_not_explicitly_provisional("Status: Not Accepted")

    def test_separator_variants_cannot_hide_rejection(self):
        for label in ('NOT-ACCEPTED', 'NOT\u00a0ACCEPTED', 'NOT\nACCEPTED',
                      'NON-CANONICAL', 'NO\nACTIONABLE WAGERS'):
            with self.subTest(label=label), self.assertRaises(ValueError):
                assert_not_explicitly_provisional('Status: ' + label)

    def test_no_rejection_label_is_not_acceptance(self):
        # This function only rejects explicit warnings; it does not grant acceptance.
        self.assertIsNone(assert_not_explicitly_provisional("# CFB Week12 source-derived conditional Hot Sheet"))


if __name__ == "__main__":
    unittest.main()
