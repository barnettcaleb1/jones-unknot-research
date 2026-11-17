"""Best general special region for a box by orbit descent: beam search over v -> X^{+-1} Y^k v minimising span a + span b;
records the minimum span a(Wv) met (a(Wv) = J of the Montesinos/arborescent closure with special region W). HEURISTIC."""
import sys, time, pickle, collections, json
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import vc, lib
from vc import span
def size(v): return span(v[0])+span(v[1])
def key(v): return (tuple(sorted(v[0].items())),tuple(sorted(v[1].items())))
def descend(v, beam=4, steps=40, kmax=6):
    v=vc.nv(v); frontier=[(size(v),v,'')]; seen={key(v)}
    best=(span(v[0]),'',v)
    for _ in range(steps):
        cand=[]
        for s,w,path in frontier:
            for mu in (1,-1):
                for k in range(-kmax,kmax+1):
                    u=vc.nv(vc.Xpow(mu,vc.Ypow(k,w)))
                    if u is None: continue
                    kk=key(u)
                    if kk in seen: continue
                    seen.add(kk)
                    p2=path+('X' if mu>0 else 'x')+('Y%d'%k if k else '')
                    cand.append((size(u),u,p2))
                    if span(u[0])<best[0]: best=(span(u[0]),p2,u)
        if not cand: break
        cand.sort(key=lambda x:x[0])
        newf=cand[:beam]
        if newf[0][0]>=frontier[0][0]+6: break      # no progress
        frontier=newf
    return best
if __name__=='__main__':
    which=sys.argv[1]; out=sys.argv[2]
    t0=time.time(); res=[]; hist=collections.Counter()
    if which=='Rpairs':
        R=lib.rational(int(sys.argv[3]))
        items=[((R[i][2],R[j][2]),vc.star(R[i][1],R[j][1])) for i in range(len(R)) for j in range(i,len(R))]
    elif which=='G':
        G=lib.general(); R=lib.rational(6)
        items=[((g[2],),g[1]) for g in G]+[((g[2],h[2]),vc.star(g[1],h[1])) for i,g in enumerate(G) for h in G[i:]]+[((g[2],u[2]),vc.star(g[1],u[1])) for g in G for u in R]
    print(which,'items',len(items),flush=True)
    for n,(lab,v) in enumerate(items):
        b=descend(v)
        sa0=span(vc.nv(v)[0])
        hist[b[0]]+=1
        res.append((b[0],sa0,b[1],lab))
        if b[0]==0: print('UNIT FOUND',lab,b[1],flush=True)
        if n%2000==0: print(' ',n,round(time.time()-t0,1),sorted(hist.items())[:6],flush=True)
    res.sort(key=lambda r:(r[0],-r[1]))
    pickle.dump(dict(which=which,res=res[:500],hist=dict(hist),time=time.time()-t0),open(out,'wb'))
    print('DONE',which,'min span a(W v) histogram',sorted(hist.items())[:12],'time',round(time.time()-t0,1))
    for r in res[:10]: print(r)
