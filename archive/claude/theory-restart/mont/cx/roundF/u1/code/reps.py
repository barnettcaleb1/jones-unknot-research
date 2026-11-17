"""reps.py -- search for homomorphisms pi_1(S^3 - K) -> G with NONABELIAN image (certificates of nontriviality).

All target groups are PERMUTATION groups (so the certificate and its checker only need permutations):
  * Aff(F_p) acting on F_p (x -> lam x + mu): metabelian reps from roots lam != 1 of the Alexander polynomial mod p
    (found by linear algebra: meridians -> (lam, mu_arc), Wirtinger relation <=> mu_out = (1-lam^s) mu_o + lam^s mu_in);
  * S_n, A_n (n <= 7) on {0..n-1};  PSL(2,p) on P^1(F_p) (p+1 points);  SL(2,p) on F_p^2 - 0 (p^2 - 1 points, faithful).
Meridians go to conjugates of a fixed element g (all Wirtinger generators are conjugate meridians).  Search: the Wirtinger
presentation is reduced by eliminations and relator multiplications ONLY (no Nielsen moves), so the surviving generators
are still meridians (a subset of the arcs); their images run over the class C of g (first fixed to g, second up to the
centraliser of g), all reduced relators are checked, the eliminated arcs are recovered from the elimination words, and
the final certificate (images of ALL Wirtinger generators) is re-checked on every Wirtinger relator by replay.check.
"""
import sys, time, random, itertools
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u1/code')
import tietze

# ------------------------------------------------------------------ permutations
def pmul(p, q): return tuple(p[i] for i in q)          # (p*q)(i) = p(q(i))
def pinv(p):
    r = [0] * len(p)
    for i, x in enumerate(p): r[x] = i
    return tuple(r)
def pid(d): return tuple(range(d))

def group_closure(gens, limit=200000):
    d = len(gens[0]); e = pid(d)
    els = {e: 0}; lst = [e]; i = 0
    while i < len(lst):
        x = lst[i]; i += 1
        for g in gens:
            y = pmul(g, x)
            if y not in els:
                els[y] = len(lst); lst.append(y)
                if len(lst) > limit: raise ValueError('group too big')
    return lst

def conj_class(g, gens):
    cl = {g}; frontier = [g]
    gi = [pinv(h) for h in gens]
    while frontier:
        nxt = []
        for x in frontier:
            for h, hi in zip(gens, gi):
                y = pmul(pmul(h, x), hi)
                if y not in cl: cl.add(y); nxt.append(y)
        frontier = nxt
    return sorted(cl)

# ------------------------------------------------------------------ groups
def cyc(n, *cycles):
    p = list(range(n))
    for c in cycles:
        for a, b in zip(c, c[1:] + c[:1]): p[a] = b
    return tuple(p)

def sym_group(n):
    return [cyc(n, (0, 1)), cyc(n, tuple(range(n)))]

def alt_group(n):
    if n % 2: return [cyc(n, (0, 1, 2)), cyc(n, tuple(range(n)))]
    return [cyc(n, (0, 1, 2)), cyc(n, tuple(range(1, n)))]

def psl2_group(p):
    """PSL(2,p) on P^1(F_p): points 0..p-1, p = infinity.  generators z -> z+1, z -> -1/z."""
    INF = p
    t = tuple(((z + 1) % p if z != INF else INF) for z in range(p + 1))
    def s(z):
        if z == INF: return 0
        if z == 0: return INF
        return (-pow(z, p - 2, p)) % p
    return [t, tuple(s(z) for z in range(p + 1))]

def sl2_group(p):
    """SL(2,p) acting on F_p^2 - {0} (faithful): vector (x,y) -> index x*p + y - 1."""
    vecs = [(x, y) for x in range(p) for y in range(p) if (x, y) != (0, 0)]
    idx = {v: i for i, v in enumerate(vecs)}
    def act(M):
        (a, b), (c, d) = M
        return tuple(idx[((a * x + b * y) % p, (c * x + d * y) % p)] for (x, y) in vecs)
    return [act(((1, 1), (0, 1))), act(((0, p - 1), (1, 0)))]

def order(g):
    e = pid(len(g)); x = g; k = 1
    while x != e: x = pmul(x, g); k += 1
    return k

def class_reps(gens, maxclass=800):
    """representatives of non-identity conjugacy classes (with class size <= maxclass), sorted by class size"""
    els = group_closure(gens)
    seen = set(); reps = []
    e = pid(len(gens[0]))
    for x in els:
        if x == e or x in seen: continue
        C = conj_class(x, gens)
        seen.update(C)
        if len(C) == 1: continue          # central: image would be abelian
        if len(C) <= maxclass: reps.append((len(C), order(x), x, C))
    reps.sort(key=lambda r: (r[0], r[1]))
    return els, reps

GROUPS = None
def target_groups():
    """list of (name, gens) in the order they are tried"""
    global GROUPS
    if GROUPS is None:
        G = []
        G.append(('S4', sym_group(4)))
        G.append(('A5', alt_group(5)))
        G.append(('S5', sym_group(5)))
        G.append(('PSL(2,7)', psl2_group(7)))
        G.append(('A6', alt_group(6)))
        G.append(('S6', sym_group(6)))
        G.append(('PSL(2,8)', None))       # placeholder (needs F_8); skipped
        G.append(('PSL(2,11)', psl2_group(11)))
        G.append(('SL(2,5)', sl2_group(5)))
        G.append(('SL(2,7)', sl2_group(7)))
        G.append(('A7', alt_group(7)))
        G.append(('S7', sym_group(7)))
        G.append(('PSL(2,13)', psl2_group(13)))
        GROUPS = [(n, g) for n, g in G if g is not None]
    return GROUPS

# ------------------------------------------------------------------ meridian-preserving reduction
def reduce_for_reps(gens, rels, time_budget=2.0):
    """eliminations (min growth) + shortening relator multiplications; returns (G, R, elims) with
    elims = [(g, word)] in elimination order (word in the generators present at that time)."""
    G, R = tietze.canon(gens, rels)
    elims = []
    t_end = time.time() + time_budget
    while time.time() < t_end:
        cands = tietze.elim_candidates(G, R)
        if cands:
            growth, g, j = min(cands)
            if tietze.total_len(R) + growth > 20000: break
            r = R[j]
            p = next(i for i, a in enumerate(r) if abs(a) == g)
            w = tietze.rot(r, p); u = w[1:]
            sub = tietze.inv(u) if w[0] > 0 else u
            elims.append((g, sub))
            G, R = tietze.apply_move(G, R, ('elim', g, j))
            continue
        sm = tietze.best_substring_mult(R, strict=True)
        if sm is not None:
            G, R = tietze.apply_move(G, R, sm[1]); continue
        break
    return G, R, elims

def extend_images(img, elims):
    """img: dict for surviving generators; returns images of all generators (eliminated ones from their words)."""
    img = dict(img)
    for g, word in reversed(elims):
        acc = None
        for a in word:
            x = img[abs(a)] if a > 0 else pinv(img[abs(a)])
            acc = x if acc is None else pmul(acc, x)
        if acc is None: acc = pid(len(next(iter(img.values()))))
        img[g] = acc
    return img

# ------------------------------------------------------------------ search in a permutation group
def search_group(G, R, gens_group, deadline, rng=None, max_nodes=None):
    """G: surviving generators (meridians), R: relators.  Try classes of the group (smallest first).
    Returns (images dict, class description) or None."""
    els, reps = class_reps(gens_group)
    index = {x: i for i, x in enumerate(els)}
    N = len(els)
    # multiplication table on indices (lazy rows)
    mt = {}
    def mul(i, j):
        row = mt.get(i)
        if row is None:
            xi = els[i]
            row = [index[pmul(xi, y)] for y in els]
            mt[i] = row
        return row[j]
    inv_idx = [index[pinv(x)] for x in els]
    e = index[pid(len(els[0]))]
    Rs = sorted(R, key=len)
    k = len(G)
    gpos = {g: t for t, g in enumerate(G)}
    Rw = [[(gpos[abs(a)], a > 0) for a in r] for r in Rs]
    for csize, cord, g0, C in reps:
        if time.time() > deadline: return None
        Ci = [index[c] for c in C]
        c0 = index[g0]
        # centraliser of g0 inside G (elements commuting with g0) for symmetry reduction of the 2nd generator
        cent = [x for x in range(N) if mul(x, c0) == mul(c0, x)]
        # orbit reps of C under conjugation by the centraliser
        seen = set(); reps2 = []
        for c in Ci:
            if c in seen: continue
            reps2.append(c)
            for z in cent:
                seen.add(mul(mul(z, c), inv_idx[z]))
        choices = [[c0], reps2] + [Ci] * (k - 2)
        if k == 1: choices = [[c0]]
        total = 1
        for ch in choices: total *= len(ch)
        if total > 3_000_000: continue
        assign = [0] * k
        cnt = 0
        for combo in itertools.product(*choices):
            cnt += 1
            if cnt % 2048 == 0 and time.time() > deadline: return None
            ok = True
            for rw in Rw:
                acc = e
                for (t, pos) in rw:
                    x = combo[t]
                    acc = mul(acc, x if pos else inv_idx[x])
                if acc != e: ok = False; break
            if not ok: continue
            # nonabelian image?
            na = None
            for a in range(k):
                for b in range(a + 1, k):
                    if mul(combo[a], combo[b]) != mul(combo[b], combo[a]): na = (a, b); break
                if na: break
            if na is None: continue
            img = {G[t]: els[combo[t]] for t in range(k)}
            return img, 'class of order-%d element, size %d' % (cord, csize)
    return None

# ------------------------------------------------------------------ affine reps
def primes(lo, hi):
    out = []
    for p in range(max(2, lo), hi + 1):
        if all(p % q for q in range(2, int(p ** 0.5) + 1)): out.append(p)
    return out

def nullspace_mod(rows, n, p):
    """basis of the nullspace of the matrix (list of dict col->val) over F_p"""
    M = [[r.get(c, 0) % p for c in range(n)] for r in rows]
    piv_cols = []; rk = 0
    for c in range(n):
        pr = next((i for i in range(rk, len(M)) if M[i][c]), None)
        if pr is None: continue
        M[rk], M[pr] = M[pr], M[rk]
        iv = pow(M[rk][c], p - 2, p)
        M[rk] = [(x * iv) % p for x in M[rk]]
        for i in range(len(M)):
            if i != rk and M[i][c]:
                f = M[i][c]
                M[i] = [(x - f * y) % p for x, y in zip(M[i], M[rk])]
        piv_cols.append(c); rk += 1
    free = [c for c in range(n) if c not in piv_cols]
    basis = []
    for fc in free:
        v = [0] * n; v[fc] = 1
        for i, c in enumerate(piv_cols): v[c] = (-M[i][fc]) % p
        basis.append(v)
    return basis

def affine_rep(gens, rels, alex_poly, pmax=400):
    """alex_poly: tuple of (exp, coeff).  Returns (images as permutations of F_p, description) or None."""
    if alex_poly is None or len(alex_poly) <= 1: return None
    n = len(gens); col = {g: j for j, g in enumerate(gens)}
    # parse Wirtinger relators (-out, +-o, in, -+o)
    cons = []
    for r in rels:
        if len(r) != 4: return None
        out = -r[0]; s = 1 if r[1] > 0 else -1; o = abs(r[1]); i = r[2]
        cons.append((out, o, i, s))
    for p in primes(3, pmax):
        roots = [l for l in range(2, p) if sum(c * pow(l, e, p) for e, c in alex_poly) % p == 0]
        for lam in roots:
            rows = []
            li = pow(lam, p - 2, p)
            for out, o, i, s in cons:
                ls = lam if s > 0 else li
                row = {}
                row[col[out]] = (row.get(col[out], 0) + 1) % p
                row[col[o]] = (row.get(col[o], 0) - (1 - ls)) % p
                row[col[i]] = (row.get(col[i], 0) - ls) % p
                rows.append(row)
            B = nullspace_mod(rows, n, p)
            for v in B:
                if len(set(v)) > 1:
                    img = {g: tuple((lam * x + v[col[g]]) % p for x in range(p)) for g in gens}
                    return img, 'Aff(F_%d), lam=%d (root of Delta mod %d)' % (p, lam, p)
    return None


# ------------------------------------------------------------------ affine reps WITHOUT the Alexander polynomial
# [cert/run fix F3 (audit-2, performance)]: on long diagrams the exact Alexander polynomial dominates the run time.  Here the
# Wirtinger presentation is first reduced by meridian-preserving moves (eliminations + relator multiplications), so every
# surviving generator g is still a meridian (abelianises to t).  An affine rep g -> (x -> lam x + mu_g) on F_p satisfies a
# relator r iff sum_g (dr/dg)(lam) mu_g = 0 (Fox calculus; the multiplier lam^(exponent sum of r) is 1 because r has exponent
# sum 0).  So for every prime p and lam in 2..p-1 we take the nullspace of the Fox matrix at t = lam over F_p; a solution mu
# that is not constant gives a NONABELIAN rep (two maps x -> lam x + a, x -> lam x + b commute iff a = b, lam != 1).  The
# eliminated generators get the images of their elimination words; the full certificate is re-checked by replay.check.
def fox_terms(G, R):
    """per relator: list of (column, sign, prefix exponent) with all generators -> t"""
    col = {g: j for j, g in enumerate(G)}
    out = []
    for r in R:
        e = 0; terms = []
        for a in r:
            if a > 0:
                terms.append((col[a], 1, e)); e += 1
            else:
                e -= 1; terms.append((col[-a], -1, e))
        out.append(terms)
    return out

def affine_rep_reduced(G, R, elims, pmax=400, deadline=None):
    if len(G) < 2: return None
    T = fox_terms(G, R)
    emin = min((e for t in T for (_, _, e) in t), default=0); emax = max((e for t in T for (_, _, e) in t), default=0)
    n = len(G)
    for p in primes(3, pmax):
        for lam in range(2, p):
            if deadline is not None and time.time() > deadline: return None
            li = pow(lam, p - 2, p)
            pw = {}
            x = pow(li, -emin, p) if emin < 0 else pow(lam, emin, p)
            for e in range(emin, emax + 1):
                pw[e] = x; x = x * lam % p
            rows = []
            for t in T:
                row = {}
                for (c, s, e) in t:
                    row[c] = (row.get(c, 0) + s * pw[e]) % p
                rows.append(row)
            B = nullspace_mod(rows, n, p)
            if len(B) < 2: continue
            for v in B:
                # the constant vector is always a solution; any basis vector that is not constant gives a nonabelian rep
                if len(set(v)) > 1:
                    img = {g: tuple((lam * xx + v[j]) % p for xx in range(p)) for j, g in enumerate(G)}
                    full = extend_images(img, elims)
                    return full, 'Aff(F_%d), lam=%d (reduced presentation %d gens, Fox matrix mod p)' % (p, lam, n)
            # if every basis vector happens to be constant up to combination, try sums
            if len(B) >= 2:
                v = [(a + 2 * b) % p for a, b in zip(B[0], B[1])]
                if len(set(v)) > 1:
                    img = {g: tuple((lam * xx + v[j]) % p for xx in range(p)) for j, g in enumerate(G)}
                    full = extend_images(img, elims)
                    return full, 'Aff(F_%d), lam=%d (reduced presentation %d gens, Fox matrix mod p)' % (p, lam, n)
    return None

# ------------------------------------------------------------------ driver
def find_rep(gens, rels, alex_poly=None, time_budget=20.0, groups=None, affine_reduced=False, pmax_reduced=200):
    """returns (images for ALL generators, group name, note) or None.
    affine_reduced=True: affine search on the reduced presentation (no Alexander polynomial needed; cert/run fix F3)."""
    t0 = time.time(); deadline = t0 + time_budget
    if alex_poly is not None and len(alex_poly) > 1:
        r = affine_rep(gens, rels, alex_poly)
        if r is not None:
            img, note = r
            p = len(next(iter(img.values())))
            return img, 'Aff(F_%d)' % p, note
    G, R, elims = reduce_for_reps(gens, rels, time_budget=min(5.0, 0.25 * time_budget))
    if len(G) <= 1: return None
    if affine_reduced:
        r = affine_rep_reduced(G, R, elims, pmax=pmax_reduced, deadline=t0 + 0.5 * time_budget)
        if r is not None:
            img, note = r
            p = len(next(iter(img.values())))
            return img, 'Aff(F_%d)' % p, note
    for name, gg in (groups or target_groups()):
        if time.time() > deadline: break
        res = search_group(G, R, gg, deadline)
        if res is not None:
            img, note = res
            full = extend_images(img, elims)
            return full, name, note + '; reduced presentation %d gens %d rels' % (len(G), len(R))
    return None

def noncommuting_pair(img, gens):
    for a in gens:
        for b in gens:
            if a < b and pmul(img[a], img[b]) != pmul(img[b], img[a]): return a, b
    return None
