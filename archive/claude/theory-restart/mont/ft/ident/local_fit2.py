import sys, random, json
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, diag, flat_search as fs
import sympy as sp
def M(J,k): return sum(c*(-1)**(e%2)*e**k for e,c in J.items())
rnd=random.Random(17); rows=[]; seen=set(); tup=set()
letters=['x1','y1','x2','y2','x3','y3']
tries=0
while len(rows)<150 and tries<20000:
    tries+=1
    # random local body: braid-like word on 3 half-strands closed by caps/cups away from the axis
    n=rnd.randint(4,12)
    body=[rnd.choice(['x2','y2','x3','y3','x4','y4']) for _ in range(n)]
    w='.'.join(['s','r2','r4']+body+['u4','u2'])
    if w in seen: continue
    seen.add(w)
    J=lp.J(w)
    if J is None: continue
    mk=diag.morse_knot(diag.quotient_constituent_tokens(w,'out'))
    if mk is None: continue
    inv=diag.knot_invariants(*mk)
    if inv is None: continue
    key=(inv['a2'],inv['v3'],inv['a4'],inv['j4'])
    rows.append(dict(w=w,M2=M(J,2),M3=M(J,3),M4=M(J,4),a2=inv['a2'],v3=inv['v3'],a4=inv['a4'],j4=inv['j4']))
    tup.add(key)
print('local samples',len(rows),'distinct tuples',len(tup))
def val(r,f):
    out=sp.Integer(1)
    for g in f.split('*'): out*=sp.Rational(str(r[g]))
    return out
def fit(target,feats):
    A=sp.Matrix([[val(r,f) for f in feats] for r in rows]); b=sp.Matrix([sp.Rational(str(r[target])) for r in rows])
    if A.rank()<len(feats): return 'rank-def %d'%A.rank()
    x=(A.T*A).LUsolve(A.T*b); res=A*x-b
    return dict(zip(feats,[str(v) for v in x])), 'maxres', max(abs(v) for v in res)
print('M2:',fit('M2',['a2'])); print('M3:',fit('M3',['v3'])); print('M4:',fit('M4',['a2*a2','a4','j4','a2']))
