"""Explicit Week8 original-lineage bootstrap/compiler; proposals only, never writes.

Retained source reconciliation is not a historical decision or scheduled replay.
The caller supplies independently earned decisions and a genuine fresh response.
"""
import argparse,copy,json,re
from pathlib import Path
import cfb_neutral_publication_gate as gate
from cfb_cbs_full_board_normalizer import normalize,WEEK8_URL,WEEK8_LINEAGE_SHA
from cfb_neutral_weekly_reconciliation import board_offer
from cfb_neutral_publication_legacy_replay import packet

PROFILE='WEEK8'
CFG=gate.profile_config(PROFILE)
MARKET_TAG=CFG['market_tag'];DECISION_TAG=CFG['decision_tag']
ROOT=Path(__file__).resolve().parents[1]
MARKET_PARENT='87d735251e328226087daa9aa1519c22c702a762'
DECISION_PARENT='65b87247a18060069402d9814692ab57ce97dcf3'
SOURCE_TAG='cfb-week8-source-bootstrap-v1'
RETAINED=[
 ('20261018T120200Z','486fa6993331a338c36ab52690a7e1952a122c99','2026-10-18T12:02:00Z'),
 ('20261018T175907Z','68ec244bd982d0822930746de52a13b8b4ba7543','2026-10-18T17:59:07Z'),
 ('20261019T120920Z','d7e942153d04e4131543c8b1b4c6f3683db17b96','2026-10-19T12:09:20Z'),
 ('20261019T180057Z','d4491d759b0ed0e8954344d2fa77a58682c35da4','2026-10-19T18:00:57Z')]


def board(capture,lineage,recovered_by):
    return normalize(capture,lineage,recovered_by,source_url=WEEK8_URL,profile=PROFILE)


def source_offer(game,at):
    offer=board_offer(game,at);offer['source_url']=WEEK8_URL
    if all(offer[k] is None for k in ('away_spread','home_spread','away_ml','home_ml','over_total','under_total')):return None
    return offer


def apply(row,quote,at):
    kick=gate.clock(row['kickoff_utc']) if row['kickoff_utc'] else None
    previous=row['current'] or row['retained']
    if quote is None:
        row.update(current=None,current_availability='UNAVAILABLE',retained=previous,diagnostic=None)
        return
    try:gate.offer(quote,gate.clock(at),kick,True)
    except ValueError as exc:
        if str(exc)!='spread/moneyline direction conflict':raise
        row.update(current=None,current_availability='UNAVAILABLE',retained=previous,
                   diagnostic={'offer':quote,'reason':'SPREAD_MONEYLINE_DIRECTION_CONFLICT'})
    else:
        if row['first'] is None:row['first']=copy.deepcopy(quote)
        elapsed=kick is not None and kick<=gate.clock(at)
        row.update(current=None if elapsed else quote,current_availability='UNAVAILABLE' if elapsed else 'AVAILABLE',
                   retained=quote if elapsed else None,diagnostic=None)


def retained_rows(lineage,loader=None):
    loader=loader or (lambda path:(ROOT/path).read_text())
    rows=None;refs=[]
    for stamp,digest,at in RETAINED:
        path='evidence/operational/CFB_CBS_WEEK8_FULL_BOARD_TABLES_'+stamp+'.md'
        raw=loader(path)
        if gate.blob(raw)!=digest:raise ValueError('retained capture byte identity mismatch')
        parsed=board(raw,lineage,at)
        if rows is None:
            rows={g['game_id']:{'game_id':g['game_id'],'kickoff_utc':g['source_kickoff_utc'],
                  'kickoff_source_url':WEEK8_URL,'kickoff_status':'RETAINED_UNVERIFIED',
                  'first':None,'current':None,'current_availability':'UNAVAILABLE','retained':None,'diagnostic':None}
                  for g in parsed['games']}
        for g in parsed['games']:
            row=rows[g['game_id']]
            if g['source_kickoff_utc'] is None:raise ValueError('bootstrap requires explicit source kickoff')
            row['kickoff_utc']=g['source_kickoff_utc']
            apply(row,source_offer(g,at),at)
        refs.append({'path':path,'blob':digest,'recovered_by':at})
    return rows,refs


def first_packet(content,tag):
    matches=list(re.finditer(r'^```'+tag+r'\n(.*?)^```[ \t]*$',content,re.M|re.S))
    if not matches:raise ValueError('missing Week8 packet')
    return content[:matches[0].start()],json.loads(matches[0][1],object_pairs_hook=gate.unique)


def bootstrap_check(market,decision,lineage):
    if gate.blob(lineage)!=WEEK8_LINEAGE_SHA:raise ValueError('unqualified Week8 original lineage')
    expected,refs=retained_rows(lineage)
    for content,tag,parent,is_market in ((market,MARKET_TAG,MARKET_PARENT,True),(decision,DECISION_TAG,DECISION_PARENT,False)):
        prefix,first=first_packet(content,tag)
        marker=list(re.finditer(r'^```'+SOURCE_TAG+r'\n(.*?)^```[ \t]*$',prefix,re.M|re.S))
        if len(marker)!=1:raise ValueError('unique qualified Week8 bootstrap declaration required')
        m=marker[0];prior=prefix[:m.start()]
        if gate.blob(prior)!=parent:raise ValueError('Week7 parent bytes changed or unqualified cross-week prefix')
        declaration=json.loads(m[1],object_pairs_hook=gate.unique)
        if declaration!={'profile':PROFILE,'original_lineage_blob':WEEK8_LINEAGE_SHA,'retained_sources':refs}:
            raise ValueError('bootstrap source/lineage declaration mismatch')
        if prefix[m.end():].strip():raise ValueError('untyped Week8 bootstrap tail')
        if gate.clock(first['as_of_utc'])<gate.clock(RETAINED[-1][2]):raise ValueError('bootstrap predates retained sources')
        ids=[r.get('game_id') for r in first['rows']]
        if len(ids)!=56 or set(ids)!=set(expected):raise ValueError('bootstrap population mismatch')
        if is_market:
            for row in first['rows']:
                known=expected[row['game_id']]['first'];actual=row.get('first')
                if known is not None and actual!=known:
                    raise ValueError('earliest retained observation rewritten or lost')
                if known is None and actual is not None and gate.clock(actual['retrieved_at'])<=gate.clock(RETAINED[-1][2]):
                    raise ValueError('unknown first observation cannot be hindsight backfilled')
    return 'PASS_WEEK8_ORIGINAL_AND_RETAINED_SOURCE_BOOTSTRAP_ONLY'


def compile(market,decision,capture,lineage,cycle,as_of,recovered_by,decision_rows):
    """Create full append-only proposals; caller earns every decision/source fact."""
    now=gate.clock(as_of);source_at=gate.clock(recovered_by)
    if not 0<=(now-source_at).total_seconds()<=900:raise ValueError('fresh source must be recovered within fifteen minutes of proposal')
    parsed=board(capture,lineage,recovered_by)
    prior=None
    if re.search(r'^```'+MARKET_TAG+r'$',market,re.M):
        bootstrap_check(market,decision,lineage)
        saved=gate.selected_block(market,MARKET_TAG,gate.WEEKLY_MARKET_SCHEMA,now)
        prior=gate.inputs(market,decision,lineage,saved['as_of_utc'],PROFILE)
        rows={gid:copy.deepcopy(row) for gid,row in prior[3].items()}
        if source_at<=gate.clock(prior[0]['as_of_utc']):raise ValueError('source must advance current boundary')
        pm,pd=market,decision
    else:
        if gate.blob(market)!=MARKET_PARENT or gate.blob(decision)!=DECISION_PARENT:
            raise ValueError('unqualified Week7-to-Week8 parent')
        if any(g['temporal_status']!='FUTURE_AT_CAPTURE' for g in parsed['games']):raise ValueError('initial Week8 bootstrap cannot reconstruct elapsed decisions')
        rows,refs=retained_rows(lineage)
        if source_at<gate.clock(RETAINED[-1][2]):raise ValueError('new source before retained source boundary')
        root=packet({'profile':PROFILE,'original_lineage_blob':WEEK8_LINEAGE_SHA,'retained_sources':refs},SOURCE_TAG)
        # packet adds a leading newline; preserve exact prior bytes as prefix.
        root=root.lstrip('\n')
        pm=market+root;pd=decision+root
    for game in parsed['games']:
        row=rows[game['game_id']]
        if game['temporal_status']!='FUTURE_AT_CAPTURE':
            if row['kickoff_utc'] is None or gate.clock(row['kickoff_utc'])>source_at:raise ValueError('elapsed source/retained kickoff conflict')
            row.update(current=None,current_availability='UNAVAILABLE',retained=row['current'] or row['retained'])
            continue
        # Source-display time never becomes independently qualified kickoff.
        if row['kickoff_status']!='QUALIFIED' or row['kickoff_utc']!=game['source_kickoff_utc']:
            row.update(kickoff_utc=game['source_kickoff_utc'],kickoff_source_url=WEEK8_URL,kickoff_status='RETAINED_UNVERIFIED')
        apply(row,source_offer(game,recovered_by),as_of)
    decisions=copy.deepcopy(decision_rows)
    conditional=any(r.get('state')=='CONDITIONAL' or 'review_ref' in r for r in decisions) or (prior is not None and prior[1]['schema']==gate.CONDITIONAL_DECISION_SCHEMA)
    for row in decisions:
        if conditional:row.setdefault('review_ref',None)
        gate.keys(row,['game_id','state','reason','reconciliation_utc','planning_cutoff_utc','cutoff_authority','acceptable_number','execution_window']+(['review_ref'] if conditional else []))
        old=prior[4].get(row['game_id']) if prior else None
        if old is not None and old['state']=='PASS' and row['state']=='PASS':
            row.update(state_recorded_at_utc=old['state_recorded_at_utc'],state_evidence=old['state_evidence'])
        else:row.update(state_recorded_at_utc=as_of,state_evidence=cycle)
    def obj(schema,rs):return {'schema':schema,'cycle_id':cycle,'as_of_utc':as_of,'rows':rs}
    pm+=packet(obj(gate.WEEKLY_MARKET_SCHEMA,list(rows.values())),MARKET_TAG).lstrip('\n')
    pd+=packet(obj(gate.CONDITIONAL_DECISION_SCHEMA if conditional else gate.WEEKLY_DECISION_SCHEMA,decisions),DECISION_TAG).lstrip('\n')
    bootstrap_check(pm,pd,lineage);gate.inputs(pm,pd,lineage,as_of,PROFILE)
    return pm,pd


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    for key in ('market','decision','capture','lineage','decision_rows','output_market','output_decision'):
        parser.add_argument('--'+key.replace('_','-'),required=True,type=Path)
    for key in ('cycle_id','as_of','recovered_by'):parser.add_argument('--'+key.replace('_','-'),required=True)
    a=parser.parse_args();inputs=(a.market,a.decision,a.capture,a.lineage,a.decision_rows)
    outputs=(a.output_market,a.output_decision)
    if len({p.resolve() for p in outputs})!=2 or any(p.resolve() in {q.resolve() for q in inputs} for p in outputs):parser.error('distinct proposal outputs must not overwrite inputs')
    pm,pd=compile(*(p.read_text() for p in inputs[:4]),a.cycle_id,a.as_of,a.recovered_by,json.loads(a.decision_rows.read_text(),object_pairs_hook=gate.unique))
    for p,s in zip(outputs,(pm,pd)):p.write_text(s)
    print(json.dumps({'status':'VALIDATED_WEEK8_PROPOSALS_ONLY_NOT_PERSISTED','market_blob':gate.blob(pm),'decision_blob':gate.blob(pd),'games':56,'predictions':49,'exclusions':7}))
