#!/usr/bin/env python3
"""
bracket.py -- exact Kauffman bracket <D> and Jones polynomial V(t) of a link
diagram given by a PD code.  Pure Python 3, no dependencies.

PD convention (KnotInfo / Knot Atlas / spherogram): each crossing is a list
[a, b, c, d] of the four edge labels met COUNTERCLOCKWISE around the crossing,
starting from the INCOMING UNDER-crossing edge.  So a -> c is the (oriented)
under strand and {b, d} is the over strand.  Every edge label appears exactly
twice in the code.  Labels may be any hashable objects (normally 1..2n).

Conventions pinned down by VALIDATION.md:
  * <X> = A <X_A> + A^-1 <X_B>,  <D u O> = delta <D>,  <O> = 1,
    delta = -A^2 - A^-2.
    For crossing [a,b,c,d]: A-smoothing joins (a,b) & (c,d);
                            B-smoothing joins (a,d) & (b,c).
  * crossing sign = +1 iff the over strand runs d -> b
    (equivalently b = d+1 in a consecutively numbered knot PD).
  * V(t) = (-A^3)^(-w) <D>,  t = A^-4,  hence t^(1/2) = A^-2.

Orientation of components is read off the under-crossings (a -> c).  A
component that never passes under anything has no such information; then the
edge numbering is used (labels increase along the orientation) and, failing
that, an arbitrary orientation is used and a warning is emitted (this can only
change V of a LINK by a unit, never the bracket).

Data types:
  * Laurent polynomials in A: dict {exponent(int): coefficient(int)}.
  * Jones polynomials: dict {k(int): coefficient(int)} meaning
        V = sum_k  c_k * t^(k/2)
    i.e. INTEGER KEYS ARE EXPONENTS OF t^(1/2).  For knots all keys are even;
    jones_t() converts to plain powers of t (keys k//2) when that holds.

Algorithm: planar-algebra contraction.  Crossings are absorbed one at a time
in a greedy order that keeps the set of "open" edges (edges with exactly one
end absorbed) small.  A state is a perfect matching of the open edges; each
state carries a Laurent polynomial.  Absorbing a crossing splits every state
into its A- and B-smoothings, concatenates arcs, and closes loops into factors
of delta.  Polynomials are stored as big Python ints (Kronecker substitution)
so that the inner loop runs at C speed; they are decoded exactly at the end.
"""

import sys
import json
import time
import warnings
from collections import defaultdict
from fractions import Fraction

# ----------------------------------------------------------------------
# Laurent polynomial helpers (dict exponent -> int)
# ----------------------------------------------------------------------

def pclean(p):
    return {e: c for e, c in p.items() if c}


def padd(p, q):
    r = dict(p)
    for e, c in q.items():
        v = r.get(e, 0) + c
        if v:
            r[e] = v
        else:
            r.pop(e, None)
    return r


def pneg(p):
    return {e: -c for e, c in p.items()}


def pscale(p, c):
    return pclean({e: c * v for e, v in p.items()})


def pshift(p, k):
    """Multiply by A^k."""
    return {e + k: c for e, c in p.items()}


def pmul(p, q):
    r = {}
    for e1, c1 in p.items():
        for e2, c2 in q.items():
            r[e1 + e2] = r.get(e1 + e2, 0) + c1 * c2
    return pclean(r)


def ppow(p, n):
    r = {0: 1}
    for _ in range(n):
        r = pmul(r, p)
    return r


DELTA = {2: -1, -2: -1}          # -A^2 - A^-2


def pdiv_delta(p):
    """Exact division by delta = -A^2 - A^-2 = -A^-2 (A^4 + 1).  Raises if
    the division is not exact."""
    if not p:
        return {}
    # p / delta = (-A^2 p) / (A^4 + 1)
    rem = pshift(pneg(p), 2)
    q = {}
    emin = min(rem)
    guard = 0
    while rem:
        e = max(rem)
        c = rem[e]
        if e - 4 < emin - 4:
            raise ArithmeticError("polynomial not divisible by delta")
        q[e - 4] = q.get(e - 4, 0) + c
        rem = padd(rem, {e: -c, e - 4: -c})
        guard += 1
        if guard > 10 ** 6:
            raise ArithmeticError("division did not terminate")
    return pclean(q)


def pstr(p, var="A"):
    """Pretty-print a Laurent polynomial with integer exponents."""
    if not p:
        return "0"
    out = []
    for e in sorted(p):
        c = p[e]
        if e == 0:
            term = str(abs(c))
        else:
            mag = "" if abs(c) == 1 else str(abs(c)) + "*"
            term = mag + (var if e == 1 else "%s^%d" % (var, e))
        out.append(("- " if c < 0 else "+ ") + term)
    s = " ".join(out)
    return s[2:] if s.startswith("+ ") else "-" + s[2:]


# ----------------------------------------------------------------------
# PD-code diagram: validation, components, orientation, writhe
# ----------------------------------------------------------------------

class Diagram:
    """A PD code with derived combinatorial data."""

    def __init__(self, pd):
        self.pd = [list(x) for x in pd]
        self.n = len(self.pd)
        occ = defaultdict(list)
        for i, x in enumerate(self.pd):
            if len(x) != 4:
                raise ValueError("crossing %d does not have 4 entries: %r" % (i, x))
            for s, e in enumerate(x):
                occ[e].append((i, s))
        for e, o in occ.items():
            if len(o) != 2:
                raise ValueError("edge label %r appears %d times (must be 2)" % (e, len(o)))
        self.occ = dict(occ)
        self.head = {}          # edge -> (crossing, slot) where it ENTERS
        self.tail = {}          # edge -> (crossing, slot) where it LEAVES
        self.components = []    # list of lists of edges, in orientation order
        self.comp_of = {}
        self.orientation_warning = None
        if self.n:
            self._orient()

    def other_end(self, i, s):
        e = self.pd[i][s]
        o = self.occ[e]
        return o[1] if o[0] == (i, s) else o[0]

    def _orient(self):
        done = set()
        for e0 in self.occ:
            if e0 in done:
                continue
            # tentative traversal: enter crossing at occ[e0][0]
            edges = []
            heads = {}
            tails = {}
            e = e0
            hd = self.occ[e0][0]
            while True:
                edges.append(e)
                heads[e] = hd
                i, s = hd
                s2 = (s + 2) % 4
                e2 = self.pd[i][s2]
                tails[e2] = (i, s2)
                hd2 = self.other_end(i, s2)
                e = e2
                hd = hd2
                if e == e0:
                    break
                if e in heads:
                    raise ValueError("PD code is not a valid 4-valent diagram")
            # evidence from under-crossings
            keep = flip = 0
            for e in edges:
                if heads[e][1] == 0:
                    keep += 1
                elif heads[e][1] == 2:
                    flip += 1
                if tails[e][1] == 2:
                    keep += 1
                elif tails[e][1] == 0:
                    flip += 1
            if keep and flip:
                raise ValueError("inconsistent under-strand orientation in PD code "
                                 "(component %r)" % (edges,))
            if not keep and not flip:
                # no under-crossings on this component: use edge numbering
                up = down = 0
                m = len(edges)
                for k in range(m):
                    a, b = edges[k], edges[(k + 1) % m]
                    if isinstance(a, int) and isinstance(b, int):
                        if b == a + 1:
                            up += 1
                        elif a == b + 1:
                            down += 1
                if up > down:
                    keep = 1
                elif down > up:
                    flip = 1
                else:
                    self.orientation_warning = ("component %r has no under-crossings and "
                                                "no usable edge numbering; orientation chosen "
                                                "arbitrarily" % (edges,))
                    warnings.warn(self.orientation_warning)
                    keep = 1
            if flip:
                edges = edges[::-1]
                heads, tails = tails, heads
            cid = len(self.components)
            self.components.append(edges)
            for e in edges:
                self.head[e] = heads[e]
                self.tail[e] = tails[e]
                self.comp_of[e] = cid
                done.add(e)

    def crossing_sign(self, i):
        a, b, c, d = self.pd[i]
        # positive iff over strand runs d -> b, i.e. edge b LEAVES at slot 1
        return 1 if self.tail[b] == (i, 1) else -1

    def signs(self):
        return [self.crossing_sign(i) for i in range(self.n)]

    def writhe(self):
        return sum(self.signs())

    def num_components(self):
        return len(self.components)

    def linking_matrix(self):
        """Pairwise linking numbers between components (dict (i,j)->lk)."""
        lk = defaultdict(int)
        for i in range(self.n):
            a, b, c, d = self.pd[i]
            ca, cb = self.comp_of[a], self.comp_of[b]
            if ca != cb:
                key = (min(ca, cb), max(ca, cb))
                lk[key] += self.crossing_sign(i)
        return {k: v // 2 for k, v in lk.items()}

    def faces(self):
        """Faces of the diagram as cyclic lists of darts (crossing, slot).
        Walking with the face on the LEFT: arriving at (i, s) we leave by
        slot s-1 (mod 4).  Returns list of faces; each face is a list of
        (edge, from_slot_pos, to_slot_pos)."""
        seen = set()
        faces = []
        for i in range(self.n):
            for s in range(4):
                if (i, s) in seen:
                    continue
                face = []
                cur = (i, s)        # dart: we are ARRIVING at cur
                while cur not in seen:
                    seen.add(cur)
                    ci, cs = cur
                    out = (ci, (cs - 1) % 4)
                    e = self.pd[ci][out[1]]
                    nxt = self.other_end(*out)
                    face.append((e, out, nxt))
                    cur = nxt
                faces.append(face)
        return faces


def pd_mirror(pd):
    """Mirror image (reflect the plane): reverses the counterclockwise order."""
    return [[a, d, c, b] for (a, b, c, d) in pd]


# ----------------------------------------------------------------------
# Greedy contraction order
# ----------------------------------------------------------------------

def _catalan(k):
    from math import comb
    return comb(2 * k, k) // (k + 1)


def greedy_order(pd, starts=None):
    """Choose a processing order of the crossings that keeps the number of
    open edges (the boundary width) small.  Tries every starting crossing
    (or the given list) and keeps the best profile."""
    n = len(pd)
    if n == 0:
        return [], 0
    occ = defaultdict(list)
    for i, x in enumerate(pd):
        for s, e in enumerate(x):
            occ[e].append(i)
    labels = [set(x) for x in pd]
    # count of occurrences of label e inside crossing i
    best = None
    if starts is None:
        starts = range(n)
    for start in starts:
        processed = [False] * n
        open_cnt = {}       # label -> number of processed occurrences (1 means open)
        order = [start]
        processed[start] = True
        for e in pd[start]:
            open_cnt[e] = open_cnt.get(e, 0) + 1
        width = sum(1 for v in open_cnt.values() if v == 1)
        maxw = width
        cost = _catalan(width // 2)
        unprocessed = set(range(n))
        unprocessed.discard(start)
        while unprocessed:
            bestj = None
            for j in unprocessed:
                delta = 0
                closed = 0
                for e in labels[j]:
                    k = pd[j].count(e)
                    if k == 2:
                        continue
                    if open_cnt.get(e, 0) == 1:
                        delta -= 1
                        closed += 1
                    else:
                        delta += 1
                key = (width + delta, -closed, j)
                if bestj is None or key < bestj:
                    bestj = key
            w2, _, j = bestj
            order.append(j)
            unprocessed.discard(j)
            processed[j] = True
            for e in pd[j]:
                open_cnt[e] = open_cnt.get(e, 0) + 1
            width = w2
            maxw = max(maxw, width)
            cost += _catalan(width // 2)
        key = (maxw, cost)
        if best is None or key < best[0]:
            best = (key, order)
    return best[1], best[0][0]


# ----------------------------------------------------------------------
# The contraction
# ----------------------------------------------------------------------

_ARC_A = (1, 0, 3, 2)   # A-smoothing: slots (0,1), (2,3)
_ARC_B = (3, 2, 1, 0)   # B-smoothing: slots (0,3), (1,2)


def kauffman_bracket(pd, order=None, stats=None):
    """Exact Kauffman bracket <D> (dict exponent->int in A) with <O> = 1."""
    pd = [list(x) for x in pd]
    n = len(pd)
    if n == 0:
        return {0: 1}
    D = Diagram(pd)          # validates
    if order is None:
        order, maxw = greedy_order(pd)
    else:
        maxw = None
    K = 2 * n + 8            # bits per coefficient (Kronecker substitution)
    OFF = 4 * n + 8          # exponent offset so all exponents are >= 1
    one = 1 << (OFF * K)
    processed = set()
    states = {(): one}
    max_states = 1
    for i in order:
        x = pd[i]
        edge_link = [None] * 4
        open_slot = {}
        for s in range(4):
            e = x[s]
            j, t = D.other_end(i, s)
            if j == i:
                edge_link[s] = (0, t)        # same crossing (kink)
            elif j in processed:
                edge_link[s] = (1, e)        # e is currently open
                open_slot[e] = s
            else:
                edge_link[s] = (2, e)        # e becomes a new open edge
        processed.add(i)
        new_states = {}
        for key, poly in states.items():
            P = {}
            for (u, v) in key:
                P[u] = v
                P[v] = u
            for sign, arc in ((1, _ARC_A), (-1, _ARC_B)):
                newP = dict(P)
                remaining = [True, True, True, True]
                loops = 0
                for s in range(4):
                    if not remaining[s]:
                        continue
                    remaining[s] = False
                    a_s = arc[s]
                    remaining[a_s] = False
                    ends = []
                    closed = False
                    for startslot, closing in ((s, a_s), (a_s, None)):
                        cur = startslot
                        while True:
                            kind, val = edge_link[cur]
                            if kind == 2:
                                ends.append(val)
                                break
                            if kind == 0:
                                t = val
                            else:
                                f = P[val]
                                newP.pop(val, None)
                                newP.pop(f, None)
                                t = open_slot.get(f)
                                if t is None:
                                    ends.append(f)
                                    break
                            if t == closing:
                                closed = True
                                break
                            remaining[t] = False
                            t2 = arc[t]
                            remaining[t2] = False
                            cur = t2
                        if closed:
                            break
                    if closed:
                        loops += 1
                    else:
                        e1, e2 = ends
                        newP[e1] = e2
                        newP[e2] = e1
                val = (poly << K) if sign == 1 else (poly >> K)
                for _ in range(loops):
                    val = -(val << (2 * K)) - (val >> (2 * K))
                k2 = tuple(sorted((u, v) for u, v in newP.items() if u < v))
                new_states[k2] = new_states.get(k2, 0) + val
        states = new_states
        if len(states) > max_states:
            max_states = len(states)
    if list(states.keys()) != [()]:
        raise RuntimeError("contraction did not close up: %r" % list(states.keys())[:5])
    N = states[()]
    # decode balanced base-2^K digits
    B = 1 << K
    half = B >> 1
    poly = {}
    e = -OFF
    while N:
        d = N & (B - 1)
        if d >= half:
            d -= B
        N = (N - d) >> K
        if d:
            poly[e] = d
        e += 1
    res = pdiv_delta(poly)
    if stats is not None:
        stats["max_states"] = max_states
        stats["max_width"] = maxw
        stats["order"] = order
    return res


# ----------------------------------------------------------------------
# Naive 2^n state sum (independent cross-check for small diagrams only)
# ----------------------------------------------------------------------

def kauffman_bracket_naive(pd):
    """Brute-force state sum over all 2^n smoothings.  Same conventions as
    kauffman_bracket(); use only for n <= ~16."""
    pd = [list(x) for x in pd]
    n = len(pd)
    if n == 0:
        return {0: 1}
    D = Diagram(pd)
    total = {}
    for mask in range(1 << n):
        parent = {}

        def find(u):
            while parent.get(u, u) != u:
                parent[u] = parent.get(parent[u], parent[u])
                u = parent[u]
            return u

        def union(u, v):
            ru, rv = find(u), find(v)
            if ru != rv:
                parent[ru] = rv

        na = 0
        for i, x in enumerate(pd):
            slots = [(i, s) for s in range(4)]
            if (mask >> i) & 1:
                na += 1
                union(slots[0], slots[1]); union(slots[2], slots[3])
            else:
                union(slots[0], slots[3]); union(slots[1], slots[2])
        for e, (p, q) in D.occ.items():
            union(p, q)
        roots = {find((i, s)) for i in range(n) for s in range(4)}
        loops = len(roots)
        term = pmul({na - (n - na): 1}, ppow(DELTA, loops - 1))
        total = padd(total, term)
    return total


# ----------------------------------------------------------------------
# Jones polynomial
# ----------------------------------------------------------------------

def jones_from_bracket(bracket, writhe):
    """V as dict {k: c} meaning sum c * t^(k/2)."""
    V = {}
    sgn = -1 if writhe % 2 else 1
    for e, c in bracket.items():
        e2 = e - 3 * writhe
        if e2 % 2:
            raise ArithmeticError("odd exponent after normalisation; invalid PD?")
        V[-e2 // 2] = sgn * c
    return V


def jones_from_pd(pd, stats=None):
    """Jones polynomial of the oriented link given by the PD code.

    Returns a dict {k: c} with INTEGER keys k meaning V = sum c * t^(k/2)
    (keys are exponents of t^(1/2); half-integer powers of t appear for links
    with an even number of components).  Use jones_t() to get powers of t."""
    pd = [list(x) for x in pd]
    if not pd:
        return {0: 1}
    D = Diagram(pd)
    br = kauffman_bracket(pd, stats=stats)
    w = D.writhe()
    if stats is not None:
        stats["writhe"] = w
        stats["components"] = D.num_components()
        stats["bracket"] = br
    return jones_from_bracket(br, w)


def jones_t(V):
    """Convert {k: c} (powers of t^(1/2)) to {m: c} powers of t.  Raises if a
    half-integer power is present."""
    out = {}
    for k, c in V.items():
        if k % 2:
            raise ValueError("half-integer power t^(%d/2) present" % k)
        out[k // 2] = c
    return out


def jones_str(V):
    """Pretty-print a Jones polynomial given in half-exponent form."""
    if not V:
        return "0"
    out = []
    for k in sorted(V):
        c = V[k]
        if k == 0:
            term = str(abs(c))
        else:
            mag = "" if abs(c) == 1 else str(abs(c)) + "*"
            if k % 2 == 0:
                m = k // 2
                term = mag + ("t" if m == 1 else "t^%d" % m)
            else:
                term = mag + "t^(%d/2)" % k
        out.append(("- " if c < 0 else "+ ") + term)
    s = " ".join(out)
    return s[2:] if s.startswith("+ ") else "-" + s[2:]


def jones_mirror(V):
    """t -> 1/t."""
    return {-k: c for k, c in V.items()}


def same_up_to_mirror(V1, V2):
    V1 = pclean(V1)
    V2 = pclean(V2)
    return V1 == V2 or V1 == jones_mirror(V2)


def parse_poly_t(s):
    """Parse strings like 't^-2 - t^-1 + 1 - t + t^2', '-q^-4+q^-3+q^-1',
    '2*t^3', '2t^3', 't^(5/2)', '-t^(-1/2)' into the half-exponent dict form."""
    import re
    s = s.replace(" ", "").replace("**", "^").replace("*", "").replace("q", "t")
    term_re = re.compile(r"([+-]?)(\d*)(t(?:\^\(?(-?\d+)(?:/(\d+))?\)?)?)?")
    V = {}
    pos = 0
    while pos < len(s):
        m = term_re.match(s, pos)
        if not m or m.end() == pos:
            raise ValueError("cannot parse %r at position %d" % (s, pos))
        sign, coef, var, ex, den = m.groups()
        if not coef and not var:
            raise ValueError("cannot parse %r at position %d" % (s, pos))
        c = int(coef) if coef else 1
        if sign == "-":
            c = -c
        if var:
            if ex is None:
                k = 2
            elif den:
                if int(den) != 2:
                    raise ValueError("only half-integer exponents supported: %r" % s)
                k = int(ex)
            else:
                k = 2 * int(ex)
        else:
            k = 0
        V[k] = V.get(k, 0) + c
        pos = m.end()
    return pclean(V)


def evaluate(V, t_half):
    """Evaluate V at a given value of t^(1/2) (any Python number)."""
    return sum(c * t_half ** k for k, c in V.items())


# ----------------------------------------------------------------------
# command line
# ----------------------------------------------------------------------

def _main(argv):
    if len(argv) < 2:
        print("usage: bracket.py FILE.json      (JSON list of crossings, or {\"pd\": [...]})")
        print("       bracket.py --pd '[[1,4,2,5],[3,6,4,1],[5,2,6,3]]'")
        return 1
    if argv[1] == "--pd":
        pd = json.loads(argv[2])
    else:
        with open(argv[1]) as fh:
            data = json.load(fh)
        pd = data["pd"] if isinstance(data, dict) else data
    stats = {}
    t0 = time.perf_counter()
    V = jones_from_pd(pd, stats=stats)
    dt = time.perf_counter() - t0
    print("crossings      :", len(pd))
    print("components     :", stats["components"])
    print("writhe         :", stats["writhe"])
    print("<D>            :", pstr(stats["bracket"]))
    print("V(t)           :", jones_str(V))
    print("V == 1         :", pclean(V) == {0: 1})
    print("max states     :", stats["max_states"], " max width:", stats["max_width"])
    print("time (s)       : %.3f" % dt)
    return 0


if __name__ == "__main__":
    sys.exit(_main(sys.argv))
