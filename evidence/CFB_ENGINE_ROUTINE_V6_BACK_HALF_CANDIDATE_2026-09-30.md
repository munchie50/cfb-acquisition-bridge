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


## 10. Routine-Control Demonstration Record
Whenever a new or modified routine control is under test, successful use alone is not sufficient to mark it DEMONSTRATED. The test must explicitly surface and persist, in a bounded demonstration record or appropriate existing checkpoint:
- trigger / starting state;
- expected control behavior;
- actual observed behavior;
- work, defect or risk detected/prevented;
- expected-vs-actual reconciliation;
- demonstration result;
- remaining debt and natural next trigger, if any.

The demonstration record must distinguish USING a control from PROVING the control behaved as intended. A control cannot receive DEMONSTRATED status from implicit success.

When authentic evidence already exists, use it; do not rerun operational work solely to make the demonstration visible.


## 11. Interface / Boundary Ancestry Check
Before classifying a required field, capability or interface as missing, trace the complete accepted boundary:
1. consumer requirement;
2. current artifact(s);
3. authoritative producer;
4. companion outputs produced by the same accepted path;
5. acceptance/reconciliation evidence for those outputs.

Absence from one artifact is not evidence that the capability is absent from the accepted boundary. Treat a governed interface as potentially composite until producer ancestry and companion outputs prove otherwise.

Only after this bounded ancestry check fails may the routine classify the requirement as genuinely missing and authorize a new interface/substrate correction.

Do not respond to a single-artifact absence by guessing, duplicating derivation, reopening a lower-authority/raw source, or extending an accepted interface unless the ancestry check establishes that such a correction is actually required.

### Demonstration — v1.246 S2_K1 role/venue interface
Trigger: prospective S2_K1 consumer construction found `side` on the accepted team-side substrate but not `venue_state` and initially classified the consumer interface as incomplete.

Expected behavior under this control: recover the accepted v1.246 producer and companion boundaries before declaring a new interface requirement.

Observed behavior after ancestry recovery:
- the accepted team-side ledger/substrate already carries explicit `side = home|away`, team identity, target kickoff, prior-game count and 17 raw features;
- the accepted target ledger carries game identity, home/away teams, `neutral_site`, population and kickoff;
- the authoritative v1.246 producer deterministically derives `venue_state = NEUTRAL|HOME` from that accepted target boundary and uses it for the frozen `venue_neutral` model term;
- therefore the accepted interface is composite and no new venue source or team-side schema extension is required.

Risk prevented: unnecessary mutation of an accepted substrate, duplicate venue derivation from lower-authority data, or reopening raw schedule data merely because one companion artifact did not contain every consumer field.

Expected vs actual: PASS.
Demonstration result: `INTERFACE_BOUNDARY_ANCESTRY_CHECK = DEMONSTRATED_PASS` for this case.

Remaining debt: correct the prospective S2_K1 consumer to compose the accepted team-side substrate with the accepted target ledger and statically reconcile their identities before any live execution.
