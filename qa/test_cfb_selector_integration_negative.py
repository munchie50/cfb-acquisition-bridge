"""Synthetic integration adversarial tests; not production acceptance."""
import contextlib
import hashlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'qa'))
from cfb_actual_canonical_selector_readback_qa import run


def blob(data):
    raw = data.encode()
    return hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()


class SelectorIntegrationNegativeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.modules = {}
        for rel in ('scripts/cfb_recovery_navigation_reader.py', 'scripts/cfb_hot_sheet_current_decision_binding_gate.py'):
            source = (ROOT / rel).read_bytes()
            target = self.root / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(source)
            self.modules[rel] = blob(source.decode())
        self.ledger = '# Synthetic decision state\n'
        self.sheet_path = 'evidence/operational/CFB_WEEK12_HOT_SHEET_2026-11-19_1338CT.md'
        self.sheet = f'Canonical inputs: market {"a"*40}; decision {blob(self.ledger)}.\n'
        self.index_path = 'evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_295.md'
        self.ledger_path = 'evidence/operational/CFB_DECISION_WAIT_LEDGER.md'

    def write(self, path, content):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content)

    def execute(self, *, pointer_override=None, sheet_override=None, trailing='', module_pin_override=None):
        sheet = self.sheet if sheet_override is None else sheet_override
        self.write(self.sheet_path, sheet)
        self.write(self.ledger_path, self.ledger)
        pointers = [
            {'path':self.ledger_path,'blob':blob(self.ledger),'purpose':'CURRENT_DECISION_STATE:synthetic'},
            {'path':self.sheet_path,'blob':blob(sheet) if pointer_override is None else pointer_override,'purpose':'CURRENT_HOT_SHEET:synthetic'},
        ]
        record = {'schema':'CFB_RECOVERY_NAVIGATION_FRONTIER_V1','as_of_utc':'2026-11-19T19:38:55+00:00',
                  'scope':'NAVIGATION_ONLY_NOT_AUTHORITY','claims':['Synthetic fixture only'],'pointers':pointers}
        index = 'Synthetic test\n```cfb-frontier-json\n' + json.dumps(record) + '\n```\n' + trailing
        self.write(self.index_path, index)
        with contextlib.redirect_stdout(io.StringIO()):
            return run(self.root,self.root/self.index_path,self.root/self.ledger_path,
                       '2026-11-20T23:59:59+00:00',blob(index),blob(self.ledger),blob(sheet),
                       self.modules['scripts/cfb_recovery_navigation_reader.py'],
                       self.modules['scripts/cfb_hot_sheet_current_decision_binding_gate.py'] if module_pin_override is None else module_pin_override)

    def test_clean_synthetic_fixture(self):
        self.assertIsNone(self.execute())

    def test_explicit_provisional_rejected_even_with_valid_hashes(self):
        with self.assertRaisesRegex(ValueError,'provisional'):
            self.execute(sheet_override=self.sheet + '\nNOT-ACCEPTED\n')

    def test_stale_sheet_pointer_rejected(self):
        with self.assertRaisesRegex(ValueError,'selected sheet pointer'):
            self.execute(pointer_override='0'*40)

    def test_uncheckpointed_index_trailing_content_rejected(self):
        with self.assertRaisesRegex(ValueError,'uncheckpointed trailing content'):
            self.execute(trailing='Unreconciled appended state\n')

    def test_binding_module_hash_mismatch_rejected(self):
        with self.assertRaisesRegex(ValueError,'staged original Python module differs'):
            self.execute(module_pin_override='0'*40)


if __name__ == '__main__':
    unittest.main()
