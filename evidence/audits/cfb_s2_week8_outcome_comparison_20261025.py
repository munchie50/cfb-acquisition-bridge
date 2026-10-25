#!/usr/bin/env python3
"""Score one authorized immutable 44-game S2/S0 cohort; no construction/fit."""
import argparse
import csv
import hashlib
import io
import json
import math
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from cfb_completed_weeks4_8_baseline_replay_20261025 import blob, pair, finals, SCORECARD

FREEZE = ROOT/'evidence/qa_s2_freezes/CFB_S2_WEEK8_20261024T032159Z'
ACCEPTANCE = '6b0d6b0983fec9c2d9ccb217413639a643409b57'
AUTHORITY_PATH = 'evidence/run_receipts/CFB_S2_WEEK8_BOUNDED_SCORING_20261025T163928Z_AUTHORITY_AND_RUN_STARTED.md'
AUTHORITY = '20ff2cf2d68347bdb0281d306f62737ee16e24b5'
DEPTHS = ('DEPTH_1_2', 'DEPTH_3_4', 'DEPTH_5_PLUS')


def clock(value):
    d = datetime.fromisoformat(value.replace('Z','+00:00'))
    if d.tzinfo is None:
        raise ValueError('clock must be aware')
    return d


def outcomes(text, frozen_rows):
    modeled = finals(text, 8)
    # Original-exclusion finals are outcome context only for the production
    # model, but are valid outcomes for this separately eligible REFRESH study.
    excluded = {}
    for gid, away, a, home, h in re.findall(r'^- `(\d+)` (.*?) (\d+), (.*?) (\d+) — original `', text, re.M):
        if gid in excluded:
            raise ValueError('duplicate context final')
        excluded[gid] = {'away_team':away, 'home_team':home, 'final_away':int(a), 'final_home':int(h)}
    joined = []
    for row in frozen_rows:
        key = pair(row['away_team'], row['home_team'])
        result = modeled.get(key)
        if result is not None and result['game_id'] != row['game_id']:
            raise ValueError('modeled final ID mismatch')
        if result is None:
            result = excluded.get(row['game_id'])
            if result is None or pair(result['away_team'],result['home_team']) != key:
                raise ValueError('missing or identity-conflicted final')
        if result['final_away'] == result['final_home']:
            raise ValueError('unexpected final tie')
        joined.append({**row, 'final_away':result['final_away'], 'final_home':result['final_home'],
                       'original_exclusion_context_used':row['game_id'] in excluded})
    return joined


def validate_rows(rows, manifest):
    ids = [r['game_id'] for r in rows]
    if len(rows) != 44 or len(set(ids)) != 44 or set(ids) != set(manifest['projection']['qualified_kickoffs_utc']):
        raise ValueError('exact common 44-game cohort required')
    for r in rows:
        minimum = min(int(r['home_qualified_prior_games']), int(r['away_qualified_prior_games']))
        depth = 'DEPTH_1_2' if 1<=minimum<=2 else 'DEPTH_3_4' if 3<=minimum<=4 else 'DEPTH_5_PLUS' if minimum>=5 else None
        if r['candidate_id']!='S2_K1' or r['k']!='1' or r['history_depth_slice']!=depth:
            raise ValueError('frozen candidate/history slice mismatch')
        if r['snapshot_cutoff_utc']!='2026-10-13T15:13:13.866672+00:00' or r['snapshot_type']!='REFRESH_SNAPSHOT':
            raise ValueError('wrong control/source boundary')
        if r['qualified_kickoff_utc']!=manifest['projection']['qualified_kickoffs_utc'][r['game_id']] or clock(r['freeze_recorded_at_utc'])>=clock(r['qualified_kickoff_utc']):
            raise ValueError('not frozen before qualified kickoff')
        for prefix in ('','s0_'):
            for field in ('margin','total','win'):
                value=float(r[prefix+'pred_'+field])
                if not math.isfinite(value) or (field=='win' and not 0<=value<=1):
                    raise ValueError('invalid frozen value')


def losses(row, prefix):
    pm, pt, pw = [float(row[prefix+'pred_'+k]) for k in ('margin','total','win')]
    am, total = row['final_home']-row['final_away'], row['final_home']+row['final_away']
    outcome = int(am>0)
    assigned = pw if outcome else 1-pw
    return {'margin_error':am-pm,'total_error':total-pt,'brier':(pw-outcome)**2,
            'log_loss':-math.log(assigned) if assigned>0 else math.inf,
            'margin_direction_correct':int((pm>0)==(am>0)),
            'probability_classifier_correct':int((pw>.5)==(am>0))}


def aggregate(rows):
    result = {'n':len(rows)}
    if not rows:
        return {**result,'S0':None,'S2_K1':None,'S2_minus_S0':None}
    for label, prefix in (('S0','s0_'),('S2_K1','')):
        ls = [losses(r,prefix) for r in rows];n=len(ls)
        mean=lambda key:math.fsum(r[key] for r in ls)/n
        m={}
        for family in ('margin','total'):
            key=family+'_error'
            m[family+'_mae']=math.fsum(abs(r[key]) for r in ls)/n
            m[family+'_rmse']=math.sqrt(math.fsum(r[key]**2 for r in ls)/n)
            m[family+'_bias']=mean(key)
        m.update(win_brier=mean('brier'),win_log_loss=mean('log_loss'),
                 margin_direction_correct=sum(r['margin_direction_correct'] for r in ls),
                 probability_classifier_correct=sum(r['probability_classifier_correct'] for r in ls))
        if math.isinf(m['win_log_loss']):m['win_log_loss']='INFINITE'
        result[label]=m
    result['S2_minus_S0']={k:result['S2_K1'][k]-v if isinstance(v,(float,int)) and isinstance(result['S2_K1'][k],(float,int)) else 'BOUNDARY_INFINITY' for k,v in result['S0'].items()}
    return result


def compare(rows):
    groups={'ALL_COMMON_GAMES':rows}
    groups.update({depth:[r for r in rows if r['history_depth_slice']==depth] for depth in DEPTHS})
    for key, threshold in (('margin',7),('total',7),('win',.10)):
        groups['DISAGREEMENT_'+key.upper()]=[r for r in rows if abs(float(r['pred_'+key])-float(r['s0_pred_'+key]))>=threshold]
    return {k:aggregate(v) for k,v in groups.items()}


def build(scorecard, authority):
    if blob(Path(authority).read_text())!=AUTHORITY:
        raise ValueError('separate bounded scoring authority not authenticated')
    acceptance=(FREEZE/'INDEPENDENT_FREEZE_ACCEPTANCE.json').read_text()
    if blob(acceptance)!=ACCEPTANCE:raise ValueError('unqualified freeze acceptance')
    a=json.loads(acceptance)
    for ref in a['output_refs']:
        raw=(ROOT/ref['path']).read_bytes()
        if hashlib.sha256(raw).hexdigest()!=ref['sha256'] or blob(raw.decode())!=ref['blob']:
            raise ValueError('immutable frozen output differs')
        if clock(ref['committed_at_utc'])>=clock(a['independent_verification']['earliest_qualified_kickoff_utc']):
            raise ValueError('output not durably pre-event')
    manifest=json.loads((FREEZE/'manifest.json').read_text())
    rows=list(csv.DictReader(io.StringIO((FREEZE/'s2_k1_predictions.csv').read_text())))
    validate_rows(rows,manifest)
    text=Path(scorecard).read_text()
    if blob(text)!=SCORECARD:raise ValueError('unqualified outcome source')
    joined=outcomes(text,rows)
    for row in joined:
        row['S0_loss']=losses(row,'s0_');row['S2_K1_loss']=losses(row,'')
        for loss in (row['S0_loss'],row['S2_K1_loss']):
            if math.isinf(loss['log_loss']):loss['log_loss']='INFINITE'
    return {'status':'PASS_BOUNDED_S2_WEEK8_COMMON_GAME_OUTCOME_COMPARISON',
            'scope':'ONE_PROSPECTIVE_COHORT_DESCRIPTIVE_ONLY_NOT_SCIENTIFIC_ACCEPTANCE_OR_PROMOTION',
            'authority':{'path':AUTHORITY_PATH,'blob':AUTHORITY},'freeze_acceptance_blob':ACCEPTANCE,
            'scorecard_blob':SCORECARD,'snapshot_cutoff_utc':manifest['snapshot_cutoff_utc'],
            'control':'EXACT_OCT13_S0_REFRESH_SAME44_NOT_ORIGINAL_FIRST_FROZEN',
            'week':8,'groups':compare(joined),'rows':joined,
            'original_exclusions_still_excluded_in_production':True,
            'disposition':'CONTINUE_IN_QA_OBSERVE_NO_AUTOMATIC_ACCEPTANCE_OR_PROMOTION',
            'market_or_wager_joined':False,'protected_2025_test_opened':False,'production_effect':'NONE'}


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for k in ('scorecard','authority','output'):p.add_argument('--'+k,type=Path,required=True)
    a=p.parse_args()
    if a.output.resolve() in (a.scorecard.resolve(),a.authority.resolve()):p.error('distinct output required')
    result=build(a.scorecard,a.authority)
    a.output.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(result['groups'],indent=2,allow_nan=False))
