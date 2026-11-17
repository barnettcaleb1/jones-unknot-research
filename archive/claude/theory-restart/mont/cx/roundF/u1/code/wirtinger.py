"""wirtinger.py -- presentations of pi_1(S^3 - K).

Words: tuples of nonzero ints, +g = generator g, -g = its inverse (generators are positive ints).

WIRTINGER (from an oriented PD code, see diagram.py).  Arcs = classes of edge labels under over_in ~ over_out at every
crossing.  Every arc begins at exactly one crossing, as the OUTGOING UNDER edge c of that crossing; the arc that begins at
crossing k is generator k+1 (canonical labelling, independent of how the PD code was produced).  Relator of crossing k with
over arc o, incoming under arc i, outgoing under arc k+1 and sign s:
        r_k = x_{k+1}^-1 . x_o^s . x_i . x_o^-s          (i.e. x_out = x_o^s x_in x_o^-s).
Soundness of the global sign choice: with the other choice (x_out = x_o^-s x_in x_o^s at every crossing) one gets the
Wirtinger presentation of the REFLECTED diagram (same arcs, all signs flipped) = a diagram of the mirror image; the two
groups are pi_1 of homeomorphic complements.  Either way the presentation presents pi_1(S^3 - K) up to isomorphism.
What must be (and is) uniform is the rule as a function of the sign.

PLAT / BRIDGE (from the Morse word, exact Artin action on free groups, independent of the PD code): sweep the word keeping,
for every strand position, the word of the loop around that strand (loops based at the viewer, left-to-right product
= loop around both).  Cap -> new generator g, strands g, g^-1.  Crossing 'x' (over TL->BR): (w_i, w_i+1) ->
(w_i w_i+1 w_i^-1, w_i);  'y' (over TR->BL): (w_i, w_i+1) -> (w_i+1, w_i+1^-1 w_i w_i+1)   [the over strand keeps its word,
the product w_i w_i+1 is preserved].  Cup at i -> relator w_i w_i+1.  (The mirror rule = reflected diagram, as above.)
"""
import sys
from diagram import PD, UF


def red(w):
    out = []
    for a in w:
        if out and out[-1] == -a: out.pop()
        else: out.append(a)
    return tuple(out)


def inv(w): return tuple(-a for a in reversed(w))


def wirtinger(pd):
    """(gens, rels) for an oriented PD code with n >= 1 crossings; for n = 0 returns ([1], [])."""
    n = pd.n
    if n == 0: return [1], []
    m = 2 * n
    uf = UF()
    for e in range(m): uf.find(e)
    for k in range(n):
        uf.union(pd.over_in(k), pd.over_out(k))
    start = {}
    for k, (a, b, c, d) in enumerate(pd.X):
        r = uf.find(c)
        if r in start: raise ValueError('arc begins twice')
        start[r] = k + 1
    if len(start) != len(set(uf.find(e) for e in range(m))): raise ValueError('arc without beginning')
    gens = list(range(1, n + 1)); rels = []
    for k, (a, b, c, d) in enumerate(pd.X):
        s = pd.sign[k]
        o = start[uf.find(b)]; i = start[uf.find(a)]; out = k + 1
        r = (-out,) + ((o,) if s > 0 else (-o,)) + (i,) + ((-o,) if s > 0 else (o,))
        rels.append(r)
    return gens, rels


def plat(full):
    """(gens, rels, orient) from the Morse word (list of (c,i)).  orient[g] = +1/-1: abelianisation exponent of the cap
    generator g (+1 if the left strand of its cap runs downwards in the knot orientation induced by ... ) -- computed
    afterwards by plat_abelianisation; here None."""
    g = 1
    pos = [(g,), (-g,)]
    gens = [g]; rels = []
    for c, i in full:
        if c in 'lr':
            g += 1; gens.append(g)
            pos[i:i] = [(g,), (-g,)]
        elif c == 'u':
            rels.append(red(pos[i] + pos[i + 1]))
            del pos[i:i + 2]
        elif c == 'x':
            a, b = pos[i], pos[i + 1]
            pos[i], pos[i + 1] = red(a + b + inv(a)), a
        elif c == 'y':
            a, b = pos[i], pos[i + 1]
            pos[i], pos[i + 1] = b, red(inv(b) + a + b)
        else:
            raise ValueError(c)
    assert not pos
    return gens, rels


def abelianisation(gens, rels):
    """For a knot group presentation: integer vector v (gcd 1) with sum of exponents of each relator = 0, i.e. the map
    to H_1 = Z.  Returns dict g -> v_g (up to global sign), or None if the exponent-sum matrix does not have corank 1."""
    from fractions import Fraction
    idx = {g: j for j, g in enumerate(gens)}
    n = len(gens)
    rows = []
    for r in rels:
        row = [0] * n
        for s in r: row[idx[abs(s)]] += 1 if s > 0 else -1
        rows.append([Fraction(x) for x in row])
    # row reduce
    piv = []; R = [r[:] for r in rows]; rk = 0
    for col in range(n):
        p = next((i for i in range(rk, len(R)) if R[i][col] != 0), None)
        if p is None: continue
        R[rk], R[p] = R[p], R[rk]
        pv = R[rk][col]
        R[rk] = [x / pv for x in R[rk]]
        for i in range(len(R)):
            if i != rk and R[i][col] != 0:
                f = R[i][col]
                R[i] = [x - f * y for x, y in zip(R[i], R[rk])]
        piv.append(col); rk += 1
    free = [c for c in range(n) if c not in piv]
    if len(free) != 1: return None
    fc = free[0]
    v = [Fraction(0)] * n; v[fc] = Fraction(1)
    for i, col in enumerate(piv):
        v[col] = -R[i][fc]
    from math import gcd
    den = 1
    for x in v: den = den * x.denominator // gcd(den, x.denominator)
    iv = [int(x * den) for x in v]
    gg = 0
    for x in iv: gg = gcd(gg, abs(x))
    iv = [x // gg for x in iv]
    return {g: iv[idx[g]] for g in gens}


def check_hom(gens, rels, images, mul, inverse, identity):
    """images: dict g -> element; returns True iff every relator maps to identity."""
    for r in rels:
        acc = identity
        for s in r:
            x = images[abs(s)]
            acc = mul(acc, x if s > 0 else inverse(x))
        if acc != identity: return False
    return True
