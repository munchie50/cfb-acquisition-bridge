# CFB production scheduled-task deep dive — November 20, 2026

**Status: VERIFIED_DISPATCH / FAILED_PRODUCER_CHECKOUT / NO_PUBLICATION / FOUR_TASKS_PRESERVED**

## Task observations (recorded task outcomes)
| Task | Last run UTC | Outcome | Next scheduled CT |
|---|---|---|---|
| Market Monitor | 2026-11-20 18:59 | RUN_INCOMPLETE; Git HTTPS DNS failure | Sat Nov21 07:00 |
| Engine Health | 2026-11-19 22:31 | RUN_INCOMPLETE; independent integrity checks succeeded | Fri Nov20 16:30 |
| Weekly QA | 2026-11-15 14:59 | RUN_INCOMPLETE; Week11 outcomes/settlement incomplete | Sat Nov21 09:00 |
| Evening Availability | 2026-11-20 01:28 | RUN_INCOMPLETE; Git HTTPS DNS failure | Fri Nov20 19:30 |

## Verified boundaries
- Friday 13CT Market Monitor recorded_status=completed is **scheduler execution completion**, not engine RUN_PASS. Its own result and persisted closure state RUN_INCOMPLETE.
- Scheduled worker created and read back RUN_STARTED. Direct shell, Python and Git passed; GitHub connector access passed. Bounded git ls-remote failed: `Could not resolve host: github.com`. Combined connector-shell route was not exposed.
- Friday 07CT Market Monitor independently failed at same Git HTTPS DNS boundary. Two distinct natural executions therefore reproduced the blocker.
- The terminal candidate and separate closure of both Nov20 Monitor runs were persisted/read back. Canonical selected Hot Sheet remained Nov19; no new production wager approval.
- The task prompts require the exact-byte checkout helper and pinned full Git ancestry. A GitHub connector read or raw-file reconstruction is **not** a compliant substitute. A shell script cannot fix missing DNS merely by being embedded in the prompt.
- All four task definitions enabled; no task mutation performed.

## Root cause analysis
- **Demonstrated failure:** worker direct Git HTTPS DNS lookup of github.com. This occurs after scheduler dispatch and after direct-shell capability, before authenticated checkout.
- **Not demonstrated:** whether DNS failure originates in worker resolver, egress policy, proxy handling, or transient platform infrastructure. Do not claim one root cause without direct network diagnostics from same worker.
- **Independent alternative:** GitHub Actions hosted runners can check out and execute repo Python outside the failing ChatGPT worker; existing read-only workflow `.github/workflows/cfb_producer_runtime_smoke_manual.yml` proves a designed diagnostic path but DOES NOT run current Week12 publication and is not a verified workaround until an actual run completes.
- **Critical design gap:** production task requires worker-local full checkout even though GitHub connector REST can read/write artifacts. The failure gate is a single point of failure across Monitor/Evening and code-dependent Health/QA checks.

## Smallest next tests (no false pass)
1. In the next natural worker, run one bounded `git ls-remote` and record sanitized resolver/host result, proxy presence boolean, DNS/HTTPS stage, and whether connector REST works; do not log secrets.
2. Separately trigger existing read-only GitHub Actions smoke via GitHub UI (Actions > CFB producer runtime smoke > Run workflow) if permitted; inspect job steps/logs for actual pinned checkout and tests. Do not confuse this with production run or mutate workflows blindly.
3. If GitHub Actions checkout passes while worker Git HTTPS fails, isolate environment-specific networking. Then design a governed transfer of immutable typed results or a dedicated repository runner path, requiring explicit acceptance before production substitution.
4. If worker DNS recovers, continue same invocation into pinned checkout, fresh source, current reviews, Week12 compiler and independent publication readback. Do not stop at probe PASS.
5. Continue independent manual review/lineage audit while runtime blocked, but never declare manual preflight to be compiler acceptance or Friday 13CT deadline met.

## Immediate operational status
- Saturday full game identity reconciliation and prior-decision crosswalk exist as manual audits; no fresh qualified venue offers or accepted Hot Sheet publication.
- Existing production schedule and selected Hot Sheet unchanged. Run remains RUN_INCOMPLETE.
