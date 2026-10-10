#!/usr/bin/env python3
"""Bind a current publication to supplied freshly recovered canonical decision bytes."""
import argparse, hashlib, json, re
from pathlib import Path

def blob(text):
    b=text.encode()
    return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

def audit(sheet, ledger):
    refs=re.findall(r'^Canonical inputs: market [0-9a-f]{40}; decision ([0-9a-f]{40})\.$',sheet,re.M)
    if len(refs)!=1:
        raise ValueError('unique canonical decision binding required')
    if refs[0]!=blob(ledger):
        raise ValueError('stale current publication: declared decision differs from supplied canonical state')
    if not ledger.strip():
        raise ValueError('empty canonical decision state')
    return {'verdict':'PASS_SUPPLIED_CURRENT_DECISION_BINDING_ONLY','decision_blob':refs[0],
            'scope':'caller must freshly recover canonical state; binding alone does not validate verdicts, freshness, availability or bets'}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--sheet',required=True,type=Path)
    p.add_argument('--current-ledger',required=True,type=Path)
    a=p.parse_args()
    print(json.dumps(audit(a.sheet.read_bytes().decode(),a.current_ledger.read_bytes().decode()),indent=2))
if __name__=='__main__':
    main()
