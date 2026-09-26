import pandas as pd, json, hashlib, os, sys
K=['season','game_id','team']
m=pd.read_csv('v109/phase4_feature_canary_v1_109.csv',dtype={'game_id':str})
d=pd.read_csv('v115/phase4_derived_feature_canary_v1_115.csv',dtype={'game_id':str})
s=pd.read_csv('evidence/phase4_qualified_schedule_2016_2024.csv',dtype={'game_id':str})
if m.duplicated(K).any() or d.duplicated(K).any(): raise SystemExit('duplicate feature key')
x=m.merge(d,on=K,validate='one_to_one',suffixes=('_m','_d'))
# accepted feature names; common metadata removed
features=['points_for_per_game','points_against_per_game','offensive_scrimmage_plays_per_game','defensive_scrimmage_plays_per_game','offensive_yards_per_play','defensive_yards_per_play','rush_play_rate','pass_play_rate','rush_yards_per_play','pass_yards_per_play','interception_rate','rest_days','offensive_explosive_play_rate','defensive_explosive_play_rate','offensive_success_rate','defensive_success_rate_allowed','average_starting_yards_to_goal']
# normalize merged names where needed
for f in features:
    if f not in x.columns:
        hits=[c for c in x.columns if c.startswith(f+'_')]
        if len(hits)==1: x[f]=x[hits[0]]
        else: raise SystemExit('missing/ambiguous feature '+f)
# authoritative schedule invariants
req=['season','game_id','start_date','home_team','away_team','home_points','away_points','neutral_site']
if any(c not in s.columns for c in req): raise SystemExit('schedule missing required column')
if s.duplicated(['season','game_id']).any(): raise SystemExit('duplicate schedule game')
if (s.season==2025).any(): raise SystemExit('2025 present in development schedule')
# temporal exclusions v1.128
excluded=set('401403894 401403903 401403911 401403920 401403927 401403935 401403940 401426613 401403957 401403899 401403906 401403914 401403919 401403922 401403944 401403956 401411122 401411129 401411132 401411141 401411147 401411157 401411160 401411168 401403959 401426564 401403912 401403925 401403929 401403938 401403941 401403953 401403962 401404001 401404007 401404009 401404013 401404019 401404031 401404037 401404042 401404051'.split())
if len(excluded)!=42: raise SystemExit('temporal exclusion cardinality')
rows=[]; ledger=[]
for _,g in s.sort_values(['season','start_date','game_id']).iterrows():
    key=(g.season,g.game_id)
    h=x[(x.season==g.season)&(x.game_id==g.game_id)&(x.team==g.home_team)]
    a=x[(x.season==g.season)&(x.game_id==g.game_id)&(x.team==g.away_team)]
    reasons=[]
    if g.game_id in excluded: reasons.append('v1.128_temporal_exclusion')
    if len(h)!=1: reasons.append('home_feature_identity')
    if len(a)!=1: reasons.append('away_feature_identity')
    if len(h)==1 and h[features].isna().any(axis=None): reasons.append('home_required_feature_na')
    if len(a)==1 and a[features].isna().any(axis=None): reasons.append('away_required_feature_na')
    if pd.isna(g.home_points) or pd.isna(g.away_points): reasons.append('target_missing')
    if pd.isna(g.neutral_site): reasons.append('venue_missing')
    if reasons:
        ledger.append({'season':g.season,'game_id':g.game_id,'home_team':g.home_team,'away_team':g.away_team,'reasons':'|'.join(sorted(set(reasons)))})
        continue
    rec={'season':int(g.season),'game_id':g.game_id,'start_date':g.start_date,'home_team':g.home_team,'away_team':g.away_team,
         'venue_state':'NEUTRAL' if bool(g.neutral_site) else 'HOME',
         'target_home_margin':float(g.home_points)-float(g.away_points),
         'target_total_points':float(g.home_points)+float(g.away_points),
         'target_home_win':int(float(g.home_points)>float(g.away_points))}
    for f in features:
        rec['home_'+f]=h.iloc[0][f]; rec['away_'+f]=a.iloc[0][f]
    rows.append(rec)
out=pd.DataFrame(rows); led=pd.DataFrame(ledger)
pred=[c for c in out.columns if c.startswith('home_') or c.startswith('away_')]
# exclude identity names from predictor audit
pred=[c for c in pred if c not in ['home_team','away_team']]
if len(pred)!=34: raise SystemExit(f'expected 34 numeric predictors, got {len(pred)}')
if out[pred].isna().any(axis=None): raise SystemExit('NA in eligible predictor matrix')
if (out.season==2025).any(): raise SystemExit('2025 leaked')
badwords=('spread','moneyline','market','consensus','clv','wager','closing','odds','favorite','underdog')
if any(any(w in c.lower() for w in badwords) for c in pred): raise SystemExit('market-like predictor')
if out.duplicated(['season','game_id']).any(): raise SystemExit('duplicate game row')
if (out.target_home_margin==0).any(): raise SystemExit('tied final score found')
out.to_csv('phase4_challenger_a_dataset_v1_131.csv',index=False)
led.to_csv('phase4_challenger_a_exclusion_ledger_v1_131.csv',index=False)
config={'version':'v1.131','authority':['v1.123','v1.124','v1.126','v1.127','v1.128','v1.129','v1.130'],
'features_team_level':features,'numeric_predictors':pred,'categorical_predictor':'venue_state',
'targets':['target_home_margin','target_total_points','target_home_win'],
'partitions':{'TRAIN':[2016,2017,2018,2019,2020,2021,2022],'VALIDATION':[2023,2024],'TEST':[2025],'LIVE_SHADOW':[2026]},
'lambda_grid':[0,0.0001,0.001,0.01,0.1,1,10,100],
'temporal_excluded_unique_games':42}
open('phase4_challenger_a_config_v1_131.json','w').write(json.dumps(config,indent=2,sort_keys=True)+'\n')
def sha(p):
 h=hashlib.sha256()
 with open(p,'rb') as f:
  for z in iter(lambda:f.read(1<<20),b''): h.update(z)
 return h.hexdigest()
manifest={'rows':len(out),'excluded_schedule_games':len(led),'rows_by_season':{str(k):int(v) for k,v in out.groupby('season').size().items()},
'exclusions_by_season':{str(k):int(v) for k,v in led.groupby('season').size().items()},
'temporal_exclusion_games_present_in_ledger':int(led.reasons.str.contains('v1.128_temporal_exclusion',regex=False).sum()),
'predictor_count_numeric':len(pred),'schedule_blob_sha':'e8d96b9135f625a868cc613e124545ac51828e54',
'sha256':{}}
for p in ['phase4_challenger_a_dataset_v1_131.csv','phase4_challenger_a_exclusion_ledger_v1_131.csv','phase4_challenger_a_config_v1_131.json']:
 manifest['sha256'][p]=sha(p)
open('phase4_challenger_a_manifest_v1_131.json','w').write(json.dumps(manifest,indent=2,sort_keys=True)+'\n')
print(json.dumps(manifest,indent=2,sort_keys=True))
