# CFB Engine — Challenger B 2026 FBS Membership Authority v1.203

Status: **PASS — 2026 MEMBERSHIP TRANSITION FROZEN**
Parent: v1.202
Source authority: NCAA current 2026 realignment reporting.

The accepted v1.157 membership lineage contains 136 FBS programs for 2025. NCAA's current 2026 realignment record identifies two additional football programs moving from FCS to FBS in 2026:
- North Dakota State — Mountain West football-only member;
- Sacramento State — MAC football-only member.

NCAA explicitly states UC Davis joins the Mountain West in other sports but remains FCS in football for 2026, so UC Davis is not added.

Therefore the Challenger B 2026 FBS membership is frozen as:
**2025 accepted membership + North Dakota State + Sacramento State = 138 teams.**

No other 2026 FCS-to-FBS addition is admitted by this checkpoint.

Population semantics remain unchanged:
- a qualified game enters the relevant-FBS universe when at least one participant is in the frozen 2026 FBS membership;
- classify as FBS_VS_FBS when both are members, otherwise FBS_VS_NONFBS;
- preserve regular / conference-championship / postseason classification semantics;
- aliases from accepted v1.157 authority remain in force.

This membership checkpoint does not itself generate predictions or expose target outcomes. It exists to prevent mutable-source or guessed membership from changing the live-shadow target population.
