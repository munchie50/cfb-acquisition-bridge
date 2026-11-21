# Saturday Nov 21 2026 — conditional run-failure recovery action plan

Status: PREPARED / NOT EXECUTED. Operational playbook only; no change to authority, production tasks, frozen model, cutoffs, or canonical publication gates.

## Triggers and clock (America/Chicago)
- Before 07:00: read latest authoritative accepted state, four task statuses, run receipts, 70-game ledger, Saturday 58-game companion and original deadline records; preserve source SHAs. Do not claim a fresh run.
- 07:00 Market Monitor: capture scheduled_for, started_at, ended_at, automation status and actual worker receipt. A scheduler completed state is not RUN_PASS. Compare exact cutoff timestamps: Nebraska–Ohio State and Maryland–USC both carry 2026-11-21T13:00:00Z (07:00 CT) planning cutoff, authority unverified. Starting at cutoff does not prove pre-cutoff acceptance.
- On any missing/failed engine receipt, stale coverage, unqualified offer, unverified selector or failed write/readback: mark RUN_INCOMPLETE, classify failure boundary (schedule/control plane; source acquisition; normalization; roster/news; market/offer; six-market coverage; selector/decision; write transport; independent readback). Capture exact failing stage, last accepted output, and SHA; recover only missing steps. No historical PASS promotion.
- 07:00–09:00: prioritize 16 early Saturday games, including 11 numeric frozen and 5 original exclusions; preserve 12 total Saturday exclusions. Verify CBS acquisition/normalization only if new evidence shows a regression; previously completed 70-game board normalization is not a reason to rerun. Resolve material QB/news and named-book offer clocks before recommendations.
- 09:00 Weekly QA: inspect existing scheduled task and its receipt separately. QA green does not promote Market Monitor; QA failure does not silently modify champion.
- Before 11:00: either independently verified canonical accepted Hot Sheet, or prominently labeled INCOMPLETE informational sheet with no executable recommendation. Never present historical Nov19 mixed-book displays as current or executable. Preserve any missed reconciliation deadlines and original cutoffs.
- 13:00 Market Monitor: check actual run timing and engine receipt, reconcile later Saturday games (42) and the full 70-game weekly obligation; no backdating or cutoff extensions. After kickoff, no pregame issuance for that game.

## Acceptance evidence and escalation
Require: verified current source acquisition, material roster/news assessment, qualified operator/jurisdiction/timestamp market evidence, six-market full-slate coverage or explicit unresolved counts, frozen champion selector and deadline integrity, accepted canonical write plus independent readback, complete run receipt. No qualified offer => no executable wager/parlay. Separate historical model win probability from spread-cover probability and betting edge. Track due/blocked/verified counts explicitly.

## Parallel independent lanes
1. Scheduler/receipt timing and control-plane evidence (read only).
2. Material QB/roster/news and deadline ledger for 16 early games.
3. Qualified named-book offer evidence and six-market completeness for eligible games.
Reconcile lanes against one authority ledger before any publication; serialize mutations. Do not investigate retired DNS checkout or execute deferred offseason Data Integrity Gate.

## Guardrails and rollback
Exactly four existing production automations, no fifth, no schedule changes. Production v1 remains champion; no threshold or cutoff change. All task prompt backups and rollback map at `evidence/operational/CFB_FOUR_TASK_CHANGE_ROLLBACK_LEDGER_20261120.md`; restore test not performed. Saturday historical companion `evidence/operational/CFB_WEEK12_SATURDAY_FULL_58_GAME_TRIAGE_NONCANONICAL_20261120.md` is NONCANONICAL, 58/58 source reconciled; do not promote it. Do not overwrite accepted canonical evidence with partial results. Preserve failure receipts for later root-cause correction.

## Explicit stop / proceed decision
PROCEED with executable pick only if all applicable accepted governance, cutoff, current market and readback gates pass. Otherwise HOLD/NO BET for affected game, continue independently useful recovery work, report precise missing evidence. Never convert the missed Friday 13:00 CT decision or an expired Saturday cutoff into a new permission window.
