# Monday Week10 recovery: verified governed runtime and publication-gate tests

- Original Monday Market Monitor terminal: CFBMM-SCHED5-20261102T190247151Z RUN_INCOMPLETE, local DNS checkout failure. Do not retroactively relabel.
- Verified GitHub-hosted runtime: Actions run 41550787699 SUCCESS; genuine pinned ancestry and review refs, Week10 source census/preflight and failure-classifier regressions PASS.
- First production-gate attempt 41551016698 failed due to test import path, not producer logic. Corrected PYTHONPATH=scripts.
- Second attempt 41551084971 failed because historical publication regression requires full Git ancestry; shallow checkout lacked historical canonical source objects. Corrected actions/checkout fetch-depth: 0; did not weaken gate.
- Final independent Actions job readback: https://github.com/munchie50/cfb-acquisition-bridge/actions/runs/41551152164 COMPLETED SUCCESS. All steps SUCCESS: full checkout, Python/governed files, pinned ancestry and immutable refs, Week10 source census, prospective preflight regression, governed publication/recovery consumer/market qualification/fallback inventory regressions, failure classifier.
- Scope accepted: runtime and regression tests EXECUTED + VERIFIED. No current model produced, no six-market live quote certification, no decision rows authored, no Hot Sheet publication, no terminal Market Monitor RUN_PASS. Historical tests are not current producer execution.
- Blocked production gates: Tuesday Week10 FIRST_FROZEN candidate and independent acceptance; live executable operator/venue/price and material evidence; current decisions; governed publication and readback. The local container DNS fault itself remains unresolved; GitHub-hosted runtime is verified alternative.
- No changes to four task topology, Champion, wagers, or canonical market/Hot Sheet.
