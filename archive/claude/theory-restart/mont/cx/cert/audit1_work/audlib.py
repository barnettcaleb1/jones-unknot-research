"""audlib.py -- AUDITOR's own independent helpers (no imports from the certifier).
  * random valid halfwords (own generator, all letter kinds incl. mid-word caps/cups and axis crossings)
  * finite permutation groups with index multiplication tables, conjugacy classes
  * hom counting |{phi: pi -> G, phi(meridian) in K}|, K = C u C^-1:
      - from the PLAT presentation, by an own Morse sweep with the exact Artin action (no arcs, no signs, no PD code);
      - from an arbitrary Wirtinger-type presentation (gens, rels with rels = (-out, s*o, i, -s*o)), by DFS + propagation.
"""
import sys, random, itertools
TOOLS = '/Users/calebbarnett/jones-lanes/theory-restart/tools'
if TOOLS not in sys.path: sys.path.insert(0, TOOLS)
import alex

# ------------------------------------------------------------------ random halfwords (own grammar walker)
def rand_halfword(rnd, L, pcap=0.12, pcup=0.12, maxhw=7, axis=0.25):
    """valid halfword: hw = half width; crossings s in [0, hw-1] (s=0 axis), caps l/r s in [1, hw+1], cups s in [1, hw-1]."""
    hw = 1; toks = []
    first = rnd.choice(['l1', 'r1']); toks.append(first); hw = 3
    steps = 0
    while steps < L:
        r = rnd.random()
        if r < pcap and hw < maxhw:
            s = rnd.randint(1, hw + 1); toks.append(rnd.choice('lr') + str(s)); hw += 2
        elif r < pcap + pcup and hw >= 5:
            s = rnd.randint(1, hw - 1); toks.append('u' + str(s)); hw -= 2
        else:
            s = 0 if rnd.random() < axis else rnd.randint(1, hw - 1)
            toks.append(rnd.choice('xy') + str(s)); steps += 1
    while hw > 1:
        s = rnd.randint(1, hw - 1); toks.append('u' + str(s)); hw -= 2
    return 's.' + '.'.join(toks)

def is_knot(w):
    full = alex.symmetrize(alex.parse(w))
    return full is not None and alex.diagram(full) is not None

def ncross(w):
    full = alex.symmetrize(alex.parse(w))
    return sum(1 for c, i in full if c in 'xy')

def ncaps(w):
    full = alex.symmetrize(alex.parse(w))
    return 1 + sum(1 for c, i in full if c in 'lr')

# ------------------------------------------------------------------ permutation groups
def pm(p, q): return tuple(p[i] for i in q)
def pinv(p):
    r = [0] * len(p)
    for i, x in enumerate(p): r[x] = i
    return tuple(r)

class Group:
    def __init__(self, name, gens):
        self.name = name
        d = len(gens[0]); e = tuple(range(d))
        els = [e]; idx = {e: 0}; i = 0
        while i < len(els):
            x = els[i]; i += 1
            for g in gens:
                y = pm(g, x)
                if y not in idx: idx[y] = len(els); els.append(y)
        self.els = els; self.idx = idx; self.N = len(els); self.e = 0
        self.mul = [[idx[pm(a, b)] for b in els] for a in els]
        self.inv = [idx[pinv(a)] for a in els]
        seen = set(); self.classes = []
        for a in range(self.N):
            if a in seen: continue
            C = sorted(set(self.mul[self.mul[h][a]][self.inv[h]] for h in range(self.N)))
            seen.update(C); self.classes.append(C)
    def conj(self, o, s, x):            # o^s x o^-s
        m = self.mul
        if s > 0: return m[m[o][x]][self.inv[o]]
        return m[m[self.inv[o]][x]][o]

def cyc(n, *cs):
    p = list(range(n))
    for c in cs:
        for a, b in zip(c, c[1:] + c[:1]): p[a] = b
    return tuple(p)

def affine(p, lam):
    return [tuple((x + 1) % p for x in range(p)), tuple((lam * x) % p for x in range(p))]

def psl2(p):
    INF = p
    t = tuple(((z + 1) % p if z != INF else INF) for z in range(p + 1))
    def s(z):
        if z == INF: return 0
        if z == 0: return INF
        return (-pow(z, p - 2, p)) % p
    return [t, tuple(s(z) for z in range(p + 1))]

def groups():
    return [Group('S3', [cyc(3, (0, 1)), cyc(3, (0, 1, 2))]),
            Group('S4', [cyc(4, (0, 1)), cyc(4, (0, 1, 2, 3))]),
            Group('A4', [cyc(4, (0, 1, 2)), cyc(4, (1, 2, 3))]),
            Group('A5', [cyc(5, (0, 1, 2)), cyc(5, (0, 1, 2, 3, 4))]),
            Group('F20', affine(5, 2)),
            Group('F42', affine(7, 3)),
            Group('PSL27', psl2(7))]

def class_K(G, C):
    Cinv = sorted(set(G.inv[c] for c in C))
    K = sorted(set(C) | set(Cinv))
    reps = [C[0]] if Cinv == C else [C[0], G.inv[C[0]]]
    return K, reps, len(C)

# ------------------------------------------------------------------ PLAT count (own Artin-action sweep)
def plat_count(full, G, K, first):
    """number of homs phi with phi(g_1) = first and every cap generator in K (cap -> strands (g, g^-1);
    'x': (a,b) -> (a b a^-1, a); 'y': (a,b) -> (b, b^-1 a b); cup -> a b = 1)."""
    m = G.mul; iv = G.inv; e = G.e
    word = list(full)
    L = len(word)
    def rec(k, pos):
        while k < L:
            c, i = word[k]
            if c in 'lr':
                tot = 0
                for g in K:
                    p2 = pos[:i] + [g, iv[g]] + pos[i:]
                    tot += rec(k + 1, p2)
                return tot
            if c == 'u':
                if m[pos[i]][pos[i + 1]] != e: return 0
                pos = pos[:i] + pos[i + 2:]
            elif c == 'x':
                a, b = pos[i], pos[i + 1]
                pos = pos[:i] + [m[m[a][b]][iv[a]], a] + pos[i + 2:]
            elif c == 'y':
                a, b = pos[i], pos[i + 1]
                pos = pos[:i] + [b, m[m[iv[b]][a]][b]] + pos[i + 2:]
            else:
                raise ValueError(c)
            k += 1
        return 1 if not pos else 0
    return rec(0, [first, iv[first]])

# ------------------------------------------------------------------ Wirtinger count (DFS + propagation)
def parse_wirt(gens, rels):
    gi = {g: t for t, g in enumerate(gens)}
    R = []
    for r in rels:
        assert len(r) == 4 and r[1] == -r[3] and r[0] < 0 and r[2] > 0, r
        out = gi[-r[0]]; o = gi[abs(r[1])]; s = 1 if r[1] > 0 else -1; i = gi[r[2]]
        R.append((out, o, i, s))
    return R

def wirt_count(n, R, G, K, first):
    Kset = set(K)
    def prop(a):
        changed = True
        while changed:
            changed = False
            for out, o, i, s in R:
                vo, vi, vu = a[o], a[i], a[out]
                if vo >= 0 and vi >= 0:
                    v = G.conj(vo, s, vi)
                    if vu < 0: a[out] = v; changed = True
                    elif vu != v: return False
                elif vo >= 0 and vu >= 0 and vi < 0:
                    a[i] = G.conj(vo, -s, vu); changed = True
        return True
    def rec(a):
        if not prop(a): return 0
        free = [t for t in range(n) if a[t] < 0]
        if not free:
            return 1
        # branch on the unassigned arc that is the over arc of most relations with a known neighbour
        best = None; bs = -1
        for t in free:
            sc = sum(1 for out, o, i, s in R if o == t and (a[i] >= 0 or a[out] >= 0))
            if sc > bs: bs, best = sc, t
        tot = 0
        for g in K:
            b = list(a); b[best] = g
            tot += rec(b)
        return tot
    a = [-1] * n; a[0] = first
    return rec(a)
