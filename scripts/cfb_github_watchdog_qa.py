#!/usr/bin/env python3
"""Read-only GitHub Actions watchdog. Public repo API; no credentials required."""
import argparse
import datetime as dt
import json
import hashlib
import urllib.request

BASE="https://api.github.com/repos/munchie50/cfb-acquisition-bridge"
TARGETS={
    ".github/workflows/cfb_weekly_monday_source_readiness.yml": 9,
    ".github/workflows/cfb_weekly_tuesday_candidate_freeze.yml": 9,
    ".github/workflows/cfb_weekly_wednesday_fallback.yml": 9,
}
def assess(runs, now):
    result=[]
    for path,age_days in TARGETS.items():
        matches=[r for r in runs if r.get("path")==path and r.get("head_branch")=="main" and r.get("event")=="schedule"]
        matches.sort(key=lambda r:r.get("created_at",""),reverse=True)
        if not matches:
            status="NO_SCHEDULED_RECEIPT"
        else:
            r=matches[0]
            age=(now-dt.datetime.fromisoformat(r["created_at"].replace("Z","+00:00"))).total_seconds()/86400
            if age>age_days: status="STALE_SCHEDULED_RECEIPT"
            elif r.get("status")!="completed": status="RUN_NOT_TERMINAL"
            elif r.get("conclusion")!="success": status="WORKFLOW_FAILURE"
            else: status="GITHUB_WORKFLOW_PASS_ONLY"
        receipt_id=str(matches[0].get("id","none")) if matches else "none"
        incident_key=hashlib.sha256((path+"|"+receipt_id+"|"+status).encode()).hexdigest()[:20]
        result.append({"path":path,"status":status,"source":"github_actions","coverage":"github_only","receipt_id":receipt_id,"incident_key":incident_key,"action_required":status!="GITHUB_WORKFLOW_PASS_ONLY"})
    return result
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--fixture")
    p.add_argument("--now")
    args=p.parse_args()
    now=dt.datetime.fromisoformat(args.now.replace("Z","+00:00")) if args.now else dt.datetime.now(dt.timezone.utc)
    if args.fixture:
        runs=json.load(open(args.fixture))
    else:
        runs=[]
        for path in TARGETS:
            workflow=path.rsplit("/",1)[-1]
            url=BASE+"/actions/workflows/"+workflow+"/runs?per_page=20&branch=main&event=schedule"
            req=urllib.request.Request(url,headers={"Accept":"application/vnd.github+json","User-Agent":"cfb-readonly-watchdog"})
            with urllib.request.urlopen(req,timeout=15) as resp:
                runs.extend(json.load(resp)["workflow_runs"])
    for item in assess(runs,now):
        print(json.dumps(item,sort_keys=True))
if __name__=="__main__":
    main()
