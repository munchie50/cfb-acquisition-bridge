# CFB QA — S2_K1 Rest-Days Executable Ancestry Recovery — 2026-09-30

Status: ANCESTRY RECOVERED / TARGET-BASELINE EXECUTABLE UNBLOCKED STRUCTURALLY / LIVE ACCEPTANCE PENDING

Routine ancestry recovery found authoritative rest_days semantics in the accepted v1.172 producer and the independent 2026-09-27 rest-days reconciliation.

Frozen rule recovered:
- v1.172 computes each pregame rest_days value as the elapsed days between consecutive same-team, same-season schedule kickoffs;
- same-team equal-kickoff ambiguity is forbidden;
- the population baseline is the season-local mean of valid rest_days observations whose pregame kickoff is strictly before the UTC-calendar-day-normalized target/source cutoff;
- no cross-season carryover, same-date state, imputation, target outcome, market or protected 2025 data.

The target-baseline companion now reconstructs that feature-history surface from the accepted 2026 mechanical primitive schedule identities already required by the companion. It does not use future v1.246 target rows.

The prior temporary fail-closed blocker `TARGET_BASELINE_BLOCKED_REST_DAYS_HISTORY_SURFACE_REQUIRED` is therefore superseded by recovered executable ancestry. The companion retains a general fail-closed `TARGET_BASELINE_UNAVAILABLE:<features>` state if any frozen baseline cannot be reproduced at an actual cutoff.

This is implementation ancestry recovery, not a formula change. No live target-baseline artifact has been executed or accepted yet; that still requires the next same-cutoff weekly package and independent reconciliation. No S2 prediction or outcome scoring occurred. Frontier remains CADENCE WAIT.
