#!/usr/bin/env python3
"""Find single-generator representatives of classes of N in a given bidegree (small diagrams, brute force)."""
import sys, collections, itertools
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mech2/states/py')
from bcube import *
from fullcube import cutpoint_structure, components

class BCube:
    def __init__(self, word):
        self.word = word
        self.widths, self.base = cutpoint_structure(word)
        self.cr = crossings_of(word)
        self.nc = len(self.cr)
        L = len(word)
        self.top_pt = 0
        self.bot = [self.base[L] + j for j in range(3)]
        self.states = {}
        for mask in range(1 << self.nc):
            bits = {self.cr[j]: (mask >> j) & 1 for j in range(self.nc)}
            comp = components(word, bits, self.widths, self.base)
            if comp[self.top_pt] == comp[self.bot[2]] and comp[self.bot[0]] == comp[self.bot[1]] and comp[self.top_pt] != comp[self.bot[0]]:
                strands = (comp[self.top_pt], comp[self.bot[0]])
                circles = sorted(set(comp) - set(strands))
                self.states[mask] = (comp, strands, circles)
        self.gens = collections.defaultdict(list)
        for mask, (comp, strands, circles) in self.states.items():
            h = bin(mask).count('1')
            for lab in itertools.product((1, -1), repeat=len(circles)):
                self.gens[(h, h + sum(lab))].append((mask, lab))
        self.index = {}
        for key, Lst in self.gens.items():
            for n, g in enumerate(Lst):
                self.index[(key, g)] = n
    def d(self, mask, lab):
        word, base, cr = self.word, self.base, self.cr
        comp, strands, circles = self.states[mask]
        lbl = dict(zip(circles, lab))
        out = []
        for j in range(self.nc):
            if (mask >> j) & 1:
                continue
            m2 = mask | (1 << j)
            if m2 not in self.states:
                continue
            comp2, strands2, circles2 = self.states[m2]
            lev = cr[j]; i = word[lev][1]
            pts = [base[lev] + i, base[lev] + i + 1, base[lev + 1] + i, base[lev + 1] + i + 1]
            A = sorted(set(comp[p] for p in pts)); B = sorted(set(comp2[p] for p in pts))
            newlbl = {c: lbl[c] for c in circles if c not in A}
            res = []
            if len(A) == 2 and len(B) == 1:
                a1, a2 = A; tgt = B[0]
                s1 = a1 in strands; s2 = a2 in strands
                if s1 and s2:
                    continue
                if s1 or s2:
                    cc = a2 if s1 else a1
                    if lbl[cc] == 1:
                        res.append(newlbl)
                else:
                    l1, l2 = lbl[a1], lbl[a2]
                    if l1 == 1 and l2 == 1:
                        nl = dict(newlbl); nl[tgt] = 1; res.append(nl)
                    elif l1 * l2 == -1:
                        nl = dict(newlbl); nl[tgt] = -1; res.append(nl)
            elif len(A) == 1 and len(B) == 2:
                a = A[0]; b1, b2 = B
                if a in strands:
                    cc = b1 if b1 not in strands2 else b2
                    nl = dict(newlbl); nl[cc] = -1; res.append(nl)
                else:
                    if lbl[a] == 1:
                        nl = dict(newlbl); nl[b1] = 1; nl[b2] = -1; res.append(nl)
                        nl = dict(newlbl); nl[b1] = -1; nl[b2] = 1; res.append(nl)
                    else:
                        nl = dict(newlbl); nl[b1] = -1; nl[b2] = -1; res.append(nl)
            for nl in res:
                out.append((m2, tuple(nl[c] for c in circles2)))
        return out
    def dmatrix(self, key):
        h, q = key
        tkey = (h + 1, q)
        rows = []
        for g in self.gens.get(key, []):
            v = 0
            if tkey in self.gens:
                for g2 in self.d(*g):
                    v ^= 1 << self.index[(tkey, g2)]
            rows.append(v)
        return rows

def span_reduce(rows):
    """returns pivot dict for the span"""
    piv = {}
    for v in rows:
        while v:
            hb = v.bit_length() - 1
            if hb in piv:
                v ^= piv[hb]
            else:
                piv[hb] = v; break
    return piv
def in_span(piv, v):
    while v:
        hb = v.bit_length() - 1
        if hb in piv:
            v ^= piv[hb]
        else:
            return False
    return True

def single_reps(cube, key):
    """generators g in bidegree key with d g = 0 and g not a boundary"""
    h, q = key
    rows_out = cube.dmatrix(key)
    rows_in = cube.dmatrix((h - 1, q))
    piv = span_reduce(rows_in)
    res = []
    for n, g in enumerate(cube.gens.get(key, [])):
        if rows_out[n] == 0 and not in_span(piv, 1 << n):
            res.append(g)
    return res

if __name__ == '__main__':
    from show_ext import fmt
    hw = sys.argv[1]
    half = parse_word(hw)
    word, lab, wr = quotient_word(half, with_twists=False)
    cube = BCube(word)
    keys = [tuple(int(x) for x in a.split(',')) for a in sys.argv[2:]]
    for key in keys:
        reps = single_reps(cube, key)
        print('bidegree', key, 'dim C =', len(cube.gens.get(key, [])), ' single-generator cycle representatives:', len(reps))
        for (mask, labs) in reps[:30]:
            bits = tuple((mask >> j) & 1 for j in range(cube.nc))
            comp, strands, circles = cube.states[mask]
            print('   ', fmt(word, lab, bits), ' labels', ''.join('+' if x > 0 else '-' for x in labs), ' ncirc', len(circles))
