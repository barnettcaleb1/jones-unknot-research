# local configurations (half-words with no x0/y0 letters): J = normalised colour-2 Jones of K_1 = K_out; fit M_k
import sys, random, json
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, diag, flat_search as fs
import sympy as sp
from fractions import Fraction as F
def M(J,k): return sum(c*(-1)**(e%2)*e**k for e,c in J.items())
rnd=random.Random(int(sys.argv[1]) if len(sys.argv)>1 else 3); rows=[]; seen=set()
while len(rows)<int(sys.argv[2] if len(sys.argv)>2 else 120):
    w=fs.gen(rnd,rnd.randint(10,24))
    if not w: continue
    toks=w.split('.')
    toks=[t for t in toks if t not in ('x0','y0')]
    w='.'.join(toks)
    if w in seen: continue
    seen.add(w)
    J=lp.J(w)
    if J is None: continue
    mk=diag.morse_knot(diag.quotient_constituent_tokens(w,'out'))
    if mk is None: continue
    inv=diag.knot_invariants(*mk)
    if inv is None: continue
    rows.append(dict(w=w,M2=M(J,2),M3=M(J,3),M4=M(J,4),M5=M(J,5),M6=M(J,6),a2=inv['a2'],v3=inv['v3'],a4=inv['a4'],j4=inv['j4']))
print('local samples',len(rows),' distinct (a2,v3,a4,j4):',len(set((r['a2'],r['v3'],r['a4'],r['j4']) for r in rows)))
def fit(target,feats):
    A=sp.Matrix([[sp.Rational(str(r[f])) if '*' not in f else sp.Rational(str(r[f.split('*')[0]]))*sp.Rational(str(r[f.split('*')[1]])) for f in feats] for r in rows])
    b=sp.Matrix([sp.Rational(str(r[target])) for r in rows])
    if A.rank()<len(feats): return 'rank-def %d'%A.rank()
    x=(A.T*A).LUsolve(A.T*b); res=A*x-b
    return dict(zip(feats,[str(v) for v in x])), 'maxres', max(abs(v) for v in res)
print('M2:',fit('M2',['a2']))
print('M3:',fit('M3',['v3']))
print('M4:',fit('M4',['a2*a2','a4','j4','a2']))
json.dump([{k:str(v) for k,v in r.items()} for r in rows],open('local_rows.json','w'))
