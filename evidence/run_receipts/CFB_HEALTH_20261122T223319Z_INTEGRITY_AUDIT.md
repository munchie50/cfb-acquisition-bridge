# CFB Health Nov22 bounded integrity audit
scheduled_for: 2026-11-22T22:30:00Z
startup_receipt: evidence/run_receipts/CFB_HEALTH_20261122T223319Z_RUN_STARTED.md
startup_blob: 7a16691ec1a8dc37b40b75d3f1cd4dcd02015efa
status: RUN_INCOMPLETE
## Exact-byte Git blob recomputation (authenticated fetch_blob; independent SHA1 over Git blob framing)
- CFB_MARKET_MONITOR_STATE.md: 6815732 UTF8 bytes, SHA 21e2172c709dcf482c4750a7490b82aacac05949 PASS
- CFB_DECISION_WAIT_LEDGER.md: 3605925 bytes, SHA 6862be6a1bd88a3290b1e90a49c33a7a87e92559 PASS
- CFB_EXECUTION_LEDGER.md: 56801 bytes, SHA 4ffc6866b629b2350dc782288426f4ba0a32988d PASS
- CFB_POSTGAME_FIRST_FROZEN_SCORECARD.md: 90544 bytes, SHA 8e158d780b29f529cc029daf9383c19a68819157 PASS
Transport note: fetch_file returned empty for large market and decision; exact fetch_blob recovered complete bytes. These PASS results are byte integrity only; full semantic and latest-tree-pinned checks remain BLOCKED.
## Findings and carry-forward
- Recovery index: newest accepted version and nontruncated fresh tree NOT VERIFIED. Guess of evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1.295.md returned NOT_FOUND. Do not advance index authority or coverage.
- Week12 user-authorized provisional display pointer: verified path blob 359357d1b42074ff09eb11245aa4cc492e7457a8, explicitly 70 games, 68 PASS decisions and 2 historical closed conditional; no actionable wagers, no canonical RUN_PASS. Display exists; do not misclassify as missing.
- Friday Evening handoff: exact blob c588f7e4307b7ff4f8a7112dd4596e7fefaafeb5 read, NONCANONICAL/INCOMPLETE. Do not upgrade its three researched games to four.
- Saturday 13CT manual catch-up continuation blob 8cd30e36765c7056b5296a01d6c984f955084dae: natural run incomplete; no verified current wagers.
- Nov20 runtime differential blob 22f09463c49658abfa3d74589822b148da77dfc4 read; historical early-start variance is not a runtime defect.
- Analytics v1 contract blob cd81e90e4691b1856bf88f08c506972bc0311ac1 read. Certified point-in-time input, latest exact-code Python execution and output readback NOT VERIFIED; Weekly QA owns certification, not automatic Health PASS.
- Historical due-vs-receipt denominators, current Monitor natural Nov22 07/13 receipts, complete predecessor acknowledgments, original Ohio State @ Nebraska and Maryland @ USC cutoff authority, exact latest current selector and full semantic invariants remain UNVERIFIED. No historical timestamp extension or retroactive PASS.
- Preserve unresolved historical cycle identities and no advanced audit watermark. Market Monitor owns current/future market and canonical Hot Sheet; Weekly QA owns analytics certification. Health owns next inspection.
- No Champion, wager, ledger, canonical selector, task, schedule or Big Nine mutation.
## Closure
Health inspection incomplete: exact byte integrity 4/4 canonical surfaces verified, but current mandatory recovery-index/tree, semantic, slot census and terminal readback obligations not all verified. This audit is not a terminal candidate or closure.
