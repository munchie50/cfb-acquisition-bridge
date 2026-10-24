"""Replay exact accepted input features only; no target outcomes or predictions."""
import argparse,ast,hashlib,json,sys
from datetime import datetime,timezone
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'scripts'))
from cfb_qa_s2_k1_input_gate import load_inputs,frozen_interface

p=argparse.ArgumentParser(description=__doc__);p.add_argument('--package-root',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
root=Path(__file__).resolve().parents[2];src=root/'scripts/cfb_qa_prospective_s2_k1_consumer_v1_2026_09_30.py'
raw=src.read_text();tree=ast.parse(raw);fs,mp=frozen_interface()
fn=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='opponent_residuals')
ns={'np':np};exec(compile(ast.Module(body=[fn],type_ignores=[]),str(src),'exec'),ns)
expr=next(n.value for n in ast.walk(tree) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='s2' for t in n.targets) and isinstance(n.value,ast.BinOp))
code=compile(ast.Expression(expr),'actual_prospective_s2_expression','eval')
s=a.package_root/'s0';f,report=load_inputs(s/'challenger_b_2026_refresh_team_side_substrate_v1_246.csv',s/'challenger_b_2026_refresh_target_ledger_v1_246.csv',a.package_root/'baseline/target_baselines.csv',a.package_root/'context/source_context.csv','2026-10-13T15:13:13.866672+00:00')
S=f['side'];B=f['baseline'].set_index(['game_id','team']);C=f['context'];eligible=set(f['predicted'].game_id)
checked=0;changed=0;maxerr=0.;per={k:0 for k in mp}
for r in S[S.game_id.isin(eligible)].itertuples():
 n=float(r.qualified_prior_games);z=C[(C.target_game_id==r.game_id)&(C.target_team==r.team)]
 for feature,pair in mp.items():
  b=float(B.loc[(r.game_id,r.team),'baseline__'+feature]);raw_target=float(getattr(r,feature));s1=n/(n+1)*raw_target+b/(n+1)
  v=z[z['context_valid__'+feature]];no=v.opponent_qualified_prior_games.to_numpy(float);raw_o=v['raw__'+pair].to_numpy(float);base_o=v['baseline__'+pair].to_numpy(float)
  residuals=ns['opponent_residuals'](no,raw_o,base_o)
  actual=eval(code,{'s1':s1,'resid':residuals})
  independent=np.zeros(len(v));positive=no>0;independent[positive]=(raw_o[positive]-base_o[positive])*no[positive]/(no[positive]+1)
  expected=s1-independent.mean();delta=abs(actual-expected);maxerr=max(maxerr,delta)
  if delta>1e-12:raise AssertionError('frozen context mismatch')
  changed+=int(abs((s1+residuals.mean())-expected)>1e-12);checked+=1;per[feature]+=1
report.update(observed_at_utc=datetime.now(timezone.utc).isoformat(),status='PASS_ACCEPTED_INPUT_AND_FROZEN_SIGN_FEATURE_REPLAY_ONLY',candidate_id='S2_K1',k=1,mapped_feature_checks=checked,checks_by_feature=per,prior_plus_sign_differences=changed,max_absolute_independent_difference=maxerr,consumer_git_blob=hashlib.sha1(b'blob '+str(len(raw.encode())).encode()+b'\0'+raw.encode()).hexdigest(),consumer_sha256=hashlib.sha256(raw.encode()).hexdigest(),historical_generator_git_blob='40447984a58dbc530cbe942bc1176f0c5bcbe9b2',full_live_consumer_executed=False,coefficients_opened_by_this_replay=False,predictions_generated=False,freeze_ready=False,next_proof='independent future-only projection/freeze qualification; no elapsed population execution')
a.output.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in report.items() if k not in ('selected_columns','input_sha256','checks_by_feature','acceptance_records')},indent=2))
