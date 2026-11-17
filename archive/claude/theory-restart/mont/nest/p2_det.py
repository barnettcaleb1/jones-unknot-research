import sys, random, time
sys.path.insert(0,'nest'); sys.path.insert(0,'.')
from nlib import *
from words import row
import alex
from fractions import Fraction
rnd=random.Random(17)
# upstairs model: box -> fraction pair (p,q) of a horizontally symmetric tangle (axis horizontal);
# identity box = 0 tangle (0,1); Y: s->s+1 ; X: 1/s -> 1/s+2 ; product = tangle sum ; F_m = X^-m ; closure s.B = D-closure, det = |q|
def act(w,pq):
    p,q=pq
    for ch in reversed(w):
        if ch=='Y': p,q=p+q,q
        elif ch=='y': p,q=p-q,q
        elif ch=='X': p,q=p,q+2*p
        elif ch=='x': p,q=p,q-2*p
    return (p,q)
def rowleaf(r):
    j=(abs(r)-1)//2
    w=('X'*j+'Y') if r>0 else ('x'*j+'y')
    return ('box','.'.join(row(r)),act(w,(0,1)))
def tsum(a,b): return (a[0]*b[1]+b[0]*a[1], a[1]*b[1])
def pq_of(T):
    if T[0]=='box': return T[2]
    ps=[pq_of(c) for c in T[2]]
    s=ps[0]
    for x in ps[1:]: s=tsum(s,x)
    m=T[1]
    return act(('x'*m) if m>0 else ('X'*(-m)), s)   # X^-m
leaves=[rowleaf(r) for r in (-5,-3,-1,1,3,5,7)]+[('box','y0',(1,1)),('box','x0',(-1,1))]
def rtree(d):
    if d==0: return rnd.choice(leaves)
    k=rnd.choice([1,2,2,3])
    kids=[rtree(d-1)]+[rtree(rnd.choice([0,d-1])) for _ in range(k-1)]
    rnd.shuffle(kids)
    return ('neck',rnd.choice([-3,-2,-1,1,2,3]),kids)
ok=bad=skip=0; t0=time.time()
for i in range(400):
    d=rnd.choice([1,2,2,3])
    T=('neck',rnd.choice([-3,-2,-1,1,2,3]),[rtree(d-1) for _ in range(rnd.choice([1,2,3]))])
    w='s.'+tree_word(T)
    if width(w[2:])>9 or len(w.split('.'))>60: continue
    dt=alex.alex_eval(w,-1)
    if dt is None: skip+=1; continue
    p,q=pq_of(T)
    if abs(q)==dt: ok+=1
    else: bad+=1; print('DET MISMATCH',w,'alex det',dt,'model',(p,q))
print('determinant check of the upstairs (arborescent) model: ok',ok,'bad',bad,'skip(not knot)',skip,'time',round(time.time()-t0,1))
