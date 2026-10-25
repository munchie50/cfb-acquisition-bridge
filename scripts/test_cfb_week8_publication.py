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

class SameDayElapsedContextTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw=(ROOT/'evidence/operational/CFB_CBS_WEEK8_TEXT_TABLE_CAPTURE_20261023T023243Z.md').read_text()
        cls.lineage=(ROOT/'evidence/scheduler_qa/CFB_WEEK8_ORIGINAL_ANCESTRY_RECOVERY_20261020.json').read_text()
    def parse(self,context=None):
        return week.board(self.raw,self.lineage,'2026-10-23T02:34:29Z',retained_elapsed_kickoffs=context)
    def test_today_date_only_still_rejects_without_prior_elapsed_identity(self):
        with self.assertRaises(ValueError):self.parse()
    def test_known_elapsed_context_does_not_invent_source_kickoff(self):
        r=self.parse({'401871056':'2026-10-22T23:00:00Z'})
        self.assertEqual(r['coverage']['matched_games'],56)
        self.assertEqual(r['coverage']['future_games'],49)
        row=next(x for x in r['games'] if x['game_id']=='401871056')
        self.assertIsNone(row['source_kickoff_utc'])
        self.assertNotEqual(row['temporal_status'],'FUTURE_AT_CAPTURE')
    def test_other_identity_cannot_resolve_missing_today_time(self):
        with self.assertRaises(ValueError):self.parse({'401866448':'2026-10-22T23:00:00Z'})
    def test_future_equal_or_wrong_local_date_context_rejected(self):
        for stamp in ('2026-10-23T02:34:29Z','2026-10-24T23:00:00Z','2026-10-21T23:00:00Z'):
            with self.subTest(stamp=stamp),self.assertRaises(ValueError):self.parse({'401871056':stamp})
    def test_unknown_context_identity_rejected(self):
        with self.assertRaises(ValueError):self.parse({'UNKNOWN':'2026-10-22T23:00:00Z'})
    def test_actual_compiler_composes_prior_stream_and_preserves_elapsed_quote(self):
        m=historical(ROOT/'evidence/operational/CFB_MARKET_MONITOR_STATE.md','8c8e98e6cb56d638da7420d42ca1fa07c7fc6691')
        d=historical(ROOT/'evidence/operational/CFB_DECISION_WAIT_LEDGER.md','13709bb0eb6e8e9c0ebc115dda22130737b198a1')
        old=gate.inputs(m,d,self.lineage,'2026-10-23T02:22:21Z','WEEK8')
        rows=[{k:v for k,v in row.items() if k not in ('state_recorded_at_utc','state_evidence')} for row in old[4].values()]
        pm,pd=week.compile(m,d,self.raw,self.lineage,'CFB_MARKET_MONITOR_20261023T023243Z','2026-10-23T02:36:00Z','2026-10-23T02:34:29Z',rows)
        new=gate.inputs(pm,pd,self.lineage,'2026-10-23T02:36:00Z','WEEK8')
        self.assertTrue(pm.startswith(m));self.assertTrue(pd.startswith(d))
        self.assertEqual(old[3]['401871056'],new[3]['401871056'])
        self.assertEqual(new[4]['401866448']['state'],'CONDITIONAL')

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
        with self.assertRaises(ValueError):gate.profile_config('WEEK10')
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

    def recovery(self, **kw):
        """Authentic retained response, explicit simulated clocks/decisions only."""
        at='2026-10-22T18:30:00Z';by='2026-10-22T18:29:00Z'
        capture=(ROOT/'evidence/operational/CFB_CBS_WEEK8_CURRENT_RESPONSE_20261022T180321Z.md').read_text()
        parsed=week.board(capture,self.lineage,by)
        rows=copy.deepcopy(self.rows)
        for row in rows:
            if row['game_id'] in week.RECOVERY_GAPS:
                row.update(state=week.GAP_STATE,reason='SYNTHETIC QA gap recognition; no earlier pre-event decision exists',
                           reconciliation_utc=None,planning_cutoff_utc=None)
        args=dict(market=self.market,decision=self.decision,capture=capture,lineage=self.lineage,
                  cycle='CFB_PRESENTATION_RECONCILIATION_20261022T182900Z',as_of=at,recovered_by=by,
                  decision_rows=rows,recovery_authority=week.RECOVERY_AUTHORITY)
        args.update(kw)
        return week.compile(**args),args

    def test_recovery_preserves_all56_and_four_honest_gaps(self):
        proposals,args=self.recovery()
        parsed=gate.inputs(*proposals,self.lineage,args['as_of'],'WEEK8')
        self.assertEqual(len(parsed[4]),56)
        self.assertEqual({gid for gid,r in parsed[4].items() if r['state']==week.GAP_STATE},week.RECOVERY_GAPS)
        for gid in week.RECOVERY_GAPS:
            self.assertIsNone(parsed[3][gid]['current'])
            self.assertEqual(parsed[4][gid]['state_recorded_at_utc'],args['as_of'])
        self.assertTrue(proposals[0].startswith(self.market));self.assertTrue(proposals[1].startswith(self.decision))

    def test_recovery_renderer_and_readiness_never_call_gap_pass(self):
        import cfb_hot_sheet_readiness as readiness
        from cfb_week8_frozen_field_invariant import audit
        proposals,args=self.recovery()
        sheet=gate.render(*proposals,'execution','scorecard',self.lineage,args['as_of'],'WEEK8')
        self.assertEqual(sheet.count('MISSED PRE-EVENT DECISION'),4)
        self.assertIn('**Primary section:** THURSDAY',sheet)
        self.assertNotIn('historical PASS',sheet)
        r=readiness.audit(*proposals,self.lineage,args['as_of'],'WEEK8')
        self.assertEqual(r['historical_gaps'],4);self.assertEqual(r['preserved_pass'],0)
        self.assertFalse(week.RECOVERY_GAPS & set(r['review_required_game_ids']))
        self.assertEqual(len(r['review_required_game_ids']),52)
        self.assertEqual(audit(sheet,self.lineage,Path(os.environ['CFB_ACCEPTED_FREEZE_ARCHIVE']))['numeric_fields'],147)

    def test_recovery_without_exact_authority_still_rejects(self):
        for authority in (None,'0'*40):
            with self.subTest(authority=authority),self.assertRaises(ValueError):self.recovery(recovery_authority=authority)

    def test_recovery_cannot_invent_pass_in_missed_history(self):
        _,args=self.recovery()
        row=next(r for r in args['decision_rows'] if r['game_id'] in week.RECOVERY_GAPS)
        row['state']='PASS'
        with self.assertRaises(ValueError):week.compile(**args)

    def test_recovery_cannot_add_a_gap_for_future_game(self):
        _,args=self.recovery()
        row=next(r for r in args['decision_rows'] if r['game_id'] not in week.RECOVERY_GAPS)
        row.update(state=week.GAP_STATE,reconciliation_utc=None,planning_cutoff_utc=None)
        with self.assertRaises(ValueError):week.compile(**args)

    def test_recovery_cannot_claim_limit_or_backdate_gap(self):
        _,args=self.recovery()
        for key,value in (('acceptable_number',{}),('planning_cutoff_utc','2026-10-22T18:00:00Z')):
            changed=copy.deepcopy(args)
            next(r for r in changed['decision_rows'] if r['game_id'] in week.RECOVERY_GAPS)[key]=value
            with self.subTest(key=key),self.assertRaises(ValueError):week.compile(**changed)
        with self.assertRaises(ValueError):self.recovery(as_of='2026-10-22T18:07:00Z',recovered_by='2026-10-22T18:06:00Z',cycle='CFB_PRESENTATION_RECONCILIATION_20261022T180600Z')

    def test_recovery_gap_cannot_be_rewritten_or_reopened(self):
        proposals,args=self.recovery()
        args.update(market=proposals[0],decision=proposals[1],as_of='2026-10-22T18:35:00Z',
                    recovered_by='2026-10-22T18:34:00Z',cycle='CFB_PRESENTATION_RECONCILIATION_20261022T183400Z',recovery_authority=None)
        second=week.compile(**args)
        week.bootstrap_check(*second,self.lineage)
        for key,value in (('reason','rewritten missing history'),('state','PASS')):
            changed=copy.deepcopy(args)
            next(r for r in changed['decision_rows'] if r['game_id'] in week.RECOVERY_GAPS)[key]=value
            with self.subTest(key=key),self.assertRaises(ValueError):week.compile(**changed)

    def test_recovery_cannot_reset_stream_or_expand_after_another_kickoff(self):
        proposals,args=self.recovery()
        args.update(market=proposals[0],decision=proposals[1])
        with self.assertRaisesRegex(ValueError,'initial-only'):week.compile(**args)
        with self.assertRaises(ValueError):self.recovery(as_of='2026-10-22T23:01:00Z',
            recovered_by='2026-10-22T23:00:01Z',cycle='CFB_PRESENTATION_RECONCILIATION_20261022T230000Z')

    def test_recovery_declaration_and_intermediate_gap_cannot_disappear(self):
        proposals,args=self.recovery()
        with self.assertRaises(ValueError):gate.inputs(proposals[0].replace(week.RECOVERY_AUTHORITY,'0'*40),proposals[1],self.lineage,args['as_of'],'WEEK8')
        prefix,packet=week.first_packet(proposals[1],week.DECISION_TAG)
        packet['rows']=[r for r in packet['rows'] if r['game_id'] not in week.RECOVERY_GAPS]
        changed=prefix+week.packet(packet,week.DECISION_TAG).lstrip('\n')
        with self.assertRaises(ValueError):gate.inputs(proposals[0],changed,self.lineage,args['as_of'],'WEEK8')

    def test_future_week8_current_selection_through_existing_recovery_consumer(self):
        from cfb_recovery_consumer_preflight import audit as preflight
        from datetime import datetime,timezone
        index=(ROOT/'evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_245.md').read_text()
        matches=list(re.finditer(r'^```cfb-frontier-json\n(.*?)^```',index,re.M|re.S))
        record=json.loads(matches[-1][1]);now=datetime.now(timezone.utc).isoformat()
        record['as_of_utc']=now;record['claims']=['SYNTHETIC FUTURE SELECTION TEST ONLY; no operational mutation']
        op='evidence/operational/'
        values={op+'CFB_MARKET_MONITOR_STATE.md':self.proposals[0],op+'CFB_DECISION_WAIT_LEDGER.md':self.proposals[1]}
        sheet_path=op+'CFB_WEEK8_HOT_SHEET_2026-10-19_1305CT.md'
        values[sheet_path]=self.sheet
        for pointer in record['pointers']:
            if pointer['purpose'].startswith('CURRENT_HOT_SHEET:'):pointer['purpose']='HISTORICAL_HOT_SHEET: retained Week7 fixture'
            if pointer['path'] in values:pointer['blob']=gate.blob(values[pointer['path']])
        record['pointers'].append({'path':sheet_path,'blob':gate.blob(self.sheet),'purpose':'CURRENT_HOT_SHEET: synthetic Week8 selector fixture'})
        proposal=index+'\n```cfb-frontier-json\n'+json.dumps(record)+'\n```\n'
        def loader(path):return values[path] if path in values else (ROOT/path).read_text()
        result=preflight(proposal,loader,now)
        self.assertEqual(result['sheet_path'],sheet_path)
        self.assertEqual(result['verdict'],'PASS_CURRENT_RECOVERY_CONSUMER_BINDINGS_ONLY')

if __name__=='__main__':unittest.main()
