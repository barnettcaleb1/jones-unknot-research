# FT at m = 7, 8 (mixed flips), plus on-axis-heavy; order of vanishing of Delta^m J at t=-1
import sys, random, itertools, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont'); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, words
from rlib import P_add, P_scale, P_divexact
from gens import sample, flip, sites

def order_at_m1(P, cap=60):
    k=0
    while P and k<cap:
        q=P_divexact(P,{0:1,1:1})
        if q is None: break
        P=q; k+=1
    return k if P else 99
rnd=random.Random(707); out=[]; t0=time.time(); done=0
while done<8:
    kind=rnd.choice(['mont','long'])
    if kind=='mont':
        w=words.mont(rnd.choice([-3,-2,2,3]),[rnd.choice([-7,-5,5,7]) for _ in range(3)],tw=rnd.choice('xy'),ax=rnd.choice('xy'),off=rnd.choice('xy'))
    else: w=sample(rnd,'long')
    if not w: continue
    fl=sites(w,'mixed'); m=rnd.choice([7,8])
    if len(fl)<m: continue
    S0=rnd.sample(fl,m); Js={}; ok=True
    for S in itertools.product([0,1],repeat=m):
        J=lp.J(flip(w,[s for s,b in zip(S0,S) if b]))
        if J is None: ok=False; break
        Js[S]=J
    if not ok: continue
    done+=1
    D={}
    for S,J in Js.items(): D=P_add(D,P_scale(J,(-1)**sum(S)))
    o=order_at_m1(D); nax=sum(1 for i in S0 if w.split('.')[i] in ('x0','y0'))
    out.append((kind,m,nax,o,o>=m))
    print(kind,'m=%d on-axis=%d order=%s ok=%s'%(m,nax,o,o>=m),' (%.0fs)'%(time.time()-t0)); sys.stdout.flush()
print('all ok:',all(x[4] for x in out))
