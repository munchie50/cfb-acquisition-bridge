# CFB QA Sandbox — Execution Attempt Ledger — 2026-09-28

Status: APPEND-ONLY QA EXECUTION HISTORY
Scope: isolated QA Sandbox candidate-freeze workflow.
Rule: GitHub Actions UI conclusion is not by itself the scientific classification. Purpose, expected stop behavior, logs, and downstream reconciliation control classification.

| Run | Run ID | Head | Purpose | GitHub conclusion | QA classification | Root cause / evidence | Resulting action |
|---|---:|---|---|---|---|---|---|
| #6 | 36360100360 | c11ae945... | Resume reconciled candidate freeze | cancelled | INFRASTRUCTURE TIMEOUT | generation still active at ~30-minute job ceiling | Increased isolated workflow timeout to 90 minutes; no scientific acceptance |
| #7 | 36362050431 | 6d50ba1... | Freeze with extended timeout | failure | SCIENTIFIC/PREEXEC COVERAGE DEFECT EXPOSED | rest_days frozen population baseline unavailable for real accepted target cases | Reconciled feature-specific rest_days coverage; corrected omission identities/cardinality |
| #8 | 36366403150 | ba722ad3... | Observe corrected generator SHA before execution | failure | EXPECTED CONTROLLED STOP / PASS FOR PURPOSE | identity printed, compile passed, intentional exit 86 before generation | Pin observed generator identity and restore execution |
| #9 | 36366519864 | 4efdccf8... | Authoritative freeze after corrections | cancelled | INFRASTRUCTURE/PERFORMANCE TIMEOUT | generation remained active through ~90-minute ceiling | Triggered structural performance audit instead of another timeout increase |
| #10 | 36413444864 | e2b0846a... | Observe optimized generator identity | failure | EXPECTED CONTROLLED STOP / PASS FOR PURPOSE | seven frozen input hashes passed; optimized generator SHA ad2609f14bc4b30d61d19ffb90083a9dc7a5b171dc9e60f513dec5d0a4145641 printed; compile passed; intentional exit 86 | Pin exact optimized identity and resume execution |
| #11 | 36413551460 | 496d5b0b... | Optimized outcome-blind candidate freeze | IN PROGRESS at checkpoint creation | ACTIVE — NOT YET CLASSIFIED | Do not infer result before completion | On completion, inspect logs/artifact and independently accept or classify failure |

## Interpretation rules
- EXPECTED CONTROLLED STOP is not a scientific failure even if GitHub renders a red failure icon.
- TIMEOUT is not evidence that candidate science failed.
- Workflow success is not candidate acceptance; artifact/readback gates remain mandatory.
- A failure that exposes a real contract/data-coverage issue must be reconciled scientifically before rerun.
- Never overwrite this history to make a prior run look successful. Append later attempts/results.

## Efficiency lesson
Run #9 established repeated-friction evidence: extending Run #6's 30-minute ceiling to 90 minutes did not resolve execution. Static hot-loop audit then identified repeated identical dataframe filtering/index construction. The bounded repair memoized/reused those computations without intentionally changing the frozen scientific contract.

Future rule: after repeated expensive execution failure, perform structural/performance inspection before increasing runtime/resources again.


## 2026-09-28 reconciliation — Runs #1–#12
This section appends the previously missing early attempts and terminal evidence discovered after the original ledger was created. Earlier rows are preserved as historical-at-the-time statements; this section supersedes their status where noted.

| Run | Run ID | Head | Terminal evidence / QA classification |
|---|---:|---|---|
| #1 | 36358628895 | 092fc052... | FAILURE — real implementation/construction defect: `invalid S1 qualified-prior count`. Frozen inputs and then-current generator identity verified before generation. |
| #2 | 36358999979 | 1687b7f... | EXPECTED CONTROLLED STOP / PASS FOR PURPOSE — corrected generator identity observed/compiled; intentional exit 86 before generation. |
| #3 | 36359139294 | ebeef8a... | FAILURE — real S2 construction defect: `non-finite S1 input`; led to deeper completion-safe S2-context reconciliation including California–San Diego State. |
| #4 | 36359963199 | 09ed85e... | IDENTITY-CONTROL FAILURE / PREEXEC STOP — workflow expected prior generator SHA; persisted generator differed; generation did not run. |
| #5 | 36360042694 | d77929a... | EXPECTED CONTROLLED STOP / PASS FOR PURPOSE — generator identity observed/compiled; intentional exit 86. |
| #6 | 36360100360 | c11ae945... | CANCELLED — ~30-minute infrastructure timeout during generation. |
| #7 | 36362050431 | 6d50ba1... | FAILURE — rest_days feature-specific baseline coverage defect exposed and reconciled. |
| #8 | 36366403150 | ba722ad3... | EXPECTED CONTROLLED STOP / PASS FOR PURPOSE — corrected identity observation. |
| #9 | 36366519864 | 4efdccf8... | CANCELLED — >90-minute performance timeout; triggered structural optimization. |
| #10 | 36413444864 | e2b0846a... | EXPECTED CONTROLLED STOP / PASS FOR PURPOSE — optimized identity observation; generator SHA-256 `ad2609f14bc4b30d61d19ffb90083a9dc7a5b171dc9e60f513dec5d0a4145641`. |
| #11 | 36413551460 | 496d5b0b... | FAILURE — optimized generation reached cardinality gate in ~19 minutes; `candidate row count mismatch`; no artifact uploaded and independent acceptance gate did not run. |
| #12 staging | 36417744069 | ebe9481c... | PREEXEC/STAGING FAILURE — diagnostic workflow still contained placeholder generator identity; no scientific evidence. |
| #12 diagnostic | 36417777142 | efef5c23... | DIAGNOSTIC FAILURE / PASS FOR PURPOSE — exact frozen inputs and diagnostic identity passed; generator emitted actual cardinalities before preserved fail-closed assertion. S0=6,246; each S1=6,204; each S2=5,731; total=53,986; S1 omissions exactly 42; S2 omissions 515. |

### Run #12 causal reconciliation
The 1,848-row shortfall from the frozen 55,834 expectation is entirely S2: 462 excess omitted games × four k values. S1 exactly reproduces its frozen 42-game omission set, so the general target baseline/rest_days path is not the source.

Comparison of the optimized and pre-optimization S2 implementations shows the optimization preserved the relevant S2 logic; the performance optimization did not create the semantic defect.

Root cause: the inner S2 source-opponent baseline handler retained legacy exception strings while current `baseline()` emits `unavailable frozen population baseline`. The current error escaped the source-residual handler to the outer candidate-level handler, causing the whole S2 candidate to be omitted instead of skipping only that unavailable historical residual and retaining other valid residuals. This contradicts the already-frozen completion-safe S2 rule; it does not justify redefining the frozen expectation to 515 omissions.

Bounded implementation correction persisted on main:
- commit `2f8aad0963d6a09ae9b8eb749163f3ff65d3566a`
- generator Git blob `40447984a58dbc530cbe942bc1176f0c5bcbe9b2`
- correction: inner S2 source-baseline handler now recognizes `unavailable frozen population baseline` while retaining legacy recognized strings.
- no S1/S2 formula, k-grid, chronology, mapping, coefficient/scaling, expected omission set, Champion, outcome boundary, or 2025 TEST boundary changed.

### Current next gate
Observe and pin the corrected generator identity under controlled pre-execution conditions, then execute a fresh outcome-blind candidate freeze. The frozen acceptance expectation remains 55,834 rows with 42 S1 omitted games and 53 S2 omitted games unless new pre-outcome evidence proves otherwise.


## Run #13 — accepted freeze
| Run | Run ID | Head | Terminal evidence / QA classification |
|---|---:|---|---|
| #13 | 36421939025 | a3318105... | SUCCESS + INDEPENDENT ACCEPTANCE — exact frozen inputs and corrected generator identity passed; generation produced 55,834 rows; independent runner gate passed; artifact 10970862853 uploaded; independent post-run download reproduced ZIP/CSV/manifest hashes, exact family counts, exact 42 S1 and 53 S2 omission sets, no 2025, no forbidden outcome/market/wager/closing columns, and outcomes_joined=false. Candidate freeze accepted in `evidence/CFB_QA_SANDBOX_CANDIDATE_FREEZE_ACCEPTANCE_2026-09-28.md`. |

Construction/freeze phase is CLOSED. Outcome scoring remains a separate authorization boundary and was not performed by Run #13.


## 2026-09-29 source-context/real-substrate terminal reconciliation
Earlier historical ledger rows remain unchanged.

| Run | Job | Result / classification |
|---|---:|---|
| 36636336698 | 109637770259 | SUCCESS; retained real v1.246 target-side substrate independently accepted in CFB_QA_V1_246_REAL_TARGET_SIDE_ACCEPTANCE_2026-09-29.md. No operational prospective prediction snapshot acceptance implied. |
| 36636555611 | 109638500020 | v2 real FAILURE: AttributeError, DataFrame has no start_date. Accepted target-side field is target_kickoff. No artifact acceptance. |
| 36637160447 | 109640501749 | v3 real FAILURE: target/source history count mismatch. v4 restores the exact accepted v1.246 population filter rather than relaxing the invariant. |
| 36637495501 | 109641596028 | First v4 static FAILURE: AssertionError in gate. Preserved; superseded by corrected static gate, not accepted. |
| 36637684023 | 109642221487 | Corrected v4 static SUCCESS; marker and exact SHA verified. |
| 36637810698 | 109642643453 | v4 real SUCCESS + independent semantic/output ACCEPTANCE as QA substrate only; artifact 11065575217, ZIP f1104a7fc509f2ef9ee1825698e0210bfd232c9acfafb34635bbd75f93567c8f. |

v0 quarantine and v1 unaccepted source remain preserved; no earlier version is silently promoted. Local audit SHA stop caused by added trailing newline in staging was corrected by restoring exact connector bytes and verifying Git blobs; no producer mutation. Initial sandbox data-reader install failed; approved install succeeded. No invariant was relaxed.
Source-context acceptance details: CFB_QA_S2_K1_SOURCE_CONTEXT_V4_ACCEPTANCE_2026-09-29.md. Immutable original manifests remain EXECUTED_NOT_ACCEPTED; post-run acceptance is separate.
Global dependency reconsideration: infrastructure closed; current frontier is weekly cadence/preflight before any S2 prediction freeze. No prospective S2 predictions, outcomes, refit, TEST access or production changes.
