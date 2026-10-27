"""Week9 exact four-case history status; never a past or active recommendation.

The first recognition must be prospective before the saved kickoff. Subsequent
packets retain the exact recognition, including after kickoff. Immutable review
bytes and actual Git ancestry remain independently enforced by load_review.
"""
import copy
import json
import re
import cfb_neutral_publication_gate as gate
from cfb_conditional_recommendation_profile import load_review

STATE = 'EXPIRED_UNPUBLISHED_REVIEW'
LINEAGE = '57afbbbc65d58d9ee739bcb2823685e3fc0a5cb9'
PRIOR_BLOB = '5df8464b0b2372134939cf81d576e155d641113b'
PRIOR_BYTES = 1504623
TAG = 'cfb-week9-decision-v1'
TRUSTED = {'401856842': {'path': 'evidence/operational/recommendation_reviews/CFB_ARIZONA_PRICE_CONDITIONAL_20261027T015520Z.json', 'commit': 'a0ecea22136f4945e046be2043f6dad7c7dee930', 'blob': 'e096376b2343667fc28b36c1f643b30ea1f854f9', 'committed_at': '2026-10-27T02:06:37Z'}, '401856848': {'path': 'evidence/operational/recommendation_reviews/CFB_CINCINNATI_CONTROLLED_BETA_20261027T015520Z.json', 'commit': '2928ff585df588489ad55fb05af7e196a3e5269e', 'blob': 'f270892ad49f6f3c19e051bb75a4763e5a98a0fb', 'committed_at': '2026-10-27T02:15:34Z'}, '401862812': {'path': 'evidence/operational/recommendation_reviews/CFB_FLORIDA_ATLANTIC_CONTROLLED_BETA_20261027T013124Z.json', 'commit': '6a3cda95cfb0ba40edfc7179172bdeda198d0bb5', 'blob': '9547eb01aad7d2272679de20c61c9c79c2b0f7c7', 'committed_at': '2026-10-27T01:36:36Z'}, '401871058': {'path': 'evidence/operational/recommendation_reviews/CFB_MIDDLE_TENNESSEE_CONTROLLED_BETA_20261026T234404Z.json', 'commit': '37f0e3edf5b09afdc4f05e14e5a70b6d4fa91ab3', 'blob': 'd0a4620f56a84b96931df1dfa8f843324ef58212', 'committed_at': '2026-10-26T23:44:05Z'}}

def packets(content):
    return [json.loads(m[1], object_pairs_hook=gate.unique) for m in re.finditer(
        r'^```'+TAG+r'\n(.*?)^```[ \t]*$', content, re.M|re.S)]


def review_for(ref, game_id):
    trusted=TRUSTED.get(game_id)
    if trusted is None or ref != {k:trusted[k] for k in ('path','commit','blob')}:
        raise ValueError('outside four authorized expired unpublished reviews')
    content, committed = load_review(ref)
    if gate.blob(content) != trusted['blob'] or gate.clock(committed) != gate.clock(trusted['committed_at']):
        raise ValueError('expired unpublished immutable bytes/commit clock mismatch')
    review=json.loads(content, object_pairs_hook=gate.unique)
    if (review['schema']!='CFB_PROSPECTIVE_CONDITIONAL_REVIEW_V2' or review['state']!='CONDITIONAL'
            or review['game_id']!=game_id or review['original_lineage_blob']!=LINEAGE):
        raise ValueError('expired unpublished review identity/schema mismatch')
    return review, committed


def decision_row(game_id):
    trusted=TRUSTED.get(game_id)
    if trusted is None: raise ValueError('outside four authorized expired unpublished reviews')
    ref={k:trusted[k] for k in ('path','commit','blob')}
    review,_=review_for(ref,game_id)
    return dict(game_id=game_id, state=STATE, reason=review['rationale'],
                reconciliation_utc=review['reconciliation_utc'],
                planning_cutoff_utc=review['planning_cutoff_utc'],
                cutoff_authority='REVIEW_EVIDENCED',
                acceptable_number=copy.deepcopy(review['acceptable_number']),
                execution_window=copy.deepcopy(review['execution_window']), review_ref=ref)


def validate(row, source, model, packet, decision, profile):
    if profile!='WEEK9' or model['first_frozen_status']!='PREDICTION':
        raise ValueError('expired unpublished status requires authorized Week9 prediction')
    if row['state']!=STATE: raise ValueError('expired unpublished state mismatch')
    review,committed=review_for(row['review_ref'],row['game_id'])
    expected=decision_row(row['game_id'])
    if {k:v for k,v in row.items() if k not in ('state_recorded_at_utc','state_evidence')}!=expected:
        raise ValueError('expired unpublished original review fields changed')
    raw=decision.encode('utf-8')
    try: prior=raw[:PRIOR_BYTES].decode('utf-8')
    except UnicodeDecodeError as exc: raise ValueError('expired unpublished canonical prior bytes changed') from exc
    if gate.blob(prior)!=PRIOR_BLOB:
        raise ValueError('expired unpublished canonical prior bytes changed')
    history=packets(decision)
    origins=[p for p in history if p['cycle_id']==row['state_evidence']]
    if len(origins)!=1: raise ValueError('expired unpublished recognition origin missing')
    origin=origins[0]
    matches=[r for r in origin['rows'] if r['game_id']==row['game_id']]
    if matches!=[row] or origin['as_of_utc']!=row['state_recorded_at_utc']:
        raise ValueError('expired unpublished recognition changed')
    before=[p for p in history if gate.clock(p['as_of_utc'])<gate.clock(origin['as_of_utc'])]
    if not before: raise ValueError('expired unpublished prior decision missing')
    earlier=[r for p in before for r in p['rows'] if r['game_id']==row['game_id']]
    if (not earlier or earlier[-1]['state']!='INCONCLUSIVE'
            or any(r.get('review_ref') is not None or r['state']!='INCONCLUSIVE' for r in earlier)):
        raise ValueError('review already published or previous state changed')
    trusted=TRUSTED[row['game_id']]
    if trusted['path'] in prior or trusted['blob'] in prior:
        raise ValueError('review already referenced in canonical prior')
    recorded,commit,review_at,cutoff,recognized,now=map(gate.clock,(
        review['recorded_at_utc'],committed,review['reconciliation_utc'],
        review['planning_cutoff_utc'],row['state_recorded_at_utc'],packet['as_of_utc']))
    kickoff=gate.clock(review['market_reference']['kickoff_utc'])
    if not recorded<=commit<review_at<=cutoff<=recognized<kickoff or recognized>now:
        raise ValueError('expired unpublished recognition chronology invalid')
    window=review['execution_window']
    if not recorded<=gate.clock(window['start_utc'])<gate.clock(window['end_utc'])==cutoff:
        raise ValueError('expired unpublished original execution window invalid')
    if source['kickoff_utc']!=review['market_reference']['kickoff_utc']:
        raise ValueError('expired unpublished saved kickoff changed')
    return review
