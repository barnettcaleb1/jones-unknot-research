#!/usr/bin/env python3
"""Referee tool (lens SIGNED SQUARE): two-box patterns as closed 'braid-like words'.

A word is a list of letters (pos, kind) read bottom to top on n strands:
   kind = +1 : sigma_pos       (twist.py convention; = A*id + A^-1*e in bracket.py's convention)
   kind = -1 : sigma_pos^-1    (= A^-1*id + A*e)
   kind = 'B1' / 'B2' : marked box on strands pos,pos+1.
Fillings of a box:  0 = id (two through strands),  1 = e (cup-cap).
In this labelling adding sigma_pos directly above a box acts on that slot's index by
M = [[A,0],[A^-1,-A^-3]]  (C -> M^T C for box 1, C -> C M for box 2), and the two-strand word [B1,B2] has C = G.
So index 0 <-> [Q_0], index 1 <-> [Q_inf] of the theorem under referee.

Three bracket evaluations:
  tl_bracket      : direct Temperley-Lieb state sum on the word (no PD code, independent of cx-tools)
  pd_bracket      : PD code via cx-tools twist.Builder, boxes smoothed by reconnection, cx-tools bracket.kauffman_bracket
  port_bracket    : my own brute-force state sum on the Builder port graph (independent of bracket.py's contraction)
All give the reduced raw bracket (<O> = 1, no writhe normalisation).
"""
import sys, itertools, math
from fractions import Fraction

CX = "/Users/calebbarnett/jones-lanes/cx-tools"
sys.dont_write_bytecode = True
if CX not in sys.path:
    sys.path.insert(0, CX)
from bracket import kauffman_bracket, padd, pmul, ppow, pshift, pscale, pclean, DELTA, pstr  # noqa
from twist import Builder  # noqa

# ---------------------------------------------------------------- Laurent helpers
def delta_pow(k, _cache={}):
    if k not in _cache:
        _cache[k] = ppow(DELTA, k)
    return _cache[k]

# ---------------------------------------------------------------- Q(zeta_8) exact
def z_eval(p):
    """Laurent dict -> element of Z[zeta_8] as 4 Fractions (basis 1,z,z^2,z^3; z^4=-1)."""
    v = [Fraction(0)] * 4
    for e, c in p.items():
        r = e % 8
        if r >= 4:
            v[r - 4] -= c
        else:
            v[r] += c
    return tuple(v)
def z_mul(a, b):
    v = [Fraction(0)] * 4
    for i in range(4):
        if a[i] == 0:
            continue
        for j in range(4):
            k = i + j
            if k >= 4:
                v[k - 4] -= a[i] * b[j]
            else:
                v[k] += a[i] * b[j]
    return tuple(v)
def z_sub(a, b):
    return tuple(x - y for x, y in zip(a, b))
def z_conj(a, k):
    """Galois conjugate z -> z^k, k odd."""
    v = [Fraction(0)] * 4
    for j in range(4):
        r = (j * k) % 8
        if r >= 4:
            v[r - 4] -= a[j]
        else:
            v[r] += a[j]
    return tuple(v)
def z_inv(a):
    o = z_mul(z_mul(z_conj(a, 3), z_conj(a, 5)), z_conj(a, 7))
    n = z_mul(a, o)
    assert n[1] == n[2] == n[3] == 0 and n[0] != 0
    return tuple(x / n[0] for x in o)
def z_iszero(a):
    return all(x == 0 for x in a)
def z_abs2_is_one(a):
    """|a|^2 == 1 for the standard embedding: a * conj_7(a) == 1."""
    n = z_mul(a, z_conj(a, 7))
    return n == (1, 0, 0, 0)
def is_square_fraction(r):
    if r < 0:
        return False
    n, d = r.numerator, r.denominator
    return math.isqrt(n) ** 2 == n and math.isqrt(d) ** 2 == d

# ---------------------------------------------------------------- TL-direct state sum
def tl_bracket(word, n, fill, closure="braid"):
    """Reduced raw bracket of the closure of the word with boxes filled by fill={'B1':0/1,'B2':0/1}."""
    L = len(word)
    cross = [k for k, (pos, kind) in enumerate(word) if kind in (1, -1)]
    total = {}
    nc = len(cross)
    def node(l, k):          # level l in 0..L, position k in 1..n
        if closure == "braid" and l == L:
            l = 0
        return l * (n + 1) + k
    for mask in range(1 << nc):
        parent = {}
        def find(u):
            while parent.get(u, u) != u:
                parent[u] = parent.get(parent[u], parent[u]); u = parent[u]
            return u
        def union(u, v):
            ru, rv = find(u), find(v)
            if ru != rv:
                parent[ru] = rv
        expo = 0
        choice = {}
        for b, k in enumerate(cross):
            pos, kind = word[k]
            is_id = (mask >> b) & 1
            choice[k] = is_id
            # sigma: id has weight A, e weight A^-1; sigma^-1: reversed
            expo += (1 if is_id else -1) * kind
        for l, (pos, kind) in enumerate(word):
            if kind in (1, -1):
                is_id = choice[l]
            else:
                is_id = (fill[kind] == 0)
            for k in range(1, n + 1):
                if k in (pos, pos + 1) and not is_id:
                    continue
                union(node(l, k), node(l + 1, k))
            if not is_id:
                union(node(l, pos), node(l, pos + 1))
                union(node(l + 1, pos), node(l + 1, pos + 1))
        if closure == "plat":
            for k in range(1, n + 1, 2):
                union(node(0, k), node(0, k + 1))
                union(node(L, k), node(L, k + 1))
        levels = range(L) if closure == "braid" else range(L + 1)
        if L == 0 and closure == "braid":
            levels = range(1)
        roots = {find(node(l, k)) for l in levels for k in range(1, n + 1)}
        term = pshift(delta_pow(len(roots) - 1), expo)
        total = padd(total, term)
    return pclean(total)

def tl_tensor(word, n, closure="braid"):
    return [[tl_bracket(word, n, {'B1': i, 'B2': j}, closure) for j in range(2)] for i in range(2)]

# ---------------------------------------------------------------- PD route (cx-tools)
_SIGMA = {"BR": 0, "TR": 1, "TL": 2, "BL": 3}
_SIGMA_INV = {"BL": 0, "BR": 1, "TR": 2, "TL": 3}
def build(word, n, closure="braid"):
    """Builder with boxes as sigma-type crossings; returns (builder, boxes{name:crossing}, free_strands)."""
    b = Builder()
    top = [None] * (n + 1); bottom = [None] * (n + 1)
    boxes = {}
    for pos, kind in word:
        c = b.new_crossing()
        if kind in (1, -1):
            slot = _SIGMA if kind == 1 else _SIGMA_INV
        else:
            slot = _SIGMA; boxes[kind] = c
        for p, port in ((pos, "BL"), (pos + 1, "BR")):
            entry = (c, slot[port])
            if top[p] is None:
                bottom[p] = entry
            else:
                b.connect(top[p], entry)
        top[pos] = (c, slot["TL"]); top[pos + 1] = (c, slot["TR"])
    free = 0
    if closure == "braid":
        for k in range(1, n + 1):
            if top[k] is None:
                free += 1
            else:
                b.connect(top[k], bottom[k])
    else:
        for k in range(1, n + 1, 2):
            if top[k] is None and top[k + 1] is None:
                free += 1
            elif top[k] is None:
                b.connect(bottom[k + 1], top[k + 1])
            elif top[k + 1] is None:
                b.connect(bottom[k], top[k])
            else:
                b.connect(bottom[k], bottom[k + 1]); b.connect(top[k], top[k + 1])
    return b, boxes, free

_PARTNER = {0: {0: 1, 1: 0, 2: 3, 3: 2},      # filling 0 = id = A-type join (slots 0-1, 2-3) of a sigma-type box
            1: {0: 3, 3: 0, 1: 2, 2: 1}}      # filling 1 = e  = B-type join (slots 0-3, 1-2)
def resolve(b, boxes, fill):
    """Smooth the boxes. Returns (new Builder or None, None); free loops are counted by free_loop_count."""
    boxc = {c: fill[name] for name, c in boxes.items()}
    keep = [c for c in range(b.ncross) if c not in boxc]
    idx = {c: k for k, c in enumerate(keep)}
    nb = Builder(); nb.ncross = len(keep)
    for c in keep:
        for s in range(4):
            p = (c, s)
            q = b.conn[p]
            while q[0] in boxc:
                q = b.conn[(q[0], _PARTNER[boxc[q[0]]][q[1]])]
            np_, nq = (idx[c], s), (idx[q[0]], q[1])
            if np_ not in nb.conn:
                nb.connect(np_, nq)
    return (nb if keep else None), None

def free_loop_count(b, boxes, fill):
    """Robust count of components that contain no outside-crossing port (union-find)."""
    boxc = {c: fill[name] for name, c in boxes.items()}
    parent = {}
    def find(u):
        while parent.get(u, u) != u:
            parent[u] = parent.get(parent[u], parent[u]); u = parent[u]
        return u
    def union(u, v):
        ru, rv = find(u), find(v)
        if ru != rv:
            parent[ru] = rv
    for p, q in b.conn.items():
        union(p, q)
    for c, f in boxc.items():
        for s, t in _PARTNER[f].items():
            union((c, s), (c, t))
    outside_roots = {find((c, s)) for c in range(b.ncross) if c not in boxc for s in range(4)}
    box_roots = {find((c, s)) for c in boxc for s in range(4)}
    return len(box_roots - outside_roots)

def pd_bracket(word, n, fill, closure="braid", return_pd=False):
    b, boxes, free = build(word, n, closure)
    nb, _ = resolve(b, boxes, fill)
    loops = free + free_loop_count(b, boxes, fill)
    if nb is None:
        val = delta_pow(loops - 1)
        return (val, []) if return_pd else val
    pd = nb.pd_code()
    val = pmul(kauffman_bracket(pd), delta_pow(loops))
    return (val, pd) if return_pd else val

def pd_tensor(word, n, closure="braid"):
    return [[pd_bracket(word, n, {'B1': i, 'B2': j}, closure) for j in range(2)] for i in range(2)]

def port_bracket(word, n, fill, closure="braid"):
    """Own brute-force state sum on the Builder port graph (slots 0-1,2-3 joined = A-smoothing, weight A)."""
    b, boxes, free = build(word, n, closure)
    boxc = {c: fill[name] for name, c in boxes.items()}
    outs = [c for c in range(b.ncross) if c not in boxc]
    total = {}
    for mask in range(1 << len(outs)):
        parent = {}
        def find(u):
            while parent.get(u, u) != u:
                parent[u] = parent.get(parent[u], parent[u]); u = parent[u]
            return u
        def union(u, v):
            ru, rv = find(u), find(v)
            if ru != rv:
                parent[ru] = rv
        for p, q in b.conn.items():
            union(p, q)
        expo = 0
        for k, c in enumerate(outs):
            if (mask >> k) & 1:
                expo += 1; union((c, 0), (c, 1)); union((c, 2), (c, 3))
            else:
                expo -= 1; union((c, 0), (c, 3)); union((c, 1), (c, 2))
        for c, f in boxc.items():
            for s, t in _PARTNER[f].items():
                union((c, s), (c, t))
        roots = {find((c, s)) for c in range(b.ncross) for s in range(4)}
        total = padd(total, pshift(delta_pow(len(roots) + free - 1), expo))
    return pclean(total)

# ---------------------------------------------------------------- the sign test at zeta_8
def analyse(C):
    """C: 2x2 of Laurent dicts. Returns dict with exact zeta_8 data and the sign-law verdict.
    Law under test: for every corner (i,j) with C_ij(zeta) != 0,
        (-1)^(i+j) det C(zeta) / C_ij(zeta)^2  is a nonnegative rational square,
    and an integer square if |C_ij(zeta)| = 1."""
    Z = [[z_eval(C[i][j]) for j in range(2)] for i in range(2)]
    det = z_sub(z_mul(Z[0][0], Z[1][1]), z_mul(Z[0][1], Z[1][0]))
    res = {"Z": Z, "det": det, "anchors": {}, "ok": True, "nonzero": False}
    for i in range(2):
        for j in range(2):
            if z_iszero(Z[i][j]):
                continue
            res["nonzero"] = True
            r = z_mul(det, z_inv(z_mul(Z[i][j], Z[i][j])))
            rational = (r[1] == 0 and r[2] == 0 and r[3] == 0)
            unit = z_abs2_is_one(Z[i][j])
            ok = rational and is_square_fraction((-1) ** (i + j) * r[0]) and (not unit or r[0].denominator == 1)
            res["anchors"][(i, j)] = {"ratio": r, "rational": rational, "unit": unit, "ok": ok}
            if not ok:
                res["ok"] = False
    return res

def zstr(a):
    names = ["", "z", "z^2", "z^3"]
    out = []
    for c, nm in zip(a, names):
        if c:
            out.append(("%s*%s" % (c, nm)) if nm else str(c))
    return " + ".join(out) if out else "0"
