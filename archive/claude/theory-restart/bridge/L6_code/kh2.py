"""Z/2 Khovanov homology of a signed chord diagram (virtual knot mod Z-move), Manturov's convention (1-1 maps = 0)."""
import itertools, numpy as np
from collections import defaultdict

def circles(word, nonseifert):
    """word: cyclic list of chord labels; nonseifert: set of labels smoothed non-Seifert. Arcs i: pos i -> i+1.
    End ids: tail(i)=2i, head(i)=2i+1. Returns list of frozensets of arcs."""
    m = len(word); par = list(range(2*m))
    def f(a):
        while par[a] != a:
            par[a] = par[par[a]]; a = par[a]
        return a
    def u(a, b): par[f(a)] = f(b)
    for i in range(m): u(2*i, 2*i+1)          # the arc itself
    pos = defaultdict(list)
    for i, c in enumerate(word): pos[c].append(i)
    for c, (p, q) in pos.items():
        hp, tp = 2*((p-1) % m)+1, 2*p          # head of arc arriving at p, tail of arc leaving p
        hq, tq = 2*((q-1) % m)+1, 2*q
        if c in nonseifert:
            u(hp, hq); u(tp, tq)
        else:
            u(hp, tq); u(hq, tp)
    comp = defaultdict(set)
    for i in range(m): comp[f(2*i)].add(i)
    return [frozenset(s) for s in comp.values()]

def kh2(word, eps):
    """eps: dict label->+-1. returns dict (r,q)->dim over GF(2)."""
    labs = sorted(set(word)); n = len(labs)
    npos = sum(1 for c in labs if eps[c] > 0); nneg = n - npos
    pos = defaultdict(list)
    for i, c in enumerate(word): pos[c].append(i)
    m = len(word)
    def arcs_at(c):
        p, q = pos[c]; return {(p-1) % m, p, (q-1) % m, q}
    states = {}
    for s in itertools.product([0, 1], repeat=n):   # 0 = A-smoothing, 1 = B
        ns = set()
        for k, c in enumerate(labs):
            A_is_seifert = eps[c] > 0
            seif = A_is_seifert if s[k] == 0 else (not A_is_seifert)
            if not seif: ns.add(c)
        states[s] = circles(word, ns)
    # generators
    gens = {}; index = {}
    for s, cs in states.items():
        r = sum(s) - nneg
        for lab in itertools.product([1, -1], repeat=len(cs)):
            q = sum(lab) + sum(s) + npos - 2*nneg
            key = (s, lab)
            index[key] = len(gens); gens[key] = (r, q)
    # differential
    rows = defaultdict(list)   # (r,q) -> list of (src_key, tgt_key)
    entries = []
    for s, cs in states.items():
        for k in range(n):
            if s[k] == 1: continue
            t = s[:k] + (1,) + s[k+1:]
            ct = states[t]; c = labs[k]; A = arcs_at(c)
            S = [i for i, z in enumerate(cs) if z & A]; T = [j for j, z in enumerate(ct) if z & A]
            same = {}
            for i, z in enumerate(cs):
                if i in S: continue
                same[i] = ct.index(z)
            if len(S) == 1 and len(T) == 1: continue      # 1-1 bifurcation: zero map over Z/2
            for lab in itertools.product([1, -1], repeat=len(cs)):
                outs = []
                base = [None]*len(ct)
                for i, j in same.items(): base[j] = lab[i]
                if len(S) == 2 and len(T) == 1:           # merge
                    a, b = lab[S[0]], lab[S[1]]
                    if a == -1 and b == -1: continue
                    base[T[0]] = 1 if (a == 1 and b == 1) else -1
                    outs.append(tuple(base))
                elif len(S) == 1 and len(T) == 2:         # split
                    a = lab[S[0]]
                    if a == 1:
                        b1 = list(base); b1[T[0]] = 1; b1[T[1]] = -1; outs.append(tuple(b1))
                        b2 = list(base); b2[T[0]] = -1; b2[T[1]] = 1; outs.append(tuple(b2))
                    else:
                        b1 = list(base); b1[T[0]] = -1; b1[T[1]] = -1; outs.append(tuple(b1))
                else:
                    raise RuntimeError('unexpected bifurcation %s %s' % (S, T))
                for o in outs:
                    entries.append((index[(s, lab)], index[(t, o)]))
    # homology per (r,q): build matrices d_r restricted to q
    by = defaultdict(list)
    for key, (r, q) in gens.items(): by[(r, q)].append(index[key])
    pos_in = {}
    for (r, q), L in by.items():
        for k, g in enumerate(L): pos_in[g] = k
    mats = defaultdict(lambda: None)
    D = defaultdict(set)
    for a, b in entries:
        D[(a, b)] ^= {1} if False else set()
    # accumulate mod 2
    cnt = defaultdict(int)
    for a, b in entries: cnt[(a, b)] ^= 1
    blocks = defaultdict(list)
    gq = {index[k]: v for k, v in gens.items()}
    for (a, b), v in cnt.items():
        if v: blocks[gq[a]].append((a, b))
    def rank2(rowsets):
        basis = []; r = 0
        for v in rowsets:
            for bb in basis: v = min(v, v ^ bb)
            if v: basis.append(v); r += 1
        return r
    rk = {}
    for (r, q), L in by.items():
        tgt = by.get((r+1, q), [])
        rowsbits = defaultdict(int)
        for (a, b) in blocks.get((r, q), []):
            rowsbits[a] |= 1 << pos_in[b]
        rk[(r, q)] = rank2(list(rowsbits.values()))
    H = {}
    for (r, q), L in by.items():
        h = len(L) - rk[(r, q)] - rk.get((r-1, q), 0)
        if h: H[(r, q)] = h
    # sanity d^2=0 check omitted for speed; dims returned
    return H

if __name__ == '__main__':
    w = [0,1,2,0,1,2]
    print('right trefoil', sorted(kh2(w, {0:1,1:1,2:1}).items()))
    w = [0,1,2,0,3,2,1,3]
    print('fig8', sorted(kh2(w, {0:1,1:-1,2:-1,3:1}).items()), sum(kh2(w, {0:1,1:-1,2:-1,3:1}).values()))
    print('unknot R1', sorted(kh2([0,0], {0:1}).items()))
