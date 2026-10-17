"""Versioned conditional display from immutable prospective review evidence.

This is a presentation validator, not a bet selector, source-truth certifier or
model promotion. No Caesars quote is required or fabricated.
"""
import json
import re
import subprocess
from pathlib import Path
import cfb_neutral_publication_gate as gate
from cfb_consensus_reference import identity_key, reference

SCHEMA = 'CFB_WEEKLY_CONDITIONAL_DECISION_V3'
REVIEW_SCHEMA = 'CFB_PROSPECTIVE_CONDITIONAL_REVIEW_V1'
ROOT = Path(__file__).resolve().parents[1]


def load_review(ref):
    gate.keys(ref, ['path', 'commit', 'blob'])
    if not isinstance(ref['path'], str) or not re.fullmatch(r'evidence/operational/recommendation_reviews/[A-Za-z0-9_-]+\.json', ref['path']):
        raise ValueError('review must be an append-only governed recommendation-review JSON')
    for key in ('commit', 'blob'):
        if not isinstance(ref[key], str) or not re.fullmatch(r'[0-9a-f]{40}', ref[key]): raise ValueError('invalid immutable review identity')
    def git(*args):
        return subprocess.check_output(['git', '-C', str(ROOT), *args], stderr=subprocess.DEVNULL).decode('utf-8')
    try:
        subprocess.run(['git', '-C', str(ROOT), 'merge-base', '--is-ancestor', ref['commit'], 'HEAD'],
                       check=True, capture_output=True)
        content = git('show', ref['commit'] + ':' + ref['path'])
        committed = git('show', '-s', '--format=%cI', ref['commit']).strip()
    except (subprocess.CalledProcessError, UnicodeDecodeError) as exc:
        raise ValueError('review commit/path not recovered in current accepted ancestry') from exc
    if gate.blob(content) != ref['blob']: raise ValueError('review blob/path binding mismatch')
    return content, committed


def validate(row, market_row, model, as_of):
    content, committed_at = load_review(row['review_ref'])
    r = json.loads(content, object_pairs_hook=gate.unique)
    gate.keys(r, ['schema', 'game_id', 'state', 'recorded_at_utc', 'original_lineage_blob',
                  'maturity', 'market', 'selection', 'rationale', 'model_review',
                  'material_sources', 'uncertainty', 'decision_rule', 'source_qualification',
                  'market_reference', 'acceptable_number', 'reconciliation_utc',
                  'planning_cutoff_utc', 'cutoff_basis', 'execution_window'])
    if r['schema'] != REVIEW_SCHEMA or r['state'] != 'CONDITIONAL': raise ValueError('unsupported recommendation review/state')
    if r['game_id'] != row['game_id'] or r['original_lineage_blob'] != gate.LINEAGE_SHA:
        raise ValueError('review game/original-model lineage mismatch')
    if model['first_frozen_status'] != 'PREDICTION': raise ValueError('conditional review cannot replace original model exclusion')
    now = gate.clock(as_of)
    recorded, committed, state_at = map(gate.clock, (r['recorded_at_utc'], committed_at, row['state_recorded_at_utc']))
    if not recorded <= committed <= state_at <= now: raise ValueError('review must pre-exist prospective decision boundary')
    kickoff = gate.clock(market_row['kickoff_utc']) if market_row['kickoff_utc'] else None
    if kickoff is None or now >= kickoff or market_row['kickoff_status'] != 'QUALIFIED':
        raise ValueError('conditional recommendation requires qualified future kickoff')
    if r['maturity'] != 'CONTROLLED_BETA_RECOMMENDATION': raise ValueError('unsupported/unearned recommendation maturity')
    for field in ('rationale', 'model_review', 'uncertainty', 'decision_rule', 'source_qualification', 'cutoff_basis'):
        gate.text(r[field])
    if not isinstance(r['material_sources'], list) or not r['material_sources']:
        raise ValueError('material availability review sources required')
    for source in r['material_sources']:
        gate.keys(source, ['url', 'retrieved_at', 'finding'])
        gate.url(source['url']); gate.text(source['finding'])
        if gate.clock(source['retrieved_at']) > recorded: raise ValueError('material source acquired after review')
    if r['market'] not in ('SPREAD', 'TOTAL', 'MONEYLINE'): raise ValueError('unknown recommendation market')
    selections = ('over', 'under') if r['market'] == 'TOTAL' else ('away', 'home')
    if r['selection'] not in selections: raise ValueError('invalid recommendation selection')
    packet = r['market_reference']
    if any(packet.get(k) != r[k] for k in ('game_id', 'market', 'selection')):
        raise ValueError('review reference game/market/selection mismatch')
    if packet.get('kickoff_utc') != market_row['kickoff_utc'] or packet.get('kickoff_source_url') != market_row['kickoff_source_url']:
        raise ValueError('review/canonical kickoff binding mismatch')
    if gate.clock(packet['collection_end']) > recorded: raise ValueError('market source acquired after review')
    benchmark = reference(packet, as_of)
    if benchmark['status'] != 'STRUCTURALLY_QUALIFIED_DESCRIPTIVE_REFERENCE':
        raise ValueError('conditional review requires qualified non-Caesars reference constituents/clocks')
    limit = r['acceptable_number']
    gate.keys(limit, ['market', 'selection', 'line', 'minimum_price', 'direction'])
    if any(limit[k] != r[k] for k in ('market', 'selection')): raise ValueError('limit selection mismatch')
    gate.number(limit['minimum_price'], True)
    if limit['minimum_price'] is None: raise ValueError('minimum acceptable price required')
    expected_direction = 'PRICE_ONLY' if r['market'] == 'MONEYLINE' else 'AT_MOST' if r['selection'] == 'over' else 'AT_LEAST'
    if limit['direction'] != expected_direction: raise ValueError('incorrect line-limit direction')
    if r['market'] == 'MONEYLINE':
        if limit['line'] is not None: raise ValueError('moneyline has no points line')
    else:
        gate.number(limit['line'])
        if limit['line'] is None or (r['market'] == 'TOTAL' and limit['line'] <= 0): raise ValueError('acceptable points limit required')
    for key in ('acceptable_number', 'reconciliation_utc', 'planning_cutoff_utc', 'execution_window'):
        if row[key] != r[key]: raise ValueError('canonical decision differs from immutable review ' + key)
    if row['reason'] != r['rationale'] or row['cutoff_authority'] != 'REVIEW_EVIDENCED':
        raise ValueError('review rationale/cutoff authority mismatch')
    review_at, cutoff = map(gate.clock, (r['reconciliation_utc'], r['planning_cutoff_utc']))
    window = r['execution_window']; gate.keys(window, ['start_utc', 'end_utc'])
    start, end = map(gate.clock, (window['start_utc'], window['end_utc']))
    if not recorded <= start < end == cutoff < kickoff or not now < review_at <= cutoff or not now < end:
        raise ValueError('conditional review/validity cutoff expired or inconsistent')
    return r, benchmark


def display(row, market_row, model, as_of):
    r, benchmark = validate(row, market_row, model, as_of)
    limit = r['acceptable_number']
    number = '' if limit['line'] is None else f"{limit['direction']} {limit['line']:g}; "
    conditions = f"{r['selection']} {r['market']}; {number}minimum price {limit['minimum_price']:+d}; valid until {r['planning_cutoff_utc']}; VENUE_CONFIRMATION_PENDING; not a placed bet"
    conditions += '; uncertainty: '+r['uncertainty']
    context = f"REVIEW-EVIDENCED non-Caesars reference: {benchmark['operator_count']} operators; points {benchmark['reference_points']}; dispersion {benchmark['points_range']}; boundary {r['market_reference']['collection_end']}; source truth independently reviewed, not certified by renderer"
    context += '; prices at reference line '+str(benchmark['exact_reference_line_price_range'])+'; '+benchmark['price_comparison']
    for q in benchmark['constituents']:
        exclusion=' [EXCLUDED FROM REFERENCE]' if any(identity_key(s).startswith('caesars') for s in (q['book'],q['operator'])) else ''
        context += f"; {q['book']}{exclusion}: line {q['line']}, price {q['price']:+d}, retrieved {q['retrieved_at']}, updated {q['offer_updated_at']}, {q['source_url']}"
    return conditions, context
