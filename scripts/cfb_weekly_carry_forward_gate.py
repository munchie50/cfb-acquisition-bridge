"""Read-only exact October11 weekly carry-forward correction, not outcome acceptance."""
import argparse, hashlib, json
from pathlib import Path

ORIGINAL_SHA='31d72be8927068879c9f5cf867c65eec3b8ff5e0'
LINEAGE_SHA='d80e26c398de48e7a386ad9a627fe44f4111ac45'
HEALTH_SHA='6b1097abd4cb082a1e60e4d1f09573576d804001'
CURRENT_SHEET_SHA='71006586178a1829c51f119fff872b6f981cd865'
R2='evidence/CFB_ENGINE_WEEKLY_BETA_LEARNING_REVIEW_2026-10-11_R2.md'
WEEK7_REVIEW='evidence/CFB_ENGINE_WEEKLY_BETA_LEARNING_REVIEW_2026-10-18_R1.md'
WEEK7_REVIEW_SHA='89d646b66ad845ef1f00985ae55ef88cabba92b6'

def blob(s):
    b=s.encode();return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

OLD_EXEC='The current Week 7 Sunday Hot Sheet was independently read back at blob b0131986d8bf6c0f3f964852a362eecf4a4b4b6f: 62 unique games, zero duplicates, section union 62, Nebraska included. It honestly carries **no earned Week 7 Engine Prediction (Frozen)** before Monday readiness / Tuesday candidate and independent acceptance. Every current market row is a labelled CBS mixed-book fallback; **CONSENSUS_UNAVAILABLE** and **Caesars UNVERIFIED** are preserved.'
NEW_EXEC='The original accepted September26 FIRST_FROZEN covers all62 currentWeek7 identities: **51 immutable predictions and11 explicit original exclusions**, including original predictions for all4Tuesday/Wednesday games. Historical ChallengerB is the active BetaProductionChampion under v1.222. The current manual14:29CT HotSheet at '+CURRENT_SHEET_SHA+' displays that original lineage; market retrieval remains13:05CT. Accepted October6 REFRESH covers61 predictions+1 exclusion and never substitutes for an original prediction/exclusion. Monday readiness/Tuesday candidate is a separate coming weekly cycle, not proof that original predictions are absent. All62 decisions remain INCONCLUSIVE, **CONSENSUS_UNAVAILABLE** and **Caesars UNVERIFIED**; saved practical clocks are UNVERIFIED / CUTOFF_AUTHORITY_UNVERIFIED. Natural corrected producer use remains DEMONSTRATION_PENDING.'
REPLACEMENTS=[
    (OLD_EXEC,NEW_EXEC),
    ('| Sunday Market Monitor persisted full Week 7 opening state and two-phase closure | Operations control success | Canonical/Hot Sheet/receipt readbacks passed | Natural current-cycle evidence exists without repairing older gaps |',
     '| Sunday Market Monitor persisted full Week 7 opening state and two-phase closure | Durable persistence present; natural output semantic fidelity UNVERIFIED | Original absence claim was false; later manual51+11 correction is separate | Original natural cycles remain unresolved; do not retroactively upgrade |'),
    ('The successful current Sunday Market Monitor is useful natural evidence but does not erase prior start-only/incomplete cycles.',
     'Sunday Market Monitor durable receipt chains are natural persistence evidence only; their false Week7 absence claims remain semantic defects. The later manual correction does not retroactively validate either natural cycle or erase prior start-only/incomplete cycles.'),
    ('| W6-L9 | Week 7 Sunday opening board completed 62/62 → operations success | Current natural path passed | Monitor repeated natural cycles | Sustained readback/closure evidence | MONITOR |',
     '| W6-L9 | Week7 durable62-game board but false FIRST_FROZEN absence → carry-forward/producer semantic defect | Original51predictions+11exclusions already existed; partial boundary recovery caused the claim | Current manual display corrected; original natural receipts preserved | Next natural producer must demonstrate complete ancestry and faithful output | OPEN / NATURAL_PRODUCER_PENDING |'),
    ('Current-cycle persistence and two-phase closure can succeed naturally, while earlier incomplete cycles and missing decision evidence remain honestly unresolved.',
     'Current-cycle persistence and two-phase closure can occur naturally without proving semantic fidelity: both Sunday views omitted existing original prediction lineage. Manual correction is bounded proof; natural corrected use and earlier incomplete cycles remain unresolved.'),
]

def expected(original,lineage,health):
    if blob(original)!=ORIGINAL_SHA or blob(lineage)!=LINEAGE_SHA or blob(health)!=HEALTH_SHA:
        raise ValueError('unqualified source byte identity')
    j=json.loads(lineage);rows=j['rows']
    if len(rows)!=62 or len({r['game_id'] for r in rows})!=62:
        raise ValueError('lineage identity union mismatch')
    if sum(r['first_frozen_status']=='PREDICTION' for r in rows)!=51 or sum(r['first_frozen_status']=='EXCLUDED' for r in rows)!=11:
        raise ValueError('first-freeze partition mismatch')
    if sum(r['oct6_refresh_status']=='PREDICTION' for r in rows)!=61 or sum(r['oct6_refresh_status']=='EXCLUDED' for r in rows)!=1:
        raise ValueError('refresh partition mismatch')
    if not all(r['first_frozen_status']=='PREDICTION' for r in rows[:4]):raise ValueError('early-week coverage mismatch')
    result=original
    for old,new in REPLACEMENTS:
        if result.count(old)!=1:raise ValueError('unsupported parent semantic boundary')
        result=result.replace(old,new,1)
    result=result.replace('— 2026-10-11 — R1','— 2026-10-11 — R2',1)
    result=result.replace('Status: AUTHORITATIVE SUNDAY LEARNING OUTPUT CANDIDATE','Status: PROSPECTIVE MANUAL CARRY-FORWARD CORRECTION — NOT A REPLAY OF SUNDAY QA',1)
    result=result.replace('Run identity: CFB_WEEKLY_QA_20261011T135620Z','Source run identity: CFB_WEEKLY_QA_20261011T135620Z (historical, unchanged)',1)
    preface='''## Prospective correction and Champion/Challenger status

This R2 prospectively supersedes only R1 Week7 carry-forward and natural-output-success classification. Original R1 at '''+ORIGINAL_SHA+''' and all natural receipts remain immutable. Week6 performance, 49 game-level rows, wager comparisons, results, limits and accounting are copied unchanged; no new outcome join, numerical model audit, financial allocation or acceptance is performed.

BetaProductionChampion v1.193 remains frozen. Original FIRST_FROZEN and accepted October6 S0 REFRESH are separate; S2_K1 remains study-only with no accepted prospective prediction set. Neither this correction nor a successful candidate job promotes a model or authorizes a bet. Newly recovered original prediction availability is not new model creation.

Health audit '''+HEALTH_SHA+''' / closure13775259fa2c3be8c36473b5067647e635014abd honestly retained RUN_INCOMPLETE. Both Sunday natural Monitor cycles and Sunday QA carry-forward remain historically defective; the current manual correction is not retroactive producer acceptance. BigNine/private-Yahoo authority and older receipt gaps stay open.

Changed: false blanket Week7 absence statement, overstated Sunday semantic-success claims and W6-L9 closure disposition. Deliberately unchanged: all Week6 numeric/evaluation/execution/accounting content, model, accepted pointer, market, current HotSheet, all62INCONCLUSIVE decisions, thresholds, cash and four task configurations. No new review or cutoff clock is invented.

Machine source boundary: original review '''+ORIGINAL_SHA+'''; original lineage census '''+LINEAGE_SHA+'''; current HotSheet '''+CURRENT_SHEET_SHA+'''. Guard scope is this exact qualified R1-to-R2 correction; later sources/weeks require separate qualification. Manual/current-CI proof is separate from NATURAL_PRODUCER_DEMONSTRATION_PENDING.

'''
    return result.replace('## 1. Executive state',preface+'## 1. Executive state',1)

def audit(review,original,lineage,health):
    result=expected(original,lineage,health)
    if review!=result:raise ValueError('carry-forward/unchanged-learning/source/closure projection mismatch')
    return {'verdict':'PASS_BOUNDED_WEEKLY_CARRY_FORWARD_ONLY','review_blob':blob(review),
            'original_review_blob':ORIGINAL_SHA,'lineage_blob':LINEAGE_SHA,'health_blob':HEALTH_SHA,
            'first_frozen_predictions':51,'first_frozen_exclusions':11,'refresh_predictions':61,'refresh_exclusions':1,
            'week6_49_game_rows_and_numeric_content':'UNCHANGED_FROM_R1',
            'scope':'carry-forward fidelity only; no new scoring/model/operational acceptance; historical failures preserved, natural producer pending'}

def bind(index,review,lineage,health,as_of):
    from cfb_recovery_navigation_reader import read
    pointers=read(index,as_of)['frontier']['pointers']
    selected=[p for p in pointers if p['purpose'].startswith('CURRENT_WEEKLY_REVIEW:')]
    # Navigation may advance to this independently recovered weekly closure.
    # The exact R1->R2 semantic audit above remains historical and unchanged.
    supported={R2:blob(review), WEEK7_REVIEW:WEEK7_REVIEW_SHA}
    if len(selected)!=1 or supported.get(selected[0]['path'])!=selected[0]['blob']:
        raise ValueError('missing/ambiguous/stale current weekly review selector')
    historical=[p for p in pointers if p['path']==R2]
    if len(historical)!=1 or historical[0]['blob']!=blob(review):
        raise ValueError('missing/stale historical weekly correction')
    for path,text in [('evidence/operational/CFB_WEEK7_ORIGINAL_FIRST_FROZEN_LINEAGE_2026-10-11.json',lineage),('evidence/scheduler_qa/CFB_DUAL_ENGINE_HEALTH_20261011T215456Z_AUDIT.md',health)]:
        matches=[p for p in pointers if p['path']==path]
        if len(matches)!=1 or matches[0]['blob']!=blob(text):raise ValueError('stale weekly source pointer')
    return {'current_weekly_review_blob':selected[0]['blob'],'binding_scope':'navigation/source only, not operational acceptance'}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for n in ('review','original','lineage','health'):p.add_argument('--'+n,required=True,type=Path)
    p.add_argument('--index',type=Path)
    a=p.parse_args();texts=[getattr(a,n).read_text() for n in ('review','original','lineage','health')]
    result=audit(*texts)
    if a.index:
        from datetime import datetime,timezone
        result.update(bind(a.index.read_text(),texts[0],texts[2],texts[3],datetime.now(timezone.utc).isoformat()))
    print(json.dumps(result,indent=2))
