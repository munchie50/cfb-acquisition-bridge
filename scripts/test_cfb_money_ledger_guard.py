import json,os,unittest
from pathlib import Path
import cfb_money_ledger_guard as gate
ROOT=Path(__file__).resolve().parents[1]
class MoneyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        local=os.environ.get('CFB_MONEY_GUARD_FIXTURE_DIR')
        if local:
            root=Path(local);cls.m=(root/'money.md').read_text();cls.e=(root/'execution.md').read_text()
        else:
            from test_cfb_week7_opening_display_gate import snapshot
            cls.m=(ROOT/gate.PATH).read_text();cls.e=snapshot('evidence/operational/CFB_EXECUTION_LEDGER.md',gate.EXECUTION_SHA)
        cls.body=gate.re.findall(r'```cfb-funding-json\n(.*?)\n```',cls.m,gate.re.S)[0];cls.record=json.loads(cls.body)
    def check(self,m=None,e=None):return gate.audit(self.m if m is None else m,self.e if e is None else e,'2026-10-12T01:34:27Z')
    def altered(self,change):
        x=json.loads(self.body);change(x);return self.m.replace(self.body,json.dumps(x,indent=2))
    def reject(self,m):
        with self.assertRaises(ValueError):self.check(m)
    def test_actual(self):self.assertEqual(self.check()['funding_usd'],'20.00')
    def test_duplicate_same_record(self):self.reject(self.m+'\n```cfb-funding-json\n'+self.body+'\n```\n')
    def test_duplicate_source_key(self):
        x=json.loads(self.body);x['funding_id']='OTHER';self.reject(self.m+'\n```cfb-funding-json\n'+json.dumps(x)+'\n```\n')
    def test_new_unqualified_record(self):
        x=json.loads(self.body);x.update(funding_id='OTHER',idempotency_key='OTHER');self.reject(self.m+'\n```cfb-funding-json\n'+json.dumps(x)+'\n```\n')
    def test_amount_rewrite(self):self.reject(self.altered(lambda x:x.update(amount_usd='40.00')))
    def test_nan(self):self.reject(self.altered(lambda x:x.update(amount_usd='NaN')))
    def test_inexact_precision(self):self.reject(self.altered(lambda x:x.update(amount_usd='20.001')))
    def test_negative(self):self.reject(self.altered(lambda x:x.update(amount_usd='-20.00')))
    def test_stake_as_funding(self):self.reject(self.altered(lambda x:x.update(transaction_type='WAGER_STAKE')))
    def test_payout_as_funding(self):self.reject(self.altered(lambda x:x.update(is_wager_return=True)))
    def test_sandbox_allocation(self):self.reject(self.altered(lambda x:x.update(budget_class='SANDBOX')))
    def test_cash_balance_inference(self):self.reject(self.altered(lambda x:x.update(cash_balance='40.00')))
    def test_ceiling_increase(self):self.reject(self.altered(lambda x:x.update(changes_sandbox_ceiling=True)))
    def test_event_backdate(self):self.reject(self.altered(lambda x:x.update(funding_event_time='2026-10-09T20:26:00-05:00')))
    def test_future_record(self):self.reject(self.altered(lambda x:x.update(recorded_at_utc='2026-10-13T01:24:34Z')))
    def test_forged_source(self):self.reject(self.altered(lambda x:x['source'].update(evidence_type='ASSISTANT_INFERENCE')))
    def test_wrong_execution_reference(self):self.reject(self.altered(lambda x:x['execution_reference'].update(blob='0'*40)))
    def test_duplicate_related_execution(self):self.reject(self.altered(lambda x:x['related_execution_ids'].__setitem__(0,'CFB_OCT09-02')))
    def test_duplicate_json_key(self):self.reject(self.m.replace('"amount_usd": "20.00",','"amount_usd": "20.00", "amount_usd": "40.00",'))
    def test_unknown_field(self):self.reject(self.altered(lambda x:x.update(bank_transfer_done=True)))
    def test_table_amount(self):self.reject(self.m.replace('| +$20.00 |','| +$40.00 |',1))
    def test_display_total(self):self.reject(self.m.replace('**+$20.00**, one transaction.','**+$40.00**, two transactions.',1))
    def test_duplicate_display_row(self):
        row=next(l for l in self.m.splitlines() if l.startswith('| CFB_'));self.reject(self.m.replace(row,row+'\n'+row))
    def test_execution_snapshot_changed(self):
        with self.assertRaises(ValueError):self.check(e=self.e+'\n')
    def test_missing_record(self):self.reject(self.m.replace('```cfb-funding-json','```other-json'))
    def nav(self,change=None):
        p=[{'path':gate.PATH,'blob':gate.blob(self.m),'purpose':'CURRENT_MONEY_LEDGER: confirmed funding'}]
        if change:change(p)
        return '```cfb-frontier-json\n'+json.dumps({'schema':'CFB_RECOVERY_NAVIGATION_FRONTIER_V1','as_of_utc':'2026-10-12T01:34:27Z','scope':'NAVIGATION_ONLY_NOT_AUTHORITY','claims':['Navigation only'],'pointers':p})+'\n```\n'
    def test_binding(self):self.assertEqual(gate.binding(self.nav(),self.m,'2026-10-12T01:34:27Z')['current_money_blob'],gate.blob(self.m))
    def test_stale_binding(self):
        with self.assertRaises(ValueError):gate.binding(self.nav(lambda p:p[0].update(blob='0'*40)),self.m,'2026-10-12T01:34:27Z')
    def test_missing_role(self):
        with self.assertRaises(ValueError):gate.binding(self.nav(lambda p:p[0].update(purpose='historical')),self.m,'2026-10-12T01:34:27Z')
if __name__=='__main__':unittest.main()
