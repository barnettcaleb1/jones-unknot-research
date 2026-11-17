# Independent check of Astra's repaired Theorem B normalization (Codex112801 section 3).
import itertools
from fractions import Fraction
# Laurent polynomials as dict exp->int
def add(a,b):
    r=dict(a)
    for e,c in b.items():
        r[e]=r.get(e,0)+c
        if r[e]==0: del r[e]
    return r
def mul(a,b):
    r={}
    for e1,c1 in a.items():
        for e2,c2 in b.items():
            r[e1+e2]=r.get(e1+e2,0)+c1*c2
    return {e:c for e,c in r.items() if c}
def mono(c,e): return {e:c}
def mat(m,v): return [add(mul(m[0][0],v[0]),mul(m[0][1],v[1])), add(mul(m[1][0],v[0]),mul(m[1][1],v[1]))]
one=mono(1,0); zero={}
Y=[[one,zero],[mono(1,-3),mono(1,-3)]]
Yi=[[one,zero],[mono(-1,0),mono(1,3)]]          # inverse of Y
X=[[one,add(one,mono(-1,4))],[zero,mono(-1,1)]]
E=[[one,add(one,mono(-1,4))],[mono(-1,0),mono(-1,0)]]   # Y^-1 X
def F(ns):
    v=[one,zero]
    for i,n in enumerate(ns):
        M=Y if n>0 else Yi
        for _ in range(abs(n)): v=mat(M,v)
        v=mat(E,v)
    return v[0]
def span(p): return max(p)-min(p) if p else None
def normalize(ns):
    ns=list(ns)
    tpow=0
    if ns and ns[0]==-1:
        while ns and ns[0]==-1: ns.pop(0); tpow+=4
        return ns,tpow
    if ns and ns[0]==0:
        ns.pop(0)
        while ns and ns[0]==1: ns.pop(0)
        if ns: ns[0]-=1
        return normalize(ns) if (ns and ns[0] in (0,-1)) else (ns,tpow)
    return ns,tpow
def formula(ms):
    if not ms: return 0
    m0=ms[0]
    s=3*m0+1 if m0>=1 else 3*abs(m0)-2
    for i in range(1,len(ms)):
        s+=3*abs(ms[i])-2+2*((ms[i]>0)!=(ms[i-1]>0))
    return s
fails=0; tot=0; ext=0
rng=[n for n in range(-5,6)]
for k in range(1,6):
    for ns in itertools.product(range(-5,5),*([[n for n in range(-4,5) if n!=0]]*(k-1))):
        tot+=1
        p=F(ns)
        ms,tp=normalize(ns)
        if ms and ms[0] in (0,-1): print('normalization left a degenerate start',ns,ms); fails+=1; continue
        sp=span(p)
        if sp!=formula(ms): fails+=1; 
        if fails and fails<4 and sp!=formula(ms): print('MISMATCH',ns,ms,sp,formula(ms),sorted(p.items()))
        if p and (abs(p[max(p)])!=1 or abs(p[min(p)])!=1): ext+=1
print('sequences',tot,'span-formula failures',fails,'non-unit-extreme-coefficient cases',ext)
print('F(-1,1)=',sorted(F((-1,1)).items()),' span',span(F((-1,1))))
