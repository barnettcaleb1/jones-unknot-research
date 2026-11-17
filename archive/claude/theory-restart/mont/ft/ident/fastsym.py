# fast symbol tables: moments of J and Vassiliev invariants of K from its Jones polynomial only.
import sys, random, json, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import diag, lp, chord, kauffman, flat_search as fs
from fractions import Fraction as F
def M(Jn,k): return sum(c*(-1)**(e%2)*e**k for e,c in Jn.items())
def flip(tokens, idxs):
    t=list(tokens)
    for i in idxs: a=t[i]; t[i]=('y' if a[0]=='x' else 'x')+a[1:]
    return '.'.join(t)
def kvals(w):
    J=lp.J(w)
    if J is None: return None
    V=diag.jones_from_bracket(kauffman.bracket(w))
    if V is None: return None
    d=diag.der
    out={'M%d'%k:M(J,k) for k in range(2,7)}
    out['a2']=F(-d(V,2),6); out['v3']=F(-(d(V,3)+3*d(V,2)),36)
    out['j4']=F(d(V,4)+6*d(V,3)+7*d(V,2)+d(V,1),24)
    out['j5']=F(d(V,5)+10*d(V,4)+25*d(V,3)+15*d(V,2)+d(V,1),120)
    return out
def config_symbol(w, sites, fn=kvals):
    toks=w.split('.'); alt={}
    for S in itertools.product([0,1],repeat=len(sites)):
        vals=fn(flip(toks,[s+1 for s,b in zip(sites,S) if b]))
        if vals is None: return None
        sg=(-1)**sum(S)
        for kk,v in vals.items(): alt[kk]=alt.get(kk,0)+sg*v
    sg=chord.site_signs(w,sites); pr=1
    for s in sites: pr*=sg[s]
    return {k:pr*v for k,v in alt.items()}
def sample(seed,m,N,minlen=6,maxlen=14,fn=kvals):
    rnd=random.Random(seed); out=[]; tries=0
    while len(out)<N and tries<50*N:
        tries+=1
        w=fs.gen(rnd,rnd.randint(minlen,maxlen))
        if not w or lp.J(w) is None: continue
        toks=w.split('.')[1:]
        fl=[i for i,a in enumerate(toks) if a[0] in 'xy']
        if len(fl)<m: continue
        sites=sorted(rnd.sample(fl,m))
        d=chord.diagram(w,sites)
        if d is None: continue
        sym=config_symbol(w,sites,fn)
        if sym is None: continue
        out.append(dict(w=w,sites=sites,type=chord.dstr(d),sym={k:str(v) for k,v in sym.items()}))
    return out
if __name__=='__main__':
    seed=int(sys.argv[1]); m=int(sys.argv[2]); N=int(sys.argv[3])
    out=sample(seed,m,N)
    json.dump(out,open('fast_m%d_s%d.json'%(m,seed),'w'))
    print('configs',len(out))
