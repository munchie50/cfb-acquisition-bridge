# CFB Engine — Challenger B 2026 First Live-Shadow Exclusion Accounting v1.215

Status: **PASS — ALL 96 FIRST-FREEZE EXCLUSIONS EXACTLY RECONCILED**
Parent authority: v1.208 first live-shadow freeze.
Supporting diagnostics: v1.209/v1.210, v1.211/v1.212, v1.213, v1.214.

Canonical census:
- run **36216535514**
- head **05d664bdb80d65ce02f3cc180413244a03333bda**
- artifact **10898090923**
- digest `sha256:b0325bd5e53f26fb341e0219acbad7214a0038123589dc0f36b379186f31739f`
- excluded targets: **96**
- ineligible team-sides: **102**
- predictions changed: false

## Side-level causes
- `prior_points_missing`: **58 team-sides / 56 targets**
- `prior_pbp_missing`: **33 team-sides / 33 targets**
- `opening_no_prior`: **11 team-sides / 11 targets**

There is no `no_prior_history` ledger reason; v1.213 confirmed zero such rows. Earlier informal references to that phrase are superseded by this exact census.

## Exact target-level combinations
- prior_points_missing only: **52**
- prior_pbp_missing only: **30**
- opening_no_prior only: **10**
- prior_pbp_missing + prior_points_missing: **3**
- opening_no_prior + prior_points_missing: **1**
Total: **96**.

## Provenance of the two dominant causes
v1.209/v1.210 proved all 58 missing-points team-side dependencies trace to **4 prior games that were not completed at the frozen cutoff**. This is expected fail-closed temporal behavior.

v1.211/v1.212 proved all 33 missing-PBP dependencies trace exclusively to completed games **401862779** and **401869941**, exactly the two PBP gaps already frozen by v1.204. No additional hidden PBP gap was found.

## Disposition
The first-freeze exclusion accounting is closed. No evidence presently requires reopening or regenerating v1.208. The 526 accepted predictions and 96 exclusions remain immutable first-frozen prospective evidence.

Any later source snapshot/prediction must be a new prospective lineage for targets still future at its own cutoff and may not overwrite this first freeze.

No model, fit, calibration, threshold, market rule, population rule, or production champion status changed.
