#!/usr/bin/env python3
"""Synthesizer sanity check (17 Nov 2026): residue-mod-4 structure of the preferred-normalised J.
Question: is the part of J supported on t-exponents = 0 mod 4 always a single monomial (+t^k)?
Uses the project's bracket_vector (flat_search.py) on random strongly invertible half-diagram words.
J(t): y in A, t = A^-4; normalised by J(-1) = 1, J'(-1) = 0 (unique sign and shift)."""
import sys, random, json
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')
import alex, kauffman
from kauffman import padd, pdelta
from flat_search import bracket_vector, gen, is_monomial

def to_t(y):
    # y: {A-exp: coeff}, exponents congruent mod 4 -> {t-exp: coeff} with t = A^-4 (up to a shift)
    es = sorted(y)
    base = es[0]
    if any((e - base) % 4 for e in es):
        return None
    return {-(e - base)//4: v for e, v in y.items()}

def normalise(J):
    v = sum(c*(-1)**(e % 2) for e, c in J.items())
    d = sum(c*e*(-1)**((e-1) % 2) for e, c in J.items())  # J'(-1)
    if v not in (1, -1):
        return None
    # J ~ c t^m mod (t+1)^2 with m = -J'(-1)/J(-1)
    if d % v:
        return None
    m = -d//v
    c = v*(-1)**(m % 2)
    return {e - m: c*cv for e, cv in J.items()}

def residues(J):
    R = {r: {} for r in range(4)}
    for e, c in J.items():
        R[e % 4][e] = c
    return R

def main(seed, count, maxlen):
    rnd = random.Random(seed)
    seen = set(); stats = dict(knots=0, nontriv=0, ok=0, viol=0, bad=0)
    viol = []; samples = []
    for _ in range(count):
        w = gen(rnd, rnd.randint(4, maxlen))
        if not w or w in seen:
            continue
        seen.add(w)
        half = alex.parse(w)
        full = alex.symmetrize(half)
        if full is None or alex.diagram(full) is None:
            continue
        stats['knots'] += 1
        kb = kauffman.bracket(w)
        if kb is None or len(kb) == 1:
            continue
        bv = bracket_vector(half)
        if bv is None:
            continue
        y, x = bv
        u = {}; padd(u, y); padd(u, pdelta(x))
        if not is_monomial(u):
            stats['bad'] += 1; continue
        Jt = to_t(y)
        if Jt is None:
            stats['bad'] += 1; continue
        J = normalise(Jt)
        if J is None:
            stats['bad'] += 1; continue
        stats['nontriv'] += 1
        R0 = residues(J)[0]
        if len(R0) == 1 and list(R0.values())[0] == 1:
            stats['ok'] += 1
            samples.append((w, sorted(J.items()), list(R0)[0]))
        else:
            stats['viol'] += 1
            viol.append((w, sorted(J.items()), sorted(R0.items())))
    return stats, viol, samples

if __name__ == '__main__':
    seed, count, maxlen = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    stats, viol, samples = main(seed, count, maxlen)
    print('STATS', stats)
    for v in viol[:15]:
        print('VIOL', v)
    for s in samples[:8]:
        print('OK', s)
