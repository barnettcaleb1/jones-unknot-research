# Sensitivity of the h=0 model: distribution of Sigma, and failure counts for WRONG loop weights (odd winding -> -1, or -> 1).
import sys, random, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/osp')
import ftraw
from fractions import Fraction as Fr
src=open('/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/osp/ftraw.py').read()
rnd=random.Random(int(sys.argv[1])); N=int(sys.argv[2])
vals={}; wrong={'odd->-1':0,'odd->1':0,'axis(1,1)':0}; done=0
import flat_search as fs
def variant(w,sites,oddw,axisw):
    # re-implement by monkeypatching: temporarily edit loop weights via a copy of statesum source
    code=src[src.index('def statesum'):src.index("if __name__")]
    code=code.replace('w=(-1 if par[j]==0 else 3)','w=(-1 if par[j]==0 else %d)'%oddw)
    code=code.replace('eps*v*Fr(3,2)); add(tog(m,par),eps*v*Fr(1,2))','eps*v*Fr(%s)); add(tog(m,par),eps*v*Fr(%s))'%axisw)
    g=dict(ftraw.__dict__); exec(code,g); return g['statesum'](w,sites)
while done<N:
    w=fs.gen(rnd,rnd.randint(8,16))
    if not w: continue
    toks=w.split('.'); fl=[i for i,a in enumerate(toks) if a[0] in 'xy' and a[1:].isdigit()]
    m=rnd.choice([2,3,4])
    if len(fl)<m: continue
    sites=rnd.sample(fl,m); ys={}; ok=True
    for S in itertools.product([0,1],repeat=m):
        y=ftraw.rawy(ftraw.flip(toks,[s for s,b in zip(sites,S) if b]))
        if y is None: ok=False; break
        ys[S]=y
    if not ok: continue
    done+=1
    D={}
    for S,y in ys.items(): ftraw.padd(D,y,(-1)**sum(S))
    u=D
    for _ in range(m): u=ftraw.pdiv(u,{4:1,0:1})
    lhs=ftraw.z8(u); y0=ftraw.z8(ys[tuple([0]*m)])
    Sg=ftraw.statesum(w,set(sites)); vals[Sg]=vals.get(Sg,0)+1
    for name,(ow,aw) in {'odd->-1':(-1,('3,2','1,2')),'odd->1':(1,('3,2','1,2')),'axis(1,1)':(3,('1,1','1,1'))}.items():
        S2=variant(w,set(sites),ow,aw)
        if [2**m*S2*c for c in y0]!=lhs: wrong[name]+=1
print('samples',done,'Sigma distribution',sorted(vals.items(),key=lambda kv:-kv[1])[:15])
print('failures of WRONG models (out of %d):'%done,wrong)
