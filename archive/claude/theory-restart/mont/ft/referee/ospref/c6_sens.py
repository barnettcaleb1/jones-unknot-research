# sensitivity: do wrong weights (odd loop 3 -> -1 or 1; on-axis (3/2,1/2) -> (1,1) or (1/2,3/2)) fail on the same raw data?
import sys, random, itertools
from fractions import Fraction as Fr
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont'); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, flat_search as fs, alex
from rlib import P_add, P_scale, P_divexact
from gens import sample, flip, sites
from statesum_ref import statesum
def rawy(word):
    if lp.J_raw(word) is None: return None
    y,x=fs.bracket_vector(alex.parse(word)); return {e:c for e,c in y.items() if c}
def zeta8(p):
    v=[0,0,0,0]
    for e,c in p.items():
        r=e%8
        if r<4: v[r]+=c
        else: v[r-4]-=c
    return v
rnd=random.Random(int(sys.argv[1])); N=int(sys.argv[2])
models={'true':(3,-1,(Fr(3,2),Fr(1,2))),'odd->-1':(-1,-1,(Fr(3,2),Fr(1,2))),'odd->1':(1,-1,(Fr(3,2),Fr(1,2))),
        'even->1':(3,1,(Fr(3,2),Fr(1,2))),'axis(1,1)':(3,-1,(Fr(1),Fr(1))),'axis(1/2,3/2)':(3,-1,(Fr(1,2),Fr(3,2)))}
fails={k:0 for k in models}; done=0
while done<N:
    w=sample(rnd,rnd.choice(['long','mont']))
    if not w: continue
    fl=sites(w,'mixed')
    if len(fl)<2: continue
    m=rnd.randint(2,min(4,len(fl))); S0=rnd.sample(fl,m); ys={}; ok=True
    if not any(w.split('.')[i] in ('x0','y0') for i in S0) and rnd.random()<0.5: continue   # bias toward on-axis sites
    for S in itertools.product([0,1],repeat=m):
        y=rawy(flip(w,[s for s,b in zip(S0,S) if b]))
        if y is None: ok=False; break
        ys[S]=y
    if not ok: continue
    done+=1
    D={}
    for S,y in ys.items(): D=P_add(D,P_scale(y,(-1)**sum(S)))
    u=D
    for _ in range(m): u=P_divexact(u,{4:1,0:1})
    lhs=zeta8(u); y0=zeta8(ys[tuple([0]*m)])
    for k,(o,e,a) in models.items():
        Sg=statesum(w,set(S0),odd=o,even=e,axw=a)
        if [2**m*Sg*c for c in y0]!=lhs: fails[k]+=1
print('samples',done,'failures per model',fails)
