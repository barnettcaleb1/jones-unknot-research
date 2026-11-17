"""a2lib.py -- AUDIT-2 independent infrastructure (imports NOTHING from cert/).

Knots are given either as
  * a Morse word  full = [(c, i), ...]  (start: one cap on positions 0,1; ('l'|'r', i) cap inserting strands i,i+1;
    ('u', i) cup joining i,i+1; ('x'|'y', i) crossing of strands i,i+1; 'x': the strand from slot (before,i) to
    (after,i+1) is OVER; 'y': the strand from (before,i+1) to (after,i) is OVER).  This is the project definition
    of the knot of a halfword: full = alex.symmetrize(alex.parse(halfword)) (tools/alex.py, the trusted definition).
  * a PD code (0-based labels, consecutive along the orientation, X[k] = (a,b,c,d) ccw from the incoming under edge).

Everything here is written from scratch for the audit: Morse sweep -> oriented crossings -> arcs -> Wirtinger
presentation (with the README's labelling: generator k+1 = arc beginning at crossing k as outgoing under edge, so
that certificates of the certifier can be checked against it), Kauffman bracket by a Morse sweep, Alexander
polynomial values by Fox calculus, an independent Tietze replayer (README move spec), and a rep checker.
"""
import sys, random
from fractions import Fraction

TOOLS = '/Users/calebbarnett/jones-lanes/theory-restart/tools'
if TOOLS not in sys.path: sys.path.insert(0, TOOLS)
import alex      # ONLY for the definition of K (symmetrize/parse); trusted project tool


def full_of(halfword):
    return alex.symmetrize(alex.parse(halfword))


# ------------------------------------------------------------------ Morse word -> oriented knot diagram
SLOTPOS = {'TL': (-1, -1), 'TR': (1, -1), 'BR': (1, 1), 'BL': (-1, 1)}   # upward picture: before = lower
OPPS = {'TL': 'BR', 'BR': 'TL', 'TR': 'BL', 'BL': 'TR'}


def morse_diagram(full):
    """Returns dict with crossings (Morse order) and the traversal, or None if the word is invalid / not a knot.
    Independent re-implementation (union-find on segments)."""
    par = {}

    def find(a):
        while par.get(a, a) != a:
            par[a] = par.get(par[a], par[a]); a = par[a]
        return a

    nid = [0]

    def new():
        nid[0] += 1; return nid[0]
    e0 = new(); pos = [e0, e0]
    cr = []
    for c, i in full:
        if i < 0: return None
        if c in 'xy':
            if i + 1 >= len(pos): return None
            a, b = pos[i], pos[i + 1]
            bl, br = new(), new()
            pos[i], pos[i + 1] = bl, br
            cr.append({'ty': c, 'TL': a, 'TR': b, 'BL': bl, 'BR': br})
        elif c in 'lr':
            if i > len(pos): return None
            e = new(); pos[i:i] = [e, e]
        elif c == 'u':
            if i + 1 >= len(pos): return None
            x, y = find(pos[i]), find(pos[i + 1])
            if x != y: par[x] = y
            del pos[i:i + 2]
        else:
            return None
    if pos: return None
    n = len(cr)
    allseg = set(find(e) for e in range(1, nid[0] + 1))
    if n == 0:
        return {'n': 0, 'ncomp': len(allseg)}
    ends = {}
    for k, x in enumerate(cr):
        for s in ('TL', 'TR', 'BL', 'BR'):
            r = find(x[s]); x[s] = r
            ends.setdefault(r, []).append((k, s))
    if any(len(v) != 2 for v in ends.values()): return None
    if set(ends) != allseg: return None          # a crossing-free closed loop exists -> link
    # traversal: start on the over strand of crossing 0 at its 'before' slot
    s0 = 'TL' if cr[0]['ty'] == 'x' else 'TR'
    trav = []                                     # list of (k, slot_in, slot_out, is_over)
    k, s = 0, s0
    seen = set()
    while (k, s) not in seen:
        seen.add((k, s))
        o = OPPS[s]
        ty = cr[k]['ty']
        over = (s in ('TL', 'BR')) if ty == 'x' else (s in ('TR', 'BL'))
        trav.append((k, s, o, over))
        e = cr[k][o]
        p, q = ends[e]
        nxt = q if p == (k, o) else p
        if p == q: return None
        k, s = nxt
    if (k, s) != (0, s0) or len(trav) != 2 * n: return None
    return {'n': n, 'cr': cr, 'trav': trav}


def arcs_signs(D):
    """From morse_diagram output: for each crossing k: over arc gen, in-under gen, out-under gen (= k+1), sign."""
    n = D['n']; trav = D['trav']
    # the arc label at each traversal step: arcs begin at under passages
    L = len(trav)
    first_under = next(j for j in range(L) if not trav[j][3])
    cur = None
    over_arc = {}; in_arc = {}; out_arc = {}
    for jj in range(L + 1):
        j = (first_under + jj) % L
        k, si, so, ov = trav[j]
        if ov:
            over_arc[k] = cur; ovdir = None
        else:
            if cur is not None: in_arc[k] = cur
            if jj < L: cur = k + 1; out_arc[k] = k + 1
    sign = {}
    for k in range(n):
        dirs = {}
        for (kk, si, so, ov) in trav:
            if kk == k:
                a, b = SLOTPOS[si], SLOTPOS[so]
                dirs[ov] = (b[0] - a[0], b[1] - a[1])
        o, u = dirs[True], dirs[False]
        cz = o[0] * u[1] - o[1] * u[0]
        sign[k] = 1 if cz > 0 else -1
    return over_arc, in_arc, out_arc, sign


def wirtinger_from_full(full, flip=False):
    D = morse_diagram(full)
    if D is None: return None
    if D['n'] == 0: return [1], []
    over_arc, in_arc, out_arc, sign = arcs_signs(D)
    n = D['n']
    rels = []
    for k in range(n):
        s = sign[k] * (-1 if flip else 1)
        o, i, out = over_arc[k], in_arc[k], out_arc[k]
        rels.append((-out, o * s, i, -o * s))
    return list(range(1, n + 1)), rels


def wirtinger_from_halfword(hw, flip=False):
    return wirtinger_from_full(full_of(hw), flip)


# ------------------------------------------------------------------ PD codes
def pd_from_full(full):
    """Oriented PD (0-based consecutive labels, ccw from incoming under) in the upward picture, plus signs."""
    D = morse_diagram(full)
    if D is None or D['n'] == 0: return None
    n = D['n']; trav = D['trav']
    lab = {}
    for j, (k, si, so, ov) in enumerate(trav):
        lab[(k, si)] = j
        lab[(k, so)] = (j + 1) % (2 * n)
    CCW = ('TL', 'TR', 'BR', 'BL')
    X = []; sg = []
    for k in range(n):
        uin = [si for (kk, si, so, ov) in trav if kk == k and not ov][0]
        st = CCW.index(uin)
        order = [CCW[(st + t) % 4] for t in range(4)]
        X.append(tuple(lab[(k, s)] for s in order))
    for k, (a, b, c, d) in enumerate(X):
        sg.append(1 if b == (d + 1) % (2 * n) else -1)
    return X, sg


def pd_signs(X):
    m = 2 * len(X)
    out = []
    for (a, b, c, d) in X:
        if b == (d + 1) % m and d != (b + 1) % m: out.append(1)
        elif d == (b + 1) % m and b != (d + 1) % m: out.append(-1)
        else: raise ValueError('ambiguous sign')
    return out


def wirtinger_from_pd(X, sg=None, flip=False):
    n = len(X)
    if sg is None: sg = pd_signs(X)
    m = 2 * n
    par = list(range(m))

    def find(a):
        while par[a] != a:
            par[a] = par[par[a]]; a = par[a]
        return a
    for (a, b, c, d) in X:
        x, y = find(b), find(d)
        if x != y: par[x] = y
    start = {}
    for k, (a, b, c, d) in enumerate(X):
        r = find(c)
        assert r not in start
        start[r] = k + 1
    rels = []
    for k, (a, b, c, d) in enumerate(X):
        s = sg[k] * (-1 if flip else 1)
        o = start[find(b)]; i = start[find(a)]
        rels.append((-(k + 1), o * s, i, -o * s))
    return list(range(1, n + 1)), rels


def pd_components(X):
    """number of components of a PD code given with arbitrary labels (strands a-c and b-d)."""
    occ = {}
    for k, x in enumerate(X):
        for j, e in enumerate(x): occ.setdefault(e, []).append((k, j))
    seen = set(); comps = 0
    for k in range(len(X)):
        for j in range(4):
            if (k, j) in seen: continue
            comps += 1
            cur = (k, j)
            while cur not in seen:
                seen.add(cur)
                kk, jj = cur
                opp = (kk, (jj + 2) % 4); seen.add(opp)
                e = X[kk][(jj + 2) % 4]
                p, q = occ[e]
                cur = q if p == opp else p
    return comps


def faces_count(X):
    occ = {}
    for k, x in enumerate(X):
        for j, e in enumerate(x): occ.setdefault(e, []).append((k, j))
    other = {}
    for e, l in occ.items():
        (k1, j1), (k2, j2) = l
        other[(k1, j1)] = (k2, j2); other[(k2, j2)] = (k1, j1)
    seen = set(); nf = 0
    for k in range(len(X)):
        for j in range(4):
            if (k, j) in seen: continue
            nf += 1; cur = (k, j)
            while cur not in seen:
                seen.add(cur)
                k2, j2 = other[cur]
                cur = (k2, (j2 - 1) % 4)
    return nf


def relabel_pd(X):
    """Take a PD code with arbitrary labels describing ONE component and relabel 0..2n-1 consecutively along an
    orientation that agrees with the under strands' a->c directions where possible.  Returns (X', signs)."""
    n = len(X)
    occ = {}
    for k, x in enumerate(X):
        for j, e in enumerate(x): occ.setdefault(e, []).append((k, j))
    # traverse starting at crossing 0 slot 0 (incoming under) going through to slot 2
    lab = {}
    k, j = 0, 0
    L = 0
    while (k, j) not in lab:
        lab[(k, j)] = L
        jo = (j + 2) % 4
        lab[(k, jo)] = (L + 1) % (2 * n)
        e = X[k][jo]
        p, q = occ[e]
        nxt = q if p == (k, jo) else p
        k, j = nxt; L += 1
    if L != 2 * n: raise ValueError('not a knot')
    Y = []
    for kk in range(n):
        labs = [lab[(kk, t)] for t in range(4)]
        # incoming under slot: under strand = slots 0,2 ; incoming is the one whose label +1 = the other
        if (labs[0] + 1) % (2 * n) == labs[2]: st = 0
        else: st = 2
        Y.append(tuple(labs[(st + t) % 4] for t in range(4)))
    return Y, pd_signs(Y)


def mirror_pd(X):
    """switch every crossing: (a,b,c,d) -> over/under exchanged.  Returns relabelled oriented PD."""
    # the over strand b-d becomes under: new tuple read ccw from the incoming end of b-d
    m = 2 * len(X)
    Y = []
    for (a, b, c, d) in X:
        if b == (d + 1) % m: Y.append((d, a, b, c))
        else: Y.append((b, c, d, a))
    return relabel_pd(Y)


# ------------------------------------------------------------------ Kauffman bracket by a Morse sweep (independent)
def _padd(p, q, c=1):
    for e, v in q.items():
        nv = p.get(e, 0) + c * v
        if nv: p[e] = nv
        else: p.pop(e, None)


def _sh(p, k): return {e + k: v for e, v in p.items()}


def _dl(p):
    r = {}
    _padd(r, _sh(p, 2), -1); _padd(r, _sh(p, -2), -1); return r


def bracket_full(full):
    """<D> / delta-normalised Kauffman bracket (poly in A) of the Morse diagram, by sweeping planar matchings.
    Smoothing weights for the UPWARD picture: at 'x' (TL-BR over) the A-smoothing joins ... (calibrated by the trefoil
    test in selftest()).  Returns dict exponent->coeff of <D> with <O> = 1."""
    # state: tuple m of partner indices for the current open strands
    state = {(1, 0): {0: 1}}
    for c, i in full:
        new = {}
        for m, p in state.items():
            if c in 'lr':
                mm = [(x + 2 if x >= i else x) for x in m]
                mm[i:i] = [i + 1, i]
                _padd(new.setdefault(tuple(mm), {}), p)
            elif c == 'u':
                a, b = m[i], m[i + 1]
                mm = list(m)
                if a == i + 1:
                    loop = True
                else:
                    loop = False; mm[a] = b; mm[b] = a
                del mm[i:i + 2]
                mm = [(x - 2 if x > i + 1 else x) for x in mm]
                _padd(new.setdefault(tuple(mm), {}), _dl(p) if loop else p)
            else:
                wv, wh = (1, -1) if c == 'x' else (-1, 1)      # vertical (identity) / horizontal (cup-cap) smoothing
                _padd(new.setdefault(m, {}), _sh(p, wv))
                a, b = m[i], m[i + 1]
                mm = list(m)
                if a == i + 1:
                    loop = True
                else:
                    loop = False; mm[a] = b; mm[b] = a
                del mm[i:i + 2]
                mm = [(x - 2 if x > i + 1 else x) for x in mm]
                mm = [(x + 2 if x >= i else x) for x in mm]
                mm[i:i] = [i + 1, i]
                _padd(new.setdefault(tuple(mm), {}), _sh(_dl(p) if loop else p, wh))
        state = {m: p for m, p in new.items() if p}
    p = state.get((), {})
    # p = <D> with the outermost loop counted as delta: divide by delta
    r = {}; p = dict(p)
    while p:
        e = max(p); v = p[e]
        r[e - 2] = -v
        _padd(p, {e: -v, e - 4: -v})
    return r


def jones_unit_test(br):
    """True iff the bracket is a monomial +-A^k  (<=> V_K = 1 for a knot)."""
    return len(br) == 1 and abs(next(iter(br.values()))) == 1


def VK_from_bracket(br, writhe=None):
    """V up to the t^k/sign ambiguity fixed by V(1)=1, V'(1)=0 (exponents of t = A^-4)."""
    es = sorted(br); r = es[0] % 4
    if any((e - r) % 4 for e in es): return None
    V = {-(e - r) // 4: c for e, c in br.items()}
    s = sum(V.values())
    if s not in (1, -1): return None
    V = {e: c * s for e, c in V.items()}
    d = sum(e * c for e, c in V.items())
    return {e - d: c for e, c in V.items()}


# ------------------------------------------------------------------ Alexander values by Fox calculus (exact, at integers)
def fox_det_at(gens, rels, tval, p=None):
    """|det| of the Alexander matrix (Fox derivatives, all gens -> t) with last row/col deleted, at integer t
    (exact via Fractions, or mod p)."""
    idx = {g: j for j, g in enumerate(gens)}
    n = len(gens)
    M = []
    for r in rels:
        row = [0] * n
        acc = 1   # value of the prefix under abelianisation (t^(sum exps))
        for a in r:
            g = abs(a); j = idx[g]
            if a > 0:
                row[j] += acc; acc *= tval
            else:
                acc = Fraction(acc) / tval if p is None else acc * pow(tval, -1, p)
                row[j] -= acc
        M.append(row)
    m = [row[:-1] for row in M[:-1]]
    if p is None:
        m = [[Fraction(x) for x in row] for row in m]
        det = Fraction(1); N = len(m)
        for c in range(N):
            piv = next((rr for rr in range(c, N) if m[rr][c] != 0), None)
            if piv is None: return 0
            if piv != c: m[c], m[piv] = m[piv], m[c]; det = -det
            det *= m[c][c]
            for rr in range(c + 1, N):
                f = m[rr][c] / m[c][c]
                if f:
                    for cc in range(c, N): m[rr][cc] -= f * m[c][cc]
        return abs(det)
    else:
        m = [[x % p for x in row] for row in m]
        det = 1; N = len(m)
        for c in range(N):
            piv = next((rr for rr in range(c, N) if m[rr][c] % p), None)
            if piv is None: return 0
            if piv != c: m[c], m[piv] = m[piv], m[c]; det = -det
            det = det * m[c][c] % p
            iv = pow(m[c][c], -1, p)
            for rr in range(c + 1, N):
                f = m[rr][c] * iv % p
                if f:
                    for cc in range(c, N): m[rr][cc] = (m[rr][cc] - f * m[c][cc]) % p
        return det % p


def alex_trivial_evidence(gens, rels):
    """|Delta(t)| up to units at t = -1, 2, 3, 5 (Fraction values; a power of t is stripped)."""
    out = {}
    for tv in (-1, 2, 3, 5):
        v = fox_det_at(gens, rels, tv)
        v = abs(v)
        if v:
            # strip powers of |t|
            while v.numerator % abs(tv) == 0 and abs(tv) > 1: v = v / abs(tv)
            while v.denominator % abs(tv) == 0 and abs(tv) > 1: v = v * abs(tv)
        out[tv] = v
    return out


# ------------------------------------------------------------------ free-group words, canonical form, replay
def red(w):
    out = []
    for a in w:
        if out and out[-1] == -a: out.pop()
        else: out.append(a)
    return tuple(out)


def inv(w): return tuple(-a for a in reversed(w))


def cycred(w):
    w = list(red(w))
    i, j = 0, len(w) - 1
    while i < j and w[i] == -w[j]: i += 1; j -= 1
    return tuple(w[i:j + 1])


def least_rot(w):
    if not w: return w
    return min(tuple(w[k:] + w[:k]) for k in range(len(w)))


def canon_word(w):
    w = cycred(w)
    if not w: return w
    return min(least_rot(w), least_rot(inv(w)))


def canon_pres(gens, rels):
    rs = set()
    for r in rels:
        c = canon_word(r)
        if c: rs.add(c)
    return sorted(gens), sorted(rs, key=lambda r: (len(r), r))


def subst(w, g, img):
    out = []
    ig = inv(img)
    for a in w:
        if a == g: out.extend(img)
        elif a == -g: out.extend(ig)
        else: out.append(a)
    return red(tuple(out))


def rotl(w, k):
    if not w: return w
    k %= len(w)
    return w[k:] + w[:k]


def my_replay(gens, rels, moves, rot_convention='left'):
    """Independent replay of tietze certificates following the README spec.  Returns (ok, msg, final)."""
    G, R = canon_pres(gens, rels)
    G = list(G); R = list(R)
    for t, mv in enumerate(moves):
        kind = mv[0]
        if kind == 'elim':
            _, g, j = mv
            if g not in G: return False, 'move %d: gen %r not present' % (t, g), (G, R)
            if not (0 <= j < len(R)): return False, 'move %d: bad relator index' % t, (G, R)
            r = R[j]
            occ = [p for p, a in enumerate(r) if abs(a) == g]
            if len(occ) != 1: return False, 'move %d: g occurs %d times' % (t, len(occ)), (G, R)
            p = occ[0]
            rr = r[p:] + r[:p]
            e = 1 if rr[0] > 0 else -1
            u = rr[1:]
            img = inv(u) if e == 1 else u
            if any(abs(a) == g for a in img): return False, 'move %d: g in image' % t, (G, R)
            R2 = [subst(x, g, img) for q, x in enumerate(R) if q != j]
            G2 = [h for h in G if h != g]
            G, R = canon_pres(G2, R2); G = list(G); R = list(R)
        elif kind == 'mult':
            _, i, j, e, kj, ki = mv
            if i == j: return False, 'move %d: i == j' % t, (G, R)
            if not (0 <= i < len(R) and 0 <= j < len(R)): return False, 'move %d: bad index' % t, (G, R)
            if e not in (1, -1): return False, 'move %d: bad exponent' % t, (G, R)
            rj = R[j] if e == 1 else inv(R[j])
            if rot_convention == 'left':
                new = red(rotl(rj, kj) + rotl(R[i], ki))
            else:
                new = red(rotl(rj, -kj) + rotl(R[i], -ki))
            R2 = list(R); R2[i] = new
            G, R = canon_pres(G, R2); G = list(G); R = list(R)
        elif kind == 'nielsen':
            _, x, a, d, side = mv
            if x == a or x not in G or a not in G: return False, 'move %d: bad nielsen' % t, (G, R)
            if not isinstance(d, int) or d == 0: return False, 'move %d: bad power' % t, (G, R)
            ad = (a,) * d if d > 0 else (-a,) * (-d)
            img = (x,) + ad if side == 'R' else ad + (x,)
            R2 = [subst(r, x, img) for r in R]
            G, R = canon_pres(G, R2); G = list(G); R = list(R)
        else:
            return False, 'move %d: unknown kind %r' % (t, kind), (G, R)
    ok = (len(G) == 1 and len(R) == 0)
    return ok, ('reached <a|>' if ok else 'final %d gens %d rels' % (len(G), len(R))), (G, R)


# ------------------------------------------------------------------ representations
def pmul(p, q): return tuple(p[i] for i in q)       # (p*q)(i) = p(q(i))


def pinv(p):
    r = [0] * len(p)
    for i, j in enumerate(p): r[j] = i
    return tuple(r)


def is_perm(p, d):
    return len(p) == d and sorted(p) == list(range(d))


def eval_word(w, img, d, conv='pq'):
    acc = tuple(range(d))
    for a in w:
        x = img[abs(a)] if a > 0 else pinv(img[abs(a)])
        acc = pmul(acc, x) if conv == 'pq' else pmul(x, acc)
    return acc


def check_rep(gens, rels, images, d, pair):
    """images: dict gen(int) -> perm tuple.  Returns (ok, msg)."""
    for g in gens:
        if g not in images: return False, 'missing image of gen %d' % g
        if not is_perm(tuple(images[g]), d): return False, 'image of %d not a permutation of degree %d' % (g, d)
    img = {g: tuple(images[g]) for g in gens}
    e = tuple(range(d))
    results = {}
    for conv in ('pq', 'qp'):
        bad = [r for r in rels if eval_word(r, img, d, conv) != e]
        results[conv] = len(bad)
    if results['pq'] and results['qp']:
        return False, 'relators fail: %r' % results
    a, b = pair
    if a not in img or b not in img: return False, 'noncommuting pair not generators'
    if pmul(img[a], img[b]) == pmul(img[b], img[a]): return False, 'pair commutes'
    return True, 'ok (relators hold with conv %s)' % ('pq' if not results['pq'] else 'qp')


# ------------------------------------------------------------------ Morse-word constructions
def mirror_full(full):
    return [(('y' if c == 'x' else 'x') if c in 'xy' else c, i) for c, i in full]


def mirror_hw(hw):
    toks = hw.split('.')
    out = []
    for t in toks:
        if t and t[0] == 'x': out.append('y' + t[1:])
        elif t and t[0] == 'y': out.append('x' + t[1:])
        else: out.append(t)
    return '.'.join(out)


def connected_sum_full(f1, f2):
    """K1 # K2: K1's word without its final ('u',0) followed by K2's word (whose implicit initial cap is glued on)."""
    assert f1[-1] == ('u', 0)
    return list(f1[:-1]) + list(f2)


def pretzel_full(ps):
    m = len(ps)
    full = [('l', 2 * i + 1) for i in range(m - 1)]
    for i, p in enumerate(ps):
        full += [('x' if p > 0 else 'y', 2 * i)] * abs(p)
    full += [('u', 1)] * (m - 1) + [('u', 0)]
    return full


def plat4_full(braid):
    """4-plat: caps (0,1),(2,3); braid letters ('x'|'y', i) on positions 0..2; cups (2,3),(0,1)."""
    return [('l', 2)] + list(braid) + [('u', 2), ('u', 0)]


def cable2(full, twists_at_end=0, twist_letter='x', clasp=None):
    """2-cable of a Morse word (blackboard).  Optionally insert 2*|twists| crossings on the LAST pair before the
    final cups, and a clasp (Whitehead double) there.  Returns the new Morse word."""
    out = [('l', 1)]                       # initial cap -> outer (0,3) implicit + inner (1,2)
    body = list(full)
    assert body[-1] == ('u', 0)
    for c, i in body[:-1]:
        if c in 'lr':
            out += [(c, 2 * i), (c, 2 * i + 1)]
        elif c == 'u':
            out += [('u', 2 * i + 1), ('u', 2 * i)]
        else:
            out += [(c, 2 * i + 1), (c, 2 * i), (c, 2 * i + 2), (c, 2 * i + 1)]
    # final: 4 strands 0,1 (cable of strand 0) and 2,3 (cable of strand 1)
    out += [(twist_letter, 2)] * (2 * twists_at_end)
    if clasp is not None:
        out += [('l', 4), (clasp, 3), (clasp, 3), ('u', 2)]
    out += [('u', 1), ('u', 0)]
    return out


def link_components_full(full):
    """number of components of the Morse diagram (crossings treated as pass-through)."""
    par = {}

    def find(a):
        while par.get(a, a) != a: a = par[a]
        return a

    def uni(a, b):
        a, b = find(a), find(b)
        if a != b: par[a] = b
    nid = [0]

    def new():
        nid[0] += 1; return nid[0]
    e0 = new(); pos = [e0, e0]
    for c, i in full:
        if c in 'xy':
            a, b = pos[i], pos[i + 1]
            bl, br = new(), new()
            uni(a, br); uni(b, bl)
            pos[i], pos[i + 1] = bl, br
        elif c in 'lr':
            e = new(); pos[i:i] = [e, e]
        elif c == 'u':
            uni(pos[i], pos[i + 1]); del pos[i:i + 2]
    return len(set(find(e) for e in range(1, nid[0] + 1)))


def linking_2cable(full):
    """For a 2-component Morse diagram: linking number (sum of signs of inter-component crossings / 2), using
    an orientation of each component from a traversal."""
    par = {}

    def find(a):
        while par.get(a, a) != a: a = par[a]
        return a

    def uni(a, b):
        a, b = find(a), find(b)
        if a != b: par[a] = b
    nid = [0]

    def new():
        nid[0] += 1; return nid[0]
    e0 = new(); pos = [e0, e0]
    cr = []
    for c, i in full:
        if c in 'xy':
            a, b = pos[i], pos[i + 1]
            bl, br = new(), new()
            cr.append((c, a, b, bl, br))
            pos[i], pos[i + 1] = bl, br
        elif c in 'lr':
            e = new(); pos[i:i] = [e, e]
        elif c == 'u':
            uni(pos[i], pos[i + 1]); del pos[i:i + 2]
    # endpoints of segments
    ends = {}
    for k, (c, a, b, bl, br) in enumerate(cr):
        for s, e in (('TL', a), ('TR', b), ('BL', bl), ('BR', br)):
            ends.setdefault(find(e), []).append((k, s))
    # traverse each component
    visited = {}
    comp = 0
    direction = {}   # (k, which strand 'A' = TL-BR or 'B' = TR-BL) -> (slot_in)
    for k0 in range(len(cr)):
        for s0 in ('TL', 'TR'):
            if (k0, s0) in visited or (k0, OPPS[s0]) in visited: continue
            k, s = k0, s0
            while (k, s) not in visited:
                visited[(k, s)] = comp; o = OPPS[s]; visited[(k, o)] = comp
                strand = 'A' if s in ('TL', 'BR') else 'B'
                direction[(k, strand)] = (s, o)
                c, a, b, bl, br = cr[k]
                e = find({'TL': a, 'TR': b, 'BL': bl, 'BR': br}[o])
                p, q = ends[e]
                nxt = q if p == (k, o) else p
                k, s = nxt
            comp += 1
    tot = 0
    for k, (c, a, b, bl, br) in enumerate(cr):
        ca = visited[(k, 'TL')]; cb = visited[(k, 'TR')]
        if ca == cb: continue
        sA = direction[(k, 'A')]; sB = direction[(k, 'B')]
        over = 'A' if c == 'x' else 'B'
        so = sA if over == 'A' else sB; su = sB if over == 'A' else sA
        o = (SLOTPOS[so[1]][0] - SLOTPOS[so[0]][0], SLOTPOS[so[1]][1] - SLOTPOS[so[0]][1])
        u = (SLOTPOS[su[1]][0] - SLOTPOS[su[0]][0], SLOTPOS[su[1]][1] - SLOTPOS[su[0]][1])
        tot += 1 if o[0] * u[1] - o[1] * u[0] > 0 else -1
    return tot // 2, comp


def whitehead_double_full(companion_full, clasp='x'):
    """Untwisted Whitehead double: 2-cable, then full twists on the last pair to make the cable's linking number 0,
    then a clasp of the given letter."""
    base = cable2(companion_full)
    lk, nc = linking_2cable(base)
    assert nc == 2, nc
    best = None
    for letter in ('x', 'y'):
        f = cable2(companion_full, twists_at_end=abs(lk), twist_letter=letter)
        lk2, nc2 = linking_2cable(f)
        if lk2 == 0: best = letter
    assert best is not None or lk == 0, (lk,)
    letter = best or 'x'
    return cable2(companion_full, twists_at_end=abs(lk), twist_letter=letter, clasp=clasp)


def random_braid_word(rng, npos, length, lo=0):
    return [(rng.choice('xy'), rng.randrange(lo, npos)) for _ in range(length)]


def inverse_braid(word):
    return [(('y' if c == 'x' else 'x'), i) for c, i in reversed(word)]


# ------------------------------------------------------------------ signed Gauss code (Regina fromData) -> PD
def gauss_to_pd(signs, comp):
    """signs[c-1] = sign of crossing c; comp = traversal, +c over, -c under.  Edge j goes from passage j to j+1.
    Positive crossing: ccw (under-in, over-out, under-out, over-in); negative: (under-in, over-in, under-out, over-out).
    Returns (X, sg) with X in crossing order 1..n (0-based labels, consecutive along the orientation)."""
    n = len(signs); m = len(comp)
    assert m == 2 * n
    pos_over = {}; pos_under = {}
    for j, c in enumerate(comp):
        if c > 0: pos_over[c] = j
        else: pos_under[-c] = j
    X = []
    for c in range(1, n + 1):
        ju, jo = pos_under[c], pos_over[c]
        ui, uo, oi, oo = (ju - 1) % m, ju, (jo - 1) % m, jo
        if signs[c - 1] > 0: X.append((ui, oo, uo, oi))
        else: X.append((ui, oi, uo, oo))
    return X, pd_signs(X)


def pd_heads(X, sg):
    """for each label e: (crossing, slot index) where edge e is INCOMING."""
    h = {}
    for k, (a, b, c, d) in enumerate(X):
        h[a] = (k, 0)
        if sg[k] > 0: h[d] = (k, 3)
        else: h[b] = (k, 1)
    return h


def pd_connected_sum(X1, s1, X2, s2, e1=0, e2=0):
    """K1 # K2 by cutting edge e1 of K1 and e2 of K2 and reconnecting tail(e1)->head(e2), tail(e2)->head(e1)."""
    m1 = 2 * len(X1)
    X2s = [tuple(e + m1 for e in x) for x in X2]
    E2 = e2 + m1
    h1 = pd_heads(X1, s1); h2 = pd_heads(X2s, s2)
    Y1 = [list(x) for x in X1]; Y2 = [list(x) for x in X2s]
    k, j = h1[e1]; Y1[k][j] = E2
    k, j = h2[E2]; Y2[k][j] = e1
    Y = [tuple(x) for x in Y1 + Y2]
    return relabel_pd(Y)


def planar_signs(comp, rng=None, max_restarts=200):
    """Recover crossing signs of an UNSIGNED Gauss code (+over/-under) by planarity: find signs with
    faces = n + 2.  Brute force for n <= 16 (crossing 1 fixed), else greedy local search on the face count."""
    import itertools, random as _r
    n = max(abs(x) for x in comp)
    def faces_of(signs):
        X, sg = gauss_to_pd(signs, comp)
        return faces_count(X)
    if n <= 16:
        for bits in itertools.product((1, -1), repeat=n - 1):
            s = [1] + list(bits)
            if faces_of(s) == n + 2: return s
        return None
    rng = rng or _r.Random(0)
    for _ in range(max_restarts):
        s = [rng.choice((1, -1)) for _ in range(n)]
        f = faces_of(s)
        improved = True
        while improved and f < n + 2:
            improved = False
            order = list(range(n)); rng.shuffle(order)
            for i in order:
                s[i] = -s[i]
                f2 = faces_of(s)
                if f2 > f: f = f2; improved = True
                elif f2 == f and rng.random() < 0.3: pass
                else: s[i] = -s[i]
        if f == n + 2: return s
    return None
