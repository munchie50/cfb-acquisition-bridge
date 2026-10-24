"""Synthetic timing quarantine and exact-parent projection rejection controls."""
import copy,json,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
import cfb_qa_s2_k1_projection as gate
from test_cfb_qa_s2_k1_input_gate import fixture,CUT

AT='2026-10-23T03:00:00+00:00'
LINEAGE=(gate.ROOT/gate.LINEAGE_PATH).read_bytes()
IDENT=json.loads(LINEAGE)['rows']


def source(rows=IDENT,split=False,live=False,token='12:00 pm'):
    parts=['All times are US/Eastern.','<h2 class="TableBase-title">Saturday, October 24, 2026</h2><table>']
    for i,r in enumerate(rows):
        if split and i==20:parts.append('</table><table>')
        a,h='A'+str(i),'H'+str(i)
        parts.append('<tr class="TableBase-bodyTr"><td><span class="TeamName"><a href="/college-football/teams/'+a+'/team/">'+r['away_team']+'</a></span></td><td><span class="TeamName"><a href="/college-football/teams/'+h+'/team/">'+r['home_team']+'</a></span></td><td><div class="CellGame"><a href="/college-football/gametracker/'+('live' if live else 'preview')+'/NCAAF_20261024_'+a+'@'+h+'/">'+token+'</a></div></td><td>FORBIDDEN_ODDS_OR_RESULT_SENTINEL</td></tr>')
    parts.append('</table>');raw=''.join(parts).encode()
    return raw,{'url':gate.URL,'response_recovered_by_utc':'2026-10-23T02:59:00+00:00','sha256':gate.sha(raw),'bytes':len(raw),'quarantine':'RAW_PAGE_NOT_CANDIDATE_INPUT'}


class TimingQuarantineTests(unittest.TestCase):
    def test_full56_live_link_future_times_and_multiple_tables(self):
        raw,meta=source(split=True,live=True)
        c=gate.schedule_census(raw,meta,LINEAGE,AT)
        self.assertEqual(len(c['rows']),56)
        self.assertTrue(all(r['qualified_kickoff_utc']=='2026-10-24T16:00:00+00:00' for r in c['rows']))
        self.assertNotIn('FORBIDDEN_',json.dumps(c))
    def test_non_time_score_or_market_text_never_leaves_quarantine(self):
        for token in ['HOME 35 - AWAY 14','12:00 pm -110','TBA','Final']:
            raw,meta=source(token=token);c=gate.schedule_census(raw,meta,LINEAGE,AT)
            self.assertTrue(all(r['qualified_kickoff_utc'] is None for r in c['rows']))
            self.assertNotIn(token,json.dumps(c))
    def test_missing_duplicate_and_wrong_names_rejected(self):
        for rows in [IDENT[:-1],IDENT+[IDENT[0]],[dict(r,away_team='Texas Tech' if r['away_team']=='Texas' else r['away_team'],home_team='Texas Tech' if r['home_team']=='Texas' else r['home_team']) for r in IDENT]]:
            raw,meta=source(rows)
            with self.assertRaises(ValueError):gate.schedule_census(raw,meta,LINEAGE,AT)
    def test_missing_timezone_and_wrong_date_or_codes_rejected(self):
        raw,meta=source()
        for before,after in [(b'US/Eastern',b'US/Central'),(b'NCAAF_20261024_A0',b'NCAAF_20261023_A0'),(b'20261024_A0@H0',b'20261024_A0@H999')]:
            changed=raw.replace(before,after);m={**meta,'sha256':gate.sha(changed),'bytes':len(changed)}
            with self.assertRaises(ValueError):gate.schedule_census(changed,m,LINEAGE,AT)
    def test_response_hash_future_clock_and_wrong_cohort_rejected(self):
        raw,meta=source()
        for m,l in [({**meta,'sha256':'0'*64},LINEAGE),({**meta,'response_recovered_by_utc':'2026-10-25T00:00:00Z'},LINEAGE),(meta,LINEAGE+b'\n')]:
            with self.assertRaises(ValueError):gate.schedule_census(raw,m,l,AT)
    def test_actual_elapsed_time_is_not_reconstructed_as_future(self):
        raw,meta=source();c=gate.schedule_census(raw,meta,LINEAGE,'2026-10-25T00:00:00Z')
        self.assertTrue(all(r['timing_status']=='EXPLICIT_ELAPSED' for r in c['rows']))


class ExactRowTests(unittest.TestCase):
    def test_byte_preserving_projection_keeps_order_and_float_spelling(self):
        raw=b'game_id,value\r\na,0.10000000000000001\r\nb,2.0\r\nc,3e-4\r\n'
        result,ordinals=gate.projected_bytes(raw,'game_id',{'c','a'})
        self.assertEqual(result,b'game_id,value\r\na,0.10000000000000001\r\nc,3e-4\r\n');self.assertEqual(ordinals,[0,2])
    def test_multiline_duplicate_header_or_malformed_width_rejected(self):
        for raw in [b'game_id,value\na,"first\nsecond"\n',b'game_id,game_id\na,a\n',b'game_id,value\na,1,EXTRA\n']:
            with self.assertRaises(ValueError):gate.projected_bytes(raw,'game_id',{'a'})
    def test_empty_selected_output_retains_header(self):
        self.assertEqual(gate.projected_bytes(b'game_id,value\na,1\n','game_id',set()),(b'game_id,value\n',[]))


class AcceptanceTests(unittest.TestCase):
    def test_arbitrary_or_outside_reference_cannot_admit_projection(self):
        for ref in [{'path':'/tmp/self_accept.json','commit':'a'*40,'blob':'b'*40}, {'path':'evidence/qa_s2_projections/X.json','commit':'latest','blob':'b'*40}]:
            with self.assertRaises(ValueError):gate.immutable_ref(ref)
    def test_unaccepted_or_future_record_rejected(self):
        ref={'path':'evidence/qa_s2_projections/X.json','commit':'a'*40,'blob':'b'*40}
        record={'schema':'CFB_S2_FUTURE_PROJECTION_ACCEPTANCE_V1','accepted_at_utc':'2026-10-24T00:00:00Z','projection_ref':{},'timing_ref':{},'confirmation_ref':{},'implementation':{},'ci':[],'verification':{},'scope':'EXACT_PROJECTION_ACCEPTED_STUDY_ONLY_NOT_PREDICTION_FREEZE'}
        with patch.object(gate,'immutable_ref',return_value=(b'{}',record)),self.assertRaisesRegex(ValueError,'FUTURE_CLOCK'):gate.apply_accepted_projection('/tmp',ref,AT)

class ProjectionVerificationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import pandas as pd
        cls.tmp=tempfile.TemporaryDirectory();cls.package=Path(cls.tmp.name)
        buckets={k:[] for k in fixture()}
        for identity in IDENT:
            f=fixture();gid=identity['game_id'];home=identity['home_team'];away=identity['away_team']
            for kind,df in f.items():
                if 'game_id' in df:df['game_id']=gid
                if 'target_game_id' in df:df['target_game_id']=gid
                if 'team' in df:df['team']=df.team.replace({'SYNTH_HOME':home,'SYNTH_AWAY':away})
                if 'target_team' in df:df['target_team']=df.target_team.replace({'SYNTH_HOME':home,'SYNTH_AWAY':away})
                if 'home_team' in df:df['home_team']=home;df['away_team']=away
                buckets[kind].append(df)
        cls.frames={k:pd.concat(v,ignore_index=True) for k,v in buckets.items()}
        gate.validate_frames(cls.frames,CUT)
        cls.paths=gate.parent_paths(cls.package)
        for kind,path in cls.paths.items():path.parent.mkdir(parents=True,exist_ok=True);cls.frames[kind].to_csv(path,index=False)
        cls.audit={'cutoff_utc':CUT,'input_sha256':{k:gate.sha(p.read_bytes()) for k,p in cls.paths.items()},'acceptance_records':{'SYNTHETIC_TEST_ONLY':'a'*40}}
        raw,meta=source(split=True,live=True);cls.census=gate.schedule_census(raw,meta,LINEAGE,AT)
        cls.confirm=copy.deepcopy(cls.census);cls.confirm['source_recovered_by_utc']='2026-10-23T02:59:30+00:00'
        with patch.object(gate,'load_inputs',return_value=(cls.frames,cls.audit)):
            cls.proposal=gate.make_projection(cls.package,cls.census,AT)
    @classmethod
    def tearDownClass(cls):cls.tmp.cleanup()
    def verify(self,p=None,c=None,confirmation=None,at=AT):
        with patch.object(gate,'load_inputs',return_value=(self.frames,self.audit)):
            return gate.verify_projection(self.package,p or self.proposal,c or self.census,confirmation or self.confirm,at)
    def test_independent_projection_verifier_and_full_accounting(self):
        frames,proof=self.verify();self.assertEqual(proof['projected_targets'],56)
        self.assertEqual(set(frames['target'].game_id),set(self.proposal['selected_game_ids']))
        self.assertEqual(len(self.proposal['parent_dispositions']),56)
        for k in frames:self.assertTrue(frames[k].equals(self.frames[k]))
    def test_changed_subset_parent_hash_or_missing_accounting_rejected(self):
        for change in ['subset','dispositions','parenthash','kickoff']:
            p=copy.deepcopy(self.proposal)
            if change=='subset':p['selected_game_ids']=p['selected_game_ids'][:-1]
            if change=='dispositions':p['parent_dispositions']=p['parent_dispositions'][:-1]
            if change=='parenthash':p['parent_input_sha256']['side']='0'*64
            if change=='kickoff':p['qualified_kickoffs_utc'][p['selected_game_ids'][0]]='2026-10-25T16:00:00Z'
            with self.subTest(change=change),self.assertRaises(ValueError):self.verify(p=p)
    def test_reordered_dropped_or_rewritten_projected_bytes_rejected(self):
        for field,value in [('row_ordinals',[1,0]),('projected_sha256','0'*64),('rows',1)]:
            p=copy.deepcopy(self.proposal);p['surfaces']['side'][field]=value
            with self.subTest(field=field),self.assertRaises(ValueError):self.verify(p=p)
    def test_timing_reacquisition_missing_disagreement_or_fake_status_rejected(self):
        for change in ['sameclock','duplicate','differenttime','fakestatus']:
            c=copy.deepcopy(self.confirm)
            if change=='sameclock':c['source_recovered_by_utc']=self.census['source_recovered_by_utc']
            if change=='duplicate':c['rows'][1]=c['rows'][0]
            if change=='differenttime':c['rows'][0]['qualified_kickoff_utc']='2026-10-24T17:00:00+00:00'
            if change=='fakestatus':c['rows'][0]['timing_status']='EXPLICIT_ELAPSED'
            with self.subTest(change=change),self.assertRaises(ValueError):self.verify(confirmation=c)
    def test_expired_projection_cannot_silently_drop_targets(self):
        with self.assertRaises(ValueError):self.verify(at='2026-10-25T00:00:00Z')


if __name__=='__main__':unittest.main()
