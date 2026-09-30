# CFB QA — Scheduled Market Monitor Silent-Completion Incident — 2026-09-30

Status: STRUCTURAL OBSERVABILITY FAILURE IDENTIFIED / SCHEDULER RESTORED / GUARD INSTALLED

## Incident
The scheduled CFB Market Monitor records a 2026-09-30 07:01 CT launch, but repository readback contains no conforming 2026-09-30 Market Monitor terminal receipt, no 2026-09-30 Hot Sheet, and no 2026-09-30 append to the canonical market/decision surfaces attributable to that cycle. Under v1.239/v1.242/v1.245 this is not RUN_PASS. Scheduler launch/completion cannot substitute for engine completion.

The task was subsequently observed disabled. Available task state exposes the current enabled flag and last_run_time but does not expose reliable actor/reason history for the disable transition. Attribution is therefore UNRESOLVED rather than inferred.

## Root-cause classification
1. Authority unavailable: REJECTED. Current recovery index and canonical surfaces were readable.
2. Governed state contamination: NOT OBSERVED. No 2026-09-30 monitor mutation, execution-ledger mutation, scorecard mutation, or Champion mutation was found.
3. Terminal persistence failure: CONFIRMED. Required terminal receipt is absent.
4. Observability design weakness: CONFIRMED. Existing control required a receipt before RUN_PASS but did not require an early durable start marker, so a task that terminated before closure could leave no repository trace.
5. Disable-transition actor/reason: UNRESOLVED with available evidence.

## Corrections installed
- Restored CFB Market Monitor scheduler to enabled without changing its 07:00/13:00 CT cadence.
- Strengthened task execution contract: after authority recovery and before external market research/governed mutation, persist/read back a timestamped RUN_STARTED marker under evidence/run_receipts/.
- RUN_STARTED is explicitly non-terminal and never proves completion.
- A separate terminal receipt remains mandatory and must end RUN_PASS, RUN_INCOMPLETE, or RUN_FAIL.
- RUN_PASS now explicitly requires Hot Sheet persistence/readback plus applicable canonical-surface and terminal-receipt readback.
- Installed independent CFB Monitor Receipt Watch at 07:30 and 13:30 CT daily. It checks the preceding scheduled cycle and alerts only when terminal receipt/Hot Sheet/persistence evidence is missing. It is not allowed to create a competing market baseline or mutate Champion state.

## Historical disposition
The 2026-09-30 07:01 CT cycle remains INCOMPLETE / TERMINAL RECEIPT MISSING. Do not fabricate a retroactive market observation, decision state, Hot Sheet, or RUN_PASS receipt for it. The next valid Market Monitor cycle resumes prospectively from the last durable state.

## Demonstration status
Configuration corrections are installed and task enabled-state readback succeeded. End-to-end RUN_STARTED + terminal-receipt + watchdog behavior requires the next actual scheduled Market Monitor cycle; do not claim DEMONSTRATED before that evidence exists.

Scientific effect: none. Champion and frozen prediction lineage unchanged.
