import json
import sympy as sp
from fractions import Fraction as F
rs=json.load(open('slsym3.json'))
seen={}
for r in rs:
    if r['type'] in seen: continue
    seen[r['type']]=r
rows=list(seen.values())
def v(r,k): return sp.Rational(str(r[k]))
for r in rows: r['D8']=str(F(r['M3'])/36-12*F(r['K.v3']))
def fit(target,feats):
    A=sp.Matrix([[v(r,f) for f in feats] for r in rows]); b=sp.Matrix([v(r,target) for r in rows])
    rk=A.rank()
    sol,params=A.gauss_jordan_solve(b) if True else None
    return sol
import itertools
feats=['K.v3','Kin.v3','Kout.v3','Uin.v3','Uout.v3','SLin','SLout']
A=sp.Matrix([[v(r,f) for f in feats] for r in rows]); b=sp.Matrix([v(r,'D8') for r in rows])
print('rank of feature symbols',A.rank(),'rank with D8',A.row_join(b).rank())
try:
    sol,params=A.gauss_jordan_solve(b); print('solution',sol.T,params)
except Exception as e: print('no exact solution:',e)
# show a few types where SL is nonzero
for r in rows:
    if r['SLin']!=0 or r['SLout']!=0 or F(r['D8'])!=0:
        print('%-14s D8=%5s Kv3=%4s Kin=%4s Kout=%4s Uin=%4s Uout=%4s SLin=%4s SLout=%4s'%(r['type'],r['D8'],r['K.v3'],r['Kin.v3'],r['Kout.v3'],r['Uin.v3'],r['Uout.v3'],r['SLin'],r['SLout']))
