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


MARKETS = ('FAVORITE_SPREAD', 'UNDERDOG_SPREAD', 'AWAY_MONEYLINE',
           'HOME_MONEYLINE', 'OVER', 'UNDER', 'ALTERNATE_SPREADS',
           'ALTERNATE_TOTALS', 'TEAM_TOTALS', 'PARLAY_SUITABILITY')


def evaluation_coverage(census, decisions, rows):
    """Account for every identity without treating PASS as completed research.

    Canonical packets do not encode a full analytical PASS review. Its absence
    here means not certified, never proof that no review exists elsewhere.
    Conditional references remain references, not an independent source audit.
    """
    by_id = {r['game_id']: r for r in rows}
    if len(by_id) != len(rows) or set(by_id) != set(census) or set(decisions) != set(census):
        raise ValueError('coverage requires complete unique census/decision/row identities')
    groups = {name: [] for name in ('ORIGINAL_EXCLUSION', 'HISTORICAL_GAP',
                                   'CONDITIONAL_REVIEW_REFERENCE', 'NOT_CERTIFIED')}
    pending = []
    for gid, model in census.items():
        state = decisions[gid]['state']
        if model['first_frozen_status'] != 'PREDICTION':
            category = 'ORIGINAL_EXCLUSION'
        elif state == 'HISTORICAL_GAP':
            category = 'HISTORICAL_GAP'
        elif state == 'CONDITIONAL' and decisions[gid].get('review_ref'):
            category = 'CONDITIONAL_REVIEW_REFERENCE'
        else:
            category = 'NOT_CERTIFIED'
        groups[category].append(gid)
        by_id[gid]['evaluation_coverage'] = category
        by_id[gid]['saved_reason'] = decisions[gid]['reason']
        window = by_id[gid]['review_window']
        if category == 'NOT_CERTIFIED' and window['review_required']:
            pending.append({'game_id': gid, 'state': state,
                            'review_due_by_utc': window['review_due_by_utc'],
                            'timing_issue': window['timing_issue'],
                            'next_action': ('QUALIFY_TIMING_BEFORE_REVIEW'
                                            if window['timing_issue'] else
                                            'RECOVER_OR_COMPLETE_REVIEW_EVIDENCE')})
    # Unknown timing is explicit work debt; it cannot silently sort past all
    # deadlines. Known deadlines use qualified clock ordering, not text offsets.
    pending.sort(key=lambda r: (r['review_due_by_utc'] is not None,
                               gate.clock(r['review_due_by_utc']).timestamp()
                               if r['review_due_by_utc'] else 0, r['game_id']))
    return {'total_games': len(census),
            'counts': {k: len(v) for k, v in groups.items()},
            'game_ids': groups, 'uncertified_open_review_queue': pending,
            'scope': 'PACKET_EVIDENCE_ACCOUNTING_NOT_FULL_RESEARCH_CERTIFICATION',
            'not_certified_meaning': 'REVIEW_NOT_PROVED_BY_PACKET; MAY_EXIST_IN_SEPARATE_EVIDENCE',
            'conditional_reference_meaning': 'REFERENCE_PRESENT; NOT_ALL_MARKETS_OR_FRESHNESS_CERTIFIED',
            'historical_backfill_authorized': False}


def review_window(decision, market, as_of):
    """Keep every state in the review pool until its existing betting cutoff.

    This is work selection, not a new decision/transition rule. Missing timing
    stays visible as work debt; it never authorizes a late recommendation.
    Reconciliation deadlines do not silently become final execution cutoffs.
    """
    now = gate.clock(as_of)
    cutoff = decision.get('planning_cutoff_utc')
    kick = market.get('kickoff_utc')
    qualified_kick = kick is not None and market.get('kickoff_status') == 'QUALIFIED'
    bounds = ([gate.clock(cutoff)] if cutoff else [])
    if qualified_kick:
        bounds.append(gate.clock(kick))
    closed = decision['state']=='HISTORICAL_GAP' or (bool(bounds) and min(bounds) <= now)
    issue = ('KICKOFF_REQUIRES_QUALIFICATION' if not qualified_kick else
             'PRACTICAL_CUTOFF_MISSING' if cutoff is None else None)
    disposition = ('PREGAME_WINDOW_CLOSED' if closed else
                   'PASS_FOR_NOW_REEVALUATE' if decision['state'] == 'PASS' else
                   'REEVALUATE_CURRENT_DECISION')
    return {'review_required': not closed, 'disposition': disposition,
            'review_due_by_utc': min(bounds).isoformat().replace('+00:00', 'Z') if bounds else None,
            'timing_issue': issue,
            'markets_to_review': list(MARKETS) if not closed else [],
            'scope': 'REVIEW_SELECTION_ONLY_NOT_REOPEN_AUTHORITY'}


def audit(market, decision, lineage, as_of, profile='WEEK7'):
    """Diagnose the bounded neutral profile from canonical packets, not prose.

    This profile cannot prove completed football/rule reviews. Do not infer
    them from a model number, a generic pending reason or an HTTP success.
    """
    now = gate.clock(as_of)
    selected = gate.selected_block(market, gate.profile_config(profile)['market_tag'],
                                   (gate.MARKET_SCHEMA, gate.WEEKLY_MARKET_SCHEMA), now)
    # Prove the saved publication at its own boundary, then diagnose age at the
    # actual audit clock. An old pregame row is stale, not permission to retime
    # its source, silently accept it as current, or reconstruct a decision.
    saved_at = selected['as_of_utc']
    m, d, census, markets, decisions = gate.inputs(market, decision, lineage, saved_at, profile)
    rows = []
    counts = Counter()
    elapsed_current = []
    overdue = []
    for gid, model in census.items():
        row = decisions[gid]
        source = markets[gid]
        if row['state']=='HISTORICAL_GAP':
            rows.append({'game_id':gid,'state':'HISTORICAL_GAP',
                         'recommendation_blockers':['PERMANENT_PRE_EVENT_HISTORY_GAP'],
                         'disposition':'MISSING_HISTORY_NOT_A_PASS_OR_RECOMMENDATION'})
            continue
        if source['current'] is not None and source['kickoff_utc'] is not None and gate.clock(source['kickoff_utc']) <= now:
            elapsed_current.append(gid)
        if row['state'] in ('INCONCLUSIVE','REVIEW_OVERDUE') and gate.clock(row['reconciliation_utc']) <= now:
            overdue.append(gid)
        if row['state'] == 'PASS':
            rows.append({'game_id': gid, 'state': 'PASS',
                         'recommendation_blockers': [],
                         'disposition': 'PASS_FOR_NOW_REEVALUATE'})
            continue
        if row['state'] == 'CONDITIONAL':
            rows.append({'game_id': gid, 'state': 'CONDITIONAL',
                         'recommendation_blockers': [],
                         'disposition': ('HISTORICAL_CONDITIONAL_WINDOW_CLOSED' if gate.closed_conditional(row,as_of) else 'REVIEW_EVIDENCED_CONDITIONAL_NOT_VERIFIED_EXECUTION'),
                         'review_ref': row['review_ref'], 'venue_confirmation': 'PENDING'})
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
    for row in rows:
        gid = row['game_id']
        window = review_window(decisions[gid], markets[gid], as_of)
        row['review_window'] = window
        if row['state'] == 'PASS':
            row['disposition'] = window['disposition']
    review_ids = [r['game_id'] for r in rows if r['review_window']['review_required']]
    coverage = evaluation_coverage(census, decisions, rows)
    return {'schema': 'CFB_NEUTRAL_READINESS_AUDIT_V1',
            'scope': 'READ_ONLY_DIAGNOSTIC_NOT_DECISION_OR_SOURCE_QUALIFICATION',
            'as_of_utc': as_of, 'canonical_cycle': m['cycle_id'],
            'canonical_as_of_utc': saved_at,
            'saved_state_validated_at_own_boundary_only': True,
            'elapsed_current_quote_game_ids': elapsed_current,
            'overdue_open_decision_game_ids': overdue,
            'market_blob': gate.blob(market), 'decision_blob': gate.blob(decision),
            'lineage_blob': gate.blob(lineage), 'games': len(rows),
            'open_games': sum(r['state'] in ('INCONCLUSIVE','REVIEW_OVERDUE') for r in rows),
            'preserved_pass': sum(r['state'] == 'PASS' for r in rows),
            'historical_gaps': sum(r['state'] == 'HISTORICAL_GAP' for r in rows),
            'conditional_recommendations': sum(r['state'] == 'CONDITIONAL' for r in rows),
            'recommendation_blocker_counts': dict(sorted(counts.items())),
            'caesars_required_for_recommendation': False,
            'publication_capability': 'CONDITIONAL_V3_SUPPORTED_WAIT_ADAPTER_OPEN',
            'review_required_game_ids': review_ids,
            'pass_for_now_game_ids': [r['game_id'] for r in rows
                                     if r['state'] == 'PASS' and r['review_window']['review_required']],
            'review_schedule': 'EXISTING_CYCLES_PLUS_FINAL_REVIEW_BEFORE_EXISTING_CUTOFF',
            'review_coverage': 'NOT_CERTIFIED_BY_QUEUE_MEMBERSHIP',
            'evaluation_coverage': coverage,
            'rows': rows}


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('market', 'decision', 'lineage'):
        p.add_argument('--' + name, type=Path, required=True)
    p.add_argument('--as-of', required=True)
    p.add_argument('--profile', choices=('WEEK7','WEEK8','WEEK9'), default='WEEK7')
    args = p.parse_args()
    print(json.dumps(audit(args.market.read_text(), args.decision.read_text(),
                           args.lineage.read_text(), args.as_of, args.profile), indent=2))
