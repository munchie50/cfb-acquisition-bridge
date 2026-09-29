exec(open('audit/reconcile.py').read().split('# Independently calculate source-opponent histories')[0])
checks=0
for r in T[T.eligible].itertuples():
 pm=M[(M.team==r.team)&(M.start_date<r.target_kickoff)];pdv=D[(D.team==r.team)&(D.start_date<r.target_kickoff)];n=len(pm)
 assert n>0 and (pm.pbp_game_present&pm.mechanical_primitive_complete).all() and (pdv.pbp_game_present&pdv.derived_primitive_complete).all()
 for f,(typ,num,den) in COMP.items():
  h=pm if typ=='M' else pdv;d=n if den=='GAME' else h[den].sum();v=h[num].sum()/d
  assert np.isclose(getattr(r,f),v,rtol=0,atol=1e-12);checks+=1
 rest=(r.target_kickoff-pm.start_date.max()).total_seconds()/86400
 assert np.isclose(r.rest_days,rest,rtol=0,atol=1e-12);checks+=1
assert T.groupby('game_id').eligible.all().sum()==551
assert (~T.groupby('game_id').eligible.all()).sum()==6
print(json.dumps({'eligible_side_feature_values_reproduced':checks,'eligible_sides':int(T.eligible.sum()),'eligible_games':551,'excluded_games':6}))
