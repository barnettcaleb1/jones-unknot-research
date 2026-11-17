"""tietze.py -- Tietze simplification of a finite presentation, recording a REPLAYABLE list of moves.

Presentation = (gens, rels): gens a list of positive ints, rels a list of tuples of nonzero ints (+g / -g).
CANONICAL FORM (applied after every move, by this module AND independently by replay.py):
  each relator is freely and cyclically reduced, then replaced by the lexicographically least tuple among all
  rotations of it and of its inverse; empty relators are dropped; duplicates dropped; relators sorted by (len, tuple);
  gens sorted.  (Each of these is a Tietze move: conjugation, inversion, deletion of a trivial or repeated relator.)
MOVES (indices refer to the canonical relator list at the time of the move):
  ('elim', g, j)              g occurs exactly once (as g or g^-1) in relator j; write relator j cyclically as g^e u
                              (u free of g); g := u^-1 (e=1) or u (e=-1) is substituted everywhere; relator j and g removed.
  ('nielsen', x, a, d, side)  automorphism x -> x a^d (side 'R') or x -> a^d x (side 'L'), x != a, d = +-1, applied to all
                              relators (an elementary Nielsen automorphism of the free group: the group is unchanged).
  ('mult', i, j, e, kj, ki)   i != j: relator i := reduce( rot(r_j^e, kj) . rot(r_i, ki) )  (a conjugate of r_j^+-1 times a
                              conjugate of r_i; the normal closure is unchanged because r_j stays).
SUCCESS = one generator and no relators: the group is infinite cyclic.
"""
import random, time

# ------------------------------------------------------------------ words
def red(w):
    out = []
    for a in w:
        if out and out[-1] == -a: out.pop()
        else: out.append(a)
    return tuple(out)

def inv(w): return tuple(-a for a in reversed(w))

def cyc_red(w):
    w = red(w)
    i, j = 0, len(w) - 1
    while i < j and w[i] == -w[j]:
        i += 1; j -= 1
    return w[i:j + 1]

def rot(w, k):
    if not w: return w
    k %= len(w)
    return w[k:] + w[:k]

def booth(s):
    """index of the lexicographically least rotation (Booth's algorithm)"""
    n = len(s)
    if n == 0: return 0
    S2 = s + s
    f = [-1] * (2 * n)
    k = 0
    for j in range(1, 2 * n):
        sj = S2[j]
        i = f[j - k - 1]
        while i != -1 and sj != S2[k + i + 1]:
            if sj < S2[k + i + 1]: k = j - i - 1
            i = f[i]
        if sj != S2[k + i + 1]:
            if sj < S2[k]: k = j
            f[j - k] = -1
        else:
            f[j - k] = i + 1
    return k

_CANON = {}
def canon_word(w):
    c = _CANON.get(w)
    if c is not None: return c
    w0 = w
    w = cyc_red(w)
    if not w: c = w
    else:
        a = rot(w, booth(w)); wi = inv(w); b = rot(wi, booth(wi))
        c = min(a, b)
    if len(_CANON) > 500000: _CANON.clear()
    _CANON[w0] = c; _CANON[c] = c
    return c

def canon(gens, rels):
    s = set()
    for r in rels:
        c = canon_word(r)
        if c: s.add(c)
    return sorted(gens), sorted(s, key=lambda w: (len(w), w))

def total_len(rels): return sum(len(r) for r in rels)

def occurrences(w, g):
    return sum(1 for a in w if a == g or a == -g)

def substitute(w, g, sub):
    """replace g by sub and g^-1 by sub^-1 in w"""
    si = inv(sub); out = []
    for a in w:
        if a == g: out.extend(sub)
        elif a == -g: out.extend(si)
        else: out.append(a)
    return red(out)

# ------------------------------------------------------------------ moves
def apply_move(gens, rels, mv):
    """apply one move to a canonical presentation; returns canonical presentation.  Raises on invalid move."""
    t = mv[0]
    if t == 'elim':
        _, g, j = mv
        r = rels[j]
        if g not in gens or occurrences(r, g) != 1: raise ValueError('bad elim')
        p = next(i for i, a in enumerate(r) if abs(a) == g)
        w = rot(r, p); e = 1 if w[0] > 0 else -1; u = w[1:]
        sub = inv(u) if e == 1 else u
        nrels = [substitute(x, g, sub) for i, x in enumerate(rels) if i != j]
        return canon([x for x in gens if x != g], nrels)
    if t == 'nielsen':
        _, x, a, d, side = mv
        if x == a or x not in gens or a not in gens or d not in (1, -1): raise ValueError('bad nielsen')
        ad = (a,) if d == 1 else (-a,)
        sub = ((x,) + ad) if side == 'R' else (ad + (x,))
        return canon(gens, [substitute(r, x, sub) for r in rels])
    if t == 'mult':
        _, i, j, e, kj, ki = mv
        if i == j: raise ValueError('bad mult')
        rj = rels[j] if e == 1 else inv(rels[j])
        new = red(rot(rj, kj) + rot(rels[i], ki))
        nrels = list(rels); nrels[i] = new
        return canon(gens, nrels)
    raise ValueError('unknown move')

# ------------------------------------------------------------------ elimination
def elim_candidates(gens, rels):
    """list of (growth, g, j): g occurs exactly once in relator j"""
    occ = {g: 0 for g in gens}
    per = []
    for r in rels:
        d = {}
        for a in r:
            d[abs(a)] = d.get(abs(a), 0) + 1
        per.append(d)
        for g, c in d.items(): occ[g] += c
    out = []
    for j, d in enumerate(per):
        L = len(rels[j])
        for g, c in d.items():
            if c == 1:
                other = occ[g] - 1
                growth = other * (L - 2) - L
                out.append((growth, g, j))
    return out

# ------------------------------------------------------------------ Whitehead length reduction
def whitehead_best(gens, rels, allow_zero=False, rng=None):
    """Best Whitehead automorphism (A, a): returns (delta, a, A) with delta < 0 (or <= 0 if allow_zero), else None.
    Letters are signed ints.  phi(y) = P(y) y S(y), P(y) = a^-1 iff y^-1 in A, S(y) = a iff y in A (y != a^{+-1})."""
    if len(gens) < 2: return None
    pair = {}
    for r in rels:
        m = len(r)
        for k in range(m):
            u, v = r[k], r[(k + 1) % m]
            pair[(u, v)] = pair.get((u, v), 0) + 1
    if not pair: return None
    pairs = list(pair.items())
    best = None
    gl = list(gens)
    for a0 in gl:
        for a in (a0, -a0):
            others = [g for g in gl if g != a0]
            k = len(others)
            # enumerate A: for each other generator x, 2 bits: (x in A, x^-1 in A)
            for mask in range(1, 4 ** k):
                inA = {a: True, -a: False}
                for idx, x in enumerate(others):
                    b = (mask >> (2 * idx)) & 3
                    inA[x] = bool(b & 1); inA[-x] = bool(b & 2)
                delta = 0
                for (u, v), c in pairs:
                    su = 0 if abs(u) == a0 else (1 if inA[u] else 0)
                    pv = 0 if abs(v) == a0 else (1 if inA[-v] else 0)
                    if su == pv: continue
                    if su:   # gap word a
                        delta += c * (-1 if v == -a else 1)
                    else:    # gap word a^-1
                        delta += c * (-1 if u == a else 1)
                if delta < 0 or (allow_zero and delta == 0):
                    key = (delta, rng.random() if rng else 0)
                    if best is None or key < best[0]:
                        best = (key, a, dict(inA))
    if best is None: return None
    return best[0][0], best[1], best[2]

def whitehead_moves(gens, a, inA):
    """elementary Nielsen moves realising the Whitehead automorphism (A, a)"""
    a0 = abs(a); d = 1 if a > 0 else -1
    mv = []
    for x in gens:
        if x == a0: continue
        if inA.get(x): mv.append(('nielsen', x, a0, d, 'R'))        # x -> x a
        if inA.get(-x): mv.append(('nielsen', x, a0, -d, 'L'))      # x -> a^-1 x
    return mv

# ------------------------------------------------------------------ substring replacement (relator multiplication)
def _enc(w):
    return ''.join(chr(0x10000 + 5000 + a) for a in w)

def best_substring_mult(rels, strict=True, rng=None, maxlen=20000):
    """find i != j and a common cyclic subword s of r_i and r_j^e with 2|s| > |r_j| (>= if not strict);
    returns (gain, move) for the largest gain = 2|s| - |r_j|, or None.  (C-speed str.find on encoded words.)"""
    best = None
    n = len(rels)
    enc = [_enc(r) for r in rels]
    encd = [x + x for x in enc]
    for j in range(n):
        mj = len(rels[j])
        if mj == 0 or mj > maxlen: continue
        L = mj // 2 + 1 if strict else (mj + 1) // 2
        if L < 1: continue
        for e in (1, -1):
            dj = encd[j] if e == 1 else _enc(inv(rels[j])) * 2
            for i in range(n):
                if i == j: continue
                mi = len(rels[i])
                if mi < L: continue
                di = encd[i]
                for kj in range(mj):
                    pos = di.find(dj[kj:kj + L])
                    if pos < 0 or pos >= mi: continue
                    k = pos
                    ln = L
                    while ln < mj and ln < mi and di[(k + ln) % (2 * mi)] == dj[(kj + ln) % (2 * mj)]:
                        ln += 1
                    gain = 2 * ln - mj
                    if gain > 0 or (not strict and gain == 0):
                        # new r_i = rot(r_j^e, kj)^-1 . rot(r_i, k)  =  rot(r_j^-e, mj - kj) . rot(r_i, k)
                        mv = ('mult', i, j, -e, (mj - kj) % mj, k)
                        key = (gain, rng.random() if rng else 0)
                        if best is None or key > best[0]:
                            best = (key, mv)
                    break   # one match per (i, j, e)
    if best is None: return None
    return best[0][0], best[1]

# ------------------------------------------------------------------ driver
def simplify(gens, rels, seed=0, time_budget=10.0, max_total=200000, restarts=40, verbose=False):
    """Try to reduce to <g | >.  Returns (success, moves, final_presentation, stats)."""
    rng = random.Random(seed)
    g0, r0 = canon(gens, rels)
    t_end = time.time() + time_budget
    best_final = None
    stats = {'attempts': 0}
    L0 = total_len(r0)
    for attempt in range(restarts):
        stats['attempts'] += 1
        # adaptive length cap: elimination orders that blow relators up are abandoned early and retried with
        # randomisation (a single uncapped greedy attempt can crawl for minutes at 50k+ letters)
        cap = min(max_total, int(max(4000, 10 * L0) * (1.6 ** attempt)))
        G, R = g0, r0
        moves = []
        noise = 0.0 if attempt == 0 else min(1.0, 0.15 * attempt)
        neutral_budget = 0 if attempt == 0 else 30 + 10 * attempt
        stuck = False
        while True:
            if time.time() > t_end: stuck = True; break
            if len(G) == 1 and not R:
                return True, moves, (G, R), stats
            if total_len(R) > cap: stuck = True; break
            # 1. eliminations
            cands = elim_candidates(G, R)
            if cands:
                if noise and rng.random() < noise:
                    cands.sort(); c = rng.choice(cands[:max(1, len(cands) // 3)])
                else:
                    c = min(cands)
                mv = ('elim', c[1], c[2])
                G, R = apply_move(G, R, mv); moves.append(mv); continue
            # 2. shortening relator multiplication
            sm = best_substring_mult(R, strict=True, rng=rng if noise else None)
            if sm is not None:
                mv = sm[1]
                G, R = apply_move(G, R, mv); moves.append(mv); continue
            # 3. Whitehead length reduction
            wh = whitehead_best(G, R, rng=rng if noise else None) if len(G) <= 6 else None
            if wh is not None:
                L0 = total_len(R)
                for mv in whitehead_moves(G, wh[1], wh[2]):
                    G, R = apply_move(G, R, mv); moves.append(mv)
                if total_len(R) > L0 + wh[0] and verbose: print('whitehead formula mismatch', L0, wh[0], total_len(R))
                continue
            # 4. neutral moves (only in randomised attempts)
            if neutral_budget > 0:
                neutral_budget -= 1
                opts = []
                sm = best_substring_mult(R, strict=False, rng=rng)
                if sm is not None: opts.append(('sub', sm[1]))
                if len(G) <= 6:
                    wh = whitehead_best(G, R, allow_zero=True, rng=rng)
                    if wh is not None: opts.append(('wh', wh))
                if len(R) >= 2:
                    i, j = rng.sample(range(len(R)), 2)
                    if len(R[j]) <= 2 * max(1, len(R[i])):
                        opts.append(('rand', ('mult', i, j, rng.choice((1, -1)), rng.randrange(len(R[j])), rng.randrange(len(R[i])))))
                if not opts: stuck = True; break
                kind, x = rng.choice(opts)
                if kind == 'wh':
                    for mv in whitehead_moves(G, x[1], x[2]):
                        G, R = apply_move(G, R, mv); moves.append(mv)
                else:
                    G, R = apply_move(G, R, x); moves.append(x)
                continue
            stuck = True; break
        fin = (G, R)
        if best_final is None or (len(G), total_len(R)) < (len(best_final[0]), total_len(best_final[1])):
            best_final = fin
        if time.time() > t_end: break
    return False, None, best_final, stats
