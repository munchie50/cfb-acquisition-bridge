import ast, hashlib, json, pathlib, zipfile
import pandas as pd, numpy as np, pyreadr
root=pathlib.Path('audit'); sha=lambda p:hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
cut=pd.Timestamp('2026-09-29T11:39:08.824054+00:00')
V=pathlib.Path('recovered/scripts/cfb_qa_s2_k1_source_context_companion_v4_2026_09_29.py').read_text()
A=pathlib.Path('recovered/scripts/phase4_challenger_b_2026_refresh_predict_v1_246.py').read_text()
H=pathlib.Path('recovered/scripts/phase4_challenger_b_corrected_features_v1_172.py').read_text()
G=pathlib.Path('recovered/scripts/cfb_qa_sandbox_candidate_generator_2026_09_27.py').read_text()
assert hashlib.sha256(V.encode()).hexdigest()=='8500b5365ccc374105156106501f2335be80de4bde7d97bb82fe3c47cc92c1f0'
def block(s):
 a=s.index('BASE2017=');m='R=R[R.home_canonical.isin(m)|R.away_canonical.isin(m)].copy()';return s[a:s.index(m,a)+len(m)]
assert block(V)==block(A)
def assignment(s,name):
 for n in ast.walk(ast.parse(s)):
  if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id==name for t in n.targets):return ast.literal_eval(n.value)
MAP=assignment(V,'MAP');COMP=assignment(V,'COMP')
assert MAP==assignment(G,'MAP') and COMP==assignment(G,'COMPONENTS')
M=pd.read_csv(root/'v4/mechanical_primitives.csv',dtype={'game_id':str});D=pd.read_csv(root/'v4/derived_primitives.csv',dtype={'game_id':str});C=pd.read_csv(root/'v4/source_context.csv',dtype={'target_game_id':str,'source_game_id':str});T=pd.read_csv(root/'s0/challenger_b_2026_refresh_team_side_substrate_v1_246.csv',dtype={'game_id':str});S=pd.read_csv(root/'raw/challenger_b_2026_future_target_projection_v1_217.csv',dtype={'game_id':str})
man=json.loads((root/'v4/manifest.json').read_text())
assert man=={'accepted_target_side_crosscheck':True,'hashes':{p.name:sha(p) for p in (root/'v4').glob('*.csv')},'market_joined':False,'primitive_ancestry_blob':'37c05aba201d3c2935b5d2b646437552949766fd','rows':{'context':4355,'derived':662,'mechanical':662},'s2_predictions_produced':False,'status':'EXECUTED_NOT_ACCEPTED','target_outcomes_joined':False}
assert [len(C),len(M),len(D),len(T),len(S)]==[4355,662,662,1114,557]
for x in (M,D):
 x['start_date']=pd.to_datetime(x.start_date,utc=True)
 assert set(x.season)=={2026} and (x.start_date<cut).all()
 assert not x.duplicated(['game_id','team']).any() and not x.duplicated(['team','start_date']).any()
 assert not set(x.game_id)&set(T.game_id)
for x,col in ((T,'target_kickoff'),(S,'start_date'),(C,'target_kickoff'),(C,'source_kickoff')):x[col]=pd.to_datetime(x[col],utc=True)
assert (T.target_kickoff>cut).all() and (C.source_kickoff<C.target_kickoff).all()
assert not C.duplicated(['target_game_id','target_team','source_game_id']).any()
for x in (M,D,C,T):
 assert not any(any(t in c.lower() for t in ['market','spread','odds','wager','moneyline','over_under','execution','prediction','target_outcome','postgame']) for c in x.columns)
assert set(C.snapshot_type)=={'S2_K1_SOURCE_CONTEXT'} and set(C.snapshot_cutoff_utc)=={cut.isoformat()}
assert set(T.snapshot_type)=={'REFRESH_SNAPSHOT'} and set(T.snapshot_cutoff_utc)=={cut.isoformat()}
assert np.isfinite(T.qualified_prior_games).all() and (T.qualified_prior_games>=0).all() and (T.qualified_prior_games%1==0).all()
assert np.isfinite(C.opponent_qualified_prior_games).all() and (C.opponent_qualified_prior_games>=0).all() and (C.opponent_qualified_prior_games%1==0).all()
# Rebuild the population with the exact accepted membership filter, preserving original identities.
R=pd.read_parquet(root/'raw/cfb_schedules_2026.parquet');R['game_id']=R.game_id.astype(str).str.replace(r'\.0$','',regex=True);R['start_date']=pd.to_datetime(R.start_date,utc=True)
ns={'R':R};exec(block(A),ns);R=ns['R'];R=R[R.start_date<cut].copy()
assert set(M.game_id)==set(R.game_id) and len(M)==2*len(R)
for r in M.itertuples():assert r.team in (r.home_team,r.away_team)
# Recover the actual v1.172 primitive producer with schedule-filtered PBP.
P=next(iter(pyreadr.read_r(root/'raw/pbp_2026.rds').values()));P['game_id']=P.game_id.astype(str).str.replace(r'\.0$','',regex=True)
p=P[P.game_id.isin(set(R.game_id))].copy()
ns={'pd':pd,'np':np,'p':p,'s':R,'missing_ids':set(R.game_id)-set(P.game_id),'mech_parts':[],'der_parts':[],'one':lambda s:s.fillna(0).eq(1)}
begin=H.index(' p["pos_team"]');end=H.index('mraw=pd.concat')
src='\n'.join(l[1:] if l.startswith(' ') else l for l in H[begin:end].splitlines())
exec(src,ns)
key=['game_id','team'];mr=['off_plays','off_yards','rush_plays','pass_plays','rush_yards','pass_yards','pass_attempts','interceptions','def_plays','def_yards'];dr=['off_scr','off_exp','off_succ_q','off_succ','def_scr','def_exp','def_succ_q','def_succ','start_ytg_sum','start_drive_n']
for actual,rebuilt,cols,flag in [(M,ns['mech_parts'][0],mr,'mechanical_primitive_complete'),(D,ns['der_parts'][0],dr,'derived_primitive_complete')]:
 cols=cols+['game_points_for','game_points_against','pbp_game_present',flag]
 pd.testing.assert_frame_equal(actual.set_index(key)[cols].sort_index(),rebuilt.set_index(key)[cols].sort_index(),check_dtype=False,rtol=0,atol=0)
# Every accepted target-side is counted, including zero-history rows with no context rows.
cg=C.groupby(['target_game_id','target_team']).size();sg=S.set_index('game_id')
for r in T.itertuples():
 g=sg.loc[r.game_id];assert r.team==g[r.side+'_team'] and r.target_kickoff==g.start_date
 prior=M[(M.team==r.team)&(M.start_date<r.target_kickoff)&(M.start_date<cut)]
 assert len(prior)==r.qualified_prior_games==cg.get((r.game_id,r.team),0)
 got=C[(C.target_game_id==r.game_id)&(C.target_team==r.team)]
 assert set(got.source_game_id)==set(prior.game_id)
 assert set(got.target_side).issubset({r.side})
# Independently calculate source-opponent histories and normalized pooled baselines.
mi=M.set_index(key);di=D.set_index(key);cache={};baseline_cache={}
for r in C.itertuples():
 a=mi.loc[(r.source_game_id,r.target_team)];o=mi.loc[(r.source_game_id,r.source_opponent)]
 assert r.source_opponent==(a.away_team if r.target_team==a.home_team else a.home_team)
 assert o.start_date==r.source_kickoff==a.start_date and r.source_opponent!=r.target_team
 ck=(r.source_game_id,r.source_opponent)
 if ck not in cache:
  pm=M[(M.team==r.source_opponent)&(M.start_date<r.source_kickoff)];pdv=D[(D.team==r.source_opponent)&(D.start_date<r.source_kickoff)]
  cache[ck]=(pm,pdv)
 pm,pdv=cache[ck];q=len(pm)
 mc=bool((pm.pbp_game_present&pm.mechanical_primitive_complete).all());dc=bool((pdv.pbp_game_present&pdv.derived_primitive_complete).all())
 assert q==r.opponent_qualified_prior_games and mc==r.mechanical_history_complete and dc==r.derived_history_complete
 for f,pair in MAP.items():
  typ,num,den=COMP[pair];hist=pm if typ=='M' else pdv;full=M if typ=='M' else D;flag='mechanical_primitive_complete' if typ=='M' else 'derived_primitive_complete'
  rawden=q if den=='GAME' else hist[den].fillna(0).sum();raw=hist[num].fillna(0).sum()/rawden if rawden else np.nan
  if pair not in ['points_for_per_game','points_against_per_game'] and not (mc if typ=='M' else dc):raw=np.nan
  bkey=(pair,r.source_kickoff.normalize())
  if bkey not in baseline_cache:
   pop=full[(full.start_date<r.source_kickoff.normalize())&full[flag]];bd=len(pop) if den=='GAME' else pop[den].sum();bn=pop[num].sum()
   baseline_cache[bkey]=bn/bd if len(pop) and bd>0 and np.isfinite(bn) and np.isfinite(bd) else np.nan
  b=baseline_cache[bkey]
  assert np.isclose(getattr(r,'baseline__'+pair),b,rtol=0,atol=1e-12,equal_nan=True)
  assert np.isclose(getattr(r,'raw__'+pair),raw,rtol=0,atol=1e-12,equal_nan=True)
  valid=bool(np.isfinite(b) and (q==0 or (mc and dc and np.isfinite(raw))))
  assert getattr(r,'context_valid__'+f)==valid
report={'status':'INDEPENDENT_RECONCILIATION_PASS','cutoff':cut.isoformat(),'rows':man['rows'],'target_sides_checked':len(T),'zero_history_target_sides':int((T.qualified_prior_games==0).sum()),'zero_history_opponent_context_rows':int((C.opponent_qualified_prior_games==0).sum()),'incomplete_mechanical_context_rows':int((~C.mechanical_history_complete).sum()),'incomplete_derived_context_rows':int((~C.derived_history_complete).sum()),'baseline_values_checked':len(C)*len(MAP),'raw_values_checked':len(C)*len(MAP),'context_flags_checked':len(C)*len(MAP),'primitive_reproduction':'actual v1.172 builder, schedule-filtered PBP, exact numeric agreement','source_scores':'strict-prior source only; unused winner/rank metadata retained, not candidate inputs','hashes':man['hashes']}
(root/'reconciliation.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
