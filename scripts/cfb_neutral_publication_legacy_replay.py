"""Authentic Oct12 saved-input normalization for QA only; never canonical writer."""
import argparse,copy,json,re,subprocess
from datetime import datetime
from pathlib import Path
from cfb_hot_sheet_current_decision_binding_gate import blob
from cfb_week7_accepted_s0_ancestry_audit import ALIASES
import cfb_neutral_publication_gate as gate

MARKET_SHA='05e5dd2d49ae9592897014515e1690ba3a784fb9'
DECISION_SHA='2d1530d038c27db5e3305233cec6add775b8aa0f'
AT='2026-10-12T18:05:00Z'
CYCLE='CFB_MARKET_MONITOR_20261012T180232Z'
CBS='https://www.cbssports.com/college-football/odds/FBS/2026/regular/week-7/'
DK='https://sportsbook.draftkings.com/leagues/football/ncaaf'
def historical(path,digest):
    path=Path(path).resolve()
    raw=path.read_text()
    if blob(raw)==digest:return raw
    # Match the immutable blob at its canonical Git history path before reading.
    # Git prints repository-relative object names even for an absolute pathspec.
    # Qualify both the history query and comparison in that same namespace.
    try:
        root=Path(subprocess.run(['git','-C',str(path.parent),'rev-parse','--show-toplevel'],
                                check=True,capture_output=True,text=True).stdout.strip()).resolve()
        canonical=path.relative_to(root).as_posix()
        objects=subprocess.run(['git','-C',str(root),'rev-list','--objects','--all','--',canonical],
                               check=True,capture_output=True,text=True).stdout.splitlines()
    except (subprocess.CalledProcessError,ValueError) as exc:
        raise ValueError('historical canonical source ancestry not recovered') from exc
    if digest+' '+canonical not in objects:raise ValueError('historical canonical source ancestry not recovered')
    result=subprocess.run(['git','-C',str(root),'cat-file','blob',digest],check=True,capture_output=True).stdout.decode()
    if blob(result)!=digest:raise ValueError('historical blob mismatch')
    return result
def cells(l):return [v.strip() for v in l.strip('|').split('|')]
def pair(g):return tuple(ALIASES.get(v,v) for v in g.split(' @ '))
def block(s,label):
    m=re.search(r'^## '+re.escape(label)+r'.*$',s,re.M)
    if not m:raise ValueError('missing saved source block')
    return s[m.end():].split('\n## ',1)[0]
def table(s,label,n):
    result={}
    for l in block(s,label).splitlines():
        if not re.match(r'^\| (Tue|Wed|Thu|Fri|Sat) Oct ',l):continue
        r=cells(l)
        if len(r)!=n or pair(r[1]) in result:raise ValueError('invalid saved source table')
        result[pair(r[1])]=r
    if len(result)!=62:raise ValueError('saved source population mismatch')
    return result
def iso(s):return datetime.strptime(s[:-3]+' 2026','%a %b %d %I:%M %p %Y').replace(tzinfo=gate.CT).astimezone(gate.timezone.utc).isoformat().replace('+00:00','Z')
def parse_quote(raw,at,book,provenance,precision):
    raw=raw.split(' — ',1)[-1];raw=re.sub(r'\(([+-]\d+)\)',r'\1',raw)
    parts=raw.split('; ')
    if len(parts)!=3:raise ValueError('unsupported authentic quote '+raw)
    def side(s):
        q=re.fullmatch(r'.+? (—|[+-]?\d+(?:\.\d+)? [+-]\d+), ML (—|[+-]\d+)',s)
        if not q:raise ValueError('unsupported partial side '+s)
        line,ml=q.groups();n,p=(None,None) if line=='—' else line.split(' ')
        return float(n) if n is not None else None,int(p) if p is not None else None,int(ml) if ml!='—' else None
    a,ap,am=side(parts[0]);h,hp,hm=side(parts[1])
    if parts[2]=='— / —':o=op=u=up=None
    else:
        t=re.fullmatch(r'o(\d+(?:\.\d+)?) ([+-]\d+) / u(\d+(?:\.\d+)?) ([+-]\d+)',parts[2])
        if not t:raise ValueError('unsupported total '+parts[2])
        o,op,u,up=t.groups();o=float(o);op=int(op);u=float(u);up=int(up)
    if all(v is None for v in [a,ap,am,h,hp,hm,o,op,u,up]):return None
    event=re.search(r'event (\d+)',provenance)
    return {'book':book,'source_type':'IDENTIFIED_SINGLE_BOOK_FALLBACK' if book=='DraftKings' else 'UNIDENTIFIED_MIXED_BOOK_FALLBACK','source_url':DK if book=='DraftKings' else CBS,'event_id':event.group(1) if event else 'EVENT_ID_UNAVAILABLE','retrieved_at':at,'retrieval_precision':precision,'offer_updated_at':None,'execution':'UNVERIFIED','away_spread':a,'away_spread_price':ap,'home_spread':h,'home_spread_price':hp,'away_ml':am,'home_ml':hm,'over_total':o,'over_price':op,'under_total':u,'under_price':up}
def normalize(market,decision,lineage):
    if (blob(market),blob(decision),blob(lineage))!=(MARKET_SHA,DECISION_SHA,gate.LINEAGE_SHA):raise ValueError('unqualified replay source identities')
    opening=table(market,'Week 7 Sunday opening-board capture',5)
    afternoon=table(market,'Week 7 afternoon board refresh',6)
    morning=table(market,'Week 7 Monday public-board observation',5)
    original_decisions=table(decision,'Week 7 Sunday opening decision capture',8)
    updates={}
    for l in block(market,'Week 7 Monday afternoon public-board observation').splitlines():
        if l.startswith('| ') and ' @ ' in cells(l)[0]:
            r=cells(l);updates[pair(r[0])]=r
    if len(updates)!=8:raise ValueError('eight saved afternoon source identities required')
    m={'schema':gate.MARKET_SCHEMA,'cycle_id':CYCLE,'as_of_utc':AT,'rows':[]}
    d={'schema':gate.DECISION_SCHEMA,'cycle_id':CYCLE,'as_of_utc':AT,'rows':[]}
    for r in json.loads(lineage)['rows']:
        key=(r['away_team'],r['home_team']);gid=r['game_id'];old=opening[key];later=afternoon[key];mon=morning[key];de=original_decisions[key]
        # Canonical correction explicitly fixes one normalization omission, preserving old text.
        if key==('Western Michigan','Central Michigan'):
            mon=mon.copy();mon[2]='Western Michigan -7 (-110), ML -298; Central Michigan +7 (-110), ML +240; o42.5 -110 / u42.5 -110';mon[4]='event 34788204; '+DK
        first=parse_quote(old[2],'2026-10-11T12:08:00Z','CBS',old[4],'MINUTE') if ' — ' in old[2] else parse_quote(later[2],'2026-10-11T18:05:00Z','CBS',later[5],'MINUTE')
        last=parse_quote(later[2],'2026-10-11T18:05:00Z','CBS',later[5],'MINUTE')
        current=parse_quote(mon[2],'2026-10-12T12:07:02Z','DraftKings',mon[4],'EXACT') if (' — ' in mon[2] or key==('Western Michigan','Central Michigan')) else None
        if key in updates and 'IDENTIFIED_SINGLE_BOOK_FALLBACK' in updates[key][2]:
            u=updates[key];current=parse_quote(u[1],AT,'DraftKings',u[4],'MINUTE')
        if first is None and current is not None:first=copy.deepcopy(current)
        # Three diagnostic conflicts are not eligible source offers; retain coherent morning observations.
        m['rows'].append({'game_id':gid,'kickoff_utc':iso(later[0]),'kickoff_source_url':CBS,'kickoff_status':'RETAINED_UNVERIFIED','first':first,'current':current,'current_availability':'AVAILABLE' if current else 'UNAVAILABLE','retained':last if current is None else None})
        cutoff='Sat Oct 17 9:00 PM CT' if key==('Nebraska','Oregon') else de[5]
        d['rows'].append({'game_id':gid,'state':'INCONCLUSIVE','reason':'Canonical Monday state: qualified consensus/Caesars/material availability/practical access unresolved; no actionable number earned','reconciliation_utc':iso(de[4]),'planning_cutoff_utc':iso(cutoff),'cutoff_authority':'UNVERIFIED','acceptable_number':None,'execution_window':None})
    return {'scope':'AUTHENTIC_SAVED_INPUT_NORMALIZATION_QA_ONLY_NOT_OPERATIONAL_APPEND','source_market_blob':MARKET_SHA,'source_decision_blob':DECISION_SHA,'market':m,'decision':d}
def packet(o,tag):return '\n```'+tag+'\n'+json.dumps(o,indent=2)+'\n```\n'
def replay(market,decision,execution,scorecard,lineage):
    n=normalize(market,decision,lineage)
    args=[market+packet(n['market'],gate.MARKET_TAG),decision+packet(n['decision'],gate.DECISION_TAG),execution,scorecard,lineage,AT]
    sheet=gate.render(*args);proof=gate.audit(sheet,*args);bootstrap=gate.bootstrap(args[0],args[1],lineage)
    return {**proof,'bootstrap':bootstrap,'normalization_scope':n['scope'],'current_quotes':sum(r['current'] is not None for r in n['market']['rows']),'historical_retained_only':sum(r['current'] is None for r in n['market']['rows']),'original_sources':[MARKET_SHA,DECISION_SHA],'limitation':'ephemeral typed append/renderer replay; canonical source bytes and primary HotSheet remain unchanged; no natural producer or source/execution authority acceptance'}
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    names=['market','decision','execution','scorecard','lineage']
    for n in names:p.add_argument('--'+n,required=True,type=Path)
    p.add_argument('--historical',action='store_true')
    a=p.parse_args();values=[getattr(a,n).read_text() for n in names]
    if a.historical:
        values[0]=historical(a.market,MARKET_SHA);values[1]=historical(a.decision,DECISION_SHA)
    print(json.dumps(replay(*values),indent=2))
