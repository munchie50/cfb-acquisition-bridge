#!/usr/bin/env python3
"""Qualified Oct11 afternoon saved projection; external authority and bets NOT certified."""
import argparse,json,re
from pathlib import Path
import cfb_week7_opening_display_gate as opening
from cfb_hot_sheet_current_decision_binding_gate import audit as binding,blob

CYCLE='CFB_MARKET_MONITOR_20261011T180208Z'
MARKET='## Week 7 afternoon board refresh — 2026-10-11 13:05 CT'
DECISION='## Week 7 afternoon decision reconciliation — 2026-10-11 13:05 CT'
OLD_MARKET='444d42107c646c379b2b51ac643460f3123ea9e6'
OLD_DECISION='4c6b3468f0e0839ce85be0c96a5e9498b94d692a'
COUNTS={**opening.COUNTS,'SATURDAY AFTERNOON':17,'SATURDAY EVENING/NIGHT':22}
PREFIX='CONSENSUS_UNAVAILABLE; Caesars UNVERIFIED; CBS mixed-book fallback 13:05 CT — '
OLD_PREFIX=PREFIX.replace('13:05','07:08')
def body(text,marker):
    if text.count(marker)!=1:raise ValueError('unsupported afternoon source boundary')
    value=text.split(marker,1)[1]
    if re.search(r'^## ',value,re.M) or '**Cycle:** '+CYCLE not in value:
        raise ValueError('later/mismatched source requires qualification')
    return value
def audit(sheet,market,decision,morning_market,morning_decision,execution,scorecard):
    binding(sheet,decision)
    refs=re.findall(r'^\*\*Canonical inputs:\*\* market ([0-9a-f]{40}); decision ([0-9a-f]{40}); execution ([0-9a-f]{40}); scorecard ([0-9a-f]{40})\.$',sheet,re.M)
    if refs!=[(blob(market),blob(decision),blob(execution),blob(scorecard))]:
        raise ValueError('four canonical source bindings mismatch')
    if blob(morning_market)!=OLD_MARKET or blob(morning_decision)!=OLD_DECISION:
        raise ValueError('immutable morning source identities mismatch')
    if not market.startswith(morning_market) or not decision.startswith(morning_decision):
        raise ValueError('prior observation/decision bytes rewritten')
    if '**Cycle:** '+CYCLE not in sheet or '**Status:** AFTERNOON MARKET REFRESH / PRE-FREEZE' not in sheet:
        raise ValueError('unsupported afternoon sheet phase')
    old=opening.source_rows(morning_market,opening.MARKET,5)
    dr=opening.source_rows(morning_decision,opening.DECISION,8)
    mr={}
    for line in body(market,MARKET).splitlines():
        if not re.match(r'^\| (Tue|Wed|Thu|Fri|Sat) Oct ',line):continue
        row=opening.cells(line)
        if len(row)!=6 or row[1] in mr:raise ValueError('duplicate/malformed afternoon source row')
        mr[row[1]]=row
    if set(mr)!=set(old) or set(dr)!=set(old):raise ValueError('source identity union mismatch')
    corrections=[opening.cells(l) for l in body(decision,DECISION).splitlines() if l.startswith('| Nebraska @ Oregon |')]
    if len(corrections)!=1 or len(corrections[0])!=8:raise ValueError('unique Nebraska correction required')
    c=corrections[0]
    if c[1]!='Sat Oct 17 2:00 PM CT (07:08 capture; now superseded prospectively)' or c[2]!='Sat Oct 17 10:00 PM CT — Oregon athletics announcement, 8:00 PM PT on FOX' or c[3]!='INCONCLUSIVE' or c[5]!='Sat Oct 17 1:00 PM CT' or c[6]!='Sat Oct 17 9:00 PM CT' or c[7]!='Not established; no execution before inputs are earned':
        raise ValueError('unqualified kickoff/decision correction')
    rows={};section=None;counts={};first=changed=0
    for line in sheet.splitlines():
        if line.startswith('## '):
            section=line[3:].strip()
            if section in COUNTS:
                if section in counts:raise ValueError('duplicate section')
                counts[section]=0
            continue
        if not re.match(r'^\| (Tue|Wed|Thu|Fri|Sat) Oct ',line):continue
        r=opening.cells(line)
        if section not in COUNTS:
            if section=='PRIORITY WATCHLIST' and len(r)==4:continue
            raise ValueError('unsectioned game row')
        if len(r)!=9 or r[1] in rows or r[1] not in mr:raise ValueError('duplicate/malformed/unknown game')
        g=r[1];o=old[g];m=mr[g];d=dr[g]
        kickoff='Sat Oct 17 10:00 PM CT' if g=='Nebraska @ Oregon' else o[0]
        if r[0]!=kickoff or m[0]!=kickoff or opening.bucket(kickoff)!=section:
            raise ValueError('saved kickoff/section mismatch')
        if r[2]!='NOT YET EARNED — Week 7 Monday readiness pending; Tuesday candidate is not acceptance':
            raise ValueError('invented model prediction')
        if r[3]!=m[2] or not m[2].startswith(PREFIX):
            raise ValueError('quote or source-role mismatch')
        quote=m[2][len(PREFIX):]
        unavailable=o[2]=='CONSENSUS_UNAVAILABLE; Caesars UNVERIFIED; CBS fallback unavailable'
        if unavailable:
            first+=1
            movement='07:08 CT unavailable → first qualified price observation 13:05 CT: '+quote
            source_movement='First qualified price observation at 13:05 CT; 07:08 CT board was unavailable.'
        else:
            if not o[2].startswith(OLD_PREFIX):raise ValueError('unknown original quote profile')
            old_quote=o[2][len(OLD_PREFIX):]
            changed+=int(old_quote!=quote)
            movement='07:08 CT first: '+old_quote+' → 13:05 CT current: '+quote
            source_movement='Movement from 07:08 CT first qualified observation: '+old_quote+' → '+quote+'.'
        if r[4]!=movement or m[3]!=source_movement:
            raise ValueError('first observation/movement chronology mismatch')
        if m[4]!='Displayed and available on CBS board; constituent books unidentified, so not consensus and not a verified Caesars offer' or m[5]!='https://www.cbssports.com/college-football/odds/FBS/2026/regular/week-7/':
            raise ValueError('source provenance/qualification mismatch')
        if d[2]!='INCONCLUSIVE' or r[5]!='INCONCLUSIVE — pre-freeze afternoon refresh':
            raise ValueError('unearned decision')
        deadline=c[5] if g=='Nebraska @ Oregon' else d[4]
        cutoff=c[6] if g=='Nebraska @ Oregon' else d[5]
        if r[7]!=deadline+'; final cutoff '+cutoff:raise ValueError('saved deadline/cutoff mismatch')
        pending='Accepted frozen snapshot not earned; consensus unavailable; Caesars unverified'
        if g=='Nebraska @ Oregon':pending+='; authoritative kickoff corrected to 10:00 PM CT'
        if r[6]!=pending:
            raise ValueError('pending qualification missing')
        if d[6]!='Not established' or r[8]!='Not established; no execution before accepted frozen prediction and qualified offer':
            raise ValueError('execution number/window invented')
        rows[g]=r;counts[section]+=1
    if set(rows)!=set(old) or counts!=COUNTS or first!=28 or changed!=34:
        raise ValueError('identity/count/movement population mismatch')
    return {'verdict':'PASS_QUALIFIED_WEEK7_SUNDAY_AFTERNOON_DISPLAY','games':62,'section_counts':counts,
            'first_price_observations':first,'changed_existing_quotes':changed,
            'sheet_blob':blob(sheet),'market_blob':blob(market),'decision_blob':blob(decision),
            'scope':'saved projection/immutable first-observation chronology only; external source/kickoff/deadline authority, model, cash and execution NOT certified'}
def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ['sheet','market','decision','morning-market','morning-decision','execution','scorecard']:
        p.add_argument('--'+name,required=True,type=Path)
    a=p.parse_args()
    print(json.dumps(audit(*(getattr(a,n.replace('-','_')).read_bytes().decode() for n in ['sheet','market','decision','morning-market','morning-decision','execution','scorecard'])),indent=2))
if __name__=='__main__':main()
