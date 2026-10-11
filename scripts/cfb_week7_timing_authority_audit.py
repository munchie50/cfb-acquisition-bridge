#!/usr/bin/env python3
"""Read-only exact Week7 timing exception audit; NO clock authority acceptance."""
import argparse,json,re
from collections import Counter
from datetime import datetime,timedelta
from pathlib import Path
from zoneinfo import ZoneInfo
from cfb_hot_sheet_current_decision_binding_gate import audit as binding,blob
from cfb_week7_opening_display_gate import bucket,cells
CT=ZoneInfo('America/Chicago')
CADENCE='63ec14c167dfb4c64fb845ebd862f6aac588e487'
CYCLE='CFB_MARKET_MONITOR_20261011T180208Z'
LEDGER='4a525667b6ecfbeaf6e74222d18640e91e5d35f2'
SECTIONS={'TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY MORNING','SATURDAY AFTERNOON','SATURDAY EVENING/NIGHT'}
def clock(value):
    m=re.fullmatch(r'(Tue|Wed|Thu|Fri|Sat) Oct (\d{2}) (\d{1,2}):(\d{2}) (AM|PM) CT',value)
    if not m:raise ValueError('unsupported saved clock')
    day,d,h,mn,half=m.groups()
    if not 13<=int(d)<=17 or not 1<=int(h)<=12 or not 0<=int(mn)<60:raise ValueError('invalid saved clock')
    result=datetime(2026,10,int(d),int(h)%12+(12 if half=='PM' else 0),int(mn),tzinfo=CT)
    if result.strftime('%a')!=day:raise ValueError('saved weekday mismatch')
    return result
def audit(sheet,ledger,cadence,sectioning,as_of):
    binding(sheet,ledger)
    if blob(cadence)!=CADENCE or blob(ledger)!=LEDGER:raise ValueError('unqualified cadence/decision boundary')
    if '**Cycle:** '+CYCLE not in sheet:raise ValueError('unqualified sheet cycle')
    if '## 2026-10-04 prospective football-week day coverage correction' not in sectioning or 'Tuesday/Wednesday games require a realistic pre-kickoff reconciliation deadline and final practical execution cutoff' not in sectioning:
        raise ValueError('missing early-week authority ancestry')
    at=datetime.fromisoformat(as_of.replace('Z','+00:00'))
    if at.tzinfo is None:raise ValueError('explicit as-of timezone required')
    at=at.astimezone(CT);rows=[];section=None;seen=set()
    for line in sheet.splitlines():
        if line.startswith('## '):section=line[3:].strip();continue
        if not re.match(r'^\| (Tue|Wed|Thu|Fri|Sat) Oct ',line):continue
        r=cells(line)
        if section=='PRIORITY WATCHLIST' and len(r)==4:continue
        if section not in SECTIONS or len(r)!=9 or r[1] in seen or bucket(r[0])!=section:
            raise ValueError('invalid timing population/section')
        seen.add(r[1]);kickoff=clock(r[0])
        parts=r[7].split('; final cutoff ')
        if len(parts)!=2:raise ValueError('saved deadline/cutoff pair required')
        deadline,cutoff=map(clock,parts)
        if deadline>=kickoff or cutoff>=kickoff or deadline>cutoff:raise ValueError('invalid saved clock ordering')
        if section in {'TUESDAY','WEDNESDAY'}:
            classification='GAME_SPECIFIC_ASSIGNED_NOT_INDEPENDENTLY_QUALIFIED'
        elif section=='THURSDAY':
            expected=kickoff.replace(hour=13,minute=0)
            classification='DEFAULT_MATCH_CONDITIONAL_ON_PRACTICAL_ACCESS' if deadline==expected else 'EARLIER_OR_DIFFERENT_CLOCK_REQUIRES_PROVENANCE'
        elif section=='SATURDAY MORNING':
            classification='NOMINAL_FLEXIBLE_EVENT_TIME_NOT_COMPLETION_DEADLINE'
        else:
            hour=7 if section=='SATURDAY AFTERNOON' else 13
            expected=kickoff.replace(hour=hour,minute=0)
            classification='EXPLICIT_DEFAULT_CLOCK_MATCH_ONLY' if deadline==expected else 'EARLIER_OR_DIFFERENT_CLOCK_REQUIRES_PROVENANCE'
        rows.append({'game':r[1],'section':section,'saved_kickoff_ct':kickoff.isoformat(),
                     'saved_reconciliation_ct':deadline.isoformat(),'deadline_class':classification,
                     'saved_default_clock_status':'FUTURE' if at<deadline else 'SAVED_CLOCK_REACHED_NOT_EFFECTIVE_DEADLINE_CERTIFICATION',
                     'saved_cutoff_ct':cutoff.isoformat(),'cutoff_minutes_before_saved_kickoff':int((kickoff-cutoff).total_seconds()/60),
                     'cutoff_authority':'UNVERIFIED_NO_INDEPENDENT_PRACTICAL_CONSTRAINT_SUPPLIED',
                     'effective_game_deadline':'NOT_CERTIFIED',
                     'decision_state':r[5]})
    if len(rows)!=62 or len(seen)!=62:raise ValueError('expected qualified62 unique timing rows')
    return {'status':'TIMING_AUTHORITY_UNRESOLVED_NOT_OPERATIONAL_ACCEPTANCE','as_of_ct':at.isoformat(),
            'scope':'saved-clock comparison against recovered rules only; no source/access/cutoff qualification, overdue decision, recommendation or new clock',
            'source_blobs':{'sheet':blob(sheet),'ledger':blob(ledger),'cadence':blob(cadence),'sectioning':blob(sectioning)},
            'counts':{'games':len(rows),'deadline_class':dict(Counter(r['deadline_class'] for r in rows)),
                      'saved_clock_status':dict(Counter(r['saved_default_clock_status'] for r in rows)),
                      'cutoffs_60_minutes_before_saved_kickoff':sum(r['cutoff_minutes_before_saved_kickoff']==60 for r in rows),
                      'independently_qualified_cutoffs':0},'rows':rows}
def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ['sheet','ledger','cadence','sectioning']:p.add_argument('--'+name,required=True,type=Path)
    p.add_argument('--as-of',required=True);a=p.parse_args()
    print(json.dumps(audit(*(getattr(a,n).read_bytes().decode() for n in ['sheet','ledger','cadence','sectioning']),a.as_of),indent=2))
if __name__=='__main__':main()
