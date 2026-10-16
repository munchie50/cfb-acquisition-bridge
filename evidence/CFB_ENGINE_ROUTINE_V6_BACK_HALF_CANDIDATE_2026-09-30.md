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


## 18. Recovery tail and declared review-scope reconciliation — candidate addition October 9

Trigger: recovery index receives a later material append or a user requests review of everything/a practical pre-trip card.

A latest explicitly tagged checkpoint is insufficient if newer index prose is silently ignored. Preserve old bytes and append a final reconciled cfb-frontier-json record with independently recovered pointer identities in the same complete mutation. Optional scripts/cfb_recovery_navigation_reader.py now rejects any non-whitespace after its last complete checkpoint; manually inspect full authority if rejected/runtime unavailable. Do not guess whether unclocked prose is immaterial, treat a reader-selected record as certified live state, or downgrade earlier incomplete runs.

Before a full-review claim, declare the expected current modeled identity set and requested markets, reconcile unique rendered/decision identities exactly once, and distinguish short ranked recommendations from full evaluated scope. A four-candidate review cannot stand for a 38-game board. Source URL inventory/naming/76 verdict count is not complete football or final availability verification; incomplete qualification remains explicit per row. Earlier practical sportsbook/travel cutoff can precede default cadence, but that is not an automatic bet or permission to loosen cutoffs. Controlled Beta uncertainty is not a requirement for perfect certainty.

Demonstration: evidence/scheduler_qa/CFB_DINNER_RECOVERY_TRAILING_UPDATE_GUARD_2026-10-09.md, blob b7c32b1142b37e1157c479641934537d9e8dbe3d. Actual prior index silently selected19:19 record despite19:53 dinner update; corrected source rejects it.16meaningful local regressions and independent GitHub run38011286883/job114091654286 PASS on exact read-back code. Actual current card38/38 identity union/76 verdicts/3conditional side recommendations/35sidePASS/38totalPASS and38rationale sections verified structurally; Caesars execution and final full-team availability remain unverified. New explicit index checkpoint is independently replayed/read back before closure. Candidate integration does not automatically install sportsbook-trip/full-slate enforcement in recurring task prompts; that producer obligation remains OPEN. Production Routine v5/model/Champion unchanged; natural consumer use pending.


### Section18 execution — full-slate scope and explicit trip-clock guard

evidence/scheduler_qa/CFB_FULL_SATURDAY_SCOPE_AND_TRIP_DEADLINE_GUARD_2026-10-09.md, blob af73e23d60731aeff36bcb915252a240378a36a0, run CFB_FULL_REVIEW_SCOPE_TRIP_GUARD_QA_20261010T010437Z. Read-only helper/test suite now built/executed/readbackverified and wired into EXISTING GitHubQA.16unitPASS; authentic narrowfourreport failsfullscope, full38report passes exactidentity/76verdict/38rationale structuralchecks. Syntheticearliertrip/default/explicitcutoff/tie/timezone tests provecomposition only; no actual user dinner cutoff invented. Activev1.237 clarifies existing earliestpracticaldeadline/fullscope-before-rankedlist rule. Taskprompt/cadence unchanged while eveningwindowactive; naturalconsumerusepending. This is candidateproceduraldemonstration, not productionroutine/science/bettingacceptance.


### Section18 execution — current decision projection
Recover evidence/scheduler_qa/CFB_HOT_SHEET_CURRENT_DECISION_PROJECTION_2026-10-09.md. Corrected full49weekly Hot Sheet now projects38Saturday/76canonical verdicts and exact3conditional line/price limits; original quote clocks retained. New bounded helper11tests and actual projection independently PASS in existing GitHub38012433466/job114095198628. Active presentation contract clarifies latest decision reconciliation, historical declared-blob recovery and conditional/unverified preservation. Built/executed/verified display fidelity is separate from natural producer use, book executability and final availability. Productionv5/Champion/science/task fields unchanged.


### Section18 execution — natural evening current-output discrepancy
Recover evidence/scheduler_qa/CFB_OCT09_EVENING_TERMINAL_AND_CURRENT_DISPLAY_RECONCILIATION.md. Natural20:19CT receipts completed two-phase persistence but claimedRUNPASS with laterFresnoWAIT ledger and olderBETNOWsheet. IndependentQA classifies current-output reconciliation incomplete, preserving original receipts. Manual2114CT49rowview corrects2conditional/1WAIT/35PASS and retainedprice/cutoff/quote clocks. Newcurrentbindinghelper8localchecks catches authenticstaleview; historical declaredblob audit doesnotprove lateststate. Activepresentationcontrol clarifies latestcanonicalbinding plus semantictransition reconciliation beforeRUNPASS. Naturalcorrecteduse/actualCaesars/finalavailability remainpending. Productionv5/Champion unchanged.


### Section18 execution — automatic current-publication binding
Recover evidence/scheduler_qa/CFB_CURRENT_HOT_SHEET_BINDING_CI_ENFORCEMENT_2026-10-09.md. Existing helper nowselects uniqueCURRENT_HOT_SHEET navigationrole, independentlymatches currentledgerpointer/sheetpointerbytes/declareddecision; historicalprojection remainsseparate.14regressions+authenticcurrentindexCLI PASS; GitHub38016732746/job114108548815 independentlySUCCESS at7040beacad92696cddb6dbdda7a087dd511ed51a, newbindingstepsPASS. Existingworkflow triggersledger/recoverychanges; no newworkflow/dispatch. Activecontract/currentindex integrated. Binding isnot renderedverdict/source/executionqualification; acceptedv1.245/knownschema qualifiedonly, futureauthoritychangesrequirequalification. Naturalcorrectedproduceruse pending; Productionv5/Champion unchanged.


### Section18 execution — Saturday source profile/current selected numeric audit
Recover evidence/scheduler_qa/CFB_SATURDAY_TOTAL_PROFILE_AND_CURRENT_SELECTION_QA_2026-10-10.md. AuthenticSaturdayboard previouslyunsupportedbyFriday-onlytotalgate; earliergreenCI sourcebindingandhistoricalbaseline didnotprovecurrentnumbers. SeparateSaturday38+Nebraska profilequalified, unknowncyclesfailclosed. Existingworkflowselectscurrentpointerforsection/frozen/totalsalongwithhistoricalbaseline.22boundarytests/actual38+1totals/frozen49/147/49/GitHub38063060107/job114245068955PASS;10:15viewcorrectsSaturdaycolumnretrievalclockonly. Source/bet/footballqualification remainsseparate;09AMQAblockedrununchanged/noretroclosure; futureproducerusepending. Productionv5/Champion unchanged.


### Section11 demonstration — original versus weekly prediction ancestry, October11

Trigger: SundayWeek7producer and boundedOctober6refreshQA treated pendingMonday/Tuesdayweeklycycle as absentWeek7Champion/FIRST_FROZEN. Firstpartialancestrycheck recoveredrefresh61+1 butnot originalfreeze; historicalChallengerB filename andweeklabel were insufficient authority. This incompleteclassification ispreserved, not silentlyrewritten.
Expectedcontrol: consumer requirement -> currentartifacts -> originalacceptedproducer/companiontarget/prediction/exclusionboundary -> naming/supersession -> separateacceptance evidence beforeclassifyingmissing.
Actual: recoveredacceptedoriginalrun36216090860/artifact10897612260 ZIP772b8683365ebf62d35fc3813beb138688b84af4172a0b261fd9218691d5adcf;622targets=526predictions+96exclusions overall; exact62Week7IDs=51originalpredictions+11originalexclusions. All4Tue/Wedoriginalpredictions exist. v1.222 establisheshistoricalChallengerB ascurrentBetaProductionChampion; v1.216 preserves originals; v1.247 weeklycadence doesnot eraseexistence. October6REFRESH61+1 remains separate;10originalexcludedtargets latereligible areNOT substituted.
Correction: appendonly canonicalancestryclarification with all62INCONCLUSIVEunchanged; prospectivecurrent1429CTview projects153numericfields/51favorite directions and11originalexclusions, unchanged13:05quotes/movement andunverifiedsavedplanningclocks. Originalviews/claims preserved. Activepresentationcontrol nowrequires originalacceptedboundarybeforeabsenceclassification;23mutation/numeric/exclusion/clocktests+12priorancestrytests installedinEXISTINGQA; no newtask/workflow.
Demonstration: independentlyrecoveredGitHub38168633837/job114556348721 at760ff6bc7652a709aea9b5f4539513d08b6614e9 SUCCESS, bothauthenticatedarchives,23tests,currentCLI51+11,currentbinding andretainedhistoricalchecksPASS. Authenticoldabsenceview rejected; expectedvsactual62identityunion and153numericfields/51directions PASS. Scope:MANUAL_AND_EXISTING_CI_DISPLAY_DEMONSTRATED, not naturalscheduledproducercompletion ornewscientificacceptance. Fullsourceidentities/report/readbacks persistedin CFB_WEEK7_FIRST_FROZEN_RECOVERY_QA_20261011T192933Z receipts/register.
Riskprevented: inventing/recomputing newpredictions tofill falsemissingdependency, suppressing acceptedFIRST_FROZEN, confusingrole with historicalfilename orreplacing exclusionswithlaterrefresh.
Remainingdebt: naturalproducer mustrecoverthecompleteboundary andcarryqualifiedclock/lineage labels atnextscheduledMarketMonitor. New weekly readiness/candidateacceptance, qualifiedconsensus/Caesars, actualcutoffs andbroadschedulerdebt remainOPEN. Productionv5 unchanged/v6candidate. No model,pointer,wager,cash,task orschedulestate changed.


## 19. Publication source-profile readiness before current-view selection — October12 candidate control

Trigger: a scheduled producer introduces a new dated Hot Sheet, source cycle, market schema or prediction consumer boundary.

Recover the actual selected-current-publication workflow route and its supported source profile before assuming a saved publication is qualified. File existence, source binding, exactly-once counts and a frozen-field-only PASS are necessary but do not establish full publication acceptance. Do not weaken the unknown-boundary rejection or add a filename-only allow rule. Qualify saved source identities, source role/availability, retained versus new quote clocks, conflict quarantine, movement ancestry, rendered decisions and practical-cutoff limits at the earned scope. Check producer status prose against the exact source-readiness/candidate/acceptance phase; copied prose can contradict a passed readiness step even while numerical fields are faithful.

When correcting a historical publication, preserve the original and select a prospective corrected display only after its source/decision binding and complete navigation proposal have passed. Keep a presentation correction separate from a new source fetch, model run, accepted snapshot, decision, wager or natural scheduled completion. Preserve every original incomplete cycle and intermediate CI failure. Bounded source profiles remain explicit; later source boundaries require qualification, never an unconditional wildcard acceptance.

October12 manual evidence: Monday13:05 dated publication was unsupported after decision binding and153original frozen fields passed. It also retained the stale sentence that Monday readiness was incomplete after source-preflight success. New18:28CT display corrects that sentence only; all62 nine-column game rows remain identical. scripts/cfb_week7_monday_publication_gate.py validates the exact canonical/source boundaries,62identity/section union,51original predictions+11exclusions,5qualified fallback updates,3withheld conflicts,7Monday quote-unavailable rows, retained movement/clock/cutoff and all62INCONCLUSIVE.20 local regression checks and actualCLI PASS; installed in EXISTING publication QA workflow. Independent CI and prospective natural-producer qualification remain separate proof requirements. Later source boundaries still fail closed; this is not general scheduler repair or tomorrow's readiness certification. Production Routine v5 remains active, Test Routine v6 candidate; no scientific/Champion/task/cadence change.


## 20. Stable source schemas instead of repeated date-pinned publication repairs — October12 candidate control

Trigger: the same publication/data consumer repeatedly fails when its date or canonical source blob advances although the semantic structure is still supported.

Separate immutable authority/identity ancestry from variable cycle/source data. Keep original model/first-observation lineage pinned to accepted bytes, but qualify a reusable typed semantic producer-consumer boundary rather than repeatedly allowlisting filenames or certifying current numbers from a prior display. Derive the entire rendered view from canonical source fields and compare it independently; source hashes alone and a freshly rendered document alone are insufficient. Unknown fields/states/authority remain failclosed. Track exactly which richer phases still require separate qualification; never discard earned facts, downgrade an actionable state, force PASS or omit started games to fit a narrower schema.

Historical regression fixtures must recover their exact immutable canonical blobs through the canonical Git history path once live ledgers advance; they cannot require tomorrow's current ledger to remain byte-identical to Monday. Preserve original failures and separate authentic-saved-data replay, synthetic boundary tests, helper/runtime installation and natural producer use. The first typed transition needs separately qualified authentic legacy/root ancestry. Never manufacture earliest observations when converting legacy data; a previously unavailable first may arise only prospectively after its documented unavailable boundary.

Demonstration: CFB_NEUTRAL_SOURCE_DERIVED_PUBLICATION_CONTRACT_2026-10-12.md and isolated saved-source normalization through scripts/cfb_neutral_publication_legacy_replay.py. Independent existingGitHub38324316715 at917125452a887a9752ea8f55b94ffe81e7e9207f passed54protocol/authentic tests, actual62-game source replay with55currentfallback/7unavailable, first/movement/source-precision/3diagnosticconflict handling and retainedQA. Currentcanonical/currentHotSheet/task/model/wager/cash unchanged. Stable route installed for supportedWeek7neutralpregame INCONCLUSIVE/PASS inputs only; exact original51+11census preserved. Natural typed-canonical source/write/render/index/closure adoption and richeractionable/consensus/verifiedoffer/postkickoff/futureweek support remainOPEN. ProductionRoutinev5 unchanged; candidatev6 notpromoted.


## 21. Full-week temporal coverage and executable reconciliation before writes — October15 demonstration

Trigger: repeated natural Monitor failures on untyped canonical tails after the pregame-only schema ceased to cover the complete weekly population.

Reconsider the entire required producer/consumer boundary before another narrow repair. A weekly sheet must retain started games and prior decisions as well as fresh future rows; a pregame schema cannot silently omit them. Qualify a separate full-week profile with independently proved historical PASS, explicitly historical last pre-event quotes, immutable known first observations, honest unknown first ancestry and quarantined conflicts. Keep clock upper bounds distinct from exact retrieval/bookmaker clocks. Never invent historical firsts, reconstruct a PASS after kickoff, discard raw conflicts or force a richer decision into a neutral schema to obtain a green gate.

Install an executable complete-response-plus-earned-decisions compiler and require it BEFORE canonical mutation, rather than relying on prose instructions to hand-create62 typed rows. The compiler must refuse missing/overdue decisions and stale source bounds, preserve closed PASS, validate the whole proposal, and leave GitHub writes/dispatch to the existing governed path. The next producer must reconcile downstream untyped tails before publication. Keep V1 failures and stricter unsupported-phase rejection intact.

Demonstration: user-directed CFB_TYPED_WEEKLY_RECONCILIATION_QA_20261016T023112Z; original-source bootstrap,70 current/new protocol checks,12 authentic original legacy checks and25 full-board checks passed. Prospective2142CT manual correction persisted/read back62games,55INCONCLUSIVE+7PASS,one quarantined direction conflict and three still-unknown firsts. Independent accepted archive preserved51predictions+11exclusions,153numericfields and51favorite directions. Existing GitHub38842011110/job116784020457 atd5eebabe2ff17b2e0c5a841103e9d7dc0e5c2248 SUCCESS; logs independently recovered; actual selected sheet7089e9253ce6bca81210f3227e7b0d1e748f78ad passed canonical binding, whole-renderV2 and original-archive invariant along with retained regressions.

Intermediate binding failures during serialized source/view/index installation remain failures. Accepted market write initially read the prior blob; exact-commit/main read-only reconciliation succeeded without repeating the mutation. The current source compiler/contract/readbacks and manual CI demonstration close this presentation defect at the earned scope. They do not upgrade any natural incomplete cycle or establish scheduled producer adoption. Friday07:00CT must demonstrate fresh capture, producer-earned decisions, complete typed compilation, writes/readbacks, selected current display and honest closure naturally. Active ProductionRoutinev5/Champion/task cadence remain unchanged; v6 remains candidate.


### Section21 integration — scheduled invocation runtime versus manual CLI

User-directed QA CFB_MONITOR_COMPILER_INTEGRATION_QA_20261016T025016Z found the existing Monitor task did not explicitly name the new compiler/runtime preflight. Preserved its entire existing prompt and appended the active-control/runtime/normal-mode/compiler-before-write requirement; independent inventory verifies exactly4enabled recurring tasks and every schedule/timezone/timing/enabled/ownership field unchanged. Actual Python3.12.14 manual CLI normal-advance, renderer and separate audit passed62games using retained-source data and explicitly hypothetical next-cycle test clocks; no fixture was written operationally. The manual entrypoint result is not proof that the scheduled invocation has computation. Natural runtime availability must be checked there; unavailable means COMPUTATION_RUNTIME_UNAVAILABLE/RUN_INCOMPLETE, never pretend execution or substitute untyped publication writes. Installation/direct task linkage/natural adoption remain distinct. Generic downstream-tail reconciliation remains explicitly OPEN: the current compiler rejects arbitrary untyped tails and no prompt change makes that semantic adapter exist. An accidentally future-dated start marker is preserved as invalid, superseded by observed-clock identity; derive run identities from actual runtime clocks rather than entering a future timestamp. Productionv5/Champion unchanged.
