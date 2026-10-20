import copy,json,re,unittest,os
from datetime import timedelta
from pathlib import Path
from unittest.mock import patch
import cfb_week8_publication as week
import cfb_neutral_publication_gate as gate
from cfb_cbs_full_board_normalizer import normalize,WEEK8_URL
from cfb_neutral_publication_legacy_replay import historical
ROOT=Path(__file__).resolve().parents[1]
AT='2026-10-19T18:05:00Z';BY='2026-10-19T18:00:57Z';CYCLE='CFB_PRESENTATION_RECONCILIATION_20261019T180400Z'

class Week8Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lineage=(ROOT/'evidence/scheduler_qa/CFB_WEEK8_ORIGINAL_ANCESTRY_RECOVERY_20261020.json').read_text()
        cls.capture=(ROOT/'evidence/operational/CFB_CBS_WEEK8_FULL_BOARD_TABLES_20261019T180057Z.md').read_text()
        cls.market=historical(ROOT/'evidence/operational/CFB_MARKET_MONITOR_STATE.md',week.MARKET_PARENT)
        cls.decision=historical(ROOT/'evidence/operational/CFB_DECISION_WAIT_LEDGER.md',week.DECISION_PARENT)
        cls.parsed=week.board(cls.capture,cls.lineage,BY)
        cls.rows=[{'game_id':g['game_id'],'state':'INCONCLUSIVE','reason':'SYNTHETIC TEST ONLY: current full market and material review not performed',
             'reconciliation_utc':(gate.clock(g['source_kickoff_utc'])-timedelta(hours=4)).isoformat(),
             'planning_cutoff_utc':(gate.clock(g['source_kickoff_utc'])-timedelta(minutes=30)).isoformat(),
             'cutoff_authority':'UNVERIFIED','acceptable_number':None,'execution_window':None} for g in cls.parsed['games']]
        cls.proposals=week.compile(cls.market,cls.decision,cls.capture,cls.lineage,CYCLE,AT,BY,cls.rows)
        cls.sheet=gate.render(*cls.proposals,'execution','scorecard',cls.lineage,AT,'WEEK8')
    def build(self,**kw):
        args={'market':self.market,'decision':self.decision,'capture':self.capture,'lineage':self.lineage,'cycle':CYCLE,'as_of':AT,'recovered_by':BY,'decision_rows':self.rows};args.update(kw);return week.compile(**args)
    def test_full56_49plus7_source_render(self):
        r=gate.audit(self.sheet,*self.proposals,'execution','scorecard',self.lineage,AT,'WEEK8')
        self.assertEqual(r['games'],56);self.assertIn('49 predictions and 7 exclusions',self.sheet)
        self.assertEqual(sum(' @ ' in l and l.startswith('| ') for l in self.sheet.splitlines()),56)
    def test_current_week7_bytes_preserved(self):
        self.assertTrue(self.proposals[0].startswith(self.market));self.assertTrue(self.proposals[1].startswith(self.decision))
    def test_bootstrap_reconciles_four_retained_captures(self):
        self.assertTrue(week.bootstrap_check(*self.proposals,self.lineage).startswith('PASS_WEEK8'))
        sources=week.retained_rows(self.lineage)[1];self.assertEqual(len(sources),4)
    def test_earliest_retained_quote_preserved(self):
        expected,_=week.retained_rows(self.lineage)
        selected=gate.inputs(*self.proposals,self.lineage,AT,'WEEK8')[3]
        self.assertEqual({k:v['first'] for k,v in selected.items()},{k:v['first'] for k,v in expected.items()})
    def test_default_week7_rejects_week8(self):
        with self.assertRaises(ValueError):gate.inputs(*self.proposals,self.lineage,AT)
    def test_unknown_profile_rejected(self):
        with self.assertRaises(ValueError):gate.profile_config('WEEK9')
    def test_page_profile_cross_binding_rejected(self):
        with self.assertRaises(ValueError):normalize(self.capture,self.lineage,BY,source_url=WEEK8_URL)
    def test_wrong_lineage_rejected(self):
        with self.assertRaises(ValueError):self.build(lineage=self.lineage+'\n')
    def test_wrong_parent_rejected(self):
        for key in ('market','decision'):
            with self.assertRaises(ValueError):self.build(**{key:getattr(self,key)+'changed'})
    def test_missing_decision_rejected(self):
        with self.assertRaises(ValueError):self.build(decision_rows=self.rows[:-1])
    def test_duplicate_decision_rejected(self):
        with self.assertRaises(ValueError):self.build(decision_rows=self.rows+[self.rows[0]])
    def test_unknown_decision_rejected(self):
        rows=copy.deepcopy(self.rows);rows[0]['game_id']='UNKNOWN'
        with self.assertRaises(ValueError):self.build(decision_rows=rows)
    def test_stale_or_future_source_rejected(self):
        for by in ('2026-10-19T17:00:00Z','2026-10-19T18:06:00Z'):
            with self.assertRaises(ValueError):self.build(recovered_by=by)
    def test_missing_team_rejected(self):
        ls=self.capture.splitlines();i=next(i for i,l in enumerate(ls) if l.startswith('| [') and '/teams/' in l);del ls[i]
        with self.assertRaises(ValueError):self.build(capture='\n'.join(ls))
    def test_reversed_directed_pair_rejected(self):
        ls=self.capture.splitlines();ix=[i for i,l in enumerate(ls) if l.startswith('| [') and '/teams/' in l];a,b=ix[:2];ls[a],ls[b]=ls[b],ls[a]
        with self.assertRaises(ValueError):self.build(capture='\n'.join(ls))
    def test_no_forced_actionable_decision(self):
        rows=copy.deepcopy(self.rows);rows[0]['state']='BET NOW'
        with self.assertRaises(ValueError):self.build(decision_rows=rows)
    def test_overdue_neutral_decision_rejected(self):
        rows=copy.deepcopy(self.rows);rows[0]['reconciliation_utc']=AT
        with self.assertRaises(ValueError):self.build(decision_rows=rows)
    def test_silent_deadline_extension_rejected(self):
        rows=copy.deepcopy(self.rows);rows[0]['reconciliation_utc']=(gate.clock(rows[0]['reconciliation_utc'])+timedelta(minutes=1)).isoformat()
        with self.assertRaisesRegex(ValueError,'deadline extension'):
            week.compile(*self.proposals,self.capture,self.lineage,'CFB_PRESENTATION_RECONCILIATION_20261019T180600Z','2026-10-19T18:07:00Z','2026-10-19T18:06:01Z',rows)
    def test_original_exclusions_never_filled(self):
        census=json.loads(self.lineage)['rows'];excluded=[r for r in census if r['first_frozen_status']=='EXCLUDED']
        self.assertEqual(len(excluded),7)
        for r in excluded:self.assertIn(r['display'].replace('|','&#124;'),self.sheet)
    def test_all_retained_boards_normalize_complete(self):
        for stamp,sha,at in week.RETAINED:
            raw=(ROOT/('evidence/operational/CFB_CBS_WEEK8_FULL_BOARD_TABLES_'+stamp+'.md')).read_text()
            result=week.board(raw,self.lineage,at);self.assertEqual(result['coverage']['source_team_rows'],112)
    def test_final_open_do_not_affect_market(self):
        lines=self.capture.splitlines()
        for i,l in enumerate(lines):
            if l.startswith('| [') and '/teams/' in l:
                c=l.strip('|').split('|');c[1]='999999';c[2]='-999999 -110';lines[i]='|'+'|'.join(c)+'|'
        a=week.board(self.capture,self.lineage,BY);b=week.board('\n'.join(lines),self.lineage,BY)
        self.assertEqual(a['games'],b['games'])
    def test_changed_retained_source_rejected(self):
        def loader(p):return (ROOT/p).read_text()+'\n'
        with self.assertRaises(ValueError):week.retained_rows(self.lineage,loader)
    def test_untyped_tail_rejected(self):
        with self.assertRaises(ValueError):gate.inputs(self.proposals[0]+'extra',self.proposals[1],self.lineage,AT,'WEEK8')
    def test_changed_first_observation_rejected(self):
        p=self.proposals[0];prefix,first=week.first_packet(p,week.MARKET_TAG);first['rows'][0]['first']=None
        changed=prefix+week.packet(first,week.MARKET_TAG).lstrip('\n')
        with self.assertRaises(ValueError):week.bootstrap_check(changed,self.proposals[1],self.lineage)
    def test_old_week_decisions_cannot_substitute(self):
        old=gate.selected_block(self.decision,gate.DECISION_TAG,(gate.DECISION_SCHEMA,)+gate.WEEKLY_DECISION_SCHEMAS,gate.clock(AT))
        rows=[{k:v for k,v in r.items() if k not in ('state_recorded_at_utc','state_evidence')} for r in old['rows']]
        with self.assertRaises(ValueError):self.build(decision_rows=rows)
    def test_future_packet_or_cycle_rejected(self):
        with self.assertRaises(ValueError):self.build(cycle='CFB_PRESENTATION_RECONCILIATION_20261019T190000Z')
    def test_kickoff_does_not_become_qualified(self):
        mr=gate.inputs(*self.proposals,self.lineage,AT,'WEEK8')[3]
        self.assertTrue(all(r['kickoff_status']=='RETAINED_UNVERIFIED' for r in mr.values()))
    def test_saved_render_tampering_rejected(self):
        with self.assertRaises(ValueError):gate.audit(self.sheet.replace('49 predictions','50 predictions'),*self.proposals,'execution','scorecard',self.lineage,AT,'WEEK8')

    def test_elapsed_games_keep_prospective_pass_and_observation(self):
        rows=copy.deepcopy(self.rows)
        for row in rows:row['state']='PASS'
        first=self.build(decision_rows=rows)
        second=week.compile(*first,self.capture,self.lineage,'CFB_PRESENTATION_RECONCILIATION_20261020T233000Z','2026-10-20T23:31:00Z','2026-10-20T23:30:01Z',rows)
        parsed=gate.inputs(*second,self.lineage,'2026-10-20T23:31:00Z','WEEK8')
        elapsed=[r for r in parsed[3].values() if gate.clock(r['kickoff_utc'])<=gate.clock('2026-10-20T23:31:00Z')]
        self.assertEqual(len(elapsed),3)
        self.assertTrue(all(r['current'] is None and r['retained'] is not None for r in elapsed))
        self.assertTrue(all(parsed[4][r['game_id']]['state_recorded_at_utc']==AT for r in elapsed))
    def test_elapsed_initial_bootstrap_cannot_reconstruct_decisions(self):
        with self.assertRaisesRegex(ValueError,'cannot reconstruct'):
            self.build(cycle='CFB_PRESENTATION_RECONCILIATION_20261020T233000Z',as_of='2026-10-20T23:31:00Z',recovered_by='2026-10-20T23:30:01Z')
    def test_missing_intermediate_identity_cannot_erase_history(self):
        prefix,first=week.first_packet(self.proposals[1],week.DECISION_TAG);first['rows'].pop()
        changed=prefix+week.packet(first,week.DECISION_TAG).lstrip('\n')
        with self.assertRaises(ValueError):week.bootstrap_check(self.proposals[0],changed,self.lineage)
    def test_no_quote_means_unavailable_not_empty_available(self):
        row=copy.deepcopy(week.retained_rows(self.lineage)[0][self.rows[0]['game_id']]);old=row['current'] or row['retained']
        week.apply(row,None,AT)
        self.assertIsNone(row['current']);self.assertEqual(row['retained'],old);self.assertEqual(row['current_availability'],'UNAVAILABLE')
    def test_original_archive_independent147numeric_fields(self):
        from cfb_week8_frozen_field_invariant import audit
        archive=Path(os.environ['CFB_ACCEPTED_FREEZE_ARCHIVE'])
        result=audit(self.sheet,self.lineage,archive);self.assertEqual(result['numeric_fields'],147)
        for changed in (self.sheet.replace('49 predictions','50 predictions'),self.sheet.replace('FIRST_FROZEN:','REFRESH:',1)):
            with self.assertRaises(ValueError):audit(changed,self.lineage,archive)
    def test_week8_readiness_and_saved_audit_are_profile_explicit(self):
        import cfb_hot_sheet_readiness as readiness
        import cfb_saved_publication_audit as saved
        r=readiness.audit(*self.proposals,self.lineage,AT,'WEEK8');self.assertEqual(r['games'],56)
        result=saved.audit(self.sheet,*self.proposals,'execution','scorecard',self.lineage,AT,'WEEK8')
        self.assertEqual(result['current_operational_acceptance'],'NOT_CERTIFIED')
    def test_conditional_review_cannot_use_unknown_lineage(self):
        import cfb_conditional_recommendation_profile as conditional
        with self.assertRaisesRegex(ValueError,'unqualified conditional lineage'):
            conditional.validate({}, {}, {}, AT, '0'*40)

if __name__=='__main__':unittest.main()
