"""Independent source/Decimal verification of the one-cohort scoring artifact."""
import csv
import json
import re
import sys
from copy import deepcopy
from decimal import Decimal, localcontext
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'scripts'))
sys.path.insert(0,str(Path(__file__).parent))
from cfb_cbs_full_board_normalizer import ALIASES
import cfb_s2_week8_outcome_comparison_20261025 as s


def verify():
    path=ROOT/'evidence/audits/CFB_S2_WEEK8_OUTCOME_COMPARISON_20261025.json'
    r=json.loads(path.read_text())
    source=(ROOT/'evidence/operational/CFB_CBS_WEEK8_RESULTS_CAPTURE_20261025T120800Z.md').read_text()
    assert s.blob(source)=='2aa53f5793bb511373eba9bbbf6e6249d3984836'
    aliases={**ALIASES,'Iowa St.':'Iowa State','Utah St.':'Utah State','Boise St.':'Boise State'}
    team_rows=[]
    for line in source.splitlines():
        if not re.match(r'L\d+: ',line):continue
        cells=[x.strip() for x in line.split(': ',1)[1].split('|')]
        if len(cells)==6 and cells[1].isdigit():
            label=re.sub(r'^\d+\s+','',cells[0]);_,name=label.split(' ',1)
            team_rows.append((aliases.get(name,name),int(cells[1])))
    assert len(team_rows)==112
    results={s.pair(team_rows[i][0],team_rows[i+1][0]):(team_rows[i][1],team_rows[i+1][1]) for i in range(0,112,2)}
    assert len(results)==56
    frozen=list(csv.DictReader((s.FREEZE/'s2_k1_predictions.csv').open()))
    original={x['game_id']:x for x in frozen}
    assert len(original)==len(r['rows'])==44 and set(original)=={x['game_id'] for x in r['rows']}
    for row in r['rows']:
        assert all(row[k]==v for k,v in original[row['game_id']].items())
        assert results[s.pair(row['away_team'],row['home_team'])]==(row['final_away'],row['final_home'])
    groups={'ALL_COMMON_GAMES':r['rows']}
    groups.update({d:[x for x in r['rows'] if x['history_depth_slice']==d] for d in s.DEPTHS})
    for field,threshold in [('margin',Decimal(7)),('total',Decimal(7)),('win',Decimal('.10'))]:
        groups['DISAGREEMENT_'+field.upper()]=[x for x in r['rows'] if abs(Decimal(x['pred_'+field])-Decimal(x['s0_pred_'+field]))>=threshold]
    verified_groups=0
    with localcontext() as ctx:
        ctx.prec=50
        for group,rows in groups.items():
            assert r['groups'][group]['n']==len(rows)
            if not rows:
                assert all(r['groups'][group][k] is None for k in ('S0','S2_K1','S2_minus_S0'));continue
            for label,prefix in [('S0','s0_'),('S2_K1','')]:
                n=Decimal(len(rows));me=[];te=[];br=[];ll=[];mc=pc=0
                for row in rows:
                    pm=Decimal(row[prefix+'pred_margin']);pt=Decimal(row[prefix+'pred_total']);pw=Decimal(row[prefix+'pred_win'])
                    am=Decimal(row['final_home']-row['final_away']);total=Decimal(row['final_home']+row['final_away']);y=int(am>0)
                    me.append(am-pm);te.append(total-pt);br.append((pw-y)**2);ll.append(-(pw if y else 1-pw).ln())
                    mc+=int((pm>0)==(am>0));pc+=int((pw>Decimal('.5'))==(am>0))
                expected={'margin_mae':sum(map(abs,me))/n,'margin_rmse':(sum(v*v for v in me)/n).sqrt(),'margin_bias':sum(me)/n,
                          'total_mae':sum(map(abs,te))/n,'total_rmse':(sum(v*v for v in te)/n).sqrt(),'total_bias':sum(te)/n,
                          'win_brier':sum(br)/n,'win_log_loss':sum(ll)/n}
                target=r['groups'][group][label]
                assert all(abs(Decimal(str(target[k]))-v)<Decimal('1e-12') for k,v in expected.items())
                assert target['margin_direction_correct']==mc and target['probability_classifier_correct']==pc
            verified_groups+=1
    manifest=json.loads((s.FREEZE/'manifest.json').read_text());rejected=[]
    def reject(label,fn):
        try:fn()
        except ValueError:rejected.append(label);return
        raise AssertionError('not rejected: '+label)
    reject('missing common game',lambda:s.validate_rows(frozen[:-1],manifest))
    reject('duplicate common game',lambda:s.validate_rows(frozen[:-1]+[frozen[0]],manifest))
    for label,key,value in [('changed history slice','history_depth_slice','DEPTH_1_2'),('changed cutoff','snapshot_cutoff_utc','2026-10-14T00:00:00Z'),('late freeze','freeze_recorded_at_utc','2026-10-26T00:00:00Z'),('invalid probability','pred_win','1.1')]:
        changed=deepcopy(frozen);changed[0][key]=value
        reject(label,lambda changed=changed:s.validate_rows(changed,manifest))
    text=(ROOT/'evidence/operational/CFB_POSTGAME_FIRST_FROZEN_SCORECARD.md').read_text()
    reject('conflicting context final',lambda:s.outcomes(text.replace('Virginia Tech 20, Clemson 16','Virginia Tech 20, Wrong Team 16'),frozen))
    return {'status':'PASS_INDEPENDENT_S2_SCORING_VERIFICATION','games':44,'source_capture_games':56,'all_finals_crosschecked':44,
            'original_exclusion_context_games':sum(x['original_exclusion_context_used'] for x in r['rows']),
            'frozen_candidate_and_control_numeric_strings':264,'all_frozen_fields_preserved':True,
            'decimal_precision':50,'nonempty_metric_groups_verified':verified_groups,'loss_metrics_per_model':8,'classifiers_per_model':2,
            'all_predeclared_empty_slices_reported':True,'rejections':rejected,
            'result_blob':s.blob(path.read_text()),'helper_blob':s.blob(Path(s.__file__).read_text()),
            'source_capture_blob':'2aa53f5793bb511373eba9bbbf6e6249d3984836'}


if __name__=='__main__':
    result=verify()
    (ROOT/'evidence/audits/CFB_S2_WEEK8_OUTCOME_VERIFICATION_20261025.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
