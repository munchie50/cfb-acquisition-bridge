"""Fail-closed gate for R91 displayed odds; no betting decisions are emitted."""
import json
import sys
from datetime import datetime, timezone

BRANCHES = ("away_spread", "home_spread", "away_ml", "home_ml", "over_total", "under_total")


def _verified_offer(proof):
    """Require independently attested quote evidence; never trust display timestamps."""
    if not isinstance(proof, dict):
        return False
    if proof.get("verification_status") != "INDEPENDENTLY_VERIFIED":
        return False
    if not proof.get("evidence_url") or not proof.get("evidence_sha256"):
        return False
    sha = proof["evidence_sha256"]
    if not isinstance(sha, str) or len(sha) != 64 or any(ch not in "0123456789abcdef" for ch in sha):
        return False
    try:
        clock = datetime.fromisoformat(proof["offer_updated_at_utc"].replace("Z", "+00:00"))
        if clock.tzinfo is None or clock.utcoffset().total_seconds() != 0:
            return False
        if clock > datetime.now(timezone.utc):
            return False
    except (KeyError, TypeError, ValueError, AttributeError):
        return False
    return True


def qualify(inventory, quote_evidence=None):
    """Only independent offer-level provenance can qualify a displayed branch.

    quote_evidence maps game ID -> branch -> {operator, offer_updated_at_utc,
    venue, venue_executable, line, price}. A missing field is WAIT.
    """
    if inventory.get("schema") != "CFB_WEEK10_R91_CBS_DIRECTED_SIX_BRANCH_SOURCE_INVENTORY":
        raise ValueError("wrong source inventory schema")
    rows = inventory.get("rows", [])
    if len(rows) != 63 or len({str(x.get("game_id")) for x in rows}) != 63:
        raise ValueError("unexpected or duplicate canonical game inventory")
    quote_evidence = quote_evidence or {}
    result = []
    for game in rows:
        gid = str(game["game_id"])
        branches = game.get("branches", {})
        if set(branches) != set(BRANCHES):
            raise ValueError("missing or extra six-market branches: " + gid)
        for branch in BRANCHES:
            display = branches[branch]
            proof = quote_evidence.get(gid, {}).get(branch, {})
            required = ("operator", "offer_updated_at_utc", "venue", "venue_executable", "price")
            valid = (display.get("status") == "DISPLAYED_UNQUALIFIED"
                     and all(proof.get(k) is not None for k in required)
                     and bool(proof.get("operator")) and bool(proof.get("venue"))
                     and proof.get("venue_executable") is True
                     and _verified_offer(proof)
                     and proof.get("price") == display.get("price")
                     and (branch.endswith("_ml") or proof.get("line") == display.get("line")))
            result.append({"game_id": gid, "branch": branch,
                           "market_provenance": "QUALIFIED_OFFER_EVIDENCE" if valid else "WAIT",
                           "decision_authorized": False})
    return {"schema": "CFB_WEEK10_MARKET_PROVENANCE_GATE", "status": "MARKET_PROVENANCE_ONLY_NO_MODEL_OR_MATERIAL_DECISION",
            "counts": {"branches": len(result), "qualified": sum(x["market_provenance"] == "QUALIFIED_OFFER_EVIDENCE" for x in result),
                       "wait": sum(x["market_provenance"] == "WAIT" for x in result)}, "rows": result}


if __name__ == "__main__":
    with open(sys.argv[1], encoding="utf-8") as f:
        inventory = json.load(f)
    quotes = {}
    if len(sys.argv) > 2:
        with open(sys.argv[2], encoding="utf-8") as f:
            quotes = json.load(f)
    print(json.dumps(qualify(inventory, quotes), indent=2))
