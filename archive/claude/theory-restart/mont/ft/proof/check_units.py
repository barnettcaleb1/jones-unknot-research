# Checks (a) J_raw(-1) = 1; (b) Delta^m J_raw divisible by (1+t)^m WITHOUT normalisation (Theorem 2.1);
# (c) normalisation J = sgn t^k J_raw: sgn constant and k_S additive over sites (Prop 2.2), with increment per site.
import sys, random, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont'); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, flat_search as fs
def flip(toks,idxs):
    t=list(toks)
    for i in idxs: a=t[i]; t[i]=('y' if a[0]=='x' else 'x')+a[1:]
    return '.'.join(t)
def divpow(p,m):   # divide Laurent poly p (dict) by (1+t)^m exactly; return None if not divisible
    p=dict(p)
    for _ in range(m):
        if not p: return {}
        lo=min(p); hi=max(p); q={}; r=dict(p)
        for e in range(lo,hi):
            c=r.get(e,0)
            if c: q[e]=c; r[e]=0; r[e+1]=r.get(e+1,0)-c
        if any(v for v in r.values()): return None
        p={e:c for e,c in q.items() if c}
    return p
def normparams(Jr):
    s=sum(c*(-1)**(e%2) for e,c in Jr.items()); d=sum(e*c*(-1)**((e-1)%2) for e,c in Jr.items())
    k=d//s; sgn=s*(-1)**(k%2); return sgn,k,s
rnd=random.Random(int(sys.argv[1]) if len(sys.argv)>1 else 7)
stats={'Jraw(-1)=1':[0,0],'div':[0,0],'sgn const':[0,0],'k additive':[0,0]}; incs={}
done=0; tries=0
while done<int(sys.argv[2] if len(sys.argv)>2 else 60) and tries<20000:
    tries+=1
    w=fs.gen(rnd,rnd.randint(8,16))
    if not w: continue
    toks=w.split('.')
    fl=[i for i,a in enumerate(toks) if len(a)>=2 and a[0] in 'xy' and a[1:].isdigit()]
    m=rnd.choice([2,3,4,5])
    if len(fl)<m: continue
    sites=rnd.sample(fl,m); Jr={}; ok=True
    for S in itertools.product([0,1],repeat=m):
        r=lp.J_raw(flip(toks,[s for s,b in zip(sites,S) if b]))
        if r is None: ok=False; break
        Jr[S]=r
    if not ok: continue
    done+=1
    for S,r in Jr.items():
        stats['Jraw(-1)=1'][0 if lp.ev(r,-1)==1 else 1]+=1
    alt={}
    for S,r in Jr.items():
        for e,c in r.items(): alt[e]=alt.get(e,0)+(-1)**sum(S)*c
    alt={e:c for e,c in alt.items() if c}
    stats['div'][0 if divpow(alt,m) is not None else 1]+=1
    P={S:normparams(r) for S,r in Jr.items()}
    sg=set(p[0] for p in P.values()); stats['sgn const'][0 if len(sg)==1 else 1]+=1
    z=tuple([0]*m); k0=P[z][1]
    inc=[P[tuple(1 if j==i else 0 for j in range(m))][1]-k0 for i in range(m)]
    add_ok=all(P[S][1]-k0==sum(inc[i] for i in range(m) if S[i]) for S in P)
    stats['k additive'][0 if add_ok else 1]+=1
    for i,si in enumerate(sites):
        key=(toks[si][0],'axis' if toks[si][1:]=='0' else 'off'); incs.setdefault(key,{}); incs[key][inc[i]]=incs[key].get(inc[i],0)+1
print('samples',done); print(stats); print('increment of k when flipping a site, by (letter, type):',incs)
