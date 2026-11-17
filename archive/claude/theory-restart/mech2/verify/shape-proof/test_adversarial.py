#!/usr/bin/env python3
"""Adversarial tests of Theorem A (my code).
 T1. All arcs with moves +-D, +-P_2 (up to NMOVES moves) and arbitrary tails at the free S-sides of the end generators:
     first-order solvable  ==>  no composable D/P junction ?
 T2. Obstructed pieces together with a second component at every relative bigrading in a window: still obstructed ?
 T3. Compact components without b-generators.
"""
import sys
from itertools import product
from tdu import *

def junction_types(word):
    """word = list of moves ('D',a,s) / ('P',n,s) along the arc (b-generators x_0..x_n).  Returns list of
    (index of b-generator, 'composable'|'source'|'sink')."""
    out = []
    for i in range(len(word) - 1):
        m1, m2 = word[i], word[i + 1]
        # at generator x_{i+1}: m1 arrives (sign s1: + means arrow INTO x_{i+1}), m2 departs (sign + means arrow OUT of x_{i+1})
        in1 = m1[2] > 0        # arrow of m1 enters x_{i+1}
        in2 = m2[2] < 0        # arrow of m2 enters x_{i+1}
        if in1 and in2:
            out.append((i + 1, 'sink'))
        elif (not in1) and (not in2):
            out.append((i + 1, 'source'))
        else:
            out.append((i + 1, 'composable'))
    return out

def tails(maxlen, Sodd=(1, 3), Dp=(1, 2), Sev=(2, 4)):
    """all tails with 1..maxlen c-generators, as lists of raw steps, read from the b-generator outwards."""
    res = [[]]
    def rec(cur):
        if len(cur) == maxlen:
            return
        if len(cur) == 0:
            opts = [('s', 'S', k, s) for k in Sodd for s in (1, -1)]
        elif cur[-1][1] == 'S':
            opts = [('s', 'D', k, s) for k in Dp for s in (1, -1)]
        else:
            opts = [('s', 'S', k, s) for k in Sev for s in (1, -1)]
        for o in opts:
            new = cur + [o]
            res.append(new)
            rec(new)
    rec([])
    return res

def rev_steps(steps):
    """the same chain travelled in the opposite direction."""
    return [(a, b, c, -d) for (a, b, c, d) in reversed(steps)]

def T1(NMOVES=4, TL=4, TL2=3):
    print('T1. arcs with moves +-D, +-P_2, up to %d moves, tails up to %d c-generators (up to %d when both ends carry one)' % (NMOVES, TL, TL2))
    tl = tails(TL)
    tl2 = tails(TL2)
    total = 0; solv = 0; bad = []
    comp_tail_solvable = {}
    for n in range(1, NMOVES + 1):
        for first in ('D', 'P'):
            kinds = [first if i % 2 == 0 else ('P' if first == 'D' else 'D') for i in range(n)]
            for signs in product((1, -1), repeat=n):
                word = [(k, 1 if k == 'D' else 2, s) for k, s in zip(kinds, signs)]
                js = junction_types(word)
                has_comp = any(t == 'composable' for (_, t) in js)
                start_free_S = (kinds[0] == 'D')       # x_0's S-side is free
                end_free_S = (kinds[-1] == 'D')        # x_n's S-side is free
                both = start_free_S and end_free_S
                T0 = (tl2 if both else tl) if start_free_S else [[]]
                T1_ = (tl2 if both else tl) if end_free_S else [[]]
                for t0 in T0:
                    for t1 in T1_:
                        full = rev_steps(t0) + word + t1
                        # the walk starts at the far end of tail t0: its idempotent is c if t0 is non-empty
                        start_idem = B
                        if t0:
                            # idempotent of the far end: all tail generators are c
                            start_idem = C
                        td = build(full, start_idem=start_idem)
                        if td is None:
                            continue
                        total += 1
                        res = first_order(td)
                        if res['solvable']:
                            solv += 1
                            if has_comp:
                                bad.append((word, t0, t1))
    print('   %d arcs tested, %d pass the first-order test, %d of those contain a composable D/P junction' % (total, solv, len(bad)))
    for b in bad[:20]:
        print('      COUNTEREXAMPLE CANDIDATE:', b)
    return bad

def T1b():
    """which 'D then tail' junctions pass (information; not covered by Theorem A)."""
    print('T1b. single D-arrow w -D-> x with tails on both S-sides (tails up to 5 c-generators, standard shapes S (D S^2)^j D and truncations):')
    def std_tail(ncgens, sign):
        steps = []
        for i in range(ncgens):
            if i == 0:
                steps.append(('s', 'S', 1, sign))
            elif i % 2 == 1:
                steps.append(('s', 'D', 1, sign))
            else:
                steps.append(('s', 'S', 2, sign))
        return steps
    for nw in range(0, 7):
        row = []
        for nx in range(0, 7):
            tw = std_tail(nw, 1)       # tail leaving w
            tx = std_tail(nx, 1)       # tail leaving x
            full = rev_steps(tw) + [('D', 1, 1)] + tx
            td = build(full, start_idem=C if tw else B)
            res = first_order(td)
            row.append('ok ' if res['solvable'] else 'OBS')
        print('   tail at w: %d c-gens | tail at x = 0..6 c-gens: %s' % (nw, ' '.join(row)))

def T2():
    print('T2. obstructed arcs plus a second component at every relative bigrading (dh in -12..12, dq in -24..24):')
    P = lambda n, s: ('P', n, s)
    Dm = lambda a, s: ('D', a, s)
    TAIL4 = [('s', 'S', 1, 1), ('s', 'D', 1, 1), ('s', 'S', 2, 1), ('s', 'D', 1, 1)]
    obstructed = {
        'D then P': build([Dm(1, 1), P(2, 1)]),
        'P then D': build([P(2, 1), Dm(1, 1)]),
        'zigzag with one composable junction': build([P(2, 1), Dm(1, -1), P(2, 1), Dm(1, 1), P(2, -1)]),
    }
    seconds = {
        'point b': build([]),
        'point c': build([], start_idem=C),
        'unit square': build([P(2, 1), Dm(1, 1), P(2, -1), Dm(1, -1)], compact=True),
        '3_1 arc': build([P(2, 1), Dm(1, -1)] + TAIL4),
        'D then P (a second obstructed piece)': build([Dm(1, 1), P(2, 1)]),
        'P then D (a second obstructed piece)': build([P(2, 1), Dm(1, 1)]),
        'c-loop [c -D-> c, c -S^2-> c]': build([('s', 'D', 1, 1), ('s', 'S', 2, -1)], compact=True, start_idem=C),
        'rational arc b -D-> b -S-> c': build([Dm(1, 1), ('s', 'S', 1, 1)]),
        'tail-like arc c -D-> c -S^2-> c -D-> c': build([('s', 'D', 1, 1), ('s', 'S', 2, 1), ('s', 'D', 1, 1)], start_idem=C),
    }
    for n1, t1 in obstructed.items():
        for n2, t2 in seconds.items():
            cnt = 0; solv = []
            for dh in range(-12, 13):
                for dq in range(-24, 25):
                    u = t1.disjoint_union(t2, dh, dq)
                    cnt += 1
                    if first_order(u)['solvable']:
                        solv.append((dh, dq))
            print('   %-38s + %-40s: %d shifts, solvable at %d of them %s' % (n1, n2, cnt, len(solv), solv[:6] if solv else ''))

def T3():
    print('T3. compact components without b-generators (hypotheses (U1), (U2) hold vacuously):')
    for title, word in [
        ('[c -D-> c, c -S^2-> c]  (cone of H on c; e.g. Q_infty with a knot having H-torsion of order 1 tied in)', [('s', 'D', 1, 1), ('s', 'S', 2, -1)]),
        ('[c -D^2-> c, c -S^4-> c]', [('s', 'D', 2, 1), ('s', 'S', 4, -1)]),
        ('4 c-generators: +D, +S^2, -D, -S^2', [('s', 'D', 1, 1), ('s', 'S', 2, 1), ('s', 'D', 1, -1), ('s', 'S', 2, -1)]),
    ]:
        td = build(word, compact=True, start_idem=C)
        if td is None:
            print('   %s: does not close up' % title)
            continue
        res = first_order(td)
        print('   %s: %d generators, mu_4 term %s, first order %s' % (title, len(td.gens), 'zero' if not res['obstruction'] else 'NON-ZERO',
              'SOLVABLE' if res['solvable'] else 'obstructed'))

if __name__ == '__main__':
    which = sys.argv[1:] or ['T3', 'T1b', 'T2', 'T1']
    if 'T3' in which: T3(); print()
    if 'T1b' in which: T1b(); print()
    if 'T2' in which: T2(); print()
    if 'T1' in which: T1()
