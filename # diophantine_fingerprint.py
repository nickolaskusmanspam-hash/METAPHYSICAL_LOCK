# diophantine_fingerprint.py
import math, json, csv, sys, random
import numpy as np
import pandas as pd
from fractions import Fraction
from collections import Counter

TAU = 2*math.pi
ALLOWED = {2,3,5,7,17,101}
QMAX = 160
TAU_BLOB_ARC = 0.995
TAU_STRIP    = 0.96
PERMS = 10000
SEED = 20251020
rng = np.random.default_rng(SEED)

def wrap(a): 
    a = float(a)
    return a % TAU

def best_rational(x, qmax=QMAX):
    # continued fraction best approx with bounded denominator
    # x in [0,1); return (p,q,abs_error)
    frac = Fraction(x).limit_denominator(qmax)
    p, q = frac.numerator, frac.denominator
    err = abs(x - p/q)
    return p, q, err

def allowed_q(q, allowed=ALLOWED):
    n = q
    for p in allowed:
        while n % p == 0 and n>1:
            n //= p
    return n == 1

def load_points(path):
    # Expect columns: phi, theta, resonance  (others ignored)
    df = pd.read_csv(path)
    cols = {c.lower(): c for c in df.columns}
    for need in ["phi","theta","resonance"]:
        assert any(need in c.lower() for c in df.columns), f"Missing column {need}"
    df = df.rename(columns={cols[[k for k in cols if "phi" in k][0]]:"phi",
                            cols[[k for k in cols if "theta" in k][0]]:"theta",
                            cols[[k for k in cols if "reson" in k][0]]:"resonance"})
    df["phi"]   = df["phi"].map(wrap)
    df["theta"] = df["theta"].map(wrap)
    return df

def region_label(phi, th):
    # conservative boxes
    blob = (0.85<=phi<=1.30) and (0.85<=th<=1.45)
    arc  = (4.30<=phi<=4.95) and (4.20<=th<=4.95)
    strip= (th>=5.80 or th<=0.10)
    if blob:  return "Blob_A"
    if arc:   return "Arc_B"
    if strip: return "Strip_C"
    return "Unlabeled"

def fingerprint(df, tau_blob_arc=TAU_BLOB_ARC, tau_strip=TAU_STRIP):
    rows=[]
    keep_mask=[]
    for _,r in df.iterrows():
        reg = region_label(r["phi"], r["theta"])
        tau = tau_blob_arc if reg in ("Blob_A","Arc_B") else tau_strip
        is_peak = r["resonance"]>=tau
        keep_mask.append(is_peak)
        if not is_peak: 
            continue
        for comp,name in [(r["phi"],"phi"),(r["theta"],"theta")]:
            x = (comp/TAU) % 1.0
            p,q,err = best_rational(x, QMAX)
            rows.append(dict(region=reg, component=name, angle=float(comp),
                             x=float(x), p=p, q=q, abs_err=float(err),
                             q_allowed=allowed_q(q)))
    F = pd.DataFrame(rows)
    return F, np.array(keep_mask, bool)

def jitter_angles(df, sigma=0.03):
    # torus-jitter: add N(0,sigma) then wrap
    ph = (df["phi"].values + rng.normal(0,sigma,size=len(df))) % TAU
    th = (df["theta"].values + rng.normal(0,sigma,size=len(df))) % TAU
    out = df.copy()
    out["phi"] = ph; out["theta"] = th
    return out

def uniform_null(n):
    out = pd.DataFrame(dict(
        phi = rng.uniform(0,TAU,size=n),
        theta = rng.uniform(0,TAU,size=n),
        resonance = np.ones(n)*1.0  # will be thresholded by region anyway
    ))
    return out

def proportion_allowed(F):
    if len(F)==0: return float('nan')
    return float(np.mean(F["q_allowed"].astype(bool)))

def odds_ratio(F):
    # OR: allowed vs not, guard zeros with Haldane-Anscombe
    a = int(F["q_allowed"].sum()); b = int(len(F)-a)
    # avoid div by zero
    return ( (a+0.5)/(b+0.5) )

def perm_test(F_peaks, df_base, make_null, perms=PERMS):
    obs = proportion_allowed(F_peaks)
    null_props=[]
    n = len(F_peaks)
    for _ in range(perms):
        null_df = make_null(df_base)
        F_null,_ = fingerprint(null_df)
        # match sample size by random draw if needed
        if len(F_null) > n: 
            F_null = F_null.sample(n, random_state=SEED+_)
        null_props.append(proportion_allowed(F_null))
    null_props = np.array([x for x in null_props if not math.isnan(x)])
    margin = obs - float(np.nanmean(null_props))
    p = float(np.mean(null_props >= obs))
    return dict(obs=obs, null_mean=float(np.nanmean(null_props)),
                margin=float(margin), pvalue=p)

def main():
    if len(sys.argv)<2:
        print("Usage: python diophantine_fingerprint.py peaks.csv")
        sys.exit(1)
    df = load_points(sys.argv[1])
    F, mask = fingerprint(df)
    # save table
    F.to_csv("diophantine_table.csv", index=False)
    # permutation tests vs two nulls
    # A) uniform angles (matched N)
    make_null_uniform = lambda base: uniform_null(len(base))
    res_uniform = perm_test(F, df, make_null_uniform, perms=PERMS)
    # B) jittered ±0.03 rad about original
    make_null_jitter = lambda base: jitter_angles(base, sigma=0.03)
    res_jitter  = perm_test(F, df, make_null_jitter, perms=PERMS)
    summary = dict(
        Qmax=QMAX, allowed=list(sorted(ALLOWED)),
        counts=dict(total=int(len(F)), allowed=int(F["q_allowed"].sum())),
        prop_allowed=float(proportion_allowed(F)),
        odds_ratio=float(odds_ratio(F)),
        null_uniform=res_uniform,
        null_jitter=res_jitter
    )
    with open("diophantine_summary.json","w") as f:
        json.dump(summary, f, indent=2)
    # quick console print
    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()
