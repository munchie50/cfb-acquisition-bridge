# Exact saved CFB Engine Health Rebuilt instructions before controlled compaction

Task ID: 6ae76df2ece4819197f91fb10076dea7
Schedule:
```
BEGIN:VEVENT
DTSTART;TZID=America/Chicago:20260927T163000
RRULE:FREQ=DAILY;BYHOUR=16;BYMINUTE=30;BYSECOND=0
END:VEVENT
```

---

## NOV21 ACTUAL RUN-TIMING DRIFT CHECK — DO NOT CONFLATE SCHEDULE WITH WORK COMPLETION
The Friday 13:00 CT Market Monitor recorded scheduled_for 2026-11-20T19:00:00Z, started_at 2026-11-20T18:58:33.477254Z (86.5 seconds early), completed_at 2026-11-20T18:59:17.059530Z (~43.6 seconds). Scheduler recorded completed but engine RUN_INCOMPLETE; full Saturday market review and canonical Hot Sheet were not verified. At next Health run compare scheduled_for, actual start, actual finish, first successful startup readback, real workload row/market counts, original cutoff timestamps and final canonical readback. Treat early start as observed scheduler timing variance, NOT proof of engine defect or timely cutoff issuance; do not demand a minimum duration as proxy for work. If incomplete, identify exact missing game-level work and owning existing task. No new scheduler or DNS investigation.

## NOV21 TWO-COLLISION CROSS-TASK AUDIT — HEALTH
At next existing run, audit the Market Monitor's ACTUAL Saturday 07:00 CT start, current Hot Sheet, and exact predecessor handoff. Two accepted Nov19 historical rows share 2026-11-21T13:00:00Z planning cutoff: Ohio State @ Nebraska and Maryland @ USC. Both cutoff authorities are UNVERIFIED; later Maryland 17:15 CT kickoff does not extend its original cutoff. Verify both game IDs were acknowledged, actual decision timestamps were not backdated, no expired historical condition was renewed, and Friday's missed deadline was not reclassified PASS. Inspect the corrected persisted handoff evidence/run_receipts/CFB_EVENING_AVAILABILITY_20261121T013041433Z_EVENING_DOWNSTREAM_HANDOFF.md; do not claim four games were researched when only three were. Distinguish 66 unavailable historical cutoff fields from accepted live deadlines; no invented cutoff. Report exact owner and receipt for any failure, without changing producer's sole Hot Sheet ownership, model, schedules or offseason hold.

## NOV21 OPERATIONAL DEFECT CORRECTIONS — USER-APPROVED TASK INTEGRATION; HIGHEST PRIORITY AFTER STARTUP RECEIPT
HEALTH: Inspect actual latest Market Monitor and Evening receipts and current recovery index, compare due-vs-verified work and identify first unresolved execution boundary. Do not count scheduler completed as engine PASS. Detect stale current Hot Sheet, unacknowledged handoffs, missing original cutoff authority, unavailable qualified quotes, incomplete full-slate coverage, and publication selector/readback defects. Correct only within accepted operational scope and own health remit; route producer work to existing Market Monitor. Do not retry abandoned DNS/checkout or Actions investigations. Preserve original deadlines, Champion, four tasks and offseason integrity hold.

## NOV21 USER-DIRECTED STOP-RETRYING ABANDONED CHECKOUT PATH — HIGHEST PRIORITY
Do not run, test, diagnose, or spend task time on Git HTTPS DNS resolution, git ls-remote, DNS checkout probes, or GitHub Actions scheduling. Those paths are retired; any contrary historical instructions below are superseded. Preserve an exact historical failure classification without rerunning it. Start with RUN_STARTED receipt/readback, use the connected GitHub API to recover pinned authority and immutable evidence, then immediately do the maximum independently authorized CBS/current-market, decision, compiler, Hot Sheet, QA or handoff work owned by THIS task. If exact original Python/runtime execution is unavailable, classify that stage BLOCKED, continue independent useful work, and terminate RUN_INCOMPLETE with stage-specific evidence; never infer RUN_PASS or publish a provisional candidate as canonical. Preserve existing four schedules, model/ledger authority and all acceptance gates.

## NOV20 STARTUP ORDER DISAMBIGUATION — first mandatory action (supersedes conflicting "before substantive work" wording only)
FIRST capture observed invocation UTC, scheduled_for, task/trigger/correlation identifiers and attempt append-only RUN_STARTED persistence with independent readback. If persistence is unavailable, retain exact attempted operation and first error in the terminal report; do not falsely assert durable startup. SECOND fresh-read governing authority/current recovery index and predecessor receipt, bounded by actual available connector operations. THIRD perform task-owned work, even when checkout is blocked, while preserving original acceptance gates. FOUR independently verify task-specific closure, next-slot handoff and user delivery status. A requirement to read the defect matrix or authority "before substantive work" means AFTER startup tracing, not before it. Do not spend the whole invocation debugging startup; report blocked receipt as a mandatory gate and continue independent permitted work. Never call RUN_PASS without all required evidence.

## NOV20 CROSS-TASK DEFECT MATRIX — scope-specific enforcement (supersedes conflicting diagnostic priorities, not governance)
Before substantive work, read evidence/scheduler_qa/CFB_RUNTIME_DIFFERENTIAL_20261120_WORKER_CAPABILITY_AND_FAILURE_BOUNDARIES.md and current single active resume frontier at fresh authenticated main. Classify observed boundaries separately: scheduler dispatch/startup; connector-to-execution runtime; SOURCE_CAPTURE/FORMAT (do not repeat already fixed Nov18 lxml th|td parsing); OFFER_QUALIFICATION (HTTP 200 with "Site Unavailable" content is NOT an offer, retrieval time is NOT sportsbook update time); CANONICAL_WRITE_TRANSPORT (3.15MB partial success versus 4.19MB failure does not prove full canonical ledger write); CURRENT_DECISION_SELECTOR_BINDING (one supported CURRENT_HOT_SHEET path, exact canonical decision pointer and byte identity, independent readback); and closure/delivery. These are historical known failure classes, NOT proof of this run's failure. No synthetic selector QA, historical 70/70 replay or known-failing DNS retry as substitute for current assigned work. Do not retry the retired Git HTTPS checkout/DNS path. Use authenticated GitHub connector reads and available original execution paths; if exact runtime execution is unavailable, classify that stage BLOCKED and continue independent obligations. Never relax original publication/acceptance gates. Record each applicable class as OBSERVED_PASS, OBSERVED_FAIL, BLOCKED, NOT_DUE or NOT_TESTED with evidence. Carry unresolved cases to correct existing owner, with game IDs and deadline. Never infer current offers or publish bets from historical provisional Week12 data.
HEALTH INSPECTOR ONLY: Inspect each existing task's latest run-specific receipt, natural scheduled_for, predecessor acknowledgment, due-now denominator, handoff/closure/readback, canonical freshness and missing downstream delivery. Report cross-task defect matrix by owner and first failing stage. Flag a scheduler 'completed' that lacks engine RUN_PASS evidence. Detect stale Nov19 recovery pointer versus Nov20 provisional preview, and oversized-write/selector blockers, without editing Monitor canonical pointers or competing in market collection. Independently close Health's own inspection and carry escalations.

## SUCCESSOR HANDOFF ACKNOWLEDGMENT — Nov20 (supplements run-specific completion; no new framework)
At startup, locate the latest applicable predecessor slot's verified receipt/handoff, using exact task ID, scheduled_for, artifact SHA and game/obligation IDs. Explicitly ACKNOWLEDGE each carry-in as ACCEPTED_FOR_THIS_SLOT, NOT_DUE_WITH_OWNER_AND_DEADLINE, ALREADY_VERIFIED_WITH_EVIDENCE, or BLOCKED_WITH_FIRST_CAUSE. Do not silently discard an unacknowledged predecessor obligation; flag missing predecessor receipt as UNKNOWN_PREDECESSOR_EVIDENCE, not proof it never ran. At closure, include successor task ID, scheduled slot, exact carried-forward IDs, reason, deadline, receipt path/SHA and independent readback. Mark THIS slot RUN_INCOMPLETE if a mandatory carry-in due now remains unresolved or a required handoff could not be persisted; do not retroactively change predecessor's status. Cross-task handoffs must preserve Monitor's sole Hot Sheet ownership and each task's own scope. Do not require unrelated future work to pass today's slot. If no predecessor carry-in exists, explicitly record NONE_VERIFIED and its checked source.

## RUN-SPECIFIC COMPLETION CONTRACT — 2026-11-20 (priority over vague weekly/partial summaries; preserves existing acceptance gates)
At START, identify actual scheduled local slot, scheduled_for, observed start UTC, task ID, trigger, current football week, prior accepted run receipt and carry-in obligations. Build an explicit due-at-this-slot checklist from this task's original governing contract and current accepted state; distinguish MANDATORY_NOW, DEPENDENCY_BLOCKED, NOT_DUE, and PREVIOUSLY_VERIFIED (with exact evidence). Task-specific obligations: 16:30 CT daily: own integrity checks, canonical pointer/receipt freshness, gap and missed-handoff audit, stage-specific evidence, alert/escalation of missed current-run obligations, verified Health closure and next-owner handoff. Do not require other tasks' unrelated unfinished weekly work to call Health complete; do not hide failed checks.
At END, for EVERY MANDATORY_NOW item record game/cohort ID when relevant, action performed, evidence path/immutable SHA and readback, completion status, first blocker and owner. Include current-slot coverage denominator, outstanding items with deadlines and named successor task/slot, and whether handoff was actually persisted/read back. RUN_PASS only when ALL mandatory work assigned to THIS slot and its required publication/handoff/readback is verified; RUN_INCOMPLETE if any mandatory due item is blocked, deferred, merely provisional or lacks verification; RUN_FAIL on failed mandatory controls as specified by existing authority. A scheduler status of "completed", an overall weekly progress summary, prior run PASS or a future run promise NEVER substitutes for this slot's closure. A future slot may accept explicitly handed-off NOT_DUE work, but cannot erase overdue work or retroactively upgrade a prior incomplete slot. Final user-facing message MUST lead with "TASK — scheduled_for America/Chicago — RUN_PASS/RUN_INCOMPLETE/RUN_FAIL", then "Due this run: N; verified N; blocked N", concise specific completed deliverables, remaining game IDs/gates, exact next run owner and durable receipt path. If no genuine slot invocation evidence, do not invent a scheduled run. Keep established four-task topology, current schedules, Champion and canonical gates. This is run-specific messaging and enforcement, not permission to relax scope or mark provisional work accepted.

ACTIVE TRANSPORT ORDER OVERRIDE — 2026-11-20: This supersedes ONLY the older DNS-first git ls-remote diagnosis below. For any repository-code checkout requirement, first attempt an actually exposed API/connector-backed commit-pinned repository ZIP or verified offline Git bundle in a Python-capable execution runtime. Authenticate commit pin and archive SHA256, safely extract, verify required exact Git blobs and original scripts, then continue the task's own work in this SAME RUN; do not stop after a transport success. The Firecrawl-hosted ZIP path was proven only in a separate manual environment; never assume it is exposed to this worker. ZIP alone is not full ancestry or production acceptance; where required, obtain verified Git bundle/ancestry or fail closed. If alternate runtime unavailable, record tool availability and exact blocked stage; do NOT repeatedly spend the run on known-failing Git DNS. Preserve original ownership, receipt/readback, four-task topology, frozen Champion and all acceptance gates. 

SUPERSEDED Nov19 DNS-first diagnosis removed. Nov20 connector/API-first override controls transport. Preserve same-run continuation and fail-closed evidence.

FIRST ACTION — STARTUP TRACE AND RECOVERY (NOV1 VERIFIED): Before expensive GitHub authority reads or source research, record observed UTC, trigger type, invocation ID when available and correlation ID; persist permitted append-only RUN_STARTED under evidence/run_receipts/ and independently read back. Absence of a marker is ambiguous, not proof of scheduler dispatch failure. Discover canonical latest accepted files from fresh main tree with exact nonzero size and blob SHA. If fetch_file returns empty for a nonempty file, use GitHub fetch_blob by exact SHA and independently cross-check API git/blobs/<sha>; verify complete beginning/end and identity. Never downgrade to older index, truncate authority or invent data. Log stage boundaries and exact first error; distinguish scheduler no_update/null chat_ref, retrieval failure and downstream workflow incompleteness. Preserve own task's original scope and ownership; Health is integrity-only, Evening is downstream and not competing Hot Sheet producer. Compiler historical replay is not current authored six-market decision evidence. Respect existing permissions, persistence contracts, Champion protection, four-enabled-task topology and fail-closed closure.

HEALTH EXECUTION ORDER — First complete connector-supported integrity checks and evidence readbacks in this invocation. A local checkout is required only for a specific required check that actually executes repository code. Record that check by name, use an actually available verified non-Git-HTTPS code execution path when needed, and if it fails record the unverified check and continue all independent audits and closure. A monitored task's failure is separate from Health's own inspection status.

VERIFIED PYTHON CHECKOUT — PRODUCTION EXACT-BYTE DIRECT SHELL (2026-11-19). This is the runtime routing used by the production CFB Market Monitor. Apply after verified RUN_STARTED and fresh authority recovery. Keep the existing Health execution order. Complete connector-supported integrity and receipt checks first. Call this checkout only for a named required check that executes repository code.

Check actual availability of a direct terminal tool and of exec_command inside the connector orchestration cell independently. When direct shell exists, invoke it directly once with printf '%s\n' CFB_DIRECT_SHELL_STARTED, then record Python and Git versions, tool identifier and exit. A tool being named in the prompt is not execution evidence. If combined connector execution is callable, use the verified combined checkout cell below and poll any returned shell session to completion. If the combined route is unavailable before the helper starts and direct shell passed, use the exact-byte direct fallback below.

For the direct fallback, authenticate fresh main and the helper's exact blob and positive byte count through the connected GitHub repository at that exact commit. When the authenticated metadata matches the embedded helper (3,780 bytes; Git blob b13930cb714eb87c8dce6136ffab6fbceeb44898), submit the entire shell command below as one direct terminal action, replacing only REPLACE_WITH_FRESH_AUTHENTICATED_MAIN_SHA with the fresh 40-hex SHA. The command decodes the embedded bytes and checks length and Git hash before it starts the unchanged helper. Do not re-download the helper from the shell, retype its source, or use a stale pin. If the authenticated helper changes, obtain exact base64 from the connector and verify its size and Git hash in direct shell before execution, or record HELPER_TRANSFER as blocked. If authority points to a different helper, follow that accepted authority. Poll any launched shell session. Use adequate output or retained result readback to recover the complete result.

Record direct-shell probe, combined-shell availability, byte verification, helper execution, and Git checkout independently. DIRECT_HELPER_BYTES_VERIFIED proves transfer only. Require SUPPORTED_GIT_RUNTIME_VERIFIED, exact HEAD, full ancestry, required current-task scripts and retained-review validation before using the resulting worktree. Checkout still requires Git HTTPS connectivity. On failure record the actual stage and exact sanitized error, preserve the runtime handoff and continue connector-supported independent work and normal closure. Run a verified checkout only once per invocation. Preserve default proxy and Git settings, task ownership, source gates and canonical write rules.

```sh
expected_size=3780
expected_blob=b13930cb714eb87c8dce6136ffab6fbceeb44898
set -eu
pinned_head='REPLACE_WITH_FRESH_AUTHENTICATED_MAIN_SHA'
case "$pinned_head" in ''|*[!0-9a-f]*) exit 2;; esac
test "${#pinned_head}" -eq 40
if command -v python3 >/dev/null 2>&1; then
  checkout_python=python3
else
  checkout_python=python
fi
"$checkout_python" --version
git --version
printf '%s\n' SHELL_PROBE_PASS
umask 077
scratch=$(mktemp -d)
base64 -d > "$scratch/cfb_runtime_checkout.py" <<'CFB_EXACT_HELPER_B64'
IiIiUHJlcGFyZSBhIHJlYWwsIHBpbm5lZCBDRkIgR2l0IHdvcmt0cmVlIGJlZm9yZSByZXNlYXJj
aDsgbmV2ZXIgcHVibGlzaCBvciB3cml0ZSBiYWNrLiIiIgppbXBvcnQgYXJncGFyc2UKaW1wb3J0
IGpzb24KaW1wb3J0IG9zCmltcG9ydCByZQppbXBvcnQgc3VicHJvY2VzcwppbXBvcnQgc3lzCmZy
b20gcGF0aGxpYiBpbXBvcnQgUGF0aAoKUkVQT1NJVE9SWSA9ICdodHRwczovL2dpdGh1Yi5jb20v
bXVuY2hpZTUwL2NmYi1hY3F1aXNpdGlvbi1icmlkZ2UuZ2l0JwpSRVFVSVJFRCA9ICgnY2ZiX3dl
ZWs5X3B1YmxpY2F0aW9uLnB5JywgJ2NmYl9ob3Rfc2hlZXRfcmVhZGluZXNzLnB5JywKICAgICAg
ICAgICAgJ2NmYl9uZXV0cmFsX3B1YmxpY2F0aW9uX2dhdGUucHknLCAnY2ZiX3JlY292ZXJ5X2Nv
bnN1bWVyX3ByZWZsaWdodC5weScpCgoKZGVmIHByZXBhcmUoZGVzdGluYXRpb24sIGV4cGVjdGVk
X2hlYWQpOgogICAgaWYgbm90IHJlLmZ1bGxtYXRjaChyJ1swLTlhLWZdezQwfScsIGV4cGVjdGVk
X2hlYWQpOgogICAgICAgIHJhaXNlIFZhbHVlRXJyb3IoJ2V4YWN0IGNvbm5lY3Rvci1vYnNlcnZl
ZCBtYWluIGNvbW1pdCByZXF1aXJlZCcpCiAgICBkZXN0aW5hdGlvbiA9IFBhdGgoZGVzdGluYXRp
b24pLnJlc29sdmUoKQogICAgaWYgZGVzdGluYXRpb24uZXhpc3RzKCk6CiAgICAgICAgcmFpc2Ug
VmFsdWVFcnJvcignZGVzdGluYXRpb24gbXVzdCBiZSBuZXc7IG5ldmVyIHJlc2V0IGFuIGV4aXN0
aW5nIHdvcmt0cmVlJykKICAgIGVudiA9IGRpY3Qob3MuZW52aXJvbiwgR0lUX1RFUk1JTkFMX1BS
T01QVD0nMCcsIEdDTV9JTlRFUkFDVElWRT0nbmV2ZXInKQogICAgZGVmIGdpdCgqYXJncyk6CiAg
ICAgICAgcmV0dXJuIHN1YnByb2Nlc3MuY2hlY2tfb3V0cHV0KFsnZ2l0JywgKmFyZ3NdLCBlbnY9
ZW52LCBzdGRlcnI9c3VicHJvY2Vzcy5QSVBFLAogICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICB0aW1lb3V0PTE4MCkuZGVjb2RlKCd1dGYtOCcpLnN0cmlwKCkKICAgICMgQSBu
b3JtYWwgZnVsbCBjbG9uZSBwcmVzZXJ2ZXMgZ2VudWluZSBjb21taXQvdHJlZS9ibG9iIGFuY2Vz
dHJ5LiBObyBncmFmdCwKICAgICMgcmVwbGFjZW1lbnQgb2JqZWN0LCBmb3JnZWQgY29tbWl0LCBz
eW50aGV0aWMgcmVmIG9yIHZhbGlkYXRvciBwYXRjaCBpcyB1c2VkLgogICAgZ2l0KCdjbG9uZScs
ICctLW5vLWNoZWNrb3V0JywgUkVQT1NJVE9SWSwgc3RyKGRlc3RpbmF0aW9uKSkKICAgIGdpdCgn
LUMnLCBzdHIoZGVzdGluYXRpb24pLCAnY2F0LWZpbGUnLCAnLWUnLCBleHBlY3RlZF9oZWFkICsg
J157Y29tbWl0fScpCiAgICBnaXQoJy1DJywgc3RyKGRlc3RpbmF0aW9uKSwgJ21lcmdlLWJhc2Un
LCAnLS1pcy1hbmNlc3RvcicsIGV4cGVjdGVkX2hlYWQsICdvcmlnaW4vbWFpbicpCiAgICBnaXQo
Jy1DJywgc3RyKGRlc3RpbmF0aW9uKSwgJ2NoZWNrb3V0JywgJy0tZGV0YWNoJywgZXhwZWN0ZWRf
aGVhZCkKICAgIGlmIGdpdCgnLUMnLCBzdHIoZGVzdGluYXRpb24pLCAncmV2LXBhcnNlJywgJ0hF
QUQnKSAhPSBleHBlY3RlZF9oZWFkOgogICAgICAgIHJhaXNlIFZhbHVlRXJyb3IoJ2NoZWNrb3V0
IEhFQUQgZGlmZmVycyBmcm9tIGNvbm5lY3RvciBhdXRob3JpdHknKQogICAgaWYgZ2l0KCctQycs
IHN0cihkZXN0aW5hdGlvbiksICdyZXYtcGFyc2UnLCAnLS1pcy1zaGFsbG93LXJlcG9zaXRvcnkn
KSAhPSAnZmFsc2UnOgogICAgICAgIHJhaXNlIFZhbHVlRXJyb3IoJ2Z1bGwgYWNjZXB0ZWQgYW5j
ZXN0cnkgcmVxdWlyZWQnKQogICAgZm9yIG5hbWUgaW4gUkVRVUlSRUQ6CiAgICAgICAgaWYgbm90
IChkZXN0aW5hdGlvbiAvICdzY3JpcHRzJyAvIG5hbWUpLmlzX2ZpbGUoKToKICAgICAgICAgICAg
cmFpc2UgVmFsdWVFcnJvcignbWlzc2luZyBnb3Zlcm5lZCBjb21waWxlcjogJyArIG5hbWUpCiAg
ICBzeXMucGF0aC5pbnNlcnQoMCwgc3RyKGRlc3RpbmF0aW9uIC8gJ3NjcmlwdHMnKSkKICAgIGZy
b20gY2ZiX2NvbmRpdGlvbmFsX3JlY29tbWVuZGF0aW9uX3Byb2ZpbGUgaW1wb3J0IGxvYWRfcmV2
aWV3CiAgICAjIFZlcmlmeSBldmVyeSBpbW11dGFibGUgcmVmIGluIHJldGFpbmVkIGNhbm9uaWNh
bCBoaXN0b3J5LCBpbmNsdWRpbmcgY2xvc2VkCiAgICAjIHJldmlld3M7IHRob3NlIG9iamVjdHMg
cmVtYWluIG5lY2Vzc2FyeSB0byB2YWxpZGF0ZSBsYXRlciB0eXBlZCBwYWNrZXRzLgogICAgcmVm
cyA9IHt9CiAgICBsZWRnZXIgPSBkZXN0aW5hdGlvbiAvICdldmlkZW5jZS9vcGVyYXRpb25hbC9D
RkJfREVDSVNJT05fV0FJVF9MRURHRVIubWQnCiAgICBmb3IgYm9keSBpbiByZS5maW5kYWxsKHIn
XmBgYGNmYi1bXlxuXStcbiguKj8pXmBgYFxzKiQnLCBsZWRnZXIucmVhZF90ZXh0KCksIHJlLk0g
fCByZS5TKToKICAgICAgICBwYWNrZXQgPSBqc29uLmxvYWRzKGJvZHkpCiAgICAgICAgZm9yIHJv
dyBpbiBwYWNrZXQuZ2V0KCdyb3dzJywgW10pOgogICAgICAgICAgICByZWYgPSByb3cuZ2V0KCdy
ZXZpZXdfcmVmJykKICAgICAgICAgICAgaWYgcmVmOgogICAgICAgICAgICAgICAgcmVmc1socmVm
Wydjb21taXQnXSwgcmVmWydwYXRoJ10sIHJlZlsnYmxvYiddKV0gPSByZWYKICAgIGlmIG5vdCBy
ZWZzOgogICAgICAgIHJhaXNlIFZhbHVlRXJyb3IoJ25vIGdvdmVybmVkIGltbXV0YWJsZSByZXZp
ZXcgcmVmcyByZWNvdmVyZWQnKQogICAgdmVyaWZpZWQgPSBbXQogICAgZm9yIHJlZiBpbiByZWZz
LnZhbHVlcygpOgogICAgICAgIF8sIGNvbW1pdHRlZCA9IGxvYWRfcmV2aWV3KHJlZikKICAgICAg
ICB2ZXJpZmllZC5hcHBlbmQoZGljdChyZWYsIGNvbW1pdHRlZF9hdD1jb21taXR0ZWQpKQogICAg
cmV0dXJuIHsnc3RhdHVzJzogJ1NVUFBPUlRFRF9HSVRfUlVOVElNRV9WRVJJRklFRCcsICdyZXBv
c2l0b3J5JzogUkVQT1NJVE9SWSwKICAgICAgICAgICAgJ2hlYWQnOiBleHBlY3RlZF9oZWFkLCAn
d29ya3RyZWUnOiBzdHIoZGVzdGluYXRpb24pLAogICAgICAgICAgICAncHl0aG9uJzogc3lzLnZl
cnNpb24uc3BsaXQoKVswXSwgJ2ltbXV0YWJsZV9yZXZpZXdzJzogdmVyaWZpZWQsCiAgICAgICAg
ICAgICdzY29wZSc6ICdydW50aW1lIGFuZCBhbmNlc3RyeSBvbmx5OyBubyByZXNlYXJjaCwgcHVi
bGljYXRpb24gb3IgcnVuIGFjY2VwdGFuY2UnfQoKCmlmIF9fbmFtZV9fID09ICdfX21haW5fXyc6
CiAgICBwID0gYXJncGFyc2UuQXJndW1lbnRQYXJzZXIoZGVzY3JpcHRpb249X19kb2NfXykKICAg
IHAuYWRkX2FyZ3VtZW50KCctLWRlc3RpbmF0aW9uJywgdHlwZT1QYXRoLCByZXF1aXJlZD1UcnVl
KQogICAgcC5hZGRfYXJndW1lbnQoJy0tZXhwZWN0ZWQtaGVhZCcsIHJlcXVpcmVkPVRydWUpCiAg
ICBhID0gcC5wYXJzZV9hcmdzKCkKICAgIHRyeToKICAgICAgICBwcmludChqc29uLmR1bXBzKHBy
ZXBhcmUoYS5kZXN0aW5hdGlvbiwgYS5leHBlY3RlZF9oZWFkKSwgaW5kZW50PTIpKQogICAgZXhj
ZXB0IChWYWx1ZUVycm9yLCBPU0Vycm9yLCBzdWJwcm9jZXNzLlN1YnByb2Nlc3NFcnJvcikgYXMg
ZXhjOgogICAgICAgIHByaW50KGpzb24uZHVtcHMoeydzdGF0dXMnOiAnQ09NUFVUQVRJT05fUlVO
VElNRV9VTkFWQUlMQUJMRScsCiAgICAgICAgICAgICAgICAgICAgICAgICAgJ2Vycm9yX3R5cGUn
OiB0eXBlKGV4YykuX19uYW1lX18sCiAgICAgICAgICAgICAgICAgICAgICAgICAgJ3Njb3BlJzog
J25vIHB1YmxpY2F0aW9uIGF0dGVtcHRlZDsgcHJlc2VydmUgdGFzayBzY2hlZHVsZXMnfSkpCiAg
ICAgICAgc3lzLmV4aXQoMSkK
CFB_EXACT_HELPER_B64
test "$(wc -c < "$scratch/cfb_runtime_checkout.py")" -eq "$expected_size"
test "$(git hash-object "$scratch/cfb_runtime_checkout.py")" = "$expected_blob"
printf '%s\n' DIRECT_HELPER_BYTES_VERIFIED
"$checkout_python" - "$scratch/cfb_runtime_checkout.py" "$pinned_head" "$scratch/checkout" <<'CFB_CHECKOUT_PY'
import json
import runpy
import subprocess
import sys

def report(stage, error, category, **extra):
    print(json.dumps({
        "status": "COMPUTATION_RUNTIME_UNAVAILABLE",
        "stage": stage,
        "error_type": type(error).__name__,
        "failure_category": category,
        **extra,
    }))
    raise SystemExit(1)

def git_stage(error):
    command = error.cmd
    if not isinstance(command, (list, tuple)) or not command or command[0] != "git":
        return "RETAINED_REVIEW_OR_OTHER_SUBPROCESS"
    verb = command[3] if len(command) > 3 and command[1] == "-C" else command[1]
    return {
        "clone": "GIT_CLONE",
        "cat-file": "PINNED_COMMIT_LOOKUP",
        "merge-base": "PINNED_ANCESTRY",
        "checkout": "DETACHED_CHECKOUT",
        "rev-parse": "HEAD_OR_SHALLOW_CHECK",
        "show": "RETAINED_REVIEW_LOOKUP",
    }.get(verb, "OTHER_GIT_SUBPROCESS")

helper, head, destination = sys.argv[1:]
prepare = runpy.run_path(helper)["prepare"]
try:
    result = prepare(destination, head)
except subprocess.CalledProcessError as error:
    stage = git_stage(error)
    stderr = error.stderr or ""
    if isinstance(stderr, bytes):
        stderr = stderr.decode("utf-8", "replace")
    stderr = stderr.casefold()
    signatures = (
        ("DNS_RESOLUTION", ("could not resolve host", "could not resolve proxy", "temporary failure in name resolution")),
        ("AUTHORIZATION", ("authentication failed", "could not read username", "repository not found", "error: 401", "error: 403", "terminal prompts disabled")),
        ("TLS_VERIFICATION", ("certificate problem", "certificate verify failed", "ssl certificate")),
        ("NETWORK_TIMEOUT", ("timed out", "timeout", "connection reset", "could not connect", "failed to connect")),
        ("MISSING_GIT_OBJECT", ("bad object", "not a valid object", "unknown revision")),
    )
    category = next((name for name, terms in signatures if any(term in stderr for term in terms)), None)
    if category is None:
        category = "PIN_NOT_ANCESTOR" if stage == "PINNED_ANCESTRY" and error.returncode == 1 else "UNCLASSIFIED_GIT_FAILURE"
    report(stage, error, category, exit_code=error.returncode, stderr_present=bool(stderr))
except subprocess.TimeoutExpired as error:
    report(git_stage(error), error, "NETWORK_OR_SUBPROCESS_TIMEOUT")
except (ValueError, OSError) as error:
    report("WORKTREE_OR_RETAINED_REVIEW_VALIDATION", error, "VALIDATION_OR_LOCAL_RUNTIME")

print(json.dumps(result))
CFB_CHECKOUT_PY
```

Original connector-to-shell JavaScript example removed: its named tools are not guaranteed exposed. Discover actual runtime actions; never simulate an unavailable connector-to-shell bridge. Preserve preceding exact-byte shell fallback only if callable and verified. Continue same-run workload or fail closed at the precise unavailable stage.


HEALTH READBACK EXECUTION — After independently reading back RUN_STARTED, resolve exact current main through the authenticated GitHub connector. Through the connector's GitHub fetch operation, read /git/commits/<verified-commit> and /git/trees/<commit-tree-sha>?recursive=1. Require the returned commit SHA and tree SHA to match their respective bindings and truncated=false. Enumerate all recovery-index paths, select newest accepted authority, and record tree SHA, index count, selected path, size and blob SHA. A bounded search is partial evidence.
HEALTH_BLOB_CHECK_20261117_R1 — Immediately after authenticating the nontruncated tree and selecting the accepted index, bind entries to that index and the four named canonical files below. Execute this JavaScript in the connector orchestration cell with entries set to those five complete tree entries. Preserve full returned text inside the cell. Persist the revision, transport, per-file expected and actual size/SHA and result in Health evidence. Continue eligible independent audits after individual failures. Use the documented fallback on a failed connector read or verification when supported, preserving the first error; a metadata match alone is insufficient. Hashing uses the connector without a local checkout.

```javascript
function gitBlob(s) {
  const bytes = unescape(encodeURIComponent(s));
  const body = "blob " + bytes.length + "\0" + bytes;
  const total = Math.ceil((body.length + 9) / 64) * 64;
  const data = new DataView(new ArrayBuffer(total));
  for (let i = 0; i < body.length; i++) data.setUint8(i, body.charCodeAt(i));
  data.setUint8(body.length, 128);
  data.setUint32(total - 4, body.length * 8);
  const rol = (x, n) => (x << n) | (x >>> (32 - n));
  const words = new Int32Array(80);
  const hash = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476, 0xc3d2e1f0];
  for (let offset = 0; offset < total; offset += 64) {
    for (let i = 0; i < 16; i++) words[i] = data.getInt32(offset + i * 4);
    for (let i = 16; i < 80; i++) words[i] = rol(words[i-3] ^ words[i-8] ^ words[i-14] ^ words[i-16], 1);
    let [a,b,c,d,e] = hash;
    for (let i = 0; i < 80; i++) {
      const band = Math.floor(i / 20);
      const f = band === 0 ? (b & c) | (~b & d) : band === 2 ? (b & c) | (b & d) | (c & d) : b ^ c ^ d;
      const k = [0x5a827999,0x6ed9eba1,0x8f1bbcdc,0xca62c1d6][band];
      const next = (rol(a,5) + f + e + k + words[i]) | 0;
      e=d; d=c; c=rol(b,30); b=a; a=next;
    }
    [a,b,c,d,e].forEach((value,i) => { hash[i] = (hash[i] + value) | 0; });
  }
  return { size: bytes.length, sha: hash.map(x => (x >>> 0).toString(16).padStart(8,"0")).join("") };
}
const results = await Promise.all(entries.map(async ({path,size,sha}) => {
  const check = {path, expectedSize:size, expectedSha:sha, transport:"github_fetch_blob"};
  try {
    const response = await tools.mcp__codex_apps__github_fetch_blob({
      repository_full_name:"munchie50/cfb-acquisition-bridge", blob_sha:sha
    });
    const body = response.structuredContent?.content;
    if (response.isError || typeof body !== "string" || !body.length) {
      throw new Error(response.content?.[0]?.text || "Missing complete blob text");
    }
    const actual = gitBlob(body);
    return {...check, actualSize:actual.size, actualSha:actual.sha,
      pass:actual.size === size && actual.sha === sha};
  } catch (error) {
    return {...check, pass:false, error:String(error).slice(0,300)};
  }
}));
text(results);
```

Run the late-afternoon CFB maintenance health check. For CFB, begin at connected GitHub repository munchie50/cfb-acquisition-bridge; deterministically discover/read back the newest accepted CFB_ENGINE_CURRENT_RECOVERY_INDEX_v*.md and active cadence/output controls from repository state/commit history, not stale version anchors or code-search indexing. Follow active v1.247 football-week cadence or later accepted superseding authority. This is an integrity/health layer, not a competing market-monitor or Hot Sheet producer. MARKET-MONITOR COMPLETION + OWNERSHIP AUDIT: independently enumerate every CFB Market Monitor cycle that should have occurred since the prior CFB Engine Health run. For each expected cycle, verify a persisted/read-back RUN_STARTED marker and a separate conforming terminal RUN_PASS/RUN_INCOMPLETE/RUN_FAIL receipt under evidence/run_receipts/. RUN_PASS additionally requires applicable canonical operational surfaces and the required governed Hot Sheet for that cycle to have been persisted/read back. Missing terminal receipt, start-only evidence, missing required Hot Sheet, or unproved readback is an incomplete Market Monitor cycle; scheduler last_run_time alone is never completion evidence. Also verify the CFB Market Monitor remains the sole primary Hot Sheet producer, is enabled, retains the governed 07:00/13:00 CT Sunday-Saturday cadence, and that Evening Availability/Weekly QA/Health remain downstream consumers or integrity layers rather than competing Hot Sheet producers. If Market Monitor is unexpectedly disabled but its authority, ownership, cadence, and scope remain unchanged and no governance conflict is present, restore only its enabled state, re-read task topology, and record that recovery. Never replay or reconstruct the missed historical cycle; recovery resumes with the next prospective cycle. If ownership/cadence/scope is ambiguous or changed, fail closed and identify the governance gate instead of restoring blindly. Any task enable/disable, schedule change, consolidation, split, rename, or responsibility transfer is incomplete until an OUTPUT OWNERSHIP / COVERAGE CHECK proves: exactly four active recurring production tasks, one enabled primary Hot Sheet producer, correct cadence, downstream consumers intact, no competing producer, and one intentionally open task slot. Do not create or enable a fifth recurring watchdog; receipt-watch responsibility is incorporated here. Read back canonical CFB_MARKET_MONITOR_STATE.md, CFB_DECISION_WAIT_LEDGER.md, CFB_EXECUTION_LEDGER.md and CFB_POSTGAME_FIRST_FROZEN_SCORECARD.md. Verify persistence/readback, accepted Champion/FIRST_FROZEN/REFRESH chronology, repository Monday/Tuesday/Wednesday automation status when applicable, source/data changes, decision/WAIT integrity, production wager integrity, separate $20 sandbox integrity, settlements, TIME-HIDDEN layers and overlapping experimental exposure. If a required earlier run failed or is incomplete, identify the blocker and next safe action rather than silently duplicating or reconstructing it. Persist any health-specific governed change plus a conforming receipt; NO_MATERIAL_CHANGE requires readback notation. Keep downstream market/availability/execution/outcome evidence separate from frozen Champion. When authoritative finals exist, score only genuinely pre-event FIRST_FROZEN predictions; never reconstruct missing predictions/decisions from outcomes. 
EVENING AVAILABILITY COMPLETION AUDIT: also enumerate every expected Wednesday/Thursday/Friday evening cycle since the prior health audit using the existing 19:30 America/Chicago flexible schedule and its permitted start window. Never flag a cycle before its window has elapsed. For each due evening cycle, reconcile invocation metadata with cycle-specific terminal-candidate readback and separate RUN_CLOSURE under evidence/CFB_TERMINAL_RUN_RECEIPT_CLOSURE_CONTRACT_2026-10-05.md; RUN_PASS additionally requires every applicable changed operational surface to be persisted/read back. Missing terminal/closure is incomplete or unverified, never success from last_run_time. Recover the invocation response where permitted before assuming a start-only cycle is still running; distinguish reported runtime result from durable closure. Check Evening Availability is enabled with its existing cadence and downstream ownership. Report drift and the next safe action; this audit grants no new task-lifecycle mutation authority and never replays missed cycles. Preserve all four existing production tasks and disabled diagnostic tasks. Record this evening audit in the existing health receipt, including no-new-due-cycle when applicable.
UNRESOLVED CYCLE CARRY-FORWARD: the prior health invocation timestamp is not a successful-reconciliation watermark. Recover the last persisted health audit's unresolved evening-cycle identities and carry every unresolved cycle forward alongside newly due cycles; do not drop a gap merely because it predates the latest health invocation. If the prior audit/receipt is missing or cannot be read, recover from the last proven coverage boundary and report any unknown coverage rather than advancing it silently. Each health receipt must record the audited coverage boundary, unresolved cycle identities, evidence class, blocker and next safe action. Resolve a historical gap only with genuine contemporaneous completion evidence or an explicit governed disposition retaining the gap; never backfill or upgrade it from a later successful cycle.
MARKET MONITOR RECEIPT WATCH: Apply evidence/scheduler_qa/CFB_MONITOR_GITHUB_RECEIPT_WATCH_20261109.md within the existing Health audit. Correlate both due Monitor slots with exact scheduler and GitHub evidence, distinguish unproved startup, missing closure, verified incomplete closure and verified publication, and persist the last proved stage and first blocker in the normal Health audit. This is detection only; never trigger or publish recovery from Health.

CFB-WIDE CLOSURE DEBT: apply the unresolved-cycle carry-forward rule to Market Monitor as well as Evening Availability, prior CFB Health coverage and required CFB Weekly QA outputs. Recover evidence/scheduler_qa/CFB_EVENING_HEALTH_COVERAGE_AND_OCT09_AFTERNOON_RECONCILIATION_V6.md and its CFB-wide extension before advancing a coverage boundary. The latest automation last_run_time is never a proved audit watermark. Retain earlier incomplete records as historical gaps; distinguish their historical disposition from still-actionable prospective work. A later successful monitor, manual recovery, task restoration or unrelated QA run does not close another cycle's evidence debt. If exact prior Health closure/coverage cannot be recovered, report COVERAGE_UNVERIFIED with the bounded search and last actually proved evidence, rather than claiming a full-history audit. Check required prior CFB Weekly QA outputs against their accepted artifact/disposition ancestry before labelling them lost or unresolved. This is CFB audit coverage only; it does not change Big Nine authority, authorize historical reconstruction or add task-lifecycle permissions.
HEALTH TERMINAL FAILURE CONTAINMENT: obey evidence/CFB_GITHUB_CONTENTS_PERSISTENCE_PROCEDURE_2026-10-03.md including Health integration, allowed retry limits and permitted diagnostic-response envelope, and evidence/CFB_TERMINAL_RUN_RECEIPT_CLOSURE_CONTRACT_2026-10-05.md. Persist/read back applicable Health evidence, then a terminal candidate, then separate RUN_CLOSURE after candidate readback. If terminal persistence fails, report the earned incomplete/fail result plus TERMINAL_PERSISTENCE_UNAVAILABLE, last proven stage and permitted content-free diagnostic fields; mark unknown values UNAVAILABLE. Do not advance proved coverage, infer closure from scheduler metadata, call another destination a GitHub completion receipt, or evade write restrictions. Own repository/tool failure never authorizes schedule changes, task disabling, replacements or reruns. Existing governed Market Monitor enabled-state restoration remains permitted only after its original authority/ownership/cadence/scope/conflict checks and independent four-task readback; report configuration recovery separately from its receipt-persistence proof. Retain unresolved cycles and historical failures.
USER-APPROVED CONSENSUS / CAESARS CONTROL: recover and obey evidence/CFB_CONSENSUS_BENCHMARK_AND_CAESARS_EXECUTION_CONTROL_2026-10-10.md. Audit the control's source separation, constituent qualification, unavailable labels and current Hot Sheet fidelity within your existing CFB scope; do not become a market/Hot Sheet producer. Prefer qualified multi-book consensus as the market benchmark, Caesars as the independently verified execution offer, and Engine Prediction (Frozen) as the unchanged independent model opinion. Preserve identified constituent line/price pairs, clocks, count and dispersion; single/mixed-book observations are labelled fallback, never consensus. Missing qualification means CONSENSUS_UNAVAILABLE; unverified actual Caesars remains UNVERIFIED. No automatic bet from book disagreement, no invented price/EV, no loosening established limits or practical cutoffs. Preserve all existing scope, authority, persistence/closure, ownership and schedule controls.

USER-DIRECTED RECOMMENDATION / VENUE SEPARATION — October16: Recover the October16 decoupling section of evidence/CFB_CONSENSUS_BENCHMARK_AND_CAESARS_EXECUTION_CONTROL_2026-10-10.md. It supersedes any older interpretation of this prompt requiring a Caesars line to form, display or rank a supported recommendation. Missing Caesars alone is NOT a recommendation blocker: show venue confirmation pending separately; do not claim a verified offer or actual execution. Preserve all independently earned maturity labels, model/market/material evidence, original acceptable number/price and deadlines; never invent a pick, threshold, EV, stake, source clock or consensus. Current neutral publishing supports only PASS/INCONCLUSIVE; qualifying richer recommendation/WAIT presentation remains OPEN, never downgrade an earned richer state to fit it. When computation is available, execute scripts/cfb_hot_sheet_readiness.py against the actual canonical market/decision/original-lineage files with the actual audit clock to report individual blockers, saved-source boundary, elapsed current quotes and overdue decisions. It validates saved packets at their own boundary and diagnoses age separately, never refreshes or retimes them. For a qualified multi-book collection, scripts/cfb_consensus_reference.py provides a bounded descriptive formatter; independently qualify source truth/operator identities first, retain all constituents/clocks, exclude Caesars, preserve unknown updates and honest unavailable status. Formatter success is not acquisition, a recommendation or full-run acceptance. Do not impose betting/execution prerequisites on an observation or experimental lean. Preserve sole Monitor publication ownership, downstream Evening scope, integrity-only QA roles, four-task topology, all schedules and scientific/execution boundaries. Natural use of these additions remains to be demonstrated.

BOUNDED CONDITIONAL V3 — USER-DIRECTED HOT SHEET QA: The October16 V3 section of evidence/CFB_NEUTRAL_SOURCE_DERIVED_PUBLICATION_CONTRACT_2026-10-12.md supersedes only the earlier claim that all conditional publication is unsupported. A genuinely earned CONDITIONAL row may use the normal compiler/renderer with an already persisted immutable review_ref, accepted original prediction, qualified future kickoff, independently qualified non-Caesars constituents, material/rule review, original line/price limits and preserved practical cutoff. Recover the actual review commit in accepted runtime ancestry first. No review or bet may be invented to pass the schema. Neutral V1/V2 remain unchanged; WAIT/BET NOW and unsupported richer facts still need separate qualification. Caesars remains optional venue confirmation. No source/review acquisition or natural adoption is proved by code tests. Preserve ownership, all four schedules and all prior controls.

USER-DIRECTED PRIORITY CHANGE — 2026-10-17 09:34 America/Chicago: Big Nine is PAUSED until the user explicitly resumes it. Do not run Big Nine research, monitoring, QA, private Yahoo/league-state checks, backup/recovery verification, recommendations or development. Preserve its existing records. Evaluate and report CFB independently; Big Nine is PAUSED / OUT OF SCOPE, not a CFB failure or incomplete prerequisite. Preserve genuine CFB blockers and historical evidence. This instruction supersedes older dual-engine responsibilities only.

USER-DIRECTED STANDING FULL-EVALUATION STANDARD — October17 11:14CT: Recover the standing full-evaluation section and bounded prospective PASS-reconsideration profile in evidence/CFB_NEUTRAL_SOURCE_DERIVED_PUBLICATION_CONTRACT_2026-10-12.md. Preserve true full-slate evaluation across favorite/underdog spreads, overs/unders, moneylines and bounded plausible parlays; do not return a static five-pick list, refresh only existing picks or copy all PASS decisions without checking continuing justification. Rank defensible current opportunities after weighing supporting evidence AND ordinary risks; latest4–5 request/prior5–7weeklyaim are not quotas. Reuse prior analysis only after checking material changes and its ongoing applicability; distinguish newly assessed, revalidated and missing research in existing provenance/reasons. Missing research is not proof of no value. Qualified new prospective reviews may reconsider earlier PASS, preserving exact prior records, original established limits/cutoffs and all model/source guards; no silent reopen or no-chase relaxation. Assess totals and ML independently; bounded parlay assessment compares quoted joint price when available, dependence, fragility and duplicate exposure with singles under existing production/sandbox authority. NO_PREFERRED_PARLAY is valid; no invented joint probability/EV/payout/stake. Keep supporting code QA separate from useful complete user decisions. User says they will MOST LIKELY bet: this is intent only, never create execution/money records without actual confirmation/tickets; actual tickets are real-money unless explicitly stated otherwise. Frozen predictions stay independent from bets/outcomes. Use existing four tasks and artifacts, no new framework/schedule/task. Big Nine remains PAUSED. Configuration installation is not demonstrated natural consistency. Within existing integrity/QA scope, assess whether production actually delivered this breadth, timely usable decisions and source/review coverage; inspect missing opportunities and cost of controls alongside integrity/results. Do not become a competing market or Hot Sheet producer.

USER-DIRECTED HOT SHEET STABILIZATION — October17 15:23CT: Follow the stabilization section of evidence/CFB_NEUTRAL_SOURCE_DERIVED_PUBLICATION_CONTRACT_2026-10-12.md and the active/deferred October17 entry in evidence/CFB_ENGINE_REVIEW_FINDINGS_AND_DURABLE_ACTION_REGISTER_2026-09-28.md. TOP 10 OPPORTUNITIES supersedes older card-width targets; distinguish supported actionable/conditional entries and never manufacture ten bets. At every existing applicable review, include all games with remaining practical windows, including PASS, across both spread sides, both moneylines and over/under independently; explicitly address alternates/team totals where offered/supported or explain unavailable/not evaluated, plus plausible parlay suitability. Use existing readiness audit review_required_game_ids/review_window to select work, not as proof research occurred or authority to reopen. Preserve original limits/cutoffs and use existing prospective reconsideration evidence for changed decisions. Missing timing/research remains visible debt. Existing cycles only: do not add tasks, triggers or gates; report unserved final-review windows honestly. Monitor publishes, Evening supplies downstream updates, Health/Weekly audit within existing ownership. Deferred ideas 5–19 are preserved for later evaluation, not automatic implementation: inspect the durable register at existing Weekly QA/manual maintenance and prioritize small justified changes. Installation/tests do not prove natural recurring consistency.
INTEGRATION / RENEWAL STATUS — October17 15:32CT: PR2 merged834d9d09e3f555fe009f66d49cbe80edc437004b and existing CI39067045249/job117496760706 SUCCESS. Earlier pending-PR note is superseded: use current readiness review_required_game_ids/review_window. Queue enumeration is not completed analytical review. Before assuming a new BET NOW/WAIT adapter is necessary, apply the October17 existing conditional-renewal clarification in the active publication contract: a genuinely NEW immutable source/material/price review can issue a new CONDITIONAL review checkpoint after an earlier checkpoint while preserving original line/price and final practical cutoff. Existing full-history/render replay supports that path; old expired review remains invalid. Synthetic replay is not actual research or a live recommendation. Keep unsupported richer semantics separate; no final-cutoff extension. Natural full-cycle/top10/all-market consistency remains open.

WEEK8 ANCESTRY/PROFILE CONSUMPTION — OCT19 CT QA: Recover evidence/CFB_WEEK8_ORIGINAL_LINEAGE_PUBLICATION_PROFILE_2026-10-20.md. Original accepted FIRST_FROZEN covers56 Week8 targets/49 predictions/7 exclusions; missing Week8 publication is not proof of missing original model numbers. Tuesday REFRESH generation/independent acceptance remains separate. Use explicit WEEK8 profile when auditing a supported Week8 typed packet/view, retaining Week7 historical ancestry and independent original-archive field checks. Distinguish611-test CI/retained-source synthetic-decision replay from genuine current source/review/kickoff/decision/publication and natural completion. Retain exact unresolved phases and historical gaps; ownership/schedules unchanged.

USER-DIRECTED OCT24 HEALTH DISPOSITION CORRECTION: Recover the October24 repair-versus-history reconciliation in evidence/scheduler_qa/CFB_EVENING_HEALTH_COVERAGE_AND_OCT09_AFTERNOON_RECONCILIATION_V6.md before repeating a defect or next action. For each carried incomplete cycle, distinguish the original cycle result, present remediation status and remaining producer-specific natural demonstration. Bind a claimed current defect to current implementation/repair evidence, not just the failed cycle's old audit. The Friday Evening cycle CFB_EVENING_AVAILABILITY_20261024T012553Z remains RUN_INCOMPLETE, but the closed-conditional defect was already repaired in merged PR5 and naturally adopted by both Saturday Monitor cycles. Do not request the same compiler repair again or claim current implementation lacks that transition. Evening-specific natural adoption and sustained reliability remain separately unproved until an applicable future Evening run. Retain older unresolved coverage identities and actual current freshness findings; this correction does not auto-pass Health, erase historical gaps, advance unproved coverage, certify quotes as current, or replay a cycle. Report current task execution/closure, present service health and historical exceptions distinctly in the existing audit and concise response; use the actual governing terminal criteria. Preserve all four task configurations apart from this Health instruction, existing cadences and sole Monitor publication ownership.

USER-DIRECTED SHARED FIRECRAWL BUDGET — OCT24: Before chargeable Firecrawl work recover evidence/CFB_FIRECRAWL_CYCLE_BUDGET_CONTROL_2026-10-24.md and obey its shared at-most1000-credit limit and cumulative daily pacing across all CFB scheduled/manual work. Read actual provider balance/cycle bounds; never issue a paid no-credit probe at zero. For B=min(1000,planCredits), N=ceil(actual cycle seconds/86400), current cycle-day bucket k, release only C=floor(B*k/N); subtract account-observed cycle consumption and confirmed/reserved unsettled cost, sharing unused released allowance rather than giving each task a new pool. Recheck before each serial request and require a known upper cost within remaining allowance; defer on unknown costs, concurrent/unsettled acquisition or invalid cycle metadata. Prioritize complete Monitor captures/material evidence, then genuinely new Evening evidence and necessary WeeklyQA checks; Health ordinarily uses saved repository/receipt/task/account state without chargeable Firecrawl research. Preserve source freshness/completeness and sole Monitor ownership: missing budget means an explicitly unserved research phase/incomplete result, never stale-as-fresh, forced PASS or invented completeness. Record bounded budget facts in existing receipts; no new tracker/task, billing/top-up/upgrade/account change or cadence mutation. Do not spend just to hit1000 or promise exact provider enforcement; apply the actual28–31day cycle and read renewed metadata after reset. Current balance was0; do not repeatedly call paid acquisition while exhausted. No quota multiplier per task or manual invocation. Installation is not natural compliance.

USER-AUTHORIZED LEARNING FOLLOW-THROUGH — October24 CT: Within existing Health scope, audit existing actions CFB_QA_LEARNING_FOLLOW_THROUGH_20261023 and CFB_QA_QUALIFICATION_LIMITS_REVIEW_20261023 for the latest applicable Weekly QA's proved baseline batch, missing evidence and next boundary. Distinguish NOT_YET_DUE, demonstrated use, blocked work and pending proof; do not infer completion or lateness from scheduler timestamps.

Distinguish identity visibility, analytical review evidence, unfinished research, exclusions and permanent gaps. PR10's readiness repair is already merged/tested; inspect actual next-producer use and benefit before proposing the same fix again. Supporting retained evidence: evidence/audits/CFB_WEEK8_EVALUATION_EVIDENCE_RECONCILIATION_20261025.md and companionJSON. Forty packet-uncertified entries were not40 unreviewed games.

Carry omissions and demonstrated benefit/cost in existing audit/action records. Keep Health an integrity/follow-through audit: no competing research, historical-baseline rebuild, unauthorized scoring, equivalent static retries, task/prompt/schedule changes or dispatched runs. Existing budgets, ownership and all guards remain. Installation/tests do not prove better predictions, profitable edge or scheduled reliability.
Fold-in checkpoint: evidence/run_receipts/CFB_LEARNING_FOLD_IN_20261025T041030Z.md. Audit Weekly QA against its latest verified completed-batch/next-boundary append, retaining earlier entries as history. Do not execute the historical baseline or treat a superseded initial resume boundary as current.

ACCEPTED ROUTINE AUTHORITY: Read main:evidence/CFB_ROUTINE_V5_1_SELECTIVE_PRODUCTION_AMENDMENT_20261030.md after original v5.0 authority. Apply only accepted v5.1-A bounded WAIT sweep and v5.1-C evidence-based closure labels. v5.1-B and other v6 controls remain QA. Record natural-use/regression evidence and rollback each independently if needed; do not treat the amendment as a model or scheduler fix.


CFB HEALTH REPORTING — NOVEMBER 12: Begin the user-facing report with whether this Health inspection finished and whether any of its own required checks remain unverified. Give each due monitored slot its own plain-English outcome and first evidenced blocker, followed by the practical effect on collection, reconciliation or Hot Sheet publication. Correlate the scheduler launch with exact cycle receipts and, where applicable, the collector run and artifact. Distinguish no launch recorded, started then blocked, terminal evidence missing, and verified delivery. If a collector lookup returned no matching run, report the lookup result and keep dispatch cause unknown. Example from November 12: “Health inspection finished. The evening task started and stopped at Git checkout. The collector lookup found no matching launch, and evening reconciliation did not run.” Preserve existing Health closure codes, coverage checks, historical exceptions and evidence requirements. Label any unresolved coverage as current or historical and identify what evidence is missing. Keep Health integrity-only.

CFB DATA GAP FOLLOW-THROUGH — Apply evidence/operational/CFB_DATA_GAP_FOLLOW_THROUGH_20261113.md in this existing run. Audit incomplete game reviews and missing ticket/recommendation follow-through; report exact gaps and next owners in the existing receipt. Verify the durable receipt before closure.

DAILY HEALTH ANALYTICS ADDENDUM (Nov20): After original Health checks, audit existence/freshness/identity of certified analytics exports and run evidence, distinguish BUILT/EXECUTED/VERIFIED/ACCEPTED/PRODUCTION, and flag missing source provenance or leakage. Analytics missingness is not proof of primary Health failure. Follow evidence/operational/CFB_ANALYTICS_V1_CADENCE_AND_LEARNING_CONTRACT_20261120.md; no competing market collection.