# CFB Engine — Challenger B Feature Producer Extension Contract v1.159

Status: PROSPECTIVELY FROZEN / NO FITTING OR SCORING
Parent: v1.158

## Producer audit
Exact v1.109 and v1.115 producer code was read back.

Important findings:
1. Neither producer intrinsically filters to FBS-vs-FBS. Each filters raw PBP by supplied schedule game IDs. The population defect lives in the schedule wrapper/input, not feature formulas.
2. Both sort team-season rows by start_date and game_id and use lagged cumulative sums, so they are structurally prior-row calculations.
3. v1.109 reads home_points/away_points from schedule to compute prior points-for/against. This is acceptable for historical TRAIN/VALIDATION, but the 2025 holdout cannot receive an outcome-bearing target schedule.
4. Both build team-game rows only from teams appearing in qualified PBP. A target game with no qualified PBP can disappear rather than produce an explicit ineligible target row.
5. Neither explicitly asserts strict prior kickoff. Ordering plus lag is insufficient for the new 2025 leakage-proof standard when timestamps tie or are ambiguous.

## Frozen extension rule
Preserve all accepted feature formulas and play semantics from v1.109/v1.115. Change only population/input/chronology mechanics required for Challenger B.

The extended producer must:
- take v1.157 corrected schedule as target authority;
- acquire PBP for all corrected schedule game IDs;
- preserve exact mechanical/derived formulas;
- construct explicit target team-game rows from schedule membership, then left-join qualified per-game primitives;
- ledger missing target PBP/primitives instead of silently dropping target rows;
- for each target row aggregate only source games with the same team and source kickoff strictly earlier than target kickoff;
- never use same-kickoff or later games;
- fail closed on missing/ambiguous target kickoff;
- preserve no preseason/previous-season prior;
- preserve opening-row NA behavior;
- for 2016-2024 use authoritative schedule outcomes only for historical prior points features;
- for 2025 obtain points-for/against for strictly prior completed games from a quarantined prior-game outcome source keyed by source game, never from target schedule projection;
- assert target game_id is absent from every target row's contributing source-game set;
- assert no 2025 target outcome fields are accessible to prediction-row construction.

## Equivalence gate
Before accepting the extension, rerun it on the old v1.108 2016-2024 schedule and require exact or numerically identical reproduction of accepted v1.109/v1.115 feature outputs on common rows. Any formula drift is a blocker.

Then run corrected 2016-2024 population and audit coverage of the 1,342 newly admitted games. 2025 execution is a separate chronology/leakage gate.

Locks unchanged.
