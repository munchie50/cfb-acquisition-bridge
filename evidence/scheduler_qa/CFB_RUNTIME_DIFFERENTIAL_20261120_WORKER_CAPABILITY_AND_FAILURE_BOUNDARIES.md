# CFB runtime differential — proven boundaries, not production acceptance

## Observations
- November 6 NATURAL_ONE_TIME_SCHEDULED shadow: evidence/scheduler_qa/CFB_EXECUTION_20261106T030123Z_vz8rxk3_RESULT.json, authentic helper blob b13930cb714eb87c8dce6136ffab6fbceeb44898 (3780 bytes), Python 3.12.14, full-history Git checkout PASS, retained compiler/render PASS, external ESPN HTTP 200. Operator offer update time and venue execution UNVERIFIED. This is a bounded historical test, not current production.
- November 18 NATURAL_SCHEDULED_ONE_TIME rehearsal: evidence/scheduler_qa/CFB_REHEARSAL_20261118T234623606Z_unknown_RESULT.json, original Week12 70/70 source capture, compiler/render PASS for 6 reviewed games, 64 carried decisions; full slate review and named offer qualification INCOMPLETE. DraftKings public URL returned 195-byte Site Unavailable body despite HTTP 200. This is a distinct application-level source/offer defect, not Git DNS.
- November 20 13CT production Market Monitor: evidence/run_receipts/CFB_MARKET_MONITOR_RUN_CLOSURE_20261120T185905892Z_scheduled-20261120-1300-ct-turn11.json, RUN_INCOMPLETE, canonical publication not verified.
- Current manual chat shell Python 3.13.5, Git 2.47.3; socket.getaddrinfo for github.com and api.github.com both failed [Errno -3] Temporary failure in name resolution. GitHub connector authenticated read separately PASS. This is a **tool-environment differential** and must NOT be labeled proof of scheduled-worker DNS.
- Existing original Nov19 combined connector-to-shell JavaScript referenced tools.exec_command and tools.mcp__codex_apps__github_fetch*; current exposed connector tools are mcp__GitHub__fetch* and direct shell is a separate tool surface. The obsolete JS example was removed from all four production task prompts with backups/readbacks. Do not confuse removal with successful live checkout.

## Differential diagnosis
1. If connector reads succeed and shell DNS fails, the fault boundary is connector-to-execution runtime networking/tool exposure, not necessarily repository permissions or missing code.
2. If checkout succeeds and complete CBS source is unavailable, classify SOURCE_CAPTURE or SOURCE_FORMAT; Nov18 lxml th|td fix already exists and should not be reinvented.
3. If source and compiler succeed but bookmaker page is Site Unavailable or quotes lack update clock/venue qualification, classify OFFER_QUALIFICATION; do not infer book offers from HTTP 200.
4. If compiler succeeds but canonical ledger writes fail on multi-megabyte HTTP/2 request, classify CANONICAL_WRITE_TRANSPORT; existing evidence/run_receipts/CFB_WEEK12_20261120_WRITE_TRANSPORT_WORKAROUND_DEEP_DIVE.md proves 3.15MB prefix success and 4.19MB failure. This is separate from runtime checkout.
5. If canonical writes and selected Hot Sheet readback pass but task still closes incomplete, isolate the exact original publication/decision gate and its deadline rather than relaxing acceptance globally.

## Next natural production test (no extra task)
After RUN_STARTED readback, log one matrix of actual exposed GitHub connector, Python/shell, HTTPS in same runtime, helper byte transfer, pinned checkout, fresh CBS capture, original refresh_rows/compile, full slate review, canonical write, selector readback, and closure. For each, record PASS/FAIL/NOT_EXPOSED/NOT_ATTEMPTED and first failing operation. No duplicate DNS-first probe, historical fixture replay, or repeated synthetic QA. Continue independent downstream evidence when dependency blocks, but do not claim RUN_PASS or wagers.

## Safety and scope
Diagnostic comparison only. No frozen champion, model, accepted ledger, wager, task count, schedule or publication change. Historical scheduled shadow is not a live production pass.
