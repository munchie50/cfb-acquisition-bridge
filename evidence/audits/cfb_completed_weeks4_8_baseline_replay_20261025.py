#!/usr/bin/env python3
"""Bounded original-only completed-week reconciliation; no model or S2 access.

Reuse accepted Week4/5/7 row evidence, finish Week6, and bind the accepted
Week8 original/final join into one descriptive baseline. Never writes canonical
production state or acquires external data.
"""
import argparse
import hashlib
import json
import math
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
from cfb_week7_first_frozen_projection_gate import archive, FIRST_SHA, CUTOFF

SCORECARD = '1e8e0a9c3cd34c163c32f6782cdfccf30b9e13d8'
SOURCES = {
    4: ('evidence/audits/CFB_COMPLETED_WEEK4_BASELINE_20261025.json', '9519abb4325b455f5f63298be1b6674a90192443'),
    5: ('evidence/audits/CFB_COMPLETED_WEEK5_BASELINE_20261025.json', '15980c694fa75098104fd22f81d400e704db8d98'),
    7: ('evidence/scheduler_qa/CFB_WEEK7_EXACT_METRIC_RECONCILIATION_20261023.json', 'eea3eecf72a6c7d2b70b86e965864716edda658a'),
}
BOUNDS = {4: ('2026-09-26', '2026-09-28', 53), 5: ('2026-09-29', '2026-10-05', 47),
          6: ('2026-10-06', '2026-10-12', 49), 7: ('2026-10-13', '2026-10-19', 51),
          8: ('2026-10-20', '2026-10-26', 49)}


def blob(text):
    b = text.encode()
    return hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()


def name(text):
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode().lower()
    text = {'fiu': 'florida international', 'connecticut':'uconn'}.get(text, text)
    text = text.replace('appalachian state', 'app state').replace('jacksonville state', 'jax state')
    return re.sub('[^a-z0-9]', '', text)


def pair(away, home):
    return (name(away), name(home))


def finals(text, week):
    if week == 6:
        section = text.split('## Week 6 authoritative postgame join', 1)[1].split('## Week 7', 1)[0]
    elif week == 8:
        section = text.split('## Week 8 Tuesday FIRST_FROZEN', 1)[1]
    else:
        raise ValueError('only qualified Week6/8 scorecard schemas supported')
    rows = {}
    for line in section.splitlines():
        if not line.startswith('| '):
            continue
        c = [x.strip() for x in line.strip('|').split('|')]
        gid = None
        if week == 6 and len(c) == 12 and ' @ ' in c[0]:
            game, score, margin, total, outcome = c[0], c[5], c[6], c[7], c[10]
            scores = re.findall(r'\b(\d+)\b', score)
        elif week == 6 and len(c) == 10 and (' @ ' in c[0] or c[0] == 'Texas vs Oklahoma'):
            game, score, margin, total, outcome = c[0], c[4], c[5], c[6], c[9]
            scores = re.findall(r'\d+', score)
        elif week == 8 and len(c) == 11 and c[0].isdigit() and ' @ ' in c[1]:
            gid, game, score, margin, total = c[0], c[1], c[5], c[6], c[7]
            scores = re.findall(r'\d+', score)
            outcome = str(int(int(margin) > 0))
        else:
            continue
        if len(scores) != 2:
            raise ValueError('ambiguous final score')
        away_score, home_score = map(int, scores)
        if home_score == away_score or int(margin) != home_score-away_score or int(total) != home_score+away_score or int(outcome) != int(home_score > away_score):
            raise ValueError('inconsistent final score/margin/total/outcome')
        away, home = game.replace('Texas vs Oklahoma', 'Texas @ Oklahoma').split(' @ ')
        key = pair(away, home)
        if key in rows:
            raise ValueError('duplicate final identity')
        rows[key] = {'game_id': gid, 'final_away': away_score, 'final_home': home_score}
    if len(rows) != BOUNDS[week][2]:
        raise ValueError('incomplete governed final population')
    return rows


def evaluated(pred, final, week):
    pm, pt, pw = [float(pred[k]) for k in ('pred_margin', 'pred_total', 'pred_win')]
    am, total = final['final_home']-final['final_away'], final['final_home']+final['final_away']
    if am == 0:
        raise ValueError('unexpected tied final')
    return {'week': week, 'game_id': pred['game_id'], 'away_team': pred['away_team'], 'home_team': pred['home_team'],
            'original_start_date': pred['start_date'], 'population_class':pred['population_class'],
            'original_numeric_strings': {k: pred[k] for k in ('pred_margin', 'pred_total', 'pred_win')},
            'final_away': final['final_away'], 'final_home': final['final_home'],
            'actual_home_margin': am, 'actual_total': total, 'margin_error': am-pm, 'total_error': total-pt,
            'margin_direction_correct': int((pm > 0) == (am > 0)),
            'probability_classifier_correct': int((pw > .5) == (am > 0)),
            'home_win_brier_component': (pw-int(am > 0))**2}


def metrics(rows):
    n = len(rows)
    def mean(key, absolute=False):
        return math.fsum(abs(r[key]) if absolute else r[key] for r in rows)/n
    return {'n': n, 'margin_direction_correct': sum(r['margin_direction_correct'] for r in rows),
            'probability_classifier_correct': sum(r['probability_classifier_correct'] for r in rows),
            'margin_mae': mean('margin_error', True), 'signed_margin_error': mean('margin_error'),
            'total_mae': mean('total_error', True), 'signed_total_error': mean('total_error'),
            'home_win_brier': mean('home_win_brier_component')}


def reused(week, predictions):
    path, digest = SOURCES[week]
    text = (ROOT/path).read_text()
    if blob(text) != digest:
        raise ValueError('accepted prior baseline evidence changed')
    source = json.loads(text)
    rows = {}
    for r in source['rows']:
        gid = r['game_id']
        if gid in rows or gid not in predictions:
            raise ValueError('duplicate/out-of-population accepted row')
        pred = predictions[gid]
        if week == 4:
            numbers = [r[k] for k in ('pred_home_margin', 'pred_total', 'pred_home_win')]
            final = {'final_away': r['cbs_final']['away_score'], 'final_home': r['cbs_final']['home_score']}
            identity = pair(r['away_team'], r['home_team'])
        elif week == 5:
            numbers = [r[k] for k in ('pred_margin', 'pred_total', 'pred_home_win')]
            am, total = r['actual_home_margin'], r['actual_total']
            if (total-am) % 2 or total < abs(am):
                raise ValueError('invalid accepted final arithmetic')
            final = {'final_away': (total-am)//2, 'final_home': (total+am)//2}
            identity = pair(r['away_team'], r['home_team'])
        else:
            numbers = [r[k] for k in ('original_margin', 'original_total', 'original_home_win_p')]
            final = {k: r[k] for k in ('final_away', 'final_home')}
            identity = pair(*r['game'].split(' @ '))
        if identity != pair(pred['away_team'], pred['home_team']) or numbers != [float(pred[k]) for k in ('pred_margin', 'pred_total', 'pred_win')]:
            raise ValueError('accepted row differs from exact original')
        rows[gid] = evaluated(pred, final, week)
    if set(rows) != set(predictions):
        raise ValueError('incomplete accepted original identity union')
    return list(rows.values())


def build(first, scorecard):
    t, p, e = archive(first, FIRST_SHA, 'challenger_b_2026_', '_v1_206', (622, 526, 96), CUTOFF)
    text = Path(scorecard).read_text()
    if blob(text) != SCORECARD:
        raise ValueError('unqualified scorecard snapshot; recover exact bound source')
    weekly, all_rows, exclusions, populations = {}, [], {}, {}
    for week, (start, end, count) in BOUNDS.items():
        targets = {gid:r for gid,r in t.items() if start <= r['start_date'][:10] < end}
        predictions = {gid:p[gid] for gid in targets if gid in p and (week == 7 or p[gid]['population_class']=='FBS_VS_FBS')}
        if len(predictions) != count:
            raise ValueError('original governed weekly count mismatch')
        if week in SOURCES:
            rows = reused(week, predictions)
        else:
            results = finals(text, week)
            if {pair(r['away_team'], r['home_team']) for r in predictions.values()} != results.keys():
                raise ValueError('scorecard/original directed-pair union differs')
            rows = []
            for gid, pred in predictions.items():
                final = results[pair(pred['away_team'], pred['home_team'])]
                if final['game_id'] not in (None, gid):
                    raise ValueError('scorecard original ID differs')
                rows.append(evaluated(pred, final, week))
        weekly[str(week)] = metrics(rows)
        populations[str(week)] = {'original_targets':len(targets),'original_predictions':sum(g in p for g in targets),
                                 'original_exclusions':sum(g in e for g in targets),'scored_published_population':len(rows),
                                 'scored_non_fbs':sum(r['population_class']!='FBS_VS_FBS' for r in rows),
                                 'modeled_outside_published_population':[g for g in targets if g in p and g not in predictions]}
        exclusions[str(week)] = [{'game_id':gid,'away_team':r['away_team'],'home_team':r['home_team'],
                                 'original_reason':e[gid]['reasons']} for gid,r in targets.items() if gid in e]
        all_rows.extend(rows)
    if len({r['game_id'] for r in all_rows}) != 249:
        raise ValueError('cross-week duplicate identity or wrong denominator')
    # Existing accepted reports are comparisons, not inputs to computed metrics.
    m = weekly['6']
    if m['margin_direction_correct'] != 25 or any(round(m[k], places) != expected for k,places,expected in (
        ('margin_mae',2,15.13),('total_mae',2,13.54),('home_win_brier',4,.2840))):
        raise ValueError('Week6 exact replay conflicts with published summary; preserve and investigate')
    m = weekly['8']
    expected = {'margin_direction_correct':29,'margin_mae':11.750492754256612,
                'signed_margin_error':1.7710434013224963,'total_mae':14.025560758280701,
                'signed_total_error':2.63962359920701,'home_win_brier':.25709837447220446}
    if any(abs(m[k]-v)>1e-12 for k,v in expected.items()):
        raise ValueError('Week8 exact join conflicts with accepted weekly record')
    return {'status':'PASS_COMPLETED_WEEKS4_8_EXACT_ORIGINAL_BASELINE', 'scope':'DESCRIPTIVE_SPENT_2026_EVIDENCE_ONLY',
            'original_artifact_id':10897612260,'original_archive_sha256':FIRST_SHA,'original_cutoff_utc':CUTOFF,
            'scorecard_blob':SCORECARD,'reused_sources':{str(w):{'path':v[0],'blob':v[1]} for w,v in SOURCES.items()},
            'week6_precision_disclosure':{'reported_signed_margin':.90,'exact_signed_margin':weekly['6']['signed_margin_error'],
                                        'reported_signed_total':-.89,'exact_signed_total':weekly['6']['signed_total_error'],
                                        'disposition':'Use exact original fields for the baseline; preserve rounded historical reports. No forecast was changed.'},
            'weekly':weekly,'weekly_population_accounting':populations,'pooled':metrics(all_rows),
            'comparable_fbs_vs_fbs':metrics([r for r in all_rows if r['population_class']=='FBS_VS_FBS']),
            'population_qualification':'Published weekly populations preserved; Week7 includes The Citadel at Texas A&M. Separate FBS-only rollup excludes that one row. Week4/5 modeled non-FBS rows remain outside their governed denominators.',
            'original_exclusions':exclusions,'rows':all_rows,
            'market_decision_execution_reconstruction':False,
            's2_outputs_opened_or_scored':False,'scientific_or_champion_change':False}


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('first','scorecard','output'):
        p.add_argument('--'+key, type=Path, required=True)
    a = p.parse_args()
    if a.output.resolve() in (a.first.resolve(), a.scorecard.resolve()):
        p.error('output must not overwrite an input')
    result = build(a.first, a.scorecard)
    a.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','weekly','pooled')},indent=2))
