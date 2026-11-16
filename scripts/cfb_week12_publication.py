"""Build and verify the first Week 12 neutral proposal from a retained CBS capture."""

import json
from pathlib import Path
import re

import cfb_neutral_publication_gate as gate
from cfb_cbs_full_board_normalizer import WEEK12_LINEAGE_SHA, WEEK12_URL, normalize
from cfb_neutral_publication_legacy_replay import packet
from cfb_neutral_weekly_reconciliation import board_offer
from cfb_week8_publication import apply


ROOT = Path(__file__).resolve().parents[1]
PROFILE = 'WEEK12'
CFG = gate.profile_config(PROFILE)
SOURCE_TAG = 'cfb-week12-source-bootstrap-v1'
MARKET_PARENT = 'dd59069b767cf563a5c4737b364249ce1d9c8535'
DECISION_PARENT = '55a9d19f6df452f1625a3f124f8201e04a1a9cf0'


def initial_rows(source, lineage, as_of):
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
    board = normalize(raw, lineage, source['recovered_by'], WEEK12_URL, profile=PROFILE)
    rows = []
    for game in board['games']:
        kickoff = game['source_kickoff_utc']
        if kickoff is None or gate.clock(kickoff) <= now:
            raise ValueError('opening proposal cannot reconstruct elapsed decisions')
        row = dict(game_id=game['game_id'], kickoff_utc=kickoff,
                   kickoff_source_url=WEEK12_URL, kickoff_status='RETAINED_UNVERIFIED',
                   first=None, current=None, current_availability='UNAVAILABLE',
                   retained=None, diagnostic=None)
        offer = board_offer(game, source['recovered_by'])
        offer['source_url'] = WEEK12_URL
        if all(offer[k] is None for k in ('away_spread', 'home_spread', 'away_ml',
                                         'home_ml', 'over_total', 'under_total')):
            offer = None
        apply(row, offer, as_of)
        rows.append(row)
    return rows


def bootstrap_check(market, decision, lineage):
    declarations = []
    packets = []
    for content, parent, tag, schema in (
        (market, MARKET_PARENT, CFG['market_tag'], gate.WEEKLY_MARKET_SCHEMA),
        (decision, DECISION_PARENT, CFG['decision_tag'], gate.WEEKLY_DECISION_SCHEMA),
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
        match = re.fullmatch(r'\s*\x60\x60\x60'+tag+r'\n(.*?)^\x60\x60\x60\s*', tail, re.M | re.S)
        if not match:
            raise ValueError('one opening Week12 packet per stream required')
        obj = json.loads(match[1], object_pairs_hook=gate.unique)
        if obj['schema'] != schema:
            raise ValueError('unsupported opening Week12 schema')
        packets.append(obj)
    if declarations[0] != declarations[1]:
        raise ValueError('Week12 source roots disagree')
    if packets[0]['rows'] != initial_rows(declarations[0]['first_source'], lineage, packets[0]['as_of_utc']):
        raise ValueError('Week12 opening rows differ from retained capture')
    gate.inputs(market, decision, lineage, packets[0]['as_of_utc'], PROFILE)
    return 'PASS_WEEK12_OPENING_NEUTRAL_PROPOSAL_ONLY'


def compile(market, decision, source, lineage, cycle, as_of, decision_rows):
    if (gate.blob(market), gate.blob(decision)) != (MARKET_PARENT, DECISION_PARENT):
        raise ValueError('unqualified Week11-to-Week12 parent')
    source_rows = initial_rows(source, lineage, as_of)
    rows = []
    for row in decision_rows:
        gate.keys(row, ['game_id', 'state', 'reason', 'reconciliation_utc',
                        'planning_cutoff_utc', 'cutoff_authority',
                        'acceptable_number', 'execution_window'])
        if row['state'] not in ('PASS', 'INCONCLUSIVE'):
            raise ValueError('earned richer decision requires a qualified Week12 continuation')
        rows.append(dict(row, state_recorded_at_utc=as_of, state_evidence=cycle))

    def boundary(schema, rows):
        return dict(schema=schema, cycle_id=cycle, as_of_utc=as_of, rows=rows)

    root = packet(dict(profile=PROFILE, lineage_blob=WEEK12_LINEAGE_SHA,
                       first_source=source), SOURCE_TAG).lstrip('\n')
    market += root + packet(boundary(gate.WEEKLY_MARKET_SCHEMA, source_rows), CFG['market_tag']).lstrip('\n')
    decision += root + packet(boundary(gate.WEEKLY_DECISION_SCHEMA, rows), CFG['decision_tag']).lstrip('\n')
    bootstrap_check(market, decision, lineage)
    return market, decision
