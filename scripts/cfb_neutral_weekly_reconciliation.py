"""One qualified saved-source transition to full-week typed records; no writes or dispatch.

This is a bootstrap QA adapter for exact October 15 canonical evidence, not a
future source collector. Future cycles must supply their own fresh typed rows.
"""
import argparse, copy, json, re
from pathlib import Path
import cfb_neutral_publication_gate as gate
from cfb_cbs_full_board_normalizer import normalize, URL
from cfb_neutral_publication_legacy_replay import parse_quote, packet, block, pair as legacy_pair

def pair(game):
    return tuple('App State' if n=='Appalachian State' else n for n in legacy_pair(game))

MARKET='05ccbf405bd1d5e35a1842d718c4e45325d7bee7'
DECISION=gate.PASS_ANCESTOR
CAPTURE='6ff67e5c57060fde38509d09afbcaaf402cdb77d'
# Immutable source persistence bounds independently recovered from Git history.
# These are upper bounds, never exact HTTP completion or bookmaker update times.
CAPTURE_BY='2026-10-15T18:02:23Z'
EVENING_BY='2026-10-16T01:13:54Z'

def board_offer(game,recovered_by):
    a,h=game['team_offers'];av=a['spread'];hv=h['spread'];ot=a['total'];ut=h['total']
    if ot['side'] not in ('o',None) or ut['side'] not in ('u',None):raise ValueError('unknown source total side orientation')
    return {'book':'CBS Sports multi-book display','source_type':'UNIDENTIFIED_MIXED_BOOK_FALLBACK','source_url':URL,'event_id':'EVENT_ID_UNAVAILABLE','retrieved_at':recovered_by,'retrieval_precision':'RECOVERED_BY','offer_updated_at':None,'execution':'UNVERIFIED','away_spread':av['line'],'away_spread_price':av['price'],'home_spread':hv['line'],'home_spread_price':hv['price'],'away_ml':a['moneyline']['price'],'home_ml':h['moneyline']['price'],'over_total':ot['line'],'over_price':ot['price'],'under_total':ut['line'],'under_price':ut['price']}

def apply_offer(row,quote,as_of):
    old_last=row['current'] or row['retained'];kick=gate.clock(row['kickoff_utc'])
    try:gate.offer(quote,gate.clock(as_of),kick,True)
    except ValueError as e:
        if str(e)!='spread/moneyline direction conflict':raise
        row.update(current=None,current_availability='UNAVAILABLE',retained=old_last,diagnostic={'offer':quote,'reason':'SPREAD_MONEYLINE_DIRECTION_CONFLICT'})
    else:
        elapsed=kick<=gate.clock(as_of)
        row.update(current=None if elapsed else quote,current_availability='UNAVAILABLE' if elapsed else 'AVAILABLE',retained=quote if elapsed else None,diagnostic=None)

def advance(market,decision,capture,lineage,cycle,as_of,recovered_by,decision_rows):
    """Compile a fresh complete board plus producer-earned decisions, without writes.

    The caller must actually retrieve the source and supply the response recovery
    bound. This formatter cannot prove source freshness, clock truth or a decision.
    """
    gate.bootstrap(market,decision,lineage)
    m=copy.deepcopy(gate.selected_block(market,gate.MARKET_TAG,(gate.MARKET_SCHEMA,gate.WEEKLY_MARKET_SCHEMA),gate.clock(as_of)))
    d=copy.deepcopy(gate.selected_block(decision,gate.DECISION_TAG,(gate.DECISION_SCHEMA,)+gate.WEEKLY_DECISION_SCHEMAS,gate.clock(as_of)))
    if m['schema']!=gate.WEEKLY_MARKET_SCHEMA or d['schema'] not in gate.WEEKLY_DECISION_SCHEMAS:raise ValueError('weekly bootstrap required before advance')
    if not gate.clock(m['as_of_utc'])<gate.clock(recovered_by)<=gate.clock(as_of):raise ValueError('fresh source recovery must follow prior typed boundary')
    board=normalize(capture,lineage,recovered_by)
    byid={r['game_id']:r for r in m['rows']};old_decisions={r['game_id']:r for r in d['rows']}
    for game in board['games']:
        row=byid[game['game_id']]
        if game['temporal_status']=='FUTURE_AT_CAPTURE':
            if row['kickoff_status']!='QUALIFIED' or gate.clock(row['kickoff_utc'])!=gate.clock(game['source_kickoff_utc']):
                row.update(kickoff_utc=game['source_kickoff_utc'],kickoff_source_url=URL,kickoff_status='RETAINED_UNVERIFIED')
            apply_offer(row,board_offer(game,recovered_by),as_of)
        else:
            if row['kickoff_utc'] is None or gate.clock(row['kickoff_utc'])>gate.clock(recovered_by):raise ValueError('source/retained kickoff conflict requires qualification')
            row.update(current=None,current_availability='UNAVAILABLE',retained=row['current'] or row['retained'])
    d['rows']=copy.deepcopy(decision_rows)
    conditional=d['schema']==gate.CONDITIONAL_DECISION_SCHEMA or any(r.get('state')=='CONDITIONAL' or 'review_ref' in r for r in d['rows'])
    if conditional:d['schema']=gate.CONDITIONAL_DECISION_SCHEMA
    for row in d['rows']:
        if conditional:row.setdefault('review_ref',None)
        gate.keys(row,['game_id','state','reason','reconciliation_utc','planning_cutoff_utc','cutoff_authority','acceptable_number','execution_window']+(['review_ref'] if conditional else []))
        if row['game_id'] not in old_decisions:raise ValueError('unknown decision game')
        old=old_decisions[row['game_id']]
        if old['state']=='PASS':
            if row['state']!='PASS':
                row.update(state_recorded_at_utc=as_of,state_evidence=cycle)
                from cfb_conditional_recommendation_profile import reconsideration
                reconsideration(row,old,as_of)
            else:row.update(state_recorded_at_utc=old['state_recorded_at_utc'],state_evidence=old['state_evidence'])
        else:row.update(state_recorded_at_utc=as_of,state_evidence=cycle)
    for obj in (m,d):obj.update(cycle_id=cycle,as_of_utc=as_of)
    pm=market+packet(m,gate.MARKET_TAG);pd=decision+packet(d,gate.DECISION_TAG)
    gate.inputs(pm,pd,lineage,as_of)
    return pm,pd

def latest(content, tag):
    return json.loads(re.findall(r'^```'+tag+r'\n(.*?)^```$',content,re.M|re.S)[-1])

def prose_offer(text, stamp, precision):
    text=re.sub(r'(?:source-rendered )?over ([\d.]+) \(([+-]\d+)\), under ([\d.]+) \(([+-]\d+)\)',r'o\1 \2 / u\3 \4',text)
    if 'total ' in text:
        text=re.sub(r'total ([\d.]+) \(([+-]\d+)/([+-]\d+)\)',r'o\1 \2 / u\1 \3',text)
    return parse_quote(text,stamp,'CBS Sports multi-book display','',precision)

def bullets(content, label, stamp, precision, names):
    found={}
    for line in block(content,label).splitlines():
        m=re.match(r'^- (.+? @ .+?) — (.+?)(?:\. (?:Compared|Since|Versus|First)|$)',line)
        if not m or ', ML ' not in m[2]:continue
        key=pair(m[1]);value=m[2].rstrip('.')
        if key not in names:raise ValueError('unknown directed source game')
        found[names[key]]=prose_offer(value,stamp,precision)
    return found

def build(market,decision,capture,lineage,cycle,as_of):
    if (gate.blob(market),gate.blob(decision),gate.blob(capture))!=(MARKET,DECISION,CAPTURE):
        raise ValueError('bootstrap adapter requires exact independently qualified source ancestors')
    if gate.clock(as_of)<gate.clock(EVENING_BY):raise ValueError('replay before retained evidence existed')
    gate.bootstrap(market,decision,lineage)
    m=copy.deepcopy(latest(market,gate.MARKET_TAG));d=copy.deepcopy(latest(decision,gate.DECISION_TAG))
    m.update(schema=gate.WEEKLY_MARKET_SCHEMA,cycle_id=cycle,as_of_utc=as_of)
    d.update(schema=gate.WEEKLY_DECISION_SCHEMA,cycle_id=cycle,as_of_utc=as_of)
    census=json.loads(lineage)['rows'];names={(r['away_team'],r['home_team']):r['game_id'] for r in census}
    byid={r['game_id']:r for r in m['rows']}
    # Retain the last actual pre-event priority offers for already elapsed games.
    updates={}
    updates.update(bullets(market,'Scheduled full-slate refresh — 2026-10-13 13:03 CT','2026-10-13T18:03:00Z','MINUTE',names))
    updates.update(bullets(market,'Scheduled full-slate refresh — 2026-10-14 12:58 CT','2026-10-14T17:58:01Z','EXACT',names))
    if len(updates)!=4:raise ValueError('four retained Tuesday/Wednesday observations required')
    board=normalize(capture,lineage,CAPTURE_BY)
    for r in board['games']:
        if r['temporal_status']!='FUTURE_AT_CAPTURE':continue
        updates[r['game_id']]=board_offer(r,CAPTURE_BY)
        # A date-only past source cannot invent an exact kickoff. Future page times
        # remain visibly unverified schedule evidence until independently qualified.
        byid[r['game_id']].update(kickoff_utc=r['source_kickoff_utc'],kickoff_source_url=URL,kickoff_status='RETAINED_UNVERIFIED')
    evening=bullets(market,'Thursday Evening Availability Friday refresh — 2026-10-15 20:09 CT',EVENING_BY,'RECOVERED_BY',names)
    if len(evening)!=3:raise ValueError('three evening Friday observations required')
    updates.update(evening)
    if set(updates)!=set(byid):raise ValueError('complete per-row market reconciliation required')
    for gid,r in byid.items():
        apply_offer(r,updates[gid],as_of)
    reasons={}
    # Latest current reasons come from canonical decision tables, never the view.
    for line in decision.splitlines():
        if not line.startswith('| ') or ' @ ' not in line:continue
        cells=[c.strip() for c in line.strip('|').split('|')]
        if pair(cells[0]) not in names:continue
        gid=names[pair(cells[0])]
        if len(cells)>=6 and 'INCONCLUSIVE' in cells[1]:reasons[gid]=cells[3]
    for r in d['rows']:
        gid=r['game_id']
        if gid in gate.HISTORICAL_PASS_TIMES:
            r.update(state='PASS',reason='Preserved prospective PASS / NO BET from independently qualified canonical decision ancestor; no reopening from price movement',state_recorded_at_utc=gate.HISTORICAL_PASS_TIMES[gid],state_evidence=DECISION)
        else:
            r.update(reason=reasons.get(gid,r['reason']),state_recorded_at_utc=as_of,state_evidence=cycle)
    proposed_market=market+packet(m,gate.MARKET_TAG);proposed_decision=decision+packet(d,gate.DECISION_TAG)
    gate.inputs(proposed_market,proposed_decision,lineage,as_of)
    return proposed_market,proposed_decision

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('market','decision','capture','lineage','output_market','output_decision'):p.add_argument('--'+key.replace('_','-'),type=Path,required=True)
    p.add_argument('--cycle-id',required=True);p.add_argument('--as-of',required=True)
    p.add_argument('--bootstrap-saved',action='store_true');p.add_argument('--recovered-by');p.add_argument('--decision-rows',type=Path)
    a=p.parse_args();values=[getattr(a,key).read_text() for key in ('market','decision','capture','lineage')]
    if a.bootstrap_saved:
        if a.recovered_by or a.decision_rows:p.error('bootstrap uses only the exact qualified saved ancestors')
        result=build(*values,a.cycle_id,a.as_of)
    else:
        if not a.recovered_by or not a.decision_rows:p.error('advance requires fresh recovery bound and independently earned complete decision rows')
        result=advance(*values,a.cycle_id,a.as_of,a.recovered_by,json.loads(a.decision_rows.read_text(),object_pairs_hook=gate.unique))
    for output,value,source in zip((a.output_market,a.output_decision),result,(a.market,a.decision)):
        if output.resolve() in (a.market.resolve(),a.decision.resolve(),a.capture.resolve(),a.lineage.resolve()):p.error('proposal output cannot overwrite a source')
    if a.output_market.resolve()==a.output_decision.resolve():p.error('proposal destinations must differ')
    for output,value in zip((a.output_market,a.output_decision),result):output.write_text(value)
    print(json.dumps({'status':'VALIDATED_PROPOSALS_ONLY_NOT_PERSISTED','market_blob':gate.blob(result[0]),'decision_blob':gate.blob(result[1]),'source_freshness_and_decision_truth':'CALLER_MUST_QUALIFY_INDEPENDENTLY'}))
