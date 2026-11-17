from collections import defaultdict
from pathlib import Path
import json


def add(*ps):
    c = defaultdict(int)
    for p in ps:
        for k, v in p.items():
            c[k] += v
    return {k: v for k, v in c.items() if v}


def mul(p, q):
    c = defaultdict(int)
    for i, x in p.items():
        for j, y in q.items():
            c[i+j] += x*y
    return {k: v for k, v in c.items() if v}


def shift(p, n):
    return {k+n: v for k, v in p.items()}


def neg(p):
    return {k: -v for k, v in p.items()}


def mm(a, b):
    n = len(a)
    return [[add(*(mul(a[i][k], b[k][j]) for k in range(n)))
             for j in range(n)] for i in range(n)]


def identity(n):
    return [[{0: 1} if i == j else {} for j in range(n)] for i in range(n)]


R = {
    1: [[{-1: -1}, {1: 1}], [{}, {1: 1}]],
    -1: [[{1: -1}, {1: 1}], [{}, {-1: 1}]],
    2: [[{1: 1}, {}], [{-1: 1}, {-1: -1}]],
    -2: [[{-1: 1}, {}], [{-1: 1}, {1: -1}]],
}
assert mm(R[1], R[-1]) == identity(2)
assert mm(R[2], R[-2]) == identity(2)
assert mm(mm(R[1], R[2]), R[1]) == mm(mm(R[2], R[1]), R[2])


def word_of_tuple(tup):
    return [g * (1 if e > 0 else -1)
            for g, e in zip([1, 2, 1, 2], tup) for _ in range(abs(e))]


def trace(word):
    a = identity(2)
    for g in word:
        a = mm(a, R[g])
    return add(a[0][0], a[1][1])


def divide_by_qnumber3(p):
    extra = max(0, -min(p)-2)
    r = shift(p, extra+2)
    q = {}
    d = {4: 1, 2: 1, 0: 1}
    while r and max(r) >= 4:
        e, c = max(r)-4, r[max(r)]
        q[e] = c
        r = add(r, {i+e: -v*c for i, v in d.items()})
    assert not r, r
    result = shift(q, -extra)
    assert mul(result, {2: 1, 0: 1, -2: 1}) == p
    return result


def pretty(p):
    return ' '.join(f'{v:+d}q^{k}' for k, v in sorted(p.items(), reverse=True))


tuples = [(-5, 2, 6, 2), (-2, -1, 1, 7), (-2, -1, 3, 5),
          (-2, 2, 3, 2), (-1, 1, 2, 3), (-2, 2, 1, 4)]
results = []
for tup in tuples:
    z = trace(word_of_tuple(tup))
    numerator = add({11: 1, 7: -1, 5: -1, 3: -1, 1: -1}, neg(z))
    target = divide_by_qnumber3(numerator)
    results.append({'quotient_tuple': tup, 'quotient_word': word_of_tuple(tup),
                    'a22': z, 'a31_target': target})
    print(tup, 'a22 =', pretty(z), '; a31 target =', pretty(target))

Path(__file__).with_suffix('.json').write_text(json.dumps(results, indent=2)+'\n')
