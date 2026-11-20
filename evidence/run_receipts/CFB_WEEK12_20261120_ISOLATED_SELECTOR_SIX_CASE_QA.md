# CFB Nov20 — isolated publication selector six-case QA

**STATUS: SIX ISOLATED TESTS PASS EXPECTATIONS; REPLICA TEST ONLY, NOT ORIGINAL-MODULE OR PRODUCTION ACCEPTANCE.**

Recovered latest main `5a804f92ac20f059d20bdb21172caf8207b46745`, original selector/navigation source, and previous exact pointer drift audit. In local Python runtime, constructed a QA-only reproduction of `cfb_hot_sheet_current_decision_binding_gate.py` selector and audit logic with a **simplified** navigation reader, synthetic ledger, schema-shaped checkpoint and content-addressed Hot Sheet candidate. No actual Week12 ledger was used in this six-case test. This is useful feasibility isolation, **not a substitute for executing original checked-in modules**.

Six expected outcomes: (1) consistent candidate ledger/sheet/pointers PASS; (2) stale decision pointer REJECT; (3) incorrect sheet blob REJECT; (4) provisional release filename REJECT; (5) duplicate CURRENT_HOT_SHEET pointers REJECT; (6) altered decision declaration REJECT (the candidate's sheet digest check rejects first, consistent with validator order). All six test assertions passed.

**Interpretation:** the current selector is not intrinsically incompatible with a virtual reconstructed ledger; it demands the canonical navigation decision pointer, a schema-compatible canonical Hot Sheet path, matching sheet bytes, and the same decision blob. The existing November19 navigation pointers and November20 provisional release fail that contract. The correct next test is original module + original navigation reader + real reconstructed ledger and a QA-only synthetic index candidate, without changing production. Must separately address governance and manifest lineage before promotion.

**Already complete:** Friday 07CT/13CT manual source/decision recovery, 70-game preview, provisional release, reconstructed decision Git SHA verified independently, equivalent real-data five-case check, exact index drift audit. Do not repeat. Original production runs RUN_INCOMPLETE; no wagers authorized. Four tasks unchanged.

No canonical ledger/index/Champion/scheduler/betting mutation performed.
