# big symbol-level fit at level 3 on one configuration per type (types from slsym3.json, where SL symbols are known)
import sys, json, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, chord, diag
import sympy as sp
from fractions import Fraction as F
def N(J,k): return sum(c*e**k for e,c in J.items())
def M(J,k): return sum(c*(-1)**(e%2)*e**k for e,c in J.items())
def flip(tokens, idxs):
    t=list(tokens)
    for i in idxs: a=t[i]; t[i]=('y' if a[0]=='x' else 'x')+a[1:]
    return '.'.join(t)
KEYS=['K','Kin','Kout','Uin','Uout']
def vals(w):
    J=lp.J(w); inv=diag.all_invariants(w)
    out={'M3':F(M(J,3)),'N3':F(N(J,3)),'N1':F(N(J,1)),'N2':F(N(J,2))}
    for k in KEYS:
        out[k+'.v3']=inv[k]['v3']; out[k+'.a2']=inv[k]['a2']
    n1=out['N1']
    for k in KEYS: out['N1*'+k+'.a2']=n1*inv[k]['a2']
    out['N1*N2']=n1*out['N2']; out['N1^3']=n1**3
    return out
rs=json.load(open('slsym3.json'))
one={}
for r in rs: one.setdefault(r['type'],r)
rows=[]
for ty,r in sorted(one.items()):
    w=r['w']; sites=r['sites']; toks=w.split('.'); alt={}
    for S in itertools.product([0,1],repeat=3):
        vv=vals(flip(toks,[s+1 for s,b in zip(sites,S) if b])); sg=(-1)**sum(S)
        for k,v in vv.items(): alt[k]=alt.get(k,0)+sg*v
    sg=chord.site_signs(w,sites); pr=sg[sites[0]]*sg[sites[1]]*sg[sites[2]]
    rec={k:pr*v for k,v in alt.items()}
    rec['SLin']=F(r['SLin']); rec['SLout']=F(r['SLout']); rec['type']=ty
    rec['D8']=rec['M3']/36-12*rec['K.v3']
    rows.append(rec)
json.dump([{k:str(v) for k,v in r.items()} for r in rows],open('bigfit_rows.json','w'))
feats=['K.v3','Kin.v3','Kout.v3','Uin.v3','Uout.v3','SLin','SLout','N3']+['N1*'+k+'.a2' for k in KEYS]+['N1*N2','N1^3']
A=sp.Matrix([[sp.Rational(str(r[f])) for f in feats] for r in rows]); b=sp.Matrix([sp.Rational(str(r['D8'])) for r in rows])
print('types',len(rows),'rank feats',A.rank(),'rank with D8',A.row_join(b).rank())
try:
    sol,par=A.gauss_jordan_solve(b); print('SOLUTION',dict(zip(feats,list(sol))),par)
except Exception as e: print('no solution')
