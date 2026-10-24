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
RECOVERY_AUTHORITY='d8a8c20cf9fe1afbb504a8474f67019dbe469fb3'
GAP_STATE='HISTORICAL_GAP'
RECOVERY_GAPS={'401871070','401871092','401871069','401871055'}
RECOVERY_NOT_BEFORE='2026-10-22T18:16:12Z'
RETAINED=[
 ('20261018T120200Z','486fa6993331a338c36ab52690a7e1952a122c99','2026-10-18T12:02:00Z'),
 ('20261018T175907Z','68ec244bd982d0822930746de52a13b8b4ba7543','2026-10-18T17:59:07Z'),
 ('20261019T120920Z','d7e942153d04e4131543c8b1b4c6f3683db17b96','2026-10-19T12:09:20Z'),
 ('20261019T180057Z','d4491d759b0ed0e8954344d2fa77a58682c35da4','2026-10-19T18:00:57Z')]


def board(capture,lineage,recovered_by,*,retained_elapsed_kickoffs=None):
    return normalize(capture,lineage,recovered_by,source_url=WEEK8_URL,profile=PROFILE,retained_elapsed_kickoffs=retained_elapsed_kickoffs)


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


def recovery_context(market,decision,lineage):
    """Authenticate the one-time gap declaration, never manufacture decisions."""
    declarations=[]
    for content,tag in ((market,MARKET_TAG),(decision,DECISION_TAG)):
        prefix,first=first_packet(content,tag)
        roots=list(re.finditer(r'^```'+SOURCE_TAG+r'\n(.*?)^```[ \t]*$',prefix,re.M|re.S))
        if len(roots)!=1:raise ValueError('unique Week8 source declaration required')
        root=json.loads(roots[0][1],object_pairs_hook=gate.unique)
        declarations.append((root.get('recovery'),first))
    a,first=declarations[0];b,decisions=declarations[1]
    if a!=b:raise ValueError('recovery declarations differ')
    if a is None:return None
    gate.keys(a,['authority_blob','as_of_utc','missing_decision_game_ids'])
    if a['authority_blob']!=RECOVERY_AUTHORITY:raise ValueError('unqualified recovery authority')
    authority=ROOT/'evidence/CFB_WEEK8_PROSPECTIVE_RECOVERY_DISPOSITION_2026-10-22.md'
    if gate.blob(authority.read_text())!=RECOVERY_AUTHORITY:raise ValueError('recovery authority bytes changed')
    if a['as_of_utc']!=first['as_of_utc'] or a['as_of_utc']!=decisions['as_of_utc']:
        raise ValueError('recovery clock differs from actual initialization')
    boundary=gate.clock(a['as_of_utc'])
    if boundary<gate.clock(RECOVERY_NOT_BEFORE):raise ValueError('recovery cannot predate user direction')
    elapsed={r['game_id'] for r in first['rows'] if r['kickoff_utc'] is not None and gate.clock(r['kickoff_utc'])<=boundary}
    ids=a['missing_decision_game_ids']
    if not isinstance(ids,list) or ids!=sorted(set(ids)) or set(ids)!=elapsed or set(ids)!=RECOVERY_GAPS:
        raise ValueError('recovery gap population differs from elapsed identities')
    initial={r['game_id']:r for r in decisions['rows']}
    for gid in ids:
        row=initial.get(gid,{})
        if row.get('state')!=GAP_STATE or row.get('state_recorded_at_utc')!=a['as_of_utc'] or row.get('state_evidence')!=decisions['cycle_id']:
            raise ValueError('gap must originate at recovery, never before kickoff')
        if any(row.get(k) is not None for k in ('reconciliation_utc','planning_cutoff_utc','acceptable_number','execution_window','review_ref')):
            raise ValueError('gap cannot claim a decision, cutoff, review or execution')
        if row.get('cutoff_authority')!='UNVERIFIED':raise ValueError('gap cannot certify authority')
        gate.text(row.get('reason'))
    for match in re.finditer(r'^```'+DECISION_TAG+r'\n(.*?)^```[ \t]*$',decision,re.M|re.S):
        packet=json.loads(match[1],object_pairs_hook=gate.unique)
        for row in packet['rows']:
            if row['game_id'] in elapsed:
                expected=initial[row['game_id']]
                if {k:v for k,v in row.items() if k!='review_ref' or v is not None}!={k:v for k,v in expected.items() if k!='review_ref' or v is not None}:
                    raise ValueError('historical gap is immutable')
            elif row.get('state')==GAP_STATE:raise ValueError('new gaps require separate disposition; no late conversion')
    return a


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
        expected_declaration={'profile':PROFILE,'original_lineage_blob':WEEK8_LINEAGE_SHA,'retained_sources':refs}
        if 'recovery' in declaration:expected_declaration['recovery']=declaration['recovery']
        if declaration!=expected_declaration:
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
    recovery_context(market,decision,lineage)
    return 'PASS_WEEK8_ORIGINAL_AND_RETAINED_SOURCE_BOOTSTRAP_ONLY'


def compile(market,decision,capture,lineage,cycle,as_of,recovered_by,decision_rows,recovery_authority=None):
    """Create full append-only proposals; caller earns every decision/source fact."""
    now=gate.clock(as_of);source_at=gate.clock(recovered_by)
    if not 0<=(now-source_at).total_seconds()<=900:raise ValueError('fresh source must be recovered within fifteen minutes of proposal')
    prior=None
    if re.search(r'^```'+MARKET_TAG+r'$',market,re.M):
        if recovery_authority is not None:raise ValueError('recovery is initial-only; cannot reset a stream')
        bootstrap_check(market,decision,lineage)
        saved=gate.selected_block(market,MARKET_TAG,gate.WEEKLY_MARKET_SCHEMA,now)
        prior=gate.inputs(market,decision,lineage,saved['as_of_utc'],PROFILE)
        rows={gid:copy.deepcopy(row) for gid,row in prior[3].items()}
        if source_at<=gate.clock(prior[0]['as_of_utc']):raise ValueError('source must advance current boundary')
        pm,pd=market,decision
    else:
        if gate.blob(market)!=MARKET_PARENT or gate.blob(decision)!=DECISION_PARENT:
            raise ValueError('unqualified Week7-to-Week8 parent')
        parsed=board(capture,lineage,recovered_by)
        elapsed=sorted(g['game_id'] for g in parsed['games'] if g['temporal_status']!='FUTURE_AT_CAPTURE')
        if elapsed and recovery_authority!=RECOVERY_AUTHORITY:raise ValueError('initial Week8 bootstrap cannot reconstruct elapsed decisions')
        if recovery_authority and set(elapsed)!=RECOVERY_GAPS:raise ValueError('recovery only covers the four declared missed identities')
        if recovery_authority is not None and (recovery_authority!=RECOVERY_AUTHORITY or not elapsed):raise ValueError('unqualified or unnecessary recovery authority')
        rows,refs=retained_rows(lineage)
        if source_at<gate.clock(RETAINED[-1][2]):raise ValueError('new source before retained source boundary')
        declaration={'profile':PROFILE,'original_lineage_blob':WEEK8_LINEAGE_SHA,'retained_sources':refs}
        if elapsed:declaration['recovery']={'authority_blob':recovery_authority,'as_of_utc':as_of,'missing_decision_game_ids':elapsed}
        root=packet(declaration,SOURCE_TAG)
        # packet adds a leading newline; preserve exact prior bytes as prefix.
        root=root.lstrip('\n')
        pm=market+root;pd=decision+root
    # Compose exact retained identity/time evidence from the authenticated prior
    # stream, never a source Final field or an invented new kickoff. Initial
    # bootstrap still has no such authority and keeps the original rejection.
    elapsed_context={gid:r['kickoff_utc'] for gid,r in rows.items()
                     if prior is not None and r['kickoff_utc'] is not None and gate.clock(r['kickoff_utc'])<source_at}
    parsed=board(capture,lineage,recovered_by,retained_elapsed_kickoffs=elapsed_context)
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
        if old is not None and old['state']==GAP_STATE:
            row.update(state_recorded_at_utc=old['state_recorded_at_utc'],state_evidence=old['state_evidence'])
        elif (old is not None and old['state']=='CONDITIONAL' and
              gate.closed_conditional(old,as_of) and
              row=={k:v for k,v in old.items() if k not in ('state_recorded_at_utc','state_evidence')}):
            # Exact closed review retention is history, never a new decision.
            row.update(state_recorded_at_utc=old['state_recorded_at_utc'],state_evidence=old['state_evidence'])
        elif old is not None and old['state']=='PASS' and row['state']=='PASS':
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
    parser.add_argument('--recovery-authority',help='Exact accepted one-time Week8 disposition blob; never permits backfill')
    a=parser.parse_args();inputs=(a.market,a.decision,a.capture,a.lineage,a.decision_rows)
    outputs=(a.output_market,a.output_decision)
    if len({p.resolve() for p in outputs})!=2 or any(p.resolve() in {q.resolve() for q in inputs} for p in outputs):parser.error('distinct proposal outputs must not overwrite inputs')
    pm,pd=compile(*(p.read_text() for p in inputs[:4]),a.cycle_id,a.as_of,a.recovered_by,json.loads(a.decision_rows.read_text(),object_pairs_hook=gate.unique),a.recovery_authority)
    for p,s in zip(outputs,(pm,pd)):p.write_text(s)
    print(json.dumps({'status':'VALIDATED_WEEK8_PROPOSALS_ONLY_NOT_PERSISTED','market_blob':gate.blob(pm),'decision_blob':gate.blob(pd),'games':56,'predictions':49,'exclusions':7}))
