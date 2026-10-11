# TestRoutinev6 authorized recovery quarantine STARTED

Run: CFB_RECOVERY_QUARANTINE_QA_20261011T190729Z
Actual prospective boundary: 2026-10-11T19:07:29Z
State: RUN_STARTED
User direction: Continue work using test routine following explicit request to mark ONLY the two malformed QA checkpoints rejected while preserving full contents/history, append valid checkpoint and independently rerun QA.
Target: evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_245.md, freshly recovered b17daac4fd71a10178c0a555552f256703189dfb.
Exact targets: active tagged records21 and22, both19:02:07Z; record21 contains two invalid scripts/ pointers, record22 repeated prior checkpoint clock. Change only their opening fence classification to cfb-frontier-json-rejected; preserve their JSON verbatim, all other prior bytes, original immutable Git history and failed/incomplete receipts.
Strict reader b6901d80f3535ee8e218755dda830ef13d3c2869 remains unchanged. No source/model/market/decision/execution/outcome/money/task/schedule change. Productionv5 retained, v6 candidate.
