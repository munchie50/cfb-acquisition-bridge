import copy
import json
import unittest
import cfb_recovery_consumer_preflight as gate

NOW = '2026-10-17T13:40:00Z'


class ConsumerPreflightTests(unittest.TestCase):
    def setUp(self):
        self.files = {p: p for p in [gate.MONEY, gate.R2, gate.LINEAGE, gate.HEALTH] +
                      ['evidence/operational/' + n for n in gate.OPERATIONAL]}
        self.sheet = 'evidence/operational/CFB_WEEK7_HOT_SHEET_2026-10-17_0708CT.md'
        self.files[self.sheet] = ('Canonical inputs: market ' + 'a' * 40 + '; decision ' +
                                 gate.blob(self.files[gate.LEDGER]) + '.\n')
        roles = {gate.MONEY: 'CURRENT_MONEY_LEDGER:', gate.R2: 'CURRENT_WEEKLY_REVIEW:',
                 self.sheet: 'CURRENT_HOT_SHEET:'}
        self.record = {'schema': 'CFB_RECOVERY_NAVIGATION_FRONTIER_V1',
                       'as_of_utc': NOW, 'scope': 'NAVIGATION_ONLY_NOT_AUTHORITY',
                       'claims': ['Fixture navigation only'],
                       'pointers': [{'path': p, 'blob': gate.blob(v),
                                     'purpose': roles.get(p, 'dependency')} for p, v in self.files.items()]}

    def run_gate(self, record=None):
        r = self.record if record is None else record
        return gate.audit('```cfb-frontier-json\n' + json.dumps(r) + '\n```\n',
                          self.files.__getitem__, NOW)

    def test_complete_composite_boundary(self):
        self.assertEqual(self.run_gate()['verified_pointers'], 9)

    def test_every_consumer_dependency_is_required(self):
        for path in self.files:
            with self.subTest(path=path):
                r = copy.deepcopy(self.record)
                r['pointers'] = [p for p in r['pointers'] if p['path'] != path]
                with self.assertRaises(ValueError): self.run_gate(r)

    def test_later_checkpoint_does_not_inherit_omitted_dependencies(self):
        older = copy.deepcopy(self.record); older['as_of_utc'] = '2026-10-17T13:39:00Z'
        later = copy.deepcopy(self.record)
        later['pointers'] = [p for p in later['pointers'] if p['path'] != gate.MONEY]
        blocks = ''.join('```cfb-frontier-json\n' + json.dumps(r) + '\n```\n' for r in (older, later))
        with self.assertRaisesRegex(ValueError, 'missing consumer dependencies'):
            gate.audit(blocks, self.files.__getitem__, NOW)

    def test_stale_pointer(self):
        self.record['pointers'][0]['blob'] = '0' * 40
        with self.assertRaisesRegex(ValueError, 'stale recovery pointer'): self.run_gate()

    def test_wrong_required_role(self):
        for path in (gate.MONEY, gate.R2, self.sheet):
            with self.subTest(path=path):
                r = copy.deepcopy(self.record)
                next(p for p in r['pointers'] if p['path'] == path)['purpose'] = 'historical'
                with self.assertRaises(ValueError): self.run_gate(r)

    def test_duplicate_current_role(self):
        other = 'evidence/other.md'; self.files[other] = 'other'
        self.record['pointers'].append({'path': other, 'blob': gate.blob('other'),
                                        'purpose': 'CURRENT_MONEY_LEDGER: ambiguous'})
        with self.assertRaises(ValueError): self.run_gate()

    def test_unknown_optional_pointer_must_still_match(self):
        self.record['pointers'].append({'path': 'evidence/optional.md', 'blob': '0' * 40,
                                        'purpose': 'optional'})
        self.files['evidence/optional.md'] = 'different'
        with self.assertRaisesRegex(ValueError, 'stale recovery pointer'): self.run_gate()

    def test_sheet_decision_binding_is_checked_beyond_file_hash(self):
        self.files[self.sheet] = self.files[self.sheet].replace(gate.blob(self.files[gate.LEDGER]), '0' * 40)
        next(p for p in self.record['pointers'] if p['path'] == self.sheet)['blob'] = gate.blob(self.files[self.sheet])
        with self.assertRaisesRegex(ValueError, 'stale current publication'): self.run_gate()


if __name__ == '__main__': unittest.main()
