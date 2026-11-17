#!/usr/bin/env python3
"""Brute-force type-b complex of a 1-3 tangle diagram (Morse word) and its homology N over F_2.
Only for small diagrams (<= ~16 crossings)."""
import sys, collections, itertools
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mech2/states/py')
from bcube import *

def cutpoint_structure(word):
    widths = [1]
    for (c, i) in word:
        w = widths[-1]
        widths.append(w + 2 if c in 'lr' else (w - 2 if c == 'u' else w))
    base = [0]
    for w in widths:
        base.append(base[-1] + w)
    return widths, base

def components(word, bits, widths, base):
    """bits: dict level->0/1 for crossing levels. returns comp[point] canonical (min point id)."""
    n = base[-1]
    par = list(range(n))
    def find(a):
        while par[a] != a:
            par[a] = par[par[a]]
            a = par[a]
        return a
    def union(a, b):
        a, b = find(a), find(b)
        if a != b:
            if a < b: par[b] = a
            else: par[a] = b
    for lev, (c, i) in enumerate(word):
        w = widths[lev]
        A, B = base[lev], base[lev + 1]
        if c in 'xy':
            is_e = (bits[lev] == 1) == one_is_e(c)
            for j in range(w):
                if j == i or j == i + 1:
                    continue
                union(A + j, B + j)
            if is_e:
                union(A + i, A + i + 1); union(B + i, B + i + 1)
            else:
                union(A + i, B + i); union(A + i + 1, B + i + 1)
        elif c in 'lr':
            union(B + i, B + i + 1)
            for j in range(w):
                union(A + j, B + (j if j < i else j + 2))
        else:
            union(A + i, A + i + 1)
            for j in range(w):
                if j == i or j == i + 1: continue
                union(A + j, B + (j if j < i else j - 2))
    return [find(a) for a in range(n)]

def full_homology(word, verbose=False):
    """returns dict (h,q) -> betti, with h = |s|, q = |s| + sum of labels (no shifts)."""
    widths, base = cutpoint_structure(word)
    cr = crossings_of(word)
    nc = len(cr)
    top_pt = 0
    bot = [base[len(word)] + j for j in range(3)]
    states = {}
    for mask in range(1 << nc):
        bits = {cr[j]: (mask >> j) & 1 for j in range(nc)}
        comp = components(word, bits, widths, base)
        # type
        if comp[top_pt] == comp[bot[2]] and comp[bot[0]] == comp[bot[1]] and comp[top_pt] != comp[bot[0]]:
            strands = (comp[top_pt], comp[bot[0]])
            circles = sorted(set(comp) - set(strands))
            states[mask] = (comp, strands, circles)
    if verbose:
        print('b-states', len(states), 'of', 1 << nc)
    # generators by (h,q)
    gens = collections.defaultdict(list)
    for mask, (comp, strands, circles) in states.items():
        h = bin(mask).count('1')
        for lab in itertools.product((1, -1), repeat=len(circles)):
            q = h + sum(lab)
            gens[(h, q)].append((mask, lab))
    index = {}
    for key, L in gens.items():
        for n, g in enumerate(L):
            index[(key, g)] = n
    def d(mask, lab):
        comp, strands, circles = states[mask]
        lbl = dict(zip(circles, lab))
        out = []
        for j in range(nc):
            if (mask >> j) & 1:
                continue
            m2 = mask | (1 << j)
            if m2 not in states:
                continue
            comp2, strands2, circles2 = states[m2]
            lev = cr[j]; i = word[lev][1]
            pts = [base[lev] + i, base[lev] + i + 1, base[lev + 1] + i, base[lev + 1] + i + 1]
            A = sorted(set(comp[p] for p in pts)); B = sorted(set(comp2[p] for p in pts))
            # untouched circles keep names
            newlbl = {c: lbl[c] for c in circles if c not in A}
            if len(A) == 2 and len(B) == 1:
                a1, a2 = A
                tgt = B[0]
                s1 = a1 in strands; s2 = a2 in strands
                if s1 and s2:
                    continue  # would be type c; cannot happen since m2 is type b
                if s1 or s2:
                    cc = a2 if s1 else a1
                    if lbl[cc] == 1:
                        out.append((m2, newlbl))
                else:
                    l1, l2 = lbl[a1], lbl[a2]
                    if l1 == 1 and l2 == 1:
                        nl = dict(newlbl); nl[tgt] = 1; out.append((m2, nl))
                    elif l1 * l2 == -1:
                        nl = dict(newlbl); nl[tgt] = -1; out.append((m2, nl))
            elif len(A) == 1 and len(B) == 2:
                a = A[0]
                b1, b2 = B
                if a in strands:
                    # strand -> strand + circle (circle gets -)
                    cc = b1 if b1 not in strands2 else b2
                    nl = dict(newlbl); nl[cc] = -1; out.append((m2, nl))
                else:
                    if lbl[a] == 1:
                        nl = dict(newlbl); nl[b1] = 1; nl[b2] = -1; out.append((m2, nl))
                        nl = dict(newlbl); nl[b1] = -1; nl[b2] = 1; out.append((m2, nl))
                    else:
                        nl = dict(newlbl); nl[b1] = -1; nl[b2] = -1; out.append((m2, nl))
            else:
                raise RuntimeError('unexpected saddle type %s %s' % (A, B))
        res = []
        for (m2, nl) in out:
            circles2 = states[m2][2]
            res.append((m2, tuple(nl[c] for c in circles2)))
        return res
    ranks = {}
    for key in sorted(gens):
        h, q = key
        tkey = (h + 1, q)
        if tkey not in gens:
            ranks[key] = 0
            continue
        rows = []
        for g in gens[key]:
            v = 0
            for g2 in d(*g):
                v ^= 1 << index[(tkey, g2)]
            rows.append(v)
        ranks[key] = rank_f2(rows)
    betti = {}
    for key in sorted(gens):
        h, q = key
        bt = len(gens[key]) - ranks[key] - ranks.get((h - 1, q), 0)
        if bt:
            betti[key] = bt
    return betti, {k: len(v) for k, v in gens.items()}

if __name__ == '__main__':
    half, orient, sym = read_kht(sys.argv[1])
    word, lab, wr = quotient_word(half, with_twists=False)
    print('word', '.'.join('%s%d' % t for t in word), 'writhe', wr)
    betti, sizes = full_homology(word, verbose=True)
    print('N (h,q):', sorted(betti.items()))
    qs = sorted(set(q for (h, q) in sizes))
    print('complex q-range', qs[0], qs[-1], ' total gens', sum(sizes.values()))
