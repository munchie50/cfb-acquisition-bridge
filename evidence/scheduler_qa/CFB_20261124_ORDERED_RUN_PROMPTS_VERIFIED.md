# Nov. 24 CT four-task ordered prompt verification

Exact prompt-only rollback records were independently read and verified before each serialized edit. Full live prompts were independently read back and matched. Task IDs, schedules, enabled states, ownership and environment settings matched the pre-edit configurations.

| Task | Installed SHA-256 | Rollback | Rollback blob |
| --- | --- | --- | --- |
| CFB Market Monitor Rebuilt | 57d27e24d651a2a5ef405055031059b37dab54a4dcf0e72dd13ba0f786f2e540 | [Exact restore](CFB_20261124_MARKET_MONITOR_ORDERED_RUN_PROMPT_ROLLBACK.json) | 99d67234d42c577b3a78465d29605e959b61d20d |
| CFB Engine Health Rebuilt | 1d775ded0da29e41ba40d4756eebfb690fd50b7734f70e2df56bef280ea9a4ba | [Exact restore](CFB_20261124_ENGINE_HEALTH_ORDERED_RUN_PROMPT_ROLLBACK.json) | f76294215ae499bcd31d569b5db0d1352439ace1 |
| CFB Evening Availability Rebuilt | 1d904385af7cbe0cc23cf052f542ece34edc0c2fbd8899848e3da1807ae48dfb | [Exact restore](CFB_20261124_EVENING_AVAILABILITY_ORDERED_RUN_PROMPT_ROLLBACK.json) | 437e7c78a10d9d507a9e63498f321f5116560809 |
| CFB Weekly Engine QA Rebuilt | 74f1fbe5ba7b8ff7bae6b401e8cca7050b079736347c17fe93ab6885c8c3d503 | [Exact restore](CFB_20261124_WEEKLY_ENGINE_QA_ORDERED_RUN_PROMPT_ROLLBACK.json) | c60f9c13f8dd8d86e31691efe2a71ad01b6bac70 |

- Market Monitor: startup receipt → current selector/profile → immediately attempt fresh CBS → validate/save/read back full tables → due reassessment → guarded publication and integration → owned output and two-phase closure. If checkout blocks, capture still runs. If capture blocks, record the exact attempt, continue independent work and preserve the prior accepted publication.
- Health: startup → current authority → actual Monitor receipts and publication bindings → exact-hash reuse or named required check → due chronology and historical coverage → saved findings and closure. Missing runtime is localized to its check.
- Evening: startup → applicable Monitor and retained source → compare handoff deadlines → availability work → typed handoff or permitted fallback → readback and closure.
- Weekly QA: startup → active selector and applicable Saturday Monitor evidence → named QA, outcomes and analytics obligations → saved QA and closure. Missing dependencies are localized and historical fixtures apply only to their governed checks.
- Common blocked path: record first attempted operation, tool, path or unavailable capability and exact error, owner and next action. Complete independent work. Save/read back the terminal candidate and separate closure when persistence is available; otherwise report the precise persistence boundary.
- Tuesday and Friday 13:00 CT decisions belong in the existing 07:00 CT Monitor slot or an earlier eligible slot. Thursday Evening hands off to Friday 07:00 CT. A 13:00 CT trigger cannot satisfy a 13:00 CT pre-deadline requirement. Elapsed decisions are preserved. Health and Weekly QA check actual clocks.
- Prompt installation and walkthrough verified. Natural scheduled proof is pending. Each next natural invocation needs evidence of its own first owned operation and two-phase closure, including incomplete runs.
