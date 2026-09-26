# CFB Engine — Challenger B Mechanical Feature Diagnostic Review v1.167

Status: NOT ACCEPTED / SUPERSEDED FOR ACCEPTANCE PURPOSES

Run 36209888977 completed successfully and artifact 10895286325 (sha256:392c7ac07e8a3cc0d65f33e622230b05d6fcac62590d7bc1912678674685e7ed) preserved 7,701 target games / 15,402 target team-sides with no 2025 access and no fit/score.

Acceptance is withheld. The producer marks 90 team-sides (45 games) as own-PBP-missing but fills their missing PBP primitives with zero before cumulative history construction. Those synthetic zeros can contaminate later same-team targets instead of failing closed on unavailable source primitives, contrary to frozen v1.159-v1.161 semantics.

The diagnostic also does not provide the required acceptance decomposition by population class, opening/no-prior versus missing-source history, or exact accounting of the 1,342 v1.158 newly admitted games.

No v1.167 feature output is accepted as Challenger-B substrate. Target-ledger preservation remains useful diagnostic evidence only.