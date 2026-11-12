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


def compare_graded_pair(opening, thursday):
    if thursday is None or opening["grade"] == "PENDING":
        return None
    result = "ALL_PUSH" if thursday["grade"] == "PUSH" else thursday["grade"]
    thursday_at_opening_price = scenario_returns(result, opening["price"])["500"]["net_cents"]
    return {
        "transition": f'{opening["grade"]}_TO_{thursday["grade"]}',
        "line_effect_cents": thursday_at_opening_price - opening["net_cents"],
        "price_effect_cents": thursday["net_cents"] - thursday_at_opening_price,
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
                "paired_effects": compare_graded_pair(opening, thursday),
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
            effects = [r["paired_effects"] for r in rows if r["paired_effects"] is not None]
            line_net = sum(e["line_effect_cents"] for e in effects) if effects else None
            price_net = sum(e["price_effect_cents"] for e in effects) if effects else None
            if effects and line_net + price_net != net:
                raise ValueError("paired effects do not reconcile")
            comparisons[key] = {
                "opening": opening, "thursday": thursday, "net_delta_cents": net,
                "grade_transitions": dict(sorted(Counter(e["transition"] for e in effects).items())),
                "line_effect_cents": line_net, "price_effect_cents": price_net,
            }
        groups[market] = {"opening": summary([r["opening"] for r in selected]), "pairs": comparisons}
    return {
        "games": len(games), "by_market": groups, "rows": results,
        "effect_method": (
            "Research arithmetic. Apply the Thursday line at the opening price first, then "
            "apply the Thursday price. The intermediate line and price combination is hypothetical."
        ),
    }


def grade_snapshots(baseline, sensitivity, finals):
    """Compare a later board while preserving the primary frozen cohort."""
    if sensitivity["schema"] != "CFB_WEEK11_SATURDAY_PASS_ACTIONS_SENSITIVITY_V1":
        raise ValueError("unsupported sensitivity schema")
    by_id = {row["id"]: row for row in sensitivity["rows"]}
    primary_ids = {row["id"] for row in baseline["rows"]}
    if set(by_id) != primary_ids or len(by_id) != len(sensitivity["rows"]):
        raise ValueError("sensitivity game coverage differs from primary")

    primary_report = grade(baseline, finals)
    alternate_rows = []
    for row in baseline["rows"]:
        later = by_id[row["id"]]
        if later["pair"] != row["pair"] or later["decision"] != row["decision"]:
            raise ValueError(f"sensitivity directed decision mismatch for {row['id']}")
        later_markets = {pair["market"]: pair for pair in later["pairs"]}
        if set(later_markets) != {"SPREAD", "ML", "TOTAL"} or len(later["pairs"]) != 3:
            raise ValueError(f"invalid sensitivity markets for {row['id']}")
        pairs = []
        for original in row["paired_opening_selections"]:
            pair = later_markets[original["market"]]
            if (pair["selection"], pair["line"], pair["price"]) != (
                original["selection"], original["opening_line"], original["opening_price"]
            ):
                raise ValueError(f"sensitivity changed a frozen selection for {row['id']}")
            pairs.append({
                **original, "thursday": pair["collector_quote"], "match": pair["match"],
            })
        alternate_rows.append({**row, "paired_opening_selections": pairs})

    later_report = grade({
        **baseline, "rows": alternate_rows, "pairing": sensitivity["counts"]["pairing"],
    }, finals)
    return {
        "primary": {"capture_utc": baseline["as_of_capture_utc"], "report": primary_report},
        "sensitivity": {"capture_utc": sensitivity["capture_utc"], "report": later_report},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("baseline")
    parser.add_argument("finals")
    parser.add_argument("--sensitivity", help="optional later collector snapshot JSON")
    args = parser.parse_args()
    with open(args.baseline, encoding="utf-8") as source:
        baseline = json.load(source)
    with open(args.finals, encoding="utf-8") as source:
        finals = json.load(source)
    if args.sensitivity:
        with open(args.sensitivity, encoding="utf-8") as source:
            result = grade_snapshots(baseline, json.load(source), finals)
    else:
        result = grade(baseline, finals)
    print(json.dumps(result, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
