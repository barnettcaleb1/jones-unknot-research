#!/usr/bin/env python3
"""Determinant of the knot K_w of a two-letter half-diagram, two ways:
 (a) Kauffman bracket of the full symmetric diagram (general planar-matching code) at A = exp(i pi/4);
 (b) 2x2 integer matrices: det K_w = |(1 0) D(L_m)...D(L_1) (1 0)^T|, D(Y^e) = [[1,0],[-e,1]], D(X^e) = [[1,-2e],[0,1]].
Validates (b) against (a) on all words of length <= 7; (b) is then used in the big enumeration."""
import itertools
from reflib import *
INV = {'Y': 'y0', 'y': 'x0', 'X': 'x1', 'x': 'y1'}
def det_mat(word):
    a, b = 1, 0
    for L in word:
        if L == 'Y': b = b - a
        elif L == 'y': b = b + a
        elif L == 'X': a = a - 2 * b
        else: a = a + 2 * b
    return abs(a)
def det_diag(word):
    letters = [('l', 1)] + [(INV[L][0], int(INV[L][1])) for L in word] + [('u', 2)]
    return det_from_bracket(knot_bracket(letters))
if __name__ == '__main__':
    bad = 0; n = 0
    for L in range(0, 8):
        for w in itertools.product('XYxy', repeat=L):
            w = ''.join(w); n += 1
            if det_mat(w) != det_diag(w):
                bad += 1
                if bad < 10: print('MISMATCH', w, det_mat(w), det_diag(w))
    print('words checked', n, 'mismatches', bad)
    for w in ['YX', 'YYx', 'YYX', 'yyx', 'YXYX', 'YYYYX', 'YxYx']:
        print(w, det_mat(w))
