# Colour-2 (spin-1) coloured Jones J_3(K) of braid closures via the 2-cable: J_3 = (A^8)^-w (<K^(2)> - 1)/Delta_2  (KL, <O> = delta).
# Checks J_3(t=-1) = 1 and prints the expansion of J_3(-e^h) to order h^4.  t = A^-4.
import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
from kauffman import padd, pshift, pdelta, cap, cup
from fractions import Fraction as F
def sweep(ops):
    state={():{0:1}}
    for c,i in ops:
        new={}
        for m,p in state.items():
            if c=='cap': padd(new.setdefault(cap(m,i),{}),p)
            elif c=='cup':
                m2,loop=cup(m,i); padd(new.setdefault(m2,{}),pdelta(p) if loop else p)
            else:
                a,b=(1,-1) if c=='x' else (-1,1)
                padd(new.setdefault(m,{}),pshift(p,a))
                m2,loop=cup(m,i); q=pdelta(p) if loop else p
                padd(new.setdefault(cap(m2,i),{}),pshift(q,b))
        state={m:p for m,p in new.items() if p}
    return state.get((),{})
def closure_ops(n,cross,cable):
    """n strands, cross = list of (letter, i) i=1..n-1; cable=1 or 2. closure strands on the left."""
    k=cable*n; ops=[('cap',0)]+[('cap',j) for j in range(1,k)]
    for c,i in cross:
        if cable==1: ops.append((c,k+i-1))
        else:
            P=k+2*(i-1); ops+= [(c,P+1),(c,P),(c,P+2),(c,P+1)]
    ops+=[('cup',j) for j in range(k-1,-1,-1)]
    return ops
def pmul(p,q):
    r={}
    for e,c in p.items():
        for f,d in q.items(): r[e+f]=r.get(e+f,0)+c*d
    return {e:c for e,c in r.items() if c}
def pdiv(p,q):
    """exact Laurent division p/q in Z[A^{+-1}]; None if not exact"""
    if not p: return {}
    p=dict(p); out={}
    qt=max(q); qb=min(q); qc=q[qt]
    while p:
        e=max(p)
        if e-qt < min(p)-qb: return None
        c=p[e]
        if c%qc: return None
        k=e-qt; out[k]=c//qc
        for f,d in q.items():
            v=p.get(f+k,0)-out[k]*d
            if v: p[f+k]=v
            else: p.pop(f+k,None)
    return out
DELTA2={4:1,0:1,-4:1}   # A^4 + 1 + A^-4
def J3(n,word):
    cross=[(('x' if s>0 else 'y'),abs(s)) for s in word]
    w=sum(1 if s>0 else -1 for s in word)
    b2=sweep(closure_ops(n,cross,2)); padd(b2,{0:-1})
    q=pdiv(b2,DELTA2)
    q=pshift(q,-8*w)
    assert all(e%4==0 for e in q), q
    return {-e//4:c for e,c in q.items()}          # t = A^-4
def Vjones(n,word):
    cross=[(('x' if s>0 else 'y'),abs(s)) for s in word]
    w=sum(1 if s>0 else -1 for s in word)
    b=sweep(closure_ops(n,cross,1))
    b=pdiv(b,{2:-1,-2:-1})
    b=pmul(b,{3*(-w):(1 if w%2==0 else -1)})                     # (-A^3)^-w
    assert all(e%4==0 for e in b), b
    return {-e//4:c for e,c in b.items()}
def expand(P,order=4):
    # coefficients of P(-e^h) in h: sum_e c (-1)^e e^k / k!
    return [sum(F(c*(-1)**(e%2)*e**k) for e,c in P.items())/F(__import__('math').factorial(k)) for k in range(order+1)]
def conway_a2(V):   # a2 = -V''(1)/6
    return F(-sum(c*e*(e-1) for e,c in V.items()),6)
def v3(V):          # -(V'''(1)+3V''(1))/36
    d2=sum(c*e*(e-1) for e,c in V.items()); d3=sum(c*e*(e-1)*(e-2) for e,c in V.items())
    return F(-(d3+3*d2),36)
KN={'3_1':(2,[1,1,1]),'3_1 stab':(3,[1,1,1,2]),'4_1':(3,[1,-2,1,-2]),'5_1':(2,[1,1,1,1,1]),'5_2':(3,[1,1,1,2,-1,2]),
    '3_1 mirror':(2,[-1,-1,-1]), '6_1':(4,[1,1,2,-1,-3,2,-3]), '3_1#3_1':(3,[1,1,1,2,2,2])}
for name,(n,wd) in KN.items():
    V=Vjones(n,wd); J=J3(n,wd)
    ex=expand(J,4)
    print(name,' V=',sorted(V.items()),' a2=',conway_a2(V),' v3=',v3(V))
    print('    J3=',sorted(J.items()))
    print('    J3(-e^h) coeffs h^0..h^4:',[str(x) for x in ex],'  ratio h^2/a2:',(ex[2]/conway_a2(V) if conway_a2(V) else None),
          ' h^3/v3:',(ex[3]/v3(V) if v3(V) else None))
