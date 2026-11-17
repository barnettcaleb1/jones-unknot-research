"""replay_fixed_proposal.py (AUDIT-2 copy of replay.py with the F2 fix; NOT the project file) -- INDEPENDENT checker for certify.py certificates.

Independence: this file imports NOTHING from the certifier (diagram.py, wirtinger.py, tietze.py, reps.py, certify.py).
It rebuilds the knot from the halfword with the project's own code (tools/alex.py: alex.symmetrize = definition of K,
alex.diagram = crossings of the Morse diagram with traversal directions; tools/kauffman.py for the bracket), writes its own
Wirtinger presentation, its own canonical form (Duval least rotation instead of Booth), and re-applies every move after
checking the move's precondition.  A certificate is accepted only if the final state is reached by valid moves.

Certificate kinds (dicts):
  {'kind': 'tietze', 'halfword': w, 'moves': [...]}           -> CERTIFIED_UNKNOT iff the replay ends at <g | >.
  {'kind': 'jones24', 'halfword': w}                          -> CERTIFIED_UNKNOT iff the Morse diagram of K has <= 24
        crossings and V_K = 1 (project bracket kauffman.bracket, ident3 normalisation); Tuzun-Sikora (JUC verified <= 24).
  {'kind': 'unknot0', 'halfword': w}                          -> the Morse diagram itself has no crossings and is a knot.
  {'kind': 'rep', 'halfword': w, 'degree': d, 'images': {gen: perm}, 'noncommuting': [g, h], 'group': str}
        -> CERTIFIED_NONTRIVIAL iff every Wirtinger relator maps to the identity permutation and the images of g, h do not
        commute.  Permutations are tuples p of length d (p[i] = image of i), product (p*q)[i] = p[q[i]].
Usage: replay.py CERT.json [...]   (or import check(cert) -> (ok, message)).
"""
import sys, json
TOOLS = '/Users/calebbarnett/jones-lanes/theory-restart/tools'
if TOOLS not in sys.path: sys.path.insert(0, TOOLS)
import alex, kauffman


# ---------------------------------------------------------------- Wirtinger from alex.diagram
class _UF:
    def __init__(self): self.p = {}
    def f(self, a):
        self.p.setdefault(a, a)
        while self.p[a] != a:
            self.p[a] = self.p[self.p[a]]; a = self.p[a]
        return a
    def u(self, a, b): self.p[self.f(a)] = self.f(b)


def knot_crossings(halfword):
    full = alex.symmetrize(alex.parse(halfword))
    if full is None: return None
    return alex.diagram(full)        # None if invalid or not a knot; [] if no crossings (single circle)


def wirtinger_presentation(halfword):
    """Returns (gens, rels) or None.  Generator k+1 = arc beginning at crossing k (outgoing under edge).
    Crossing sign in the picture where the Morse word is drawn upwards (slots before = lower):
      'x': over TL->BR has direction (+1,+1), under TR->BL (-1,+1);  'y': over TR->BL (-1,+1), under TL->BR (+1,+1);
      a strand traversed against the word (alex flag od/ud False) has the negated vector; sign = sign(over x under).
    Relator: x_out^-1 x_o^s x_in x_o^-s."""
    cr = knot_crossings(halfword)
    if cr is None: return None
    n = len(cr)
    if n == 0: return [1], []
    uf = _UF()
    for x in cr:
        for key in ('ot', 'ob', 'ut', 'ub'): uf.f(x[key])
        uf.u(x['ot'], x['ob'])
    begin = {}
    for k, x in enumerate(cr):
        out_e = x['ub'] if x['ud'] else x['ut']
        r = uf.f(out_e)
        if r in begin: return None
        begin[r] = k + 1
    rels = []
    for k, x in enumerate(cr):
        if x['ty'] == 'x': ov, un = (1, 1), (-1, 1)
        else: ov, un = (-1, 1), (1, 1)
        if not x['od']: ov = (-ov[0], -ov[1])
        if not x['ud']: un = (-un[0], -un[1])
        cross = ov[0] * un[1] - ov[1] * un[0]
        s = 1 if cross > 0 else -1
        in_e = x['ut'] if x['ud'] else x['ub']
        o = begin.get(uf.f(x['ot'])); i = begin.get(uf.f(in_e))
        if o is None or i is None: return None
        rels.append((-(k + 1), s * o, i, -s * o))
    return list(range(1, n + 1)), rels


# ---------------------------------------------------------------- free group words, canonical form (own code)
def freered(w):
    st = []
    for a in w:
        if st and st[-1] + a == 0: st.pop()
        else: st.append(a)
    return tuple(st)


def inverse(w): return tuple(-a for a in w[::-1])


def cycred(w):
    w = list(freered(w))
    while len(w) >= 2 and w[0] + w[-1] == 0:
        w = w[1:-1]
    return tuple(w)


def least_rotation_start(s):
    """Duval/Lyndon-factorisation based minimal rotation (different algorithm from tietze.booth)."""
    n = len(s)
    if n == 0: return 0
    ss = s + s; i = 0; ans = 0
    while i < n:
        ans = i; j = i + 1; k = i
        while j < 2 * n and ss[k] <= ss[j]:
            if ss[k] < ss[j]: k = i
            else: k += 1
            j += 1
        while i <= k: i += j - k
    return ans


def canonical_cyclic(w):
    w = cycred(w)
    if not w: return ()
    k = least_rotation_start(w); a = w[k:] + w[:k]
    wi = inverse(w); k2 = least_rotation_start(wi); b = wi[k2:] + wi[:k2]
    return a if a <= b else b


def normal_form(gens, rels):
    cs = []
    seen = set()
    for r in rels:
        c = canonical_cyclic(r)
        if c and c not in seen:
            seen.add(c); cs.append(c)
    cs.sort(key=lambda w: (len(w), w))
    return sorted(gens), cs


def subst(w, g, img):
    out = []
    ii = inverse(img)
    for a in w:
        if a == g: out.extend(img)
        elif a == -g: out.extend(ii)
        else: out.append(a)
    return freered(out)


def rotate(w, k):
    if not w: return w
    k = k % len(w)
    return w[k:] + w[:k]


def replay_moves(gens, rels, moves):
    G, R = normal_form(gens, rels)
    for idx, mv in enumerate(moves):
        kind = mv[0]
        if kind == 'elim':
            g, j = mv[1], mv[2]
            if g not in G or not (0 <= j < len(R)): return None, 'move %d: bad indices' % idx
            r = R[j]
            pos = [p for p, a in enumerate(r) if a == g or a == -g]
            if len(pos) != 1: return None, 'move %d: generator %d does not occur exactly once' % (idx, g)
            w = rotate(r, pos[0])
            rest = w[1:]
            img = inverse(rest) if w[0] == g else rest       # g^e rest = 1
            if any(abs(a) == g for a in img): return None, 'move %d: internal' % idx
            R2 = [subst(x, g, img) for q, x in enumerate(R) if q != j]
            G, R = normal_form([x for x in G if x != g], R2)
        elif kind == 'nielsen':
            x, a, d, side = mv[1], mv[2], mv[3], mv[4]
            if x == a or x not in G or a not in G or d not in (1, -1) or side not in ('R', 'L'):
                return None, 'move %d: bad nielsen' % idx
            img = (x, d * a) if side == 'R' else (d * a, x)
            G, R = normal_form(G, [subst(r, x, img) for r in R])
        elif kind == 'mult':
            i, j, e, kj, ki = mv[1], mv[2], mv[3], mv[4], mv[5]
            if i == j or not (0 <= i < len(R)) or not (0 <= j < len(R)) or e not in (1, -1):
                return None, 'move %d: bad mult' % idx
            rj = R[j] if e == 1 else inverse(R[j])
            new = freered(rotate(rj, kj) + rotate(R[i], ki))
            R2 = list(R); R2[i] = new
            G, R = normal_form(G, R2)
        else:
            return None, 'move %d: unknown kind %r' % (idx, kind)
    return (G, R), 'ok'


# ---------------------------------------------------------------- Jones polynomial (project bracket)
def VK_project(halfword):
    """V_K from tools/kauffman.bracket with the ident3 normalisation (V(1) = 1, V'(1) = 0)."""
    kb = kauffman.bracket(halfword)
    if not kb: return None
    kb = {e: c for e, c in kb.items() if c}
    es = sorted(kb); r = es[0] % 4
    if any((e - r) % 4 for e in es): return None
    V = {-(e - r) // 4: c for e, c in kb.items()}
    s = sum(V.values())
    if s not in (1, -1): return None
    V = {e: c * s for e, c in V.items()}
    d = sum(e * c for e, c in V.items())
    return {e - d: c for e, c in V.items()}


# ---------------------------------------------------------------- permutations
def pmul(p, q): return tuple(p[i] for i in q)


def pinv(p):
    r = [0] * len(p)
    for i, x in enumerate(p): r[x] = i
    return tuple(r)


def check(cert):
    """(accepted, message).  Any exception while checking is a rejection."""
    try:
        return _check(cert)
    except Exception as e:
        return False, 'checker exception (rejected): %r' % (e,)


def _check(cert):
    kind = cert.get('kind'); w = cert.get('halfword')
    if kind == 'tietze':
        P = wirtinger_presentation(w)
        if P is None: return False, 'not a knot diagram'
        res, msg = replay_moves(P[0], P[1], [tuple(m) for m in cert['moves']])
        if res is None: return False, msg
        G, R = res
        if len(G) == 1 and not R: return True, 'UNKNOT: Tietze replay reaches <%d | > (%d moves, %d crossings)' % (G[0], len(cert['moves']), len(P[0]))
        return False, 'replay ends at %d generators, %d relators' % (len(G), len(R))
    if kind == 'jones24':
        cr = knot_crossings(w)
        if cr is None: return False, 'not a knot diagram'
        if len(cr) > 24: return False, '%d crossings > 24' % len(cr)
        V = VK_project(w)
        if V == {0: 1}: return True, 'UNKNOT: diagram with %d <= 24 crossings and V_K = 1 (Tuzun-Sikora)' % len(cr)
        return False, 'V_K != 1'
    if kind == 'unknot0':
        cr = knot_crossings(w)
        if cr == []: return True, 'UNKNOT: crossing-free one-component diagram'
        return False, 'diagram has crossings or is not a knot'
    if kind == 'rep':
        P = wirtinger_presentation(w)
        if P is None: return False, 'not a knot diagram'
        gens, rels = P
        d = int(cert['degree'])
        img = {int(k): tuple(v) for k, v in cert['images'].items()}
        ident = tuple(range(d))
        for g in gens:
            p = img.get(g)
            if p is None or len(p) != d or sorted(p) != list(range(d)): return False, 'image of %d missing or not a permutation' % g
        for r in rels:
            acc = ident
            for a in r:
                acc = pmul(acc, img[a] if a > 0 else pinv(img[-a]))
            if acc != ident: return False, 'relator %r not satisfied' % (r,)
        if set(img) != set(gens): return False, 'images must be given for exactly the Wirtinger generators'
        g, h = cert['noncommuting']
        if g not in gens or h not in gens or g == h:
            return False, 'noncommuting pair must be two distinct Wirtinger generators'
        if pmul(img[g], img[h]) == pmul(img[h], img[g]): return False, 'claimed noncommuting pair commutes'
        return True, 'NONTRIVIAL: hom to %s (degree %d), all %d relators checked, images of %d,%d do not commute' % (cert.get('group', '?'), d, len(rels), g, h)
    return False, 'unknown certificate kind'


if __name__ == '__main__':
    for f in sys.argv[1:]:
        c = json.load(open(f))
        certs = c if isinstance(c, list) else [c]
        for cc in certs:
            print(check(cc))
