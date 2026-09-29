#!/usr/bin/env python3
# Pure synthetic semantic gate for frozen S2_K1 source-context rules. No external/live data.
import pandas as pd, numpy as np
# Per-game primitive population: normalized cutoff must exclude entire same UTC calendar date.
mp=pd.DataFrame([
 {"start_date":pd.Timestamp("2026-09-01T18:00Z"),"complete":True,"num":10.0,"den":2.0},
 {"start_date":pd.Timestamp("2026-09-02T01:00Z"),"complete":True,"num":1000.0,"den":1.0},
 {"start_date":pd.Timestamp("2026-09-03T01:00Z"),"complete":False,"num":9999.0,"den":1.0},
])
def pooled(t):
 cut=pd.Timestamp(t).normalize(); z=mp[(mp.start_date<cut)&mp.complete]
 if z.empty: raise RuntimeError("unavailable frozen population baseline")
 return float(z.num.sum()/z.den.sum())
assert pooled("2026-09-02T20:00Z")==5.0 # Sep 2 row excluded despite earlier clock time.
assert pooled("2026-09-03T20:00Z")==1010.0/3.0 # Sep 1+2 included.
assert pooled("2026-09-04T20:00Z")==1010.0/3.0 # incomplete Sep 3 excluded.
# S1 k=1 and frozen source residual eligibility.
def s1(raw,b,n):
 if n==0:return b
 return n/(n+1)*raw+1/(n+1)*b
def residual(raw,b,n,mech,derived):
 if not np.isfinite(b):return None
 if n==0:return 0.0
 if not (mech and derived) or not np.isfinite(raw):return None
 return s1(raw,b,n)-b
assert residual(np.nan,7.0,0,False,False)==0.0
assert residual(9.0,7.0,1,False,True) is None
assert residual(9.0,7.0,1,True,False) is None
assert residual(np.nan,7.0,1,True,True) is None
assert abs(residual(9.0,7.0,1,True,True)-1.0)<1e-12
# Feature-specific context: invalidity in one pair must not invalidate another.
ctx={"A":residual(9.0,7.0,1,True,True),"B":residual(np.nan,4.0,1,True,True)}
assert ctx["A"]==1.0 and ctx["B"] is None
# Strict chronology / own target exclusion.
target=pd.Timestamp("2026-09-10T12:00Z")
sources=[pd.Timestamp("2026-09-09T12:00Z"),pd.Timestamp("2026-09-10T12:00Z"),pd.Timestamp("2026-09-11T12:00Z")]
valid=[x for x in sources if x<target]
assert valid==[pd.Timestamp("2026-09-09T12:00Z")]
print("S2_K1_SOURCE_CONTEXT_SYNTHETIC_SEMANTIC_PASS")
