"""Reconcile four observed Covers moneyline-pair identities with CBS gaps.
Observations are discovery evidence only; no stored current prices or offer clock.
"""
import json
from cfb_week10_fallback_branch_inventory import inventory

OBSERVED_PAIR_IDS = {
    "401856743": "Texas vs Missouri",
    "401856740": "Alabama vs LSU",
    "401856745": "Kentucky vs Tennessee",
    "401856741": "Georgia vs Ole Miss",
}

def report(board):
    by_id = {r["game_id"]: r for r in board["rows"]}
    rows = []
    for game_id, name in OBSERVED_PAIR_IDS.items():
        game = by_id[game_id]
        missing = [b for b in ("away_ml", "home_ml")
                   if game["branches"][b]["availability"] != "DISPLAYED"]
        rows.append({"game_id": game_id, "matchup": name,
                     "cbs_missing_moneyline_branches": missing,
                     "unqualified_candidate_count": len(missing)})
    return {"status": "SHADOW_CANDIDATE_GAP_REPORT_ONLY",
            "observed_pair_games": len(rows),
            "candidate_missing_branches": sum(r["unqualified_candidate_count"] for r in rows),
            "prices_freshness_verified": False, "decision_authorized": False, "rows": rows}

if __name__ == "__main__":
    print(json.dumps(report(inventory()), indent=2))
