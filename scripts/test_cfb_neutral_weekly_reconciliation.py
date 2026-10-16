"""Authentic saved-source replay plus mutation tests; never operational evidence."""
import copy,json,unittest
from pathlib import Path
import cfb_neutral_publication_gate as gate
import cfb_neutral_weekly_reconciliation as repair
from cfb_neutral_publication_legacy_replay import historical,packet

ROOT=Path('evidence/operational')
AT='2026-10-16T02:31:12Z'
CYCLE='CFB_PRESENTATION_RECONCILIATION_20261016T023112Z'

class WeeklyReconciliationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.market=historical(ROOT/'CFB_MARKET_MONITOR_STATE.md',repair.MARKET)
        cls.decision=historical(ROOT/'CFB_DECISION_WAIT_LEDGER.md',repair.DECISION)
        cls.capture=historical(ROOT/'CFB_CBS_FULL_BOARD_TABLES_20261015T175838Z.md',repair.CAPTURE)
        cls.lineage=(ROOT/'CFB_WEEK7_ORIGINAL_FIRST_FROZEN_LINEAGE_2026-10-11.json').read_text()
        cls.pm,cls.pd=repair.build(cls.market,cls.decision,cls.capture,cls.lineage,CYCLE,AT)
    def setUp(self):
        self.m=copy.deepcopy(repair.latest(self.pm,gate.MARKET_TAG));self.d=copy.deepcopy(repair.latest(self.pd,gate.DECISION_TAG))
    def args(self):return [self.market+packet(self.m,gate.MARKET_TAG),self.decision+packet(self.d,gate.DECISION_TAG),'execution fixture','scorecard fixture',self.lineage,AT]
    def reject(self):
        with self.assertRaises((ValueError,KeyError,TypeError)):gate.render(*self.args())
    def test_authentic_full_week_and_first_ancestry(self):
        old=repair.latest(self.market,gate.MARKET_TAG)
        self.assertTrue(self.pm.startswith(self.market));self.assertTrue(self.pd.startswith(self.decision))
        self.assertEqual([r['first'] for r in self.m['rows']],[r['first'] for r in old['rows']])
        s=gate.render(*self.args());self.assertEqual(gate.audit(s,*self.args())['games'],62)
        self.assertIn('55 INCONCLUSIVE; 7 PASS',s);self.assertEqual(s.count('[AT/PAST SAVED KICKOFF — historical PASS; no execution]'),7)
        self.assertEqual(sum(r['diagnostic'] is not None for r in self.m['rows']),1)
    def test_historical_quotes_cannot_become_current(self):
        r=self.m['rows'][0];r.update(current=r['retained'],retained=None,current_availability='AVAILABLE');self.reject()
    def test_hindsight_pass_timestamp_rejected(self):self.d['rows'][0]['state_recorded_at_utc']=AT;self.reject()
    def test_historical_pass_wrong_ancestor_rejected(self):self.d['rows'][0]['state_evidence']='0'*40;self.reject()
    def test_historical_pass_relabelled_as_new_rejected(self):
        self.d['rows'][0].update(state_evidence=CYCLE,state_recorded_at_utc=AT);self.reject()
    def test_historical_ancestor_tamper_rejected(self):
        a=self.args();a[1]=a[1].replace('Thursday Evening Availability','Changed Evening Availability',1)
        with self.assertRaises(ValueError):gate.render(*a)
    def test_elapsed_inconclusive_rejected(self):self.d['rows'][0]['state']='INCONCLUSIVE';self.reject()
    def test_retained_quote_after_kickoff_rejected(self):self.m['rows'][0]['retained']['retrieved_at']=AT;self.reject()
    def test_first_observation_rewrite_rejected(self):self.m['rows'][0]['first']['over_total']+=1;self.reject()
    def test_missing_identity_rejected(self):self.m['rows'].pop();self.reject()
    def test_weekly_profile_pair_required(self):self.d['schema']=gate.DECISION_SCHEMA;self.reject()
    def test_diagnostic_cannot_be_current(self):
        r=next(r for r in self.m['rows'] if r['diagnostic']);r['current']=r['diagnostic']['offer'];r['current_availability']='AVAILABLE';r['retained']=None;self.reject()
    def test_diagnostic_cannot_hide_other_errors(self):
        r=next(r for r in self.m['rows'] if r['diagnostic']);r['diagnostic']['offer']['over_price']=None;self.reject()
    def test_diagnostic_requires_actual_conflict(self):
        r=next(r for r in self.m['rows'] if r['diagnostic']);r['diagnostic']['offer']['away_ml']=110;self.reject()
    def test_current_friday_update_preserved(self):
        r=next(r for r in self.m['rows'] if r['game_id']=='401858493');self.assertEqual(r['current']['over_total'],49.5);self.assertEqual(r['current']['under_total'],50.5)
        reason=next(r for r in self.d['rows'] if r['game_id']=='401858493')['reason'];self.assertIn('Demond Williams',reason)
    def test_recovered_by_not_exact_clock(self):
        s=gate.render(*self.args());self.assertIn('response recovered by '+repair.EVENING_BY,s);self.assertIn('RECOVERED_BY precision',s)
    def test_null_first_stays_unknown_with_saved_current(self):
        self.assertEqual(sum(r['first'] is None for r in self.m['rows']),3)
        self.assertIn('No qualified first observation',gate.render(*self.args()))
    def test_deterministic_whole_view_tamper_rejected(self):
        a=self.args();s=gate.render(*a).replace('55 INCONCLUSIVE','54 INCONCLUSIVE')
        with self.assertRaises(ValueError):gate.audit(s,*a)
    def test_future_inconclusive_deadline_remains_enforced(self):
        a=self.args();a[-1]='2026-10-16T18:00:00Z'
        with self.assertRaises(ValueError):gate.render(*a)
    def test_new_prospective_pass_has_typed_proof_and_carries_forward(self):
        r=self.d['rows'][7];r.update(state='PASS',reason='Synthetic future QA only')
        m=self.args()[0];d=self.args()[1]
        later_m=copy.deepcopy(self.m);later_d=copy.deepcopy(self.d)
        for p in (later_m,later_d):p.update(cycle_id='CFB_MARKET_MONITOR_20261016T115900Z',as_of_utc='2026-10-16T12:00:00Z')
        a=[m+packet(later_m,gate.MARKET_TAG),d+packet(later_d,gate.DECISION_TAG),'execution','scorecard',self.lineage,'2026-10-16T12:00:00Z'];gate.render(*a)
        later_d['rows'][7]['state']='INCONCLUSIVE';a[1]=d+packet(later_d,gate.DECISION_TAG)
        with self.assertRaises(ValueError):gate.render(*a)
    def test_source_adapter_rejects_changed_unqualified_source(self):
        with self.assertRaises(ValueError):repair.build(self.market+'changed',self.decision,self.capture,self.lineage,CYCLE,AT)
    def next_rows(self):
        return [{k:v for k,v in r.items() if k not in ('state_recorded_at_utc','state_evidence')} for r in self.d['rows']]
    def advance(self,stamp='2026-10-16T12:00:00Z',recovered='2026-10-16T11:59:30Z',rows=None):
        return repair.advance(self.pm,self.pd,self.capture,self.lineage,'CFB_MARKET_MONITOR_20261016T115900Z',stamp,recovered,self.next_rows() if rows is None else rows)
    def test_ephemeral_next_cycle_complete_compilation(self):
        m,d=self.advance();self.assertEqual(len(repair.latest(m,gate.MARKET_TAG)['rows']),62)
        self.assertEqual(sum(r['state']=='PASS' for r in repair.latest(d,gate.DECISION_TAG)['rows']),7)
    def test_ephemeral_evening_uses_its_own_identity_without_untyped_tail(self):
        cycle='CFB_EVENING_AVAILABILITY_20261016T030000Z';at='2026-10-16T03:01:00Z'
        m,d=repair.advance(self.pm,self.pd,self.capture,self.lineage,cycle,at,'2026-10-16T03:00:30Z',self.next_rows())
        self.assertEqual(repair.latest(m,gate.MARKET_TAG)['cycle_id'],cycle)
        self.assertEqual(repair.latest(d,gate.DECISION_TAG)['cycle_id'],cycle)
        sheet=gate.render(m,d,'execution','scorecard',self.lineage,at)
        self.assertEqual(gate.audit(sheet,m,d,'execution','scorecard',self.lineage,at)['games'],62)
        # The next Monitor consumes the complete Evening packet without adopting
        # an Evening publication or changing output ownership.
        m,d=repair.advance(m,d,self.capture,self.lineage,'CFB_MARKET_MONITOR_20261016T115900Z','2026-10-16T12:00:00Z','2026-10-16T11:59:30Z',self.next_rows())
        self.assertEqual(repair.latest(m,gate.MARKET_TAG)['cycle_id'],'CFB_MARKET_MONITOR_20261016T115900Z')
    def test_evening_identity_does_not_expand_v1_pregame_profile(self):
        from test_cfb_neutral_publication_gate import fixture
        m,d,lineage=fixture();m['cycle_id']=d['cycle_id']='CFB_EVENING_AVAILABILITY_20261012T233632Z'
        with self.assertRaises(ValueError):gate.render(packet(m,gate.MARKET_TAG),packet(d,gate.DECISION_TAG),'e','s',lineage,'2026-10-12T23:36:32Z')
    def test_unknown_producer_identity_still_rejected(self):
        self.m['cycle_id']=self.d['cycle_id']='CFB_UNKNOWN_PRODUCER_20261016T023112Z';self.reject()
    def test_advance_rejects_stale_source_bound(self):
        with self.assertRaises(ValueError):self.advance(recovered=AT)
    def test_advance_rejects_future_source_bound(self):
        with self.assertRaises(ValueError):self.advance(recovered='2026-10-16T12:00:01Z')
    def test_advance_rejects_missing_producer_decision(self):
        with self.assertRaises(ValueError):self.advance(rows=self.next_rows()[:-1])
    def test_advance_rejects_reopening_prior_pass(self):
        rows=self.next_rows();rows[0]['state']='INCONCLUSIVE'
        with self.assertRaises(ValueError):self.advance(rows=rows)
    def test_advance_does_not_automatically_extend_deadline(self):
        with self.assertRaises(ValueError):self.advance(stamp='2026-10-16T18:00:00Z')
    def test_advance_rejects_unearned_actionable_state(self):
        rows=self.next_rows();rows[7]['state']='BET NOW'
        with self.assertRaises(ValueError):self.advance(rows=rows)

if __name__=='__main__':unittest.main()
