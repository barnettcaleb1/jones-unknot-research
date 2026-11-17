# Controls for raw_congruence.py: (a) wrong framing corrections must FAIL; (b) record F(1), G(1), exponents a,b mod 5.
import sys, random
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, flat_search as fs, kauffman, alex
from collections import Counter
from raw_congruence import polymod_phi5, F_raw
def G_with(kb,m):
    out={}
    for e,c in kb.items():
        E=e+3*m
        if E%2: return None
        out[E//2]=out.get(E//2,0)+c*(-1)**(m%2)
    return {e:c for e,c in out.items() if c}
def ok(F,G):
    d={}
    for e,c in F.items(): d[e]=d.get(e,0)+c
    for e,c in G.items(): d[e]=d.get(e,0)-c
    return all(v==0 for v in polymod_phi5(d))
def val1(p): return sum(p.values())
def der1(p): return sum(e*c for e,c in p.items())
rnd=random.Random(int(sys.argv[1])); N=int(sys.argv[2]); n=0; st=Counter()
while n<N:
    w=fs.gen(rnd,rnd.randint(6,18))
    if not w: continue
    half=alex.parse(w); full=alex.symmetrize(half)
    if full is None or alex.diagram(full) is None: continue
    bv=fs.bracket_vector(half)
    if bv is None: continue
    y,x=bv; y={e:c for e,c in y.items() if c}
    u={}; fs.padd(u,y); fs.padd(u,fs.pdelta(x)); u={e:c for e,c in u.items() if c}
    if len(u)!=1: continue
    kb=kauffman.bracket(w)
    if not kb: continue
    kb={e:c for e,c in kb.items() if c}
    nx=sum(1 for c,s in half if c=='x' and s==0); ny=sum(1 for c,s in half if c=='y' and s==0)
    if nx==ny: continue      # controls only informative when the on-axis count is unbalanced
    n+=1
    F=F_raw(y)
    for lab,m in (('claimed ny-nx',ny-nx),('none',0),('reversed nx-ny',nx-ny),('double',2*(ny-nx))):
        G=G_with(kb,m)
        if G is None: st[lab+': odd exps']+=1
        elif ok(F,G): st[lab+': pass']+=1
        else: st[lab+': FAIL']+=1
    G=G_with(kb,ny-nx)
    F1,G1=val1(F),val1(G); st['F(1)=%d'%F1]+=1; st['G(1)=%d'%G1]+=1
    a=der1(F)//F1; b=der1(G)//G1
    st['(a-b) mod 5 = %d'%((a-b)%5)]+=1
print('samples with nx!=ny:',n); [print(' ',k,v) for k,v in sorted(st.items())]
