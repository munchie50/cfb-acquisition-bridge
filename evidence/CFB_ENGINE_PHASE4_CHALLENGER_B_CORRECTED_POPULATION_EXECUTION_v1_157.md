# CFB Engine — Challenger B Corrected Population Execution v1.157

Status: BOUNDED PASS / POPULATION MEMBERSHIP AND REQUIRED INCLUSION CLASSES PROVED
Run: 36208254662
Head: aad54a42e59e03d6679c023c40377a706a21ad79
Artifact: 10893997859
Artifact digest: sha256:e6d8b794dda56535fcabe4c479444c600325fedb00e0186afe0a031f7a74263a
No model fit or scoring. 2025 outcomes not scored.

## Inputs and authority
v1.153 population source/membership contract; v1.154 exact recovered CBS membership authority 2017-2025; v1.155 prospective same-provider 2016 membership resolution; v1.156 legacy-ledger integrity reconciliation; current SportsDataverse/cfbfastR schedule parquet source lineage with raw SHA recorded per season.

Membership counts asserted exactly:
2016 128; 2017 130; 2018 130; 2019 130; 2020 130; 2021 130; 2022 131; 2023 133; 2024 134; 2025 136.

## Corrected qualified population
Per season qualified relevant-FBS games:
2016 873 = 760 FBS-FBS + 113 FBS-nonFBS
2017 874 = 776 + 98
2018 884 = 772 + 112
2019 888 = 774 + 114
2020 570 = 534 + 36
2021 887 = 770 + 117
2022 896 = 776 + 120
2023 910 = 792 + 118
2024 919 = 798 + 121
2025 934 = 808 + 126

Postseason rows are present for every season:
2016 41; 2017 40; 2018 39; 2019 40; 2020 28; 2021 38; 2022 42; 2023 42; 2024 46; 2025 46.

Thus the v1.124 classes previously missing from Challenger A are now actually represented: FBS-vs-nonFBS and postseason.

## Legacy reconciliation
Independent exact-ID reconciliation against the recovered v0.22 2017-2025 pre-scope FBS-vs-FBS ledger proves that the current corrected population retains the entire old regular FBS-vs-FBS universe exactly:
2017 736/736 exact IDs; 2018 733/733; 2019 734/734; 2020 508/508; 2021 732/732; 2022 734/734; 2023 750/750; 2024 752/752; 2025 762/762.
No old regular FBS-vs-FBS IDs were removed and no new regular FBS-vs-FBS IDs appeared.

For 2016, corrected source counts reconcile to the old 719 FBS-vs-FBS regular universe plus 41 postseason FBS-FBS games, while adding qualified FBS-vs-nonFBS games under corrected v1.124 semantics.

## Conference-championship classification boundary
The current schedule source includes conference championship games. Explicit notes-based championship labeling is available for 2022-2025 (10,10,9,9 respectively). Earlier conference championship games remain included in the regular-season source population but are not separately labeled by the source metadata used here.

Population inclusion PASS is not blocked because those games are present. A claim of complete historical conference-championship subclass labeling before 2022 is NOT made. Subclass labeling is diagnostic metadata and must not be invented from performance.

## 2025 isolation
The persisted 2025 projection contains only season, game_id, start_date, home_team, away_team, neutral_site, population_class, competition_class.
It contains no score/points/winner/market/postgame fields.
Projection SHA-256: 289b72810b0c1ebcf0426b9b869d37f46601c40f9f2028d58e79bfa96616ee34.
No 2025 outcome scoring occurred.

## Dependency consequence
Population construction blocker is CLOSED for Challenger B.
Next gate is feature-substrate availability/conformance across newly admitted FBS-vs-nonFBS and postseason rows, plus chronology-safe 2025 feature construction. Do not assume accepted Challenger-A feature artifacts cover newly admitted games.

Locks: no fitting; no scoring; no market join; no production promotion.
