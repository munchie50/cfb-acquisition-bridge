# CFB Scheduler Canary V4 — Source Complete

- invocation_id: 20261007T124135170Z
- actual_utc_scrape_start: 2026-10-07T12:42:18.122Z
- actual_utc_scrape_end: 2026-10-07T12:42:23.125Z
- actual_utc_extraction_time: 2026-10-07T12:43:43.871Z
- task_id: 6ac4e807aaac8191b3255fae8ab82577
- test_version: V4
- requested_url: https://www.cbssports.com/college-football/scoreboard/
- returned_url: https://www.cbssports.com/college-football/scoreboard/
- page_title: College Football Scores 2026-27 - CBS Sports
- page_date: UNAVAILABLE
- season_explicitly_present: 2026 Season
- week_explicitly_present: Week 6
- firecrawl_search_id: 01a11662-3cb6-77e7-b603-7206b0e8e4e2
- firecrawl_scrape_id: 01a11662-d68f-7611-b3a7-51092a1869df
- firecrawl_request_id: UNAVAILABLE
- response_is_error: false
- response_error: NONE
- response_status_code: 200
- response_content_type: text/html; charset=UTF-8
- response_success_field: UNAVAILABLE
- nonempty_markdown_returned: true
- markdown_character_count: 73219
- actual_game_identities_extracted: 5
- game_bearing_content: true
- source_content_status: GAME_BEARING_CONTENT_RETURNED
- search_validation_note: SEARCH_COMPLETE recorded false for an exact week-path regex; SCRAPE_PENDING preserved that field and documented that the returned generic CBS college-football scoreboard URL satisfies the requested actual-CBS-scoreboard requirement.

## Diagnostic factual observations

| # | Game identity | Explicit kickoff field | Explicit status field |
|---:|---|---|---|
| 1 | Jacksonville St. at Kennesaw St. | 7:00PM | UNAVAILABLE |
| 2 | New Mexico St. at FIU | 7:30PM | UNAVAILABLE |
| 3 | Missouri St. at W. Kentucky | Thu, 10/08, 7:00PM | UNAVAILABLE |
| 4 | Sam Houston at Liberty | Thu, 10/08, 7:00PM | UNAVAILABLE |
| 5 | South Alabama at Arkansas St. | Thu, 10/08, 7:30PM | UNAVAILABLE |

## Expected versus actual

- expected_actual_cbs_football_scoreboard_url: true
- actual_cbs_football_scoreboard_url: true
- expected_nonempty_game_bearing_content: true
- actual_nonempty_game_bearing_content: true
- expected_independent_exact_readback: true
- actual_independent_exact_readback: VERIFIED_BY_ARTIFACT_FETCH
- operational_market_effect: NONE
- recommendations_or_wagering_evaluation: NONE
