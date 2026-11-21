# CFB Saturday 13CT manual catch-up — scoped continuation

Status: MANUAL_CATCHUP_IN_PROGRESS / PRODUCTION_RUN_INCOMPLETE / NO_WAGERS.
Source run: scheduled-20261121-1300-ct-turn11; natural scheduler closure RUN_INCOMPLETE.
Authority: original contracts, recovery index v1.295, retained November 20 reconstruction and November 21 run receipts. Do not promote noncanonical preview or renew elapsed cutoffs.

## Fresh-read evidence
- Saturday 13CT frontier: evidence/run_receipts/CFB_MARKET_MONITOR_20261121T190208Z_13CT_FRONTIER_RECONCILIATION_NONCANONICAL.md SHA 978b23cff1ddbd3d2d335107b18801bb6e6b442f.
- Preserved 70-game preview: 68 PASS (not wagers), two closed historical conditionals, zero inconclusive; not accepted. 58 Saturday matchups, 12 original exclusions; 20 saved kickoff windows at or before the afternoon worker start; 38 later windows not automatically eligible because original cutoff authority and named-book offers unverified.
- Existing read-only adapter: scripts/cfb_overlay_publication_probe.py, previous commit b6a37b372e19e2310e9d214f6cb6934ce97bfa82. It now rejects duplicate cycles and non-increasing UTC timestamps in paired packet streams.
- Existing original selector gate requires exact full decision ledger SHA and recovery-index canonical decision pointer; unchanged.
- Existing QA: qa/test_cfb_overlay_preview_binding.py. Newly added regression fixture had double-escaped literal packet framing. Corrected in commit ac6c23bb0c1e315a2acdbc951ebbf1f4ceb0d01a; fresh GitHub readback verified. No tests executed in this turn; do not mark QA PASS.

## Completed in this catch-up
1. Fresh-read actual 13CT reconciliation and latest overlay/QA sources.
2. Detected and corrected malformed newly added QA fixture, read back from GitHub main.
3. Preserved canonical ledgers, selector, Champion, schedules, frozen predictions, wagers, money and historical cutoffs.

## Unfinished, ordered
1. Execute qa/test_cfb_overlay_preview_binding.py with original existing QA and report actual results. Correct any observed regression without weakening gate.
2. Execute actual immutable Week12 manifest-pinned pair reconstruction and original selector integration QA, using verified Git blob inputs and retained lineage; test stale lease/parent/sequence and duplicate/missing/reordered pairs. Distinguish fixtures from real-data validation.
3. Independently qualify only genuinely prospective games against original deadline and timestamped named-book offers. Do not retroactively authorize Saturday games or use historical prices as executable quotes.
4. Governed selector decision: no automatic canonical ledger/recovery pointer promotion from a noncanonical preview. Run original publication gate only after approved state and exact readback.
5. Record final RUN_PASS only if all original production obligations genuinely met; otherwise RUN_INCOMPLETE with precise remaining blockers.

Do not repeat abandoned DNS troubleshooting or already completed CBS 70/70 normalization/compiler. No fifth automation.
