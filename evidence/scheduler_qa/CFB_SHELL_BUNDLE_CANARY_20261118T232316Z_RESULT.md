# CFB shell bundle canary recheck

- Original scheduled time (UTC) — 2026-11-18T23:20:09Z
- Follow-up execution start (UTC) — 2026-11-18T23:23:16Z
- Shell and Git — `SHELL_STARTED`, Git 2.52.0, `SHELL_PROBE_PASS`
- Source SHA-256 — matched `3a4336f1e63572af4efbfe74867a5a38f36739ab6118e521bce2ee83190449da` before invocation
- Result — `BUNDLE_BYTES_VERIFIED`, `RESULT=BUNDLE_DELIVERY_AND_LOCAL_CHECKOUT_PASS HEAD=243507b45ff27a88287539b500dc5b85aa87d32e SHALLOW=false`, exit 0
- First failed stage and exact error — none
- Sanitized stderr — empty
- Receipt verification — independent readback at the creation commit, with exact content comparison reported after the fetch

The script was available in this follow-up. This result establishes offline checkout and object connectivity for the pinned fixture history in the follow-up invocation.
