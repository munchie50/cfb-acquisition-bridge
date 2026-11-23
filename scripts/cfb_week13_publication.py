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
REFRESH_TAG = 'cfb-week13-source-refresh-v1'
MARKET_PARENT = '21e2172c709dcf482c4750a7490b82aacac05949'
DECISION_PARENT = '6862be6a1bd88a3290b1e90a49c33a7a87e92559'
KICKOFF_SOURCES = {
    '401866470': 'https://emueagles.com/sports/football/schedule/',
    '401866471': 'https://miamiredhawks.com/coverage',
}


def build_rows(source, lineage, as_of, prior_rows=None):
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
    body = prior_rows or {}
    elapsed = {gid: row['kickoff_utc'] for gid, row in body.items()
               if row['kickoff_utc'] and gate.clock(row['kickoff_utc']) < observed}
    board = normalize(raw, lineage, source['recovered_by'], WEEK13_URL, profile=PROFILE,
                      retained_elapsed_kickoffs=elapsed)
    originals = week13_census(lineage)
    rows = []
    for game in board['games']:
        gid, kickoff = game['game_id'], game['source_kickoff_utc']
        old = body.get(gid)
        if kickoff is None or gate.clock(kickoff) <= now:
            if old is None or gate.clock(old['kickoff_utc']) > observed:
                raise ValueError('elapsed game requires a matching earlier publication')
            row = dict(old)
            apply(row, None, as_of)
            rows.append(row)
            continue
        approved = originals[gid].get('operational_kickoff_utc')
        if approved and gate.clock(approved) != gate.clock(kickoff):
            raise ValueError('CBS kickoff disagrees with approved operational clock')
        row = dict(old) if old else dict(game_id=gid, first=None, current=None, current_availability='UNAVAILABLE',
                   retained=None, diagnostic=None, kickoff_utc=approved or kickoff,
                   kickoff_source_url=KICKOFF_SOURCES.get(gid, WEEK13_URL),
                   kickoff_status='QUALIFIED' if approved else 'RETAINED_UNVERIFIED')
        if old and gate.clock(old['kickoff_utc']) != gate.clock(kickoff):
            row.update(kickoff_utc=kickoff, kickoff_source_url=WEEK13_URL,
                       kickoff_status='RETAINED_UNVERIFIED')
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
    pattern = r'^```(' + '|'.join((SOURCE_TAG, REFRESH_TAG, tag)) + r')\n(.*?)^```[ \t]*$'
    blocks = list(re.finditer(pattern, content, re.M | re.S))
    if not blocks or len(blocks) % 2 or gate.blob(content[:blocks[0].start()]) != parent:
        raise ValueError('Week13 parent or source history mismatch')
    if re.sub(pattern, '', content[blocks[0].start():], flags=re.M | re.S).strip():
        raise ValueError('untyped Week13 publication history')
    result = []
    for i in range(0, len(blocks), 2):
        declaration, data = blocks[i:i+2]
        if declaration[1] != (SOURCE_TAG if i == 0 else REFRESH_TAG) or data[1] != tag:
            raise ValueError('Week13 source and publication packets out of order')
        if any(sum(line == '```' + tag for line in block[0].splitlines()) > 1
               for block in (declaration, data)):
            raise ValueError('ambiguous Week13 packet')
        declared = json.loads(declaration[2], object_pairs_hook=gate.unique)
        gate.keys(declared, ['profile', 'lineage_blob', 'source'])
        if (declared['profile'], declared['lineage_blob']) != (PROFILE, WEEK13_LINEAGE_SHA):
            raise ValueError('Week13 source declaration mismatch')
        result.append((declared['source'], json.loads(data[2], object_pairs_hook=gate.unique),
                       data.end()))
    return result


def bootstrap_check(market, decision, lineage):
    market_stream = streams(market, MARKET_PARENT, CFG['market_tag'])
    decision_stream = streams(decision, DECISION_PARENT, CFG['decision_tag'])
    previous = None
    for (source, m, mi), (decision_source, d, di) in zip(market_stream, decision_stream, strict=True):
        if source != decision_source or (m['cycle_id'], m['as_of_utc']) != (d['cycle_id'], d['as_of_utc']):
            raise ValueError('Week13 source/decision history mismatch')
        if previous and gate.clock(source['recovered_by']) <= gate.clock(previous[0]['as_of_utc']):
            raise ValueError('Week13 refresh must use a new capture after the last publication')
        expected = build_rows(source, lineage, m['as_of_utc'], previous[3] if previous else None)
        by_id = {row['game_id']: row for row in expected}
        validated = gate.inputs(market[:mi], decision[:di], lineage, m['as_of_utc'], PROFILE)
        for row in validated[4].values():
            if row['state'] == 'CONDITIONAL' and row['state_evidence'] == d['cycle_id']:
                qualify_kickoff(by_id[row['game_id']], row)
        if m['rows'] != expected:
            raise ValueError('Week13 market rows differ from retained capture')
        previous = validated
    return previous


def compile(market, decision, source, lineage, cycle, as_of, decision_rows):
    if (gate.blob(market), gate.blob(decision)) == (MARKET_PARENT, DECISION_PARENT):
        prior = None
    else:
        prior = bootstrap_check(market, decision, lineage)
    source_rows = build_rows(source, lineage, as_of, prior[3] if prior else None)
    sources = {row['game_id']: row for row in source_rows}
    conditional = (any(row['state'] == 'CONDITIONAL' for row in decision_rows)
                   or (prior is not None and prior[1]['schema'] == gate.CONDITIONAL_DECISION_SCHEMA))
    decisions = []
    for candidate in decision_rows:
        row = dict(candidate)
        if conditional:
            row.setdefault('review_ref', None)
        old = prior[4].get(row['game_id']) if prior else None
        same = old is not None and {k: v for k, v in old.items()
                                    if k not in ('state_recorded_at_utc', 'state_evidence')} == row
        if old and row['state'] == old['state'] == 'PASS':
            if not same and gate.clock(sources[row['game_id']]['kickoff_utc']) <= gate.clock(as_of):
                raise ValueError('elapsed PASS cannot rewrite pregame rationale')
            origin = old
        elif same and row['state'] in ('CONDITIONAL', 'OBSERVATION_ONLY'):
            origin = old
        else:
            origin = None
        if row['state'] == 'CONDITIONAL' and origin is None:
            qualify_kickoff(sources[row['game_id']], row)
        decisions.append(dict(row, state_recorded_at_utc=origin['state_recorded_at_utc'] if origin else as_of,
                              state_evidence=origin['state_evidence'] if origin else cycle))
    root = packet(dict(profile=PROFILE, lineage_blob=WEEK13_LINEAGE_SHA, source=source),
                  REFRESH_TAG if prior else SOURCE_TAG).lstrip('\n')
    m = dict(schema=gate.WEEKLY_MARKET_SCHEMA, cycle_id=cycle, as_of_utc=as_of, rows=source_rows)
    d = dict(schema=gate.CONDITIONAL_DECISION_SCHEMA if conditional else gate.WEEKLY_DECISION_SCHEMA,
             cycle_id=cycle, as_of_utc=as_of, rows=decisions)
    proposal = (market + root + packet(m, CFG['market_tag']).lstrip('\n'),
                decision + root + packet(d, CFG['decision_tag']).lstrip('\n'))
    bootstrap_check(*proposal, lineage)
    return proposal
