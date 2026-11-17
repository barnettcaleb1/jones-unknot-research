import sys; sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mech/maps/scripts')
from typeD import *
from collections import Counter

def twist(n):
    """DD of the vertical twist tangle with |n| crossings, antiparallel (knot-closure) orientation.
    n>0: c(-n,-2n) -S-> b(1-n,1-2n) -D-> b -S2-> b -D-> ... -> b(0,-1)   [all crossings negative]
    n<0: mirror of the above."""
    m = abs(n)
    gens = [('c', -m, -2 * m)] + [('b', i - m, 2 * i - 1 - 2 * m) for i in range(1, m + 1)]
    d = {0: [(1, ('S', 'c', 1))]}
    for i in range(1, m):
        d[i] = [(i + 1, ('D', 'b', 1) if i % 2 == 1 else ('S', 'b', 2))]
    X = TD(gens, d); X.check()
    if n < 0: X = X.mirror(); X.check()
    return X

def poincare(X, Y, hr=range(-40, 41), qr=range(-90, 91)):
    return hom_table(X, Y, hr, qr)

def show(t):
    by = {}
    for (h, q), m in sorted(t.items()):
        by.setdefault(q / 2 - h, []).append((h, q, m))
    return {dl: v for dl, v in sorted(by.items())}

if __name__ == '__main__':
    R31 = parse_chain(3, 15, '⬮~~S~>⬯—>⬯~>⬯—>⬯~>⬯<—⬯<~⬯<—⬯<~⬮<—').shift(-8, -24)
    S31 = parse_chain(-1, 9, '⬮~~S~>⬯—>⬯~>⬯—>⬯~>⬮—>⬮<~⬯<—⬯<~⬯<—⬯<~⬮<—').shift(-8, -24)
    for n in [2, -2, 4, -4]:
        X = twist(n)
        print('n =', n, ' twist complex gens', X.gens)
        print('   rational part:', show(poincare(X, R31)))
        print('   special part :', show(poincare(X, S31)))
