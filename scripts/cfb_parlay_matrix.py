"""Evaluate one archived ranked card without writing or publishing anything.

Input JSON contains card_at, legs, and optional offers and straight_top10.
Each leg has rank, game_id, market (SPREAD/ML/MONEYLINE/TOTAL), side, line, kickoff
and cutoff. Moneyline line is null. Each offer has kind, book, source,
observed_at, price (American odds), and its exact leg identities. Only
BOOK_OFFER observations qualify. straight_top10 contains exact leg
identities from the independently selected straight card, if available.
"""

import argparse
from collections import Counter, defaultdict
from datetime import datetime
from itertools import combinations
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
        token = (ranks, book, source, observed, price)
        if token in seen:
            rejected["duplicate_observation"] += 1
            continue
        seen.add(token)
        qualified[ranks].append({
            "book": book, "source": source, "observed_at": observed.isoformat(), "price": price,
            "break_even_probability": -price / (100 - price) if price < 0 else 100 / (100 + price),
        })

    builds = []
    for ranks, offers in sorted(qualified.items()):
        keys = [identity(legs[rank - 1]) for rank in ranks]
        builds.append({
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
            cells.append({
                "depth": depth, "legs": count, "missing_ranks": max(0, depth - len(prefix)),
                "distinct_game_combinations_by_market": dict(sorted(market_mix.items())),
                "qualified_builds": len(offered), "shared_game_build_counts": dict(sorted(exposure.items())),
            })
    return {"cells": cells, "builds": builds, "rejected_offers": dict(sorted(rejected.items()))}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="archived card JSON")
    args = parser.parse_args()
    with open(args.input, encoding="utf-8") as source:
        report = evaluate(json.load(source))
    print(json.dumps(report, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
