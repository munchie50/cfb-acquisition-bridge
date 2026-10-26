"""Bounded recognition of the proved Week9 missed research deadline.

REVIEW_OVERDUE is unfinished work, never an earned PASS, WAIT or recommendation.
The original missed deadline is retained; no replacement deadline is created.
"""
import json
import re
from pathlib import Path
from functools import lru_cache

ROOT=Path(__file__).resolve().parents[1]
AUTHORITY_PATH='evidence/CFB_WEEK9_MISSED_REVIEW_DISPOSITION_2026-10-26.json'
AUTHORITY_SHA='72655649b230413c91c106e3df902a9716d313aa'
STATE='REVIEW_OVERDUE'


@lru_cache(maxsize=4)
def context(decision, raw):
    import cfb_neutral_publication_gate as g
    a=json.loads(raw,object_pairs_hook=g.unique)
    tag=g.profile_config('WEEK9')['decision_tag']
    packets=list(re.finditer(r'^```'+tag+r'\n(.*?)^```[ \t]*$',decision,re.M|re.S))
    recovered=[m for m in packets if any(r.get('state')==STATE for r in json.loads(m[1],object_pairs_hook=g.unique)['rows'])]
    if not recovered:raise ValueError('missing review-overdue origin')
    first=recovered[0]
    prefix=decision[:first.start()]
    if g.blob(prefix)!=a['parent_decision_blob']:raise ValueError('unqualified missed-review parent')
    parent=g.selected_block(prefix,tag,g.WEEKLY_DECISION_SCHEMAS,g.clock(json.loads(first[1])['as_of_utc']))
    if parent['cycle_id']!=a['parent_cycle']:raise ValueError('missed-review parent cycle differs')
    old={r['game_id']:r for r in parent['rows']}
    bound={r['game_id']:r for r in a['rows']}
    if len(bound)!=56 or set(bound)!=set(old):raise ValueError('incomplete missed-review identity union')
    for gid,r in old.items():
        b=bound[gid]
        if (r['state']!='INCONCLUSIVE' or b['prior_row_blob']!=g.blob(json.dumps(r,sort_keys=True,separators=(',',':'))) or
                r['reconciliation_utc']!=a['missed_reconciliation_utc'] or
                any(b[k]!=r[k] for k in ('reconciliation_utc','planning_cutoff_utc'))):
            raise ValueError('missed-review original row changed')
    return a,bound


def validate(row, source, decision, as_of, profile):
    import cfb_neutral_publication_gate as g
    if profile!='WEEK9':raise ValueError('review-overdue disposition qualified for Week9 only')
    raw=(ROOT/AUTHORITY_PATH).read_text()
    if g.blob(raw)!=AUTHORITY_SHA:raise ValueError('missed-review authority changed')
    a,bound=context(decision,raw)
    b=bound[row['game_id']]
    if (row['state']!=STATE or row['reconciliation_utc']!=b['reconciliation_utc'] or
            row['planning_cutoff_utc']!=b['planning_cutoff_utc']):
        raise ValueError('missed review deadline/cutoff cannot be removed or extended')
    if (row['cutoff_authority']!='UNVERIFIED' or row['acceptable_number'] is not None or
            row['execution_window'] is not None or row.get('review_ref') is not None):
        raise ValueError('overdue research cannot claim recommendation/execution authority')
    now=g.clock(as_of)
    if not g.clock(a['missed_reconciliation_utc'])<=g.clock(a['recorded_at_utc'])<=g.clock(row['state_recorded_at_utc'])<=now:
        raise ValueError('overdue recognition must be prospective after missed deadline')
    if source['kickoff_utc'] is None or g.clock(source['kickoff_utc'])<=now:
        raise ValueError('review-overdue route cannot reconstruct elapsed-game decisions')
    g.text(row['reason'])
    return a
