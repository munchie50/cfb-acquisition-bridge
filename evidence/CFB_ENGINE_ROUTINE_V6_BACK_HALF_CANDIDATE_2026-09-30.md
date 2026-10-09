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


## 12. Failure-Class Closure and Representative-Load Gate — candidate addition 2026-10-03

Trigger: a material correction addresses infrastructure, persistence, scheduling, integration, producer behavior, or another mechanism whose failure can vary by payload, boundary condition, workload, timing, or downstream consumer.

A reproduction-specific PASS is not sufficient evidence that the failure class is closed.

Before using FIXED/CLOSED language for that class:
1. **Classify the failure envelope.** State what is actually proven and what remains unknown. Distinguish mechanism failure from payload/content envelope, scale, timing, concurrency, permission, stale-state, and downstream-integration possibilities when applicable.
2. **Test the corrected primitive.** Verify the smallest deterministic reproduction of the failed mechanism.
3. **Test material boundaries.** Exercise known materially different conditions that could reproduce the class, using existing evidence/static replay before creating live work. Do not claim a proprietary/opaque trigger more narrowly than evidence permits.
4. **Representative-load demonstration.** Execute the corrected path with a workload representative of real production complexity/size, not only a toy diagnostic. When only a natural scheduled event can supply the representative workload, status is DEMONSTRATION_PENDING.
5. **End-to-end demonstration.** For shared infrastructure, prove the correction through the complete affected producer-to-consumer path, including persistence/readback and terminal evidence required by that path.
6. **Independent reconciliation.** Compare expected vs actual identities, cardinalities, persistence locations, readbacks, terminal state, and any relevant invariants.
7. **Closure language discipline.** Until steps 1-6 applicable to the case pass, report the narrow proven state: e.g. PRIMITIVE_VERIFIED, BOUNDARY_TEST_PENDING, REPRESENTATIVE_LOAD_PENDING, END_TO_END_PENDING, or DEMONSTRATION_PENDING. Do not collapse these into FIXED.

If a later representative run exposes another failure mode in the same class, reopen the lifecycle record at the newly discovered causal layer rather than treating it as an unrelated surprise or merely stacking another patch.

This gate strengthens, and does not replace, v1.133 repeated-friction escalation and this candidate's existing Demonstration Gate.

### 2026-10-03 motivating case — Market Monitor persistence
- Toy/primitive evidence proved create_file/readback and SHA-guarded update_file/readback.
- A 07:19 CT real cycle reached RUN_PASS.
- A later 13:00 CT cycle exposed a connected write-safety/content-envelope rejection on a larger canonical mutation.
- A later minimal append to the same canonical file passed, ruling out persistent repository permission/branch/update-primitive failure but not identifying the opaque safety trigger.
- Correct classification after the minimal diagnostic is therefore **PRIMITIVE_VERIFIED / HARDENING_PERSISTED / REPRESENTATIVE_SCHEDULED_LOAD_DEMONSTRATION_PENDING**, not fully FIXED.
- Closure requires a subsequent representative scheduled Market Monitor cycle to persist/read back applicable canonical surfaces and Hot Sheet and end in a read-back terminal RUN_PASS under the hardened procedure.

Scientific effect: NONE.
Champion effect: NONE.


## 13. Time-Hidden Prior-Week Replay-Ahead Gate — candidate addition 2026-10-06

Purpose: use already-completed prior-week evidence to expose later-week operational defects before the current live week reaches the same frontier, without hindsight contamination.

When a completed prior football week has sufficient genuinely timestamped/frozen evidence, Test Routine v6 SHOULD run a bounded replay track in parallel with natural live confirmation.

### Replay controls
1. Freeze the replay start boundary. Identify the accepted pre-event prediction artifact, exclusions, source/market/decision artifacts, timestamps and producer authority that actually existed for the replayed week.
2. Time-hide future information. At each simulated checkpoint, expose only evidence whose authoritative timestamp is at or before that checkpoint. Final scores, later market observations/closing lines, later injuries/availability, execution evidence and postgame learning are prohibited before their historical availability boundary.
   - Mutable-artifact chronology rule: filename/path timestamp is not sufficient replay authority. For an artifact that can be updated in place, establish checkpoint eligibility from repository commit/blob history, explicit embedded boundary metadata, or a contemporaneous immutable receipt/reference. Quarantine current bytes containing later information from earlier simulated checkpoints; never reconstruct an earlier state from current mutable bytes unless history proves those exact bytes existed then.
3. Advance chronologically. Replay the governed weekly checkpoints in order, including source/candidate boundaries where applicable, Hot Sheet sectioning, market/decision updates, INCONCLUSIVE/WAIT maturity, practical execution cutoffs, persistence/readback, terminal closure and postgame learning.
4. Replay ahead of the live frontier. During a current week, preferentially replay prior-week stages that the current week has not yet reached when sufficient historical evidence exists. The objective is early defect discovery, not retrospective optimization.
5. Expected-vs-actual reconciliation. At each checkpoint compare expected inputs, producer/control behavior, identities/cardinalities, state transitions, persistence/readback and terminal state with what the historical path actually produced. A known historical defect is valid replay test evidence; do not rewrite history to make it pass.
6. Smallest correction and affected-segment rerun. A replay-detected procedural/control defect may justify the smallest non-scientific correction under existing authority, followed by rerun of the affected replay segment. Model/science/Champion/Challenger changes require their separate governance and are never authorized merely by replay error.
7. Separate proof classes. Record REPLAY_DEMONSTRATED separately from NATURAL_PRODUCTION_DEMONSTRATED. Replay can prove deterministic logic/control behavior against authentic historical evidence; it cannot by itself prove scheduler, current external-source, current connector, or other live production behavior.
8. No hindsight learning leakage. Outcomes may score genuinely frozen predictions after the simulated final boundary and may generate diagnostic hypotheses. They may not alter the replayed pre-event prediction, decision, market chronology, exclusions, or execution history.

### Replay demonstration record
A material replay must record replay week and immutable starting boundary; simulated checkpoints and evidence-visibility cutoff; hidden/prohibited future evidence classes; expected behavior; actual historical behavior; defects detected/prevented; corrections; affected-segment rerun result; proof classification; and remaining debt/natural trigger.

### Week 5 initial demonstration target
Use Week 5 as the first controlled replay because accepted v1.208 FIRST_FROZEN predictions and a complete 47-game postgame scorecard are durably recoverable, while known operational defects provide authentic detection targets. The first pass must test whether the replay control can surface known persistence/scheduled-completion, Hot Sheet/decision-maturity and end-stage reconciliation weaknesses without exposing Week 5 outcomes before their simulated final boundaries. Existing Week 5 outcomes are scoring/diagnostic evidence only after those boundaries.

This gate changes QA sequencing only. It does not change Production Routine v5, Champion v1.193, v1.208 frozen predictions, candidate acceptance, betting authority, execution history or scientific acceptance.

## 14. Review / Decision / Execution Timing Authority Check — candidate addition 2026-10-09

Trigger: classify a game review or decision as overdue, missing a deadline, or ready for an execution cutoff.

Recover the complete active boundary before the classification: decision-cadence contract and its accepted amendments, game-specific canonical ledger, authoritative kickoff/context and any actual execution-access constraint. Keep separate the initial review obligation, default decision-reconciliation deadline, effective game-specific deadline, and hard final execution cutoff. A review day passing does not prove that a later default deadline passed. A default does not override an earned earlier constraint or establish executable access. Missing clock detail in one ledger is not evidence that the governing contract lacks it.

Record unresolved effective deadlines/cutoffs explicitly. Do not derive a final execution cutoff from kickoff, invent an evening hour, or silently relax a missed earlier obligation. Fail closed on missing/ambiguous recovered authority.

Bounded demonstration: evidence/operational/CFB_WEEK6_OCT08_DECISION_LEDGER_COVERAGE_GAP_V6.md, October 9 morning correction. The corrected coverage helper requires recovered cadence authority and separately exposes review timing/default clocks. Eighteen authority, timing-boundary and CLI assertions passed. Friday five had a missed Thursday review day but a future default Friday 13:00 clock at the audited 07:27:26 CT boundary; effective earlier constraints and hard cutoffs remained uncertified.

This demonstrates a manual QA detection control, not an accepted betting decision, automated recurring integration, natural production success or routine promotion. Existing v1.237 authority and Production Routine v5 remain unchanged.

## 15. Composite Source Region / Chronology Gate — candidate addition 2026-10-09

Trigger: a fetched page or search excerpt combines a dated article, live navigation/scoreboard widgets, availability statements or market display, especially when an event/status conflicts with the observation clock.

Do not treat primary-domain provenance, successful fresh retrieval or the article publication date as chronology proof for every surrounding region. Qualify identity and time semantics per region. A score/final for a corroborated future kickoff is SOURCE_CHRONOLOGY_CONFLICT and is quarantined from outcome, availability inference and betting/model use pending independent resolution. Preserve the conflict; do not select the convenient region, manufacture a result, or infer health from absent search results.

A dated expected-absence report remains an expectation unless independently confirmed as current/final. Quote retrieval time remains distinct from book offer time. Keep qualified facts at their earned scope and maturity.

Manual demonstration: evidence/operational/CFB_WEEK6_OCT09_FRIDAY_PROSPECTIVE_BENCHMARK_AND_DECISION_REVIEW.md. Fresh BYU dated game-week page supplied a future kickoff but surrounding chrome displayed score-like output; that region was excluded. Opponent-authored availability expectations and the official Iowa kickoff-minute conflict remained unresolved. Five uniquely identified linked benchmark blocks passed 26 extraction/clock checks and were preserved separately from executable offers. No outcome or frozen prediction was changed.

Result: MANUAL_SOURCE_GATE_DEMONSTRATED; recurring producer enforcement and natural production acceptance remain pending. Production Routine v5 and scientific/Champion authority unchanged.

## 16. STARTED-only Runtime Evidence Recovery — candidate addition 2026-10-09

Trigger: a scheduled cycle has STARTED but no durable terminal evidence.

Recover the invocation's own response/error evidence, scheduler timestamps/state and exact repository receipts before describing it as slow, stuck or still running. Distinguish dispatch, reported runtime result, durable terminal persistence and future schedule enablement. Re-enabling a task is not evidence that an earlier run resumed. A reported terminal-write failure explains why a stopped invocation can remain STARTED-only; preserve that distinction without fabricating closure.

If response/trace access is unavailable, say runtime state is unverified rather than inferring activity from elapsed time. Current connector tooling exposes metadata, not an active-execution trace; recovered conversation output must be labelled separately from raw tool logs.

Demonstration: October 9 07:45 investigation in evidence/scheduler_qa/CFB_SCHEDULER_V6_OCT09_START_ONLY_AND_TASK_LIFECYCLE_REPAIR.md recovered the 07:04:52 response reporting incomplete writes and rejected terminal attempts, reconciling the 07:05 scheduler timestamp and later disabled state. Exact transcript retrieval failed; narrower payload/root-cause claims remain prohibited. Status: MANUAL_RECOVERY_DEMONSTRATED; production reliability remains OPEN.

## 17. Frozen versus operational clock authority — candidate addition October9

Trigger: original frozen timestamp conflicts with current schedule, a dated join/filter omits a game, or a source-clock label implies current kickoff authority. Preserve original bytes, recover exact game identity and separately qualified operational schedule. Compare explicit timezone-normalized timestamps; distinguish snapshot provenance, operational kickoff and independent execution clock. Do not use immutable FIRST_FROZENstart_date as operational deadline authority or reconstruct/replace predictions. Read-only date scoping must not silently drop identities whose original snapshot local date differs. Qualify known day/section at its earned scope while retaining unresolved exact-current-source conflicts.
Audit evidence/scheduler_qa/CFB_WEEK6_FROZEN_VERSUS_OPERATIONAL_CLOCK_AUDIT_2026-10-09.json, blob ddd3e4eedbc828b91fb6d35ba5c6b48511e1a2d9; run CFB_FROZEN_OPERATIONAL_CLOCK_QA_20261009T224139Z. Bounded49row audit found18exact matches and31local-date differences;38Saturdaygame-ID/time references matched retained research. Historical audit wordFrozen applied to saved schedule display, not originalCSV clock; provenance clarification recorded prospectively. No new current source fetch, source clock root-cause proof, deadline change, natural scheduler demonstration, productionRoutinev5promotion or scientific acceptance.
