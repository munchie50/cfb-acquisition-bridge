# CFB Engine — Challenger B Corrected PBP Coverage Acceptance v1.165

Status: BOUNDED PASS / 45 SOURCE-MISSING GAMES FAIL CLOSED
Run 36209518532; artifact 10894969326; digest sha256:6cd0be2b3a3abccc0ad46cd97240c9d6d027bde84334cd90372b80488f8d3b57.

Of 7,701 corrected 2016-2024 target games, 7,656 have game IDs present in the cfbfastR PBP source and 45 do not. Missing classification: 39 FBS_VS_FBS, 6 FBS_VS_NONFBS; 44 regular, 1 postseason. Missing by season: 2016=16, 2017=5, 2018=3, 2019=1, 2020=20, 2021-2024=0.

The 45 games remain members of the authoritative population. They are not silently deleted. Their own-game primitives are source-unavailable and must be ledgered/fail closed where a required feature cannot be qualified. This does not prevent them from receiving prior-game features if those prior inputs are independently qualified; target-row construction remains schedule-first.

v1.163 summary class counters are superseded by v1.165. No 2025 access; no fit/score.
