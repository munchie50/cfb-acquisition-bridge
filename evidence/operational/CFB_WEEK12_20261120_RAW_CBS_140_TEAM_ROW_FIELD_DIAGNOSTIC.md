# Week12 overdue Friday 07CT and 13CT — raw CBS 140-team-row market field diagnostic

Status: independent connector-side structural/field-level diagnostic, NOT official Python normalizer PASS, qualified offers or champion v1 publication.

Raw immutable input: evidence/operational/CFB_WEEK12_20261120_MANUAL_FRESH_CBS_SOURCE_RAW_20261120T201925Z.md; blob 01980f097247a4e8a03b6c925bc7faf63997c3a4; captured 2026-11-20T20:19:25.829Z (after 13CT). Governed Python normalizer script blob 35536c3e4988640935e7754be08c3ec464e29215, read separately. Connector-side JS diagnostic reconstructed game header/team rows, extracted CBS columns 3-5 (spread, moneyline, total), removed markdown image/link/html wrappers, validated numeric token formats.

- Exactly 70 game headers, 140 directed team rows, exactly two teams and six cells in every game group; no structural errors.
- Six Friday Nov20 games, 58 Saturday Nov21, six earlier-week elapsed games.
- All nonmissing spread, ML, total field strings match expected basic display format; 0 malformed token formats in this diagnostic.
- Four team moneyline fields unavailable (two games); no spread or total fields missing.
- 28 of 70 games have unequal-and-opposite displayed away/home spread numbers; 25 of 70 have unequal displayed over/under total numbers. These are per-cell mixed-book observations and MUST NOT be merged into a synthetic executable offer. Counts are from fresh raw source, not historical Nov20 07CT snapshot.
- Example Vanderbilt at Florida: away +13.5 -110, home -13.5 -105; over 45.5 -111, under 46.5 -110. Example Wake Forest at Georgia Tech: away -20.5 -108, home +20.5 -108; total 56.5 both sides. No game-specific model recommendation derived.

This is a meaningful step beyond the prior header census: all 420 team-market fields (140 x 3) structurally inspected. NOT verified full official normalize(): original 70-game lineage identity/aliases, clock statuses, exact book icon identity and Python dependencies not executed in authenticated full checkout. No current book-identified offers, champion v1 decision compile, or accepted Hot Sheet. RUN_INCOMPLETE; no frozen line, task, wager or ledger mutation.
