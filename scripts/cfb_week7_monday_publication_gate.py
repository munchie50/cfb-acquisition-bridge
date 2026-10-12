"""Bounded Monday saved-source projection, not live source or betting acceptance."""
import argparse, json, re
from pathlib import Path
from cfb_hot_sheet_current_decision_binding_gate import audit as binding, blob
from cfb_week7_accepted_s0_ancestry_audit import ALIASES
from cfb_week7_opening_display_gate import bucket

MORNING_SHA = '6ca663dbf6eb883ededb2155b152aa0941c10a03'
MARKET_SHA = '05e5dd2d49ae9592897014515e1690ba3a784fb9'
DECISION_SHA = '2d1530d038c27db5e3305233cec6add775b8aa0f'
EXECUTION_SHA = '75caee4052e02ea7d2453d1d37fd3866e13ecc07'
SCORECARD_SHA = '6f7650d340bf63f8f93a2b825e35f8b8e41fa80b'
LINEAGE_SHA = 'd80e26c398de48e7a386ad9a627fe44f4111ac45'
COUNTS = dict(zip(['TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY MORNING','SATURDAY AFTERNOON','SATURDAY EVENING/NIGHT','UNRESOLVED KICKOFF'],[2,2,3,3,13,17,22,0]))
MARKER = '## Week 7 Monday afternoon public-board observation — 2026-10-12 13:05 CT'
CYCLE = 'CFB_MARKET_MONITOR_20261012T180232Z'
PREFIX = 'CONSENSUS_UNAVAILABLE; Caesars UNVERIFIED; DraftKings public single-book fallback 13:05 CT — '

def cells(line): return [v.strip() for v in line.strip('|').split('|')]
def pair(game): return tuple(ALIASES.get(v,v) for v in game.split(' @ '))

def rows(sheet):
    section=None; result={}; counts={}
    for line in sheet.splitlines():
        if line.startswith('## '):
            section=line[3:].strip()
            if section in COUNTS:
                if section in counts: raise ValueError('duplicate section')
                counts[section]=0
            continue
        if not line.startswith('| '): continue
        r=cells(line)
        if not re.match(r'^(Tue|Wed|Thu|Fri|Sat) Oct ',r[0]): continue
        if section=='PRIORITY WATCHLIST' and len(r)==4: continue
        if len(r)!=9 or section not in COUNTS: raise ValueError('unsupported governed row')
        key=pair(r[1])
        if len(key)!=2 or key in result: raise ValueError('duplicate/malformed identity')
        if bucket(r[0])!=section: raise ValueError('kickoff/section conflict')
        result[key]=r; counts[section]+=1
    if len(result)!=62 or counts!=COUNTS: raise ValueError('exact 62-game section union required')
    return result

def quote(raw, source_game, display_game):
    # Formatting normalization only. Preserve side-specific values and prices.
    result=re.sub(r'\(([+-]\d+)\)',r'\1',raw)
    for original,display in sorted(zip(source_game.split(' @ '),display_game.split(' @ ')),key=lambda p:-len(p[0])):
        result=result.replace(original,display)
    return result

def audit(sheet, market, decision, execution, scorecard, morning, lineage):
    for content,digest in [(market,MARKET_SHA),(decision,DECISION_SHA),(execution,EXECUTION_SHA),(scorecard,SCORECARD_SHA),(morning,MORNING_SHA),(lineage,LINEAGE_SHA)]:
        if blob(content)!=digest: raise ValueError('unqualified source boundary; new profile required')
    binding(sheet,decision)
    declaration=f'**Canonical inputs:** market {blob(market)}; decision {blob(decision)}; execution {blob(execution)}; scorecard {blob(scorecard)}.'
    if [l for l in sheet.splitlines() if 'Canonical inputs:' in l]!=[declaration]: raise ValueError('four canonical bindings mismatch')
    if '**Cycle:** '+CYCLE not in sheet: raise ValueError('unknown source cycle')
    if 'Monday source-readiness is incomplete' in sheet: raise ValueError('stale Monday readiness statement after successful preflight')
    if 'Monday source-readiness passed; Tuesday candidate generation and acceptance remain separate.' not in sheet:
        raise ValueError('readiness/candidate/acceptance distinction required')
    if 'This is a presentation correction only; quote retrieval remains 13:05 CT' not in sheet:
        raise ValueError('saved quote versus publication clock distinction required')
    decision_headers=[l for l in sheet.splitlines() if l.startswith('**Monday decision state:**')]
    if len(decision_headers)!=1 or '62/62 INCONCLUSIVE' not in decision_headers[0] or 'Retained practical cutoffs remain CUTOFF_AUTHORITY_UNVERIFIED.' not in decision_headers[0]:
        raise ValueError('decision summary or practical-cutoff authority changed')
    prior=rows(morning); current=rows(sheet)
    if set(current)!=set(prior): raise ValueError('directed identity union mismatch')
    census={ (r['away_team'],r['home_team']):r['display'] for r in json.loads(lineage)['rows'] }
    if set(census)!=set(current): raise ValueError('original lineage union mismatch')
    source={}
    body=market.split(MARKER,1)[1]
    for line in body.splitlines():
        if not line.startswith('| ') or ' @ ' not in cells(line)[0]: continue
        r=cells(line)
        if len(r)!=5 or pair(r[0]) in source: raise ValueError('malformed/duplicate source row')
        source[pair(r[0])]=r
    if len(source)!=8: raise ValueError('eight source identities required')
    accepted=conflicts=unavailable=0
    for key,r in current.items():
        p=prior[key]
        if any(r[n]!=p[n] for n in (0,2,7,8)) or r[2]!=census[key]: raise ValueError('frozen/clock/cutoff/execution projection changed')
        expected_market=p[3]; expected_movement=p[4]
        if key in source:
            s=source[key]
            if 'FIELD_DIRECTION_CONFLICT' in s[2]:
                conflicts+=1
                if 'WITHHELD' not in s[3]: raise ValueError('conflict quarantine absent')
                expected_movement+=' Mon 13:05 CT raw DraftKings fields withheld: spread and moneyline favorite directions conflict; morning qualified fallback retained.'
            elif 'IDENTIFIED_SINGLE_BOOK_FALLBACK' in s[2]:
                accepted+=1
                q=quote(s[1],s[0],r[1]); expected_market=PREFIX+q
                expected_movement+=' → Mon 13:05 CT DraftKings: '+q
            else: raise ValueError('unknown quote qualification')
        unavailable+=expected_market.startswith('MONDAY CURRENT QUOTE UNAVAILABLE')
        if r[3]!=expected_market or r[4]!=expected_movement: raise ValueError('market/price/movement/retained observation mismatch')
        if r[5]!='INCONCLUSIVE — Monday afternoon recheck; no actionable state earned': raise ValueError('unearned decision transition')
        pending=('Original FIRST_FROZEN available' if r[2].startswith('FIRST_FROZEN:') else 'Original FIRST_FROZEN excluded; no REFRESH substitution')+'; consensus unavailable; Caesars unverified; material availability/practical access unresolved'
        if r[6]!=pending: raise ValueError('pending qualification projection mismatch')
    if (accepted,conflicts,unavailable)!=(5,3,7): raise ValueError('source classification counts mismatch')
    return {'verdict':'PASS_QUALIFIED_MONDAY_SAVED_PUBLICATION_PROJECTION_ONLY','games':62,'section_counts':COUNTS,'updated_fallbacks':accepted,'withheld_conflicts':conflicts,'monday_quote_unavailable':unavailable,'sheet_blob':blob(sheet),'scope':'saved-source display/current-state fidelity only; no natural run upgrade, live consensus/Caesars/cutoff/EV/betting acceptance; later source boundaries fail closed'}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    names=['sheet','market','decision','execution','scorecard','morning','lineage']
    for n in names:p.add_argument('--'+n,required=True,type=Path)
    a=p.parse_args();print(json.dumps(audit(*(getattr(a,n).read_text() for n in names)),indent=2))
