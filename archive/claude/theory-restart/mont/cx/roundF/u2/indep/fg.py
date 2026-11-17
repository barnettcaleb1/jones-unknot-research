"""u2/indep/fg.py -- free groups and Whitehead's algorithm, written from scratch for U2 (no import from regress/critic/cert).
Words: tuples of nonzero ints (+k = generator k, -k = its inverse).  Whitehead reduction works on a TUPLE of cyclic words
(Whitehead's peak-reduction theorem holds for finite tuples of cyclic words: if the total cyclic length is not minimal in the
Aut-orbit, some Whitehead automorphism of type II strictly reduces it)."""
import itertools

def red(w):
    s = []
    for a in w:
        if s and s[-1] == -a: s.pop()
        else: s.append(a)
    return tuple(s)

def inv(w): return tuple(-a for a in reversed(w))

def cyc(w):
    w = red(w)
    i, j = 0, len(w) - 1
    while i < j and w[i] == -w[j]: i += 1; j -= 1
    return w[i:j + 1]

def subst(img, w):
    """img: dict gen -> word (missing gens fixed); returns reduced image of w"""
    out = []
    for a in w:
        g = abs(a)
        im = img.get(g, (g,))
        out.extend(im if a > 0 else inv(im))
    return red(out)

def cyc_equal(u, v):
    """u, v cyclic words equal up to rotation"""
    u = cyc(u); v = cyc(v)
    if len(u) != len(v): return False
    if not u: return True
    s = u + u
    n = len(v)
    return any(s[k:k + n] == v for k in range(len(u)))

def conj_class_equal(u, v):
    """u conjugate to v (free group): cyclic reductions agree up to rotation"""
    return cyc_equal(u, v)

def whitehead_autos(n):
    """all type-II Whitehead automorphisms (a, A) of F_n as substitution dicts, built from the definition:
    a a letter, A a set of letters with a in A, a^-1 not in A; x -> x a if x in A, x^-1 notin A; x -> a^-1 x if x^-1 in A,
    x notin A; x -> a^-1 x a if both; else x."""
    letters = [s * g for g in range(1, n + 1) for s in (1, -1)]
    res = []
    for a in letters:
        rest = [x for x in letters if abs(x) != abs(a)]
        for r in range(1, len(rest) + 1):
            for S in itertools.combinations(rest, r):
                A = set(S)
                img = {}
                for g in range(1, n + 1):
                    if g == abs(a): continue
                    i1, i2 = (g in A), (-g in A)
                    if i1 and i2: img[g] = (-a, g, a)
                    elif i1: img[g] = (g, a)
                    elif i2: img[g] = (-a, g)
                if img: res.append(img)
    return res

_AUT = {}
def autos(n):
    if n not in _AUT: _AUT[n] = whitehead_autos(n)
    return _AUT[n]

def compose(n, f, g):
    """substitution dict of 'first f then g' as maps on words: w -> g(f(w))"""
    return {k: subst(g, f.get(k, (k,))) for k in range(1, n + 1)}

def wh_reduce(n, rels, maxit=100000):
    """greedy Whitehead reduction of the tuple rels (cyclic words in F_n).  Returns (phi, reduced tuple) with
    reduced[i] = cyc(phi(rels[i])); the result has minimal total length in its Aut(F_n)-orbit (Whitehead)."""
    phi = {k: (k,) for k in range(1, n + 1)}
    cur = [cyc(r) for r in rels]
    L = sum(map(len, cur))
    it = 0
    while it < maxit:
        it += 1
        best = None
        for al in autos(n):
            new = [cyc(subst(al, r)) for r in cur]
            L2 = sum(map(len, new))
            if L2 < L and (best is None or L2 < best[0]): best = (L2, al, new)
        if best is None: break
        L, al, cur = best
        phi = compose(n, phi, al)
    return phi, cur

def free_quotient_solver(n, rels):
    """If, after Whitehead reduction, every relator is empty or a single letter, then F_n/<<rels>> is free on the remaining
    generators; returns a function w -> bool (w = 1 in the quotient) and the killed generators; else (None, reduced)."""
    phi, cur = wh_reduce(n, rels)
    if any(len(r) > 1 for r in cur): return None, cur
    killed = {abs(r[0]) for r in cur if len(r) == 1}
    def triv(w):
        x = subst(phi, w)
        return red(tuple(a for a in x if abs(a) not in killed)) == ()
    return triv, sorted(killed)

def in_free_factor(w, allowed):
    """cyclically reduced w uses only generators in 'allowed' (w lies in a conjugate of that free factor)"""
    return all(abs(a) in allowed for a in cyc(w))

if __name__ == '__main__':
    # self tests
    assert len(whitehead_autos(3)) == 6 * (2 ** 4 - 1)
    f, k = free_quotient_solver(3, [(1, 2, 1, 2, 3)])
    print('primitive x y x y z :', f is not None, k)
    f2, cur = free_quotient_solver(3, [(1, 2, -1, -2)])
    print('commutator [x,y] not primitive:', f2 is None, cur)
    f3, k3 = free_quotient_solver(4, [(1, 2), (3, 2, 4)])
    print('pair (xy, zyw):', f3 is not None, k3, ' x*y^-1... ', f3((1,)) if f3 else None)
