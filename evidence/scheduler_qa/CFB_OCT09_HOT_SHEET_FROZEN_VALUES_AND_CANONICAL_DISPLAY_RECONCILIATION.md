# October 9 Hot Sheet — frozen-value and canonical-display reconciliation

Scope: user-directed Test Routine v6 independent audit and prospective presentation correction. Production Routine v5 and Champion v1.193 unchanged.

## Accepted source recovery
Original accepted FIRST_FROZEN producer run 36216090860 / artifact 10897612260 was directly downloaded. ZIP SHA256 verified 772b8683365ebf62d35fc3813beb138688b84af4172a0b261fd9218691d5adcf. Read only the 2026 prediction/target/exclusion CSVs; no numerical model rerun or protected 2025 TEST access. Frozen date scope October 6–10 America/Chicago yields 58 unique target IDs = 49 prediction IDs + 9 exclusion IDs, disjoint/exhaustive. Nebraska game 401858481 is excluded for away_prior_points_missing.

## Reproducible execution and results
Persisted read-only helper scripts/cfb_hot_sheet_frozen_values_audit.py; independently read-back Git blob b9688257e20a9b6f95b57b8af8711dfdf6caa728, executed source SHA256 480718ffad46d798a87acfad1d7989424d4646d9d20d7a0dc6280cea04e7018d.
Executed invocation: python scripts/cfb_hot_sheet_frozen_values_audit.py --archive <accepted ZIP> --hot-sheet-json <fetch_file structuredContent JSON> --first-date 2026-10-06 --last-date 2026-10-10 --expected-modeled 49.
Parent result retained at evidence/scheduler_qa/CFB_OCT09_1301_HOT_SHEET_FROZEN_VALUE_AUDIT.json, exact read-back blob 516775ada36f551afbe5c7328b9aeaf9f246a19e, JSON SHA256 2cbdc7f51722c79b962632906afec8a297f4b266f410db40234f21565f556aec.
Parent production Hot Sheet blob 0d99c7c2aa1cebbce35e726992c38fa7e6c43083: 49/49 unique one-to-one ordered matchup joins, 147/147 rounded prediction numbers, 49/49 favorite directions, all home-probability labels, source ID union equality PASS. Explicit FIU=Florida International alias; Texas vs Oklahoma preserves ordered sides, no fuzzy matching. Hot Sheet lacks game IDs; exact ordered-name mapping is accepted only after uniqueness and full ID-union proof in this bounded audit.
Additional current-sheet per-row CT kickoff bucket audit: 49/49 membership checks PASS. This validates displayed sectioning, not independent current schedule truth.

## Real display defect and correction
UCF @ Oklahoma State total was rendered 52.5–54.5, while same-cycle canonical market blob bbc222ec291ba1faff3f083f6da132d8e8214cae explicitly retained displayed totals 53.5/54.5. The extra 52.5 was unsupported by that canonical entry. Correction binds display to canonical state; it does not assert the original external source could never have shown another value.
Created prospective corrected view evidence/operational/CFB_WEEK6_HOT_SHEET_2026-10-09_1538CT.md, read-back blob eaeded90f81dd1190e0ef77fc52a448f73ea5dca. Original 13:01 snapshot and its scheduled receipts remain unchanged. Exactly one game row changed (market total display), 48 other rows byte-identical; all frozen values/decisions/kickoffs unchanged. Corrected sheet rerun of the frozen-value helper passed. Underlying quote retrieval stays approximately 13:02 CT, expressly not refreshed at 15:38.
Manual correction cycle CFB_PRESENTATION_QA_20261009T203813Z: STARTED read-back 2d380cae402afb422d114e81ffab63f54f3c5992; terminal candidate 92ab582e212adb938771ad5ea16324381050e912; separate closure a7c2051b2d7fee886310f8145a11788daedad861 ending RUN_PASS, independently read back. This PASS is bounded manual presentation QA, not another successful scheduled Monitor cycle.

## Producer/closure debt
The current correction is persisted/read back and deterministic audit demonstrates values retained. No prompt or scheduled-producer code was changed during this audit. Natural future Hot Sheet producers must still demonstrate canonical quote-display reconciliation; numerical/frozen audit helper is reusable manual tooling, not claimed recurring integration. The helper checks frozen values and identity, not external-source truth, calibrated edges, actionable thresholds, prices or Caesars execution.
Opaque rejection cause, Health and Evening natural demonstration debt remain OPEN. No source capture, new wager, settlement, model/calibration/Champion change or routine promotion.


## Producer-control follow-through
After artifact correction, appended a prospective canonical row-value fidelity guard to the active deterministic Hot Sheet contract already bound to Market Monitor. Exact independent contract readback: 7636214c24ea061f70dc225cbce0cd28b146feb9. Requires frozen-value/identity reconciliation and displayed market tuple/divergence/timestamp fidelity before persistence; unsupported range endpoints fail closed. Existing task prompts/cadences unchanged. This addresses the recreating producer requirement; natural enforcement remains pending and is not certified by manual helper execution.
