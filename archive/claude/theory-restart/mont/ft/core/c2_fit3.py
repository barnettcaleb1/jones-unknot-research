# Is M_3 a Z-linear combination of classical invariants of K and of the constituent knots K_in, K_out (+ j, a2 products)?
import sys, random, json
import clib, lp
from c1_constituents import constituents
from fractions import Fraction as F
import sympy as sp
rnd=random.Random(int(sys.argv[1])); N=int(sys.argv[2])
rows=[]; seen=set()
while len(rows)<N:
    w,J=clib.randJ(rnd,6,16)
    if w in seen: continue
    seen.add(w)
    V=clib.VK(w); Vi,Vo=constituents(w)
    if V is None or Vi is None or Vo is None: continue
    rows.append(dict(w=w,M2=clib.M(J,2),M3=clib.M(J,3),M4=clib.M(J,4),j=clib.j_of(J),
        a2=clib.a2_of_V(V),v3=clib.v3_of_V(V),a2i=clib.a2_of_V(Vi),v3i=clib.v3_of_V(Vi),a2o=clib.a2_of_V(Vo),v3o=clib.v3_of_V(Vo)))
json.dump([{k:(str(v) if isinstance(v,F) else v) for k,v in r.items()} for r in rows],open('c2_rows_%s.json'%sys.argv[1],'w'))
feats=['v3','v3i','v3o','a2','a2i','a2o','j']
def fit(feats,target='M3'):
    A=sp.Matrix([[r[f] for f in feats]+[1] for r in rows]); b=sp.Matrix([r[target] for r in rows])
    # exact least squares via normal equations
    try:
        x=(A.T*A).LUsolve(A.T*b)
    except Exception as e:
        return None,None
    res=A*x-b
    return x, sum(1 for v in res if v!=0)
for fs_ in (['v3'],['v3','v3i'],['v3','v3i','v3o'],['v3','v3i','v3o','a2','a2i','a2o'],feats):
    x,bad=fit(fs_)
    print('M3 ~',fs_,'+1 :',None if x is None else [str(v) for v in x],' residual nonzero rows:',bad,'/',len(rows))
print('sample K_out nontrivial rows:',sum(1 for r in rows if r['a2o']!=0 or r['v3o']!=0))
