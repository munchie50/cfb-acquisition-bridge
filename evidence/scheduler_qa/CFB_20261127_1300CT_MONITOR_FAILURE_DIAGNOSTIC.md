# Nov. 27 13:00 CT Market Monitor failure diagnosis

## Scheduled worker

Matched task 6ae766e788d881919726d0eeb44450dd and run b07ccc75-4cd0-8322-9a5c-f40f9c7c649b. Nominal 19:00 UTC. Scheduler reports start 18:56:49.346382 UTC and completion 18:57:00.684185 UTC, approximately 11.34 seconds and before the nominal slot. Treat this clock difference as observed metadata. Its cause is unavailable. The matching worker result reports authenticated read of 624592c5df2997ec2b0c749c51fba866ee1c484f and write-capability discovery, then no startup write attempt. Main receipt inventory contains the scoped manual 13:00 CT chain only. There is no native startup, source, publication, candidate or closure for that slot. The scheduler's completion denotes delivery of the result; the result itself is RUN_INCOMPLETE.

Live prompt SHA-256 ecd54c5cae852ed136f3a442b189efb47f94f84b9bf45d611ad3c2c2577ee5e9 exactly matches the Nov. 26 installed repair. Its first step already requires the target check, guarded append and exact readback. Task revision timestamp 18:57:25.942947 UTC is after the recorded run. The invocation prompt snapshot and precise dispatch/termination trace are unavailable. Exposed metadata does not establish whether the worker chose to finalize or was prevented from dispatching. DNS, quota, time limit, 404/409 and write denial are unproved causes for this slot.

Differential evidence: Nov. 24 13 CT same task wrote its startup receipt on main at b12971c8ba921b2174a2bda5d075fe4cfbbb49aa. Nov. 25 07 CT stopped after discovery before authenticated read. Nov. 26 07 CT reported source acquisition after verified startup and stopped ahead of normalization. Nov. 26 13 CT saved startup and stopped before CBS acquisition. Nov. 27 07 CT reported authenticated read and stopped before startup persistence. Nov. 27 13 CT also stopped before startup persistence. The observed boundary moves and elapsed durations differ. Work Mode successfully ran guarded startup/write/readback and the full 69-game CBS archive after this slot. Prior Run Now diagnostics returned inline Work Mode and cannot establish native-worker parity. The independently diagnostic evidence still needed is the task worker's tool-dispatch and termination trace keyed to the run ID and its invocation prompt snapshot. The next native proof is that its own start, capture, output and closure persist and read back. A further prompt wording edit has no demonstrated effect on the observed boundary.

## Manual publication

Reproduced against accepted main ancestry (diagnostic baseline 97d8e3179e9aef827e417c64b4aecc2e6cfaa592), using the morning canonical parents, exact retained afternoon CBS board 1488b8ba8fde3b93e36409cb7ea4b2cb6a7ad61a, and a replay clock of 21:22 UTC, within the collection freshness window. The morning saved-publication audit returned PASS_SAVED_PUBLICATION_INTEGRITY_ONLY. The afternoon market-only compiler built all 69 rows. Decision transition probes returned:

| Probe | Exact response |
| --- | --- |
| Retain previous INCONCLUSIVE states | missing/overdue INCONCLUSIVE reconciliation; prospective decision required |
| Give them a new PASS at the actual post-kickoff clock | postkickoff decision reconstruction |
| Record elapsed rows as HISTORICAL_GAP and resolve the still-pregame rows | historical gap requires qualified recovery profile |

The after-kickoff unresolved rows are 401869930, 401856759 and 401864549. The neutral gate restricts typed historical gaps to Weeks 8 and 10. Week 10 provides precedent for a qualified, append-only admission bound to actual time and elapsed identities, without a retrospective pregame decision or executable record. Its existing declaration is profile-specific. A Week 13 repair needs its own qualified evidence boundary and rejection checks for future identities, backdating, chronology rewriting and execution. Both this publication recovery and native scheduled dispatch require independent proof. This diagnosis changed no production task, publication, scorecard, or historical status.
