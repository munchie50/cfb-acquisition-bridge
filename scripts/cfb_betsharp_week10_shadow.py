"""Date-scoped BetSharp discovery for CBS-unpriced Week10 games; not an odds feed."""
import json
import re
import sys

def discover(markdown, unpriced_queue, day="2026-11-07"):
    if day not in ("2026-11-03", "2026-11-04", "2026-11-06", "2026-11-07"):
        raise ValueError("unsupported Week10 day")
    slugs = set(re.findall(r"https://betsharp\.com/ncaaf/game/("+re.escape(day)+r"-[a-z0-9-]+)", markdown))
    targets = []
    for row in unpriced_queue:
        # Discovery evidence is not an identity join; requires separate canonical validation.
        targets.append({"game_id": row["game_id"], "away_team": row["away_team"],
                        "home_team": row["home_team"], "identity_verified": False})
    return {"status": "SHADOW_DISCOVERY_ONLY", "day": day,
            "discovered_source_game_urls": sorted("https://betsharp.com/ncaaf/game/"+x for x in slugs),
            "source_urls_count": len(slugs), "unpriced_targets": targets,\n            "source_game_urls_exceed_canonical_slate": len(slugs) > 63,\n            "unverified_cross_league_rows_possible": True,
            "canonical_join_authorized": False, "prices_qualified": False,
            "decision_authorized": False}

if __name__ == "__main__":
    print(json.dumps(discover(sys.stdin.read(), json.load(open(sys.argv[1]))["targets"], sys.argv[2]), indent=2))
