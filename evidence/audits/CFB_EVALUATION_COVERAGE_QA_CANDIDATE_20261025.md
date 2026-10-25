# QA candidate — evaluation coverage and learning follow-through

Observed recording clock: 2026-10-25T03:48:11Z.
Existing actions: CFB_QA_LEARNING_FOLLOW_THROUGH_20261023 and CFB_QA_QUALIFICATION_LIMITS_REVIEW_20261023.
User direction: expedite learning and fixes for recurring evaluation gaps.
Status: IMPLEMENTED AND TARGETED-TESTED ON QA BRANCH; NOT PRODUCTION OR NATURAL ADOPTION.

## Demonstrated seam and bounded remedy

The current readiness audit retains PASS for reconsideration, but its PASS rows carry empty recommendation_blockers. That is preservation of the decision, not proof of completed football research. A full-row count or absence of blockers can therefore be mistaken for analytical coverage unless the audit makes evidence completeness explicit.

The existing read-only readiness producer now adds a mutually exclusive full-census evaluation accounting and a deadline-ordered uncertified review work list. It preserves original exclusions, permanent gaps, conditional review references and unknown analytical completion separately. Saved reasons are copied verbatim for follow-through. No reason-text heuristic turns a PASS into a researched no-value finding. NOT_CERTIFIED means the summary packet does not prove completion; separate retained research may exist and must be reconciled before declaring a game missed. Conditional reference presence does not certify all markets, fresh research or source truth.

Unknown timing remains visible work debt with QUALIFY_TIMING_BEFORE_REVIEW, not an executable opportunity. Known clocks sort by actual timestamp, including offsets. Elapsed windows stay closed under the existing review_window logic; this accounting does not change it or authorize historical reopening. No betting decision, threshold, cutoff, venue prerequisite or original source state changes.

The existing PR CI path filters now include the readiness producer and tests, so this candidate cannot silently miss that existing workflow solely because no contract file changed. This is a CI trigger repair, not a recurring-task or schedule change.

## Retained actual-source diagnostic

Pinned source commit: c3eca98aa43f72b4da1f5d7906fa72a10aa30379. Each complete source was independently fetched at that immutable commit and compared with the input used:
- evidence/operational/CFB_MARKET_MONITOR_STATE.md
- evidence/operational/CFB_DECISION_WAIT_LEDGER.md
- evidence/scheduler_qa/CFB_WEEK8_ORIGINAL_ANCESTRY_RECOVERY_20261020.json

The last paired Week8 typed packets have source boundary 2026-10-24T18:10:00Z. Their exact 56-ID union was checked against the original lineage before diagnostic replay. Results:
- 7 ORIGINAL_EXCLUSION
- 4 HISTORICAL_GAP
- 5 CONDITIONAL_REVIEW_REFERENCE
- 40 NOT_CERTIFIED

These groups account for all 56 identities. This does NOT assert 40 missed reviews or 40 current bettable games. An original exclusion takes precedence in this mutually exclusive partition; the unchanged existing historical_gaps counter continues to count canonical history state independently. Any open-work entry with uncertain kickoff/cutoff requires timing qualification, and source freshness is not established by this historical replay.

Replay used extraction of the final paired canonical packets, the retained original lineage and evaluation_coverage/review_window directly. The complete publication validation and independent source-truth qualification were NOT rerun locally. No outcomes were joined, no new source credits spent and no hypothetical profits created.

## Verification and limits

21 targeted tests passed: 6 new coverage regressions plus 15 existing recommendation/venue separation and review-window cases. They cover identity omission/duplication, missing decisions, original exclusions, non-certifying PASS, reference-only labels, immutable decisions/reasons, unknown timing, closed windows and offset-aware deadline ordering. A diagnostic replay of the retained 56-game snapshot passed full identity/count accounting.

The two existing Git-history-dependent authentic readiness audit tests were not executed in the partial local checkout. The full existing repository workflow remains required on the PR; targeted tests are not its substitute. Remote candidate source/test/workflow files were independently read back in full after SHA-guarded writes.

## Next work and acceptance

Prioritize the existing Monitor's current/future-game research over historical backfill. Reconcile NOT_CERTIFIED rows against already retained pre-event research before spending acquisition budget. Where the evidence shows unfinished work and a valid future window, the existing Monitor should complete research in practical-deadline order under the current source and credit controls. A specific failed preview is not proof every permitted source failed; absent attempt traces stay UNKNOWN. Do not repeatedly search expired games to manufacture old recommendations.

At existing Weekly QA, grade recoverable original predictions and authentic pregame signals across the complete eligible population, with actual tickets separate. Preserve missing historical decisions. Carry this change within the two existing actions rather than another tracker.

Acceptance is pending full CI, review of this bounded diagnostic change, and actual use in existing producer/weekly work. Benefit so far is honest coverage accounting and an inspectable work list. Timely completed evaluations, fewer missed windows, reduced manual intervention and predictive/financial benefit remain UNPROVED. No new task, schedule, model, production betting rule or money movement.
