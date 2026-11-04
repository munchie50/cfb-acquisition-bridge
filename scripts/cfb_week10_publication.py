"""Explicit Week10 source-rooted neutral compiler; proposals only, never writes.

The caller supplies independently recorded decisions and an actual fresh source.
Original archives are never rerun as models, and Week9 history stays byte-exact.
"""
import argparse
import copy
import json
import re
from pathlib import Path
from urllib.parse import urlparse
import cfb_neutral_publication_gate as gate
from cfb_cbs_full_board_normalizer import normalize, WEEK10_URL, WEEK10_LINEAGE_SHA as SOURCE_IDENTITY_SHA
from cfb_neutral_weekly_reconciliation import board_offer
from cfb_neutral_publication_legacy_replay import packet
from cfb_week8_publication import apply

ROOT = Path(__file__).resolve().parents[1]
PROFILE = 'WEEK10'
CFG = gate.profile_config(PROFILE)
MARKET_TAG = CFG['market_tag']
DECISION_TAG = CFG['decision_tag']
SOURCE_TAG = 'cfb-week10-source-bootstrap-v1'
MARKET_PARENT = '69caf5b1184eedccc90be7562e4a3bd7cb8b7375'
DECISION_PARENT = 'bb5a9cc83b6a1425dc2972ca84b33aa2bbbf8fa9'
FIRST_SOURCE = {
    'path': 'evidence/operational/CFB_CBS_WEEK10_LIVE_MARKDOWN_CAPTURE_20261031.md',
    'blob': '14daae1a67fd96385c321eccb3fcf828041874a0',
    'recovered_by': '2026-10-31T17:08:33Z',
}


RETAINED_SOURCES = [FIRST_SOURCE, {
    'path': 'evidence/operational/CFB_WEEK10_R90_CBS_FRESH_SOURCE_CAPTURE_20261101T173123853Z.md',
    'blob': '1b9605ef579aad8e55e2a7f116f7b817f2bb988a',
    'recovered_by': '2026-11-01T17:31:25.116Z',
}]

WEEK10_LINEAGE_SHA = '47736c0fd9ff49545db7e46b508805658a1c7a92'
RECOVERY_AUTHORITY = 'db05e58bb7c76a16837f3a2ad50804e1936951f0'
RECOVERY_PATH = 'evidence/CFB_WEEK10_ORIGINAL_LINEAGE_PUBLICATION_PROFILE_2026-11-04.md'
RECOVERY_GAPS = {'401866453', '401866454'}
RECOVERY_NOT_BEFORE = '2026-11-04T17:55:06Z'
SOURCE_IDENTITY_PATH = 'evidence/operational/CFB_WEEK10_CANDIDATE_CANONICAL_IDENTITY_BASELINE_20261031.json'


def board(capture, lineage, recovered_by, *, retained_elapsed_kickoffs=None):
    if gate.blob(lineage) != WEEK10_LINEAGE_SHA:
        raise ValueError('unqualified Week10 original lineage')
    identity = (ROOT / SOURCE_IDENTITY_PATH).read_text()
    if gate.blob(identity) != SOURCE_IDENTITY_SHA:
        raise ValueError('Week10 source identity bytes changed')
    original = {r['game_id']: r for r in json.loads(lineage)['rows']}
    baseline = json.loads(identity)['rows']
    if len(baseline) != 63 or {r['game_id'] for r in baseline} != set(original):
        raise ValueError('Week10 source/original identity union mismatch')
    for row in baseline:
        if any(row[k].replace('Hawaii', "Hawai'i") != original[row['game_id']][k]
               for k in ('away_team', 'home_team')):
            raise ValueError('Week10 source/original directed identity mismatch')
    return normalize(capture, identity, recovered_by, source_url=WEEK10_URL, profile=PROFILE,
                     retained_elapsed_kickoffs=retained_elapsed_kickoffs)


def source_offer(game, at):
    offer = board_offer(game, at)
    offer['source_url'] = WEEK10_URL
    return None if all(offer[k] is None for k in ('away_spread', 'home_spread', 'away_ml', 'home_ml', 'over_total', 'under_total')) else offer


def first_rows(lineage):
    rows = None
    for ref in RETAINED_SOURCES:
        raw = (ROOT / ref['path']).read_text()
        if gate.blob(raw) != ref['blob']:
            raise ValueError('Week10 retained source bytes changed')
        parsed = board(raw, lineage, ref['recovered_by'])
        if parsed['coverage']['future_games'] != 63:
            raise ValueError('Week10 retained source cannot reconstruct elapsed observations')
        if rows is None:
            rows = {game['game_id']: {
                'game_id': game['game_id'], 'kickoff_utc': game['source_kickoff_utc'],
                'kickoff_source_url': WEEK10_URL, 'kickoff_status': 'RETAINED_UNVERIFIED',
                'first': None, 'current': None, 'current_availability': 'UNAVAILABLE',
                'retained': None, 'diagnostic': None,
            } for game in parsed['games']}
        for game in parsed['games']:
            row = rows[game['game_id']]
            row['kickoff_utc'] = game['source_kickoff_utc']
            apply(row, source_offer(game, ref['recovered_by']), ref['recovered_by'])
    return rows


def first_packet(content,tag):
    matches=list(re.finditer(r'^```'+tag+r'\n(.*?)^```[ \t]*$',content,re.M|re.S))
    if not matches:raise ValueError('missing Week10 packet')
    return content[:matches[0].start()],json.loads(matches[0][1],object_pairs_hook=gate.unique)


def recovery_context(market,decision,lineage):
    """Authenticate the one-time gap declaration, never manufacture decisions."""
    declarations=[]
    for content,tag in ((market,MARKET_TAG),(decision,DECISION_TAG)):
        prefix,first=first_packet(content,tag)
        roots=list(re.finditer(r'^```'+SOURCE_TAG+r'\n(.*?)^```[ \t]*$',prefix,re.M|re.S))
        if len(roots)!=1:raise ValueError('unique Week10 source declaration required')
        root=json.loads(roots[0][1],object_pairs_hook=gate.unique)
        declarations.append((root.get('recovery'),first))
    a,first=declarations[0];b,decisions=declarations[1]
    if a!=b:raise ValueError('recovery declarations differ')
    if a is None:raise ValueError('Week10 initial recovery declaration required')
    gate.keys(a,['authority_blob','as_of_utc','missing_decision_game_ids'])
    if a['authority_blob']!=RECOVERY_AUTHORITY:raise ValueError('unqualified recovery authority')
    authority=ROOT/RECOVERY_PATH
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
        if row.get('state')!='HISTORICAL_GAP' or row.get('state_recorded_at_utc')!=a['as_of_utc'] or row.get('state_evidence')!=decisions['cycle_id']:
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
            elif row.get('state')=='HISTORICAL_GAP':raise ValueError('new gaps require separate disposition; no late conversion')
    return a



def bootstrap_check(market, decision, lineage):
    if gate.blob(lineage) != WEEK10_LINEAGE_SHA:
        raise ValueError('unqualified Week10 original lineage')
    expected = first_rows(lineage)
    first = []
    for content, tag, parent in ((market, MARKET_TAG, MARKET_PARENT), (decision, DECISION_TAG, DECISION_PARENT)):
        sources = list(re.finditer(r'^```' + SOURCE_TAG + r'\n(.*?)^```[ \t]*$', content, re.M | re.S))
        if len(sources) != 1:
            raise ValueError('unique Week10 source root required')
        root = sources[0]
        if gate.blob(content[:root.start()]) != parent:
            raise ValueError('Week10 prior-week parent bytes changed')
        declaration = json.loads(root[1], object_pairs_hook=gate.unique)
        expected_declaration = {'profile': PROFILE, 'original_lineage_blob': WEEK10_LINEAGE_SHA,
                                'first_source': FIRST_SOURCE, 'retained_sources': RETAINED_SOURCES, 'source_identity_blob': SOURCE_IDENTITY_SHA,
                                'recovery': declaration.get('recovery')}
        if declaration != expected_declaration:
            raise ValueError('Week10 source root mismatch')
        tail = content[root.end():]
        blocks = list(re.finditer(r'^```' + tag + r'\n(.*?)^```[ \t]*$', tail, re.M | re.S))
        if not blocks or re.sub(r'^```' + tag + r'\n.*?^```[ \t]*$', '', tail, flags=re.M | re.S).strip():
            raise ValueError('missing or untyped Week10 stream')
        obj = json.loads(blocks[0][1], object_pairs_hook=gate.unique)
        if gate.clock(obj['as_of_utc']) < gate.clock(RETAINED_SOURCES[-1]['recovered_by']):
            raise ValueError('Week10 initialization before source')
        if len(obj['rows']) != 63 or {r['game_id'] for r in obj['rows']} != set(expected):
            raise ValueError('Week10 initial identity union mismatch')
        first.append(obj)
    if (first[0]['cycle_id'], first[0]['as_of_utc']) != (first[1]['cycle_id'], first[1]['as_of_utc']):
        raise ValueError('Week10 initial paired source/decision boundary mismatch')
    for row in first[0]['rows']:
        earliest = expected[row['game_id']]['first']
        if earliest is not None and row.get('first') != earliest:
            raise ValueError('Week10 earliest observation changed or lost')
        if earliest is None and row.get('first') is not None and gate.clock(row['first']['retrieved_at']) <= gate.clock(RETAINED_SOURCES[-1]['recovered_by']):
            raise ValueError('Week10 unknown first cannot be backfilled')
    recovery_context(market, decision, lineage)
    return 'PASS_WEEK10_ORIGINAL_AND_FIRST_SOURCE_BOOTSTRAP_ONLY'


def compile(market, decision, capture, lineage, cycle, as_of, recovered_by, decision_rows):
    now = gate.clock(as_of)
    source_at = gate.clock(recovered_by)
    if not 0 <= (now - source_at).total_seconds() <= 900:
        raise ValueError('fresh source must be recovered within fifteen minutes of proposal')
    prior = None
    if re.search(r'^```' + MARKET_TAG + r'$', market, re.M):
        bootstrap_check(market, decision, lineage)
        saved = gate.selected_block(market, MARKET_TAG, gate.WEEKLY_MARKET_SCHEMA, now)
        prior = gate.inputs(market, decision, lineage, saved['as_of_utc'], PROFILE)
        if source_at <= gate.clock(prior[0]['as_of_utc']):
            raise ValueError('source must advance current boundary')
        rows = copy.deepcopy(prior[3])
        pm, pd = market, decision
    else:
        if gate.blob(market) != MARKET_PARENT or gate.blob(decision) != DECISION_PARENT:
            raise ValueError('unqualified Week9-to-Week10 parent')
        rows = first_rows(lineage)
        if source_at < gate.clock(RETAINED_SOURCES[-1]['recovered_by']):
            raise ValueError('Week10 source precedes retained first source')
        root = packet({'profile': PROFILE, 'original_lineage_blob': WEEK10_LINEAGE_SHA,
                       'first_source': FIRST_SOURCE, 'retained_sources': RETAINED_SOURCES, 'source_identity_blob': SOURCE_IDENTITY_SHA,
                       'recovery': {'authority_blob': RECOVERY_AUTHORITY, 'as_of_utc': as_of,
                                    'missing_decision_game_ids': sorted(RECOVERY_GAPS)}}, SOURCE_TAG).lstrip('\n')
        pm, pd = market + root, decision + root
    elapsed_context = {gid: r['kickoff_utc'] for gid, r in rows.items()
                       if r['kickoff_utc'] is not None and gate.clock(r['kickoff_utc']) < source_at}
    parsed = board(capture, lineage, recovered_by, retained_elapsed_kickoffs=elapsed_context)
    for game in parsed['games']:
        row = rows[game['game_id']]
        if prior is None and game['temporal_status'] != 'FUTURE_AT_CAPTURE' and game['game_id'] not in RECOVERY_GAPS:
            raise ValueError('initial Week10 cannot expand historical gaps')
        if game['temporal_status'] != 'FUTURE_AT_CAPTURE':
            if row['kickoff_utc'] is None or gate.clock(row['kickoff_utc']) > source_at:
                raise ValueError('Week10 elapsed source/retained kickoff conflict')
            row.update(current=None, current_availability='UNAVAILABLE', retained=row['current'] or row['retained'])
            continue
        if row['kickoff_status'] != 'QUALIFIED' or row['kickoff_utc'] != game['source_kickoff_utc']:
            row.update(kickoff_utc=game['source_kickoff_utc'], kickoff_source_url=WEEK10_URL, kickoff_status='RETAINED_UNVERIFIED')
        apply(row, source_offer(game, recovered_by), as_of)
    decisions = copy.deepcopy(decision_rows)
    conditional = any(r.get('state') == 'CONDITIONAL' or 'review_ref' in r for r in decisions) or (prior is not None and prior[1]['schema'] == gate.CONDITIONAL_DECISION_SCHEMA)
    for row in decisions:
        if conditional:
            row.setdefault('review_ref', None)
        gate.keys(row, ['game_id', 'state', 'reason', 'reconciliation_utc', 'planning_cutoff_utc',
                        'cutoff_authority', 'acceptable_number', 'execution_window'] + (['review_ref'] if conditional else []))
        if row['state'] not in ('PASS', 'INCONCLUSIVE', 'CONDITIONAL', 'HISTORICAL_GAP'):
            raise ValueError('Week10 cannot downgrade an earned unsupported richer decision')
        old = prior[4].get(row['game_id']) if prior else None
        retained = (old is not None and gate.closed_conditional(old, as_of)
                    and row == {k: v for k, v in old.items() if k not in ('state_recorded_at_utc', 'state_evidence')})
        retained_expired = (old is not None and old['state']==gate.EXPIRED_UNPUBLISHED
                            and row == {k:v for k,v in old.items() if k not in ('state_recorded_at_utc','state_evidence')})
        if row['state'] == 'CONDITIONAL' and not retained:
            # Independent qualification lives in the immutable review, never
            # in CBS display timing. Full shared validation still runs below.
            from cfb_conditional_recommendation_profile import load_review
            content, _ = load_review(row['review_ref'])
            review = json.loads(content, object_pairs_hook=gate.unique)
            source = rows[row['game_id']]
            reference = review['market_reference']
            if (review['game_id'] != row['game_id'] or review['original_lineage_blob'] != WEEK10_LINEAGE_SHA
                    or reference['kickoff_utc'] != source['kickoff_utc']):
                raise ValueError('Week10 review/source kickoff or lineage mismatch')
            kickoff_source = urlparse(reference['kickoff_source_url'])
            if (kickoff_source.hostname in ('cbssports.com', 'www.cbssports.com')
                    and kickoff_source.path.rstrip('/').lower().startswith('/college-football/odds')):
                raise ValueError('CBS display alone cannot qualify conditional kickoff')
            source.update(kickoff_status='QUALIFIED', kickoff_source_url=reference['kickoff_source_url'])
        if old is not None and old['state'] == row['state'] == 'PASS':
            kickoff = rows[row['game_id']]['kickoff_utc']
            if (kickoff is not None and gate.clock(kickoff) <= now
                    and row != {k: v for k, v in old.items()
                                if k not in ('state_recorded_at_utc', 'state_evidence')}):
                raise ValueError('elapsed PASS must retain exact pre-event decision; no retrospective reason rewrite')
        # PASS evidence identifies the original state, not the latest review.
        # Future reassessment remains in this packet's reason/current boundary.
        origin = old if retained or (old is not None and old['state'] == row['state'] and row['state'] in ('PASS','HISTORICAL_GAP')) else None
        row.update(state_recorded_at_utc=origin['state_recorded_at_utc'] if origin else as_of,
                   state_evidence=origin['state_evidence'] if origin else cycle)
    def obj(schema, rs):
        return {'schema': schema, 'cycle_id': cycle, 'as_of_utc': as_of, 'rows': rs}
    pm += packet(obj(gate.WEEKLY_MARKET_SCHEMA, list(rows.values())), MARKET_TAG).lstrip('\n')
    pd += packet(obj(gate.CONDITIONAL_DECISION_SCHEMA if conditional else gate.WEEKLY_DECISION_SCHEMA, decisions), DECISION_TAG).lstrip('\n')
    bootstrap_check(pm, pd, lineage)
    gate.inputs(pm, pd, lineage, as_of, PROFILE)
    return pm, pd


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('market', 'decision', 'capture', 'lineage', 'decision_rows', 'output_market', 'output_decision'):
        p.add_argument('--' + key.replace('_', '-'), type=Path, required=True)
    for key in ('cycle_id', 'as_of', 'recovered_by'):
        p.add_argument('--' + key.replace('_', '-'), required=True)
    a = p.parse_args()
    source = (a.market, a.decision, a.capture, a.lineage, a.decision_rows)
    output = (a.output_market, a.output_decision)
    if len({x.resolve() for x in output}) != 2 or {x.resolve() for x in output} & {x.resolve() for x in source}:
        p.error('distinct proposal outputs must not overwrite inputs')
    pm, pd = compile(*(x.read_text() for x in source[:4]), a.cycle_id, a.as_of, a.recovered_by,
                     json.loads(a.decision_rows.read_text(), object_pairs_hook=gate.unique))
    a.output_market.write_text(pm)
    a.output_decision.write_text(pd)
    print(json.dumps({'status': 'VALIDATED_WEEK10_PROPOSALS_ONLY_NOT_PERSISTED',
                      'games': 63, 'predictions': 55, 'exclusions': 8,
                      'market_blob': gate.blob(pm), 'decision_blob': gate.blob(pd)}))
