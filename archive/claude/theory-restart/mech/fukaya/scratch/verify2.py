import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mech/fukaya/scratch')
from typed import *

R = row(2); S = special(2)
print("== V3a: a(k-4) ~ Cone(iota: a(k) -> R), iota(source b of a(k)) = sink b of R, identity label, k<=0")
for k in (0, -4, -8, -12):
    A = arc(k)
    # R at source (0,0): sink index 5 at (8,5). iota is a degree-(0,1) arrow b(A) -> sink(R): A.b at (8,4)
    A2 = A.shift(8, 4)
    C = cone([(0, 5, '1')], A2, R)      # arrows from A2 (first summand) to R
    Cr = cancel(C)
    target = arc(k - 4)
    ok, f = is_isomorphic(Cr, target.shift(Cr.q[[i for i in range(len(Cr)) if Cr.idem[i]==0][0]] - 0, Cr.h[[i for i in range(len(Cr)) if Cr.idem[i]==0][0]] - 0))
    print(f"  k={k}: |Cone reduced|={len(Cr)}  iso to a({k-4}) = {ok}")
print("== V3b: W^hook(k) := Cone(D.iota) has the SAME pieces with a(k) shifted by q^-2 (gr D): R source (0,0), a(k).b at (6,4)")
print("== V3c: a(k+4) ~ Cone(iota^+: R -> a(k)), iota^+(source b of R) = b of a(k) (a sink), k>=0")
for k in (0, 4, 8):
    A = arc(k)   # b at (0,0) is the sink
    R2 = R.shift(0, -1)     # R.source at (0,-1) so that the identity arrow source(R) -> b(A) has degree (0,1)
    C = cone([(0, 0, '1')], R2, A)
    Cr = cancel(C)
    target = arc(k + 4)
    bidx = [i for i in range(len(Cr)) if Cr.idem[i] == 0][0]
    ok, f = is_isomorphic(Cr, target.shift(Cr.q[bidx], Cr.h[bidx]))
    print(f"  k={k}: |Cone reduced|={len(Cr)} iso to a({k+4}) = {ok}; b at {(Cr.q[bidx], Cr.h[bidx])}")
print("== V3d: quotient triangle  a(k+4) -> R -> a(k), k<=-4 :  Cone(iota~: R -> a(k)) ~ a(k+4)")
for k in (-4, -8, -12):
    A = arc(k)             # b at (0,0), c_i at (2i-1, i)
    R2 = R.shift(0, -1)    # R.source at (0,-1)
    arrows = [(i, i, '1') for i in range(5)]
    if k <= -8: arrows.append((5, 5, 'S'))     # sink b of R -> c_5 of a(k), label S
    C = cone(arrows, R2, A)
    Cr = cancel(C)
    target = arc(k + 4)
    bidx = [i for i in range(len(Cr)) if Cr.idem[i] == 0][0]
    ok, f = is_isomorphic(Cr, target.shift(Cr.q[bidx], Cr.h[bidx]))
    print(f"  k={k}: |Cone reduced|={len(Cr)} iso to a({k+4}) = {ok}; b at {(Cr.q[bidx], Cr.h[bidx])}")
print("== V4: bend arcs are cones between a(0) and the closed special S")
# g: a(0) -> S, b |-> sink b_6 of S (index 6 at (10,6)); identity arrow of degree (0,1): a(0).b at (10,5)
C = cancel(cone([(0, 6, '1')], arc(0).shift(10, 5), S))
print('  Cone(a(0) -> S) reduced:', C.show())
# g': S -> a(0), source b_0 of S |-> b ; a(0).b at (0,1)
C2 = cancel(cone([(0, 0, '1')], S, arc(0).shift(0, 1)))
print('  Cone(S -> a(0)) reduced:', C2.show())
print("== V5: applying Cone_H: exact triangle r_1(k) -> q^-1h^-1 s4 -> r_1(k-4): check Cone_H(a(k-4)) has HF-pairings = those of the cone object (automatic); check K_0 identity")
import sympy as sp
q = sp.symbols('q')
def poly(d): return sum(v * q**k for k, v in d.items())
for k in (0, -4, -8):
    A2 = arc(k).shift(8, 4)
    lhs = [poly(x) for x in arc(k - 4).klass()]
    rhs = [poly(R.klass()[i]) - poly(A2.klass()[i]) for i in range(2)]   # cone: R (+) A2 shifted by h^-1 i.e. sign flip... 
    # In Cone(iota) the summand A2 sits with the gradings given (A2.b at (8,4)), so class = [R] + [A2]
    rhs = [poly(R.klass()[i]) + poly(A2.klass()[i]) for i in range(2)]
    # a(k-4) with b at (0,0)
    print(f"  k={k}: [a({k-4})] == [R] + [q^8 h^4 a({k})] :", [sp.simplify(lhs[i] - rhs[i]) == 0 for i in range(2)])
