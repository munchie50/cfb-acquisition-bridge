# CFB Engine — Review Findings and Durable Action Register — 2026-09-28

Status: ACTIVE REVIEW/ACTION REGISTER
Scope: findings from the bounded historical-integrity, whole-engine seam, production-operations, technical-debt, recovery/governance, and cold-recovery reviews. This record does not change Champion/model/scientific authority.

## Confirmed healthy / closed findings
1. Historical/model seams are strongly reconciled: 7,701-game population -> 15,402 team-sides -> 6,246 eligible + 1,455 excluded -> 4,700 TRAIN + 1,546 spent/corroborative -> v1.193 fit -> 2026 prospective lineage.
2. v1.193 correctly repaired v1.184 evidence-transcription errors without refitting; accepted artifacts outrank prose.
3. 2026 FIRST_FROZEN lineage is independently reproducible and immutable under v1.208/v1.215/v1.216.
4. Current `.github/workflows/Main.yml` is path-limited/manual; the earlier concern that it broadly triggers on nearly every main push is stale historical debt, not current debt.
5. QA performance optimization materially reduced candidate generation from >90 minutes to about 19 minutes to the cardinality gate; Run #12 comparison found no evidence that the optimization introduced the S2 semantic defect.

## QA Sandbox findings
A. Full execution history Runs #1–#12 and Run #12 root cause are now reconciled in `evidence/CFB_QA_SANDBOX_EXECUTION_ATTEMPT_LEDGER_2026-09-28.md`.
B. Current Sandbox recovery doorway is `evidence/CFB_QA_SANDBOX_CURRENT_CHECKPOINT_2026-09-28.md`.
C. Stale S2 inner exception handling was confirmed causal for Run #12's excess omissions and boundedly corrected on main commit `2f8aad0963d6a09ae9b8eb749163f3ff65d3566a`; corrected generator blob `40447984a58dbc530cbe942bc1176f0c5bcbe9b2`.
D. CLOSED: corrected generator identity was observed/pinned and fresh candidate freeze accepted from run 36421939025; artifact 10970862853.
E. CLOSED: historical outcome scoring was separately authorized, executed by run 36491252415, independently reproduced, and accepted as valid evidence. S2_K1 alone continues to prospective Sandbox study; no promotion.

## Production operational findings — open durable actions
1. **Controlled execution reconciliation:** the canonical execution ledger currently lacks the previously established 2026-09-26 controlled executions. Reconcile only from original screenshot/evidence records; do not backfill from memory. Preserve downstream/execution-only classification and prohibit model contamination.
2. **Closing-market surface:** recovery authority says prediction, market, decision, execution, close and outcome must remain separate, but the canonical operational surfaces currently provide no dedicated durable closing-market ledger. Establish an append-only close surface with qualified source/timestamp semantics and no retrospective substitution when genuine close was not captured.
3. **Terminal receipt closure:** a reviewed Sunday-market receipt declared RUN_PASS while its own persistence/readback section still described same-commit creation/readback as pending. Strengthen terminal semantics so RUN_PASS is issued only after applicable surfaces and the terminal receipt itself have persisted/readback proof; use a closure/finalization pattern rather than optimistic certification.
4. **2026-09-28 market-monitor persistence:** the 07:00 CT run correctly remained RUN_INCOMPLETE when canonical mutation was blocked. Do not reconstruct or smuggle those observations into authoritative history. Handle future observations prospectively after the write path is valid.
5. **Sunday Early Board evidence:** verify exact persisted location/readback/closure before treating the earlier RUN_PASS receipt as fully reconciled.

## Recovery/governance findings
1. Current production recovery is usable from v1.245, but the QA doorway was stale before this reconciliation. The current Sandbox checkpoint now includes a staleness rule: terminal external run or superseded parent -> reconcile before following NEXT.
2. Operating procedure should be explicit at recovery surfaces: Production Routine v5 (v1.103) + active learning rule v1.132 + active execution controls v1.133.
3. Shared Universal Project Standards v1.4 does not silently alter CFB authority. Perform a bounded CFB applicability review and record adopt/defer/not-applicable for material v1.4 changes.
4. Recovery must not rely on code-search indexing or conversation memory; direct repository enumeration/readback remains authority.

## Technical-debt classification
HIGH: production close-market durable surface.
HIGH: terminal receipt/readback closure semantics.
RESOLVED: corrected S2 generator identity/pinning/fresh freeze.
MEDIUM: controlled execution ledger reconciliation from original evidence.
MEDIUM: permanent diagnostic ergonomics so cardinality failures expose actual family counts/omissions before generic assertion without weakening fail-closed gates.
LOW/RESOLVED: broad Main.yml trigger concern (current trigger is already bounded).
DO NOT WEAKEN: generator/input identity controls despite controlled-stop workflow noise.

## Required closure discipline
For each open action:
- preserve predecessor evidence;
- make the smallest bounded correction;
- keep scientific/model authority unchanged unless separately governed;
- persist and directly read back the changed surface;
- record demonstration evidence before classifying the lesson LEARNED.

This register is an action/review record, not authorization for outcome access, model tuning, Champion mutation, Challenger promotion, destructive cleanup, or retrospective manufacture of missing pre-event evidence.


## Scheduler/output ownership incident review — 2026-09-29

### Incident
The governed Hot Sheet existed and was successfully produced on the 2026-09-27 Sunday Market run, but its continuing in-week refresh responsibility became operationally orphaned.

### Evidence chain
1. The 2026-09-27 13:13 CT Sunday Market run completed the 47-game Week 5 sweep, persisted market and decision state, created the Sunday Early Board, and explicitly named continued scheduled market monitoring/deeper reconciliation as the next safe action.
2. The 2026-09-28 07:00 CT Market Monitor found material fresh Week 5 information but canonical mutation was blocked. It correctly terminated RUN_INCOMPLETE and explicitly required prospective persistence plus rerun of the Early Board/Hot Sheet completion gate.
3. The failed Monday observation itself remains non-authoritative and must not be reconstructed.
4. During later scheduler consolidation the CFB Market Monitor was paused while other tasks retained only partial market/availability/health responsibilities. No control verified that the Hot Sheet's end-to-end owner had become disabled.
5. The result was not loss of the frozen model or canonical Sunday evidence. It was loss of continuing output ownership: ingredients continued to exist, but no enabled task was explicitly responsible for assembling and delivering the governed Hot Sheet through Saturday.

### Root cause classification
- PRIMARY: scheduler/output ownership gap during task consolidation.
- CONTRIBUTING: Monday persistence failure left an explicit recovery action pending.
- CONTRIBUTING: task prompts overlapped on market/availability/health but did not define producer-vs-consumer ownership clearly enough.
- CONTRIBUTING: prior Hot Sheet delivery wording emphasized Sunday/Monday instead of an explicit daily through-Saturday refresh requirement.
- NOT CAUSAL: Champion/model failure, prediction contamination, or loss of FIRST_FROZEN evidence.

### Corrections installed
- CFB Market Monitor restored as the sole primary Hot Sheet producer and runs 07:00/13:00 CT Sunday-Saturday.
- Active output contract now explicitly requires daily Hot Sheet refresh through Saturday.
- Evening Availability is downstream incremental availability/wager management and must persist material changes for the next Market Monitor; it does not own a competing Hot Sheet.
- Dual Engine Health is an integrity/readback layer and must detect failed/incomplete prerequisite runs rather than silently duplicate them.
- Dual Weekly Engine QA consumes the latest Hot Sheet/market/decision state for Saturday/Sunday CFB QA; Tuesday CFB model/data candidate generation remains repository-automation owned.
- Stale fixed recovery-version anchors were removed from the four active task prompts; each must discover current repository authority.

### Durable control — required for future scheduler/cadence changes
Any enable/disable, schedule change, consolidation, split, rename, or responsibility transfer involving an operational task must perform an OUTPUT OWNERSHIP / COVERAGE CHECK before the change is considered complete:
1. enumerate required recurring outputs and governed surfaces;
2. identify exactly one primary producer/owner for each output and any downstream consumers;
3. verify every required owner remains enabled on a cadence capable of meeting the active contract;
4. verify dependency order and avoid competing baselines;
5. inspect unresolved RUN_INCOMPLETE/RUN_FAIL receipts whose next-safe-action depends on the changed task;
6. after mutation, re-enumerate active tasks and prove no required output is orphaned;
7. preserve one intentionally open task slot when the user's four-active-task operating constraint applies.

A scheduler consolidation is not complete merely because the desired number of tasks is active. Coverage and ownership must also pass.

### Disposition
CORRECTED / DEMONSTRATION PENDING. The structural correction is installed in task ownership and prompts. Demonstration requires successful prospective Market Monitor runs that persist/read back current state and surface the Hot Sheet under the corrected cadence. Do not mark LEARNED until demonstrated.


## Hot Sheet chronological decision-window correction — 2026-09-29

### User-facing problem
A single mixed Hot Sheet made near-term Thursday/Friday games compete visually with larger Saturday model-market disagreements, and INCONCLUSIVE did not have an explicit enforced maturity deadline.

### Correction
Active output/decision controls now require:
- chronological NEXT-UP sections for Thursday, Friday, Saturday morning, Saturday afternoon, and Saturday evening/night;
- all governed games in the applicable chronological section regardless of normal priority rank;
- earliest active section visually first;
- PRIORITY WATCHLIST retained separately across days;
- FULL WEEKLY SLATE retained so no game disappears;
- label Engine Prediction (Frozen) to distinguish the locked Engine fair line from sportsbook market lines;
- every INCONCLUSIVE receives a kickoff-window reconciliation deadline;
- deadline transition is actionable / governed WAIT with explicit trigger + hard final cutoff / PASS; a deadline never forces a wager;
- final practical execution cutoff resolves WAIT to actionable or PASS;
- decision windows remain separate from execution-trip planning and must not manufacture extra trips.

### Default CT reconciliation windows
- Thursday: final governed Market Monitor pass that still leaves practical pre-kickoff execution opportunity; normally 13:00 CT if safely pre-kickoff, otherwise earlier.
- Friday: normally 13:00 CT, earlier when kickoff/execution requires.
- Saturday before 12:00 CT: Friday evening availability review, or last Friday Market Monitor if no evening review applies.
- Saturday 12:00–16:59 CT: Saturday 07:00 CT Market Monitor.
- Saturday 17:00 CT or later: Saturday 13:00 CT Market Monitor.

### Ownership / contamination check
- Sole Hot Sheet producer remains CFB Market Monitor.
- CFB Evening Availability is downstream and persists canonical state for the next Market Monitor; it does not create a competing Hot Sheet.
- Dual Engine Health remains integrity-only.
- Dual Weekly Engine QA remains consumer/QA.
- Four-active-task / one-open-slot constraint remains satisfied.
- Frozen Champion/model predictions, Tuesday candidate automation, FIRST_FROZEN chronology, market append-only chronology, and scientific authority are unchanged.
- Market/injury/wager/execution/outcome evidence remains downstream and cannot alter Engine Prediction (Frozen).

### Disposition
INSTALLED / DEMONSTRATION PENDING. Demonstrate on the next scheduled Hot Sheet cycle and verify chronological sections, deadline fields, state transitions, canonical readback, and task ownership before classifying LEARNED.


## October 4 QA continuation — execution reconciliation evidence gate — 2026-10-05

### Finding
The canonical CFB_EXECUTION_LEDGER remains empty of the previously established Sep. 26 / Oct. 2 actual wager executions. A bounded recovery sweep found no original ticket image/evidence object in the repository tree and no recoverable original ticket file in current Project/Library file search. The active v1.224 screenshot boundary permits routing sufficiently established screenshot observations to the execution ledger, but the execution ledger itself explicitly prohibits backfill from memory.

### Disposition
BLOCKED ON ORIGINAL EVIDENCE / NO CANONICAL MUTATION.
- Do not populate exact line, odds, stake, timestamp, ticket state, settlement, or game identity into the canonical ledger from conversation memory alone.
- Do not reinterpret the missing execution evidence as proof that no wagers occurred.
- Do not use execution/ticket information as Champion model input, fitting/calibration evidence, or retrospective decision reconstruction.
- When original ticket evidence becomes directly recoverable, route it observation-by-observation through v1.224 and append only established fields.

### Routine classification
This is a genuine external-evidence gate for this action, not a reason to stop independent QA work. Bug #3 remains OPEN/EVIDENCE-BLOCKED.


## October 4 QA continuation — closing-market durable surface — 2026-10-05

### Correction
Established evidence/operational/CFB_CLOSING_MARKET_LEDGER.md as the prospective append-only CLOSE surface required by v1.226. Initialization deliberately contains no hindsight Week 5 closing lines. Missing historical qualified closes remain CLV UNVERIFIED.

### Verification
Create-file persistence succeeded and direct repository readback confirmed ACTIVE append-only status, no-backfill language, and fail-closed CLV semantics.

### Disposition
CLOSED FOR SURFACE EXISTENCE / PROSPECTIVE DEMONSTRATION PENDING.
The structural debt (no durable close surface) is corrected. Full LEARNED closure requires a future genuinely pre-kickoff qualified CLOSE observation to be appended and independently read back under normal operation.


## October 4 QA continuation — terminal receipt closure semantics — 2026-10-05

### Correction
Formalized the already-demonstrated two-phase terminal closure pattern in evidence/CFB_TERMINAL_RUN_RECEIPT_CLOSURE_CONTRACT_2026-10-05.md. Historical receipts remain immutable. RUN_PASS now requires applicable surface readback plus independent terminal-receipt-candidate readback before a separate RUN_CLOSURE certification.

### Verification
Contract persisted and direct readback confirmed the two-phase rule, immutable-history rule, and prospective-demonstration requirement.

### Disposition
STRUCTURAL CORRECTION VERIFIED / PROSPECTIVE NATURAL-SCHEDULE DEMONSTRATION PENDING.
The 2026-09-27 13:13 Sunday Market receipt remains historical evidence and is not rewritten; because it declared RUN_PASS while its own closure proof was pending, audit consumers must not use it as sole proof of fully closed completion absent a later conforming closure record.
