import sys, json
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
import butterfly as bf
import sympy as sp
rows=json.load(open('inv_rows.json'))
for r in rows:
    for axis in ('out','in'):
        s=bf.sato_levine(r['w'],axis)
        r['SL'+axis]=s['a3']
json.dump(rows,open('inv_rows2.json','w'))
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
for feats in (['K.v3','SLout','SLin'],['K.v3','SLout','SLin','Kin.v3','Kout.v3'],['K.v3','SLout','SLin','Kin.v3','Kout.v3','Uin.v3','Uout.v3']):
    print(feats, fit('M3',feats))
