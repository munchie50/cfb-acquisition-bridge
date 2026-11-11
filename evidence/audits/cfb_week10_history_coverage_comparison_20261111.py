import csv, io, json, zipfile, hashlib, statistics
from pathlib import Path
from datetime import datetime, timezone
from decimal import Decimal

import argparse
a=argparse.ArgumentParser()
a.add_argument('--repository-root',type=Path,required=True)
a.add_argument('--archive-directory',type=Path,required=True)
a.add_argument('--output',type=Path,required=True)
args=a.parse_args()
root=args.repository_root
base=args.archive_directory
specs=[('original','artifact0.zip','772b8683365ebf62d35fc3813beb138688b84af4172a0b261fd9218691d5adcf'),('refresh','artifact2.zip','98e6af5534b233f3284b6178fe410a1fffcb80420e0da3dae8b1c92a13c52567')]
sources={}; data={}
for label,filename,digest in specs:
    raw=(base/filename).read_bytes(); assert hashlib.sha256(raw).hexdigest()==digest
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        manifest_name=next(n for n in z.namelist() if n.endswith('manifest_v1_206.json') or n.endswith('s0/manifest_v1_246.json'))
        manifest=json.loads(z.read(manifest_name)); prefix=manifest_name.rsplit('/',1)[0]+'/' if '/' in manifest_name else ''
        for name,sha in manifest['hashes'].items(): assert hashlib.sha256(z.read(prefix+name)).hexdigest()==sha
        def read(kind):
            name=next(n for n in manifest['hashes'] if kind in n)
            return list(csv.DictReader(io.StringIO(z.read(prefix+name).decode())))
        data[label]={'cutoff':datetime.fromisoformat(manifest['cutoff_utc']), 'features':{(r['game_id'],r['side']):r for r in read('feature_eligibility')},'chronology':{(r['game_id'],r['side']):r for r in read('chronology_audit')}}
        sources[label]={'archive_sha256':digest,'manifest_sha256':hashlib.sha256(z.read(manifest_name)).hexdigest(),'cutoff':manifest['cutoff_utc'],'manifest_hashes_verified':len(manifest['hashes'])}
paired_path=root/'evidence/audits/CFB_WEEK10_ORIGINAL_REFRESH_PAIRED_QA_20261108T165731Z.json'
paired=json.loads(paired_path.read_text()); rows=[]
for prior in paired['rows']:
    if prior['original'] is None: continue
    row={k:prior[k] for k in ['game_id','away_team','home_team']}; row['inputs']={}
    for label,ds in data.items():
        sides={}
        for side in ['home','away']:
            f=ds['features'][row['game_id'],side]; c=ds['chronology'][row['game_id'],side]
            assert f['team']==c['team']==row[side+'_team'] and int(f['qualified_prior_games'])==int(c['prior_games'])
            target=datetime.fromisoformat(f['target_kickoff']); last=datetime.fromisoformat(c['max_prior_kickoff'])
            assert last<ds['cutoff']<target and c['strict_chronology']=='True' and c['own_game_excluded']=='True'
            rest=(target-last).total_seconds()/86400; assert abs(rest-float(f['rest_days']))<1e-10
            sides[side]={'prior_games':int(f['qualified_prior_games']),'days_since_last_qualified_prior':rest,'days_cutoff_to_target':(target-ds['cutoff']).total_seconds()/86400,'target_kickoff':f['target_kickoff']}
        row['inputs'][label]=sides
    row['errors']={'original':prior['original'],'refresh':prior['accepted_refresh']}
    row['minimum_original_prior_games']=min(s['prior_games'] for s in row['inputs']['original'].values())
    rows.append(row)
assert len(rows)==len({r['game_id'] for r in rows})==55
def summary(rs):
    out={'games':len(rs)}
    for label in data:
        sides=[s for r in rs for s in r['inputs'][label].values()]
        out[label]={}
        for key in ['prior_games','days_since_last_qualified_prior','days_cutoff_to_target']:
            values=[s[key] for s in sides];out[label][key]={'min':min(values),'median':statistics.median(values),'max':max(values)}
        for key in ['margin_abs','total_abs','brier']:
            out[label][key+'_mean']=str(sum(Decimal(r['errors'][label][key]) for r in rs)/len(rs))
    return out
out={'schema':'CFB_WEEK10_HISTORY_COVERAGE_DESCRIPTIVE_V1','recorded_at':datetime.now(timezone.utc).isoformat(),'authority_head':'6a15ace6e513f07e027ba185830bc38096f35b67','scope':'Postgame exploratory descriptive comparison of the same55 ORIGINAL-modeled games; not preregistered, causal, training, model selection or betting evidence. All8 original exclusions remain outside the matched cohort.','sources':sources,'paired_evidence_sha256':hashlib.sha256(paired_path.read_bytes()).hexdigest(),'all55':summary(rows),'coverage_groups':{label:summary(rs) for label,rs in [('minimum_original_priors_below3',[r for r in rows if r['minimum_original_prior_games']<3]),('minimum_original_priors_at_least3',[r for r in rows if r['minimum_original_prior_games']>=3])] if rs},'rows':rows,'limits':['Same single week, narrow original lead-time range; cannot isolate a lead-time effect.','Refresh jointly changes history, all derived features and source schedule; cannot attribute gains to sample size or rest alone.','Exploratory strata selected after outcomes were known; no held-out confirmation or causal significance claim.','No original prediction substitution, threshold tuning, scientific promotion or model/routine/task/wager/money mutation.'],'next':'Before any held-out comparison, predeclare independent temporal/coverage cohorts and metrics under existing protected-split authority; this single-week descriptive result cannot justify a model change.'}
args.output.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['all55','coverage_groups']},indent=2))
