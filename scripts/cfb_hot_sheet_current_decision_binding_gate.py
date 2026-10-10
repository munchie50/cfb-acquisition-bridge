#!/usr/bin/env python3
"""Current publication source binding; no verdict, source or betting acceptance."""
import argparse, hashlib, json, re
from datetime import datetime, timezone
from pathlib import Path
from cfb_recovery_navigation_reader import read

CURRENT_ROLE = 'CURRENT_HOT_SHEET:'
LEDGER = 'evidence/operational/CFB_DECISION_WAIT_LEDGER.md'

def blob(text):
    b=text.encode()
    return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

def audit(sheet, ledger):
    # A qualified execution reference is optional metadata, not decision authority.
    refs=re.findall(r'^Canonical inputs: market [0-9a-f]{40}; decision ([0-9a-f]{40})(?:; execution [0-9a-f]{40})?\.$',sheet,re.M)
    if len(refs)!=1:
        raise ValueError('unique canonical decision binding required')
    if refs[0]!=blob(ledger):
        raise ValueError('stale current publication: declared decision differs from supplied canonical state')
    if not ledger.strip():
        raise ValueError('empty canonical decision state')
    return {'verdict':'PASS_SUPPLIED_CURRENT_DECISION_BINDING_ONLY','decision_blob':refs[0],
            'scope':'caller must freshly recover canonical state; binding alone does not validate verdicts, freshness, availability or bets'}

def publication(index, ledger, loader, as_of):
    navigation=read(index,as_of)
    pointers=navigation['frontier']['pointers']
    current=[p for p in pointers if p['purpose'].startswith(CURRENT_ROLE)]
    if len(current)!=1:
        raise ValueError('one explicit CURRENT_HOT_SHEET pointer required; no date/name inference')
    pointer=current[0]
    if not re.fullmatch(r'evidence/operational/CFB_WEEK\d{1,2}_HOT_SHEET_\d{4}-\d{2}-\d{2}_\d{4}CT\.md',pointer['path']):
        raise ValueError('unsupported current publication path')
    states=[p for p in pointers if p['path']==LEDGER]
    if len(states)!=1 or states[0]['blob']!=blob(ledger):
        raise ValueError('recovery canonical decision pointer is stale or missing')
    sheet=loader(pointer['path'])
    if blob(sheet)!=pointer['blob']:
        raise ValueError('current publication bytes differ from recovery pointer')
    result=audit(sheet,ledger)
    return {**result,'sheet_path':pointer['path'],'sheet_blob':pointer['blob'],
            'navigation_index_blob':navigation['index_blob']}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    source=p.add_mutually_exclusive_group(required=True)
    source.add_argument('--sheet',type=Path)
    source.add_argument('--index',type=Path)
    p.add_argument('--current-ledger',required=True,type=Path)
    p.add_argument('--repository-root',type=Path,default=Path('.'))
    p.add_argument('--as-of',default=None)
    a=p.parse_args()
    ledger=a.current_ledger.read_bytes().decode()
    if a.sheet:
        result=audit(a.sheet.read_bytes().decode(),ledger)
    else:
        root=a.repository_root.resolve()
        def loader(path):
            resolved=(root/path).resolve()
            if not resolved.is_relative_to(root):
                raise ValueError('publication path escapes repository')
            return resolved.read_bytes().decode()
        at=a.as_of or datetime.now(timezone.utc).isoformat()
        result=publication(a.index.read_bytes().decode(),ledger,loader,at)
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
