# CFB Engine Routine v6 Candidate — Back-Half Reconciliation, Demonstration, Monitoring — 2026-09-30

Status: CANDIDATE / TEST PROCEDURAL CONTROL
Production/master routine remains v5. v4 remains stable fallback.
Scope: procedural only; no model/science/Champion/Challenger promotion.

## Why this exists
Production v5 made authority recovery, execution, audit, persistence/readback, integration debt and stopping materially stronger. Current operations have now reached a phase where the dominant residual risk is later in the lifecycle: a correction can be documented or installed without being demonstrated through the real producer path and independently reconciled before closure.

This candidate strengthens that back half without weakening or reordering v5's front half.

## Candidate sequence
Retain production v5 through Correct and Verify, then apply:
Correct
-> Verify Producer
-> Persist + Readback Verify
-> Demonstration Gate
-> Reconcile Expected vs Actual
-> Monitor Invariants / Exceptions
-> Closure-Debt Check
-> Integration-Debt Check
-> Stop/Transition Check
-> Repeat.

Existing v5 controls remain mandatory.

## 1. FIX -> VERIFY PRODUCER
After a material defect, do not stop at repairing the visible artifact.
Identify the authoritative producer/path that created it and determine whether that producer can recreate the defect.
A correction is not structurally complete until either:
- the producer/control is corrected and verified, or
- evidence proves the artifact was a one-off external failure not reproducible by the producer.
Preserve the defective artifact/evidence when required for audit.

## 2. Demonstration Gate
Material corrections progress through explicit states:
CORRECTED -> PERSISTED -> READ_BACK -> DEMONSTRATED -> INDEPENDENTLY_RECONCILED -> CLOSED.

A correction may not be called CLOSED merely because code, task text, documentation or an artifact changed.
DEMONSTRATED requires the corrected behavior to execute through the applicable real path.
Where live execution is not necessary, a deterministic static/replay demonstration against existing authoritative evidence is preferred.
Do not manufacture extra live runs solely to satisfy ceremony when existing evidence can prove the control.
If a future event is genuinely required, record DEMONSTRATION_PENDING and the natural next trigger.

## 3. Expected-vs-Actual Reconciliation
For every material governed run/boundary, define and reconcile, as applicable:
- expected authoritative inputs;
- expected producer/path;
- expected output identities;
- expected cardinalities/population;
- expected persistence locations;
- expected readback evidence;
- expected terminal state.
Compare expected with actual. Cardinality and identity invariants outrank visual plausibility.
Any unresolved mismatch is explicit debt and prohibits unsupported completion claims.

## 4. MONITOR means invariants and exceptions
Monitoring is not repeated manual inspection of everything.
Define stable invariants and surface exceptions, including as applicable:
- expected scheduled cycle with no RUN_STARTED;
- RUN_STARTED with no conforming terminal receipt;
- RUN_PASS without required canonical persistence/readback;
- governed population count != rendered/accepted population count;
- duplicate or omitted identity;
- stale WAIT/INCONCLUSIVE past governed deadline/cutoff;
- candidate generated without independent acceptance;
- accepted artifact/pointer without persistence/readback proof;
- output relying on superseded authority;
- disabled/temporary control accidentally treated as production authority.
Normal invariant satisfaction should remain quiet; exceptions should be prominent and actionable.

## 5. Lightweight Closure/Debt Ledger
Each material defect or correction should have one lifecycle record, embedded in an existing checkpoint/incident/receipt when practical rather than creating document sprawl:
Issue -> Root Cause -> Correction -> Producer Control -> Demonstration Required -> Demonstration Evidence -> Independent Reconciliation -> CLOSED.
Open items are demonstration/closure debt. Do not rediscover them as new work.

## 6. Stronger WAIT -> SWEEP
A legitimate WAIT triggers bounded independent work before idling:
1. open demonstration/closure debt;
2. integration debt and stale recovery pointers;
3. monitoring/invariant gaps;
4. temporary/disabled controls that could be mistaken for authority;
5. lessons documented but not installed;
6. independent QA/reconciliation work not dependent on the awaited event.
Do not manufacture runs, observations, model candidates, decisions or outcomes merely to create work.

## 7. Repeated-friction escalation
Retain v1.133 repeated-failure control and strengthen timing:
when the same material friction recurs or a correction fails to close its producer path, investigate structural cause before another equivalent retry.
Install a prevention/detection control and demonstrate it.

## 8. Run minimization / proof reuse
Prefer proof reuse in this order:
1. existing authoritative persisted evidence;
2. deterministic static validation;
3. deterministic replay using already-captured inputs;
4. natural next scheduled/qualified run;
5. extra live run only when the prior four cannot establish the required behavior and the run is safe/governed.
Never create extra market/model/outcome observations solely for procedural proof.

## 9. Closure rule
CLOSED requires:
- root cause sufficiently classified;
- correction persisted/read back;
- producer/path addressed;
- applicable demonstration passed;
- expected-vs-actual reconciliation passed;
- independent verification completed when required;
- no unresolved material closure debt.
If a natural future run is required, status remains DEMONSTRATION_PENDING, not failed and not closed.

## Candidate shorthand
WAIT -> SWEEP
CHANGE -> RECONSIDER
CLAIM COMPLETION -> PROVE
REPEATED FAILURE -> INVESTIGATE SYSTEM
FIX -> VERIFY PRODUCER -> DEMONSTRATE -> RECONCILE -> CLOSE

## Candidate evaluation
Test this candidate first against existing real CFB operational/rebuild evidence. Do not promote it to production/master routine until demonstrated across materially different cases and explicitly authorized under routine governance.
