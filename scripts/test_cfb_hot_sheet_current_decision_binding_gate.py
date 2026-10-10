import copy, json, unittest
from cfb_hot_sheet_current_decision_binding_gate import audit,blob,publication,LEDGER

PATH='evidence/operational/CFB_WEEK6_HOT_SHEET_2026-10-09_2114CT.md'
NOW='2026-10-10T02:20:24Z'

class CurrentBindingTests(unittest.TestCase):
    def setUp(self):
        self.ledger='canonical decision v2\n'
        self.sheet='Canonical inputs: market '+'a'*40+'; decision '+blob(self.ledger)+'.\n'
        self.record={'schema':'CFB_RECOVERY_NAVIGATION_FRONTIER_V1','scope':'NAVIGATION_ONLY_NOT_AUTHORITY',
            'as_of_utc':'2026-10-10T02:17:21Z','claims':['fixture; no semantic certification'],
            'pointers':[{'path':LEDGER,'blob':blob(self.ledger),'purpose':'canonical state'},
                        {'path':PATH,'blob':blob(self.sheet),'purpose':'CURRENT_HOT_SHEET: current view'}]}
    def index(self,r=None):return '```cfb-frontier-json\n'+json.dumps(r or self.record)+'\n```\n'
    def run_publication(self,r=None,sheet=None,ledger=None,index=None):
        return publication(index or self.index(r),self.ledger if ledger is None else ledger,
                           lambda path:self.sheet if sheet is None else sheet,NOW)
    def test_valid_current(self):self.assertEqual(self.run_publication()['sheet_path'],PATH)
    def test_hash(self):
        import hashlib
        self.assertEqual(blob('é\n'),hashlib.sha1(b'blob 3\0'+ 'é\n'.encode()).hexdigest())
    def test_stale_sheet(self):
        with self.assertRaisesRegex(ValueError,'stale current'):audit(self.sheet,'later canonical')
    def test_duplicate_binding(self):
        with self.assertRaises(ValueError):audit(self.sheet*2,self.ledger)
    def test_missing_binding(self):
        with self.assertRaises(ValueError):audit('no binding',self.ledger)
    def test_empty_ledger(self):
        with self.assertRaises(ValueError):audit('Canonical inputs: market '+'a'*40+'; decision '+blob('')+'.\n','')
    def test_no_current_role(self):
        r=copy.deepcopy(self.record);r['pointers'][1]['purpose']='historical retained view'
        with self.assertRaises(ValueError):self.run_publication(r)
    def test_multiple_current_roles(self):
        r=copy.deepcopy(self.record);p=copy.deepcopy(r['pointers'][1]);p['path']=PATH.replace('2114','2012');r['pointers'].append(p)
        with self.assertRaises(ValueError):self.run_publication(r)
    def test_current_pointer_mismatch(self):
        with self.assertRaisesRegex(ValueError,'publication bytes'):self.run_publication(sheet=self.sheet+'extra')
    def test_stale_index_decision(self):
        with self.assertRaisesRegex(ValueError,'recovery canonical'):self.run_publication(ledger=self.ledger+'new')
    def test_newer_filename_does_not_select(self):
        r=copy.deepcopy(self.record);r['pointers'].append({'path':PATH.replace('2114','2359'),'blob':'b'*40,'purpose':'historical later filename'})
        self.assertEqual(self.run_publication(r)['sheet_path'],PATH)
    def test_unsupported_publication_path(self):
        r=copy.deepcopy(self.record);r['pointers'][1]['path']='evidence/arbitrary.md'
        with self.assertRaises(ValueError):self.run_publication(r)
    def test_uncheckpointed_tail(self):
        with self.assertRaises(ValueError):self.run_publication(index=self.index()+'new state')
    def test_future_checkpoint(self):
        r=copy.deepcopy(self.record);r['as_of_utc']='2026-10-11T00:00:00Z'
        with self.assertRaises(ValueError):self.run_publication(r)

    def test_exact_optional_execution_reference(self):
        sheet=self.sheet.replace('.\n','; execution '+'b'*40+'.\n')
        self.assertEqual(audit(sheet,self.ledger)['decision_blob'],blob(self.ledger))
    def test_optional_execution_does_not_override_stale_decision(self):
        sheet=self.sheet.replace('.\n','; execution '+'b'*40+'.\n')
        with self.assertRaisesRegex(ValueError,'stale current'):audit(sheet,'later canonical')
    def test_malformed_execution_reference(self):
        with self.assertRaises(ValueError):audit(self.sheet.replace('.\n','; execution bbb.\n'),self.ledger)
    def test_unknown_extra_source_reference(self):
        with self.assertRaises(ValueError):audit(self.sheet.replace('.\n','; arbitrary '+'b'*40+'.\n'),self.ledger)
    def test_duplicate_extended_binding(self):
        sheet=self.sheet.replace('.\n','; execution '+'b'*40+'.\n')
        with self.assertRaises(ValueError):audit(sheet*2,self.ledger)

if __name__=='__main__':unittest.main()
