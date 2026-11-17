import sys, itertools
sys.path.insert(0,'nest')
from nlib import *
import alex
B='y0.r2.y0.y1.y0.y1.x2.u1'
vB=vec(B)[0]
# 1) is v_B = unit * X^-m (p1*p2) with p1,p2 rational (words <= 5)?
rat={}
for n in range(0,6):
    for w in itertools.product('XxYy',repeat=n):
        w=''.join(w)
        v=apply(w)
        if not v[0]: continue
        nv=normalize(v[0])
        if nv is None: continue
        s,k=unit_ratio([nv,{}],[v[0],{}])
        vv=[shift({e:s*c for e,c in v[0].items()},k),shift({e:s*c for e,c in v[1].items()},k)]
        rat.setdefault((tuple(sorted(vv[0].items())),tuple(sorted(vv[1].items()))),(w,vv))
rl=list(rat.values())
print('distinct rational vectors (words<=5):',len(rl))
hits=[]
for m in range(-4,5):
    q=mvec(Xpow(m),vB)   # candidate p up to unit
    # normalise q
    if not q[0]: continue
    nq=normalize(q[0])
    if nq is None: continue
    s,k=unit_ratio([nq,{}],[q[0],{}])
    q=[shift({e:s*c for e,c in q[0].items()},k),shift({e:s*c for e,c in q[1].items()},k)]
    print('m=%d: a(X^m v_B) normalised ='%m, fmt(q[0]), '  rational?', (tuple(sorted(q[0].items())),tuple(sorted(q[1].items()))) in rat)
    for (w1,v1),(w2,v2) in itertools.combinations_with_replacement(rl,2):
        if mul(v1[0],v2[0])!=q[0]: continue
        if star(v1,v2)==q: hits.append((m,w1,w2))
print('Montesinos (2 rational boxes) decompositions found:',hits[:10])
# 2) alexander of the pieces
Np='r2.y1.y0.y1.x2.u1'
print('J(s.'+Np+') =',fmt(J('s.'+Np)) if J('s.'+Np) else None)
print('alex s.B',alex.alex_poly('s.'+B))
