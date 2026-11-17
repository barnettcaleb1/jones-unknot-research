#!/usr/bin/env python3
"""Enumerate closed curves in the strip as cyclic words of moves and test the first-order U^2 obstruction (uext.first_order).
Moves alternate between D-type (inside the lens) and P-type (outside).  usage: uenum.py MAXPAIRS [Dpowers] [Pruns]"""
import sys, itertools
from uext import *
def canonical(w):
    L = len(w); rots = [w[i:] + w[:i] for i in range(0, L, 2)]
    # also orientation reversal: reverse order and flip signs
    rev = tuple((k, n, -s) for (k, n, s) in reversed(w))
    rev = rev[-1:] + rev[:-1]        # make it start with a P-type move again? keep alternation D,P,D,P...: w = (D,P,D,P,...)
    rots += [rev[i:] + rev[:i] for i in range(0, L, 2)] if rev[0][0] == w[0][0] else []
    return min(rots)
def primitive(w):
    L = len(w)
    for d in range(2, L, 2):
        if L % d == 0 and w == w[:d] * (L // d): return False
    return True
def wraps_special(w):
    """three consecutive co-oriented moves P, D^1, P (same sign) wrap around the special puncture (KWZ Thm 4.1); cyclic"""
    L = len(w)
    for i in range(L):
        a, b, c = w[i], w[(i + 1) % L], w[(i + 2) % L]
        if a[0] == 'P' and b[0] == 'D' and c[0] == 'P' and b[1] == 1 and a[2] == b[2] == c[2]: return True
    return False
if __name__ == '__main__':
    maxpairs = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    Dp = [int(x) for x in sys.argv[2].split(',')] if len(sys.argv) > 2 else [1]
    Pn = [int(x) for x in sys.argv[3].split(',')] if len(sys.argv) > 3 else [2]
    Dm = [('D', a, s) for a in Dp for s in (1, -1)]
    Pm = [('P', n, s) for n in Pn for s in (1, -1)]
    seen = set(); tot = 0; okl = []
    for r in range(1, maxpairs + 1):
        for ds in itertools.product(Dm, repeat=r):
            for ps in itertools.product(Pm, repeat=r):
                w = tuple(x for pair in zip(ds, ps) for x in pair)
                # gradability
                h = sum(s * (1 if k == 'D' else 2 * n + 1) for (k, n, s) in w)
                q = sum(s * (2 * n if k == 'D' else 4 * n) for (k, n, s) in w)
                if h or q: continue
                if not primitive(w): continue
                c = canonical(w)
                if c in seen: continue
                seen.add(c)
                td = curve(list(w), True)
                if td is None: continue
                tot += 1
                ok = first_order(td)[0]
                if ok: okl.append((w, wraps_special(w)))
    print('D powers', Dp, 'P runs', Pn, 'max pairs', maxpairs, ': gradable primitive cyclic words:', tot, ' passing first order:', len(okl))
    for w, ws in okl:
        print('   ', ' '.join('%s%s%d' % ('+' if s > 0 else '-', k, n) for (k, n, s) in w), '  wraps special puncture:' , ws)
