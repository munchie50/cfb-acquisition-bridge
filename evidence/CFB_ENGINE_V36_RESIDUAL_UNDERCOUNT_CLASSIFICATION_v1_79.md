# CFB Engine V36 Residual Undercount Classification — v1.79
Date: 2026-09-25
Status: bounded diagnostic checkpoint; no V37 and no semantic/model/source/gate/production promotion.

## Test-routine action
Continued v5 from v1.78 on the executable RAW_TURNOVER_RATE branch. Audited the preserved V36 artifact directly and classified the 183 conservative-shadow fumbles_lost undercount team-games.

## Residual undercount shape
Conservative shadow undercounts: 183 team-games.
Difference depth:
- replay 0 vs official 1: 112
- replay 0 vs official 2: 14
- replay 0 vs official 3: 1
- replay 1 vs official 2: 37
- replay 1 vs official 3: 5
- replay 2 vs official 3: 8
- replay 2 vs official 5: 1
- replay 3 vs official 4: 5

Thus 127/183 undercount team-games still have zero replay fumble losses, but 56/183 are partial-count misses rather than zero-detection cases.

## Link to V27/V36 zero-vs-one diagnostics
112 of the 183 residual undercount team-games are members of the earlier exact replay=0 / official=1 target population.
Among residual undercount targets, 46 team-games have one or more already-detected raw fumble candidate rows in the V27 candidate diagnostic, but none of those candidate rows were classified as a loss under the frozen loss semantics.

Those 46 target groups are dominated by explicit recovery rows. Candidate play-type/coprocess structure includes:
- Fumble Recovery (Own): 34 coposs false, 1 coposs true
- Fumble Recovery (Opponent): 24 coposs true, 3 coposs false
- plus small punt/kickoff/sack cases.

The sample text demonstrates an important semantic warning: play-type labels such as "Fumble Recovery (Opponent)" cannot be treated as authoritative lost-fumble labels by themselves. Several rows' explicit recovery text resolves to the fumbling team's own side despite that play-type label. Therefore a blanket play_type-based V37 rule would be unsafe.

## Consequence
The residual undercount population is at least two problems:
1. occurrence/count incompleteness (including zero-detection and partial-count misses), and
2. already-detected fumble occurrences whose loss/recovery semantics do not classify as official losses.

Do not collapse these into one broad rule. Next diagnostic should isolate the 46 candidate-bearing residual undercounts and reconcile explicit recovery identity / possession-change contradictions before considering any semantic code change. Separately preserve the candidate-free undercount population for occurrence discovery.

RAW_TURNOVER_RATE remains OPEN.

## Governance
V36 frozen inputs/artifact remain the evidence substrate. v1.78 remains predecessor diagnostic.
Latest integrated Library ZIP remains v1.73; v1.74-v1.79 are bounded repository evidence checkpoints.
Production/master routine v4; active test routine v5.
Production v1 untouched; v2 challenger/shadow; 2025 TEST protected.
Primitive Historical Coverage Gate OPEN. Prediction cutoff UNKNOWN/fail-closed. Second-order lineage evidence boundary preserved.
No fitting/tuning/source/model/production promotion.
