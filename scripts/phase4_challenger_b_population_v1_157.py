#!/usr/bin/env python3
import hashlib,json,sys
from pathlib import Path
import pandas as pd

BASE2017=["Air Force","Akron","Alabama","Appalachian State","Arizona","Arizona State","Arkansas","Arkansas State","Army","Auburn","BYU","Ball State","Baylor","Boise State","Boston College","Bowling Green","Buffalo","California","Central Michigan","Charlotte","Cincinnati","Clemson","Coastal Carolina","Colorado","Colorado State","Duke","East Carolina","Eastern Michigan","FIU","Florida","Florida Atlantic","Florida State","Fresno State","Georgia","Georgia Southern","Georgia State","Georgia Tech","Hawaii","Houston","Idaho","Illinois","Indiana","Iowa","Iowa State","Kansas","Kansas State","Kent State","Kentucky","LSU","Louisiana","Louisiana Tech","Louisville","Marshall","Maryland","Memphis","Miami (FL)","Miami (OH)","Michigan","Michigan State","Middle Tennessee","Minnesota","Mississippi State","Missouri","NC State","Navy","Nebraska","Nevada","New Mexico","New Mexico State","North Carolina","North Texas","Northern Illinois","Northwestern","Notre Dame","Ohio","Ohio State","Oklahoma","Oklahoma State","Old Dominion","Ole Miss","Oregon","Oregon State","Penn State","Pittsburgh","Purdue","Rice","Rutgers","SMU","San Diego State","San Jose State","South Alabama","South Carolina","South Florida","Southern Miss","Stanford","Syracuse","TCU","Temple","Tennessee","Texas","Texas A&M","Texas State","Texas Tech","Toledo","Troy","Tulane","Tulsa","UAB","UCF","UCLA","UConn","UL Monroe","UMass","UNLV","USC","UTEP","UTSA","Utah","Utah State","Vanderbilt","Virginia","Virginia Tech","Wake Forest","Washington","Washington State","West Virginia","Western Kentucky","Western Michigan","Wisconsin","Wyoming"]
TRANS={2018:({"Liberty"},{"Idaho"}),2022:({"James Madison"},set()),2023:({"Jacksonville State","Sam Houston"},set()),2024:({"Kennesaw State"},set()),2025:({"Delaware","Missouri State"},set())}
ALIASES={"Hawai'i":"Hawaii","App State":"Appalachian State","San José State":"San Jose State","Massachusetts":"UMass","Florida International":"FIU","Miami":"Miami (FL)"}
COUNTS={2016:128,2017:130,2018:130,2019:130,2020:130,2021:130,2022:131,2023:133,2024:134,2025:136}

def memberships():
    out={2016:set(BASE2017)-{"Coastal Carolina","UAB"},2017:set(BASE2017)}
    cur=set(BASE2017)
    for y in range(2018,2026):
        if y in TRANS:
            add,rem=TRANS[y]; cur=(cur|add)-rem
        out[y]=set(cur)
    assert {y:len(v) for y,v in out.items()}==COUNTS
    return out

def canon(x): return ALIASES.get(str(x),str(x))
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

src=Path(sys.argv[1]); out=Path(sys.argv[2]); out.mkdir(parents=True,exist_ok=True)
M=memberships(); audits=[]; allproj=[]
for y in range(2016,2026):
    p=src/f"cfb_schedules_{y}.parquet"
    df=pd.read_parquet(p)
    rawsha=sha(p)
    s=df[df.season.astype(int)==y].copy()
    completed=s.completed.fillna(False).astype(bool)
    s=s[completed].copy()
    s["home_canonical"]=s.home_team.map(canon); s["away_canonical"]=s.away_team.map(canon)
    s["home_fbs"]=s.home_canonical.isin(M[y]); s["away_fbs"]=s.away_canonical.isin(M[y])
    q=s[s.home_fbs|s.away_fbs].copy()
    q["population_class"]=q.apply(lambda r:"FBS_VS_FBS" if r.home_fbs and r.away_fbs else "FBS_VS_NONFBS",axis=1)
    st=q.season_type.astype(str).str.lower()
    notes=q.notes.fillna("").astype(str).str.lower()
    q["competition_class"]="POSTSEASON" 
    q.loc[st=="regular","competition_class"]="REGULAR"
    champ=(st=="regular") & notes.str.contains("championship",regex=False)
    q.loc[champ,"competition_class"]="CONFERENCE_CHAMPIONSHIP"
    keep=["season","game_id","start_date","home_team","away_team","neutral_site","population_class","competition_class"]
    proj=q[keep].copy().sort_values(["start_date","game_id"])
    assert proj.game_id.notna().all() and not proj.game_id.duplicated().any()
    assert proj.start_date.notna().all()
    if y==2025:
        bad=("point","score","winner","spread","moneyline","over_under","odds","bet","post_win","postgame")
        assert not [c for c in proj if any(t in c.lower() for t in bad)]
    op=out/f"challenger_b_schedule_{y}_v1_157.csv"; proj.to_csv(op,index=False)
    audits.append({"season":y,"raw_sha256":rawsha,"raw_rows":int(len(df)),"completed_rows":int(len(s)),
      "qualified_rows":int(len(proj)),"fbs_vs_fbs":int((q.population_class=="FBS_VS_FBS").sum()),
      "fbs_vs_nonfbs":int((q.population_class=="FBS_VS_NONFBS").sum()),
      "regular":int((q.competition_class=="REGULAR").sum()),
      "conference_championship":int((q.competition_class=="CONFERENCE_CHAMPIONSHIP").sum()),
      "postseason":int((q.competition_class=="POSTSEASON").sum()),
      "neutral":int(q.neutral_site.fillna(False).astype(bool).sum()),"projection_sha256":sha(op)})
    allproj.append(proj)
a=pd.DataFrame(audits)
assert (a.fbs_vs_nonfbs>0).all(), "required FBS-vs-nonFBS class absent"
# Postseason availability is source-dependent; fail if absent in seasons where current source should carry it.
missing_post=a[(a.season>=2017)&(a.postseason==0)].season.tolist()
status="PASS" if not missing_post else "BLOCKED_SOURCE_POSTSEASON_COVERAGE"
manifest={"status":status,"membership_counts":COUNTS,"audits":audits,
 "missing_postseason_seasons":missing_post,"model_fit_or_score_performed":False,"outcomes_scored_2025":False,
 "authority":"v1.153-v1.156; exact recovered CBS 2017-2025 membership lineage + v1.155 2016 derivation"}
(out/"manifest.json").write_text(json.dumps(manifest,indent=2)+"\n")
print(json.dumps(manifest,indent=2))
if status!="PASS": raise SystemExit(3)
