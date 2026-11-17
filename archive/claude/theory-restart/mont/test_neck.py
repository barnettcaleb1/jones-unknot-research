import sys, itertools, random
sys.path.insert(0,'.'); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
from jtools import *; from words import *
import alex
def vrow(r):
    j=(abs(r)-1)//2
    if r>0: M=X**j*Y
    else: M=(X.inv())**j*Y.inv()
    v=M*e1
    return sp.Matrix([sp.expand(sp.simplify(v[0])),sp.expand(sp.simplify(v[1]))])
def formula(m,rows):
    p=vrow(rows[0])
    for r in rows[1:]: p=star(p,vrow(r))
    M=X**m if m>=0 else (X.inv())**(-m)
    return sp.expand(sp.simplify((e1.T*M*p)[0]))
ok=bad=skip=0
cases=[]
for nb in (1,2,3,4):
    for rows in itertools.product([-5,-3,-1,1,3,5,7],repeat=nb):
        for m in (-2,-1,0,1,2,3):
            cases.append((m,list(rows)))
random.seed(1)
random.shuffle(cases)
cases=cases[:260]+[(-1,[3,5]),(-1,[3,7]),(-1,[3,9]),(2,[3,3,3]),(1,[5,5,5,5])]
for m,rows in cases:
    w=mont(m,rows)
    J=J_raw(w)
    if J is None: skip+=1; continue
    N=normalize(J); F=normalize(formula(m,rows))
    if N is not None and F is not None and sp.expand(N-F)==0: ok+=1
    else:
        bad+=1
        if bad<6: print('MISMATCH',m,rows,w,N,F)
print('ok',ok,'bad',bad,'skip(not knot)',skip)
for m,rows in [(-1,[3,5]),(-1,[3,7])]:
    w=mont(m,rows); N=normalize(J_raw(w))
    print(m,rows,w,'alex',sp.factor(alex.alex_poly(w)),'a2',a2(N))
