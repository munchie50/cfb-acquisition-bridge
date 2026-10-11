"""Exact Week7 lineage/display correction; no prediction, decision or acceptance creation."""
import csv, hashlib, io, json, math, re, zipfile
from pathlib import Path
from cfb_week7_accepted_s0_ancestry_audit import sheet_rows
from cfb_hot_sheet_current_decision_binding_gate import blob, audit as binding

FIRST_SHA='772b8683365ebf62d35fc3813beb138688b84af4172a0b261fd9218691d5adcf'
REFRESH_SHA='674501a82f6eb207b58b30c483910304c881b3ce29ba2506258152455cb6047b'
PARENT_SHA='c027e59eb0f752cd0225d69938f52e924f5c1a68'
DECISION_SHA='4a525667b6ecfbeaf6e74222d18640e91e5d35f2'
CUTOFF='2026-09-26T03:47:37.497112+00:00'
MARKER='## Week 7 FIRST_FROZEN lineage clarification — 2026-10-11 14:29 CT'
NEW_PATH='evidence/operational/CFB_WEEK7_HOT_SHEET_2026-10-11_1429CT.md'

def archive(path,digest,prefix,suffix,counts,cutoff):
    raw=Path(path).read_bytes()
    if hashlib.sha256(raw).hexdigest()!=digest:raise ValueError('archive identity mismatch')
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        manifest=json.loads(z.read('s0/manifest_v1_246.json' if prefix.startswith('s0/') else 'manifest_v1_206.json'))
        if manifest['cutoff_utc']!=cutoff:raise ValueError('immutable cutoff mismatch')
        for name,sha in manifest['hashes'].items():
            if hashlib.sha256(z.read(('s0/' if prefix.startswith('s0/') else '')+name)).hexdigest()!=sha:
                raise ValueError('manifest byte mismatch')
        def table(n):return list(csv.DictReader(io.StringIO(z.read(prefix+n+suffix+'.csv').decode())))
        t,p,e=[table(n) for n in ('target_ledger','fair_predictions','exclusions')]
    if tuple(map(len,(t,p,e)))!=counts:raise ValueError('frozen full population mismatch')
    def index(rows):
        result={r['game_id']:r for r in rows}
        if len(result)!=len(rows):raise ValueError('duplicate archive ID')
        return result
    ti,pi,ei=map(index,(t,p,e))
    if pi.keys()&ei.keys() or pi.keys()|ei.keys()!=ti.keys():raise ValueError('partition mismatch')
    for r in p+e:
        if any(r[k]!=ti[r['game_id']][k] for k in ('away_team','home_team')):raise ValueError('directed identity mismatch')
    for r in p:
        if not all(math.isfinite(float(r[k])) for k in ('pred_margin','pred_total','pred_win')) or not 0<=float(r['pred_win'])<=1:
            raise ValueError('invalid frozen number')
    return ti,pi,ei

def fair(r):
    margin=float(r['pred_margin'])
    favorite=r['home_team'] if margin>=0 else r['away_team']
    return f"FIRST_FROZEN: {favorite} -{abs(margin):.1f} / {float(r['pred_total']):.1f} / {float(r['pred_win']):.3f} home"

def inventory(first,refresh,parent):
    if blob(parent)!=PARENT_SHA:raise ValueError('unqualified parent sheet')
    t,p,e=archive(first,FIRST_SHA,'challenger_b_2026_','_v1_206',(622,526,96),CUTOFF)
    rt,rp,rex=archive(refresh,REFRESH_SHA,'s0/challenger_b_2026_refresh_','_v1_246',(498,495,3),'2026-10-06T15:11:29.838398+00:00')
    by_pair={}
    for row in t.values():by_pair.setdefault((row['away_team'],row['home_team']),[]).append(row)
    current=sheet_rows(parent);result=[]
    for pair,clock in current:
        candidates=by_pair.get(pair,[])
        if len(candidates)!=1:raise ValueError('missing/ambiguous exact directed pair')
        row=candidates[0];gid=row['game_id']
        if gid not in rt or any(row[k]!=rt[gid][k] for k in ('away_team','home_team')):raise ValueError('refresh ID mismatch')
        reason=e[gid]['reasons'] if gid in e else None
        refresh_state='PREDICTION' if gid in rp else 'EXCLUDED'
        display=fair(p[gid]) if gid in p else 'FIRST_FROZEN EXCLUDED — '+reason+'; Oct6 REFRESH '+refresh_state+' (not substituted)'
        result.append({'game_id':gid,'away_team':pair[0],'home_team':pair[1],
                       'first_frozen_status':'PREDICTION' if gid in p else 'EXCLUDED',
                       'first_frozen_exclusion':reason,'oct6_refresh_status':refresh_state,
                       'display':display,'first_frozen_start':row['start_date'],
                       'current_display_start':clock.isoformat()})
    if len({r['game_id'] for r in result})!=62 or sum(r['first_frozen_status']=='PREDICTION' for r in result)!=51:
        raise ValueError('bounded first-freeze population mismatch')
    return result

def ledger_append():
    return '\n\n'+MARKER+'\n\nOriginal September26 accepted artifact10897612260 (ZIP '+FIRST_SHA+') covers all62 currentWeek7 targets:51 immutable FIRST_FROZEN predictions and11 explicit original exclusions. This prospectively corrects the earlier blanket no-accepted-Week7-FIRST_FROZEN claim; historical statements remain preserved. All4Tuesday/Wednesday games have original predictions. Historical Challenger B is the active Beta Production Champion under v1.222, not a different model.\n\nAccepted October6 REFRESH artifact11423386216 (ZIP '+REFRESH_SHA+') covers61 predictions+1 exclusion, including10 targets excluded in the original snapshot. REFRESH never substitutes for or rewrites original predictions/exclusions. The upcoming Monday readiness/Tuesday candidate is a separate weekly-cycle dependency, not the existence test for original accepted predictions.\n\nAll62 decision dispositions remain INCONCLUSIVE; acceptable numbers/prices remain not established. No bet, trip, execution or confidence is authorized. Qualified consensus/current Caesars and material availability remain unresolved.51 rows can display accepted original numbers;11 original exclusions stay explicit. Current schedule and historical model clocks remain separate. Existing saved reconciliation/cutoff values are retained only as planning information: CUTOFF_AUTHORITY_UNVERIFIED; effective practical provenance remains unresolved. No deadline is relaxed or invented.\n'

def project(parent,decision,rows):
    if blob(parent)!=PARENT_SHA or blob(decision)!=DECISION_SHA:raise ValueError('unqualified projection ancestry')
    updated=decision+ledger_append()
    result=parent.replace('# CFB Week 7 Hot Sheet — Sunday 2026-10-11 13:05 CT', '# CFB Week 7 Hot Sheet — Sunday 2026-10-11 14:29 CT lineage correction',1)
    result=result.replace('**Status:** AFTERNOON MARKET REFRESH / PRE-FREEZE','**Status:** FIRST_FROZEN LINEAGE RESTORED / NEW WEEKLY REFRESH PENDING',1)
    result=re.sub(r'^\*\*Frozen-model boundary:\*\*.*$', '**Frozen-model boundary:** Original accepted September26 FIRST_FROZEN covers51 predictions+11 explicit exclusions; cutoff '+CUTOFF+'. Historical Challenger B is the Beta Production Champion. Accepted October6 REFRESH is separate and never substituted. New Monday/Tuesday weekly cycle is pending. This14:29CT correction is not a new market retrieval, model run or betting decision.',result,count=1,flags=re.M)
    result=result.replace('decision '+DECISION_SHA,'decision '+blob(updated),1)
    lines=result.splitlines();i=0;section=None
    for n,line in enumerate(lines):
        if line.startswith('## '):section=line[3:]
        cells=[c.strip() for c in line.strip('|').split('|')]
        if len(cells)!=9 or not re.match(r'^(Tue|Wed|Thu|Fri|Sat) Oct ',cells[0]):continue
        if i>=len(rows):raise ValueError('extra row')
        row=rows[i];i+=1
        cells[2]=row['display']
        cells[5]='INCONCLUSIVE — lineage clarified; no new decision'
        cells[6]=('Original FIRST_FROZEN available' if row['first_frozen_status']=='PREDICTION' else 'Original FIRST_FROZEN excluded; no refresh substitution')+'; new weekly cycle pending; consensus unavailable; Caesars unverified'
        if cells[1]=='Nebraska @ Oregon':cells[6]+='; authoritative kickoff corrected to 10:00 PM CT'
        cells[7]='UNVERIFIED planning times — '+cells[7]+'; CUTOFF_AUTHORITY_UNVERIFIED'
        cells[8]='Not established; no executable recommendation from lineage display'
        lines[n]='| '+' | '.join(cells)+' |'
    if i!=62:raise ValueError('missing row')
    result='\n'.join(lines)+'\n'
    result=result.replace('no frozen prediction','original FIRST_FROZEN available; new weekly cycle pending')
    result=result.replace('Accepted prediction lineage plus qualified benchmark or verified Caesars offer','Independent weekly-cycle reconciliation plus qualified benchmark or verified Caesars offer')
    result=result.replace('reconcile Tue Oct 13 1:00 PM CT','unverified planning reconciliation Tue Oct 13 1:00 PM CT')
    result=result.replace('reconcile Sat Oct 17 1:00 PM CT, cutoff 9:00 PM CT','unverified planning reconciliation Sat Oct 17 1:00 PM CT, cutoff 9:00 PM CT; CUTOFF_AUTHORITY_UNVERIFIED')
    result+='\n## Frozen-source provenance and limits\n\nOriginal accepted FIRST_FROZEN: producer36216090860/artifact10897612260; ZIP '+FIRST_SHA+'; acceptancev1.208; namingv1.222; lineagev1.216.51numbers faithfully projected at1decimal spread/total and3decimals home-win probability;11original exclusions retained. October6 accepted REFRESH artifact11423386216/ZIP '+REFRESH_SHA+' is separate ancestry only. No refresh value replaces an original value/exclusion. Current market/quote retrieval remains13:05CT, not14:29CT; saved planning clocks are not practical execution authority. Earlier Hot Sheets and decisions remain immutable historical evidence.\n'
    return updated,result

def audit(sheet,parent,decision,prior_decision,first,refresh):
    rows=inventory(first,refresh,parent)
    expected_decision,expected_sheet=project(parent,prior_decision,rows)
    if decision!=expected_decision:raise ValueError('canonical append mismatch or historical rewrite')
    binding(sheet,decision)
    if sheet!=expected_sheet:raise ValueError('lineage/quote/clock/decision projection mismatch')
    return {'verdict':'PASS_EXACT_FIRST_FROZEN_LINEAGE_DISPLAY_ONLY','games':62,'first_frozen_predictions':51,
            'first_frozen_exclusions':11,'refresh_predictions':61,'refresh_exclusions':1,
            'sheet_blob':blob(sheet),'decision_blob':blob(decision),'original_zip_sha256':FIRST_SHA,
            'scope':'immutable accepted numbers/display only; no new weekly acceptance, market/source truth, deadline, bet or execution authority'}

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('sheet','parent','decision','prior-decision','first','refresh'):p.add_argument('--'+name,required=True,type=Path)
    a=p.parse_args()
    print(json.dumps(audit(a.sheet.read_text(),a.parent.read_text(),a.decision.read_text(),a.prior_decision.read_text(),a.first,a.refresh),indent=2))
