"""Independent frozen-parameter prediction audit; no target outcomes or markets."""
import argparse,ast,hashlib,json,sys
from datetime import datetime,timezone
from pathlib import Path
import numpy as np,pandas as pd
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'scripts'))
from cfb_qa_s2_k1_projection import apply_accepted_projection,immutable_ref,clock,sha,blob,ROOT
from cfb_qa_s2_k1_input_gate import check,load_inputs
from cfb_qa_s2_k1_projection import parent_paths

COEF_SHA='bf15ce41180bfb4e250d311df279e98c13b65432756ae07f7a30264cbae0e221'
SCALE_SHA='68fb5193ccb8828ac8d34dfe820101181c2bde078a04a6d5afd4c08bcf0cab45'


def audit(package,fit,out,ref,as_of):
    frames,context=apply_accepted_projection(package,ref,as_of)
    paths=parent_paths(package);_,inputs=load_inputs(paths['side'],paths['target'],paths['baseline'],paths['context'],'2026-10-13T15:13:13.866672+00:00')
    manifest=json.loads((out/'manifest.json').read_text())
    check(manifest['status']=='EXECUTED_NOT_ACCEPTED' and manifest['candidate_id']=='S2_K1' and manifest['k']==1,'FREEZE_IDENTITY')
    check(all(manifest[k] is False for k in ('target_outcomes_opened','market_joined','wager_or_execution_joined','protected_2025_test_opened','fit_or_optimization_performed')),'FREEZE_FORBIDDEN_JOIN')
    check(set(manifest['hashes'])=={'s2_k1_predictions.csv','s2_k1_side_exclusions.csv','s2_k1_game_exclusions.csv'},'OUTPUT_FILE_UNION')
    for name,digest in manifest['hashes'].items():check(sha((out/name).read_bytes())==digest,'OUTPUT_BYTE_HASH')
    check(manifest['projection']==context and manifest['input_sha256']==inputs['input_sha256'] and manifest['input_acceptance_records']==inputs['acceptance_records'],'FROZEN_INPUT_BINDINGS')
    check(manifest['raw_source_sha256']==inputs['raw_source_sha256'] and manifest['input_gate_sha256']==inputs['input_gate_sha256'],'RAW_OR_GATE_BINDING')
    consumer=(ROOT/'scripts/cfb_qa_prospective_s2_k1_consumer_v1_2026_09_30.py').read_bytes()
    check(manifest['consumer_sha256']==sha(consumer) and manifest['consumer_git_blob']==blob(consumer),'CONSUMER_BINDING')
    legacy=(ROOT/'scripts/cfb_qa_sandbox_candidate_generator_2026_09_27.py').read_bytes()
    check(blob(legacy)=='40447984a58dbc530cbe942bc1176f0c5bcbe9b2','FROZEN_TRANSFORM_ANCESTRY')
    tree=ast.parse(legacy);constants={n.targets[0].id:ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id in ('FEATURES','MAP')}
    fs,mp=constants['FEATURES'],constants['MAP'];config=manifest['frozen_config']
    check(config['features']==fs and config['mapping']==mp and config['context_sign']=='SUBTRACT_MEAN_PAIRED_RESIDUAL' and config['lambdas']=={'margin':.1,'total':.1,'win':.01} and config['candidate_id']=='S2_K1' and config['k']==1,'FROZEN_CONFIG_SEMANTICS')
    cfgsha=sha(json.dumps(config,sort_keys=True,separators=(',',':')).encode());check(cfgsha==manifest['frozen_config_sha256'],'FROZEN_CONFIG_HASH')
    check(sha((fit/'selected_coefficients.csv').read_bytes())==COEF_SHA and sha((fit/'train_scaling.csv').read_bytes())==SCALE_SHA,'FROZEN_PARAMETERS')
    check(manifest['coefficient_sha256']==COEF_SHA and manifest['scaling_sha256']==SCALE_SHA and config['coefficient_sha256']==COEF_SHA and config['scaling_sha256']==SCALE_SHA,'PARAMETER_DECLARATION')
    coef=pd.read_csv(fit/'selected_coefficients.csv');scale=pd.read_csv(fit/'train_scaling.csv').set_index('feature')
    S,G,B,C,P0=(frames[k] for k in ('side','target','baseline','context','predicted'))
    baseline=B.set_index(['game_id','team']);side_features={};invalid=set();eligible=set(P0.game_id)
    for row in S.itertuples():
        key=(row.game_id,row.team)
        if row.game_id not in eligible or int(row.qualified_prior_games)<=0:invalid.add(key);continue
        n=float(row.qualified_prior_games);values={}
        for feature in fs:
            raw=float(getattr(row,feature));b=float(baseline.loc[key,'baseline__'+feature])
            if not np.isfinite(raw) or not np.isfinite(b):invalid.add(key);break
            value=n/(n+1)*raw+b/(n+1)
            if feature in mp:
                z=C[(C.target_game_id==row.game_id)&(C.target_team==row.team)]
                z=z[z['context_valid__'+feature].map(lambda v:str(v).lower() in ('true','1'))]
                if z.empty:invalid.add(key);break
                no=z.opponent_qualified_prior_games.to_numpy(float);ro=z['raw__'+mp[feature]].to_numpy(float);bo=z['baseline__'+mp[feature]].to_numpy(float)
                residual=np.zeros(len(z));positive=no>0
                residual[positive]=(ro[positive]-bo[positive])*no[positive]/(no[positive]+1)
                if not np.isfinite(residual).all():invalid.add(key);break
                value-=float(np.mean(residual))
            values[feature]=value
        if key not in invalid:side_features[key]=values
    expected_ids={r.game_id for r in G.itertuples() if (r.game_id,r.home_team) in side_features and (r.game_id,r.away_team) in side_features}
    P=pd.read_csv(out/'s2_k1_predictions.csv',dtype={'game_id':str});E=pd.read_csv(out/'s2_k1_side_exclusions.csv',dtype={'game_id':str});GE=pd.read_csv(out/'s2_k1_game_exclusions.csv',dtype={'game_id':str})
    check(not P.game_id.duplicated().any() and set(P.game_id)==expected_ids,'PREDICTION_ELIGIBILITY_UNION')
    check(not E.duplicated(['game_id','team']).any() and set(zip(E.game_id,E.team))==invalid and E.reason.notna().all() and len(GE)==0,'EXCLUSION_ACCOUNTING')
    check(set(P.game_id)|set(E.game_id)==set(G.game_id),'FULL_FROZEN_POPULATION')
    check((len(P),len(E),len(GE))==(manifest['prediction_rows'],manifest['side_exclusion_rows'],manifest['game_exclusion_rows']),'OUTPUT_ROW_COUNTS')
    _,acceptance=immutable_ref(ref);start=clock(manifest['freeze_recorded_at_utc']);end=clock(manifest['prediction_completed_at_utc']);now=clock(as_of)
    check(clock(acceptance['accepted_at_utc'])<=start<=end<=now and all(now<clock(k) for k in context['qualified_kickoffs_utc'].values()),'PRE_EVENT_FREEZE_CLOCKS')
    check(pd.Timestamp(manifest['snapshot_cutoff_utc'])==pd.Timestamp(inputs['cutoff_utc']),'ORIGINAL_CUTOFF')
    controls=P0.set_index('game_id');targets=G.set_index('game_id');side=S.set_index(['game_id','team']);maxdiff=0.
    for row in P.itertuples():
        gid=row.game_id;g=targets.loc[gid];h=side.loc[(gid,g.home_team)];a=side.loc[(gid,g.away_team)]
        check(row.season==2026 and row.candidate_id=='S2_K1' and row.k==1 and row.snapshot_type=='REFRESH_SNAPSHOT','ROW_IDENTITY')
        check((row.home_team,row.away_team,row.start_date)==(g.home_team,g.away_team,g.start_date),'ORIGINAL_TARGET_FIELDS_RETIMED')
        check(pd.Timestamp(row.snapshot_cutoff_utc)==pd.Timestamp(inputs['cutoff_utc']) and row.qualified_kickoff_utc==context['qualified_kickoffs_utc'][gid],'ROW_CUTOFF_OR_KICKOFF')
        check((row.home_qualified_prior_games,row.away_qualified_prior_games)==(h.qualified_prior_games,a.qualified_prior_games),'ROW_HISTORY_COUNTS')
        depth=min(int(h.qualified_prior_games),int(a.qualified_prior_games));expected_slice='DEPTH_1_2' if depth<=2 else 'DEPTH_3_4' if depth<=4 else 'DEPTH_5_PLUS'
        check(row.history_depth_slice==expected_slice,'HISTORY_SLICE')
        neutral=str(g.neutral_site).lower() in ('true','1');check(row.venue_state==('NEUTRAL' if neutral else 'HOME'),'ORIGINAL_VENUE')
        values={p+f:side_features[(gid,team)][f] for p,team in [('home_',g.home_team),('away_',g.away_team)] for f in fs}
        names=['intercept']+list(values)+['venue_neutral']
        vector=np.array([1.]+[(values[name]-scale.loc[name,'mean'])/scale.loc[name,'sd'] for name in values]+[float(neutral)])
        for target in ('margin','total','win'):
            c=coef[coef.target==target].set_index('term').coefficient
            check(set(c.index)==set(names),'COEFFICIENT_TERM_UNION')
            expected=float(sum(float(v)*float(c.loc[n]) for n,v in zip(names,vector)))
            if target=='win':expected=float(1/(1+np.exp(-np.clip(expected,-40,40))))
            got=float(getattr(row,'pred_'+target));delta=abs(got-expected);maxdiff=max(maxdiff,delta)
            check(np.isfinite(got) and delta<=1e-12,'INDEPENDENT_PREDICTION_MISMATCH')
            check(abs(float(getattr(row,'s0_pred_'+target))-float(controls.loc[gid,'pred_'+target]))<=1e-12,'S0_CONTROL_CHANGED')
        check(0<=row.pred_win<=1,'WIN_PROBABILITY_RANGE')
        for kind,digest in inputs['input_sha256'].items():check(getattr(row,kind+'_input_sha256')==digest,'ROW_PARENT_BINDING')
        for kind,digest in context['projected_input_sha256'].items():check(getattr(row,kind+'_projected_sha256')==digest,'ROW_PROJECTED_BINDING')
        check(row.projection_sha256==context['projection_sha256'] and row.frozen_config_sha256==cfgsha and row.consumer_sha256==sha(consumer) and row.consumer_git_blob==blob(consumer) and row.input_gate_sha256==inputs['input_gate_sha256'],'ROW_IMPLEMENTATION_BINDING')
        check(row.freeze_recorded_at_utc==manifest['freeze_recorded_at_utc'],'ROW_FREEZE_CLOCK')
        for kind,digest in inputs['raw_source_sha256'].items():check(getattr(row,'raw_'+kind+'_sha256')==digest,'ROW_RAW_SOURCE_BINDING')
    return {'verdict':'PASS_INDEPENDENT_S2_PRE_EVENT_PREDICTION_BYTES_ONLY','audit_observed_at_utc':as_of,'prediction_rows':len(P),'side_exclusions':len(E),'game_exclusions':len(GE),'projected_targets':len(G),'parent_targets':context['parent_targets'],'independent_prediction_fields':3*len(P),'max_absolute_prediction_difference':maxdiff,'freeze_recorded_at_utc':manifest['freeze_recorded_at_utc'],'prediction_completed_at_utc':manifest['prediction_completed_at_utc'],'earliest_qualified_kickoff_utc':min(context['qualified_kickoffs_utc'].values()),'manifest_sha256':sha((out/'manifest.json').read_bytes()),'output_sha256':manifest['hashes'],'projection_acceptance_ref':ref,'production_effect':'NONE','outcomes_opened':False,'scoring_authorized':False,'durable_remote_freeze':'NOT_CERTIFIED_BY_LOCAL_AUDIT'}


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('package','fit','out','acceptance_ref','output'):p.add_argument('--'+name.replace('_','-'),type=Path,required=True)
    a=p.parse_args();r=audit(a.package,a.fit,a.out,json.loads(a.acceptance_ref.read_text()),datetime.now(timezone.utc).isoformat());a.output.write_text(json.dumps(r,indent=2,sort_keys=True)+'\n');print(json.dumps(r,indent=2))
