"""Complete CBS markdown board capture; display fallback only, not consensus or bets."""
import argparse, hashlib, html, json, re
from datetime import datetime,timezone
from pathlib import Path
from zoneinfo import ZoneInfo
from cfb_week7_accepted_s0_ancestry_audit import ALIASES

URL='https://www.cbssports.com/college-football/odds/FBS/2026/regular/week-7/'
LINEAGE_SHA='d80e26c398de48e7a386ad9a627fe44f4111ac45'
WEEK8_LINEAGE_SHA='337a23b03a10617ff87d9ba8c1c224cd3ebe1d9c'
WEEK8_URL=URL.replace('week-7','week-8')
def blob(s):
    b=s.encode();return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def at(s):
    t=datetime.fromisoformat(s.replace('Z','+00:00'))
    if t.tzinfo is None:raise ValueError('timezone required')
    return t.astimezone(timezone.utc)
def cells(line):return [x.strip() for x in line.strip('|').split('|')]
def plain(s):
    s=re.sub(r'!\[[^\]]*\]\([^)]*\)',' ',s)
    s=re.sub(r'\[([^\]]*)\]\([^)]*\)',r'\1',s)
    return ' '.join(html.unescape(re.sub(r'<[^>]*>',' ',s)).split())
def market(cell,kind):
    ids=re.findall(r'/books-icons/(\d+)\.svg',cell)
    if len(ids)>1:raise ValueError('ambiguous per-cell book icon')
    s=plain(cell).replace('Remove','').strip()
    missing=s in ('','—','--','-','N/A')
    book=ids[0] if ids else None
    if missing:return {'availability':'UNAVAILABLE','line':None,'price':None,'side':None,'opaque_book_icon_id':book}
    if kind=='moneyline':
        if not re.fullmatch(r'[+-]\d+',s):raise ValueError('malformed moneyline '+s)
        line=None;side=None;price=int(s)
    else:
        m=re.fullmatch(r'([ou])?([+-]?\d+(?:\.\d+)?|PK|pk)\s+([+-]\d+)',s)
        if not m:raise ValueError('malformed market pair '+s)
        side,n,p=m.groups();line=0.0 if n.lower()=='pk' else float(n);price=int(p)
        if kind=='spread' and side is not None:raise ValueError('total in spread column')
        if kind=='total' and (side not in ('o','u') or line<=0):raise ValueError('spread/invalid number in total column')
    if abs(price)<100:raise ValueError('invalid American price')
    return {'availability':'DISPLAYED','line':line,'price':price,'side':side,'opaque_book_icon_id':book}

def normalize(markdown,lineage,recovered_by,source_url=URL,source_timezone='America/New_York',*,profile='WEEK7',retained_elapsed_kickoffs=None):
    observed=at(recovered_by)
    profiles={'WEEK7':(URL,LINEAGE_SHA,62),'WEEK8':(WEEK8_URL,WEEK8_LINEAGE_SHA,56)}
    if profile not in profiles:raise ValueError('unqualified source profile')
    page,digest,count=profiles[profile]
    if source_url!=page or source_timezone!='America/New_York':raise ValueError('unqualified source page/year/timezone')
    if blob(lineage)!=digest:raise ValueError('unqualified original identity baseline')
    census=json.loads(lineage)['rows'];expected={(r['away_team'],r['home_team']):r['game_id'] for r in census}
    if len(expected)!=count:raise ValueError('identity baseline mismatch')
    retained_elapsed_kickoffs={} if retained_elapsed_kickoffs is None else retained_elapsed_kickoffs
    if not isinstance(retained_elapsed_kickoffs,dict) or set(retained_elapsed_kickoffs)-set(expected.values()):raise ValueError('unqualified retained elapsed identities')
    if retained_elapsed_kickoffs and profile!='WEEK8':raise ValueError('unqualified retained elapsed context profile')
    elapsed={gid:at(stamp) for gid,stamp in retained_elapsed_kickoffs.items()}
    if any(kick>=observed for kick in elapsed.values()):raise ValueError('retained elapsed context must precede observation')
    aliases={**ALIASES,**({'New Mexico St.':'New Mexico State','Boise St.':'Boise State','Utah St.':'Utah State','Iowa St.':'Iowa State'} if profile=='WEEK8' else {})}
    result=[];pending=None;rows=[];all_team_rows=0
    def finish():
        nonlocal pending,rows
        if pending is None:return
        if len(rows)!=2:raise ValueError('partial game: exactly two team offer rows required')
        pair=tuple(x['team'] for x in rows)
        if pair not in expected:raise ValueError('unknown/reversed directed game identity '+str(pair))
        kick,status=pending[:2]
        if status=='SAME_DAY_DATE_ONLY_REQUIRES_RETAINED_CONTEXT':
            prior=elapsed.get(expected[pair])
            if prior is None or prior.astimezone(ZoneInfo(source_timezone)).date()!=pending[2]:
                raise ValueError('unresolved nonpast source kickoff requires separate qualification')
            # The prior stream proves elapsed identity only. Do not fabricate a
            # timestamp as if the newly retrieved source had printed one.
            status='PAST_SOURCE_DATE_ONLY_EXACT_KICKOFF_UNAVAILABLE'
        result.append({'game_id':expected[pair],'away_team':pair[0],'home_team':pair[1],'source_kickoff_utc':kick.isoformat().replace('+00:00','Z') if kick else None,'temporal_status':status,'team_offers':rows})
        pending=None;rows=[]
    for line in markdown.splitlines():
        if not line.startswith('|'):continue
        c=cells(line)
        if len(c)>=1 and re.match(r'^(Tue|Wed|Thu|Fri|Sat|Sun|Mon) [A-Z][a-z]{2} \d{1,2}(,|$)',c[0]):
            finish()
            if len(c)!=6 or list(map(plain,c[1:]))!=['Final','Open','Spread','MLMoneyline','Total']:raise ValueError('unsupported source column order/schema')
            m=re.match(r'^(\w{3}) (\w{3}) (\d{1,2}),\s*(\d{1,2}:\d{2})(am|pm)',plain(c[0]),re.I)
            if not m:
                date=datetime.strptime('2026 '+plain(c[0]),'%Y %a %b %d').date()
                today=observed.astimezone(ZoneInfo(source_timezone)).date()
                if date>today:raise ValueError('unresolved nonpast source kickoff requires separate qualification')
                if date==today:
                    pending=(None,'SAME_DAY_DATE_ONLY_REQUIRES_RETAINED_CONTEXT',date);continue
                pending=(None,'PAST_SOURCE_DATE_ONLY_EXACT_KICKOFF_UNAVAILABLE');continue
            day,month,date,t,half=m.groups();local=datetime.strptime(f'2026 {month} {date} {t}{half}','%Y %b %d %I:%M%p').replace(tzinfo=ZoneInfo(source_timezone))
            if local.strftime('%a')!=day:raise ValueError('source weekday/date conflict')
            kick=local.astimezone(timezone.utc)
            pending=(kick,'FUTURE_AT_CAPTURE' if kick>observed else 'STARTED_OR_PAST_AT_CAPTURE');continue
        names=re.findall(r'(?<!!)\[([^\]]+)\]\(https://www\.cbssports\.com/college-football/teams/[^)]+\)',c[0]) if c else []
        if not names:continue
        all_team_rows+=1
        if pending is None or len(c)!=6:raise ValueError('unscoped/malformed team offer row')
        name=names[-1];team=aliases.get(name,name)
        # Explicitly quarantine Final and Open columns: never parse as live prices/outcomes.
        rows.append({'team':team,'spread':market(c[3],'spread'),'moneyline':market(c[4],'moneyline'),'total':market(c[5],'total')})
        if len(rows)>2:raise ValueError('extra team offer row')
    finish()
    ids=[r['game_id'] for r in result]
    if len(ids)!=len(set(ids)):raise ValueError('duplicate game identity')
    if set(ids)!=set(expected.values()):raise ValueError('incomplete source identity coverage')
    active=[r for r in result if r['temporal_status']=='FUTURE_AT_CAPTURE']
    return {'schema':'CFB_CBS_COMPLETE_FALLBACK_CAPTURE_V1','source_url':source_url,'response_recovered_by_utc':recovered_by,'clock_semantics':'RESPONSE_RECOVERED_BY_NOT_EXACT_FETCH_OR_BOOK_UPDATE','source_timezone':source_timezone,'source_sha256':hashlib.sha256(markdown.encode()).hexdigest(),'games':result,'coverage':{'governed_games':count,'matched_games':len(result),'source_team_rows':all_team_rows,'future_games':len(active),'future_team_rows':sum(len(r['team_offers']) for r in active),'past_or_started_games':len(result)-len(active),'missing_game_ids':[]},'qualification':'UNIDENTIFIED_FIELD_LEVEL_MIXED_BOOK_FALLBACK_ONLY','consensus':'CONSENSUS_UNAVAILABLE','caesars':'UNVERIFIED','book_update_time':'UNKNOWN','executability':'UNVERIFIED','quarantined_columns':['Final','Open'],'scope':'exact source-display capture and identity completeness only; no outcome/schedule-truth/consensus/execution/decision acceptance'}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--markdown',required=True,type=Path);p.add_argument('--lineage',required=True,type=Path);p.add_argument('--recovered-by',required=True);p.add_argument('--output',type=Path)
    a=p.parse_args();r=normalize(a.markdown.read_text(),a.lineage.read_text(),a.recovered_by)
    if a.output:a.output.write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps({k:v for k,v in r.items() if k!='games'},indent=2))
