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
