#!/usr/bin/env python3
"""Extract explicitly dated navigation checkpoints; never certify their claims."""
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

TAG = 'cfb-frontier-json'
SCHEMA = 'CFB_RECOVERY_NAVIGATION_FRONTIER_V1'

def unique(pairs):
    out = {}
    for k,v in pairs:
        if k in out: raise ValueError('duplicate JSON key')
        out[k]=v
    return out

def clock(value):
    if not isinstance(value,str): raise ValueError('invalid timestamp')
    d=datetime.fromisoformat(value.replace('Z','+00:00'))
    if d.tzinfo is None: raise ValueError('timezone required')
    return d.astimezone(timezone.utc)

def read(text, as_of):
    now=clock(as_of)
    markers=re.findall(r'^```'+TAG+r'[ \t]*\r?$',text,re.M)
    matches=list(re.finditer(r'^```'+TAG+r'[ \t]*\r?\n(.*?)^```[ \t]*\r?$',text,re.M|re.S))
    bodies=[match.group(1) for match in matches]
    if not bodies or len(bodies)!=len(markers): raise ValueError('missing or incomplete explicit navigation checkpoint')
    # The writer must reconcile every later append into a new checkpoint.
    # Never guess whether uncheckpointed prose is material or still current.
    if text[matches[-1].end():].strip():
        raise ValueError('uncheckpointed trailing content; inspect complete index and append a reconciled checkpoint')
    prior=None
    records=[]
    for body in bodies:
        r=json.loads(body,object_pairs_hook=unique)
        if not isinstance(r,dict) or set(r)!={'schema','as_of_utc','scope','claims','pointers'}:
            raise ValueError('unsupported checkpoint fields')
        if r['schema']!=SCHEMA or r['scope']!='NAVIGATION_ONLY_NOT_AUTHORITY':
            raise ValueError('unsupported checkpoint authority/schema')
        at=clock(r['as_of_utc'])
        if at>now or (prior is not None and at<=prior):
            raise ValueError('future, duplicate or reversed checkpoint clock')
        prior=at
        if not isinstance(r['claims'],list) or not r['claims'] or any(not isinstance(s,str) or not s.strip() for s in r['claims']):
            raise ValueError('invalid navigation claims')
        if not isinstance(r['pointers'],list) or not r['pointers']: raise ValueError('empty pointers')
        paths=[]
        for p in r['pointers']:
            if not isinstance(p,dict) or set(p)!={'path','blob','purpose'}: raise ValueError('invalid pointer fields')
            if not isinstance(p['path'],str) or not re.fullmatch(r'evidence/[A-Za-z0-9_./-]+',p['path']) or '..' in p['path'].split('/'):
                raise ValueError('invalid repository pointer path')
            if not isinstance(p['blob'],str) or not re.fullmatch(r'[0-9a-f]{40}',p['blob']): raise ValueError('invalid blob identity')
            if not isinstance(p['purpose'],str) or not p['purpose'].strip(): raise ValueError('missing pointer purpose')
            paths.append(p['path'])
        if len(set(paths))!=len(paths): raise ValueError('duplicate pointer path')
        records.append(r)
    raw=text.encode('utf-8')
    return {'status':'NAVIGATION_ONLY_NOT_AUTHORITY','checkpoint_count':len(records),'frontier':records[-1],
            'index_blob':hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest(),
            'age_seconds':(now-prior).total_seconds(),'pointer_readback':'NOT_PERFORMED',
            'limitations':['Recover full detailed authority; verify each applicable pointer independently before reliance.',
                           'Declared checkpoint clock orders navigation records only; claims are not certified.',
                           'Later material state changes require reconciliation; this is explicitly as-of state, not a live feed.',
                           'Trailing content after the last checkpoint is rejected; this does not certify intervening claims.',
                           'Old untagged summaries are historical context, not reader-selected current checkpoints.']}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--index',required=True,type=Path)
    p.add_argument('--as-of',required=True)
    a=p.parse_args()
    print(json.dumps(read(a.index.read_text(),a.as_of),indent=2))

if __name__=='__main__':main()

