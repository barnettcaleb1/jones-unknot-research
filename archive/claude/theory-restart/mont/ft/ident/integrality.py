# spanning-family check of the integrality lemmas:
#   f = M3 - 432 v3(K)  : level-1,2 alternating sums mod 180 (level-3 symbols are 1440*D' = 0 mod 180)
#   g = M4 - M4loc(K)   : level-1,2,3 alternating sums mod 1440, level-4 symbols mod 1440 on random 4-site configurations
import sys, json, glob, random, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, diag, chord, flat_search as fs
from fractions import Fraction as F
def M(J,k): return sum(c*(-1)**(e%2)*e**k for e,c in J.items())
cache={}
def fg(w):
    if w in cache: return cache[w]
    J=lp.J(w); inv=diag.K_invariants(w)
    if J is None or inv is None: cache[w]=None; return None
    a2,v3,a4,j4=inv['a2'],inv['v3'],inv['a4'],inv['j4']
    f=F(M(J,3))-432*v3
    g=F(M(J,4))-(-1440*a2*a2-1440*a4+864*j4-120*a2)
    cache[w]=(f,g); return cache[w]
def flip(tokens, idxs):
    t=list(tokens)
    for i in idxs: a=t[i]; t[i]=('y' if a[0]=='x' else 'x')+a[1:]
    return '.'.join(t)
def alt(w,sites):
    toks=w.split('.'); A=[0,0]
    for S in itertools.product([0,1],repeat=len(sites)):
        v=fg(flip(toks,[s+1 for s,b in zip(sites,S) if b]))
        if v is None: return None
        sg=(-1)**sum(S); A[0]+=sg*v[0]; A[1]+=sg*v[1]
    return A
rnd=random.Random(int(sys.argv[1])); res={}
for m,N in ((1,150),(2,250),(3,200),(4,int(sys.argv[2]))):
    cnt=0; badf=0; badg=0; types=set(); tries=0
    while cnt<N and tries<40*N:
        tries+=1
        w=fs.gen(rnd,rnd.randint(6,14))
        if not w or lp.J(w) is None: continue
        toks=w.split('.')[1:]; fl=[i for i,a in enumerate(toks) if a[0] in 'xy']
        if len(fl)<m: continue
        sites=sorted(rnd.sample(fl,m)); d=chord.diagram(w,sites)
        if d is None: continue
        A=alt(w,sites)
        if A is None: continue
        cnt+=1; types.add(chord.dstr(d))
        if m<=2 and A[0]%180!=0: badf+=1
        if m<=3 and A[1]%1440!=0: badg+=1
        if m==4 and A[1]%1440!=0: badg+=1
    print('level %d: configs %d types %d   f-alt not 0 mod 180: %s   g-alt not 0 mod 1440: %d'%(m,cnt,len(types),badf if m<=2 else '-',badg))
