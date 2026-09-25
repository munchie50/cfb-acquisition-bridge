# CFB Engine Phase 4 Derived Feature Canary Acceptance v1.120

Status: BOUNDED PASS — CHALLENGER/SHADOW ONLY  
Production effect: NONE  
Model fitting/tuning: NOT AUTHORIZED  
2025 TEST: EXCLUDED / UNTOUCHED

## Authority and scope

This checkpoint accepts only the three prospectively frozen derived-feature domains implemented by v1.115 under v1.112:
- offensive/defensive explosive-play rate,
- offensive success rate / defensive success rate allowed,
- average offensive starting yards-to-goal.

It does not accept finishing drives, combined turnover rate, opponent adjustment/SOS, prediction-cutoff substitution, model fitting, weighting, or production promotion.

## Executed canary

Corrected v1.115 run: 36200520092  
Head SHA: 213b3dfc53d488b485e3b1f081456de67b3a3238  
Artifact ID: 10891634424  
Published artifact digest: sha256:2b1531b5f7f70b54c9a32b7130316c37c903b097379a75c45b9f4b8711a7b852  
Independent downloaded ZIP SHA-256: 2b1531b5f7f70b54c9a32b7130316c37c903b097379a75c45b9f4b8711a7b852

Structural audit:
- 12,718 feature rows and 12,718 primitive rows.
- zero duplicate team-game keys.
- zero 2025 rows.
- 1,173 season-team groups; every first row resets to qualified_prior_games=0.
- zero negative denominators.
- zero-denominator features remain NA; no positive denominator unexpectedly yields NA.

## Independent reproduction — v1.118

Diagnostic run: 36201419265  
Head SHA: deb546e81685757e093ccabc5d14aae5cfc13e33  
Artifact ID: 10892122075  
Artifact digest: sha256:f97a7b45a54f156cd854f38775a72238f40c86da56c49426bb2e0746e0e94fab

35 independently recomputed target rows spanning 2016–2024 and prior-history depths 1, 5, 8, and 12 where available were joined directly to the v1.115 artifact.

Results:
- 0 unmatched sample rows.
- 0 mismatches: offensive explosive rate.
- 0 mismatches: defensive explosive rate.
- 0 mismatches: offensive success rate.
- 0 mismatches: defensive success rate allowed.
- 0 mismatches: average starting yards-to-goal.
- 0 mismatches across explosive, success, and field-position denominators.

## Field-position chronology

v1.118 compared raw source-row ordering with numeric id_play ordering for every comparable valid drive start in the 2016–2024 qualified population.

Result:
- 166,398 audited/comparable drives.
- 0 different selected starting plays.
- 0 different starting yards-to-goal values.

Disposition: chronology concern CLOSED for this canary population. Raw source-row ordering and id_play ordering are empirically equivalent for the audited drive-start selection.

## Overtime semantic compatibility — v1.119

Detailed diagnostic run: 36201576884  
Head SHA: d092111ea6c8a55d08378a1446f9d5df97277814  
Artifact ID: 10891664216  
Artifact digest: sha256:c8acbe5db1546344eedfd6ea17a3b2265c96893eb732dd7e7a84985ecd1e8074

The v1.118 broad two-point text heuristic initially surfaced overtime rows that were also classified as scrimmage. v1.119 inspected the exact records.

Finding:
- Explicit 2021+ third-and-later-OT Two Point Pass / Two Point Rush records generally have rush/pass/pass_attempt flags off and therefore are NOT admitted by the current scrimmage classifier.
- Many heuristic overlaps were legitimate preceding overtime touchdown scrimmage plays whose source description also appended the subsequent two-point conversion text.
- Irregular/uncategorized conversion records observed in the bounded audit likewise were not admitted solely because conversion language appeared in text.

Disposition:
- No evidence of a systemic 2021+ third-and-later-OT conversion contamination defect in the v1.115 scrimmage denominator.
- Small irregular source-record edge population remains part of the broader historical rules/statistical-semantics gate; this does not reopen the proved v1.115 mechanics absent new contradictory evidence.
- 2019–2020 versus 2021+ OT regime remains documented as a historical semantic/environment boundary for pre-fitting compatibility review.

## Acceptance

BOUNDED PASS for the v1.115 implementation of:
1. explosive-play rates,
2. success rates,
3. average starting field position,

within the frozen 2016–2024 TRAIN/VALIDATION qualified population and v1.112 definitions.

This checkpoint does not authorize model fitting. The historical rules/statistical-semantics gate remains PARTIAL and blocks fitting. Remaining pre-fitting work must be selected through the authoritative dependency/routine process, not by reopening this accepted canary without new evidence.
