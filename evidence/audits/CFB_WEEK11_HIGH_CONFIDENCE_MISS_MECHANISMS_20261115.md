# Week 11 high-confidence miss diagnosis — first two games

Cohort fixed by the two highest-confidence wrong winner picks in the [frozen triage](CFB_WEEK11_FROZEN_MODEL_MISS_TRIAGE_20261115.json), blob `3462a0388ee573931700b647ab4e8f180cadd9a4`. Selection is diagnostic and outcome-conditioned. Both were saved PASS. Official game mechanisms are observations; hypotheses about original model inputs or weighting remain unproved.

| Game | Frozen call | Actual | Home margin error |
|---|---|---|---:|
| Stanford at Virginia Tech (401858299) | Virginia Tech by 26.14, 92.6% home win | Stanford 40–22 | −44.14 |
| Jacksonville State at Western Kentucky (401870752) | Jacksonville State by 21.60, 91.2% away win | Western Kentucky 34–24 | +31.60 |

## Stanford at Virginia Tech

Pregame: the saved PASS explicitly recognized Stanford's recent passing and Virginia Tech's vulnerable secondary, while Stanford's listed absences tempered the case. Stanford moved ahead 21–0 on three rushing touchdowns and led 24–7 at halftime. Stanford rushed for 233 yards and four scores, recorded five sacks and took the ball away three times. The observed upset path included ground production and disruption of Virginia Tech's offense, beyond the passing matchup used in the saved explanation. The favorite's large model margin did not obligate a play, and the existing review retained PASS.

QA disposition: test whether a rushing and pass-protection countercase, demonstrable only from pregame evidence, discriminates high-probability favorites that are vulnerable. Record comparable high-confidence wins as controls. The original feature contribution and whether updated information was knowable at the freeze boundary remain open.

Sources: [Virginia Tech recap](https://hokiesports.com/news/2026/11/14/hokies-drop-home-contest-to-stanford) and [ACC box score](https://theacc.com/boxscore.aspx?id=JcLFfL9RUu0H5ystoOMbjQ7A58QMysWHEEqi7hufVoQXO5nVxbctjHh%2F6ifARsoKUNz2Cn1GpJx0eQgL%2FI8uNugW6%2F65ooJ9xE6%2BliOEFRks9siuyFubd2wbCSoEz4a%2FE0KomwUCQcbFtY9fdJY%2BSfQxESrRMugmh9hJgpGX4hv1rK35yVdIhfFOTsUUG%2BMZ&path=football).

## Jacksonville State at Western Kentucky

Pregame: Jacksonville State's dual-threat rushing was the archived spread rationale. The Friday card retained PASS with a same-number price miss and pending C-USA material report. Western Kentucky held Jacksonville State to 48 rushing yards, and Jacksonville State did not score after halftime. WKU won the fourth quarter 13–0 after trailing 24–21 entering it. WKU quarterback Brock Glenn ran for 71 yards and two scores and threw a touchdown. Opponent rush containment and the home quarterback's rushing contribution are concrete game mechanisms. Applying five additional odds points at the same spread would not change the grade.

QA disposition: test whether pregame opponent run defense and documented quarterback role uncertainty qualify the favorite's rushing case, including comparably priced winners. Preserve the quote and missing material report as separate historical holds. No confirmed injury surprise or feature defect is assigned.

Sources: [WKU recap](https://wkusports.com/news/2026/11/14/football-hilltoppers-take-down-jax-state-34-24-on-homecoming), [Jacksonville State box score](https://jaxstatesports.com/sports/football/stats/2026/western-kentucky/boxscore/8717), and [archived Friday card](../operational/CFB_WEEK11_FRIDAY_BETTING_CARD_20261111.md).

## Next QA step

Apply the same pregame-evidence test to comparable high-confidence winners and the two largest remaining queued margin errors. Only advance a candidate adjustment if the countercase could have been identified prospectively and it adds discrimination without suppressing useful opportunities. Week 12's registered probability shadow remains independent. No production or historical decision changes.
