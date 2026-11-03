# CFB Market Monitor stage trace
correlation_id: CFBMM-AUTO6-20261103T125825032Z
timestamp_utc: 2026-11-03T12:59:25.335Z
trigger: SCHEDULED_AUTOMATION
startup_blob: 4aba17db89bb512dcc7a56191affa08b6227db88

| stage | outcome | failure_category | fallback_attempted | fallback_result | required_for_this_invocation |
| --- | --- | --- | --- | --- | --- |
| STARTUP_TRACE | PASS independently read back | NONE | false | NOT_NEEDED | true |
| MAIN_TREE_RECOVERY | PASS 2017 entries, not truncated; v1.249 exact SHA 2f7f9d78116a491746b1b7c533990eeec81442cd | NONE | false | NOT_NEEDED | true |
| AUTHORITY_READ | PASS current v1.249 and original 32901-char task backup | NONE | false | NOT_NEEDED | true |
| TUESDAY_CANDIDATE | PASS prior push run 41551746133; 125640761298 job success; candidate artifact 13193176113 | NONE | false | NOT_NEEDED | true |
| ACCEPTED_SOURCE | PASS pointer SHA 7fe8df30d5b75d5ba57e8680d98265ba691f598b; cutoff 2026-11-03T00:17:26.895461Z; independent acceptance evidence blob ce926da923fadd41b4f4b9af75d84d3b82223190 | NONE | false | NOT_NEEDED | true |
| NATURAL_TUESDAY_TRIGGER | WAIT_FOR_SCHEDULED_TRIGGER at pre-09:00 CST observation; earlier candidate push success does not prove natural schedule | NONE | false | NOT_NEEDED | false |
| PROSPECTIVE_QUOTES | INCOMPLETE: two-game FanDuel editorial retrieval-only benchmarks found in current repository, no executable venue/update clock; 12 branches not qualified for production | MISSING_INPUT | false | NOT_NEEDED | true |
| FOOTBALL_MATERIAL | INCOMPLETE: last official MAC report status pending; no new independently verified player report | MISSING_INPUT | false | NOT_NEEDED | true |
| WORKTREE_COMPUTATION | NOT_RUN; no authenticated worktree established for unchanged market gate/decision compiler | MISSING_INPUT | false | NOT_NEEDED | true |
| PUBLICATION | NOT_ATTEMPTED; no current authenticated six-market decisions | PUBLICATION | false | NOT_NEEDED | true |

classifier_execution: NOT_RUN
sanitized_error_excerpt: No connector exception at startup. GitHub workflow-specific /actions/workflows/.../runs endpoint rejected by connector INVALID_ARGUMENT; used supported /actions/runs collection and filtered exact workflow name; not a workflow failure.
next_safe_action: at 09:00 CST verify actual natural Tuesday run/artifact, then qualify both Tuesday games' independently sourced selection/line/paired-price/update clocks and official material, execute unchanged gates in authorized worktree; preserve prior Hot Sheet until accepted publication.
No schedule, model, Champion, wagers, money or canonical market/decision mutation.
