# CFB Engine — Phase 4 Challenger A Dataset Freeze Acceptance and Pre-Fit Reconciliation v1.134

Status: DATASET FREEZE BOUNDED PASS; PRE-FITTING GOVERNANCE RECONCILED; FITTING STILL REQUIRES EXPLICIT AUTHORIZATION
Scope: Challenger A / shadow only
Production v1: untouched champion/fallback
2025 TEST: protected; no performance exposure

## Executed dataset-freeze evidence

Corrected v1.131 workflow run: 36204590513
Head commit: 8a91d03969b1ffc6414ad9acd08bb812a409de1e
Run conclusion: SUCCESS
Artifact ID: 10893287560
Artifact digest: sha256:8f3cf0299ca6322393cf9d0b9e7d42c65f217cb8234197862a713b832d51a2da
Artifact size: 963136 bytes
Artifact expired at acceptance: false
Builder blob: 5505c9c55efec9756586dee741a73ae03de7ce96
Qualified schedule blob: e8d96b9135f625a868cc613e124545ac51828e54

Artifact manifest:
- eligible game rows: 5164
- excluded schedule games: 1234
- numeric predictors: 34
- temporal exclusion games in ledger: 42
- temporal exclusion team-sides represented: 43
- 2025 rows: prohibited by executable assertion; run passed
- duplicate eligible game rows: prohibited by executable assertion; run passed
- NA in eligible predictor matrix: prohibited by executable assertion; run passed
- market-like predictor names: prohibited by executable assertion; run passed
- tied final scores: prohibited by executable assertion; run passed

Eligible rows by season:
2016 625
2017 595
2018 594
2019 595
2020 373
2021 597
2022 556
2023 613
2024 616

Exclusions by season:
2016 94
2017 141
2018 139
2019 139
2020 135
2021 135
2022 178
2023 137
2024 136

File SHA256 values:
- dataset: 17939728b9939e9b2b2f11f02da0b449656c0a01034c954d4e5d0f6655509053
- exclusion ledger: 346c4f0a5acd690195a13d3a8def979de6c97130aa8e6c68a45dabac5e5baaab
- config: fbcca938b75d3c151cd8ad8547c24ddecc6bd86b02030495d65da240a6df63a7

## Independent acceptance audit

The prior green v1.131 execution was not accepted merely because the workflow succeeded. Independent audit identified and corrected two proof-quality defects before this accepted run:
1. venue-state parsing now uses explicit accepted boolean encodings and fails closed on unknown values;
2. temporal exclusion evidence now preserves the exact 43 affected team-sides across 42 unique games, including the two-sided Auburn–Mississippi State game.

The corrected builder was independently read back before execution.

## v1.121 blocker reconciliation

The original v1.121 gate remains historical authority for what had to be decided before fitting. Its blockers have since been prospectively resolved as follows:

1. Historical semantic review -> v1.122 bounded review plus v1.116–v1.120 evidence. CLOSED for Challenger A accepted features.
2. Exact feature/play eligibility -> v1.123. CLOSED.
3. Finishing drives / combined turnover / SOS -> prospectively excluded by v1.123. CLOSED for Challenger A.
4. Special plays / garbage time -> v1.123. CLOSED.
5. Missingness / early season -> v1.123 and v1.126; complete-case, no imputation, no preseason/previous-season prior/shrinkage. CLOSED.
6. Target / population -> v1.124. CLOSED.
7. Temporal qualification -> v1.127, v1.128, v1.129 and executable v1.131 ledger. CLOSED by conservative fail-closed exclusion for Challenger A.
8. Modeling/search/evaluation/calibration -> v1.126. CLOSED prospectively.
9. Game-level predictor representation -> v1.130. CLOSED prospectively.
10. Exact dataset/code/config identity + market-blind/2025 assertions -> corrected v1.131 execution documented above. BOUNDED PASS.

## Remaining gate

No unresolved technical blocker from the v1.121 readiness matrix remains for the first Challenger A fit under the frozen contracts listed above.

This checkpoint DOES NOT authorize fitting. Existing governance still requires explicit fitting authorization before any TRAIN/VALIDATION model performance is exposed.

2025 TEST remains untouched. Production v1 remains champion/fallback. Challenger A remains shadow/challenger only.

## Core-rule demonstration

This cycle demonstrates v1.132/v1.133:
- WAIT -> SWEEP: independent acceptance audit ran while the external workflow was pending.
- CLAIM COMPLETION -> PROVE IT: first green run was not accepted; proof defects were corrected and rerun.
- REPEATED FAILURE -> INVESTIGATE SYSTEM: workflow/persistence failures produced core controls rather than repeated ad hoc patching.
- CHANGE -> RECONSIDER DEPENDENCIES: after corrected dataset success, the routine returned to v1.121 and reconciled the actual remaining gate instead of continuing the stale next-step list.

No fitting or tuning occurred in this checkpoint.
