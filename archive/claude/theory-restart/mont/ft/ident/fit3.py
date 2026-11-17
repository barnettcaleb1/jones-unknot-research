import sys, random, json
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import diag, lp
import sympy as sp
from fractions import Fraction as F
def M(Jn,k): return sum(c*(-1)**(e%2)*e**k for e,c in Jn.items())
rows=json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident3_rows.json'))
data=[]
for r in rows:
    w=r[0]; J=lp.J(w); inv=diag.all_invariants(w)
    rec=dict(w=w,M2=M(J,2),M3=M(J,3),M4=M(J,4))
    for k in ('K','Kin','Kout','Uin','Uout'):
        for q in ('a2','v3','j4','a4'):
            rec[k+'.'+q]=inv[k][q]
    data.append(rec)
json.dump([{k:(str(v) if isinstance(v,F) else v) for k,v in d.items()} for d in data],open('inv_rows.json','w'))
def fit(target, feats, data):
    A=sp.Matrix([[sp.Rational(str(d[f])) for f in feats] for d in data])
    b=sp.Matrix([sp.Rational(str(d[target])) for d in data])
    # exact least squares via normal equations, then residual
    ATA=A.T*A; 
    if ATA.det()==0: return None,'singular'
    x=ATA.LUsolve(A.T*b)
    res=A*x-b
    return x, max(abs(v) for v in res)
for feats in (['K.v3'],['K.v3','Kin.v3','Kout.v3'],['K.v3','Uin.v3','Uout.v3'],['K.v3','Kin.v3','Kout.v3','Uin.v3','Uout.v3']):
    x,res=fit('M3',feats,data)
    print(feats, [str(v) for v in x] if x is not None else x, 'max residual',res)
