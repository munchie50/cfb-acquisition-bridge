#!/usr/bin/env python3
"""Pure, deterministic CFB incident ledger reconciler. No network or mutations."""
import json
import sys
from pathlib import Path

def reconcile(previous, observations, observed_at):
    ledger={item["incident_key"]:dict(item) for item in previous}
    events=[]
    for o in observations:
        key=o["incident_key"]
        if o["action_required"]:
            if key not in ledger:
                ledger[key]={"incident_key":key,"path":o["path"],"status":"OPEN","failure_class":o["status"],"first_seen":observed_at,"last_seen":observed_at,"observations":1,"recovery_attempts":0}
                events.append({"event":"OPENED","incident_key":key})
            else:
                entry=ledger[key]
                if entry["status"]=="OPEN":
                    entry["last_seen"]=observed_at
                    entry["observations"]+=1
                    events.append({"event":"OBSERVED_EXISTING","incident_key":key})
                else:
                    events.append({"event":"REOPEN_REQUIRES_REVIEW","incident_key":key})
        else:
            for entry in ledger.values():
                if entry["path"]==o["path"] and entry["status"]=="OPEN":
                    # A successful GitHub job is not proof of producer recovery.
                    entry["status"]="AWAITING_PRODUCER_VERIFICATION"
                    entry["last_seen"]=observed_at
                    events.append({"event":"WORKFLOW_GREEN_NOT_CLOSED","incident_key":entry["incident_key"]})
    return sorted(ledger.values(),key=lambda x:x["incident_key"]),events

def main():
    previous=json.loads(Path(sys.argv[1]).read_text())
    observations=[json.loads(line) for line in Path(sys.argv[2]).read_text().splitlines() if line.strip()]
    ledger,events=reconcile(previous,observations,sys.argv[3])
    print(json.dumps({"ledger":ledger,"events":events},indent=2,sort_keys=True))
if __name__=="__main__":
    main()
