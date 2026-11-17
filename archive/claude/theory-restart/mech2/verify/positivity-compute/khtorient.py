#!/usr/bin/env python3
"""Simulation of the orientation bookkeeping ('cuts') of kht++ for a symmetric half-diagram word (Tangles.cpp 34-120)
and of Tangle::writhe (1195-1215). fix_letters(word) returns the word with cap letters l/r chosen so that no cup has
an orientation mismatch (so kht++ never has to auto-correct), plus the kht-style writhe."""
import sys, os, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sidiag as S

def cuts_of(half, top=1):
    cuts = [[top, top]]
    for (c, i) in half:
        cur = list(cuts[-1])
        if c in 'xy':
            if i == 0:
                cur[1] = 1 - cur[1]
            else:
                cur[i], cur[i + 1] = cur[i + 1], cur[i]
        elif c == 'u':
            if cur[i] == cur[i + 1]:
                return None
            del cur[i:i + 2]
        elif c == 'l':
            cur[i:i] = [0, 1]
        elif c == 'r':
            cur[i:i] = [1, 0]
        cuts.append(cur)
    return cuts

def kht_writhe(half, cuts):
    w = 0
    for k, (c, i) in enumerate(half):
        if c in 'xy':
            ch = -1 if c == 'x' else 1
            if cuts[k][i + 1] == cuts[k + 1][i + 1]:
                w += ch
            else:
                w -= ch
    return w

def fix_letters(word):
    half = S.parse(word)
    caps = [k for k, (c, i) in enumerate(half) if c in 'lr']
    sols = []
    for choice in itertools.product('lr', repeat=len(caps)):
        h2 = list(half)
        for k, ch in zip(caps, choice):
            h2[k] = (ch, half[k][1])
        cu = cuts_of(h2)
        if cu is not None:
            sols.append((h2, cu))
    if len(sols) != 1:
        return None
    h2, cu = sols[0]
    return 's.' + '.'.join('%s%d' % t for t in h2), kht_writhe(h2, cu)

if __name__ == '__main__':
    for w in sys.argv[1:]:
        print(w, fix_letters(w))
