"""Build and verify Week 12 publication proposals from a retained CBS capture."""

import json
from pathlib import Path
import re
from urllib.parse import urlparse

import cfb_neutral_publication_gate as gate
from cfb_cbs_full_board_normalizer import WEEK12_LINEAGE_SHA, WEEK12_URL, normalize
from cfb_neutral_publication_legacy_replay import packet
from cfb_neutral_weekly_reconciliation import board_offer
from cfb_week8_publication import apply
from cfb_conditional_recommendation_profile import load_review


ROOT = Path(__file__).resolve().parents[1]
PROFILE = 'WEEK12'
CFG = gate.profile_config(PROFILE)
SOURCE_TAG = 'cfb-week12-source-bootstrap-v1'
MARKET_PARENT = 'dd59069b767cf563a5c4737b364249ce1d9c8535'
DECISION_PARENT = '55a9d19f6df452f1625a3f124f8201e04a1a9cf0'


def source_board(source, lineage, as_of, *, elapsed=None):
    gate.keys(source, ['path', 'blob', 'recovered_by'])
    path = (ROOT / source['path']).resolve()
    if path.parent != (ROOT / 'evidence/operational').resolve() or path.suffix != '.md':
        raise ValueError('retained operational capture required')
    raw = path.read_text()
    if gate.blob(raw) != source['blob']:
        raise ValueError('retained capture blob mismatch')
    observed = gate.clock(source['recovered_by'])
    now = gate.clock(as_of)
    if not CFG['start'] <= observed < CFG['end'] or not 0 <= (now - observed).total_seconds() <= 900:
        raise ValueError('fresh Week12 capture required within fifteen minutes of proposal')
    return normalize(raw, lineage, source['recovered_by'], WEEK12_URL, profile=PROFILE,
                     retained_elapsed_kickoffs=elapsed)


def source_offer(game, recovered_by):
    offer = board_offer(game, recovered_by)
    offer['source_url'] = WEEK12_URL
    if all(offer[k] is None for k in ('away_spread', 'home_spread', 'away_ml',
                                     'home_ml', 'over_total', 'under_total')):
        return None
    return offer


def initial_rows(source, lineage, as_of):
    board = source_board(source, lineage, as_of)
    now = gate.clock(as_of)
    rows = []
    for game in board['games']:
        kickoff = game['source_kickoff_utc']
        if kickoff is None or gate.clock(kickoff) <= now:
            raise ValueError('opening proposal cannot reconstruct elapsed decisions')
        row = dict(game_id=game['game_id'], kickoff_utc=kickoff,
                   kickoff_source_url=WEEK12_URL, kickoff_status='RETAINED_UNVERIFIED',
                   first=None, current=None, current_availability='UNAVAILABLE',
                   retained=None, diagnostic=None)
        apply(row, source_offer(game, source['recovered_by']), as_of)
        rows.append(row)
    return rows


def bootstrap_check(market, decision, lineage):
    declarations = []
    packets = []
    for content, parent, tag, schema in (
        (market, MARKET_PARENT, CFG['market_tag'], (gate.WEEKLY_MARKET_SCHEMA,)),
        (decision, DECISION_PARENT, CFG['decision_tag'], gate.WEEKLY_DECISION_SCHEMAS),
    ):
        root = list(re.finditer(r'^\x60\x60\x60' + SOURCE_TAG + r'\n(.*?)^\x60\x60\x60[ \t]*$', content, re.M | re.S))
        if len(root) != 1 or gate.blob(content[:root[0].start()]) != parent:
            raise ValueError('Week12 parent or source root mismatch')
        declaration = json.loads(root[0][1], object_pairs_hook=gate.unique)
        gate.keys(declaration, ['profile', 'lineage_blob', 'first_source'])
        if (declaration['profile'], declaration['lineage_blob']) != (PROFILE, WEEK12_LINEAGE_SHA):
            raise ValueError('Week12 source declaration mismatch')
        declarations.append(declaration)
        tail = content[root[0].end():]
        pattern = r'^```' + tag + r'\n(.*?)^```[ 	]*$'
        matches = list(re.finditer(pattern, tail, re.M | re.S))
        if not matches or re.sub(pattern, '', tail, flags=re.M | re.S).strip():
            raise ValueError('missing or untyped Week12 packet stream')
        stream = [json.loads(match[1], object_pairs_hook=gate.unique) for match in matches]
        if any(obj['schema'] not in schema for obj in stream):
            raise ValueError('unsupported Week12 publication schema')
        packets.append(stream)
    if declarations[0] != declarations[1]:
        raise ValueError('Week12 source roots disagree')

    def boundaries(stream):
        return [(obj['cycle_id'], obj['as_of_utc']) for obj in stream]

    if boundaries(packets[0]) != boundaries(packets[1]):
        raise ValueError('Week12 market and decision packet boundaries disagree')
    first = packets[0][0]
    expected = initial_rows(declarations[0]['first_source'], lineage, first['as_of_utc'])
    expected_by_id = {row['game_id']: row for row in expected}
    for row in packets[1][0]['rows']:
        if row['state'] == 'CONDITIONAL':
            qualify_kickoff(expected_by_id[row['game_id']], row)
    if first['rows'] != expected:
        raise ValueError('Week12 opening rows differ from retained capture')
    gate.inputs(market, decision, lineage, packets[0][-1]['as_of_utc'], PROFILE)
    if packets[1][-1]['schema'] == gate.CONDITIONAL_DECISION_SCHEMA:
        return 'PASS_WEEK12_CONDITIONAL_PROPOSAL_ONLY'
    return 'PASS_WEEK12_OPENING_NEUTRAL_PROPOSAL_ONLY' if len(packets[0]) == 1 else 'PASS_WEEK12_NEUTRAL_CONTINUATION_ONLY'


def refresh_rows(prior, source, lineage, as_of):
    observed = gate.clock(source['recovered_by'])
    if observed <= gate.clock(prior[0]['as_of_utc']):
        raise ValueError('refresh must advance the prior source boundary')
    rows = prior[3]
    elapsed = {gid: r['kickoff_utc'] for gid, r in rows.items()
               if r['kickoff_utc'] is not None and gate.clock(r['kickoff_utc']) < observed}
    board = source_board(source, lineage, as_of, elapsed=elapsed)
    for game in board['games']:
        row = rows[game['game_id']]
        kickoff = game['source_kickoff_utc']
        if game['temporal_status'] != 'FUTURE_AT_CAPTURE':
            if row['kickoff_utc'] is None or gate.clock(row['kickoff_utc']) > observed:
                raise ValueError('elapsed source conflicts with retained kickoff')
            # No new quote from an elapsed event enters the pregame ledger.
            apply(row, None, as_of)
        else:
            if row['kickoff_utc'] != kickoff:
                row.update(kickoff_utc=kickoff, kickoff_source_url=WEEK12_URL,
                           kickoff_status='RETAINED_UNVERIFIED')
            apply(row, source_offer(game, source['recovered_by']), as_of)
    return list(rows.values())


def qualify_kickoff(source_row, decision_row):
    content, _ = load_review(decision_row['review_ref'])
    review = json.loads(content, object_pairs_hook=gate.unique)
    reference = review['market_reference']
    if (review['game_id'] != source_row['game_id']
            or review['original_lineage_blob'] != WEEK12_LINEAGE_SHA
            or reference['kickoff_utc'] != source_row['kickoff_utc']):
        raise ValueError('Week12 review/source kickoff or lineage mismatch')
    kickoff_source = urlparse(reference['kickoff_source_url'])
    if (kickoff_source.hostname in ('cbssports.com', 'www.cbssports.com')
            and kickoff_source.path.rstrip('/').lower().startswith('/college-football/odds')):
        raise ValueError('CBS display alone cannot qualify conditional kickoff')
    source_row.update(kickoff_status='QUALIFIED', kickoff_source_url=reference['kickoff_source_url'])


def compile(market, decision, source, lineage, cycle, as_of, decision_rows):
    prior = None
    root = ''
    if ('```' + SOURCE_TAG) in market or ('```' + SOURCE_TAG) in decision:
        bootstrap_check(market, decision, lineage)
        saved = gate.selected_block(market, CFG['market_tag'], gate.WEEKLY_MARKET_SCHEMA, gate.clock(as_of))
        prior = gate.inputs(market, decision, lineage, saved['as_of_utc'], PROFILE)
        source_rows = refresh_rows(prior, source, lineage, as_of)
    else:
        if (gate.blob(market), gate.blob(decision)) != (MARKET_PARENT, DECISION_PARENT):
            raise ValueError('unqualified Week11-to-Week12 parent')
        source_rows = initial_rows(source, lineage, as_of)
        root = packet(dict(profile=PROFILE, lineage_blob=WEEK12_LINEAGE_SHA,
                           first_source=source), SOURCE_TAG).lstrip('\n')

    sources = {row['game_id']: row for row in source_rows}
    conditional = (any(row.get('state') == 'CONDITIONAL' for row in decision_rows)
                   or (prior is not None and prior[1]['schema'] == gate.CONDITIONAL_DECISION_SCHEMA))
    rows = []
    for candidate in decision_rows:
        row = dict(candidate)
        if conditional:
            row.setdefault('review_ref', None)
        gate.keys(row, ['game_id', 'state', 'reason', 'reconciliation_utc',
                        'planning_cutoff_utc', 'cutoff_authority',
                        'acceptable_number', 'execution_window']
                  + (['review_ref'] if conditional else []))
        if row['state'] not in ('PASS', 'INCONCLUSIVE', 'CONDITIONAL'):
            raise ValueError('unsupported Week12 decision state')
        source_row = sources.get(row['game_id'])
        if source_row is None:
            raise ValueError('unknown Week12 decision identity')
        old = prior[4].get(row['game_id']) if prior else None
        saved = {k: v for k, v in old.items() if k not in ('state_recorded_at_utc', 'state_evidence')} if old else None
        retained = old and gate.closed_conditional(old, as_of) and row == saved
        if row['state'] == 'CONDITIONAL' and not retained:
            qualify_kickoff(source_row, row)
        same_pass = old and old['state'] == row['state'] == 'PASS'
        if same_pass:
            kickoff = source_row['kickoff_utc']
            if kickoff and gate.clock(kickoff) <= gate.clock(as_of):
                comparable = {k: v for k, v in row.items() if k != 'review_ref' or k in saved}
                if comparable != saved:
                    raise ValueError('elapsed PASS cannot rewrite pregame decision')
        origin = old if same_pass or retained else None
        rows.append(dict(row, state_recorded_at_utc=origin['state_recorded_at_utc'] if origin else as_of,
                         state_evidence=origin['state_evidence'] if origin else cycle))

    def boundary(schema, rows):
        return dict(schema=schema, cycle_id=cycle, as_of_utc=as_of, rows=rows)

    market += root + packet(boundary(gate.WEEKLY_MARKET_SCHEMA, source_rows), CFG['market_tag']).lstrip('\n')
    schema = gate.CONDITIONAL_DECISION_SCHEMA if conditional else gate.WEEKLY_DECISION_SCHEMA
    decision += root + packet(boundary(schema, rows), CFG['decision_tag']).lstrip('\n')
    bootstrap_check(market, decision, lineage)
    return market, decision
