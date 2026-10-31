"""Week10 shadow six-branch CBS inventory. Never current consensus or a wager."""
import json
from pathlib import Path
from cfb_cbs_full_board_normalizer import normalize, WEEK10_URL

ROOT = Path(__file__).resolve().parents[1]
CAPTURE = ROOT / "evidence/operational/CFB_CBS_WEEK10_LIVE_MARKDOWN_CAPTURE_20261031.md"
BASELINE = ROOT / "evidence/operational/CFB_WEEK10_CANDIDATE_CANONICAL_IDENTITY_BASELINE_20261031.json"
# Conservative end-of-day upper bound, NOT a certified retrieval timestamp.
RECOVERED_BY_UPPER_BOUND = "2026-10-31T23:59:59Z"
BRANCHES = ("away_spread", "home_spread", "away_ml", "home_ml", "over_total", "under_total")

def inventory():
    board = normalize(CAPTURE.read_text(), BASELINE.read_text(), RECOVERED_BY_UPPER_BOUND,
                      source_url=WEEK10_URL, profile="WEEK10")
    rows = []
    for game in board["games"]:
        away, home = game["team_offers"]
        if away["total"]["side"] not in ("o", None) or home["total"]["side"] not in ("u", None):
            raise ValueError("unqualified total side orientation")
        fields = (away["spread"], home["spread"], away["moneyline"], home["moneyline"],
                  away["total"], home["total"])
        branches = {name: {"availability": field["availability"], "line": field["line"],
                           "price": field["price"], "opaque_book_icon_id": field["opaque_book_icon_id"]}
                    for name, field in zip(BRANCHES, fields)}
        rows.append({"game_id": game["game_id"], "away_team": game["away_team"],
                     "home_team": game["home_team"], "cbs_display_kickoff_utc": game["source_kickoff_utc"],
                     "independently_verified_kickoff": False, "branches": branches})
    if len(rows) != 63 or len({r["game_id"] for r in rows}) != 63:
        raise ValueError("incomplete Week10 source identity")
    counts = {b: sum(r["branches"][b]["availability"] == "DISPLAYED" for r in rows)
              for b in BRANCHES}
    return {"status": "SHADOW_FALLBACK_BRANCH_INVENTORY_ONLY", "source": WEEK10_URL,
            "capture_recovery_upper_bound_utc": RECOVERED_BY_UPPER_BOUND,
            "recovery_bound_not_exact_fetch": True, "games": 63, "possible_branches": 378,
            "displayed_by_branch": counts, "consensus": "UNAVAILABLE",
            "executability": "UNVERIFIED", "decision_authorized": False, "rows": rows}

if __name__ == "__main__":
    print(json.dumps(inventory(), indent=2))
