import sys, json
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
import axislink, lp
import sympy as sp
from fractions import Fraction as F
def N(J,k): return sum(c*e**k for e,c in J.items())
rows=json.load(open('inv_rows2.json'))
for r in rows:
    s=axislink.sato_levine(r['w']); vals=set(s.values())
    assert len(vals)==1, (r['w'],s)
    r['SLax']=str(vals.pop())
    J=lp.J(r['w']); r['N1']=N(J,1); r['N3']=N(J,3); r['N2']=N(J,2)
    r['D']=str((F(r['M3'])/36-12*F(r['K.v3']))/5)
json.dump(rows,open('inv_rows4.json','w'))
def val(r,f):
    if '*' in f:
        out=sp.Integer(1)
        for g in f.split('*'): out*=val(r,g)
        return out
    return sp.Rational(str(r[f]))
def fit(target, feats):
    A=sp.Matrix([[val(d,f) for f in feats] for d in rows]); b=sp.Matrix([val(d,target) for d in rows])
    if A.rank()<len(feats): return 'rank-deficient %d<%d'%(A.rank(),len(feats))
    x=(A.T*A).LUsolve(A.T*b); res=A*x-b
    return [str(v) for v in x], 'maxres %s'%max(abs(v) for v in res)
print(fit('D',['SLax']))
print(fit('D',['SLax','K.v3']))
print(fit('D',['SLax','K.v3','Kin.v3','Kout.v3','Uin.v3','Uout.v3','SLin','SLout']))
print(fit('D',['SLax','K.v3','Kin.v3','Kout.v3','Uin.v3','Uout.v3','SLin','SLout','N3','N1','N1*K.a2','N1*N1*N1','N1*N2']))
