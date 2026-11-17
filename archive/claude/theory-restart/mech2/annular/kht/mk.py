#!/usr/bin/env python3
"""write a .kht file for the closure of a braid (list of signed generator indices), cut open at strand 1.
sigma_i -> y(i-1), sigma_i^-1 -> x(i-1)."""
import sys
def word(braid, n):
    w = ['r%d' % i for i in range(1, n)]
    for g in braid:
        w.append(('y' if g > 0 else 'x') + str(abs(g) - 1))
    for i in range(n - 1, 0, -1): w.append('u%d' % i)
    return '.'.join(w)
if __name__ == '__main__':
    name = sys.argv[1]; n = int(sys.argv[2]); braid = [int(t) for t in sys.argv[3].split(',')]
    open('examples/knots/%s.kht' % name, 'w').write('%% %s braid %s\n%s\n,1\n' % (name, braid, word(braid, n)))
    print(word(braid, n))
