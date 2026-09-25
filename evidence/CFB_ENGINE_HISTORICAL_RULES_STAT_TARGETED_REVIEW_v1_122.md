# CFB Engine — Historical Rules/Stat Semantics Targeted Review v1.122

Status: BOUNDED PRIMARY-SOURCE REVIEW — input to v1.116/v1.117/v1.121
Scope: unresolved 2016, 2017, 2020, 2022, 2026 seasons plus previously identified regime boundaries
Production effect: NONE
2025 TEST performance: NOT INSPECTED

## Method

Targeted NCAA-primary-source review only for changes plausibly capable of altering current/future engine raw-event meaning, official statistical credit, play eligibility, possession/scoring, drive/field-position boundaries, pace/opportunity, or population membership. Administrative/recruiting/practice/equipment/replay-process changes are classified NONE unless they change on-field statistical representation.

## Season dispositions

### 2016 — BOUNDED PASS for current initial feature semantics
NCAA's approved 2016 changes located in primary material include expanded targeting replay authority, low-block restrictions, feet-first-slide defenseless-player treatment, tripping foul treatment, and enforcement emphasis for ineligible receivers downfield. These can affect penalties/play outcomes as football events, but the review found no new official statistical-credit regime requiring a version change to the current initial scoring/play-volume/yards/rush-pass/explosiveness/success/drive-start definitions.
Disposition: no identified cross-season statistical-definition normalization required for the current initial feature set. Preserve ordinary rule-environment effects.

### 2017 — BOUNDED PASS for current initial feature semantics
Existing ledger identified kick-block leaping/hurdling foul change. Primary NCAA 2017 material also includes practice/recruiting changes, which do not alter game statistical semantics.
Disposition: the identified on-field foul change is an environment/play-legality rule, not a newly identified statistical-credit formula for current initial features. No special feature rewrite established. Penalty-nullified play handling remains governed by actual source play representation, not a retrospective normalization.

### 2020 — BOUNDED PASS with DISTINCT ENVIRONMENT label
NCAA primary COVID playing-rule waivers found: expanded team areas and restricted coin-toss participation, plus related operational safety changes. These do not alter the current initial feature statistical formulas. The season remains an abnormal football environment because schedule/population/opportunity were materially disrupted by COVID, but that is not itself a reason to exclude/downweight it after seeing performance.
Overtime remains in the separately documented 2019–20 regime.
Disposition: label 2020 as distinct environment; no newly identified COVID statistical-credit rewrite for current initial feature set. Any modeling exclusion/downweighting must be prospectively frozen before performance.

### 2022 — BOUNDED PASS for current initial feature semantics
NCAA primary 2022 football proposals/changes located include targeting carryover appeal, blocking-below-waist restrictions, fake-slide treatment, defensive-holding first-down treatment, and related safety/administration changes.
Disposition: these are on-field rule/environment changes but no identified new official statistical-credit regime requiring versioned formulas for the current initial feature set. Preserve the real environment rather than normalize it away.

### 2026 — LIVE SHADOW METADATA / no historical backfill
NCAA 2026 Division I targeting penalty structure changed on a one-year trial basis: first targeting disqualification no longer automatically carries a next-game first-half absence; repeat offenses escalate. 2026 governance also contains prospective 2027 calendar proposals/changes, not historical TRAIN/VALIDATION semantics.
Disposition: 2026 is LIVE SHADOW context only. No backfill into 2016–2024. Current rule changes are metadata for prospective evaluation and do not alter frozen historical feature values.

## Previously identified regime boundaries retained

- 2018 free-kick fair-catch/touchback rule: ENVIRONMENT + field-position opportunity regime. v1.120 proves drive-start chronology/measurement mechanics; the real distribution shift must remain, not be normalized away.
- 2019–20 overtime regime: SEMANTIC + ENVIRONMENT boundary retained.
- 2021+ third-and-later OT two-point conversions: conversion attempts, not scrimmage plays. v1.119/v1.120 found no systemic contamination in current scrimmage classifier.
- 2023 Division I first-down clock regime: ENVIRONMENT shift affecting pace/play volume; preserve.
- 2024 two-minute timeout/timing synchronization: ENVIRONMENT shift affecting pace/end-half opportunity; preserve.
- 2025: metadata only; TEST performance sealed.

## Gate disposition

For the CURRENT ACCEPTED initial/derived feature semantics, the targeted unresolved-season review is now BOUNDED PASS.

The historical-rules gate does NOT certify every conceivable future feature. A later feature touching kick returns, penalties, targeting/player availability, detailed overtime scoring, or other rule-sensitive domains must re-run applicability against the ledger.

Remaining pre-fitting historical-semantic work is narrowed to:
1. encode/document the known regime labels in the first-fit dataset/config where relevant (2018 field-position environment, 2019–20 OT, 2020 distinct environment, 2021+ OT, 2023/2024 timing);
2. verify first-challenger special-play eligibility contract (kneels/spikes/OT) against the exact feature set;
3. do not use these regime labels to choose exclusions/downweights after observing validation performance.

This checkpoint does not authorize fitting.
