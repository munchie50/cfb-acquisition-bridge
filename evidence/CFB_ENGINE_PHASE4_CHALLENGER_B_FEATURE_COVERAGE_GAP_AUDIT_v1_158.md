# CFB Engine — Challenger B Feature Coverage Gap Audit v1.158

Status: EXACT COVERAGE GAP PROVED / PRODUCER EXTENSION REQUIRED
Parent: v1.157
No fitting or scoring.

## Exact artifact comparison
Accepted v1.109 mechanical and v1.115 derived feature artifacts were downloaded from their original workflow artifacts and compared by exact game_id to the v1.157 corrected schedule.

Both accepted feature artifacts cover exactly the same game-ID subset. Corrected population coverage:
2016 706/873, missing 167
2017 732/874, missing 142
2018 731/884, missing 153
2019 733/888, missing 155
2020 489/570, missing 81
2021 732/887, missing 155
2022 734/896, missing 162
2023 750/910, missing 160
2024 752/919, missing 167

Total corrected 2016-2024 games: 7,701.
Existing accepted feature-substrate game coverage: 6,359.
Missing corrected-population games: 1,342.

## Missing-class decomposition
The gap is structural, not random.

FBS-vs-nonFBS missing by season:
2016 113; 2017 98; 2018 112; 2019 114; 2020 36; 2021 117; 2022 120; 2023 118; 2024 121.

Postseason missing by season:
2016 41; 2017 40; 2018 39; 2019 40; 2020 28; 2021 38; 2022 42; 2023 42; 2024 46.

Additional missing FBS-vs-FBS regular games are the legacy scope/classification differences already bounded by population recovery; exact IDs must be reconciled by the extended producer rather than inferred.

## Consequence
Accepted v1.109/v1.115 artifacts cannot serve as Challenger-B feature substrate. They remain valid Challenger-A legacy-scope evidence.

A new producer execution must preserve the frozen v1.109/v1.115 feature definitions while expanding raw PBP ingestion to the corrected relevant-FBS schedule.

The producer must prove:
1. target-game identity comes from v1.157 schedule, not old primitive universe;
2. only games with available/qualified PBP contribute;
3. same-season cumulative features use strictly prior games;
4. newly admitted FBS-vs-nonFBS and postseason games are not silently dropped by old FBS-vs-FBS filters;
5. 2025 target rows use strictly earlier 2025 games only and never target/later PBP;
6. missing PBP/input qualification fails closed and is ledgered;
7. feature definitions remain byte/logic-equivalent to accepted v1.109/v1.115 semantics except for population/input wrapper changes.

## Next
Audit the exact v1.109/v1.115 producer code for population filters and chronology mechanics, then implement the smallest corrected-population wrapper/extension. Do not redesign features.

Locks unchanged: no fitting, no scoring, 2025 protected.
