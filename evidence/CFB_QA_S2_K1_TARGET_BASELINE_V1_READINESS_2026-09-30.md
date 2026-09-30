# CFB QA — Prospective S2_K1 Target-Baseline Companion v1 Readiness — 2026-09-30

Status: EXECUTABLE CONSTRUCTED / FAIL-CLOSED REST_DAYS BLOCKER / NO BASELINE ARTIFACT ACCEPTED
Scope: S2_K1 substrate only.

The v1 target-baseline companion implements the frozen season-local/cutoff-local pooled primitive baselines for the 16 primitive-backed features using accepted v4 mechanical/derived primitive surfaces and UTC-date-midnight strict-prior semantics.

During executable construction, ancestry recovery exposed that rest_days is different: the frozen historical rule is the season-local mean of valid strictly-prior pregame rest intervals before the cutoff. The accepted v4 package does not persist the historical feature surface required to reconstruct those intervals. The future v1.246 target-side ledger cannot be used as that population pool because those are future target states, not the strictly-prior feature-history population.

Accordingly the executable deliberately exits with:
`TARGET_BASELINE_BLOCKED_REST_DAYS_HISTORY_SURFACE_REQUIRED`

It does not substitute, impute, use future target rows, or generate S2 predictions.

Next readiness dependency: expose/retain a completion-safe strictly-prior rest_days feature-history surface from the same v4 primitive ancestry, or demonstrate an already-accepted equivalent surface. Do not alter the frozen rest_days baseline formula.

A static gate protects the fail-closed behavior. No live execution or scientific evidence was created. Frontier remains CADENCE WAIT.
