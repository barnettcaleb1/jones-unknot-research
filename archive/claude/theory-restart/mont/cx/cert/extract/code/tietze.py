"""pi_1(S^3 - K) of the covering knot of a halfword from its plat structure (all caps, then crossings, then cups, in the full
symmetric Morse word of tools/alex.symmetrize), and greedy Tietze reduction with a replayable log.
Presentation: each cap creates a generator g on its left strand and g^-1 on its right strand (loop around a cap's two ends is
trivial); a crossing ('x', i) acts by the Artin automorphism sigma_i (x_i -> x_i x_{i+1} x_i^-1, x_{i+1} -> x_i), ('y', i) by its
inverse (one global convention; a global mirror does not change pi_1); a cup at (i, i+1) gives the relator w_i w_{i+1} and
removes the two strands.  Validated by Fox calculus against tools/alex.py (determinant and |Delta(2)|, |Delta(3)|)."""
import sys
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')
import alex
def red(w):
    out = []
    for a in w:
        if out and out[-1] == -a: out.pop()
        else: out.append(a)
    return tuple(out)
def inv(w): return tuple(-a for a in reversed(w))
def cyc(w):
    w = list(red(w))
    while len(w) >= 2 and w[0] == -w[-1]: w = w[1:-1]
    return tuple(w)
def presentation(word):
    full = alex.symmetrize(alex.parse(word))
    strands = [(1,), (-1,)]; rels = []; ng = 1          # the initial top cap of s. (alex.diagram starts with pos = [0,0])
    for c, i in full:
        if c in 'lr':
            ng += 1; strands[i:i] = [(ng,), (-ng,)]
        elif c in 'xy':
            a, b = strands[i], strands[i + 1]
            if c == 'x': strands[i], strands[i + 1] = red(a + b + inv(a)), a
            else: strands[i], strands[i + 1] = b, red(inv(b) + a + b)
        elif c == 'u':
            rels.append(cyc(strands[i] + strands[i + 1])); del strands[i:i + 2]
    assert not strands
    return ng, rels
def subst(w, g, img):
    out = []
    for a in w:
        if abs(a) == g: out.extend(img if a > 0 else inv(img))
        else: out.append(a)
    return cyc(out)
def canon(r):
    """canonical representative of a relator up to cyclic permutation and inversion (for deduplication)"""
    if not r: return ()
    cands = []
    for w in (r, inv(r)):
        for k in range(len(w)): cands.append(w[k:] + w[:k])
    return min(cands)
def simplify(ng, rels, maxlen=4000):
    """greedy Tietze: repeatedly eliminate a generator occurring exactly once in some relator.  Returns (gens, rels, log)."""
    gens = set(range(1, ng + 1)); rels = [cyc(r) for r in rels]; log = []
    while True:
        rels = [r for r in rels if r]
        seen = {}; nr = []
        for r in rels:
            k = canon(r)
            if k not in seen: seen[k] = 1; nr.append(r)
        rels = nr
        best = None
        for ri, r in enumerate(rels):
            cnt = {}
            for a in r: cnt[abs(a)] = cnt.get(abs(a), 0) + 1
            for g, c in cnt.items():
                if c == 1:
                    occ = sum(1 for s in rels for a in s if abs(a) == g)
                    key = (len(r), occ)
                    if best is None or key < best[0]: best = (key, ri, g)
        if best is None: break
        _, ri, g = best
        r = rels[ri]; k = next(j for j, a in enumerate(r) if abs(a) == g)
        u, v = r[:k], r[k + 1:]
        img = red(inv(u) + inv(v)) if r[k] > 0 else red(v + u)
        log.append((canon(r), g))
        rels = [subst(s, g, img) for j, s in enumerate(rels) if j != ri]
        gens.discard(g)
        if any(len(s) > maxlen for s in rels): break
    return gens, rels, log
def certify(word):
    ng, rels = presentation(word)
    gens, rest, log = simplify(ng, rels)
    ok = (len(gens) == 1 and all(len(r) == 0 for r in rest))
    return ok, {'ngen0': ng, 'nrel0': len(rels), 'gens_left': len(gens), 'rels_left': [len(r) for r in rest], 'log': log}
def replay(word, log):
    """re-run the logged eliminations: each step must find a relator equal (up to cyclic permutation/inversion) to the logged one,
    in which the logged generator occurs exactly once; returns (gens_left, rels_left)"""
    ng, rels = presentation(word)
    gens = set(range(1, ng + 1)); rels = [cyc(r) for r in rels]
    for key, g in log:
        rels = [r for r in rels if r]
        ri = next(j for j, r in enumerate(rels) if canon(r) == tuple(key))
        r = rels[ri]
        assert sum(1 for a in r if abs(a) == g) == 1
        k = next(j for j, a in enumerate(r) if abs(a) == g)
        u, v = r[:k], r[k + 1:]
        img = red(inv(u) + inv(v)) if r[k] > 0 else red(v + u)
        rels = [subst(s, g, img) for j, s in enumerate(rels) if j != ri]
        gens.discard(g)
    rels = [r for r in rels if r]
    return gens, rels
# ---------------- Fox calculus check ----------------
def fox_alexander(word, tval):
    """|det| of the Alexander matrix (Fox derivatives, abelianised g -> t) with one column and one row deleted, at t = tval"""
    from fractions import Fraction
    ng, rels = presentation(word)
    # abelianisation g_k -> t^(eps_k): signs fixed by requiring exponent sum 0 on every relator (orientation of each cap)
    eps = {1: 1}; changed = True
    ev = []
    for r in rels:
        e = {}
        for a in r: e[abs(a)] = e.get(abs(a), 0) + (1 if a > 0 else -1)
        ev.append({g: c for g, c in e.items() if c})
    while changed:
        changed = False
        for e in ev:
            unk = [g for g in e if g not in eps]
            if len(unk) == 1:
                g = unk[0]; s = sum(c * eps[h] for h, c in e.items() if h != g)
                eps[g] = -s // e[g]; changed = True
    assert len(eps) == ng and all(sum((1 if a > 0 else -1) * eps[abs(a)] for a in r) == 0 for r in rels), 'abelianisation'
    def fox(r, g):
        tot = Fraction(0); e = 0
        for a in r:
            if a == g: tot += Fraction(tval) ** e
            if a == -g: tot -= Fraction(tval) ** (e - eps[g])
            e += (1 if a > 0 else -1) * eps[abs(a)]
        return tot * (1 if eps[g] == 1 else 1)
    M = [[fox(r, g) for g in range(1, ng)] for r in rels[:-1]]   # delete the last generator and the last relator
    n = len(M)
    det = Fraction(1); M = [row[:] for row in M]
    for c in range(n):
        p = next((i for i in range(c, n) if M[i][c] != 0), None)
        if p is None: return 0
        if p != c: M[c], M[p] = M[p], M[c]; det = -det
        det *= M[c][c]
        for i in range(c + 1, n):
            f = M[i][c] / M[c][c]
            if f: M[i] = [x - f * y for x, y in zip(M[i], M[c])]
    return abs(det)
def presentation_rev(word):
    """presentation read from the BOTTOM (diagram reflected top <-> bottom: events reversed, cups <-> caps, x <-> y; this is
    a diagram of the mirror image, whose complement has an isomorphic pi_1)"""
    full = alex.symmetrize(alex.parse(word))
    ev = []
    for c, i in full:
        if c in 'lr': ev.append(('u', i))
        elif c == 'u': ev.append(('l', i))
        else: ev.append(('y' if c == 'x' else 'x', i))
    ev = ev[::-1] + [('u', 0)]          # the implicit initial cap of s. becomes the final cup
    strands = []; rels = []; ng = 0
    for c, i in ev:
        if c == 'l':
            ng += 1; strands[i:i] = [(ng,), (-ng,)]
        elif c in 'xy':
            a, b = strands[i], strands[i + 1]
            if c == 'x': strands[i], strands[i + 1] = red(a + b + inv(a)), a
            else: strands[i], strands[i + 1] = b, red(inv(b) + a + b)
        else:
            rels.append(cyc(strands[i] + strands[i + 1])); del strands[i:i + 2]
    assert not strands
    return ng, rels
def simplify_rand(ng, rels, rnd, maxlen=4000):
    """greedy Tietze with random tie-breaking among the best few choices"""
    gens = set(range(1, ng + 1)); rels = [cyc(r) for r in rels]; log = []
    while True:
        rels = [r for r in rels if r]
        seen = {}; nr = []
        for r in rels:
            k = canon(r)
            if k not in seen: seen[k] = 1; nr.append(r)
        rels = nr
        cands = []
        for ri, r in enumerate(rels):
            cnt = {}
            for a in r: cnt[abs(a)] = cnt.get(abs(a), 0) + 1
            for g, c in cnt.items():
                if c == 1: cands.append((len(r), ri, g))
        if not cands: break
        cands.sort(); cut = cands[:3]
        _, ri, g = rnd.choice(cut)
        r = rels[ri]; k = next(j for j, a in enumerate(r) if abs(a) == g)
        u, v = r[:k], r[k + 1:]
        img = red(inv(u) + inv(v)) if r[k] > 0 else red(v + u)
        log.append((canon(r), g))
        rels = [subst(s, g, img) for j, s in enumerate(rels) if j != ri]
        gens.discard(g)
        if any(len(s) > maxlen for s in rels): break
    return gens, rels, log
def certify_multi(word, tries=20, seed=0):
    """try: greedy top-down, greedy bottom-up, then randomised orders on both; returns (ok, info) with a replayable log"""
    import random
    rnd = random.Random(seed)
    for direction, pres in (('top', presentation), ('bottom', presentation_rev)):
        ng, rels = pres(word)
        gens, rest, log = simplify(ng, rels)
        if len(gens) == 1 and all(len(r) == 0 for r in rest):
            return True, {'direction': direction, 'log': log, 'ngen0': ng}
    for k in range(tries):
        direction, pres = (('top', presentation), ('bottom', presentation_rev))[k % 2]
        ng, rels = pres(word)
        gens, rest, log = simplify_rand(ng, rels, rnd)
        if len(gens) == 1 and all(len(r) == 0 for r in rest):
            return True, {'direction': direction, 'log': log, 'ngen0': ng}
    return False, {}
def replay_dir(word, direction, log):
    pres = presentation if direction == 'top' else presentation_rev
    ng, rels = pres(word)
    gens = set(range(1, ng + 1)); rels = [cyc(r) for r in rels]
    for key, g in log:
        rels = [r for r in rels if r]
        ri = next(j for j, r in enumerate(rels) if canon(r) == tuple(key))
        r = rels[ri]
        assert sum(1 for a in r if abs(a) == g) == 1, 'generator does not occur exactly once'
        k = next(j for j, a in enumerate(r) if abs(a) == g)
        u, v = r[:k], r[k + 1:]
        img = red(inv(u) + inv(v)) if r[k] > 0 else red(v + u)
        rels = [subst(s, g, img) for j, s in enumerate(rels) if j != ri]
        gens.discard(g)
    rels = [r for r in rels if r]
    return gens, rels
