"""Bounded descriptive consensus formatter; no odds acquisition or betting rule.

The caller independently qualifies source truth, identities and operator
independence. Unknown bookmaker clocks remain unknown; retrieval is not update.
"""
import argparse
import json
from pathlib import Path
from statistics import median
import cfb_neutral_publication_gate as gate


def reference(packet, as_of):
    gate.keys(packet, ['game_id', 'market', 'selection', 'period',
                       'kickoff_utc', 'kickoff_source_url', 'collection_start', 'collection_end', 'quotes'])
    gate.text(packet['game_id']); gate.text(packet['selection'])
    if packet['market'] not in ('SPREAD', 'TOTAL', 'MONEYLINE') or packet['period'] != 'PREGAME_FULL_GAME':
        raise ValueError('unsupported market/period')
    start, end, now = map(gate.clock, (packet['collection_start'], packet['collection_end'], as_of))
    if not start <= end <= now:
        raise ValueError('invalid/future collection window')
    kickoff = gate.clock(packet['kickoff_utc']); gate.url(packet['kickoff_source_url'])
    if end >= kickoff: raise ValueError('postkickoff collection is not pregame')
    if not isinstance(packet['quotes'], list): raise ValueError('quotes must be list')
    eligible = {}; excluded = []; reasons = set()
    if now >= kickoff: reasons.add('AT_OR_AFTER_KICKOFF')
    for q in packet['quotes']:
        gate.keys(q, ['game_id', 'market', 'selection', 'period', 'book', 'operator',
                      'operator_evidence_url', 'source_url', 'retrieved_at',
                      'offer_updated_at', 'line', 'price'])
        for k in ('game_id', 'market', 'selection', 'period'):
            if q[k] != packet[k]: raise ValueError('quote identity/selection/period mismatch')
        gate.text(q['book']); gate.text(q['operator'])
        gate.url(q['source_url']); gate.url(q['operator_evidence_url'])
        at = gate.clock(q['retrieved_at'])
        if not start <= at <= end: raise ValueError('retrieval outside collection window')
        gate.number(q['price'], True)
        if q['price'] is None: raise ValueError('missing paired price')
        if packet['market'] == 'MONEYLINE':
            if q['line'] is not None: raise ValueError('moneyline must not invent a points line')
        else:
            gate.number(q['line'])
            if q['line'] is None or (packet['market'] == 'TOTAL' and q['line'] <= 0):
                raise ValueError('missing/invalid points line')
        # Book and operator labels must both be checked; don't let a skin label
        # accidentally introduce Caesars into the non-Caesars benchmark.
        if any(s.casefold().startswith('caesars') for s in (q['book'], q['operator'])):
            excluded.append({'book': q['book'], 'reason': 'CAESARS_EXCLUDED'}); continue
        if q['offer_updated_at'] is None:
            reasons.add('OFFER_UPDATE_UNKNOWN')
        else:
            updated = gate.clock(q['offer_updated_at'])
            if updated > at: raise ValueError('offer update after retrieval')
            if updated < start: reasons.add('OFFER_UPDATE_OUTSIDE_COLLECTION_WINDOW')
        operator = q['operator'].casefold()
        if operator in eligible and (q['line'], q['price']) != (eligible[operator]['line'], eligible[operator]['price']):
            raise ValueError('conflicting same-operator observations require reconciliation')
        eligible.setdefault(operator, q)
    if len(eligible) < 3: reasons.add('FEWER_THAN_THREE_INDEPENDENT_OPERATORS')
    quotes = list(eligible.values())
    points = [q['line'] for q in quotes] if packet['market'] != 'MONEYLINE' else []
    value = median(points) if points else None
    prices = [q['price'] for q in quotes if value is not None and q['line'] == value]
    return {'status': 'CONSENSUS_UNAVAILABLE' if reasons else 'STRUCTURALLY_QUALIFIED_DESCRIPTIVE_REFERENCE',
            'scope': 'CALLER_MUST_QUALIFY_SOURCE_TRUTH_AND_OPERATOR_INDEPENDENCE_NOT_BETTING_AUTHORITY',
            'reference_boundary_utc': packet['collection_end'],
            'audit_as_of_utc': as_of, 'current_freshness_certified': False,
            'reasons': sorted(reasons), 'operator_count': len(quotes),
            'reference_points': value, 'points_range': [min(points), max(points)] if points else None,
            'reference_is_executable_offer': False,
            'exact_reference_line_price_range': [min(prices), max(prices)] if prices else None,
            'price_comparison': 'ACTUAL_QUOTES_AT_REFERENCE_LINE_ONLY' if prices else 'PRICE_NOT_COMPARABLE',
            'moneyline_probability': None, 'constituents': packet['quotes'], 'excluded': excluded}


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input', type=Path, required=True); p.add_argument('--as-of', required=True)
    args = p.parse_args()
    print(json.dumps(reference(json.loads(args.input.read_text(), object_pairs_hook=gate.unique), args.as_of), indent=2))
