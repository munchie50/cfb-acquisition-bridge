# CBS capture handoff deployment and verification

November 23, 2026. Result: DEPLOYED / MANUAL CAPTURE AND COMPILER VERIFIED / NATURAL PRODUCER PROOF PENDING.

Compiler commit d7ffb4b7acdcf31d8914f563587b312ff1217767 verifies exact retained UTF-8 bytes. Shared procedure commit 120dfaf7bf92144a004b28ab1991c229a8031087. Independently read back both files on main and all four live task prompts: Market Monitor Rebuilt, Engine Health Rebuilt, Evening Availability Rebuilt, Weekly Engine QA Rebuilt. Schedules, enabled state, titles and task identities matched.

Exact verified 07:58 CT parent replay reproduced canonical market and decision blobs and independently verified v1.297 selector and selected sheet. Missing capture, wrong blob, stale capture and a correctly hashed research-only file each failed the source gate.

Fresh CBS tables recovered by 19:09:48Z, normalized against accepted lineage (69 directed games), retained at evidence/operational/CFB_WEEK13_CBS_FBS_TABLES_20261123T190948Z.md in d80d27635cdba9303f51e6cc6e303720da92b97f. Independent full-content equality and Git blob 92af482686985fb574f5ac76685b741be8ff749e matched. Actual canonical parent blobs were independently recomputed. Fresh append-only compiler verification executed at 19:10:24.302915Z with retained prior decisions as a controlled input. Candidate market 7b461ec79b885719e7d5ba59538ab9c211efcca1 and decision 26f43fc2398c946d4bf32e664d54bdf1327c04ef passed replay. The candidate did not represent freshly earned decision deltas and was not promoted. No canonical ledger, current selector, or financial changes.

Next natural proof: Nov. 23 16:30 CT Health verifies existing accepted bindings. Nov. 24 07:00 CT Market Monitor must produce its own fresh capture, exact independent blob readback and earned decisions, then compiler result, saved publication and selector readback, or record the first attempted operation and exact blocker. The manual capture does not satisfy the next run's freshness requirement.
