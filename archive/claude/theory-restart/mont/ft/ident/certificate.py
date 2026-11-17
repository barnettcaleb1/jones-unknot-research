# find a small set of types certifying that D8 is not in the span of the candidate symbols
import json, itertools, random
import sympy as sp
rows=json.load(open('bigfit_rows.json'))
feats=['K.v3','Kin.v3','Kout.v3','Uin.v3','Uout.v3','SLin','SLout','N3','N1*K.a2','N1*Kin.a2','N1*Kout.a2','N1*Uin.a2','N1*Uout.a2','N1*N2','N1^3']
def R(r,f): return sp.Rational(r[f])
def incons(sub):
    A=sp.Matrix([[R(r,f) for f in feats] for r in sub]); b=sp.Matrix([R(r,'D8') for r in sub])
    return A.row_join(b).rank()>A.rank()
assert incons(rows)
# greedy removal
cur=list(rows); random.seed(1); random.shuffle(cur)
changed=True
while changed:
    changed=False
    for i in range(len(cur)):
        trial=cur[:i]+cur[i+1:]
        if incons(trial): cur=trial; changed=True; break
print('minimal certificate size',len(cur))
A=sp.Matrix([[R(r,f) for f in feats] for r in cur]); b=sp.Matrix([R(r,'D8') for r in cur])
# left null vector y with y^T A = 0, y^T b != 0
ns=(A.T).nullspace()
for y in ns:
    if (y.T*b)[0]!=0:
        y=y/ min(abs(v) for v in y if v!=0)
        print('certificate: sum_i y_i * symbol_i(type_i) vanishes for every candidate, but not for D8')
        for yi,r in zip(y,cur):
            if yi!=0: print('   y=%6s  %-16s D8=%s'%(yi,r['type'],r['D8']))
        print('   y.D8 =',(y.T*b)[0])
        break
