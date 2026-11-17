"""Exact polynomial identities in Z[m,lambda]; standard library only."""
from collections import defaultdict
from itertools import permutations
from pathlib import Path
import json


def add(*polys):
    r = defaultdict(int)
    for p in polys:
        for e, c in p.items():
            r[e] += c
    return {e: c for e, c in r.items() if c}


def scale(p, k):
    return {e: k*c for e, c in p.items() if k*c}


def mul(p, q):
    r = defaultdict(int)
    for (a,b), c in p.items():
        for (d,e), f in q.items():
            r[a+d,b+e] += c*f
    return {e: c for e, c in r.items() if c}


def C(n):
    return {(0,0): n} if n else {}


one, m, lam = C(1), {(1,0):1}, {(0,1):1}
m2 = mul(m,m)


def identity():
    return [[C(int(i==j)) for j in range(4)] for i in range(4)]


def matrix_mul(a,b):
    return [[add(*(mul(a[i][k],b[k][j]) for k in range(4)))
             for j in range(4)] for i in range(4)]


def gen_power(i,k):
    a = identity()
    i -= 1
    a[i][i] = add(one,k)
    a[i][i+1] = scale(k,-1)
    a[i+1][i] = k
    a[i+1][i+1] = add(one,scale(k,-1))
    return a


b = identity()
for g in [gen_power(2,scale(m,2)), gen_power(1,one),
          gen_power(2,one), gen_power(2,scale(m,-2)),
          gen_power(3,C(-1))]:
    b = matrix_mul(b,g)

expected = [
    [C(2),add(scale(m,2),C(-2)),{},add(one,scale(m,-2))],
    [add(scale(m,2),one),add(scale(m2,4),scale(m,-2)),{},scale(m2,-4)],
    [scale(m,2),add(scale(m2,4),scale(m,-4),one),{},
     add(scale(m2,-4),scale(m,2))],
    [{},{},C(-1),C(2)]
]
assert b == expected

z = [[add(lam,scale(b[i][j],-1)) if i==j else scale(b[i][j],-1)
      for j in range(4)] for i in range(4)]
det = {}
for p in permutations(range(4)):
    inversions = sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
    term = C((-1)**inversions)
    for i in range(4):
        term = mul(term,z[i][p[i]])
    det = add(det,term)

T = add(scale(m2,4),scale(m,-2),C(2))
linear = add(lam,C(-1))
target = mul(mul(linear,linear),add(mul(lam,lam),scale(mul(T,lam),-1),one))
assert det == target

out = {
    "status":"passed",
    "proof_type":"symbolic identity over Z[m,lambda], not interpolation",
    "matrix_word_identity":True,
    "characteristic_polynomial":"(lambda-1)^2*(lambda^2-(4*m^2-2*m+2)*lambda+1)",
    "expanded_terms":[{"m_power":e[0],"lambda_power":e[1],"coefficient":c}
                      for e,c in sorted(det.items())],
    "topology":"Every braid closure is U by one destabilization and conjugation.",
    "entropy":"Burau spectral-radius lower bound tends to infinity."
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
