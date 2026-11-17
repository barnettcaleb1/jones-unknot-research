import sys, itertools, random
sys.path.insert(0,'.')
from lp import *; from words import *
def vrow(r):
    j=(abs(r)-1)//2
    return apply(('X'*j+'Y') if r>0 else ('x'*j+'y'))
def formula(m,rows):
    p=vrow(rows[0])
    for r in rows[1:]: p=star(p,vrow(r))
    return normalize(close(-m,p))
ok=bad=skip=0
random.seed(2)
cases=[]
for nb in (1,2,3,4,5):
    for rows in itertools.product([-7,-5,-3,-1,1,3,5,7,9],repeat=nb):
        for m in range(-4,5):
            cases.append((m,list(rows)))
random.shuffle(cases)
cases=cases[:4000]
for m,rows in cases:
    w=mont(m,rows)
    Jw=J(w)
    if Jw is None: skip+=1; continue
    F=formula(m,rows)
    if F==Jw: ok+=1
    else:
        bad+=1
        if bad<6: print('MISMATCH',m,rows,w,Jw,F)
print('ok',ok,'bad',bad,'skip',skip)
