# CFB Monitor — routine authority and scheduling-mode differential
Date: 2026-10-30. Status: QA diagnostic verified by live task peek; no production mutation.

Routine: Production Routine v5 and Test Routine v6 for scheduler diagnosis, subject to newer accepted contracts and current recovery frontier. Consulted evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_245.md and operational Friday supersession. This QA note is subordinate, not production authority.

Fresh four-task peek: Market Monitor enabled exact_schedule last NO_UPDATE; Weekly Engine QA enabled exact_schedule last completed; Evening Availability enabled flexible_schedule last completed; Engine Health enabled flexible_schedule last completed. Therefore the claim 'exact_schedule always fails' is contradicted by the Weekly QA last completion. This does NOT prove the Monitor's exact_schedule path is healthy or that the completed QA ran at its natural intended time; timing-mode causal hypothesis remains unproven and weaker.

Follow-up differential: inspect Monitor-specific task execution bootstrap, prompt/context provisioning, connection/tool availability and invocation logs if exposed; compare last natural successful Monitor task configuration at that date before changing timing_mode. Current task metadata does not expose startup exception. Never confuse no linked chat/no receipt with definitive no dispatch.

Production protection: four enabled tasks retained; no task run_now, no schedule, timing mode, prompt, cloud merge, canonical model, Hot Sheet, wager or ledger changes. Preserve after-Friday-13:00 grouped review and UCF expired-old-review boundary. Next natural Monitor requires receipt-directory enumeration, terminal and canonical independent readback, and full-slate acceptance; RUN_PASS cannot be inferred from task status alone.
