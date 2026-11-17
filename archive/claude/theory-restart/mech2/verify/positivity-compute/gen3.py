#!/usr/bin/env python3
"""Enumerate all three-strand half-diagram projections  s.(cap at 1|2).<c crossings at positions 0,1,2>.u(1|2), c = 5..9,
keep those whose symmetric diagram is a knot, and produce the unique all-negative word of each projection
(crossing letters forced by the orientations: axis -> y; off-axis parallel -> x, antiparallel -> y)."""
import sys, itertools, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sidiag as S

def negative_word(capi, pos, cupi):
    """returns the all-negative word (with cap letter 'l' as placeholder) or None if not a knot / invalid"""
    half = [('l', capi)] + [('x', p) for p in pos] + [('u', cupi)]
    full = S.full_word(half)
    K = S.Knot(full)
    if not K.valid or not K.ok:
        return None
    # choose letters: crossing with letter x has sign s; if s > 0 switch to y (changes the sign), axis: y
    src = []
    for hi, (c, s) in enumerate(half):
        src += [hi] if s == 0 else [hi, hi]
    letters = {}
    for x in K.cr:
        hi = src[x['src']]
        want = 'x' if x['sign'] < 0 else 'y'
        if hi in letters and letters[hi] != want:
            raise RuntimeError('mirror pair disagrees')
        letters[hi] = want
    w = []
    for hi, (c, s) in enumerate(half):
        if c == 'x':
            w.append(letters[hi] + str(s))
        else:
            w.append(c + str(s))
    return 's.' + '.'.join(w)

def mirror(word):
    return word.replace('x', 'X').replace('y', 'x').replace('X', 'y')

if __name__ == '__main__':
    cmin, cmax = int(sys.argv[1]), int(sys.argv[2])
    out = open(sys.argv[3], 'w')
    tot = 0; knots = 0
    for c in range(cmin, cmax + 1):
        n_c = 0
        for capi in (1, 2):
            for cupi in (1, 2):
                for pos in itertools.product((0, 1, 2), repeat=c):
                    tot += 1
                    w = negative_word(capi, pos, cupi)
                    if w is None:
                        continue
                    knots += 1; n_c += 1
                    out.write(w + '\n')
        print('c =', c, 'knot projections:', n_c, flush=True)
    print('projections', tot, 'knots', knots)
