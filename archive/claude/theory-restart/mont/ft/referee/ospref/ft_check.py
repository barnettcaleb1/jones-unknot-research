# Claims 3/4: order of vanishing at t=-1 of Delta^m J (normalised lp.J), own alternating sums and own exact division.
import sys, random, itertools, time
from rlib import P_add, P_scale, P_divexact
from gens import *
def order_at_m1(P, cap=40):
    k=0
    while P and k<cap:
        q=P_divexact(P,{0:1,1:1})
        if q is None: break
        P=q; k+=1
    return k if P else 99
seed=int(sys.argv[1]); N=int(sys.argv[2]); kinds=sys.argv[3].split(','); modes=sys.argv[4].split(',')
rnd=random.Random(seed); stats={}; fails=[]; t0=time.time()
for kind in kinds:
  for mode in modes:
    done=0; tries=0
    while done<N and tries<20000:
        tries+=1
        w=sample(rnd,kind)
        if not w: continue
        fl=sites(w,mode)
        mmax=min(6,len(fl))
        if mmax<1: continue
        m=rnd.randint(1,mmax)
        S0=rnd.sample(fl,m); Js={}; ok=True
        for S in itertools.product([0,1],repeat=m):
            J=lp.J(flip(w,[s for s,b in zip(S0,S) if b]))
            if J is None: ok=False; break
            Js[S]=J
        if not ok: continue
        done+=1
        D={}
        for S,J in Js.items(): D=P_add(D,P_scale(J,(-1)**sum(S)))
        o=order_at_m1(D)
        need=m+1 if mode=='axis' else m
        key=(kind,mode); st=stats.setdefault(key,{'n':0,'ok':0,'fail':0,'exact_m':0,'exact_m1':0,'zero':0,'maxm':0})
        st['n']+=1; st['maxm']=max(st['maxm'],m)
        if o==99: st['zero']+=1
        if o>=need: st['ok']+=1
        else: st['fail']+=1; fails.append((w,S0,m,o))
        if o==m: st['exact_m']+=1
        if o==m+1: st['exact_m1']+=1
for k,v in stats.items(): print(k,v)
print('fails',fails[:5],' time %.1fs'%(time.time()-t0))
