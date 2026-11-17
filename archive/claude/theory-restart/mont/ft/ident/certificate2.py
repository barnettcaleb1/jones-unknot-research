# robustness: add products with HYPOTHETICAL order-1 invariants lambda (symbol supported on T^ only, or on C- only)
import sys, json, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, chord, diag, alex
import sympy as sp
from fractions import Fraction as F
def N(J,k): return sum(c*e**k for e,c in J.items())
def flip(tokens, idxs):
    t=list(tokens)
    for i in idxs: a=t[i]; t[i]=('y' if a[0]=='x' else 'x')+a[1:]
    return '.'.join(t)
KEYS=['K','Kin','Kout','Uin','Uout']
cache={}
def vals(w):
    if w in cache: return cache[w]
    J=lp.J(w); inv=diag.all_invariants(w)
    out={'N1':F(N(J,1)),'N2':F(N(J,2))}
    for k in KEYS: out[k+'.a2']=inv[k]['a2']
    cache[w]=out; return out
def elem_type(w, site):
    """('T', delta) or ('C', label) for a single site, labels counting all windings"""
    seq3=chord.traverse(w)
    wcount=[0]
    for (t,k,d) in seq3: wcount.append(wcount[-1]+(1 if k=='w' else 0))
    ps=[(p,d) for p,(t,k,d) in enumerate(seq3) if t==site]
    if len(ps)==1: return ('T','v' if ps[0][1]==1 else '^')
    (p,_),(q,_)=ps; return ('C','+' if (wcount[q]-wcount[p+1])%2==0 else '-')
def level2(w, sites2, key):
    toks=w.split('.'); alt=0
    for S in itertools.product([0,1],repeat=2):
        alt+=(-1)**sum(S)*vals(flip(toks,[s+1 for s,b in zip(sites2,S) if b]))[key]
    sg=chord.site_signs(w,sites2)
    return sg[sites2[0]]*sg[sites2[1]]*alt
def level1(w, site, key):
    toks=w.split('.')
    a=vals(w)[key]-vals(flip(toks,[site+1]))[key]
    return chord.site_signs(w,[site])[site]*a
rows=json.load(open('bigfit_rows.json'))
src=json.load(open('slsym3.json')); conf={}
for r in src: conf.setdefault(r['type'],r)
lamT=lambda et: 1 if et==('T','^') else 0
lamC=lambda et: 1 if et==('C','-') else 0
extra_names=[]
for r in rows:
    c=conf[r['type']]; w=c['w']; sites=c['sites']
    ets={s:elem_type(w,s) for s in sites}
    for lname,lam in (('lT',lamT),('lC',lamC)):
        for key in ['N2']+[k+'.a2' for k in KEYS]:
            tot=0
            for e in sites:
                rest=[s for s in sites if s!=e]
                if lam(ets[e]): tot+=lam(ets[e])*level2(w,rest,key)
            r[lname+'*'+key]=str(tot)
        # triple products of order-1 symbols: lam*N1*N1, lam*lam*N1, lam^3
        n1={s:level1(w,s,'N1') for s in sites}   # valid since N1 has order 1 (level-1 eval = symbol)
        def triple(f,g,h):
            return sum(f(a)*g(b)*h(cc) for a,b,cc in itertools.permutations(sites))
        L=lambda s: lam(ets[s]); NN=lambda s: n1[s]
        r[lname+'*N1*N1']=str(triple(L,NN,NN)); r[lname+'^2*N1']=str(triple(L,L,NN)); r[lname+'^3']=str(triple(L,L,L))
    r['lT*lC*N1']=str(sum(lamT(ets[a])*lamC(ets[b])*level1(w,cc,'N1') for a,b,cc in itertools.permutations(sites)))
feats=['K.v3','Kin.v3','Kout.v3','Uin.v3','Uout.v3','SLin','SLout','N3','N1*K.a2','N1*Kin.a2','N1*Kout.a2','N1*Uin.a2','N1*Uout.a2','N1*N2','N1^3']
feats+=[k for k in rows[0] if k.startswith('lT') or k.startswith('lC')]
A=sp.Matrix([[sp.Rational(r[f]) for f in feats] for r in rows]); b=sp.Matrix([sp.Rational(r['D8']) for r in rows])
print('features',len(feats),'rank',A.rank(),'rank with D8',A.row_join(b).rank())
json.dump(rows,open('bigfit_rows2.json','w'))
