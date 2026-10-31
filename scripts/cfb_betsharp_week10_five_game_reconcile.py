"""Reconcile five frozen BetSharp game tables; discovery observations only."""
import json
import re
from pathlib import Path
from cfb_betsharp_week10_market_shadow import inspect

SNAPSHOT = Path("evidence/operational/CFB_BETSHARP_WEEK10_FIVE_GAME_MARKET_SHADOW_20261031.md")

def reconcile(text):
    parts = re.split(r"^SOURCE_URL (https://betsharp\.com/ncaaf/game/[^\s]+)\s*$", text, flags=re.M)
    if len(parts) != 11:
        raise ValueError("expected exactly five source page snapshots")
    observations = []
    for i in range(1, len(parts), 2):
        observations.append(inspect(parts[i+1], parts[i]))
    urls = [x["source_url"] for x in observations]
    if len(set(urls)) != 5:
        raise ValueError("duplicate source page")
    available = {k: sum(x["branches"][k]["availability"] == "DISPLAYED_SHADOW" for x in observations)
                 for k in observations[0]["branches"]}
    return {"status": "FROZEN_SHADOW_FIVE_GAME_RECONCILIATION", "games":len(observations),
            "displayed_branch_counts": available, "displayed_total": sum(available.values()),
            "missing_total": 30-sum(available.values()), "canonical_identity_verified": False,
            "source_price_executable": False, "decision_authorized": False,
            "observations": observations}

if __name__ == "__main__":
    result = reconcile(SNAPSHOT.read_text())
    assert result["displayed_total"] == 10
    assert result["missing_total"] == 20
    assert result["decision_authorized"] is False
    print(json.dumps(result, indent=2))
