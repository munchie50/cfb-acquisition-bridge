# Saturday 13CT frontier reconciliation — NONCANONICAL / NO WAGERS
observed_utc: 2026-11-21T19:02:08.161Z
correlation_id: scheduled-20261121-1300-ct-turn11
startup_trace: evidence/run_receipts/CFB_MARKET_MONITOR_TRACE_20261121T190208161Z_scheduled-20261121-1300-ct-turn11.md
startup_blob: 9f9bea998c3e2dc18b516fd0e4c75ada0fa225aa
trigger: natural_scheduled
status: RUN_INCOMPLETE
source: fresh authenticated GitHub connector reads of retained authority; NOT a new live market offer
first_failure: GitHub fetch_file evidence/operational/CFB_WEEK12_20261120_MANUAL_PROVISIONAL_RELEASE.md returned HTTP 404 NOT_FOUND; independently verified continuation deep dive and preview remain accessible; do not infer release missing without tree enumeration
verified_existing_frontier: evidence/run_receipts/CFB_WEEK12_20261120_CONTINUATION_FRONTIER_BINDING_DEEP_DIVE.md blob dbf16aa2b616d9dfae7c428b990421783b300311
preview: evidence/operational/CFB_WEEK12_20261120_MANUAL_RENDERED_HOT_SHEET_PREVIEW_NOT_ACCEPTED.md blob 00cb3eac893e34187769b56924e553d52681cb92
preview_state: 70 games; 68 PASS (non-bet decision state); 2 historical closed CONDITIONAL; 0 INCONCLUSIVE; no executable wagers; NOT_ACCEPTED
handoff: evidence/run_receipts/CFB_EVENING_AVAILABILITY_20261121T013041433Z_EVENING_DOWNSTREAM_HANDOFF.md blob c588f7e4307b7ff4f8a7112dd4596e7fefaafeb5
Saturday_denominator: 58 retained; 46 numeric FIRST_FROZEN; 12 original exclusions
saved_kickoff_cohorts: 16 at/before noon CT; 4 at 13CT; 38 later; retained kickoff clocks not current proof
at_13CT: 20/58 saved kickoff windows at or before worker start; no new pregame issuance for those games; remaining 38 have original cutoff authority unverified, so no automatic authorization
historical_same_cutoff: Ohio State @ Nebraska and Maryland @ USC both 07CT; expired, no renewal
material_reassessment: Wisconsin @ Purdue QB change invalidates reliance on retained PASS; Rutgers @ Penn State retains frozen exclusion
existing_compiler: previously completed 70/70 CBS normalization, refresh/compiler and reconstructed ledger pair; NOT rerun; no regression demonstrated
selector_defect: scripts/cfb_hot_sheet_current_decision_binding_gate.py blob 8a6022e3aeea0d5c5fc0e9d455a9b56b4f1eb581 demands full ledger SHA1 binding and canonical index decision pointer; preview/reconstructed overlay not canonical
next_engineering: read-only manifest-pinned overlay adapter with exact parent/sequence/pair and stale lease/missing/reordered/duplicate negative tests; governed selector contract decision required before authority promotion
offer_qualification: BLOCKED; no fresh named-book executable quotes, timestamps or original deadline proof
canonical_publication: BLOCKED; preserve last accepted Nov19 Hot Sheet
analytics: NOT_ATTEMPTED; primary obligations incomplete
no_changes: champion, frozen lineage, original cutoffs, task schedules, canonical ledgers, wagers, money
next_owner: Market Monitor for live eligible cases and verified named-book offers; governed engineering for overlay consumer contract; current selector owner for canonical publication
