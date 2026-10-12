"""Ephemeral protocol fixtures; no future operational evidence is persisted."""
import copy,json,unittest
from pathlib import Path
import cfb_neutral_publication_gate as gate

LINEAGE='evidence/operational/CFB_WEEK7_ORIGINAL_FIRST_FROZEN_LINEAGE_2026-10-11.json'
def packet(value,tag):return '\n```'+tag+'\n'+json.dumps(value)+'\n```\n'
def fixture(boundary='2026-10-12T23:36:32Z',cycle='CFB_MARKET_MONITOR_20261012T233632Z'):
    lineage=Path(LINEAGE).read_text();c=json.loads(lineage)['rows']
    market={'schema':gate.MARKET_SCHEMA,'cycle_id':cycle,'as_of_utc':boundary,'rows':[]}
    decision={'schema':gate.DECISION_SCHEMA,'cycle_id':cycle,'as_of_utc':boundary,'rows':[]}
    for r in c:
        # Unknown schedules/quotes are a supported synthetic protocol test, not a source claim.
        market['rows'].append({'game_id':r['game_id'],'kickoff_utc':None,'kickoff_source_url':None,'kickoff_status':'UNRESOLVED','first':None,'current':None,'current_availability':'UNAVAILABLE','retained':None})
        decision['rows'].append({'game_id':r['game_id'],'state':'INCONCLUSIVE','reason':'Synthetic QA only; no operational evidence','reconciliation_utc':'2026-10-13T18:00:00Z','planning_cutoff_utc':None,'cutoff_authority':'UNVERIFIED','acceptable_number':None,'execution_window':None})
    return market,decision,lineage
def offer():
    return {'book':'Synthetic QA book','source_type':'IDENTIFIED_SINGLE_BOOK_FALLBACK','source_url':'https://example.invalid/qa','event_id':'fixture-only','retrieved_at':'2026-10-12T23:36:32Z','retrieval_precision':'EXACT','offer_updated_at':None,'execution':'UNVERIFIED','away_spread':-3.5,'away_spread_price':-110,'home_spread':3.5,'home_spread_price':-110,'away_ml':-150,'home_ml':130,'over_total':48.5,'over_price':-105,'under_total':49.5,'under_price':-115}

class NeutralPublicationTests(unittest.TestCase):
    def setUp(self):self.m,self.d,self.l=fixture();self.at='2026-10-12T23:36:32Z'
    def args(self):return [packet(self.m,gate.MARKET_TAG),packet(self.d,gate.DECISION_TAG),'retained execution fixture','retained scorecard fixture',self.l,self.at]
    def render(self):return gate.render(*self.args())
    def reject(self):
        with self.assertRaises((ValueError,KeyError,TypeError)):self.render()
    def available(self):
        o=offer();self.m['rows'][0].update(first=o,current=copy.deepcopy(o),current_availability='AVAILABLE')
    def test_ephemeral_unknown_quotes_and_schedule(self):
        s=self.render();self.assertEqual(gate.audit(s,*self.args())['games'],62);self.assertEqual(s.count('| UNRESOLVED |'),62)
    def test_date_independent_next_cycle(self):
        self.m,self.d,self.l=fixture('2026-10-13T12:01:00Z','CFB_MARKET_MONITOR_20261013T120100Z');self.at=self.m['as_of_utc'];self.render()
    def test_changed_canonical_quotes_drive_output(self):
        self.available();s=self.render();self.m['rows'][0]['current']['away_spread_price']=-115;new=self.render();self.assertNotEqual(s,new)
        with self.assertRaises(ValueError):gate.audit(s,*self.args())
    def test_unknown_schema(self):self.m['schema']='UNKNOWN';self.reject()
    def test_unknown_field(self):self.m['rows'][0]['raw_result']='future result';self.reject()
    def test_missing_row(self):self.m['rows'].pop();self.reject()
    def test_duplicate_identity(self):self.m['rows'][0]['game_id']=self.m['rows'][1]['game_id'];self.reject()
    def test_unknown_game(self):self.m['rows'][0]['game_id']='999999';self.reject()
    def test_decision_union(self):self.d['rows'].pop();self.reject()
    def test_future_source_boundary(self):self.m['as_of_utc']='2026-10-13T12:01:00Z';self.reject()
    def test_mismatched_cycles(self):self.d['cycle_id']='CFB_MARKET_MONITOR_20261012T233633Z';self.reject()
    def test_cycle_start_after_boundary(self):self.m['cycle_id']='CFB_MARKET_MONITOR_20261013T120000Z';self.reject()
    def test_bet_now_unsupported(self):self.d['rows'][0]['state']='BET NOW';self.reject()
    def test_wait_unsupported(self):self.d['rows'][0]['state']='WAIT';self.reject()
    def test_missing_reconciliation(self):self.d['rows'][0]['reconciliation_utc']=None;self.reject()
    def test_overdue_inconclusive(self):self.at='2026-10-13T18:00:00Z';self.reject()
    def test_pass_does_not_create_bet(self):
        for r in self.d['rows']:r['state']='PASS';r['reconciliation_utc']=None
        self.at='2026-10-13T18:00:00Z';s=self.render();self.assertIn('0 INCONCLUSIVE; 62 PASS',s)
    def test_pass_reason_required(self):self.d['rows'][0].update(state='PASS',reason='');self.reject()
    def test_verified_cutoff_prohibited(self):self.d['rows'][0]['cutoff_authority']='VERIFIED';self.reject()
    def test_number_invented(self):self.d['rows'][0]['acceptable_number']='-3.5';self.reject()
    def test_execution_invented(self):self.d['rows'][0]['execution_window']='tonight';self.reject()
    def test_table_injection(self):self.d['rows'][0]['reason']='reason | BET NOW';self.reject()
    def test_lineage_changed(self):self.l+='\n';self.reject()
    def test_real_quote_roles_fixed(self):
        self.available();s=self.render();self.assertIn('CONSENSUS_UNAVAILABLE; Caesars UNVERIFIED;',s);self.assertIn('o48.5 -105 / u49.5 -115',s)
    def test_future_offer(self):self.available();self.m['rows'][0]['current']['retrieved_at']='2026-10-13T12:00:00Z';self.reject()
    def test_bool_number(self):self.available();self.m['rows'][0]['current']['over_total']=True;self.reject()
    def test_nonfinite(self):self.available();self.m['rows'][0]['current']['over_total']=float('inf');self.reject()
    def test_partial_pair(self):self.available();self.m['rows'][0]['current']['over_price']=None;self.reject()
    def test_ml_conflict(self):self.available();self.m['rows'][0]['current']['away_ml']=150;self.reject()
    def test_offer_time_invented(self):self.available();self.m['rows'][0]['current']['offer_updated_at']=self.at;self.reject()
    def test_execution_verified(self):self.available();self.m['rows'][0]['current']['execution']='VERIFIED';self.reject()
    def test_no_current_when_unavailable(self):self.m['rows'][0]['current']=offer();self.reject()
    def test_retained_historical_label(self):
        self.m['rows'][0].update(first=offer(),retained=offer());self.assertIn('CURRENT QUOTE UNAVAILABLE; historical retained',self.render())
    def test_first_after_current(self):
        self.available();self.m['rows'][0]['current']['retrieved_at']='2026-10-12T22:00:00Z';self.reject()
    def test_new_synthetic_schedule_section(self):
        self.m['rows'][0].update(kickoff_utc='2026-10-13T23:00:00Z',kickoff_source_url='https://example.invalid/schedule',kickoff_status='RETAINED_UNVERIFIED');self.assertIn('Tue Oct 13 6:00 PM CT [RETAINED_UNVERIFIED]',self.render())
    def test_unresolved_cannot_invent_time(self):self.m['rows'][0]['kickoff_utc']='2026-10-13T23:00:00Z';self.reject()
    def test_reconcile_at_kickoff(self):
        self.m['rows'][0].update(kickoff_utc='2026-10-13T18:00:00Z',kickoff_source_url='https://example.invalid/schedule',kickoff_status='QUALIFIED');self.reject()
    def test_started_game_rejected(self):
        self.m['rows'][0].update(kickoff_utc='2026-10-13T18:00:00Z',kickoff_source_url='https://example.invalid/schedule',kickoff_status='QUALIFIED');self.m['as_of_utc']=self.d['as_of_utc']='2026-10-13T18:01:00Z';self.at=self.m['as_of_utc'];self.reject()
    def test_untyped_tail(self):
        a=self.args();a[0]+='Later untyped market update'
        with self.assertRaises(ValueError):gate.render(*a)
    def test_duplicate_json_key(self):
        a=self.args();a[0]=a[0].replace('"schema":','"schema":"fake", "schema":',1)
        with self.assertRaises(ValueError):gate.render(*a)
    def test_append_chain_preserves_first(self):
        self.available();old=packet(self.m,gate.MARKET_TAG);self.m['cycle_id']='CFB_MARKET_MONITOR_20261013T120000Z';self.m['as_of_utc']='2026-10-13T12:00:00Z';self.d['cycle_id']=self.m['cycle_id'];self.d['as_of_utc']=self.m['as_of_utc'];self.at=self.m['as_of_utc']
        a=self.args();a[0]=old+a[0];gate.render(*a)
        self.m['rows'][0]['first']['over_total']=49.0;a=self.args();a[0]=old+a[0]
        with self.assertRaises(ValueError):gate.render(*a)
    def test_forged_render_rejected(self):
        self.available();s=self.render().replace('o48.5 -105','o48.5 -115',1)
        with self.assertRaises(ValueError):gate.audit(s,*self.args())

if __name__=='__main__':unittest.main()
