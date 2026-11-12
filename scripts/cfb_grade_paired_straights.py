"""Grade a frozen PASS comparison against qualified directed final scores.

Run with the pregame baseline JSON and a finals JSON object keyed by game ID.
Final records use status QUALIFIED_FINAL, source, away_team, home_team,
away, and home. Scores are integers. Output is research-only JSON.
"""

import argparse
from collections import Counter
import json

from cfb_parlay_matrix import grade_leg, identity, scenario_returns


def ticket(game, market, side, line, price, finals):
    if type(price) is not int or abs(price) < 100:
        raise ValueError(f"invalid American odds for {game}")
    key = identity(dict(game_id=game, market=market, side=side, line=line))
    grade = grade_leg(key, finals)
    net = scenario_returns("ALL_PUSH" if grade == "PUSH" else grade, price)["500"]["net_cents"]
    return {"line": line, "price": price, "grade": grade, "net_cents": net}


def summary(tickets):
    counts = Counter(t["grade"] for t in tickets)
    graded = [t for t in tickets if t["net_cents"] is not None]
    return {
        "selections": len(tickets), "graded": len(graded),
        "wins": counts["WIN"], "losses": counts["LOSS"], "pushes": counts["PUSH"],
        "pending": counts["PENDING"], "graded_stake_cents": 500 * len(graded),
        "graded_net_cents": sum(t["net_cents"] for t in graded) if graded else None,
    }


def grade(baseline, finals):
    if baseline["schema"] != "CFB_WEEK11_SATURDAY_PASS_PREGAME_BASELINE_V1":
        raise ValueError("unsupported pregame baseline schema")
    results, games = [], set()
    for row in baseline["rows"]:
        game = row["id"]
        if game in games or row["decision"] != "PASS":
            raise ValueError(f"duplicate or non-PASS game {game}")
        games.add(game)
        final = finals.get(game)
        if final and final.get("status") == "QUALIFIED_FINAL":
            if (final["away_team"], final["home_team"]) != tuple(row["pair"]):
                raise ValueError(f"final has the wrong directed teams for {game}")
        markets = set()
        for pair in row["paired_opening_selections"]:
            market, side = pair["market"], pair["selection"]
            if market in markets:
                raise ValueError(f"duplicate market for {game}")
            markets.add(market)
            opening = ticket(game, market, side, pair["opening_line"], pair["opening_price"], finals)
            q = pair["thursday"]
            comparison = "UNAVAILABLE"
            thursday = None
            if q is not None:
                line = q.get("line")
                if market == "TOTAL" and q["side"] != side:
                    raise ValueError(f"total side mismatch for {game}")
                comparison = "SAME_LINE" if line == opening["line"] else "CHANGED_LINE"
                thursday = ticket(game, market, side, line, q["price"], finals)
            if comparison != pair["match"]:
                raise ValueError(f"pair classification mismatch for {game}")
            results.append({
                "id": game, "market": market, "side": side, "comparison": comparison,
                "opening": opening, "thursday": thursday,
                "qualified_final_source": final["source"] if opening["grade"] != "PENDING" else None,
            })
        if markets != {"SPREAD", "ML", "TOTAL"}:
            raise ValueError(f"incomplete frozen selections for {game}")

    comparison_types = ("SAME_LINE", "CHANGED_LINE", "UNAVAILABLE")
    expected = {key: sum(r["comparison"] == key for r in results) for key in comparison_types}
    if expected != baseline["pairing"] or len(games) != baseline["counts"]["games"]:
        raise ValueError("pregame denominators changed")

    groups = {}
    for market in ("ALL", "SPREAD", "ML", "TOTAL"):
        selected = [r for r in results if market == "ALL" or r["market"] == market]
        comparisons = {}
        for key in comparison_types:
            rows = [r for r in selected if r["comparison"] == key]
            opening = summary([r["opening"] for r in rows])
            thursday = summary([r["thursday"] for r in rows if r["thursday"] is not None])
            net = None
            if key != "UNAVAILABLE" and opening["graded"]:
                net = thursday["graded_net_cents"] - opening["graded_net_cents"]
            comparisons[key] = {"opening": opening, "thursday": thursday, "net_delta_cents": net}
        groups[market] = {"opening": summary([r["opening"] for r in selected]), "pairs": comparisons}
    return {"games": len(games), "by_market": groups, "rows": results}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("baseline")
    parser.add_argument("finals")
    args = parser.parse_args()
    with open(args.baseline, encoding="utf-8") as source:
        baseline = json.load(source)
    with open(args.finals, encoding="utf-8") as source:
        finals = json.load(source)
    print(json.dumps(grade(baseline, finals), indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
