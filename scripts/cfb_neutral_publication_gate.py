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
CONDITIONAL_DECISION_SCHEMA='CFB_WEEKLY_CONDITIONAL_DECISION_V3'
WEEKLY_DECISION_SCHEMAS=(WEEKLY_DECISION_SCHEMA,CONDITIONAL_DECISION_SCHEMA)
# Independently recovered canonical ancestor, not a new decision or a source of outcomes.
PASS_ANCESTOR='0ed8166d1cbeab88d6e9ec5259a0c033de1f90db'
PASS_ANCESTOR_CHARS=119941
HISTORICAL_PASS_TIMES={
 '401871067':'2026-10-13T18:04:00Z', '401871053':'2026-10-13T18:04:00Z',
 '401871054':'2026-10-14T18:00:00Z', '401871068':'2026-10-14T18:00:00Z',
 '401862800':'2026-10-15T01:16:00Z', '401860923':'2026-10-15T01:16:00Z',
 '401869950':'2026-10-15T18:00:00Z'}
CT=ZoneInfo('America/Chicago')


def profile_config(profile):
    if profile == 'WEEK7':
        return {'week':7,'lineage':LINEAGE_SHA,'count':62,'predictions':51,'exclusions':11,
                'market_tag':MARKET_TAG,'decision_tag':DECISION_TAG,
                'start':datetime(2026,10,13,tzinfo=CT),'end':datetime(2026,10,18,tzinfo=CT)}
    if profile == 'WEEK8':
        return {'week':8,'lineage':'337a23b03a10617ff87d9ba8c1c224cd3ebe1d9c','count':56,'predictions':49,'exclusions':7,
                'market_tag':'cfb-week8-market-v1','decision_tag':'cfb-week8-decision-v1',
                'start':datetime(2026,10,20,tzinfo=CT),'end':datetime(2026,10,25,tzinfo=CT)}
    if profile == 'WEEK9':
        return {'week':9,'lineage':'57afbbbc65d58d9ee739bcb2823685e3fc0a5cb9','count':56,'predictions':45,'exclusions':11,
                'market_tag':'cfb-week9-market-v1','decision_tag':'cfb-week9-decision-v1',
                'start':datetime(2026,10,27,tzinfo=CT),'end':datetime(2026,11,1,tzinfo=CT)}
    raise ValueError('unqualified publication profile')

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
def selected_block(content,tag,schema,as_of,expected_ids=None):
    markers=re.findall(r'^```'+tag+r'[ \t]*$',content,re.M)
    blocks=list(re.finditer(r'^```'+tag+r'[ \t]*\n(.*?)^```[ \t]*$',content,re.M|re.S))
    if not blocks or len(markers)!=len(blocks):raise ValueError('missing/incomplete canonical presentation block')
    prior=None; result=None; cycles=set(); established_limits={}
    for m in blocks:
        r=json.loads(m.group(1),object_pairs_hook=unique)
        keys(r,['schema','cycle_id','as_of_utc','rows'])
        if r['schema'] not in ((schema,) if isinstance(schema,str) else schema):raise ValueError('unknown schema')
        at=clock(r['as_of_utc'])
        if at>as_of or (prior and at<=prior):raise ValueError('future/reversed canonical clock')
        cycle_pattern=r'(?:CFB_MARKET_MONITOR|CFB_PRESENTATION_RECONCILIATION|CFB_EVENING_AVAILABILITY)_\d{8}T\d{6}Z' if r['schema'] in (WEEKLY_MARKET_SCHEMA,)+WEEKLY_DECISION_SCHEMAS else r'CFB_MARKET_MONITOR_\d{8}T\d{6}Z'
        if not re.fullmatch(cycle_pattern,r['cycle_id']):raise ValueError('unsupported cycle identity')
        if r['cycle_id'] in cycles:raise ValueError('duplicate canonical cycle')
        cycles.add(r['cycle_id'])
        if clock(datetime.strptime(r['cycle_id'].split('_')[-1],'%Y%m%dT%H%M%SZ').replace(tzinfo=timezone.utc).isoformat())>at:
            raise ValueError('cycle start after source boundary')
        if not isinstance(r['rows'],list):raise ValueError('rows must be list')
        # Validate each historical packet before building dictionaries or
        # comparing adjacent constraints. An omitted row must never erase its
        # deadline/PASS history, and duplicates must not collapse silently.
        ids=[x.get('game_id') if isinstance(x,dict) else None for x in r['rows']]
        if any(not isinstance(gid,str) for gid in ids) or len(set(ids))!=len(ids):
            raise ValueError('unknown/duplicate canonical history identity')
        required=expected_ids if expected_ids is not None else ({x['game_id'] for x in result['rows']} if result is not None else None)
        if required is not None and set(ids)!=set(required):raise ValueError('canonical history identity union changed')
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
        if result is not None and r['schema'] in WEEKLY_DECISION_SCHEMAS:
            old={x['game_id']:x for x in result['rows']}
            for x in r['rows']:
                if x.get('state')=='CONDITIONAL' and x['game_id'] in established_limits and x.get('acceptable_number')!=established_limits[x['game_id']]:
                    raise ValueError('historical original conditional limits cannot change through PASS')
                previous=old.get(x['game_id'])
                if previous is not None:
                    # Current-cycle clocks cannot erase an earlier constraint.
                    # A separately qualified amendment profile would be needed
                    # for any later deadline; the neutral profile has none.
                    prior_deadline=previous.get('reconciliation_utc')
                    if x['state']=='INCONCLUSIVE' and prior_deadline is not None:
                        if x.get('reconciliation_utc') is None or clock(x['reconciliation_utc'])>clock(prior_deadline):raise ValueError('INCONCLUSIVE deadline extension prohibited')
                    prior_cutoff=previous.get('planning_cutoff_utc')
                    if prior_cutoff is not None:
                        if x.get('planning_cutoff_utc') is None or clock(x['planning_cutoff_utc'])>clock(prior_cutoff):raise ValueError('saved planning cutoff removal/extension prohibited')
                    if previous['state']=='CONDITIONAL':
                        if x['state'] not in ('CONDITIONAL','PASS'):raise ValueError('conditional recommendation cannot silently downgrade')
                        if x['state']=='CONDITIONAL' and x.get('acceptable_number')!=previous.get('acceptable_number'):
                            raise ValueError('original conditional number/price limits cannot change')
                if x['game_id'] in old and old[x['game_id']]['state']=='PASS':
                    if x['state']!='PASS':
                        from cfb_conditional_recommendation_profile import reconsideration
                        reconsideration(x,old[x['game_id']],r['as_of_utc'])
                    else:
                        for k in ('state_recorded_at_utc','state_evidence'):
                            if k in old[x['game_id']] and x[k]!=old[x['game_id']][k]:raise ValueError('PASS evidence rewritten')
        if result is not None and result['schema'] in (WEEKLY_MARKET_SCHEMA,)+WEEKLY_DECISION_SCHEMAS and r['schema'] in (MARKET_SCHEMA,DECISION_SCHEMA):raise ValueError('weekly schema downgrade')
        if result is not None and result['schema']==CONDITIONAL_DECISION_SCHEMA and r['schema']!=CONDITIONAL_DECISION_SCHEMA:
            raise ValueError('conditional schema downgrade')
        if r['schema'] in WEEKLY_DECISION_SCHEMAS:
            for x in r['rows']:
                if x.get('acceptable_number') is not None:
                    established_limits.setdefault(x['game_id'],x['acceptable_number'])
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

def closed_conditional(row,as_of):
    """An elapsed immutable final cutoff closes betting, not recorded history."""
    return (row['state']=='CONDITIONAL' and row.get('planning_cutoff_utc') is not None
            and clock(row['planning_cutoff_utc'])<=clock(as_of))


def conditional_boundary(row,packet,market,decision,profile):
    """Validate retained Week8/Week9 history at its genuine originating source boundary.

    Exact origin equality and ordinary validation still apply. No new/changed
    recommendation, expired renewal or current execution is authorized here.
    """
    cfg=profile_config(profile)
    if profile not in ('WEEK8','WEEK9') or not closed_conditional(row,packet['as_of_utc']):
        return packet['as_of_utc'],None
    if row['state_evidence']==packet['cycle_id']:
        raise ValueError('closed conditional cannot originate in current cycle')
    def origin(content,tag):
        matches=[json.loads(m[1],object_pairs_hook=unique) for m in re.finditer(
            r'^```'+tag+r'\n(.*?)^```[ \t]*$',content,re.M|re.S)]
        matches=[p for p in matches if p['cycle_id']==row['state_evidence']]
        if len(matches)!=1:raise ValueError('retained conditional origin missing/ambiguous')
        return matches[0]
    d=origin(decision,cfg['decision_tag']);m=origin(market,cfg['market_tag'])
    if (d['schema']!=CONDITIONAL_DECISION_SCHEMA or m['schema']!=WEEKLY_MARKET_SCHEMA
            or d['as_of_utc']!=m['as_of_utc'] or clock(d['as_of_utc'])>=clock(packet['as_of_utc'])):
        raise ValueError('retained conditional paired origin invalid')
    originals=[r for r in d['rows'] if r['game_id']==row['game_id']]
    sources=[r for r in m['rows'] if r['game_id']==row['game_id']]
    if len(originals)!=1 or originals[0]!=row or len(sources)!=1:
        raise ValueError('retained conditional differs from exact origin')
    return d['as_of_utc'],sources[0]


def state_evidence(row,packet,content,kickoff,now,decision_tag=DECISION_TAG,gaps=None):
    recorded=clock(row['state_recorded_at_utc']);proof=row['state_evidence']
    if recorded>clock(packet['as_of_utc']) or recorded>now:raise ValueError('future state evidence')
    if row['state']=='HISTORICAL_GAP':
        if gaps is None or row['game_id'] not in gaps['missing_decision_game_ids'] or row['state_recorded_at_utc']!=gaps['as_of_utc']:
            raise ValueError('unqualified historical gap')
        if kickoff is None or kickoff>recorded:raise ValueError('gap cannot replace a future decision')
        return  # Recognition of a missing decision, explicitly not pre-event evidence.
    if proof==PASS_ANCESTOR:
        if blob(content[:PASS_ANCESTOR_CHARS])!=PASS_ANCESTOR:raise ValueError('historical decision ancestor missing/changed')
        if row['state']!='PASS' or HISTORICAL_PASS_TIMES.get(row['game_id'])!=row['state_recorded_at_utc']:raise ValueError('unqualified historical PASS evidence')
    else:
        origins=[json.loads(m.group(1),object_pairs_hook=unique) for m in re.finditer(r'^```'+decision_tag+r'[ \t]*\n(.*?)^```[ \t]*$',content,re.M|re.S)]
        origins=[p for p in origins if p['schema'] in WEEKLY_DECISION_SCHEMAS and p['cycle_id']==proof]
        if len(origins)!=1:raise ValueError('state evidence origin missing/ambiguous')
        origin=origins[0];matches=[r for r in origin['rows'] if r['game_id']==row['game_id']]
        if len(matches)!=1 or any(matches[0][k]!=row[k] for k in ('state','state_recorded_at_utc','state_evidence')):raise ValueError('state evidence origin mismatch')
        if row['state']=='CONDITIONAL' and any(matches[0].get(k)!=row.get(k) for k in ('review_ref','reason','acceptable_number','reconciliation_utc','planning_cutoff_utc','cutoff_authority','execution_window')):
            raise ValueError('conditional review differs from originating decision')
        cycle_at=clock(datetime.strptime(proof.split('_')[-1],'%Y%m%dT%H%M%SZ').replace(tzinfo=timezone.utc).isoformat())
        if not cycle_at<=recorded<=clock(origin['as_of_utc']):raise ValueError('backdated typed decision')
        if kickoff is not None and clock(origin['as_of_utc'])>=kickoff:raise ValueError('postkickoff decision reconstruction')
    if kickoff is not None and kickoff<=now:
        retained=(decision_tag in (profile_config('WEEK8')['decision_tag'],profile_config('WEEK9')['decision_tag']) and closed_conditional(row,now.isoformat())
                  and proof!=packet['cycle_id'])
        if (row['state']!='PASS' and not retained) or recorded>=kickoff:raise ValueError('elapsed game requires proved prospective PASS')

def inputs(market,decision,lineage,as_of,profile='WEEK7'):
    cfg=profile_config(profile);market_tag=cfg['market_tag'];decision_tag=cfg['decision_tag']
    now=clock(as_of)
    if blob(lineage)!=cfg['lineage']:raise ValueError('unqualified original '+profile+' lineage')
    census=json.loads(lineage,object_pairs_hook=unique)['rows']; c={r['game_id']:r for r in census}
    if len(c)!=cfg['count'] or len(census)!=cfg['count']:raise ValueError('original identity census mismatch')
    m=selected_block(market,market_tag,(MARKET_SCHEMA,WEEKLY_MARKET_SCHEMA),now,set(c));d=selected_block(decision,decision_tag,(DECISION_SCHEMA,)+WEEKLY_DECISION_SCHEMAS,now,set(c))
    weekly=m['schema']==WEEKLY_MARKET_SCHEMA
    conditional=d['schema']==CONDITIONAL_DECISION_SCHEMA
    if weekly!=(d['schema'] in WEEKLY_DECISION_SCHEMAS):raise ValueError('market/decision schema profile mismatch')
    if (m['cycle_id'],m['as_of_utc'])!=(d['cycle_id'],d['as_of_utc']):raise ValueError('market/decision boundary mismatch')
    gaps=None
    if any(r.get('state')=='HISTORICAL_GAP' for r in d['rows']):
        if profile!='WEEK8' or not weekly:raise ValueError('historical gap requires qualified Week8 recovery')
        from cfb_week8_publication import bootstrap_check,recovery_context
        bootstrap_check(market,decision,lineage)
        gaps=recovery_context(market,decision,lineage)
        if gaps is None:raise ValueError('historical gap requires recovery declaration')
    if conditional:
        # A later PASS or complete packet cannot conceal an invalid earlier
        # conditional review. Validate each V3 packet at its own paired source
        # boundary, without promoting it to current source/decision truth.
        source_packets={}
        for match in re.finditer(r'^```'+market_tag+r'[ \t]*\n(.*?)^```[ \t]*$',market,re.M|re.S):
            packet=json.loads(match.group(1),object_pairs_hook=unique)
            source_packets[packet['cycle_id']]=packet
        for match in re.finditer(r'^```'+decision_tag+r'[ \t]*\n(.*?)^```[ \t]*$',decision,re.M|re.S):
            packet=json.loads(match.group(1),object_pairs_hook=unique)
            if packet['schema']!=CONDITIONAL_DECISION_SCHEMA:continue
            paired=source_packets.get(packet['cycle_id'])
            if paired is None or paired['as_of_utc']!=packet['as_of_utc'] or paired['schema']!=WEEKLY_MARKET_SCHEMA:
                raise ValueError('conditional history paired source boundary missing')
            sources={r['game_id']:r for r in paired['rows']}
            for row in packet['rows']:
                keys(row,['game_id','state','reason','reconciliation_utc','planning_cutoff_utc','cutoff_authority','acceptable_number','execution_window','state_recorded_at_utc','state_evidence','review_ref'])
                source_row=sources[row['game_id']]
                kick=clock(source_row['kickoff_utc']) if source_row['kickoff_utc'] else None
                state_evidence(row,packet,decision,kick,clock(packet['as_of_utc']),decision_tag,gaps)
                if row['state']=='CONDITIONAL':
                    from cfb_conditional_recommendation_profile import validate
                    boundary,original_source=conditional_boundary(row,packet,market,decision,profile)
                    if original_source is not None and any(source_row[k]!=original_source[k] for k in ('kickoff_utc','kickoff_source_url','kickoff_status')):
                        raise ValueError('retained conditional kickoff binding changed')
                    validate(row,original_source or source_row,c[row['game_id']],boundary,cfg['lineage'])
                elif row['state'] not in (('PASS','INCONCLUSIVE','HISTORICAL_GAP') if gaps else ('PASS','INCONCLUSIVE')) or row['review_ref'] is not None:
                    raise ValueError('unsupported conditional history state/review')
                else:
                    text(row['reason'])
                    if row['cutoff_authority']!='UNVERIFIED' or row['acceptable_number'] is not None or row['execution_window'] is not None:
                        raise ValueError('neutral history row cannot claim conditional authority')
                    if row['state']=='INCONCLUSIVE' and (row['reconciliation_utc'] is None or clock(row['reconciliation_utc'])<=clock(packet['as_of_utc'])):
                        raise ValueError('overdue historical neutral decision in conditional profile')
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
            if not cfg['start']<=local<cfg['end']:raise ValueError('outside qualified '+profile+' identity/week')
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
        keys(r,['game_id','state','reason','reconciliation_utc','planning_cutoff_utc','cutoff_authority','acceptable_number','execution_window']+(['state_recorded_at_utc','state_evidence'] if weekly else [])+(['review_ref'] if conditional else []))
        gid=r['game_id']
        if not isinstance(gid,str) or gid not in c or gid in dr:raise ValueError('unknown/duplicate decision identity')
        allowed=('INCONCLUSIVE','PASS','CONDITIONAL') if conditional else ('INCONCLUSIVE','PASS')
        if gaps:allowed+=('HISTORICAL_GAP',)
        if r['state'] not in allowed:raise ValueError('unsupported actionable/WAIT decision; separate qualified profile required')
        text(r['reason'])
        if r['state']!='CONDITIONAL':
            if r['cutoff_authority']!='UNVERIFIED' or r['acceptable_number'] is not None or r['execution_window'] is not None:raise ValueError('neutral schema cannot certify cutoff/number/execution')
            if conditional and r['review_ref'] is not None:raise ValueError('neutral decision cannot carry a conditional review')
        deadline=clock(r['reconciliation_utc']) if r['reconciliation_utc'] is not None else None
        if r['state']=='INCONCLUSIVE' and (deadline is None or deadline<=now):raise ValueError('missing/overdue INCONCLUSIVE reconciliation; prospective decision required')
        k=clock(mr[gid]['kickoff_utc']) if gid in mr and mr[gid]['kickoff_utc'] is not None else None
        if weekly:
            state_evidence(r,d,decision,k,now,decision_tag,gaps)
        if r['state']=='CONDITIONAL':
            from cfb_conditional_recommendation_profile import validate
            boundary,original_source=conditional_boundary(r,d,market,decision,profile)
            validate(r,original_source or mr[gid],c[gid],boundary,cfg['lineage'])
        if deadline and k and deadline>=k:raise ValueError('reconciliation cannot wait until kickoff')
        if r['planning_cutoff_utc'] is not None:
            cut=clock(r['planning_cutoff_utc'])
            if k and cut>=k:raise ValueError('unverified planning cutoff reaches kickoff')
        dr[gid]=r
    if set(mr)!=set(c) or set(dr)!=set(c):raise ValueError('full market/decision/census union required')
    return m,d,c,mr,dr

def render(market,decision,execution,scorecard,lineage,as_of,profile='WEEK7'):
    cfg=profile_config(profile)
    m,d,c,mr,dr=inputs(market,decision,lineage,as_of,profile);groups={s:[] for s in SECTIONS}
    conditional=d['schema']==CONDITIONAL_DECISION_SCHEMA
    for gid in c:
        x=mr[gid];y=dr[gid];kick=x['kickoff_utc']
        if kick is None:section='UNRESOLVED KICKOFF';display='UNRESOLVED'
        else:
            ct=clock(kick).astimezone(CT);day=ct.strftime('%A').upper()
            section=day if day!='SATURDAY' else 'SATURDAY MORNING' if ct.hour<12 else 'SATURDAY AFTERNOON' if ct.hour<17 else 'SATURDAY EVENING/NIGHT'
            display=ct.strftime('%a %b %d %-I:%M %p CT')+(' [RETAINED_UNVERIFIED]' if x['kickoff_status']=='RETAINED_UNVERIFIED' else '')
        elapsed=kick is not None and clock(kick)<=clock(as_of)
        if elapsed and y['state']=='CONDITIONAL':display+=' [AT/PAST SAVED KICKOFF — retained conditional history; execution tracked separately]'
        elif elapsed:display+=(' [MISSED PRE-EVENT DECISION — permanent history gap; no execution]' if y['state']=='HISTORICAL_GAP' else ' [AT/PAST SAVED KICKOFF — historical PASS; no execution]')
        roles='CONSENSUS_UNAVAILABLE; Caesars UNVERIFIED; '
        current=roles+(source(x['current']) if x['current'] else 'CURRENT QUOTE UNAVAILABLE'+('; historical retained '+source(x['retained']) if x['retained'] else ''))
        if m['schema']==WEEKLY_MARKET_SCHEMA and x['diagnostic'] is not None:
            current+='; CURRENT SOURCE CONFLICT QUARANTINED — '+source(x['diagnostic']['offer'])+'; '+x['diagnostic']['reason']
        movement='No qualified first observation' if x['first'] is None else 'First '+source(x['first'])+(' → current '+source(x['current']) if x['current'] else '; no current observation, historical only')
        cutoff=('Reconcile '+y['reconciliation_utc'] if y['reconciliation_utc'] else 'Reconciliation unavailable')+'; planning cutoff '+(y['planning_cutoff_utc'] or 'UNAVAILABLE')+'; CUTOFF_AUTHORITY_UNVERIFIED'
        if m['schema']==WEEKLY_MARKET_SCHEMA:
            cutoff+='; state recorded '+y['state_recorded_at_utc']+('; source-declared minute precision' if y['state_evidence']==PASS_ANCESTOR else '')+'; evidence '+y['state_evidence']
        model_display=c[gid]['display'].replace('|','&#124;') if profile in ('WEEK8','WEEK9') else c[gid]['display']
        row=[display,c[gid]['away_team']+' @ '+c[gid]['home_team'],model_display,current,movement,y['state'],y['reason'],cutoff,'Not established; no executable recommendation']
        if y['state']=='CONDITIONAL':
            from cfb_conditional_recommendation_profile import display as conditional_display
            boundary,original_source=conditional_boundary(y,d,market,decision,profile)
            row[8],reference_context=conditional_display(y,original_source or x,c[gid],boundary,cfg['lineage'])
            row[3]=reference_context+'; Caesars NOT_CHECKED; fallback observation retained separately: '+current[len(roles):]
            row[6]='CONTROLLED BETA CONDITIONAL — '+y['reason']+'; review '+y['review_ref']['blob']
            row[7]=cutoff.replace('CUTOFF_AUTHORITY_UNVERIFIED','CUTOFF_REVIEW_EVIDENCED_NOT_EXECUTION_VERIFIED')
            if original_source is not None:
                row[5]='HISTORICAL CONDITIONAL — WINDOW CLOSED'
                row[6]='RETAINED PRE-EVENT REVIEW ONLY — '+y['reason']+'; original review '+y['review_ref']['blob']
                row[8]='WINDOW CLOSED; no new wager or chase; original limits retained in history; execution tracked separately'
                row[3]='HISTORICAL REVIEW REFERENCE at '+boundary+'; '+row[3]
        groups[section].append((kick or '9999',gid,row))
    lines=[f"# CFB Week{cfg['week']} neutral source-derived Hot Sheet",'', '**Presentation schema:** '+('CFB_NEUTRAL_WEEKLY_PUBLICATION_V2' if m['schema']==WEEKLY_MARKET_SCHEMA else 'CFB_NEUTRAL_PUBLICATION_V1'),'**Cycle:** '+m['cycle_id'],'**Publication boundary:** '+m['as_of_utc'],'**Scope:** canonical neutral display only; source/kickoff/execution truth and full-run completion require independent qualification.', f"**Frozen-model boundary:** Original accepted FIRST_FROZEN cutoff 2026-09-26T03:47:37.497112+00:00; {cfg['predictions']} predictions and {cfg['exclusions']} exclusions; no REFRESH substitution.",f'**Canonical inputs:** market {blob(market)}; decision {blob(decision)}; execution {blob(execution)}; scorecard {blob(scorecard)}.', '**Neutral summary:** '+str(sum(r['state']=='INCONCLUSIVE' for r in dr.values()))+' INCONCLUSIVE; '+str(sum(r['state']=='PASS' for r in dr.values()))+' PASS; no actionable recommendation; consensus unavailable; Caesars unverified; practical cutoffs unverified.','']
    if conditional:
        lines[0]=f"# CFB Week{cfg['week']} source-derived conditional Hot Sheet"
        lines[2]='**Presentation schema:** CFB_WEEKLY_CONDITIONAL_PUBLICATION_V3'
        lines[5]='**Scope:** canonical conditional display from immutable prospective review; no verified venue offer, automatic bet or full-run acceptance.'
        lines[8]='**Decision summary:** '+str(sum(r['state']=='INCONCLUSIVE' for r in dr.values()))+' INCONCLUSIVE; '+str(sum(r['state']=='PASS' for r in dr.values()))+' PASS; '+str(sum(r['state']=='CONDITIONAL' for r in dr.values()))+' CONDITIONAL; venue confirmation separate; no recorded execution created.'
    closed_count=sum(profile in ('WEEK8','WEEK9') and closed_conditional(r,as_of) for r in dr.values())
    if closed_count:lines+=['**Closed conditional history:** '+str(closed_count)+' retained pre-event reviews; windows closed; excluded from current opportunities; actual executions remain separately recorded.','']
    gap_count=sum(r['state']=='HISTORICAL_GAP' for r in dr.values())
    if gap_count:lines+=['**Permanent coverage gaps:** '+str(gap_count)+' HISTORICAL_GAP; missing pre-event decisions, never PASS or recommendations. Remaining research and natural delivery are not certified by this display.','']
    section_order=SECTIONS
    if m['schema']==WEEKLY_MARKET_SCHEMA:
        active=[s for s in SECTIONS if any(dr[gid]['state'] not in ('PASS','HISTORICAL_GAP') and not (profile in ('WEEK8','WEEK9') and closed_conditional(dr[gid],as_of)) for _,gid,_ in groups[s])]
        primary=active[0] if active else 'NONE'
        lines+=['**Primary section:** '+primary+' — '+('earliest open neutral decision section; saved kickoff qualification labels remain applicable' if active else 'no open neutral decisions; all governed games remain visible below'), '']
        section_order=active+[s for s in SECTIONS if s not in active]
    for s in section_order:
        lines+=['## '+s,'']
        if not groups[s]:lines+=['No governed games.',''];continue
        lines+=['| Kickoff CT | Game | Engine Prediction (Frozen) | Current qualified market / price | Movement from first observation | Decision state | Pending reason / information | Reconciliation deadline / final execution cutoff | Acceptable number / execution window |','|---|---|---|---|---|---|---|---|---|']
        for _,gid,r in sorted(groups[s]):lines+=['| '+' | '.join(r)+' |']
        lines+=['']
    watchlist='Conditional recommendations are shown in their chronological rows; all original limits apply; venue confirmation pending.' if conditional and any(r['state']=='CONDITIONAL' and not (profile in ('WEEK8','WEEK9') and closed_conditional(r,as_of)) for r in dr.values()) else 'No actionable neutral-schema recommendations. See chronological rows for pending information.'
    lines+=['## PRIORITY WATCHLIST','',watchlist,'','## FULL WEEKLY SLATE','',str(cfg['count'])+' governed games; exactly once across chronological sections. Counts: '+json.dumps({s:len(groups[s]) for s in SECTIONS})+'.','']
    return '\n'.join(lines)

def audit(sheet,market,decision,execution,scorecard,lineage,as_of,profile='WEEK7'):
    expected=render(market,decision,execution,scorecard,lineage,as_of,profile)
    if sheet!=expected:raise ValueError('publication differs from independent canonical-source rendering')
    conditional='**Presentation schema:** CFB_WEEKLY_CONDITIONAL_PUBLICATION_V3' in sheet.splitlines()
    return {'verdict':'PASS_CONDITIONAL_CANONICAL_PRESENTATION_ONLY' if conditional else 'PASS_NEUTRAL_CANONICAL_PRESENTATION_ONLY','games':profile_config(profile)['count'],'sheet_blob':blob(sheet),'scope':'typed canonical display only; no source truth/betting/natural-run acceptance' if conditional else 'typed neutral canonical display only; no source truth/betting/natural-run acceptance'}

def bootstrap(market,decision,lineage,profile='WEEK7'):
    profile_config(profile)
    if profile == 'WEEK9':
        from cfb_week9_publication import bootstrap_check
        return bootstrap_check(market,decision,lineage)
    if profile == 'WEEK8':
        from cfb_week8_publication import bootstrap_check
        return bootstrap_check(market,decision,lineage)
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
    p.add_argument('--profile',choices=('WEEK7','WEEK8','WEEK9'),default='WEEK7')
    p.add_argument('--as-of',required=True);p.add_argument('--sheet',type=Path);p.add_argument('--render-output',type=Path)
    a=p.parse_args();values=[getattr(a,n).read_text() for n in ['market','decision','execution','scorecard','lineage']]
    if bool(a.sheet)==bool(a.render_output):p.error('choose exactly one --sheet or --render-output')
    bootstrap(values[0],values[1],values[4],a.profile)
    if a.render_output:a.render_output.write_text(render(*values,a.as_of,a.profile));print('RENDERED_NEUTRAL_PRESENTATION_NOT_PERSISTED')
    else:print(json.dumps(audit(a.sheet.read_text(),*values,a.as_of,a.profile),indent=2))
