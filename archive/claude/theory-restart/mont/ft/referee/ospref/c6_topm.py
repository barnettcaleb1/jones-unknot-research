# Claim 6: [h^m] of raw alternating sum D = sum_S (-1)^|S| y_S equals 2^m y_0(A_0) Sigma (own state sum, own Z[zeta_8] arithmetic);
# and the normalised 1T-projection formula against lp.J moments. Independent samples (seed, generators differ from the builder's).
import sys, random, itertools, math
from fractions import Fraction as Fr
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont'); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, flat_search as fs, alex
from rlib import P_add, P_scale, P_divexact
from gens import sample, flip, sites
from statesum_ref import statesum
def rawy(word):
    if lp.J_raw(word) is None: return None
    y,x=fs.bracket_vector(alex.parse(word)); return {e:c for e,c in y.items() if c}
def zeta8(p):   # p in Z[A,1/A] at A = e^{i pi/4}: vector in basis 1,z,z^2,z^3 with z^4 = -1
    v=[0,0,0,0]
    for e,c in p.items():
        r=e%8
        if r<4: v[r]+=c
        else: v[r-4]-=c
    return v
def Mk(J,k): return sum(c*(-1)**(e%2)*e**k for e,c in J.items())
seed=int(sys.argv[1]); N=int(sys.argv[2]); kinds=sys.argv[3].split(",")
rnd=random.Random(seed); res={'raw_ok':0,'raw_bad':0,'norm_ok':0,'norm_bad':0,'nonzeroSigma':0,'nonzero_norm':0,'n':0}
bad=[]; Sig_vals={}
for kind in kinds:
    done=0; tries=0
    while done<N and tries<5000:
        tries+=1
        w=sample(rnd,kind)
        if not w: continue
        fl=sites(w,'mixed')
        if len(fl)<1: continue
        m=rnd.randint(1,min(5,len(fl)))
        S0=rnd.sample(fl,m); ys={}; Js={}; ok=True
        for S in itertools.product([0,1],repeat=m):
            ww=flip(w,[s for s,b in zip(S0,S) if b])
            y=rawy(ww); J=lp.J(ww)
            if y is None or J is None: ok=False; break
            ys[S]=y; Js[S]=J
        if not ok: continue
        done+=1; res['n']+=1
        D={}
        for S,y in ys.items(): D=P_add(D,P_scale(y,(-1)**sum(S)))
        u=D
        for _ in range(m):
            u=P_divexact(u,{4:1,0:1}) if u is not None else None
        Sg=statesum(w,set(S0)); Sig_vals[Sg]=Sig_vals.get(Sg,0)+1
        if Sg!=0: res['nonzeroSigma']+=1
        if u is None: res['raw_bad']+=1; bad.append(('nodiv',w,S0)); continue
        lhs=zeta8(u); y0=zeta8(ys[tuple([0]*m)])
        rhs=[2**m*Sg*c for c in y0]
        if lhs==rhs: res['raw_ok']+=1
        else: res['raw_bad']+=1; bad.append(('raw',w,S0,lhs,rhs))
        # normalised formula (lp convention): [h^m] Delta^m J = (-2)^m sum_T prod_{i in T}(-Sigma_i) Sigma(rest)
        lhsN=Fr(sum((-1)**sum(S)*Mk(J,m) for S,J in Js.items()),math.factorial(m))
        s1={s:statesum(w,{s}) for s in S0}; rhsN=Fr(0)
        for r in range(m+1):
            for T in itertools.combinations(S0,r):
                rest=set(S0)-set(T); val=statesum(w,rest) if rest else Fr(1); p=Fr(1)
                for i in T: p*=-s1[i]
                rhsN+=p*val
        rhsN*=(-2)**m
        if lhsN==rhsN: res['norm_ok']+=1
        else: res['norm_bad']+=1; bad.append(('norm',w,S0,lhsN,rhsN))
        if lhsN!=0: res['nonzero_norm']+=1
print(res); print('Sigma values',sorted(Sig_vals.items(),key=lambda kv:-kv[1])[:12]); print('bad',bad[:4])
