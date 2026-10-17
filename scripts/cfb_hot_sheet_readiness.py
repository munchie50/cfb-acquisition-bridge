"""Read-only bottleneck audit. Never creates a recommendation or execution.

Recommendation review and venue confirmation are deliberately separate. Earned
review inputs are caller assertions requiring independent governed evidence;
this helper checks completeness, not their truth or scientific acceptance.
"""
import argparse
import json
from collections import Counter
from pathlib import Path
import cfb_neutral_publication_gate as gate

REVIEW_FIELDS = ('model_review', 'market_reference', 'material_review',
                 'line_price_limits', 'practical_cutoff', 'decision_rule')
STATUS = ('EARNED', 'MISSING', 'UNREVIEWED')


def assess(review, venue_verified=False):
    """Return missing recommendation prerequisites, never BET NOW or a stake."""
    gate.keys(review, REVIEW_FIELDS)
    if type(venue_verified) is not bool:
        raise ValueError('venue verification must be boolean')
    if any(value not in STATUS for value in review.values()):
        raise ValueError('unknown readiness status')
    blockers = [name.upper() + '_' + review[name]
                for name in REVIEW_FIELDS if review[name] != 'EARNED']
    return {'recommendation_review_complete': not blockers,
            'recommendation_blockers': blockers,
            'venue_confirmation': 'VERIFIED' if venue_verified else 'PENDING',
            'scope': 'COMPLETENESS_ONLY_NOT_RECOMMENDATION_OR_EXECUTION_AUTHORITY'}


def audit(market, decision, lineage, as_of):
    """Diagnose the bounded neutral profile from canonical packets, not prose.

    This profile cannot prove completed football/rule reviews. Do not infer
    them from a model number, a generic pending reason or an HTTP success.
    """
    now = gate.clock(as_of)
    selected = gate.selected_block(market, gate.MARKET_TAG,
                                   (gate.MARKET_SCHEMA, gate.WEEKLY_MARKET_SCHEMA), now)
    # Prove the saved publication at its own boundary, then diagnose age at the
    # actual audit clock. An old pregame row is stale, not permission to retime
    # its source, silently accept it as current, or reconstruct a decision.
    saved_at = selected['as_of_utc']
    m, d, census, markets, decisions = gate.inputs(market, decision, lineage, saved_at)
    rows = []
    counts = Counter()
    elapsed_current = []
    overdue = []
    for gid, model in census.items():
        row = decisions[gid]
        source = markets[gid]
        if source['current'] is not None and source['kickoff_utc'] is not None and gate.clock(source['kickoff_utc']) <= now:
            elapsed_current.append(gid)
        if row['state'] == 'INCONCLUSIVE' and gate.clock(row['reconciliation_utc']) <= now:
            overdue.append(gid)
        if row['state'] == 'PASS':
            rows.append({'game_id': gid, 'state': 'PASS',
                         'recommendation_blockers': [],
                         'disposition': 'PRESERVE_CLOSED_PASS'})
            continue
        review = {name: 'UNREVIEWED' for name in REVIEW_FIELDS}
        # Qualified consensus cannot be represented by this neutral market
        # schema. A fallback observation is retained, never renamed consensus.
        review['market_reference'] = 'MISSING'
        if model['first_frozen_status'] != 'PREDICTION':
            review['model_review'] = 'MISSING'
        if row['acceptable_number'] is None:
            review['line_price_limits'] = 'MISSING'
        if row['cutoff_authority'] == 'UNVERIFIED':
            review['practical_cutoff'] = 'MISSING'
        result = assess(review)
        counts.update(result['recommendation_blockers'])
        rows.append({'game_id': gid, 'game': model['away_team'] + ' @ ' + model['home_team'],
                     'state': row['state'], 'review': review,
                     'reconciliation_utc': row['reconciliation_utc'],
                     'planning_cutoff_utc': row['planning_cutoff_utc'],
                     'source_type': (markets[gid]['current'] or markets[gid]['retained'] or {}).get('source_type'),
                     **result})
    return {'schema': 'CFB_NEUTRAL_READINESS_AUDIT_V1',
            'scope': 'READ_ONLY_DIAGNOSTIC_NOT_DECISION_OR_SOURCE_QUALIFICATION',
            'as_of_utc': as_of, 'canonical_cycle': m['cycle_id'],
            'canonical_as_of_utc': saved_at,
            'saved_state_validated_at_own_boundary_only': True,
            'elapsed_current_quote_game_ids': elapsed_current,
            'overdue_open_decision_game_ids': overdue,
            'market_blob': gate.blob(market), 'decision_blob': gate.blob(decision),
            'lineage_blob': gate.blob(lineage), 'games': len(rows),
            'open_games': sum(r['state'] == 'INCONCLUSIVE' for r in rows),
            'preserved_pass': sum(r['state'] == 'PASS' for r in rows),
            'recommendation_blocker_counts': dict(sorted(counts.items())),
            'caesars_required_for_recommendation': False,
            'publication_capability': 'NEUTRAL_ONLY_RICHER_RECOMMENDATION_ADAPTER_OPEN',
            'rows': rows}


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('market', 'decision', 'lineage'):
        p.add_argument('--' + name, type=Path, required=True)
    p.add_argument('--as-of', required=True)
    args = p.parse_args()
    print(json.dumps(audit(args.market.read_text(), args.decision.read_text(),
                           args.lineage.read_text(), args.as_of), indent=2))
