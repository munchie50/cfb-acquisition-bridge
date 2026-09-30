#!/usr/bin/env python3
from pathlib import Path
p=Path("scripts/cfb_qa_prospective_s2_k1_consumer_v1_2026_09_30.py").read_text()
required=[
 'MAPPED=set(MAP); S1ONLY=set(FEATURES)-MAPPED',
 'len(MAPPED)==10 and len(S1ONLY)==7',
 'n/(n+1.0)*float(raw)+1/(n+1.0)*float(b)',
 'resid=(no/(no+1.0)*rawo+1/(no+1.0)*bo)-bo',
 's2=s1+float(resid.mean())',
 'candidate_id":"S2_K1"',
 '"k":1',
 'bf15ce41180bfb4e250d311df279e98c13b65432756ae07f7a30264cbae0e221',
 '68fb5193ccb8828ac8d34dfe820101181c2bde078a04a6d5afd4c08bcf0cab45',
 '"target_outcomes_opened":False',
 '"market_joined":False',
 '"wager_or_execution_joined":False',
 '"protected_2025_test_opened":False',
 '"fit_or_optimization_performed":False',
 'role=S[["game_id","side","team"]].merge(G[["game_id","home_team","away_team","neutral_site"]]',
 'venue["venue_state"]=np.where(venue.neutral_site.map(neutral_state),"NEUTRAL","HOME")',
]
for x in required: assert x in p, f"missing S2_K1 invariant: {x}"
for forbidden in ("pyreadr","read_parquet","cfb_schedules_2026","pbp_2026","S2_K1_CONSUMER_ROLE_VENUE_INTERFACE_REQUIRED","k={1,2,4,8}"):
    assert forbidden not in p, f"consumer reopened forbidden/raw surface: {forbidden}"
assert p.count("s2=s1+") == 1
print("PASS_PROSPECTIVE_S2_K1_CONSUMER_STATIC_GATE")
