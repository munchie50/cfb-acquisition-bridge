"""QA-only proposal: record an expired review without inventing canonical history.
No production schema registration, canonical writes, renewal, PASS conversion or execution.
"""
import argparse, copy, hashlib, json, re
from datetime import datetime, timezone
from pathlib import Path

SCHEMA = "CFB_EXPIRED_UNPUBLISHED_REVIEW_FACT_V1"
LINEAGE = "57afbbbc65d58d9ee739bcb2823685e3fc0a5cb9"
# These four exact remote-readback identities only; not a general gap exception.
TRUSTED = {"401856842":{"path":"evidence/operational/recommendation_reviews/CFB_ARIZONA_PRICE_CONDITIONAL_20261027T015520Z.json","commit":"a0ecea22136f4945e046be2043f6dad7c7dee930","blob":"e096376b2343667fc28b36c1f643b30ea1f854f9","committed_at":"2026-10-27T02:06:37Z"},"401856848":{"path":"evidence/operational/recommendation_reviews/CFB_CINCINNATI_CONTROLLED_BETA_20261027T015520Z.json","commit":"2928ff585df588489ad55fb05af7e196a3e5269e","blob":"f270892ad49f6f3c19e051bb75a4763e5a98a0fb","committed_at":"2026-10-27T02:15:34Z"},"401862812":{"path":"evidence/operational/recommendation_reviews/CFB_FLORIDA_ATLANTIC_CONTROLLED_BETA_20261027T013124Z.json","commit":"6a3cda95cfb0ba40edfc7179172bdeda198d0bb5","blob":"9547eb01aad7d2272679de20c61c9c79c2b0f7c7","committed_at":"2026-10-27T01:36:36Z"},"401871058":{"path":"evidence/operational/recommendation_reviews/CFB_MIDDLE_TENNESSEE_CONTROLLED_BETA_20261026T234404Z.json","commit":"37f0e3edf5b09afdc4f05e14e5a70b6d4fa91ab3","blob":"d0a4620f56a84b96931df1dfa8f843324ef58212","committed_at":"2026-10-26T23:44:05Z"}}
def blob(text):
    b=text.encode("utf-8")
    return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def clock(value):
    t=datetime.fromisoformat(value.replace("Z","+00:00"))
    if t.tzinfo is None: raise ValueError("timezone required")
    return t.astimezone(timezone.utc)
def facts(item, canonical, expected_canonical_blob, lineage, now):
    if blob(canonical)!=expected_canonical_blob: raise ValueError("canonical binding")
    if blob(lineage)!=LINEAGE: raise ValueError("original lineage binding")
    if not re.fullmatch(r"evidence/operational/recommendation_reviews/[A-Za-z0-9_-]+\.json",item["path"]): raise ValueError("review path")
    if not re.fullmatch("[0-9a-f]{40}",item["commit"]): raise ValueError("review commit")
    if blob(item["content"])!=item["blob"]: raise ValueError("review bytes binding")
    trusted=TRUSTED.get(item["game"])
    if trusted is None or any(item[k]!=v for k,v in trusted.items()): raise ValueError("outside four independently recovered immutable reviews")
    review=json.loads(item["content"])
    if review["schema"]!="CFB_PROSPECTIVE_CONDITIONAL_REVIEW_V2" or review["state"]!="CONDITIONAL": raise ValueError("unqualified review")
    if review["game_id"]!=item["game"] or review["original_lineage_blob"]!=LINEAGE: raise ValueError("review identity")
    census={r["game_id"]:r for r in json.loads(lineage)["rows"]}
    if census[item["game"]]["first_frozen_status"]!="PREDICTION": raise ValueError("model exclusion")
    packets=[json.loads(m) for m in re.findall(r"^```cfb-week9-decision-v1\n(.*?)^```[ \t]*$",canonical,re.M|re.S)]
    if not packets: raise ValueError("missing canonical history")
    if item["blob"] in canonical or item["path"] in canonical: raise ValueError("review already canonically referenced")
    latest={r["game_id"]:r for r in packets[-1]["rows"]}
    if latest[item["game"]]["state"]!="INCONCLUSIVE" or latest[item["game"]].get("review_ref") is not None: raise ValueError("not unpublished current case")
    recorded,committed,reconcile,cutoff,observed=map(clock,[review["recorded_at_utc"],item["committed_at"],review["reconciliation_utc"],review["planning_cutoff_utc"],now])
    kickoff=clock(review["market_reference"]["kickoff_utc"])
    if not recorded<=committed<reconcile<=cutoff<=observed<kickoff: raise ValueError("chronology/expired-window boundary")
    window=review["execution_window"]
    if not recorded<=clock(window["start_utc"])<clock(window["end_utc"])==cutoff: raise ValueError("immutable window")
    limit=review["acceptable_number"]
    if limit["market"]!=review["market"] or limit["selection"]!=review["selection"] or not isinstance(limit["minimum_price"],int): raise ValueError("limit binding")
    return {"schema":SCHEMA,"state":"EXPIRED_UNPUBLISHED_REVIEW","game_id":item["game"],
            "recorded_at_utc":now,"review_ref":{k:item[k] for k in ("path","commit","blob")},
            "original_acceptable_number":copy.deepcopy(limit),"original_reconciliation_utc":review["reconciliation_utc"],
            "original_planning_cutoff_utc":review["planning_cutoff_utc"],"original_execution_window":copy.deepcopy(window),
            "canonical_prior_blob":expected_canonical_blob,"canonical_prior_as_of_utc":packets[-1]["as_of_utc"],
            "canonical_prior_state":"INCONCLUSIVE","recommendation_active":False,"execution_created":False,
            "qualification":"QA_PROPOSAL_ONLY_NOT_REGISTERED_IN_PRODUCTION_SCHEMA",
            "meaning":"The immutable review existed before expiry; it never entered the recovered canonical history. The missed publication remains a failure; no bet, historical decision or fresh recommendation is reconstructed."}
def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ("inputs","canonical","lineage","output"): p.add_argument("--"+k,type=Path,required=True)
    a=p.parse_args()
    x=json.loads(a.inputs.read_text());canonical=a.canonical.read_text();lineage=a.lineage.read_text()
    records=[facts(i,canonical,x["canonical_blob"],lineage,x["now"]) for i in x["records"]]
    if len({r["game_id"] for r in records})!=len(records): raise ValueError("duplicate identity")
    out={"status":"PROPOSED_HISTORY_ONLY_LIFECYCLE_NOT_PRODUCTION_ACCEPTANCE","canonical_mutation":False,"records":records}
    a.output.write_text(json.dumps(out,indent=2)+"\n");print(json.dumps({"status":out["status"],"records":len(records)}))
if __name__=="__main__":main()
