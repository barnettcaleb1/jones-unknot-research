#!/usr/bin/env python3
"""Enumerations (my code): cyclic words in +-D^a, +-P_n; which pass the first-order test."""
import sys
from itertools import product
from tdu import *

def canon(word):
    """canonical representative of a cyclic word under rotation and reversal of the direction of travel
    (reversal = reverse the order and flip all signs)."""
    n = len(word)
    rev = tuple((k, p, -s) for (k, p, s) in reversed(word))
    best = None
    for w in (tuple(word), rev):
        for r in range(n):
            c = w[r:] + w[:r]
            if best is None or c < best:
                best = c
    return best

def primitive(word):
    n = len(word)
    for d in range(1, n):
        if n % d == 0 and word[d:] + word[:d] == tuple(word):
            return False
    return True

def gradable(word):
    h = q = 0
    for (k, p, s) in word:
        if k == 'D':
            h += s; q += 2 * p * s
        else:
            h += s * (2 * p + 1); q += s * 4 * p
    return h == 0 and q == 0

def cyclic_words(nmoves, Dpowers, Pns):
    """alternating D / P moves, nmoves even."""
    r = nmoves // 2
    Dm = [('D', a, s) for a in Dpowers for s in (1, -1)]
    Pm = [('P', n, s) for n in Pns for s in (1, -1)]
    seen = set()
    for ds in product(Dm, repeat=r):
        for ps in product(Pm, repeat=r):
            w = tuple(x for pair in zip(ds, ps) for x in pair)
            if not gradable(w) or not primitive(w):
                continue
            c = canon(w)
            if c in seen:
                continue
            seen.add(c)
            yield c

def fmt(word):
    return ' '.join(('+' if s > 0 else '-') + (('D' + ('' if p == 1 else '^%d' % p)) if k == 'D' else 'P%d' % p) for (k, p, s) in word)

def survey(title, maxmoves, Dpowers, Pns, show_pass=True):
    print(title)
    tot = 0; passed = []
    for nm in range(2, maxmoves + 1, 2):
        cnt = 0
        for w in cyclic_words(nm, Dpowers, Pns):
            td = build(list(w), compact=True)
            if td is None:
                continue
            cnt += 1
            res = first_order(td)
            if res['solvable']:
                passed.append(w)
        print('   %d moves: %d classes of gradable primitive cyclic words' % (nm, cnt))
        tot += cnt
    print('   total %d classes; %d pass the first-order test' % (tot, len(passed)))
    if show_pass:
        for w in passed:
            print('      PASS:', fmt(w))
    return passed

if __name__ == '__main__':
    survey('A. moves +-D, +-P_2, up to 10 moves', 10, [1], [2])
    survey('B. moves +-D, +-P_1, up to 10 moves', 10, [1], [1])
    survey('C. moves +-D, +-P_3, up to 10 moves', 10, [1], [3])
    survey('D. moves +-D, +-P_1, +-P_2, +-P_3 (mixed legs), up to 8 moves', 8, [1], [1, 2, 3])
    survey('E. moves +-D, +-D^2, +-P_2, up to 8 moves', 8, [1, 2], [2])
