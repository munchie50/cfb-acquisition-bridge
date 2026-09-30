#!/usr/bin/env python3
"""Static lock for the prospective S2_K1 consumer specification."""
from pathlib import Path
p=Path("evidence/CFB_QA_PROSPECTIVE_S2_K1_CONSUMER_SPEC_2026-09-30.md").read_text()
required=[
 "k = 1 only",
 "candidate_id=S2_K1",
 "No recursion",
 "DEPTH_1_2",
 "DEPTH_3_4",
 "DEPTH_5_PLUS",
 "target outcomes/PBP",
 "market/spread/odds/closing",
 "protected 2025 TEST",
 "margin 0.1; total 0.1; win 0.01",
 "same-cutoff",
 "independently accepted weekly boundary",
 "independently accepted target-baseline companion",
 "B_F(target cutoff)",
 "Unused source schedule metadata",
 "winner/rank fields",
 "Outcome scoring remains separately gated",
]
for t in required: assert t in p, f"missing prospective S2_K1 lock: {t}"
for t in ["S1_K2","S1_K4","S1_K8","S2_K2","S2_K4","S2_K8"]:
    assert t not in p, f"unauthorized prospective grid expansion: {t}"
pairs=[
 "points_for_per_game ↔ points_against_per_game",
 "offensive_scrimmage_plays_per_game ↔ defensive_scrimmage_plays_per_game",
 "offensive_yards_per_play ↔ defensive_yards_per_play",
 "offensive_explosive_play_rate ↔ defensive_explosive_play_rate",
 "offensive_success_rate ↔ defensive_success_rate_allowed",
]
for t in pairs: assert t in p, f"missing frozen S2 mapping pair: {t}"
print("PASS_PROSPECTIVE_S2_K1_CONSUMER_SPEC_STATIC_GATE")
