"""Evaluate one archived ranked card without writing or publishing anything.

Input JSON contains card_at, legs, and optional offers and straight_top10.
Each leg has rank, game_id, market (SPREAD/ML/MONEYLINE/TOTAL), side, line, kickoff
and cutoff. Moneyline line is null. Each offer has kind, book, source,
observed_at, price (American odds), and its exact leg identities. Only
BOOK_OFFER observations qualify. A ranked leg with min_leg_price requires
a matching displayed price on the offered leg in the combined observation. straight_top10 contains exact leg
identities from the independently selected straight card, if available.
Optional finals are keyed by game_id and contain status, source, away,
and home. Only QUALIFIED_FINAL scores are graded. Push-adjusted book
payouts require separate evidence and are left unresolved.
Optional portfolio_policy specifies depth, legs, quote_from, and select_at.
The policy ranks builds lexicographically by original leg ranks and selects
the best latest observed quote per build within the declared time window.
"""

import argparse
from collections import Counter, defaultdict
from datetime import datetime
from itertools import combinations
from fractions import Fraction
import json
import math


def timestamp(value):
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.utcoffset() is None:
        raise ValueError("timestamps require a UTC offset")
    return parsed


def identity(leg):
    game = leg["game_id"]
    market, side, line = leg["market"], leg["side"], leg["line"]
    if not isinstance(game, str) or not game.strip():
        raise ValueError("game_id must be a nonempty string")
    if market == "MONEYLINE":
        market = "ML"
    if market not in ("SPREAD", "ML", "TOTAL"):
        raise ValueError("unsupported market")
    if side not in (("over", "under") if market == "TOTAL" else ("home", "away")):
        raise ValueError("invalid side")
    if market == "ML":
        if line is not None:
            raise ValueError("moneyline requires a null line")
    elif type(line) not in (int, float) or not math.isfinite(line):
        raise ValueError("market requires a finite line")
    return game, market, side, line


def grade_leg(key, finals):
    game, market, side, line = key
    final = finals.get(game)
    if not final or final.get("status") != "QUALIFIED_FINAL":
        return "PENDING"
    away, home = final["away"], final["home"]
    if any(type(score) is not int or score < 0 for score in (away, home)):
        raise ValueError(f"invalid qualified score for {game}")
    if not final["source"].strip():
        raise ValueError(f"missing final provenance for {game}")
    if market == "TOTAL":
        margin = home + away - line
        margin = margin if side == "over" else -margin
    else:
        margin = home - away if side == "home" else away - home
        if market == "SPREAD":
            margin += line
    return "WIN" if margin > 0 else "LOSS" if margin < 0 else "PUSH"


def scenario_returns(result, price):
    returns = {}
    for stake in (200, 500):
        if result == "WIN":
            profit = Fraction(stake * price, 100) if price > 0 else Fraction(stake * 100, -price)
            net = int(profit + Fraction(1, 2))
        elif result == "LOSS":
            net = -stake
        elif result == "ALL_PUSH":
            net = 0
        else:
            net = None
        returns[str(stake)] = {"net_cents": net, "gross_cents": None if net is None else stake + net}
    return returns


def compare_portfolios(policy, builds, legs, card_at, ineligible_prices):
    depth, count = policy["depth"], policy["legs"]
    start, end = timestamp(policy["quote_from"]), timestamp(policy["select_at"])
    if depth not in (10, 15, 20, 25, 30) or count not in (2, 3, 4, 5):
        raise ValueError("invalid portfolio matrix cell")
    if not card_at <= start <= end:
        raise ValueError("invalid portfolio quote window")

    selected = []
    for build in builds:
        ranks = build["ranks"]
        if len(ranks) != count or max(ranks) > depth:
            continue
        if any(end > timestamp(legs[rank - 1]["cutoff"]) or
               end >= timestamp(legs[rank - 1]["kickoff"]) for rank in ranks):
            continue
        latest = {}
        for offer in build["offers"]:
            observed = timestamp(offer["observed_at"])
            if start <= observed <= end:
                current = latest.get(offer["book"])
                if current is None or observed > timestamp(current["observed_at"]):
                    latest[offer["book"]] = offer
                elif observed == timestamp(current["observed_at"]) and (
                    offer["price"], offer["displayed_leg_prices_by_rank"]
                ) != (current["price"], current["displayed_leg_prices_by_rank"]):
                    raise ValueError("conflicting prices from one book at the same time")
        for book, offer in list(latest.items()):
            observed = timestamp(offer["observed_at"])
            if any(observed <= invalid <= end for invalid in ineligible_prices[tuple(ranks), book]):
                del latest[book]
        if latest:
            def quote_order(offer):
                price = offer["price"]
                decimal_profit = Fraction(price, 100) if price > 0 else Fraction(100, -price)
                return -decimal_profit, offer["book"], offer["source"]

            selected.append((build, min(latest.values(), key=quote_order)))

    scenarios = []
    for requested in range(11):
        positions = selected[:requested]
        games = Counter(game for build, _ in positions for game in build["game_ids"])
        outcomes = Counter(build["result"] for build, _ in positions)
        loss_by_game = Counter(game for build, _ in positions if build["result"] == "LOSS"
                               for game in build["losing_game_ids"])
        returns = {}
        for stake in (200, 500):
            nets = [offer["scenario_returns_by_stake_cents"][str(stake)]["net_cents"]
                    for _, offer in positions]
            net = None if any(value is None for value in nets) else sum(nets)
            returns[str(stake)] = {
                "stake_cents": stake * len(positions),
                "net_cents": net,
                "gross_cents": None if net is None else stake * len(positions) + net,
                "max_stake_exposed_to_one_game_cents": stake * max(games.values(), default=0),
            }
        scenarios.append({
            "requested_builds": requested, "selected_builds": len(positions),
            "unfilled_slots": requested - len(positions),
            "result_counts": dict(sorted(outcomes.items())),
            "shared_game_build_counts": dict(sorted(games.items())),
            "losing_builds_by_game": dict(sorted(loss_by_game.items())),
            "returns_by_stake_cents": returns,
        })

    return {
        "policy": {"depth": depth, "legs": count, "quote_from": start.isoformat(),
                   "select_at": end.isoformat(), "ordering": "ORIGINAL_LEG_RANKS"},
        "available_builds": len(selected),
        "positions": [{"ranks": build["ranks"], "offer": offer,
                       "straight_overlap": build["straight_overlap"]}
                      for build, offer in selected[:10]],
        "scenarios": scenarios,
    }


def evaluate(data):
    card_at = timestamp(data["card_at"])
    legs = sorted(data["legs"], key=lambda leg: leg["rank"])
    if any(type(leg["rank"]) is not int for leg in legs) or (
        [leg["rank"] for leg in legs] != list(range(1, len(legs) + 1))
    ):
        raise ValueError("ranks must form an authentic contiguous prefix")
    by_identity = {identity(leg): leg for leg in legs}
    if len(by_identity) != len(legs):
        raise ValueError("duplicate ranked leg")
    minimum_prices = {key: leg["min_leg_price"] for key, leg in by_identity.items()
                      if "min_leg_price" in leg}
    if any(type(price) is not int or abs(price) < 100 for price in minimum_prices.values()):
        raise ValueError("invalid registered minimum leg price")
    timing = {
        key: (timestamp(leg["cutoff"]), timestamp(leg["kickoff"]))
        for key, leg in by_identity.items()
    }
    straights = data.get("straight_top10")
    straight_keys = None if straights is None else {identity(leg) for leg in straights}
    if straight_keys is not None and (len(straight_keys) != len(straights) or len(straights) > 10):
        raise ValueError("invalid straight Top 10")
    qualified = defaultdict(list)
    rejected = Counter()
    ineligible_prices = defaultdict(list)
    seen = set()
    for offer in data.get("offers", []):
        if offer.get("kind") != "BOOK_OFFER":
            rejected["not_book_offer"] += 1
            continue
        keys = tuple(identity(leg) for leg in offer["legs"])
        if len(keys) not in (2, 3, 4, 5) or len({key[0] for key in keys}) != len(keys):
            rejected["invalid_leg_count_or_same_game"] += 1
            continue
        if any(key not in by_identity for key in keys):
            rejected["leg_mismatch"] += 1
            continue
        price = offer["price"]
        book, source = offer["book"], offer["source"]
        if type(price) is not int or abs(price) < 100 or not book.strip() or not source.strip():
            rejected["invalid_price_or_provenance"] += 1
            continue
        observed = timestamp(offer["observed_at"])
        if observed < card_at or any(
            observed > timing[key][0] or observed >= timing[key][1] for key in keys
        ):
            rejected["outside_pregame_window"] += 1
            continue
        ranks = tuple(sorted(by_identity[key]["rank"] for key in keys))
        displayed = {key: leg.get("price") for key, leg in zip(keys, offer["legs"])}
        if any(type(displayed[key]) is not int or abs(displayed[key]) < 100
               for key in keys if key in minimum_prices):
            rejected["missing_or_invalid_displayed_leg_price"] += 1
            ineligible_prices[ranks, book].append(observed)
            continue
        if any(displayed[key] < minimum_prices[key] for key in keys if key in minimum_prices):
            rejected["below_registered_leg_price"] += 1
            ineligible_prices[ranks, book].append(observed)
            continue
        displayed_by_rank = {by_identity[key]["rank"]: displayed[key]
                             for key in keys if key in minimum_prices}
        token = (ranks, book, source, observed, price, tuple(sorted(displayed_by_rank.items())))
        if token in seen:
            rejected["duplicate_observation"] += 1
            continue
        seen.add(token)
        qualified[ranks].append({
            "book": book, "source": source, "observed_at": observed.isoformat(), "price": price,
            "displayed_leg_prices_by_rank": dict(sorted(displayed_by_rank.items())),
            "break_even_probability": -price / (100 - price) if price < 0 else 100 / (100 + price),
        })

    finals = data.get("finals", {})
    builds = []
    for ranks, offers in sorted(qualified.items()):
        keys = [identity(legs[rank - 1]) for rank in ranks]
        grades = [grade_leg(key, finals) for key in keys]
        if "PENDING" in grades:
            result = "PENDING"
        elif "LOSS" in grades:
            result = "LOSS"
        elif all(grade == "PUSH" for grade in grades):
            result = "ALL_PUSH"
        elif "PUSH" in grades:
            result = "PUSH_REPRICE_REQUIRED"
        else:
            result = "WIN"
        for offer in offers:
            offer["scenario_returns_by_stake_cents"] = scenario_returns(result, offer["price"])
        builds.append({
            "result": result,
            "leg_grades": grades,
            "losing_game_ids": [key[0] for key, grade in zip(keys, grades) if grade == "LOSS"],
            "ranks": list(ranks),
            "game_ids": [key[0] for key in keys],
            "straight_overlap": None if straight_keys is None else sum(key in straight_keys for key in keys),
            "offers": sorted(offers, key=lambda offer: (
                offer["observed_at"], offer["book"], offer["source"], offer["price"]
            )),
        })

    cells = []
    for depth in (10, 15, 20, 25, 30):
        prefix = [identity(leg) for leg in legs[:depth]]
        for count in (2, 3, 4, 5):
            market_mix = Counter()
            for keys in combinations(prefix, count):
                if len({key[0] for key in keys}) == count:
                    market_mix["+".join(sorted(key[1] for key in keys))] += 1
            offered = [build for build in builds if len(build["ranks"]) == count and max(build["ranks"]) <= depth]
            exposure = Counter(game for build in offered for game in build["game_ids"])
            losing_exposure = Counter(
                game for build in offered if build["result"] == "LOSS" for game in build["losing_game_ids"]
            )
            cells.append({
                "losing_builds_by_game": dict(sorted(losing_exposure.items())),
                "build_result_counts": dict(sorted(Counter(build["result"] for build in offered).items())),
                "depth": depth, "legs": count, "missing_ranks": max(0, depth - len(prefix)),
                "distinct_game_combinations_by_market": dict(sorted(market_mix.items())),
                "qualified_builds": len(offered), "shared_game_build_counts": dict(sorted(exposure.items())),
            })
    report = {"cells": cells, "builds": builds, "rejected_offers": dict(sorted(rejected.items()))}
    if "portfolio_policy" in data:
        report["portfolio"] = compare_portfolios(data["portfolio_policy"], builds, legs, card_at, ineligible_prices)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="archived card JSON")
    args = parser.parse_args()
    with open(args.input, encoding="utf-8") as source:
        report = evaluate(json.load(source))
    print(json.dumps(report, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
