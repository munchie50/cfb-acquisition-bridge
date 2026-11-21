# Market Monitor offline-bundle production routing — November 21, 2026

Status: ACTIVE_TASK_INSTRUCTION_INSTALLED_AND_READBACK; CODE_HELPER_CANDIDATE_NOT_PROMOTED; NATURAL_EXECUTION_NOT_VERIFIED.

Existing production automation: 6ae766e788d881919726d0eeb44450dd, CFB Market Monitor Rebuilt. Updated its prompt to put previously proven offline full-history Git bundle recovery ahead of Firecrawl ZIP, DNS, and Git HTTPS. Readback confirms enabled=true, unchanged daily 07:00 and 13:00 America/Chicago RRULE, and active heading NOV21 PRODUCTION OFFLINE-BUNDLE RECOVERY ROUTE — ACTIVE, GUARDED.

Source evidence:
- evidence/operational/CFB_WEEK12_20261120_MANUAL_MONITOR_RECOVER_EXISTING_BUNDLE_EVIDENCE.md
- evidence/scheduler_qa/CFB_MONITOR_OFFLINE_CHECKOUT_AND_ARTIFACT_READBACK_20261111.md
- evidence/scheduler_qa/CFB_SHELL_BUNDLE_CANARY_20261118T232316Z_RESULT.md
- evidence/scheduler_qa/CFB_VERIFIED_BUNDLE_CHECKOUT_RULE_CANDIDATE_20261118.md

Production gate: authenticate fresh main and expected SHA256; deliver current-main complete bundle to same worker; verify bytes, exact main ref, git bundle verify, local file-only checkout, nonshallow ancestry, immutable retained reviews and governed original validators. Historical fixture bundle cannot substitute for current main. Nov18 helper --bundle patch remains candidate, NOT silently promoted; absent current-main transport must be recorded NOT_EXPOSED and independent source/market work continued. Do not retry abandoned DNS/Git HTTPS, GitHub Actions scheduling, or Firecrawl credit route.

No new code helper, canonical Hot Sheet, Champion, wager, ledger, task count, or schedule mutation. Instruction installation does not constitute SUPPORTED_GIT_RUNTIME_VERIFIED or a completed production run. Next evidence: natural or explicitly user-triggered Monitor run with exact attempted transport and per-stage terminal closure.
