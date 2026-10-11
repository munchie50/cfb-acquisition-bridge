#!/usr/bin/env python3
"""Exact Week7 Sunday pre-freeze projection; not source truth or betting acceptance."""
import argparse, json, re
from datetime import datetime
from pathlib import Path
from cfb_hot_sheet_current_decision_binding_gate import audit as binding, blob

CYCLE='CFB_MARKET_MONITOR_20261011T120436Z'
MARKET='## Week 7 Sunday opening-board capture — 2026-10-11 07:08 CT'
DECISION='## Week 7 Sunday opening decision capture — 2026-10-11 07:08 CT'
COUNTS={'TUESDAY':2,'WEDNESDAY':2,'THURSDAY':3,'FRIDAY':3,'SATURDAY MORNING':13,'SATURDAY AFTERNOON':18,'SATURDAY EVENING/NIGHT':21}
def cells(line): return [c.strip() for c in line.strip().strip('|').split('|')]
def block(text,marker):
    if text.count(marker)!=1: raise ValueError('unsupported opening source boundary')
    body=text.split(marker,1)[1]
    if re.search(r'^## ',body,re.M) or '**Cycle:** '+CYCLE not in body:
        raise ValueError('later/mismatched source boundary requires qualification')
    return body
def source_rows(text, marker, n):
    rows={}
    for line in block(text,marker).splitlines():
        if not re.match(r'^\| (Tue|Wed|Thu|Fri|Sat) Oct ',line): continue
        r=cells(line)
        if len(r)!=n or r[1] in rows: raise ValueError('duplicate or malformed source row')
        rows[r[1]]=r
    if len(rows)!=62: raise ValueError('opening source population mismatch')
    return rows
def bucket(clock):
    match=re.fullmatch(r'(Tue|Wed|Thu|Fri|Sat) Oct (\d{2}) (\d{1,2}):(\d{2}) (AM|PM) CT',clock)
    if not match: raise ValueError('unsupported kickoff display')
    day,date,h,m,half=match.groups()
    if not 1<=int(h)<=12 or not 0<=int(m)<=59: raise ValueError('invalid kickoff clock')
    if datetime(2026,10,int(date)).strftime('%a')!=day or not 13<=int(date)<=17: raise ValueError('weekday/date mismatch')
    hour=int(h)%12+(12 if half=='PM' else 0)
    if day=='Sat': return 'SATURDAY MORNING' if hour<12 else 'SATURDAY AFTERNOON' if hour<17 else 'SATURDAY EVENING/NIGHT'
    return {'Tue':'TUESDAY','Wed':'WEDNESDAY','Thu':'THURSDAY','Fri':'FRIDAY'}[day]
def audit(sheet,market,decision):
    binding(sheet,decision)
    refs=re.findall(r'^Canonical inputs: market ([0-9a-f]{40}); decision [0-9a-f]{40}\.$',sheet,re.M)
    if refs!=[blob(market)]: raise ValueError('market source binding mismatch')
    if '**Cycle:** '+CYCLE not in sheet or '**Status:** OPENING-BOARD CAPTURE / PRE-FREEZE' not in sheet:
        raise ValueError('unsupported sheet phase/cycle')
    mr=source_rows(market,MARKET,5);dr=source_rows(decision,DECISION,8)
    if set(mr)!=set(dr): raise ValueError('market/decision identity union mismatch')
    rows={};section=None;counts={}
    for line in sheet.splitlines():
        if line.startswith('## '):
            section=line[3:].strip()
            if section in COUNTS:
                if section in counts: raise ValueError('duplicate kickoff section')
                counts[section]=0
            continue
        if not re.match(r'^\| (Tue|Wed|Thu|Fri|Sat) Oct ',line): continue
        r=cells(line)
        # Separate priority views are not the canonical kickoff population.
        if section not in COUNTS:
            if section=='PRIORITY WATCHLIST' and len(r)==4: continue
            raise ValueError('unsectioned opening game row')
        if len(r)!=9 or r[1] in rows: raise ValueError('duplicate or malformed display row')
        if bucket(r[0])!=section: raise ValueError('kickoff/section conflict')
        if r[1] not in mr or r[0]!=mr[r[1]][0] or r[0]!=dr[r[1]][0]: raise ValueError('game/kickoff source mismatch')
        if r[2]!='NOT YET EARNED — Week 7 Monday readiness pending; Tuesday candidate is not acceptance':
            raise ValueError('pre-freeze model opinion invented or changed')
        if r[3]!=mr[r[1]][2]: raise ValueError('market quote/availability display mismatch')
        if 'CONSENSUS_UNAVAILABLE; Caesars UNVERIFIED;' not in r[3]: raise ValueError('source roles missing')
        unavailable = mr[r[1]][2]=='CONSENSUS_UNAVAILABLE; Caesars UNVERIFIED; CBS fallback unavailable'
        if unavailable and mr[r[1]][3]!='spread —; total —': raise ValueError('unavailable source has invented open reference')
        wanted = 'No qualified observation; CBS showed no market' if unavailable else 'First qualified observation; movement 0. Source-displayed Open reference: '+mr[r[1]][3]
        if r[4]!=wanted:
            raise ValueError('opening/movement reference changed')
        if dr[r[1]][2]!='INCONCLUSIVE' or r[5]!='INCONCLUSIVE — pre-freeze opening capture':
            raise ValueError('unearned or stale opening decision')
        if r[7]!=dr[r[1]][4]+'; final cutoff '+dr[r[1]][5]: raise ValueError('saved deadline/cutoff display mismatch')
        if dr[r[1]][6]!='Not established' or r[8]!='Not established; no execution before accepted frozen prediction and qualified offer':
            raise ValueError('opening execution number/window invented')
        if r[6]!='Accepted frozen snapshot not yet earned; consensus unavailable; Caesars unverified':
            raise ValueError('missing opening pending qualifiers')
        rows[r[1]]=r;counts[section]+=1
    if len(rows)!=62 or set(rows)!=set(mr) or counts!=COUNTS: raise ValueError('opening displayed identity/count mismatch')
    if len([g for g in rows if 'Nebraska' in g.split(' @ ')])!=1: raise ValueError('mandatory Nebraska inclusion missing')
    return {'verdict':'PASS_QUALIFIED_WEEK7_SUNDAY_PREFREEZE_DISPLAY','games':62,'section_counts':counts,
            'market_blob':blob(market),'decision_blob':blob(decision),'sheet_blob':blob(sheet),
            'scope':'exact canonical projection, clock buckets and no-invented-model/execution display; schedule/source/deadline authority, predictions and bets NOT certified'}
def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ['sheet','market','decision']: p.add_argument('--'+name,required=True,type=Path)
    a=p.parse_args()
    print(json.dumps(audit(a.sheet.read_bytes().decode(),a.market.read_bytes().decode(),a.decision.read_bytes().decode()),indent=2))
if __name__=='__main__':main()
