"""Synthetic interface/negative controls, no live candidate predictions."""
import ast,copy,tempfile,unittest
from pathlib import Path
from types import SimpleNamespace
import numpy as np,pandas as pd
import cfb_qa_s2_k1_input_gate as gate

CUT='2026-10-13T15:13:13+00:00';TARGET='2026-10-24T18:00:00+00:00';SOURCE='2026-10-01T18:00:00+00:00'

def fixture():
    fs,mp=gate.frozen_interface();snap={'snapshot_type':'REFRESH_SNAPSHOT','snapshot_cutoff_utc':CUT}
    G=pd.DataFrame([dict(season=2026,game_id='SYNTHETIC',start_date=TARGET,home_team='SYNTH_HOME',away_team='SYNTH_AWAY',neutral_site=False,population_class='FBS_VS_FBS',**snap)])
    sides=[];base=[];context=[];chron=[]
    for side,team in [('home','SYNTH_HOME'),('away','SYNTH_AWAY')]:
        sides.append(dict(game_id='SYNTHETIC',side=side,team=team,target_kickoff=TARGET,qualified_prior_games=1,eligible=True,reason='',**{f:9.0 for f in fs},**snap))
        base.append(dict(game_id='SYNTHETIC',team=team,target_kickoff=TARGET,qualified_prior_games=1,**{p+f:(7.0 if p=='baseline__' else True) for f in fs for p in ('baseline__','available__')},snapshot_type='S2_K1_TARGET_BASELINE',snapshot_cutoff_utc=CUT))
        context.append(dict(target_game_id='SYNTHETIC',target_side=side,target_team=team,target_kickoff=TARGET,source_game_id='PRIOR_'+side,source_kickoff=SOURCE,source_opponent='OPP_'+side,opponent_qualified_prior_games=1,mechanical_history_complete=True,derived_history_complete=True,**{p+mp[f] if p!='context_valid__' else p+f:(True if p=='context_valid__' else 9.0 if p=='raw__' else 7.0) for f in mp for p in ('baseline__','raw__','context_valid__')},snapshot_type='S2_K1_SOURCE_CONTEXT',snapshot_cutoff_utc=CUT))
        chron.append(dict(game_id='SYNTHETIC',side=side,team=team,prior_games=1,max_prior_kickoff=SOURCE,target_kickoff=TARGET,own_game_excluded=True,strict_chronology=True,**snap))
    P=G.drop(columns=['neutral_site','population_class']).assign(venue_state='HOME',pred_margin=1.,pred_total=50.,pred_win=.51)
    E=pd.DataFrame(columns=gate.schemas()['excluded'])
    return dict(side=pd.DataFrame(sides),target=G,baseline=pd.DataFrame(base),context=pd.DataFrame(context),predicted=P,excluded=E,chronology=pd.DataFrame(chron))


class InterfaceTests(unittest.TestCase):
    def test_valid_complete_interface(self):
        self.assertEqual(gate.validate_frames(fixture(),CUT)['s0_eligible_games'],1)
    def test_source_at_or_after_cutoff_and_target_self_reference(self):
        for field,value in [('source_kickoff',CUT),('source_kickoff',TARGET),('source_game_id','SYNTHETIC')]:
            f=fixture();f['context'].loc[0,field]=value
            with self.subTest(field=field,value=value),self.assertRaises(ValueError):gate.validate_frames(f,CUT)
    def test_positive_integer_counts_only(self):
        for value in [-1,.5,np.nan,np.inf]:
            f=fixture();f['side']['qualified_prior_games']=f['side']['qualified_prior_games'].astype(float);f['side'].loc[0,'qualified_prior_games']=value
            with self.subTest(value=value),self.assertRaises(ValueError):gate.validate_frames(f,CUT)
    def test_context_count_and_identity_are_exact(self):
        for mutation in ['missing','duplicate','wrong_team','wrong_role','self_opponent','wrong_target_time']:
            f=fixture();c=f['context']
            if mutation=='missing':f['context']=c.iloc[1:]
            if mutation=='duplicate':f['context']=pd.concat([c,c.iloc[:1]])
            if mutation=='wrong_team':c.loc[0,'target_team']='UNKNOWN'
            if mutation=='wrong_role':c.loc[0,'target_side']='away'
            if mutation=='self_opponent':c.loc[0,'source_opponent']='SYNTH_HOME'
            if mutation=='wrong_target_time':c.loc[0,'target_kickoff']='2026-10-25T18:00:00+00:00'
            with self.subTest(mutation=mutation),self.assertRaises(ValueError):gate.validate_frames(f,CUT)
    def test_s0_eligibility_not_manufactured(self):
        f=fixture();f['side'].loc[0,'eligible']=False
        with self.assertRaisesRegex(ValueError,'S0_ELIGIBILITY'):gate.validate_frames(f,CUT)
    def test_s0_partition_identity_and_probability(self):
        for mutation in ['missing','duplicate','identity','probability']:
            f=fixture()
            if mutation=='missing':f['predicted']=f['predicted'].iloc[:0]
            if mutation=='duplicate':f['predicted']=pd.concat([f['predicted']]*2)
            if mutation=='identity':f['predicted'].loc[0,'away_team']='UNKNOWN'
            if mutation=='probability':f['predicted'].loc[0,'pred_win']=1.1
            with self.subTest(mutation=mutation),self.assertRaises(ValueError):gate.validate_frames(f,CUT)
    def test_false_completion_flags_not_treated_as_true_strings(self):
        f=fixture();f['context']['mechanical_history_complete']=f['context']['mechanical_history_complete'].astype(object);f['context'].loc[0,'mechanical_history_complete']='False'
        with self.assertRaisesRegex(ValueError,'COMPLETION_FLAG'):gate.validate_frames(f,CUT)
    def test_zero_history_context_raw_missing_is_valid(self):
        f=fixture();f['context']['opponent_qualified_prior_games']=0
        for c in f['context']:
            if c.startswith('raw__'):f['context'][c]=np.nan
        gate.validate_frames(f,CUT)
    def test_baseline_binding_and_availability(self):
        for field,value in [('qualified_prior_games',2),('target_kickoff',SOURCE),('available__points_for_per_game',False)]:
            f=fixture();f['baseline'].loc[0,field]=value
            with self.subTest(field=field),self.assertRaises(ValueError):gate.validate_frames(f,CUT)
    def test_chronology_proof_required_and_bound(self):
        for field,value in [('own_game_excluded',False),('strict_chronology','False'),('max_prior_kickoff','2026-10-02T18:00:00+00:00'),('prior_games',2)]:
            f=fixture();f['chronology'][field]=f['chronology'][field].astype(object);f['chronology'].loc[0,field]=value
            with self.subTest(field=field),self.assertRaises(ValueError):gate.validate_frames(f,CUT)
    def test_2025_and_mixed_cutoff_rejected(self):
        for kind,field,value in [('target','season',2025),('context','snapshot_cutoff_utc','2026-10-14T15:00:00+00:00')]:
            f=fixture();f[kind].loc[0,field]=value
            with self.subTest(kind=kind),self.assertRaises(ValueError):gate.validate_frames(f,CUT)
    def test_naive_and_missing_clock_rejected(self):
        for v in ['2026-10-01T18:00:00',None]:
            f=fixture();f['context'].loc[0,'source_kickoff']=v
            with self.subTest(v=v),self.assertRaises(ValueError):gate.validate_frames(f,CUT)
    def test_forbidden_or_unknown_fields_never_enter_dataframe(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'side.csv';cols=gate.schemas()['side']
            for bad in ['winner','ranking','actual_score','unused_new_metadata']:
                fixture()['side'].assign(**{bad:'FORBIDDEN_SENTINEL'}).to_csv(p,index=False)
                with self.subTest(bad=bad),self.assertRaisesRegex(ValueError,'ALLOWLIST'):gate.read_projected(p,cols)
            fixture()['side'].to_csv(p,index=False)
            self.assertEqual(set(gate.read_projected(p,cols)),set(cols))
    def test_duplicate_header_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'bad.csv';p.write_text('game_id,game_id\na,a\n')
            with self.assertRaisesRegex(ValueError,'DUPLICATE_INPUT_COLUMN'):gate.read_projected(p,['game_id'])


class HistoricalSignTests(unittest.TestCase):
    def test_frozen_exact_mapping_and_sign(self):
        p=Path(__file__).with_name('cfb_qa_sandbox_candidate_generator_2026_09_27.py')
        source=p.read_text();import hashlib
        raw=source.encode();self.assertEqual(hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest(),'40447984a58dbc530cbe942bc1176f0c5bcbe9b2')
        tree=ast.parse(source);s2=next(n for n in ast.walk(tree) if isinstance(n,ast.FunctionDef) and n.name=='s2')
        ns={'np':np,'pd':pd,'MAP':{'points_for_per_game':'points_against_per_game'},'s1':lambda r,f,k:8. if r.team=='SYNTH_TEAM' else 9.,'baseline':lambda *a:7.,'prior_history_cache':{},'feature_history_idx':pd.DataFrame([{'season':2016,'game_id':'PRIOR','team':'OPP','_mechanical_complete_bool':True,'_derived_complete_bool':True}]).set_index(['season','game_id','team'])}
        source_at=pd.Timestamp('2016-09-01T12:00:00Z');target_at=pd.Timestamp('2016-10-01T12:00:00Z')
        ns['ident']=pd.DataFrame([dict(season=2016,game_id='PRIOR',team='SYNTH_TEAM',opponent='OPP',start_date=source_at)])
        ns['side_idx']=pd.DataFrame([dict(season=2016,game_id='PRIOR',team='OPP',start_date=source_at,qualified_prior_games=1,points_against_per_game=11.)]).set_index(['season','game_id','team'],drop=False)
        exec(compile(ast.Module(body=[s2],type_ignores=[]),str(p),'exec'),ns)
        expected=ns['s2'](SimpleNamespace(season=2016,game_id='TARGET',team='SYNTH_TEAM',start_date=target_at,qualified_prior_games=1),'points_for_per_game',1)
        self.assertEqual(expected,6.)
        current=Path(__file__).with_name('cfb_qa_prospective_s2_k1_consumer_v1_2026_09_30.py')
        assignments=[n for n in ast.walk(ast.parse(current.read_text())) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='s2' for t in n.targets) and isinstance(n.value,ast.BinOp)]
        self.assertEqual(len(assignments),1)
        got=eval(compile(ast.Expression(assignments[0].value),'prospective_sign','eval'),{'s1':8.,'resid':np.array([2.])})
        self.assertEqual(got,expected)
        self.assertNotEqual(8.+2.,expected)
        frozenmap=next(n for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='MAP' for t in n.targets))
        self.assertEqual(gate.frozen_interface()[1],ast.literal_eval(frozenmap.value))

class ExecutionBoundaryTests(unittest.TestCase):
    def test_new_cutoff_requires_separate_acceptance(self):
        with self.assertRaisesRegex(ValueError,'UNQUALIFIED_INPUT_ACCEPTANCE'):
            gate.accepted_input_binding({},'2026-10-20T15:00:00+00:00')
    def test_modified_accepted_bytes_cannot_enter(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'modified.csv';p.write_text('synthetic modified input')
            with self.assertRaisesRegex(ValueError,'ACCEPTED_INPUT_BYTES'):
                gate.accepted_input_binding({'side':p},'2026-10-13T15:13:13.866672+00:00')
    def test_full_synthetic_prediction_matches_independent_frozen_config_math(self):
        # Synthetic fixture and explicit simulated clock only. No real target
        # feature rows, actual live snapshot or retrospective predictions.
        import os,sys,io,contextlib,hashlib,json
        from datetime import datetime,timezone
        from unittest.mock import patch
        fit=Path(os.environ['CFB_S2_FROZEN_FIT'])
        source=Path(__file__).with_name('cfb_qa_prospective_s2_k1_consumer_v1_2026_09_30.py')
        tree=ast.parse(source.read_text())
        tree.body=[n for n in tree.body if not (isinstance(n,ast.ImportFrom) and n.module=='datetime')]
        frames=fixture()
        gate.validate_frames(frames,CUT)
        audit={'input_sha256':{k:'a'*64 for k in frames},'input_gate_sha256':'b'*64,
               'raw_source_sha256':{'schedule':'c'*64,'pbp':'d'*64},'acceptance_records':{'SYNTHETIC_TEST_ONLY':'e'*40}}
        class SimulatedDateTime:
            @staticmethod
            def now(tz):return datetime(2026,10,13,16,tzinfo=timezone.utc)
        code=compile(tree,str(source),'exec')
        with tempfile.TemporaryDirectory() as d:
            out=Path(d)/'synthetic_only'
            argv=['consumer','side','target','baseline','context',str(fit),str(out),CUT,'--execute-prospective']
            with patch.object(sys,'argv',argv),patch.object(gate,'load_inputs',return_value=(copy.deepcopy(frames),copy.deepcopy(audit))),contextlib.redirect_stdout(io.StringIO()):
                exec(code,{'__file__':str(source),'datetime':SimulatedDateTime,'timezone':timezone})
            got=pd.read_csv(out/'s2_k1_predictions.csv').iloc[0]
            fs,mp=gate.frozen_interface();scale=pd.read_csv(fit/'train_scaling.csv').set_index('feature');coef=pd.read_csv(fit/'selected_coefficients.csv')
            vals={prefix+f:(7. if f in mp else 8.) for f in fs for prefix in ('home_','away_')}
            for target in ('margin','total','win'):
                c=coef[coef.target==target].set_index('term').coefficient
                expected=c['intercept']+sum((value-scale.loc[name,'mean'])/scale.loc[name,'sd']*c[name] for name,value in vals.items())
                if target=='win':expected=1/(1+np.exp(-np.clip(expected,-40,40)))
                self.assertAlmostEqual(got['pred_'+target],expected,places=11)
            self.assertEqual(got.history_depth_slice,'DEPTH_1_2')
            self.assertEqual(got.s0_pred_margin,1.)
            manifest=json.loads((out/'manifest.json').read_text())
            self.assertEqual(manifest['frozen_config']['context_sign'],'SUBTRACT_MEAN_PAIRED_RESIDUAL')
            self.assertEqual(manifest['input_sha256'],audit['input_sha256'])
            for name,digest in manifest['hashes'].items():self.assertEqual(hashlib.sha256((out/name).read_bytes()).hexdigest(),digest)
            self.assertEqual(list(pd.read_csv(out/'s2_k1_side_exclusions.csv').columns),['game_id','team','reason'])
        # The CLI refuses a source-valid but now-elapsed population before any fit
        # is opened or output is created. A simulated observation clock is explicit.
        class AfterKickoff:
            @staticmethod
            def now(tz):return datetime(2026,10,25,16,tzinfo=timezone.utc)
        with tempfile.TemporaryDirectory() as d:
            out=Path(d)/'must_not_exist'
            argv=['consumer','side','target','baseline','context','UNOPENED_FIT',str(out),CUT,'--execute-prospective']
            with patch.object(sys,'argv',argv),patch.object(gate,'load_inputs',return_value=(copy.deepcopy(frames),copy.deepcopy(audit))),self.assertRaisesRegex(SystemExit,'ELAPSED_TARGETS_PROHIBITED'):
                exec(code,{'__file__':str(source),'datetime':AfterKickoff,'timezone':timezone})
            self.assertFalse(out.exists())


if __name__=='__main__':unittest.main()
