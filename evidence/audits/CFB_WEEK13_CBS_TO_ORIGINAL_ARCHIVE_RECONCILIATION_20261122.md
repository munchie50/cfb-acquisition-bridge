# Week13 CBS-to-original archive recovery — actual executed join

Status: QA_ONLY_67_EXACT_DIRECTED_MATCHES / 2_ORIGINAL_MISSING / 2_ARCHIVE_KICKOFF_CONFLICTS / PROFILE_ACTIVATION_HOLD

## Source evidence and execution
- Original original-engine 2026 Challenger B archive: GitHub Actions artifact 10897612260, independently downloaded and verified ZIP SHA-256 **772b8683365ebf62d35fc3813beb138688b84af4172a0b261fd9218691d5adcf** against accepted Week11/12 archive authority. Contains original target ledger 622 rows, 526 frozen fair predictions, 96 exclusions; archive cutoff 2026-09-26T03:47:37.497112Z. This is the actual archived game-ID population, NOT an inferred replacement.
- CBS Week13 raw capture: artifact 14771817242, 3033720 bytes, SHA-256 f2319f9354cc3fd5dac23edd328740fb62fb24e98fd75b20e1dfda38d0a6b695. Original lxml extraction: artifact 14771846354, 69 CBS IDs with two-team directed identities, GitHub Actions 45067085739 PASS.
- Manual original join used archive target ledger, prediction and exclusion CSVs; explicit display-name normalization, directed away/home pair matching; no fabricated IDs. **67/69 unique matches, zero ambiguous**. Among 67: **56 archive predictions, 11 archive exclusions**. Original archive ZIP hash verified independently before join.

## Exact unresolved CBS-only pairs — do not synthesize engine IDs
1. CBS 50052032, NCAAF_20261128_SDGST@WASHST: San Diego State at Washington State — no matching directed game in original September target ledger.
2. CBS 50052033, NCAAF_20261128_TXSTSM@UTAHST: Texas State at Utah State — no matching directed game in original September target ledger.

## Exact archive-date conflicts — do not recycle earlier frozen clock
1. CBS 50052031, NCAAF_20261128_BOISE@COLOST, Boise State at Colorado State matches archived original engine ID **401860911**, but original archive kickoff **2026-11-07T23:00:00Z**, not the Week13 CBS game date.
2. CBS 50052034, NCAAF_20261128_OREGST@FRESNO, Oregon State at Fresno State matches archived original engine ID **401860924**, but original archive kickoff **2026-10-31T04:00:00Z**, not the Week13 CBS game date.

The original archive is genuine and contains prospective Week13 game IDs, but does not by itself establish authentic current kickoff/source-clock qualifications or initial Week13 publication. The 67 identity joins are **QA_ONLY**, including the two date-conflicted pairs; do not count 67 as accepted activation or treat 56 historical predictions as contemporaneously activated Week13 recommendations. Need original source admission, date-conflict resolution, exact game census/2 absent matchups, profile authorization, and governed freeze/publication contract before promotion. No wager, money, Champion, FIRST_FROZEN, canonical index, or scheduled-task mutation.
