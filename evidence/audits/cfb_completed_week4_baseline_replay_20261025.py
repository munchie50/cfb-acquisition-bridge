"""Week4 exact frozen replay against CBS final cards; outcomes only."""
import csv,hashlib,io,json,re,statistics,zipfile
from datetime import datetime,timezone
from pathlib import Path
from zoneinfo import ZoneInfo
from lxml import html

ARCHIVE_SHA='772b8683365ebf62d35fc3813beb138688b84af4172a0b261fd9218691d5adcf'
ALIASES={'Ball St.':'Ball State','Kent St.':'Kent State','Colorado St.':'Colorado State',
 'San Diego St.':'San Diego State','E. Michigan':'Eastern Michigan','N. Illinois':'Northern Illinois',
 'Georgia St.':'Georgia State','Cent. Ark.':'Central Arkansas','Hawaii':"Hawai'i",'Boise St.':'Boise State',
 'W. Michigan':'Western Michigan','New Mexico St.':'New Mexico State','Miami-OH':'Miami (OH)',
 'Iowa St.':'Iowa State','Ga. Southern':'Georgia Southern','NC Central':'North Carolina Central',
 'Michigan St.':'Michigan State','Texas St.':'Texas State','LIU':'Long Island University',
 'C. Michigan':'Central Michigan','Miami (Fla.)':'Miami','Kennesaw St.':'Kennesaw State',
 'Arkansas St.':'Arkansas State','W. Kentucky':'Western Kentucky','Middle Tenn.':'Middle Tennessee',
 'Jacksonville St.':'Jacksonville State','So. Miss':'Southern Miss','App. St.':'App State',
 'Washington St.':'Washington State','Utah St.':'Utah State','Miss. State':'Mississippi State',
 'FAU':'Florida Atlantic','UL-Monroe':'UL Monroe','Missouri St.':'Missouri State','UMass':'Massachusetts',
 'Sacramento St.':'Sacramento State','Fresno St.':'Fresno State','C. Carolina':'Coastal Carolina',
 'FIU':'Florida International'}

def unique(rows,key):
 result={key(r):r for r in rows}
 if len(result)!=len(rows):raise ValueError('duplicate identity')
 return result

def cards(raw):
 root=html.fromstring(raw)
 nodes=root.xpath('//div[contains(concat(" ",normalize-space(@class)," ")," single-score-card ")]')
 results=[]
 for node in nodes:
  if 'postgame' not in node.get('class','').split():raise ValueError('non-final source game')
  status=node.xpath('.//div[contains(@class,"game-status")]')
  if len(status)!=1 or not ''.join(status[0].itertext()).strip().lower().startswith('final'):
   raise ValueError('missing final status')
  teams=[]
  for tr in node.xpath('.//tbody/tr'):
   name=tr.xpath('.//a[contains(@class,"team-name-link")]/text()')
   total=tr.xpath('./td[@class="total"]/text()')
   if name or total:
    if len(name)!=1 or len(total)!=1 or not total[0].isdigit():raise ValueError('invalid team/score')
    quarters=tr.xpath('./td[not(contains(@class,"team")) and not(@class="total")]/text()')
    if sum(int(n) for n in quarters)!=int(total[0]):raise ValueError('quarter-total disagreement')
    teams.append({'raw':name[0],'name':ALIASES.get(name[0],name[0]),'score':int(total[0])})
  if len(teams)!=2:raise ValueError('incomplete final game')
  match=re.fullmatch(r'NCAAF_(\d{8})_(\w+)@(\w+)',node.get('data-abbrev',''))
  if not match or not match[1].startswith('202609'):raise ValueError('unknown date/source identity')
  results.append({'date':datetime.strptime(match[1],'%Y%m%d').date().isoformat(),
                  'cbs_game_id':node.get('id'),'cbs_abbrev':node.get('data-abbrev'),
                  'away_team':teams[0]['name'],'home_team':teams[1]['name'],
                  'away_score':teams[0]['score'],'home_score':teams[1]['score'],
                  'status':''.join(status[0].itertext()).strip(),'raw_team_names':[t['raw'] for t in teams]})
 unique(results,lambda r:(r['date'],r['away_team'],r['home_team']))
 return results

def replay(archive,raw):
 if hashlib.sha256(archive).hexdigest()!=ARCHIVE_SHA:raise ValueError('changed original archive')
 with zipfile.ZipFile(io.BytesIO(archive)) as z:
  m=json.loads(z.read('manifest_v1_206.json'))
  for name,digest in m['hashes'].items():
   if hashlib.sha256(z.read(name)).hexdigest()!=digest:raise ValueError('archive manifest mismatch')
  read=lambda n:list(csv.DictReader(io.StringIO(z.read(n).decode())))
  p=read('challenger_b_2026_fair_predictions_v1_206.csv')
  targets=read('challenger_b_2026_target_ledger_v1_206.csv')
  excluded=read('challenger_b_2026_exclusions_v1_206.csv')
  eligibility=read('challenger_b_2026_feature_eligibility_ledger_v1_206.csv')
 p=[r for r in p if '2026-09-24'<=r['start_date'][:10]<='2026-09-27']
 targets=[r for r in targets if '2026-09-24'<=r['start_date'][:10]<='2026-09-27']
 excluded=[r for r in excluded if '2026-09-24'<=r['start_date'][:10]<='2026-09-27']
 pi=unique(p,lambda r:r['game_id']);ti=unique(targets,lambda r:r['game_id']);ei=unique(excluded,lambda r:r['game_id'])
 if set(pi)&set(ei) or set(pi)|set(ei)!=set(ti):raise ValueError('prediction/exclusion accounting')
 finals=cards(raw);fi=unique(finals,lambda r:(r['date'],r['away_team'],r['home_team']))
 rows=[]
 for pred in p:
  source_date=datetime.fromisoformat(pred['start_date']).astimezone(ZoneInfo('America/New_York')).date().isoformat()
  key=(source_date,pred['away_team'],pred['home_team'])
  if key not in fi:raise ValueError('missing final: '+str(key))
  result=fi[key];margin=result['home_score']-result['away_score'];total=result['home_score']+result['away_score']
  pm,pt,pw=map(float,(pred['pred_margin'],pred['pred_total'],pred['pred_win']))
  if margin==0:raise ValueError('unhandled final tie')
  direction=int(pm>0)==int(margin>0);probability=int(pw>=.5)==int(margin>0)
  rows.append({'game_id':pred['game_id'],'away_team':pred['away_team'],'home_team':pred['home_team'],
               'date':key[0],'population_class':pred['population_class'],
               'pred_home_margin':pm,'pred_total':pt,'pred_home_win':pw,
               'cbs_final':result,'actual_home_margin':margin,'actual_total':total,
               'signed_margin_error':margin-pm,'signed_total_error':total-pt,
               'direction_correct':direction,'probability_classifier_correct':probability,
               'brier':(pw-int(margin>0))**2})
 scored=[r for r in rows if r['population_class']=='FBS_VS_FBS']
 def metrics(rs):
  return {'n':len(rs),'margin_direction_correct':sum(r['direction_correct'] for r in rs),
          'probability_classifier_correct':sum(r['probability_classifier_correct'] for r in rs),
          'margin_mae':statistics.mean(abs(r['signed_margin_error']) for r in rs),
          'total_mae':statistics.mean(abs(r['signed_total_error']) for r in rs),
          'signed_margin_error':statistics.mean(r['signed_margin_error'] for r in rs),
          'signed_total_error':statistics.mean(r['signed_total_error'] for r in rs),
          'brier':statistics.mean(r['brier'] for r in rs)}
 target_keys={(datetime.fromisoformat(r['start_date']).astimezone(ZoneInfo('America/New_York')).date().isoformat(),r['away_team'],r['home_team']) for r in targets}
 return {'schema':'CFB_COMPLETED_WEEK_BASELINE_RECONCILIATION_V1','week':4,
         'archive_sha256':ARCHIVE_SHA,'cutoff_utc':m['cutoff_utc'],
         'fresh_final_html_sha256':hashlib.sha256(raw).hexdigest(),
         'population':{'source_games':len(finals),'original_targets':len(targets),
                       'original_predictions':len(p),'original_exclusions':len(excluded),
                       'governed_fbs_vs_fbs_scored':len(scored),
                       'modeled_nonfbs_kept_separate':len(rows)-len(scored)},
         'source_games_outside_original_targets':[r for r in finals if (r['date'],r['away_team'],r['home_team']) not in target_keys],
         'metrics':metrics(scored),'all_modeled_diagnostic_metrics_not_governed_population':metrics(rows),
         'largest_margin_errors':sorted(scored,key=lambda r:abs(r['signed_margin_error']),reverse=True)[:5],
         'largest_total_errors':sorted(scored,key=lambda r:abs(r['signed_total_error']),reverse=True)[:5],
         'rows':scored,'modeled_nonfbs_rows':[r for r in rows if r['population_class']!='FBS_VS_FBS'],
         'original_exclusions':excluded,'eligible_feature_ledger_columns':list(eligibility[0])}

if __name__=='__main__':
 import argparse
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--archive',type=Path,required=True);parser.add_argument('--html',type=Path,required=True)
 parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
 result=replay(args.archive.read_bytes(),args.html.read_bytes())
 result['final_source_url']='https://www.cbssports.com/college-football/scoreboard/FBS/2026/regular/4/'
 result['source_file_recovered_by_utc']=datetime.fromtimestamp(args.html.stat().st_mtime,timezone.utc).isoformat()
 result['replayed_at_utc']=datetime.now(timezone.utc).isoformat()
 args.output.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({k:result[k] for k in ('population','metrics','eligible_feature_ledger_columns')},indent=2))
