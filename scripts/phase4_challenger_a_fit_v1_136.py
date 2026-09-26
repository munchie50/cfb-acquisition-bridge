import json, hashlib, math, os
import numpy as np, pandas as pd
from scipy.optimize import minimize

DATA="phase4_challenger_a_dataset_v1_131.csv"
CFG="phase4_challenger_a_config_v1_131.json"
OUT="phase4_challenger_a_fit_v1_136"
LAM=[0,0.0001,0.001,0.01,0.1,1,10,100]
df=pd.read_csv(DATA,dtype={"game_id":str})
cfg=json.load(open(CFG))
if any(df.season==2025): raise SystemExit("2025 TEST exposure")
features=cfg["numeric_predictor_order"]
if len(features)!=34 or df[features].isna().any().any(): raise SystemExit("bad predictor matrix")
if any(any(x in c.lower() for x in ["spread","moneyline","over_under","market","odds"]) for c in features): raise SystemExit("market-like predictor")
if not set(df.venue_state).issubset({"HOME","NEUTRAL"}): raise SystemExit("unknown venue")
df["venue_neutral"]=(df.venue_state=="NEUTRAL").astype(float)
preds=features+["venue_neutral"]
targets={"margin":"target_home_margin","total":"target_total_points","win":"target_home_win"}

def prep(train,ev):
    mu=train[features].mean().to_numpy(float); sd=train[features].std(ddof=0).to_numpy(float)
    if np.any(~np.isfinite(sd)) or np.any(sd==0): raise SystemExit("zero/nonfinite sd")
    A=(train[features].to_numpy(float)-mu)/sd; B=(ev[features].to_numpy(float)-mu)/sd
    A=np.c_[A,train["venue_neutral"].to_numpy(float)]; B=np.c_[B,ev["venue_neutral"].to_numpy(float)]
    return A,B,mu,sd

def fit_gauss(X,y,lam):
    Z=np.c_[np.ones(len(X)),X]; P=np.eye(Z.shape[1]); P[0,0]=0
    return np.linalg.solve(Z.T@Z/len(y)+lam*P,Z.T@y/len(y))
def fit_logit(X,y,lam):
    Z=np.c_[np.ones(len(X)),X]
    def fun(w):
        z=Z@w
        loss=np.mean(np.logaddexp(0,z)-y*z)+lam*np.dot(w[1:],w[1:])/2
        p=1/(1+np.exp(-np.clip(z,-40,40)))
        g=Z.T@(p-y)/len(y); g[1:]+=lam*w[1:]
        return loss,g
    r=minimize(lambda w: fun(w),np.zeros(Z.shape[1]),jac=True,method="L-BFGS-B",options={"maxiter":2000,"ftol":1e-12})
    if not r.success: raise SystemExit("logit convergence: "+r.message)
    return r.x
def predict(X,w,kind):
    z=np.c_[np.ones(len(X)),X]@w
    return 1/(1+np.exp(-np.clip(z,-40,40))) if kind=="win" else z
def metrics(y,p,kind):
    if kind=="win":
        q=np.clip(p,1e-15,1-1e-15)
        return {"n":len(y),"brier":float(np.mean((p-y)**2)),"logloss":float(-np.mean(y*np.log(q)+(1-y)*np.log(1-q)))}
    e=p-y
    return {"n":len(y),"mae":float(np.mean(abs(e))),"rmse":float(np.sqrt(np.mean(e*e))),"bias":float(np.mean(e))}

foldrows=[]; selected={}
for kind,tcol in targets.items():
    for lam in LAM:
        vals=[]
        for yr in range(2017,2023):
            tr=df[(df.season>=2016)&(df.season<yr)]; ev=df[df.season==yr]
            X,E,_,_=prep(tr,ev); y=tr[tcol].to_numpy(float); ye=ev[tcol].to_numpy(float)
            w=fit_logit(X,y,lam) if kind=="win" else fit_gauss(X,y,lam)
            m=metrics(ye,predict(E,w,kind),kind)
            score=m["brier"] if kind=="win" else m["mae"]; vals.append(score)
            foldrows.append({"target":kind,"lambda":lam,"eval_season":yr,"score":score,**m})
        foldrows.append({"target":kind,"lambda":lam,"eval_season":"MEAN","score":float(np.mean(vals))})
    cand=[r for r in foldrows if r["target"]==kind and r["eval_season"]=="MEAN"]
    best=min(cand,key=lambda r:(round(r["score"],12),-r["lambda"]))
    selected[kind]=best["lambda"]

train=df[df.season.between(2016,2022)].copy(); val=df[df.season.between(2023,2024)].copy()
results={}; coefrows=[]; predout=val[["season","game_id","start_date","home_team","away_team","venue_state"]].copy()
X,V,mu,sd=prep(train,val)
for kind,tcol in targets.items():
    y=train[tcol].to_numpy(float); yv=val[tcol].to_numpy(float); lam=selected[kind]
    w=fit_logit(X,y,lam) if kind=="win" else fit_gauss(X,y,lam)
    p=predict(V,w,kind); predout["pred_"+kind]=p; predout["actual_"+kind]=yv
    results[kind]={"selected_lambda":lam,"validation":metrics(yv,p,kind)}
    for name,valc in zip(["intercept"]+preds,w): coefrows.append({"target":kind,"lambda":lam,"term":name,"coefficient":float(valc)})
# calibration
cal=[]
p=predout.pred_win.to_numpy(); y=predout.actual_win.to_numpy()
bins=np.minimum((p*10).astype(int),9)
for b in range(10):
    z=bins==b
    if z.any(): cal.append({"bin":b,"lo":b/10,"hi":(b+1)/10,"n":int(z.sum()),"mean_pred":float(p[z].mean()),"actual_rate":float(y[z].mean())})
# stability: season, venue, early/later (35 days from season first game), regime, abs predicted margin >=14
predout["start_date"]=pd.to_datetime(predout.start_date,utc=True)
first=predout.groupby("season").start_date.transform("min")
predout["season_phase"]=np.where((predout.start_date-first).dt.days<35,"EARLY_35D","LATER")
predout["margin_bucket"]=np.where(abs(predout.pred_margin)>=14,"ABS_MARGIN_GE_14","ABS_MARGIN_LT_14")
predout["regime"]=predout.season.map({2023:"2023_FIRST_DOWN_CLOCK",2024:"2024_TWO_MINUTE_TIMING"}).fillna("OTHER")
slices=[]
for kind in targets:
    for dim in ["season","venue_state","season_phase","margin_bucket","regime"]:
        for key,g in predout.groupby(dim):
            slices.append({"target":kind,"dimension":dim,"slice":str(key),**metrics(g["actual_"+kind].to_numpy(),g["pred_"+kind].to_numpy(),kind)})
os.makedirs(OUT,exist_ok=True)
pd.DataFrame(foldrows).to_csv(f"{OUT}/train_forward_chain_grid.csv",index=False)
pd.DataFrame(coefrows).to_csv(f"{OUT}/selected_coefficients.csv",index=False)
predout.to_csv(f"{OUT}/blind_validation_predictions.csv",index=False)
pd.DataFrame(cal).to_csv(f"{OUT}/win_calibration.csv",index=False)
pd.DataFrame(slices).to_csv(f"{OUT}/validation_stability_slices.csv",index=False)
sc=pd.DataFrame({"feature":features,"mean":mu,"sd":sd}); sc.to_csv(f"{OUT}/train_scaling.csv",index=False)
summary={"status":"EXECUTED_NOT_ACCEPTED","train_rows":len(train),"validation_rows":len(val),"selected":selected,"validation":results,"lambda_grid":LAM,"fit_seasons":[2016,2017,2018,2019,2020,2021,2022],"validation_seasons":[2023,2024],"test_2025_rows":int((df.season==2025).sum()),"unavailable_slices":["FBS_vs_FCS (classification metadata absent from frozen matrix)","conference (qualified conference metadata absent from frozen matrix)"],"software":{"numpy":np.__version__,"pandas":pd.__version__}}
json.dump(summary,open(f"{OUT}/summary.json","w"),indent=2)
manifest={}
for fn in sorted(os.listdir(OUT)):
    b=open(f"{OUT}/{fn}","rb").read(); manifest[fn]={"sha256":hashlib.sha256(b).hexdigest(),"bytes":len(b)}
json.dump(manifest,open(f"{OUT}/manifest.json","w"),indent=2)
print(json.dumps(summary,indent=2))
