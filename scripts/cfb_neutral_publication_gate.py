"""Source-derived Week7 neutral presentation schema; no source or betting acceptance."""
import argparse, json, math, re
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo
from cfb_hot_sheet_current_decision_binding_gate import blob
from cfb_recovery_navigation_reader import unique, clock

LINEAGE_SHA='d80e26c398de48e7a386ad9a627fe44f4111ac45'
SECTIONS=['TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY MORNING','SATURDAY AFTERNOON','SATURDAY EVENING/NIGHT','UNRESOLVED KICKOFF']
MARKET_TAG='cfb-neutral-market-v1'
DECISION_TAG='cfb-neutral-decision-v1'
MARKET_SCHEMA='CFB_NEUTRAL_MARKET_PRESENTATION_V1'
DECISION_SCHEMA='CFB_NEUTRAL_DECISION_PRESENTATION_V1'
WEEKLY_MARKET_SCHEMA='CFB_NEUTRAL_WEEKLY_MARKET_PRESENTATION_V2'
WEEKLY_DECISION_SCHEMA='CFB_NEUTRAL_WEEKLY_DECISION_PRESENTATION_V2'
# Independently recovered canonical ancestor, not a new decision or a source of outcomes.
PASS_ANCESTOR='0ed8166d1cbeab88d6e9ec5259a0c033de1f90db'
PASS_ANCESTOR_CHARS=119941
HISTORICAL_PASS_TIMES={
 '401871067':'2026-10-13T18:04:00Z', '401871053':'2026-10-13T18:04:00Z',
 '401871054':'2026-10-14T18:00:00Z', '401871068':'2026-10-14T18:00:00Z',
 '401862800':'2026-10-15T01:16:00Z', '401860923':'2026-10-15T01:16:00Z',
 '401869950':'2026-10-15T18:00:00Z'}
CT=ZoneInfo('America/Chicago')

def keys(value,expected):
    if not isinstance(value,dict) or set(value)!=set(expected):raise ValueError('unsupported/missing schema fields')
def text(value):
    if not isinstance(value,str) or not value.strip() or any(ord(c)<32 for c in value) or any(c in value for c in '|`<>'):
        raise ValueError('invalid single-line presentation text')
    return value
def number(value,price=False):
    if value is None:return
    if isinstance(value,bool) or not isinstance(value,(int,float)) or not math.isfinite(value):raise ValueError('invalid quote number')
    if price and (not isinstance(value,int) or abs(value)<100):raise ValueError('invalid American price')
def url(value):
    text(value)
    if not re.fullmatch(r'https://[^\s/]+/[^\s]*',value):raise ValueError('source URL required')
def selected_block(content,tag,schema,as_of):
    markers=re.findall(r'^```'+tag+r'[ \t]*$',content,re.M)
    blocks=list(re.finditer(r'^```'+tag+r'[ \t]*\n(.*?)^```[ \t]*$',content,re.M|re.S))
    if not blocks or len(markers)!=len(blocks):raise ValueError('missing/incomplete canonical presentation block')
    prior=None; result=None; cycles=set()
    for m in blocks:
        r=json.loads(m.group(1),object_pairs_hook=unique)
        keys(r,['schema','cycle_id','as_of_utc','rows'])
        if r['schema'] not in ((schema,) if isinstance(schema,str) else schema):raise ValueError('unknown schema')
        at=clock(r['as_of_utc'])
        if at>as_of or (prior and at<=prior):raise ValueError('future/reversed canonical clock')
        cycle_pattern=r'(?:CFB_MARKET_MONITOR|CFB_PRESENTATION_RECONCILIATION)_\d{8}T\d{6}Z' if r['schema'] in (WEEKLY_MARKET_SCHEMA,WEEKLY_DECISION_SCHEMA) else r'CFB_MARKET_MONITOR_\d{8}T\d{6}Z'
        if not re.fullmatch(cycle_pattern,r['cycle_id']):raise ValueError('unsupported cycle identity')
        if r['cycle_id'] in cycles:raise ValueError('duplicate canonical cycle')
        cycles.add(r['cycle_id'])
        if clock(datetime.strptime(r['cycle_id'].split('_')[-1],'%Y%m%dT%H%M%SZ').replace(tzinfo=timezone.utc).isoformat())>at:
            raise ValueError('cycle start after source boundary')
        if not isinstance(r['rows'],list):raise ValueError('rows must be list')
        if result is not None and r['schema'] in (MARKET_SCHEMA,WEEKLY_MARKET_SCHEMA):
            old={x['game_id']:x for x in result['rows']};new={x['game_id']:x for x in r['rows']}
            if set(old)!=set(new):raise ValueError('canonical history identity union changed')
            for gid,x in new.items():
                if old[gid]['first'] is not None and x['first']!=old[gid]['first']:raise ValueError('earliest observation rewritten')
                if old[gid]['first'] is None and x['first'] is not None and clock(x['first']['retrieved_at'])<=prior:
                    raise ValueError('hindsight first-observation backfill')
                old_last=old[gid]['current'] or old[gid]['retained'];new_last=x['current'] or x['retained']
                if old_last is not None:
                    if new_last is None:raise ValueError('latest historical observation lost')
                    if x['current'] is None and new_last!=old_last and not (r['schema']==WEEKLY_MARKET_SCHEMA and clock(new_last['retrieved_at'])>clock(old_last['retrieved_at'])):raise ValueError('unavailable update must retain prior latest observation')
                    old_at=clock(old_last['retrieved_at']);new_at=clock(new_last['retrieved_at'])
                    if new_at<old_at or (new_at==old_at and new_last!=old_last):raise ValueError('latest observation rewritten or chronology reversed')
        if result is not None and r['schema']==WEEKLY_DECISION_SCHEMA:
            old={x['game_id']:x for x in result['rows']}
            for x in r['rows']:
                if x['game_id'] in old and old[x['game_id']]['state']=='PASS':
                    if x['state']!='PASS':raise ValueError('closed PASS reopened')
                    for k in ('state_recorded_at_utc','state_evidence'):
                        if k in old[x['game_id']] and x[k]!=old[x['game_id']][k]:raise ValueError('PASS evidence rewritten')
        if result is not None and result['schema'] in (WEEKLY_MARKET_SCHEMA,WEEKLY_DECISION_SCHEMA) and r['schema'] in (MARKET_SCHEMA,DECISION_SCHEMA):raise ValueError('weekly schema downgrade')
        prior=at;result=r
    # The typed block closes the canonical surface's current presentation boundary.
    if content[blocks[-1].end():].strip():raise ValueError('untyped canonical tail requires reconciliation')
    return result

def offer(value,as_of,kickoff,weekly=False):
    if value is None:return
    keys(value,['book','source_type','source_url','event_id','retrieved_at','retrieval_precision','offer_updated_at','execution','away_spread','away_spread_price','home_spread','home_spread_price','away_ml','home_ml','over_total','over_price','under_total','under_price'])
    text(value['book']);url(value['source_url']);text(value['event_id'])
    if value['source_type'] not in ('IDENTIFIED_SINGLE_BOOK_FALLBACK','UNIDENTIFIED_MIXED_BOOK_FALLBACK') or value['retrieval_precision'] not in (('EXACT','MINUTE','RECOVERED_BY') if weekly else ('EXACT','MINUTE')):
        raise ValueError('unsupported source role/clock precision')
    at=clock(value['retrieved_at'])
    if at>as_of or (kickoff is not None and at>=kickoff):raise ValueError('future/postkickoff quote in pregame schema')
    if value['offer_updated_at'] is not None or value['execution']!='UNVERIFIED':raise ValueError('unsupported offer/execution certification')
    for k in ['away_spread','home_spread','away_ml','home_ml','over_total','under_total','away_spread_price','home_spread_price','over_price','under_price']:
        number(value[k],k.endswith('price') or k.endswith('_ml'))
    for n,p in [('away_spread','away_spread_price'),('home_spread','home_spread_price'),('over_total','over_price'),('under_total','under_price')]:
        if (value[n] is None)!=(value[p] is None):raise ValueError('partial line/price pair')
    for k in ['over_total','under_total']:
        if value[k] is not None and value[k]<=0:raise ValueError('invalid total')
    a,h=value['away_spread'],value['home_spread']
    if a is not None and h is not None and a!=-h and value['source_type']=='IDENTIFIED_SINGLE_BOOK_FALLBACK':raise ValueError('asymmetric single-book spread conflict')
    am,hm=value['away_ml'],value['home_ml']
    if a is not None and a!=0 and am is not None and hm is not None:
        if (a<0 and am>hm) or (a>0 and am<hm):raise ValueError('spread/moneyline direction conflict')

def fmt(n):return '—' if n is None else f'{n:g}'
def price(n):return '—' if n is None else f'{n:+d}'
def quote(o):
    return ('away '+fmt(o['away_spread'])+' '+price(o['away_spread_price'])+', ML '+price(o['away_ml'])+'; home '+fmt(o['home_spread'])+' '+price(o['home_spread_price'])+', ML '+price(o['home_ml'])+'; o'+fmt(o['over_total'])+' '+price(o['over_price'])+' / u'+fmt(o['under_total'])+' '+price(o['under_price']))
def source(o):return o['book']+(' single-book fallback' if o['source_type']=='IDENTIFIED_SINGLE_BOOK_FALLBACK' else ' mixed-book fallback, constituents unidentified')+(' response recovered by ' if o['retrieval_precision']=='RECOVERED_BY' else ' retrieved ')+o['retrieved_at']+' ('+o['retrieval_precision']+' precision) — '+quote(o)+'; offer-update UNKNOWN; execution UNVERIFIED; '+o['source_url']

def state_evidence(row,packet,content,kickoff,now):
    recorded=clock(row['state_recorded_at_utc']);proof=row['state_evidence']
    if recorded>clock(packet['as_of_utc']) or recorded>now:raise ValueError('future state evidence')
    if proof==PASS_ANCESTOR:
        if blob(content[:PASS_ANCESTOR_CHARS])!=PASS_ANCESTOR:raise ValueError('historical decision ancestor missing/changed')
        if row['state']!='PASS' or HISTORICAL_PASS_TIMES.get(row['game_id'])!=row['state_recorded_at_utc']:raise ValueError('unqualified historical PASS evidence')
    else:
        origins=[json.loads(m.group(1),object_pairs_hook=unique) for m in re.finditer(r'^```'+DECISION_TAG+r'[ \t]*\n(.*?)^```[ \t]*$',content,re.M|re.S)]
        origins=[p for p in origins if p['schema']==WEEKLY_DECISION_SCHEMA and p['cycle_id']==proof]
        if len(origins)!=1:raise ValueError('state evidence origin missing/ambiguous')
        origin=origins[0];matches=[r for r in origin['rows'] if r['game_id']==row['game_id']]
        if len(matches)!=1 or any(matches[0][k]!=row[k] for k in ('state','state_recorded_at_utc','state_evidence')):raise ValueError('state evidence origin mismatch')
        cycle_at=clock(datetime.strptime(proof.split('_')[-1],'%Y%m%dT%H%M%SZ').replace(tzinfo=timezone.utc).isoformat())
        if not cycle_at<=recorded<=clock(origin['as_of_utc']):raise ValueError('backdated typed decision')
        if kickoff is not None and clock(origin['as_of_utc'])>=kickoff:raise ValueError('postkickoff decision reconstruction')
    if kickoff is not None and kickoff<=now:
        if row['state']!='PASS' or recorded>=kickoff:raise ValueError('elapsed game requires proved prospective PASS')

def inputs(market,decision,lineage,as_of):
    now=clock(as_of)
    if blob(lineage)!=LINEAGE_SHA:raise ValueError('unqualified original Week7 lineage')
    census=json.loads(lineage,object_pairs_hook=unique)['rows']; c={r['game_id']:r for r in census}
    if len(c)!=62:raise ValueError('original identity census mismatch')
    m=selected_block(market,MARKET_TAG,(MARKET_SCHEMA,WEEKLY_MARKET_SCHEMA),now);d=selected_block(decision,DECISION_TAG,(DECISION_SCHEMA,WEEKLY_DECISION_SCHEMA),now)
    weekly=m['schema']==WEEKLY_MARKET_SCHEMA
    if weekly!=(d['schema']==WEEKLY_DECISION_SCHEMA):raise ValueError('market/decision schema profile mismatch')
    if (m['cycle_id'],m['as_of_utc'])!=(d['cycle_id'],d['as_of_utc']):raise ValueError('market/decision boundary mismatch')
    at=clock(m['as_of_utc']);mr={};dr={}
    for r in m['rows']:
        keys(r,['game_id','kickoff_utc','kickoff_source_url','kickoff_status','first','current','current_availability','retained']+(['diagnostic'] if weekly else []))
        gid=r['game_id']
        if not isinstance(gid,str) or gid not in c or gid in mr:raise ValueError('unknown/duplicate market identity')
        status=r['kickoff_status'];kickoff=None
        if status=='UNRESOLVED':
            if r['kickoff_utc'] is not None or r['kickoff_source_url'] is not None:raise ValueError('unresolved kickoff must stay unknown')
        elif status in ('QUALIFIED','RETAINED_UNVERIFIED'):
            kickoff=clock(r['kickoff_utc']);url(r['kickoff_source_url'])
            local=kickoff.astimezone(CT)
            if not datetime(2026,10,13,tzinfo=CT)<=local<datetime(2026,10,18,tzinfo=CT):raise ValueError('outside qualified Week7 identity/week')
            if kickoff<=now and not weekly:raise ValueError('started game unsupported by pregame schema')
        else:raise ValueError('unknown kickoff qualification')
        for k in ['first','current','retained']:offer(r[k],at,kickoff,weekly)
        if weekly and r['diagnostic'] is not None:
            diag=r['diagnostic'];keys(diag,['offer','reason'])
            if diag['reason']!='SPREAD_MONEYLINE_DIRECTION_CONFLICT' or diag['offer'] is None:raise ValueError('unsupported diagnostic')
            try:offer(diag['offer'],at,kickoff,weekly)
            except ValueError as e:
                if str(e)!='spread/moneyline direction conflict':raise
            else:raise ValueError('diagnostic does not contain declared conflict')
            if r['current'] is not None or r['current_availability']!='UNAVAILABLE':raise ValueError('quarantined quote cannot be current')
        if weekly and kickoff is not None and kickoff<=now and (r['current'] is not None or r['current_availability']!='UNAVAILABLE'):raise ValueError('elapsed game cannot carry a current pregame offer')
        if r['current_availability']=='AVAILABLE':
            if r['current'] is None or r['retained'] is not None:raise ValueError('available observation requires unique current offer')
            if r['first'] is None and not weekly:raise ValueError('current offer needs first-observation ancestry')
        elif r['current_availability']=='UNAVAILABLE':
            if r['current'] is not None:raise ValueError('unavailable current offer invented')
        else:raise ValueError('unknown availability')
        history=[o for o in [r['retained'],r['current']] if o is not None]
        if history and r['first'] is None and not weekly:raise ValueError('retained/current offer lacks first observation')
        if r['first'] and any(clock(r['first']['retrieved_at'])>clock(o['retrieved_at']) for o in history):raise ValueError('first observation after later offer')
        mr[gid]=r
    for r in d['rows']:
        keys(r,['game_id','state','reason','reconciliation_utc','planning_cutoff_utc','cutoff_authority','acceptable_number','execution_window']+(['state_recorded_at_utc','state_evidence'] if weekly else []))
        gid=r['game_id']
        if not isinstance(gid,str) or gid not in c or gid in dr:raise ValueError('unknown/duplicate decision identity')
        if r['state'] not in ('INCONCLUSIVE','PASS'):raise ValueError('unsupported actionable/WAIT decision; separate qualified profile required')
        text(r['reason'])
        if r['cutoff_authority']!='UNVERIFIED' or r['acceptable_number'] is not None or r['execution_window'] is not None:raise ValueError('neutral schema cannot certify cutoff/number/execution')
        deadline=clock(r['reconciliation_utc']) if r['reconciliation_utc'] is not None else None
        if r['state']=='INCONCLUSIVE' and (deadline is None or deadline<=now):raise ValueError('missing/overdue INCONCLUSIVE reconciliation; prospective decision required')
        k=clock(mr[gid]['kickoff_utc']) if gid in mr and mr[gid]['kickoff_utc'] is not None else None
        if weekly:
            state_evidence(r,d,decision,k,now)
        if deadline and k and deadline>=k:raise ValueError('reconciliation cannot wait until kickoff')
        if r['planning_cutoff_utc'] is not None:
            cut=clock(r['planning_cutoff_utc'])
            if k and cut>=k:raise ValueError('unverified planning cutoff reaches kickoff')
        dr[gid]=r
    if set(mr)!=set(c) or set(dr)!=set(c):raise ValueError('full market/decision/census union required')
    return m,d,c,mr,dr

def render(market,decision,execution,scorecard,lineage,as_of):
    m,d,c,mr,dr=inputs(market,decision,lineage,as_of);groups={s:[] for s in SECTIONS}
    for gid in c:
        x=mr[gid];y=dr[gid];kick=x['kickoff_utc']
        if kick is None:section='UNRESOLVED KICKOFF';display='UNRESOLVED'
        else:
            ct=clock(kick).astimezone(CT);day=ct.strftime('%A').upper()
            section=day if day!='SATURDAY' else 'SATURDAY MORNING' if ct.hour<12 else 'SATURDAY AFTERNOON' if ct.hour<17 else 'SATURDAY EVENING/NIGHT'
            display=ct.strftime('%a %b %d %-I:%M %p CT')+(' [RETAINED_UNVERIFIED]' if x['kickoff_status']=='RETAINED_UNVERIFIED' else '')
        elapsed=kick is not None and clock(kick)<=clock(as_of)
        if elapsed:display+=' [AT/PAST SAVED KICKOFF — historical PASS; no execution]'
        roles='CONSENSUS_UNAVAILABLE; Caesars UNVERIFIED; '
        current=roles+(source(x['current']) if x['current'] else 'CURRENT QUOTE UNAVAILABLE'+('; historical retained '+source(x['retained']) if x['retained'] else ''))
        if m['schema']==WEEKLY_MARKET_SCHEMA and x['diagnostic'] is not None:
            current+='; CURRENT SOURCE CONFLICT QUARANTINED — '+source(x['diagnostic']['offer'])+'; '+x['diagnostic']['reason']
        movement='No qualified first observation' if x['first'] is None else 'First '+source(x['first'])+(' → current '+source(x['current']) if x['current'] else '; no current observation, historical only')
        cutoff=('Reconcile '+y['reconciliation_utc'] if y['reconciliation_utc'] else 'Reconciliation unavailable')+'; planning cutoff '+(y['planning_cutoff_utc'] or 'UNAVAILABLE')+'; CUTOFF_AUTHORITY_UNVERIFIED'
        if m['schema']==WEEKLY_MARKET_SCHEMA:
            cutoff+='; state recorded '+y['state_recorded_at_utc']+('; source-declared minute precision' if y['state_evidence']==PASS_ANCESTOR else '')+'; evidence '+y['state_evidence']
        row=[display,c[gid]['away_team']+' @ '+c[gid]['home_team'],c[gid]['display'],current,movement,y['state'],y['reason'],cutoff,'Not established; no executable recommendation']
        groups[section].append((kick or '9999',gid,row))
    lines=['# CFB Week7 neutral source-derived Hot Sheet','', '**Presentation schema:** '+('CFB_NEUTRAL_WEEKLY_PUBLICATION_V2' if m['schema']==WEEKLY_MARKET_SCHEMA else 'CFB_NEUTRAL_PUBLICATION_V1'),'**Cycle:** '+m['cycle_id'],'**Publication boundary:** '+m['as_of_utc'],'**Scope:** canonical neutral display only; source/kickoff/execution truth and full-run completion require independent qualification.', '**Frozen-model boundary:** Original accepted FIRST_FROZEN cutoff 2026-09-26T03:47:37.497112+00:00; 51 predictions and 11 exclusions; no REFRESH substitution.',f'**Canonical inputs:** market {blob(market)}; decision {blob(decision)}; execution {blob(execution)}; scorecard {blob(scorecard)}.', '**Neutral summary:** '+str(sum(r['state']=='INCONCLUSIVE' for r in dr.values()))+' INCONCLUSIVE; '+str(sum(r['state']=='PASS' for r in dr.values()))+' PASS; no actionable recommendation; consensus unavailable; Caesars unverified; practical cutoffs unverified.','']
    for s in SECTIONS:
        lines+=['## '+s,'']
        if not groups[s]:lines+=['No governed games.',''];continue
        lines+=['| Kickoff CT | Game | Engine Prediction (Frozen) | Current qualified market / price | Movement from first observation | Decision state | Pending reason / information | Reconciliation deadline / final execution cutoff | Acceptable number / execution window |','|---|---|---|---|---|---|---|---|---|']
        for _,gid,r in sorted(groups[s]):lines+=['| '+' | '.join(r)+' |']
        lines+=['']
    lines+=['## PRIORITY WATCHLIST','','No actionable neutral-schema recommendations. See chronological rows for pending information.','','## FULL WEEKLY SLATE','','62 governed games; exactly once across chronological sections. Counts: '+json.dumps({s:len(groups[s]) for s in SECTIONS})+'.','']
    return '\n'.join(lines)

def audit(sheet,market,decision,execution,scorecard,lineage,as_of):
    expected=render(market,decision,execution,scorecard,lineage,as_of)
    if sheet!=expected:raise ValueError('publication differs from independent canonical-source rendering')
    return {'verdict':'PASS_NEUTRAL_CANONICAL_PRESENTATION_ONLY','games':62,'sheet_blob':blob(sheet),'scope':'typed neutral canonical display only; no source truth/betting/natural-run acceptance'}

def bootstrap(market,decision,lineage):
    # The first typed boundary must descend from the independently qualified
    # complete Monday legacy sources, not a self-authored packet or sheet.
    from cfb_neutral_publication_legacy_replay import normalize,MARKET_SHA,DECISION_SHA,AT
    prefixes=[];first=[]
    for content,tag,digest in [(market,MARKET_TAG,MARKET_SHA),(decision,DECISION_TAG,DECISION_SHA)]:
        m=re.search(r'^```'+tag+r'[ \t]*\n(.*?)^```[ \t]*$',content,re.M|re.S)
        if not m:raise ValueError('typed source missing for bootstrap')
        prefix=content[:m.start()]
        if blob(prefix)!=digest:
            if prefix.endswith('\n') and blob(prefix[:-1])==digest:prefix=prefix[:-1]
            else:raise ValueError('unqualified first typed source ancestry; independent bootstrap required')
        prefixes.append(prefix);first.append(json.loads(m.group(1),object_pairs_hook=unique))
    expected=normalize(*prefixes,lineage)
    base={r['game_id']:r for r in expected['market']['rows']}
    for r in first[0]['rows']:
        if r['game_id'] not in base:raise ValueError('first typed observation ancestry mismatch')
        old=base[r['game_id']]['first']
        if old is not None and r['first']!=old:raise ValueError('first typed observation ancestry mismatch')
        if old is None and r['first'] is not None and clock(r['first']['retrieved_at'])<=clock(AT):raise ValueError('bootstrap first observation hindsight-backfilled')
    return 'PASS_QUALIFIED_LEGACY_TO_TYPED_FIRST_OBSERVATION_ANCESTRY_ONLY'

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for n in ['market','decision','execution','scorecard','lineage']:p.add_argument('--'+n,required=True,type=Path)
    p.add_argument('--as-of',required=True);p.add_argument('--sheet',type=Path);p.add_argument('--render-output',type=Path)
    a=p.parse_args();values=[getattr(a,n).read_text() for n in ['market','decision','execution','scorecard','lineage']]
    if bool(a.sheet)==bool(a.render_output):p.error('choose exactly one --sheet or --render-output')
    bootstrap(values[0],values[1],values[4])
    if a.render_output:a.render_output.write_text(render(*values,a.as_of));print('RENDERED_NEUTRAL_PRESENTATION_NOT_PERSISTED')
    else:print(json.dumps(audit(a.sheet.read_text(),*values,a.as_of),indent=2))
