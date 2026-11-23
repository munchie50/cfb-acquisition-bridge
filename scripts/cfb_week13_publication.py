"""Compile and replay Week 13 append-only publication proposals."""
import json
import re
from pathlib import Path
from urllib.parse import urlparse

import cfb_neutral_publication_gate as gate
from cfb_cbs_full_board_normalizer import WEEK13_LINEAGE_SHA, WEEK13_URL, normalize, week13_census
from cfb_conditional_recommendation_profile import load_review
from cfb_neutral_publication_legacy_replay import packet
from cfb_neutral_weekly_reconciliation import board_offer
from cfb_week8_publication import apply

ROOT = Path(__file__).resolve().parents[1]
PROFILE = 'WEEK13'
CFG = gate.profile_config(PROFILE)
SOURCE_TAG = 'cfb-week13-source-bootstrap-v1'
MARKET_PARENT = '21e2172c709dcf482c4750a7490b82aacac05949'
DECISION_PARENT = '6862be6a1bd88a3290b1e90a49c33a7a87e92559'
KICKOFF_SOURCES = {
    '401866470': 'https://emueagles.com/sports/football/schedule/',
    '401866471': 'https://miamiredhawks.com/coverage',
}


def build_rows(source, lineage, as_of):
    gate.keys(source, ['path', 'blob', 'recovered_by'])
    path = (ROOT / source['path']).resolve()
    if path.parent != (ROOT / 'evidence/operational').resolve() or path.suffix != '.md':
        raise ValueError('retained operational capture required')
    raw = path.read_text()
    if gate.blob(raw) != source['blob']:
        raise ValueError('retained capture blob mismatch')
    observed, now = gate.clock(source['recovered_by']), gate.clock(as_of)
    if not CFG['start'] <= observed < CFG['end'] or not 0 <= (now - observed).total_seconds() <= 900:
        raise ValueError('fresh Week13 capture required within fifteen minutes of proposal')
    board = normalize(raw, lineage, source['recovered_by'], WEEK13_URL, profile=PROFILE)
    originals = week13_census(lineage)
    rows = []
    for game in board['games']:
        gid, kickoff = game['game_id'], game['source_kickoff_utc']
        if kickoff is None or gate.clock(kickoff) <= now:
            raise ValueError('opening proposal cannot reconstruct an elapsed decision')
        approved = originals[gid].get('operational_kickoff_utc')
        if approved and gate.clock(approved) != gate.clock(kickoff):
            raise ValueError('CBS kickoff disagrees with approved operational clock')
        row = dict(game_id=gid, first=None, current=None, current_availability='UNAVAILABLE',
                   retained=None, diagnostic=None, kickoff_utc=approved or kickoff,
                   kickoff_source_url=KICKOFF_SOURCES.get(gid, WEEK13_URL),
                   kickoff_status='QUALIFIED' if approved else 'RETAINED_UNVERIFIED')
        offer = board_offer(game, source['recovered_by'])
        offer['source_url'] = WEEK13_URL
        if not any(offer[k] is not None for k in ('away_spread', 'home_spread', 'away_ml',
                                                 'home_ml', 'over_total', 'under_total')):
            offer = None
        apply(row, offer, as_of)
        rows.append(row)
    return rows


def qualify_kickoff(row, decision):
    content, _ = load_review(decision['review_ref'])
    review = json.loads(content, object_pairs_hook=gate.unique)
    reference = review['market_reference']
    if (review['game_id'] != row['game_id']
            or review['original_lineage_blob'] != WEEK13_LINEAGE_SHA
            or gate.clock(reference['kickoff_utc']) != gate.clock(row['kickoff_utc'])):
        raise ValueError('Week13 review/source kickoff or lineage mismatch')
    url = urlparse(reference['kickoff_source_url'])
    if url.hostname in ('cbssports.com', 'www.cbssports.com') and url.path.startswith('/college-football/odds'):
        raise ValueError('CBS display alone cannot qualify conditional kickoff')
    row.update(kickoff_status='QUALIFIED', kickoff_source_url=reference['kickoff_source_url'])


def streams(content, parent, tag):
    root = list(re.finditer(r'^\x60\x60\x60' + SOURCE_TAG + r'\n(.*?)^\x60\x60\x60[ \t]*$', content, re.M | re.S))
    if len(root) != 1 or gate.blob(content[:root[0].start()]) != parent:
        raise ValueError('Week13 parent or source root mismatch')
    declared = json.loads(root[0][1], object_pairs_hook=gate.unique)
    gate.keys(declared, ['profile', 'lineage_blob', 'source'])
    if (declared['profile'], declared['lineage_blob']) != (PROFILE, WEEK13_LINEAGE_SHA):
        raise ValueError('Week13 source declaration mismatch')
    pattern = r'^```' + tag + r'\n(.*?)^```[ \t]*$'
    tail = content[root[0].end():].lstrip('\n')
    match = re.fullmatch(pattern, tail.rstrip('\n'), re.M | re.S)
    if match is None or len(re.findall(r'^```' + tag + r'$', tail, re.M)) != 1:
        raise ValueError('exactly one qualified Week13 opening packet required')
    return declared, json.loads(match[1], object_pairs_hook=gate.unique)


def bootstrap_check(market, decision, lineage):
    market_root, m = streams(market, MARKET_PARENT, CFG['market_tag'])
    decision_root, d = streams(decision, DECISION_PARENT, CFG['decision_tag'])
    if market_root != decision_root or (m['cycle_id'], m['as_of_utc']) != (d['cycle_id'], d['as_of_utc']):
        raise ValueError('Week13 source/decision history mismatch')
    expected = build_rows(market_root['source'], lineage, m['as_of_utc'])
    by_id = {row['game_id']: row for row in expected}
    _, _, _, _, rows = gate.inputs(market, decision, lineage, m['as_of_utc'], PROFILE)
    for row in rows.values():
        if row['state'] == 'CONDITIONAL':
            qualify_kickoff(by_id[row['game_id']], row)
    if m['rows'] != expected:
        raise ValueError('Week13 market rows differ from retained capture')
    return 'PASS_WEEK13_PUBLICATION_PROPOSAL_ONLY'


def compile(market, decision, source, lineage, cycle, as_of, decision_rows):
    # Opening publication pins both canonical parents before appending a packet.
    if (gate.blob(market), gate.blob(decision)) != (MARKET_PARENT, DECISION_PARENT):
        raise ValueError('unqualified Week13 initial canonical parents')
    source_rows = build_rows(source, lineage, as_of)
    sources = {row['game_id']: row for row in source_rows}
    conditional = any(row['state'] == 'CONDITIONAL' for row in decision_rows)
    decisions = []
    for candidate in decision_rows:
        row = dict(candidate)
        if conditional:
            row.setdefault('review_ref', None)
        if row['state'] == 'CONDITIONAL':
            qualify_kickoff(sources[row['game_id']], row)
        decisions.append(dict(row, state_recorded_at_utc=as_of, state_evidence=cycle))
    root = packet(dict(profile=PROFILE, lineage_blob=WEEK13_LINEAGE_SHA, source=source), SOURCE_TAG).lstrip('\n')
    m = dict(schema=gate.WEEKLY_MARKET_SCHEMA, cycle_id=cycle, as_of_utc=as_of, rows=source_rows)
    d = dict(schema=gate.CONDITIONAL_DECISION_SCHEMA if conditional else gate.WEEKLY_DECISION_SCHEMA,
             cycle_id=cycle, as_of_utc=as_of, rows=decisions)
    proposal = (market + root + packet(m, CFG['market_tag']).lstrip('\n'),
                decision + root + packet(d, CFG['decision_tag']).lstrip('\n'))
    bootstrap_check(*proposal, lineage)
    return proposal
