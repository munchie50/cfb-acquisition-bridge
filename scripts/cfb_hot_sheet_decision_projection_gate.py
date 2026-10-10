#!/usr/bin/env python3
"""Check the scoped dinner decision projection, not quote truth or bet acceptance."""
import argparse
import hashlib
import re
import json
import subprocess
from pathlib import Path
from cfb_full_review_scope_gate import check, expected_games, review_rows, cells

MARKER='## October 9 19:53:50 CT — full Saturday dinner review'

def blob(text):
    b=text.encode();return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

def decisions(ledger,expected):
    if ledger.count(MARKER)!=1:raise ValueError('unsupported decision boundary')
    body=ledger.split(MARKER)[1]
    if re.search(r'^## ',body,re.M):raise ValueError('later decision block requires qualification')
    rows=[cells(l) for l in body.splitlines() if l.startswith('| ') and len(cells(l))==3 and cells(l)[0] in expected]
    if len(rows)!=38 or len({r[0] for r in rows})!=38:raise ValueError('canonical decision coverage mismatch')
    return {r[0]:(r[1],r[2]) for r in rows}

def cutoffs(review):
    rows=[cells(l) for l in review.splitlines() if l.startswith('| Sat') and len(cells(l))==7]
    result={}
    for r in rows:
        match=re.fullmatch(r'(.+) ([+-]\d+(?:\.\d+)?)',r[1])
        if not match or not re.fullmatch(r'-\d+',r[5]):raise ValueError('unsupported recommendation cutoff')
        team=match[1]
        if team in result:raise ValueError('duplicate recommendation selection')
        result[team]={'selection':r[1],'line':r[4],'price':r[5]}
    if len(result)!=3:raise ValueError('supported three recommendation card required')
    return result

def audit(sheet,baseline,review,ledger):
    expected=expected_games(baseline);check(expected,review)
    binding=re.findall(r'^Canonical inputs: market [0-9a-f]{40}; decision ([0-9a-f]{40})\.$',sheet,re.M)
    if binding!=[blob(ledger)]:raise ValueError('sheet canonical decision binding mismatch')
    canonical=decisions(ledger,set(expected))
    observed={r[1]:(r[6],r[7]) for r in review_rows(review)}
    if canonical!=observed:raise ValueError('review differs from canonical decisions')
    published=[cells(l) for l in sheet.splitlines() if l.startswith('| Sat')]
    if len(published)!=38 or any(len(r)!=9 for r in published) or len({r[1] for r in published})!=38:
        raise ValueError('published Saturday identity/schema mismatch')
    if {r[1] for r in published}!=set(expected):raise ValueError('published identity union mismatch')
    cuts=cutoffs(review);matched=0
    current_body=ledger.split(MARKER)[1]
    caps=re.findall(r'each maximum (-\d+)',current_body)
    if len(caps)!=1:raise ValueError('canonical maximum price missing/ambiguous')
    for c in cuts.values():
        number=c['selection'].rsplit(' ',1)[1]
        if c['selection']+' or better' not in current_body or c['line']!=number+' or better' or c['price']!=caps[0]:
            raise ValueError('review cutoff differs from canonical decision')
    aliases={'Massachusetts':'UMass'}
    for r in published:
        side,total=canonical[r[1]]
        if r[5]!=side+' / TOTAL '+total:raise ValueError('stale or changed published decision: '+r[1])
        if side.startswith('BET NOW CONDITIONAL'):
            teams=[aliases.get(t,t) for t in re.split(r' @ | vs ',r[1])]
            choices=[cuts[t] for t in teams if t in cuts]
            if len(choices)!=1:raise ValueError('recommendation identity mismatch')
            c=choices[0]
            if r[8]!=c['line']+'; max '+c['price']+'; tonight before kickoff; actual Caesars check':
                raise ValueError('published cutoff changed')
            if 'Caesars offer UNVERIFIED' not in r[6]:raise ValueError('execution qualifier missing')
            matched+=1
        elif r[8]!='None / PASS':raise ValueError('PASS has invented execution window')
    if matched!=3:raise ValueError('conditional recommendation count mismatch')
    if 'NO NEW MARKET RETRIEVAL' not in sheet or 'Underlying quote retrieval remains approximately 13:02 CT' not in sheet:
        raise ValueError('retained quote age not explicit')
    return {'verdict':'PASS_CURRENT_SCOPED_DECISION_PROJECTION','matched_games':38,'matched_market_verdicts':76,
            'matched_conditional_cutoffs':3,'decision_blob':blob(ledger),'sheet_blob':blob(sheet),
            'scope':'saved decision/cutoff display only; market/source/availability/betting acceptance unverified'}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ['sheet','baseline','review']:p.add_argument('--'+k,required=True,type=Path)
    p.add_argument('--ledger',type=Path,help='exact declared source snapshot; otherwise recover canonical Git history')
    a=p.parse_args()
    sheet=a.sheet.read_bytes().decode()
    if a.ledger:
        ledger=a.ledger.read_bytes().decode()
    else:
        refs=re.findall(r'^Canonical inputs: market [0-9a-f]{40}; decision ([0-9a-f]{40})\.$',sheet,re.M)
        if len(refs)!=1:raise ValueError('unique source binding required')
        path='evidence/operational/CFB_DECISION_WAIT_LEDGER.md'
        objects=subprocess.run(['git','rev-list','--objects','--all','--',path],check=True,capture_output=True,text=True).stdout.splitlines()
        if refs[0]+' '+path not in objects:raise ValueError('decision blob not recovered at canonical Git path')
        ledger=subprocess.run(['git','cat-file','blob',refs[0]],check=True,capture_output=True).stdout.decode()
    print(json.dumps(audit(sheet,a.baseline.read_bytes().decode(),a.review.read_bytes().decode(),ledger),indent=2))

if __name__=='__main__':main()
