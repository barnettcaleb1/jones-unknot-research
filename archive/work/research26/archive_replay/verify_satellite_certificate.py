"""Small exact checks supplementing the handwritten all-d proof; stdlib only."""
from itertools import permutations


def add(p, q):
    r = dict(p)
    for a, b in q.items():
        r[a] = r.get(a, 0) + b
        if not r[a]:
            del r[a]
    return r


def mul(p, q):
    r = {}
    for a, b in p.items():
        for c, d in q.items():
            e = tuple(x+y for x, y in zip(a, c))
            r[e] = r.get(e, 0) + b*d
    return {a: b for a, b in r.items() if b}


def scale(p, n):
    return {a: b*n for a, b in p.items() if b*n}


def mono(d, i, r, n=1):
    a = [0]*d
    a[i] = r
    return {tuple(a): n}


for d in range(1, 5):
    one = {(0,)*d: 1}
    matrix = [[add(mono(d, i, r), scale(one, -1))
               for i in range(d)] for r in range(1, d+1)]
    det = {}
    for p in permutations(range(d)):
        inversions = sum(p[i] > p[j] for i in range(d) for j in range(i+1, d))
        term = one
        for i in range(d):
            term = mul(term, matrix[i][p[i]])
        det = add(det, scale(term, (-1)**inversions))
    target = one
    for i in range(d):
        target = mul(target, add(mono(d, i, 1), scale(one, -1)))
    for i in range(d):
        for j in range(i+1, d):
            target = mul(target, add(mono(d, j, 1), mono(d, i, 1, -1)))
    assert det == target
print('Symbolic determinant identities verified for d=1,...,4.')

f = {0: {}}
for r in range(1, 9):
    f[r] = add(mul(mono(1, 0, 1), f[r-1]), mono(1, 0, -1-3*(r-1), (-1)**(r-1)))
    f[-r] = add(mul(mono(1, 0, -1), f[-r+1]), mono(1, 0, 1+3*(r-1), (-1)**(r-1)))
    assert f[r] == {(r-2-4*j,): (-1)**j for j in range(r)}
    assert f[-r] == {(2-r+4*j,): (-1)**j for j in range(r)}
print('Signed lasso product factors verified for r=±1,...,±8.')

# Use y=q^(1/2), so all exponents below are integers.
for j in range(1, 13):
    numerator = {}
    for a in range(j+1):
        shift = 3*(a*(a+1)-j*(j+2))
        numerator = add(numerator, {(shift+k,): (-1)**(j-a)
                                   for k in range(-2*a, 2*a+1, 2)})
    denominator_minimum = -j
    assert min(a[0] for a in numerator)-denominator_minimum == -(3*j*j+5*j)
print('Trefoil numerator/denominator valuations verified through color j+1=13.')
