"""Whitehead's algorithm in F_3 = <1,2,3> (words = tuples of nonzero ints) and the one-relator word problem for
G = F_3 / <<r>> when r is PRIMITIVE (then G = F_2 explicitly): find phi in Aut(F_3) with phi(r) cyclically = z^{+-1},
then w = 1 in G  <=>  phi(w) with z deleted freely reduces to ().  Exact; returns None when r is not primitive
(no cyclic-length-reducing Whitehead move from length > 1: Whitehead's peak-reduction theorem)."""
import itertools
def red(w):
    out = []
    for a in w:
        if out and out[-1] == -a: out.pop()
        else: out.append(a)
    return tuple(out)
def cyc(w):
    w = list(red(w))
    while len(w) >= 2 and w[0] == -w[-1]: w = w[1:-1]
    return tuple(w)
def inv(w): return tuple(-a for a in reversed(w))
def apply(phi, w):
    """phi: dict gen (1..3) -> word"""
    out = []
    for a in w:
        img = phi[abs(a)]
        out.extend(img if a > 0 else inv(img))
    return red(out)
def compose(phi, psi):
    """first phi then psi: x -> psi(phi(x))"""
    return {g: apply(psi, phi[g]) for g in (1, 2, 3)}
ID = {1: (1,), 2: (2,), 3: (3,)}
LET = [1, -1, 2, -2, 3, -3]
def wh_autos():
    autos = []
    for a in LET:
        others = [x for x in LET if abs(x) != abs(a)]
        for k in range(1, len(others) + 1):
            for S in itertools.combinations(others, k):
                A = set(S) | {a}
                phi = {}
                for g in (1, 2, 3):
                    if g == abs(a): phi[g] = (g,); continue
                    xin, xiin = (g in A), (-g in A)
                    if xin and xiin: phi[g] = red((-a, g, a))
                    elif xin: phi[g] = (g, a)
                    elif xiin: phi[g] = (-a, g)
                    else: phi[g] = (g,)
                autos.append(phi)
    return autos
AUTOS = wh_autos()
def primitive_basis(r, maxit=10000):
    """returns (phi, z, sign) with cyc(phi(r)) == (sign*z,) or None"""
    phi = dict(ID); w = cyc(r)
    if not w: return None
    it = 0
    while len(w) > 1 and it < maxit:
        it += 1
        best = None
        for al in AUTOS:
            w2 = cyc(apply(al, w))
            if len(w2) < len(w) and (best is None or len(w2) < len(best[1])): best = (al, w2)
        if best is None: return None
        phi = compose(phi, best[0]); w = best[1]
    if len(w) != 1: return None
    return phi, abs(w[0]), (1 if w[0] > 0 else -1)
def trivial_in_quotient(w, r):
    """w = 1 in F_3/<<r>> ?  True/False when r is primitive; None if r not primitive"""
    pb = primitive_basis(r)
    if pb is None: return None
    phi, z, s = pb
    x = apply(phi, w)
    x = red(tuple(a for a in x if abs(a) != z))
    return x == ()
if __name__ == '__main__':
    print(len(AUTOS), 'Whitehead automorphisms of type II')
    print(primitive_basis((1, 2, 1, 2, 3)), primitive_basis((1, 2, -1, -2)))
    print(trivial_in_quotient((1, 2, -1), (2,)), trivial_in_quotient((1,), (2,)), trivial_in_quotient((1, 3, -1, -3), (1, 2, 2)))
