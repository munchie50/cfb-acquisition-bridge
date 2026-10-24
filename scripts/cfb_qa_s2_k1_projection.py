"""Outcome-blind future-only projection of exact accepted S2 parent inputs.

Preparers and source parsers never accept their own output or generate predictions.
"""
import argparse,csv,hashlib,html,io,json,re,subprocess
from datetime import datetime,timezone
from pathlib import Path
from zoneinfo import ZoneInfo
from cfb_qa_s2_k1_input_gate import check,load_inputs,validate_frames
from cfb_week7_accepted_s0_ancestry_audit import ALIASES

ROOT=Path(__file__).resolve().parents[1]
LINEAGE_PATH='evidence/scheduler_qa/CFB_WEEK8_ORIGINAL_ANCESTRY_RECOVERY_20261020.json'
LINEAGE_BLOB='337a23b03a10617ff87d9ba8c1c224cd3ebe1d9c'
PROTOCOL_PATH='evidence/qa_s2_projections/CFB_S2_WEEK8_PROJECTION_PROTOCOL_2026-10-23.md'
PROTOCOL_BLOB='23fd1f85251b3ed708e16ea2225d87421cb5c638'
URL='https://www.cbssports.com/college-football/schedule/FBS/2026/regular/8/'
SCHEDULE_ALIASES={**ALIASES,'New Mexico St.':'New Mexico State','Iowa St.':'Iowa State','Boise St.':'Boise State','Utah St.':'Utah State'}
TIMING_SCHEMA='CFB_S2_WEEK8_KICKOFF_CENSUS_V1'
PROJECTION_SCHEMA='CFB_S2_EXACT_PARENT_WEEK8_PROJECTION_V1'
IDCOL={'side':'game_id','target':'game_id','baseline':'game_id','context':'target_game_id','predicted':'game_id','excluded':'game_id','chronology':'game_id'}


def sha(raw):return hashlib.sha256(raw).hexdigest()
def blob(raw):return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
def clock(s):
    t=datetime.fromisoformat(s.replace('Z','+00:00'));check(t.tzinfo is not None,'NAIVE_PROJECTION_CLOCK');return t.astimezone(timezone.utc)
def canonical(obj):return json.dumps(obj,sort_keys=True,separators=(',',':'),allow_nan=False).encode()
def plain(s):return ' '.join(html.unescape(re.sub(r'<[^>]*>',' ',s)).split())


def schedule_census(raw,meta,lineage,as_of):
    now=clock(as_of);observed=clock(meta['response_recovered_by_utc'])
    check(meta['url']==URL and observed<=now and sha(raw)==meta['sha256'] and len(raw)==meta['bytes'],'SCHEDULE_SOURCE_BINDING')
    check(blob(lineage)==LINEAGE_BLOB,'WEEK8_COHORT_IDENTITY')
    rows=json.loads(lineage)['rows'];pairs={(r['away_team'],r['home_team']):r['game_id'] for r in rows}
    check(len(rows)==len(pairs)==56,'WEEK8_COHORT_UNION')
    doc=raw.decode('utf-8');check('All times are US/Eastern.' in doc,'EXPLICIT_SCHEDULE_TIMEZONE_REQUIRED')
    headings=list(re.finditer(r'<h2\b[^>]*class="[^"]*TableBase-title[^"]*"[^>]*>(.*?)</h2>',doc,re.S))
    output=[]
    for index,h in enumerate(headings):
        date_text=plain(h[1])
        if not re.fullmatch(r'(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday), October \d{1,2}, 2026',date_text):continue
        date=datetime.strptime(date_text,'%A, %B %d, %Y')
        check(date.strftime('%A')==date_text.split(',')[0] and 20<=date.day<=24,'SCHEDULE_DATE_PROFILE')
        region=doc[h.end():headings[index+1].start() if index+1<len(headings) else len(doc)]
        check('<table' in region,'SCHEDULE_TABLE_MISSING')
        for row in re.findall(r'<tr\b[^>]*class="[^"]*TableBase-bodyTr[^"]*"[^>]*>(.*?)</tr>',region,re.S):
            teams=re.findall(r'<span\b[^>]*class="TeamName"[^>]*>\s*<a\b[^>]*href="([^"]+)"[^>]*>(.*?)</a>',row,re.S)
            check(len(teams)==2,'SCHEDULE_EXACT_TEAM_PAIR_REQUIRED')
            names=[SCHEDULE_ALIASES.get(plain(n),plain(n)) for _,n in teams];pair=tuple(names)
            check(pair in pairs,'UNKNOWN_SCHEDULE_TEAM_PAIR')
            gid=pairs[pair]
            cells=re.search(r'<div\b[^>]*class="CellGame"[^>]*>\s*<a\b[^>]*href="([^"]+)"[^>]*>(.*?)</a>',row,re.S)
            check(cells is not None,'SCHEDULE_EVENT_LINK_REQUIRED')
            href=html.unescape(cells[1]);kick=None;status='NO_EXPLICIT_FUTURE_KICKOFF'
            event=re.fullmatch(r'/college-football/gametracker/(?:preview|live|recap)/NCAAF_(\d{8})_([^/@]+)@([^/]+)/',href)
            check(event is not None and event[1]==date.strftime('%Y%m%d'),'SCHEDULE_EVENT_DATE_BINDING')
            codes=[re.fullmatch(r'/college-football/teams/([^/]+)/[^/]+/',link) for link,_ in teams]
            check(all(codes) and [c[1] for c in codes]==[event[2],event[3]],'SCHEDULE_EVENT_TEAM_BINDING')
            # CBS uses both preview and live links for future scheduled games.
            # Only a complete time-token match may leave quarantine; all other
            # link text (including results) is discarded, never a model field.
            m=re.fullmatch(r'(\d{1,2}):(\d{2}) (am|pm)',plain(cells[2]))
            if m:
                hour,minute=int(m[1]),int(m[2]);check(1<=hour<=12 and 0<=minute<60,'SCHEDULE_TIME_RANGE')
                local=date.replace(hour=hour%12+(12 if m[3]=='pm' else 0),minute=minute,tzinfo=ZoneInfo('America/New_York'))
                check(local.replace(fold=0).utcoffset()==local.replace(fold=1).utcoffset(),'AMBIGUOUS_SCHEDULE_TIME')
                kick=local.astimezone(timezone.utc).isoformat();status='EXPLICIT_FUTURE' if clock(kick)>now else 'EXPLICIT_ELAPSED'
            output.append({'game_id':gid,'away_team':names[0],'home_team':names[1],'source_date':date.date().isoformat(),
                           'qualified_kickoff_utc':kick,'source_event_url':'https://www.cbssports.com'+href,'timing_status':status})
    check(len(output)==56 and len({r['game_id'] for r in output})==56 and {r['game_id'] for r in output}=={r['game_id'] for r in rows},'SCHEDULE_FULL_COHORT_UNION')
    return {'schema':TIMING_SCHEMA,'source_url':URL,'source_recovered_by_utc':meta['response_recovered_by_utc'],
            'source_sha256':meta['sha256'],'source_bytes':meta['bytes'],'source_clock_semantics':'RESPONSE_RECOVERED_BY',
            'timezone':'America/New_York','cohort_lineage_blob':LINEAGE_BLOB,'parsed_at_utc':as_of,'rows':sorted(output,key=lambda r:r['game_id'])}


def parent_paths(package):
    s=Path(package)/'s0';prefix='challenger_b_2026_refresh_'
    return {'side':s/(prefix+'team_side_substrate_v1_246.csv'),'target':s/(prefix+'target_ledger_v1_246.csv'),
      'baseline':Path(package)/'baseline/target_baselines.csv','context':Path(package)/'context/source_context.csv',
      'predicted':s/(prefix+'fair_predictions_v1_246.csv'),'excluded':s/(prefix+'exclusions_v1_246.csv'),
      'chronology':s/(prefix+'chronology_audit_v1_246.csv')}


def projected_bytes(raw,idcol,selected):
    # Preserve actual parent bytes and their order, not reserialized float values.
    text=raw.decode('utf-8');lines=text.splitlines(keepends=True);records=list(csv.reader(io.StringIO(text,newline='')))
    check(len(lines)==len(records) and len(records)>0,'MULTILINE_OR_EMPTY_PARENT_CSV')
    check(len(records[0])==len(set(records[0])) and idcol in records[0],'PARENT_CSV_IDENTITY')
    pos=records[0].index(idcol);ordinals=[];kept=[lines[0]]
    for ordinal,(values,line) in enumerate(zip(records[1:],lines[1:])):
        check(len(values)==len(records[0]),'PARENT_CSV_ROW_WIDTH')
        if values[pos] in selected:ordinals.append(ordinal);kept.append(line)
    return ''.join(kept).encode('utf-8'),ordinals


def make_projection(package,census,as_of):
    paths=parent_paths(package);f,a=load_inputs(paths['side'],paths['target'],paths['baseline'],paths['context'],'2026-10-13T15:13:13.866672+00:00')
    check(blob((ROOT/PROTOCOL_PATH).read_bytes())==PROTOCOL_BLOB,'PROJECTION_PROTOCOL_BINDING')
    check(census['schema']==TIMING_SCHEMA and census['source_url']==URL and census['cohort_lineage_blob']==LINEAGE_BLOB,'TIMING_PROFILE')
    now=clock(as_of);check(clock(census['source_recovered_by_utc'])<=clock(census['parsed_at_utc'])<=now,'TIMING_CLOCK_ORDER')
    cohort=json.loads((ROOT/LINEAGE_PATH).read_text())['rows'];ident={r['game_id']:(r['away_team'],r['home_team']) for r in cohort}
    check(len(census['rows'])==56 and {r['game_id'] for r in census['rows']}==set(ident),'TIMING_UNION')
    check(all((r['away_team'],r['home_team'])==ident[r['game_id']] for r in census['rows']),'TIMING_IDENTITY_BINDING')
    times={r['game_id']:r['qualified_kickoff_utc'] for r in census['rows'] if r['timing_status']=='EXPLICIT_FUTURE' and r['qualified_kickoff_utc'] and clock(r['qualified_kickoff_utc'])>now}
    check(bool(times),'NO_FUTURE_COHORT_TARGETS')
    targets=f['target'];all_ids=set(targets.game_id);check(set(ident)<=all_ids,'COHORT_NOT_IN_ACCEPTED_PARENT')
    for r in targets[targets.game_id.isin(ident)].itertuples():check((r.away_team,r.home_team)==ident[r.game_id],'COHORT_PARENT_IDENTITY_BINDING')
    selected=set(times);projected={k:df[df[IDCOL[k]].isin(selected)].copy() for k,df in f.items()}
    validate_frames(projected,a['cutoff_utc'])
    surfaces={}
    for kind,p in paths.items():
        raw,ordinals=projected_bytes(p.read_bytes(),IDCOL[kind],selected)
        surfaces[kind]={'parent_sha256':a['input_sha256'][kind],'projected_sha256':sha(raw),'row_ordinals':ordinals,'rows':len(ordinals)}
    dispositions=[{'game_id':gid,'disposition':'SELECTED_FUTURE_WEEK8' if gid in selected else 'COHORT_WITHOUT_VERIFIED_FUTURE_KICKOFF' if gid in ident else 'OUTSIDE_PREDECLARED_WEEK8_COHORT'} for gid in sorted(all_ids)]
    return {'schema':PROJECTION_SCHEMA,'prepared_at_utc':as_of,'parent_cutoff_utc':a['cutoff_utc'],
      'protocol_ref':{'path':PROTOCOL_PATH,'blob':PROTOCOL_BLOB},'cohort_lineage_ref':{'path':LINEAGE_PATH,'blob':LINEAGE_BLOB},
      'timing_census_sha256':sha(canonical(census)),'parent_input_sha256':a['input_sha256'],'parent_acceptance_records':a['acceptance_records'],
      'selected_game_ids':sorted(selected),'qualified_kickoffs_utc':times,'surfaces':surfaces,'parent_dispositions':dispositions,
      'scope':'PROPOSED_PROJECTION_ONLY_NOT_ACCEPTANCE_OR_PREDICTION_FREEZE'}




def verify_projection(package,projection,census,confirmation,as_of):
    """Independent projection accounting; never calls the preparer."""
    now=clock(as_of);paths=parent_paths(package)
    f,a=load_inputs(paths['side'],paths['target'],paths['baseline'],paths['context'],projection['parent_cutoff_utc'])
    check(set(projection)=={'schema','prepared_at_utc','parent_cutoff_utc','protocol_ref','cohort_lineage_ref','timing_census_sha256','parent_input_sha256','parent_acceptance_records','selected_game_ids','qualified_kickoffs_utc','surfaces','parent_dispositions','scope'},'PROJECTION_SCHEMA_FIELDS')
    check(projection['schema']==PROJECTION_SCHEMA and projection['scope']=='PROPOSED_PROJECTION_ONLY_NOT_ACCEPTANCE_OR_PREDICTION_FREEZE','PROJECTION_SCHEMA')
    check(clock(projection['prepared_at_utc'])<=now,'PROJECTION_FUTURE_CLOCK')
    check(projection['protocol_ref']=={'path':PROTOCOL_PATH,'blob':PROTOCOL_BLOB} and blob((ROOT/PROTOCOL_PATH).read_bytes())==PROTOCOL_BLOB,'PROJECTION_PROTOCOL_BINDING')
    check(projection['cohort_lineage_ref']=={'path':LINEAGE_PATH,'blob':LINEAGE_BLOB} and blob((ROOT/LINEAGE_PATH).read_bytes())==LINEAGE_BLOB,'PROJECTION_COHORT_BINDING')
    ident={r['game_id']:(r['away_team'],r['home_team']) for r in json.loads((ROOT/LINEAGE_PATH).read_text())['rows']}
    for timing in (census,confirmation):
        check(set(timing)=={'schema','source_url','source_recovered_by_utc','source_sha256','source_bytes','source_clock_semantics','timezone','cohort_lineage_blob','parsed_at_utc','rows'},'TIMING_SCHEMA_FIELDS')
        check(timing['schema']==TIMING_SCHEMA and timing['source_url']==URL and timing['timezone']=='America/New_York' and timing['source_clock_semantics']=='RESPONSE_RECOVERED_BY' and timing['cohort_lineage_blob']==LINEAGE_BLOB,'TIMING_PROFILE')
        check(clock(timing['source_recovered_by_utc'])<=clock(timing['parsed_at_utc'])<=now,'TIMING_CLOCK_ORDER')
        check(len(timing['rows'])==56 and len({r['game_id'] for r in timing['rows']})==56 and {r['game_id'] for r in timing['rows']}==set(ident),'TIMING_FULL_UNION')
        for row in timing['rows']:
            check(set(row)=={'game_id','away_team','home_team','source_date','qualified_kickoff_utc','source_event_url','timing_status'},'TIMING_ROW_FIELDS')
            check((row['away_team'],row['home_team'])==ident[row['game_id']],'TIMING_IDENTITY_BINDING')
            check(row['timing_status'] in ('EXPLICIT_FUTURE','EXPLICIT_ELAPSED','NO_EXPLICIT_FUTURE_KICKOFF'),'TIMING_STATUS')
            check(row['source_event_url'].startswith('https://www.cbssports.com/college-football/gametracker/'),'TIMING_SOURCE_EVENT')
            if row['qualified_kickoff_utc'] is not None:
                k=clock(row['qualified_kickoff_utc'])
                check(k.astimezone(ZoneInfo('America/New_York')).date().isoformat()==row['source_date'],'TIMING_LOCAL_DATE_BINDING')
                check(row['timing_status']==('EXPLICIT_FUTURE' if k>clock(timing['parsed_at_utc']) else 'EXPLICIT_ELAPSED'),'TIMING_STATUS_CLOCK_BINDING')
            else:check(row['timing_status']=='NO_EXPLICIT_FUTURE_KICKOFF','TIMING_MISSING_KICKOFF_STATUS')
    check(clock(census['source_recovered_by_utc'])<=clock(projection['prepared_at_utc']) and clock(confirmation['source_recovered_by_utc'])>clock(census['source_recovered_by_utc']),'INDEPENDENT_TIMING_ORDER')
    check(projection['timing_census_sha256']==sha(canonical(census)),'TIMING_CENSUS_BINDING')
    semantic=lambda t:{r['game_id']:(r['away_team'],r['home_team'],r['source_date'],r['qualified_kickoff_utc']) for r in t['rows']}
    check(semantic(census)==semantic(confirmation),'TIMING_REACQUISITION_DISAGREEMENT')
    expected={r['game_id']:r['qualified_kickoff_utc'] for r in confirmation['rows'] if r['timing_status']=='EXPLICIT_FUTURE' and r['qualified_kickoff_utc'] and clock(r['qualified_kickoff_utc'])>now}
    selected=set(expected)
    check(bool(selected) and projection['selected_game_ids']==sorted(selected) and projection['qualified_kickoffs_utc']==expected,'SELECTED_FUTURE_UNION')
    check(projection['parent_input_sha256']==a['input_sha256'] and projection['parent_acceptance_records']==a['acceptance_records'],'PROJECTION_PARENT_BINDING')
    all_ids=set(f['target'].game_id)
    expected_dispositions=[{'game_id':gid,'disposition':'SELECTED_FUTURE_WEEK8' if gid in selected else 'COHORT_WITHOUT_VERIFIED_FUTURE_KICKOFF' if gid in ident else 'OUTSIDE_PREDECLARED_WEEK8_COHORT'} for gid in sorted(all_ids)]
    check(projection['parent_dispositions']==expected_dispositions,'PARENT_FULL_ACCOUNTING')
    check(set(projection['surfaces'])==set(IDCOL),'PROJECTED_SURFACE_UNION')
    subset={}
    for kind,df in f.items():
        ordinals=[i for i,value in enumerate(df[IDCOL[kind]]) if value in selected]
        subset[kind]=df.iloc[ordinals].copy()
        lines=paths[kind].read_bytes().splitlines(keepends=True)
        check(len(lines)==len(df)+1,'PARENT_LINE_ORDINALS')
        # This verifier derives indices from validated parent dataframes, while
        # the preparer independently parses raw CSV identities.
        raw=b''.join([lines[0]]+[lines[i+1] for i in ordinals])
        expected_surface={'parent_sha256':a['input_sha256'][kind],'projected_sha256':sha(raw),'row_ordinals':ordinals,'rows':len(ordinals)}
        check(projection['surfaces'][kind]==expected_surface,'PROJECTED_BYTES_OR_ORDINALS')
    validate_frames(subset,a['cutoff_utc'])
    return subset,{'verdict':'PASS_EXACT_PARENT_FUTURE_PROJECTION_ONLY','parent_targets':len(all_ids),'cohort_targets':len(ident),'projected_targets':len(selected),
      's0_eligible_projected':len(subset['predicted']),'s0_excluded_projected':len(subset['excluded']),
      'original_model_kickoff_preserved':True,'outcomes_opened':False,'predictions_generated':False}


def immutable_ref(ref):
    check(set(ref)=={'path','commit','blob'},'IMMUTABLE_REF_FIELDS')
    check(re.fullmatch(r'evidence/qa_s2_projections/[A-Za-z0-9_-]+\.json',ref['path']) is not None,'PROJECTION_REF_PATH')
    check(all(re.fullmatch(r'[0-9a-f]{40}',ref[k]) for k in ('commit','blob')),'PROJECTION_REF_DIGEST')
    subprocess.run(['git','-C',str(ROOT),'merge-base','--is-ancestor',ref['commit'],'HEAD'],check=True,capture_output=True)
    raw=subprocess.check_output(['git','-C',str(ROOT),'show',ref['commit']+':'+ref['path']])
    check(blob(raw)==ref['blob'],'IMMUTABLE_REF_BLOB')
    return raw,json.loads(raw)


def apply_accepted_projection(package,acceptance_ref,as_of):
    raw,acceptance=immutable_ref(acceptance_ref)
    check(set(acceptance)=={'schema','accepted_at_utc','projection_ref','timing_ref','confirmation_ref','implementation','ci','verification','scope'},'PROJECTION_ACCEPTANCE_FIELDS')
    check(acceptance['schema']=='CFB_S2_FUTURE_PROJECTION_ACCEPTANCE_V1' and acceptance['scope']=='EXACT_PROJECTION_ACCEPTED_STUDY_ONLY_NOT_PREDICTION_FREEZE','PROJECTION_ACCEPTANCE_SCOPE')
    check(clock(acceptance['accepted_at_utc'])<=clock(as_of),'ACCEPTANCE_FUTURE_CLOCK')
    p_raw,p=immutable_ref(acceptance['projection_ref']);_,c=immutable_ref(acceptance['timing_ref']);_,confirm=immutable_ref(acceptance['confirmation_ref'])
    check(clock(confirm['source_recovered_by_utc'])<=clock(acceptance['accepted_at_utc']),'ACCEPTANCE_BEFORE_SOURCE')
    for path,digest in acceptance['implementation'].items():check(blob((ROOT/path).read_bytes())==digest,'ACCEPTED_IMPLEMENTATION_CHANGED')
    required={'scripts/cfb_qa_prospective_s2_k1_consumer_v1_2026_09_30.py','scripts/cfb_qa_s2_k1_input_gate.py','scripts/cfb_qa_s2_k1_projection.py'}
    check(set(acceptance['implementation'])==required and acceptance['verification']['verdict']=='PASS_EXACT_PARENT_FUTURE_PROJECTION_ONLY','UNQUALIFIED_ACCEPTANCE_IMPLEMENTATION')
    check(bool(acceptance['ci']) and all(r['conclusion']=='success' for r in acceptance['ci']),'ACCEPTANCE_CI_INCOMPLETE')
    frames,verified=verify_projection(package,p,c,confirm,as_of)
    check(verified==acceptance['verification'],'ACCEPTANCE_VERIFICATION_CHANGED')
    context={'acceptance_ref':acceptance_ref,'acceptance_sha256':sha(raw),'projection_ref':acceptance['projection_ref'],
             'projection_sha256':sha(p_raw),'timing_ref':acceptance['timing_ref'],'confirmation_ref':acceptance['confirmation_ref'],
             'implementation':acceptance['implementation'],'qualified_kickoffs_utc':p['qualified_kickoffs_utc'],'projected_input_sha256':{k:v['projected_sha256'] for k,v in p['surfaces'].items()},
             'parent_targets':verified['parent_targets'],'projected_targets':verified['projected_targets'],
             'freeze_scope':'PROSPECTIVE_STUDY_ONLY_NO_SCORING_OR_PRODUCTION'}
    return frames,context


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--package-root',type=Path,required=True);p.add_argument('--census',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
    args=p.parse_args();r=make_projection(args.package_root,json.loads(args.census.read_text()),datetime.now(timezone.utc).isoformat());args.output.write_text(json.dumps(r,indent=2,sort_keys=True)+'\n');print(json.dumps({'selected':len(r['selected_game_ids']),'parent_dispositions':len(r['parent_dispositions']),'status':r['scope']}))
