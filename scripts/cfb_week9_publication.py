"""Explicit Week9 source-rooted neutral compiler; proposals only, never writes.

The caller supplies independently recorded decisions and an actual fresh source.
Original archives are never rerun as models, and Week8 history stays byte-exact.
"""
import argparse
import copy
import json
import re
from pathlib import Path
from urllib.parse import urlparse
import cfb_neutral_publication_gate as gate
from cfb_cbs_full_board_normalizer import normalize, WEEK9_URL, WEEK9_LINEAGE_SHA
from cfb_neutral_weekly_reconciliation import board_offer
from cfb_neutral_publication_legacy_replay import packet
from cfb_week8_publication import apply

ROOT = Path(__file__).resolve().parents[1]
PROFILE = 'WEEK9'
CFG = gate.profile_config(PROFILE)
MARKET_TAG = CFG['market_tag']
DECISION_TAG = CFG['decision_tag']
SOURCE_TAG = 'cfb-week9-source-bootstrap-v1'
MARKET_PARENT = '0c7d0fd878f1d364674bb89bff8660d164b7ff22'
DECISION_PARENT = '7f8bfefbe4c943ea35691f7a7db3e43ec4beac6c'
FIRST_SOURCE = {
    'path': 'evidence/operational/CFB_CBS_WEEK9_TEXT_TABLE_CAPTURE_20261025T154923Z.md',
    'blob': '3cfeeaace7e3ff7d62e19a01c77dbb907ead9574',
    'recovered_by': '2026-10-25T15:49:23.713Z',
}


def board(capture, lineage, recovered_by, *, retained_elapsed_kickoffs=None):
    return normalize(capture, lineage, recovered_by, source_url=WEEK9_URL, profile=PROFILE, retained_elapsed_kickoffs=retained_elapsed_kickoffs)


def source_offer(game, at):
    offer = board_offer(game, at)
    offer['source_url'] = WEEK9_URL
    return None if all(offer[k] is None for k in ('away_spread', 'home_spread', 'away_ml', 'home_ml', 'over_total', 'under_total')) else offer


def first_rows(lineage):
    raw = (ROOT / FIRST_SOURCE['path']).read_text()
    if gate.blob(raw) != FIRST_SOURCE['blob']:
        raise ValueError('Week9 first source bytes changed')
    parsed = board(raw, lineage, FIRST_SOURCE['recovered_by'])
    if parsed['coverage']['future_games'] != 56:
        raise ValueError('Week9 first source cannot reconstruct elapsed observations')
    rows = {}
    for game in parsed['games']:
        row = {'game_id': game['game_id'], 'kickoff_utc': game['source_kickoff_utc'],
               'kickoff_source_url': WEEK9_URL, 'kickoff_status': 'RETAINED_UNVERIFIED',
               'first': None, 'current': None, 'current_availability': 'UNAVAILABLE',
               'retained': None, 'diagnostic': None}
        apply(row, source_offer(game, FIRST_SOURCE['recovered_by']), FIRST_SOURCE['recovered_by'])
        rows[game['game_id']] = row
    return rows


def bootstrap_check(market, decision, lineage):
    if gate.blob(lineage) != WEEK9_LINEAGE_SHA:
        raise ValueError('unqualified Week9 original lineage')
    expected = first_rows(lineage)
    first = []
    for content, tag, parent in ((market, MARKET_TAG, MARKET_PARENT), (decision, DECISION_TAG, DECISION_PARENT)):
        sources = list(re.finditer(r'^```' + SOURCE_TAG + r'\n(.*?)^```[ \t]*$', content, re.M | re.S))
        if len(sources) != 1:
            raise ValueError('unique Week9 source root required')
        root = sources[0]
        if gate.blob(content[:root.start()]) != parent:
            raise ValueError('Week9 prior-week parent bytes changed')
        declaration = json.loads(root[1], object_pairs_hook=gate.unique)
        if declaration != {'profile': PROFILE, 'original_lineage_blob': WEEK9_LINEAGE_SHA,
                           'first_source': FIRST_SOURCE}:
            raise ValueError('Week9 source root mismatch')
        tail = content[root.end():]
        blocks = list(re.finditer(r'^```' + tag + r'\n(.*?)^```[ \t]*$', tail, re.M | re.S))
        if not blocks or re.sub(r'^```' + tag + r'\n.*?^```[ \t]*$', '', tail, flags=re.M | re.S).strip():
            raise ValueError('missing or untyped Week9 stream')
        obj = json.loads(blocks[0][1], object_pairs_hook=gate.unique)
        if gate.clock(obj['as_of_utc']) < gate.clock(FIRST_SOURCE['recovered_by']):
            raise ValueError('Week9 initialization before source')
        if len(obj['rows']) != 56 or {r['game_id'] for r in obj['rows']} != set(expected):
            raise ValueError('Week9 initial identity union mismatch')
        first.append(obj)
    if (first[0]['cycle_id'], first[0]['as_of_utc']) != (first[1]['cycle_id'], first[1]['as_of_utc']):
        raise ValueError('Week9 initial paired source/decision boundary mismatch')
    for row in first[0]['rows']:
        earliest = expected[row['game_id']]['first']
        if earliest is not None and row.get('first') != earliest:
            raise ValueError('Week9 earliest observation changed or lost')
        if earliest is None and row.get('first') is not None and gate.clock(row['first']['retrieved_at']) <= gate.clock(FIRST_SOURCE['recovered_by']):
            raise ValueError('Week9 unknown first cannot be backfilled')
    return 'PASS_WEEK9_ORIGINAL_AND_FIRST_SOURCE_BOOTSTRAP_ONLY'


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
            raise ValueError('unqualified Week8-to-Week9 parent')
        rows = first_rows(lineage)
        if source_at < gate.clock(FIRST_SOURCE['recovered_by']):
            raise ValueError('Week9 source precedes retained first source')
        root = packet({'profile': PROFILE, 'original_lineage_blob': WEEK9_LINEAGE_SHA,
                       'first_source': FIRST_SOURCE}, SOURCE_TAG).lstrip('\n')
        pm, pd = market + root, decision + root
    elapsed_context = {gid: r['kickoff_utc'] for gid, r in rows.items()
                       if prior is not None and r['kickoff_utc'] is not None and gate.clock(r['kickoff_utc']) < source_at}
    parsed = board(capture, lineage, recovered_by, retained_elapsed_kickoffs=elapsed_context)
    for game in parsed['games']:
        row = rows[game['game_id']]
        if prior is None and game['temporal_status'] != 'FUTURE_AT_CAPTURE':
            raise ValueError('initial Week9 cannot reconstruct elapsed decisions')
        if game['temporal_status'] != 'FUTURE_AT_CAPTURE':
            if row['kickoff_utc'] is None or gate.clock(row['kickoff_utc']) > source_at:
                raise ValueError('Week9 elapsed source/retained kickoff conflict')
            row.update(current=None, current_availability='UNAVAILABLE', retained=row['current'] or row['retained'])
            continue
        if row['kickoff_status'] != 'QUALIFIED' or row['kickoff_utc'] != game['source_kickoff_utc']:
            row.update(kickoff_utc=game['source_kickoff_utc'], kickoff_source_url=WEEK9_URL, kickoff_status='RETAINED_UNVERIFIED')
        apply(row, source_offer(game, recovered_by), as_of)
    decisions = copy.deepcopy(decision_rows)
    conditional = any(r.get('state') == 'CONDITIONAL' or 'review_ref' in r for r in decisions) or (prior is not None and prior[1]['schema'] == gate.CONDITIONAL_DECISION_SCHEMA)
    for row in decisions:
        if conditional:
            row.setdefault('review_ref', None)
        gate.keys(row, ['game_id', 'state', 'reason', 'reconciliation_utc', 'planning_cutoff_utc',
                        'cutoff_authority', 'acceptable_number', 'execution_window'] + (['review_ref'] if conditional else []))
        if row['state'] not in ('PASS', 'INCONCLUSIVE', 'CONDITIONAL'):
            raise ValueError('Week9 cannot downgrade an earned unsupported richer decision')
        old = prior[4].get(row['game_id']) if prior else None
        retained = (old is not None and gate.closed_conditional(old, as_of)
                    and row == {k: v for k, v in old.items() if k not in ('state_recorded_at_utc', 'state_evidence')})
        if row['state'] == 'CONDITIONAL' and not retained:
            # Independent qualification lives in the immutable review, never
            # in CBS display timing. Full shared validation still runs below.
            from cfb_conditional_recommendation_profile import load_review
            content, _ = load_review(row['review_ref'])
            review = json.loads(content, object_pairs_hook=gate.unique)
            source = rows[row['game_id']]
            reference = review['market_reference']
            if (review['game_id'] != row['game_id'] or review['original_lineage_blob'] != WEEK9_LINEAGE_SHA
                    or reference['kickoff_utc'] != source['kickoff_utc']):
                raise ValueError('Week9 review/source kickoff or lineage mismatch')
            kickoff_source = urlparse(reference['kickoff_source_url'])
            if (kickoff_source.hostname in ('cbssports.com', 'www.cbssports.com')
                    and kickoff_source.path.rstrip('/').lower().startswith('/college-football/odds')):
                raise ValueError('CBS display alone cannot qualify conditional kickoff')
            source.update(kickoff_status='QUALIFIED', kickoff_source_url=reference['kickoff_source_url'])
        origin = old if retained or (old is not None and old['state'] == row['state'] == 'PASS') else None
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
    print(json.dumps({'status': 'VALIDATED_WEEK9_PROPOSALS_ONLY_NOT_PERSISTED',
                      'games': 56, 'predictions': 45, 'exclusions': 11,
                      'market_blob': gate.blob(pm), 'decision_blob': gate.blob(pd)}))
