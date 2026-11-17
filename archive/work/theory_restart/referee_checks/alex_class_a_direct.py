"""One specified cofactor, direct polynomial Bareiss (no interpolation or scan).

Reuses Claude's diagram and Alexander-matrix conventions; checks the polynomial
determinant independently of the reported integer-evaluation interpolation.
"""
import sys
sys.dont_write_bytecode = True
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')
import alex


def trim(a):
    while a and not a[-1]:
        a.pop()
    return a


def sub(a, b):
    c = a[:] + [0] * max(0, len(b) - len(a))
    for i, v in enumerate(b):
        c[i] -= v
    return trim(c)


def mul(a, b):
    if not a or not b:
        return []
    c = [0] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            c[i+j] += u*v
    return trim(c)


def div_exact(a, b):
    assert b
    a = a[:]
    out = [0] * max(0, len(a) - len(b) + 1)
    while a and len(a) >= len(b):
        k = len(a) - len(b)
        v, rem = divmod(a[-1], b[-1])
        assert rem == 0
        out[k] = v
        for j, z in enumerate(b):
            a[k+j] -= v*z
        trim(a)
    assert not a
    return trim(out)


def determinant(M):
    M = [[a[:] for a in row] for row in M]
    sign, previous = 1, [1]
    for k in range(len(M)-1):
        if not M[k][k]:
            p = next((i for i in range(k+1, len(M)) if M[i][k]), None)
            if p is None:
                return []
            M[k], M[p] = M[p], M[k]
            sign = -sign
        pivot = M[k][k]
        for i in range(k+1, len(M)):
            for j in range(k+1, len(M)):
                M[i][j] = div_exact(sub(mul(M[i][j], pivot),
                                        mul(M[i][k], M[k][j])), previous)
        previous = pivot
    return [sign*v for v in M[-1][-1]]


word = 's.r1.y0.x2.r3.y0.y2.u1.x2.x2.y0.y1.x0.u1'
crossings = alex.diagram(alex.symmetrize(alex.parse(word)))
M0, _ = alex.alex_matrix(crossings, 0)
M1, _ = alex.alex_matrix(crossings, 1)
assert len(M0) == len(M0[0]) == len(crossings)
cofactor = [[trim([M0[i][j], M1[i][j]-M0[i][j]])
             for j in range(len(M0)-1)] for i in range(len(M0)-1)]
result = determinant(cofactor)
terms = [(i, c) for i, c in enumerate(result) if c]
assert len(terms) == 1 and abs(terms[0][1]) == 1
print('word:', word)
print('crossings:', len(crossings))
print('cofactor size:', len(cofactor))
print('raw polynomial terms (degree, coefficient):', terms)
print('normalized Alexander polynomial: 1')
