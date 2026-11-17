import sys, itertools, random, time
sys.path.insert(0,'.')
from lp import *; from words import *
def vrow(r):
    j=(abs(r)-1)//2
    return apply(('X'*j+'Y') if r>0 else ('x'*j+'y'))
def formula(m,rows):
    p=vrow(rows[0])
    for r in rows[1:]: p=star(p,vrow(r))
    return normalize(close(-m,p))
t0=time.time()
ok=bad=skip=0
for rows in [[3,5],[3,7],[3,3,3],[5,-3],[3,-3],[3,5,-5],[7,7],[-3,-5,9]]:
    for m in (-3,-2,-1,1,2,3):
        w=mont(m,rows); Jw=J(w)
        if Jw is None: skip+=1; continue
        F=formula(m,rows)
        if F==Jw: ok+=1
        else: bad+=1; print('MISMATCH',m,rows,w)
print('ok',ok,'bad',bad,'skip',skip,'time',round(time.time()-t0,1))
for m,rows in [(1,[3,5]),(1,[3,7]),(1,[3,3]),(-1,[3,7])]:
    w=mont(m,rows)
    print(m,rows,'alex',alex.alex_poly(w),'J',sorted(J(w).items()),'a2',a2(J(w)))
