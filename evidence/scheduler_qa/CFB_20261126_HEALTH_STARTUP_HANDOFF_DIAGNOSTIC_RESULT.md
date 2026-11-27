# Nov. 26 Health startup handoff diagnostic result

Original scheduled run `ad0dc8d8-3138-8330-869e-1d4563d9f503`, slot 22:30Z. Scheduler result identity matches; started 22:31:29.664938Z and ended 22:31:42.271551Z. It reported authenticated main read PASS and startup write NOT_ATTEMPTED. At authenticated pin 326357195a287cc3089b1dadabbbddfbe0a18bab the expected startup, terminal candidate and closure all returned NOT_FOUND. Last verified stage from run record: authenticated main read. First unverified boundary: receipt target check/startup write; the write was expressly not attempted. No same-run verified closure. Nov. 25 startup blob 059231c9d7e2e0f1791ab223b16ff35a4aa45cb9 demonstrates that the previous natural slot crossed this boundary.

Current live prompt hash ac47faf6b19659142928138131395214e1f56df1e9795a0d6e8d32499b5febc7; authenticated read, guarded receipt creation and independent readback are already required. Rollback blob 384b0842f4c2e9a386d58151818efd742194f4d8 independently checked against its stored prompt SHA-256, exact restore target and revision. Live prompt readback does not expose the original invocation prompt snapshot. No dispatch or termination trace endpoint was available for this run. No outage, timeout, GitHub write rejection or other root cause is verified.

Isolated manual proof: evidence/scheduler_qa/CFB_HEALTH_MANUAL_STARTUP_DIAGNOSTIC_20261127002718886_ad0dc8d8.md at b9bbb651c46127da782ac2ea58b433448bad9f1c, Git blob 72ee90bbc9b24a6a47b4fde479354a878be47710. One orchestration call executed this sequence:

```json
[
  {
    "at": "2026-11-27T00:27:18.886Z",
    "operation": "github_fetch_commit(main)",
    "result": "326357195a287cc3089b1dadabbbddfbe0a18bab"
  },
  {
    "at": "2026-11-27T00:27:19.128Z",
    "operation": "github_fetch_file(unique path at pinned main)",
    "result": "GitHub API error 404: {\"message\":\"Not Found\",\"documentation_url\":\"https://docs.github.com/rest/repos/contents#get-repository-content\",\"status\":\"404\"}"
  },
  {
    "at": "2026-11-27T00:27:19.497Z",
    "operation": "pre-write main recheck",
    "result": "326357195a287cc3089b1dadabbbddfbe0a18bab"
  },
  {
    "at": "2026-11-27T00:27:21.054Z",
    "operation": "github_create_file",
    "result": "b9bbb651c46127da782ac2ea58b433448bad9f1c"
  },
  {
    "at": "2026-11-27T00:27:21.332Z",
    "operation": "github_fetch_file(exact path at write commit)",
    "result": {
      "blob": "72ee90bbc9b24a6a47b4fde479354a878be47710",
      "exact_bytes": true
    }
  }
]
```

The 404 was the expected absence check. Exact GitHub write/readback worked in Work Mode; no handoff defect reproduced there. Four production tasks are enabled and all existing canaries are paused; none supplied a natural Health worker test for this slot. No live-prompt or checkpoint instrumentation edits were made under the reproducible-defect condition. The manual receipt does not close or change the original run.

Next natural Health slot: 2026-11-27T16:30:00-06:00 CT. Acceptance requires an exact-slot verified startup, both Monitor-slot reconciliations, saved Health findings and independently verified separate closure, or an incomplete closure recording the specific blocker. Scheduled proof is pending.
