# symbol-level fit of D8 = M3/36 - 12 v3(K) using moments at t=+1 (N_k) and products with the order-1 invariant N_1
import sys, json, itertools, glob
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, chord, diag, kauffman
import sympy as sp
from fractions import Fraction as F
def N(J,k): return sum(c*e**k for e,c in J.items())
def M(J,k): return sum(c*(-1)**(e%2)*e**k for e,c in J.items())
def flip(tokens, idxs):
    t=list(tokens)
    for i in idxs: a=t[i]; t[i]=('y' if a[0]=='x' else 'x')+a[1:]
    return '.'.join(t)
def vals(w):
    J=lp.J(w); V=diag.jones_from_bracket(kauffman.bracket(w)); d=diag.der
    a2=F(-d(V,2),6); v3=F(-(d(V,3)+3*d(V,2)),36)
    n1,n2,n3=N(J,1),N(J,2),N(J,3)
    return {'M3':F(M(J,3)),'v3':v3,'a2':a2,'N1':F(n1),'N2':F(n2),'N3':F(n3),
            'N1a2':n1*a2,'N1N2':F(n1*n2),'N1^3':F(n1**3),'N1^2':F(n1*n1),'N1':F(n1)}
rs=[]
for f in glob.glob('fast_m3_s2*.json'): rs+=json.load(open(f))
by={}
for r in rs: by.setdefault(r['type'],[]).append(r)
recs=[]
for ty,rr in sorted(by.items()):
    for r in rr[:2]:
        w=r['w']; sites=r['sites']; toks=w.split('.'); alt={}
        for S in itertools.product([0,1],repeat=3):
            vv=vals(flip(toks,[s+1 for s,b in zip(sites,S) if b])); sg=(-1)**sum(S)
            for k,v in vv.items(): alt[k]=alt.get(k,0)+sg*v
        sg=chord.site_signs(w,sites); pr=sg[sites[0]]*sg[sites[1]]*sg[sites[2]]
        rec={k:pr*v for k,v in alt.items()}; rec['type']=ty
        rec['D8']=rec['M3']/36-12*rec['v3']
        recs.append(rec)
# consistency of new symbols per type
cons={}
for r in recs: cons.setdefault(r['type'],set()).add((r['N3'],r['N1a2'],r['N1N2'],r['N1^3']))
print('types',len(cons),'inconsistent N-symbols:',sum(1 for v in cons.values() if len(v)>1))
one={}
for r in recs: one.setdefault(r['type'],r)
rows=list(one.values())
for feats in (['v3','N3'],['v3','N3','N1a2'],['v3','N3','N1a2','N1N2','N1^3']):
    A=sp.Matrix([[sp.Rational(str(r[f])) for f in feats] for r in rows]); b=sp.Matrix([sp.Rational(str(r['D8'])) for r in rows])
    print(feats,'rank',A.rank(),'rank+D8',A.row_join(b).rank())
    try:
        sol,par=A.gauss_jordan_solve(b); print('   SOLUTION',list(sol))
    except Exception as e: print('   no solution')
json.dump([{k:str(v) for k,v in r.items()} for r in rows],open('nfit_rows.json','w'))
for r in rows:
    if r['N3']!=0 or r['D8']!=0:
        print('%-16s D8=%5s v3=%4s N3=%6s N1a2=%4s'%(r['type'],r['D8'],r['v3'],r['N3'],r['N1a2']))
