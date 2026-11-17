import sys
sys.path.insert(0,'nest')
from nlib import *
B='y0.r2.y0.y1.y0.y1.x2.u1'
vB=vec(B)[0]
a=a_of(vB); b=b_of(vB)
L=P((1,0),(-1,1)); Q2=P((1,0),(1,2))   # 1-t, 1+t^2
PB=add(a,mul(mul(L,Q2),vB[1]))
QB=neg(mul(mul(L,Q2),vB[1]))
print('a(v_B) =',fmt(a)); print('b(v_B) =',fmt(b)); print('P_B (X-eigenvalue 1 channel) =',fmt(PB)); print('Q_B ((-t) channel) =',fmt(QB))
alpha=mul(mono(-5),P((1,2),(-1,1),(1,0)))
beta=add(mul(mono(2),P((1,4),(-1,3),(-1,0))), mul(mono(-6),P((1,2),(-1,1),(1,0))))
print('alpha =',fmt(alpha)); print('beta  =',fmt(beta))
print('t^4 P_B / alpha unit:',unit_ratio([mul(mono(4),PB),{}],[alpha,{}]))
print('-t^3 Q_B / beta unit:',unit_ratio([neg(mul(mono(3),QB)),{}],[beta,{}]))
# rationality test: compare with all rational boxes Y^k X^e Y^f e1 with closure trefoil
import itertools
found=[]
for w in ['XY','xy','XYY','xyy']:
    pass
# general: b channel of rational boxes with a = J(trefoil): v = Y^k M e1 with M in {XY, x^-1...}; brute force short words
seen=set()
def words(L):
    for n in range(1,L+1):
        for w in itertools.product('XxYy',repeat=n):
            yield ''.join(w)
cnt=0
for w in words(7):
    v=apply(w)
    nv=normalize(v[0]) if v[0] else None
    if nv!=a: continue
    # normalise vector by the same unit
    r=unit_ratio([nv,{}],[v[0],{}])
    s,k=r
    vv=[shift({e:s*c for e,c in v[0].items()},k),shift({e:s*c for e,c in v[1].items()},k)]
    key=tuple(sorted(vv[1].items()))
    if key in seen: continue
    seen.add(key); cnt+=1
    if vv==vB: found.append(w)
print('distinct rational box vectors (words <=7) with a = J(trefoil):',cnt,' equal to v_B:',found)
print('number of terms of b for those:',sorted(set(len(b_of([a,dict(k)])) for k in seen)))
