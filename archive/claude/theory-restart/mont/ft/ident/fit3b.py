import sys, json, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
import chord
import sympy as sp
from fractions import Fraction as F
rows=json.load(open('inv_rows.json'))
for r in rows:
    r.update(chord.lam_counts(r['w']))
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
print('lm values:',sorted(set(r['lm'] for r in rows)))
base=['K.v3','Kin.v3','Kout.v3','Uin.v3','Uout.v3']
extra=['lm','lm*K.a2','lm*Kin.a2','lm*Kout.a2','lm*Uin.a2','lm*Uout.a2','lm*lm*lm']
print(fit('M3',base+extra))
