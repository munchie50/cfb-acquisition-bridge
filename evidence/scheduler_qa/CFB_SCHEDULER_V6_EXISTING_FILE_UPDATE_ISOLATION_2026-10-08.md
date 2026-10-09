# Test Routine v6 — existing-file update isolation

Status: MANUAL DIAGNOSTIC PASS, production write failure still OPEN.

Controlled existing-file target: evidence/scheduler_qa/CFB_SCHEDULER_V6_FAST_LOOP_49_ROW_PAYLOAD_PREPARED_2026-10-08.md.
Before SHA: 47f4211880d1c8eba7da3a0faaf2e859b7330a91.
Update: append one diagnostic-only observation; all prior checkpoint facts retained.
GitHub update commit: dfe96eef6a86e40057ab87d33bc42cd99ec24f1c.
After SHA: 1336b51ca1bb4a8a8fb12612b3a148d9ba18f3db.
Independent exact-content readback: PASS.

Comparison: October 8 morning scheduled Market Monitor reported two safety-check rejections updating existing canonical evidence/operational/CFB_MARKET_MONITOR_STATE.md, SHA c8616b340917e5db2674ec6c16581dd0d09275a5. Current independent readback still has this SHA, with 28,865 characters. Therefore GitHub update_file is not universally blocked; failure may depend on target path, content, request shape, or execution context. No causal distinction among these is proven yet. Do not modify canonical market state as a diagnostic experiment.

Next controlled tests: use a newly isolated scheduler_qa fixture to vary replacement payload size and content independently while keeping source authority, readback, and SHA guards. Do not infer scheduled-run health from manual connector success. Four production tasks unchanged; no wager or frozen prediction mutation.
