"""Exact single-template certificate; no knot/word enumeration."""
from pathlib import Path
import json
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
data = json.loads((ROOT / 'collab/data/engineB/rho2_matrices.json').read_text())
t = sp.Symbol('t')
def poly(items):
    return sum(c*t**e for e, c in items)
def clean(mat):
    return mat.applyfunc(sp.cancel)
def equal(a, b):
    return clean(a-b) == sp.zeros(*a.shape)

M = {k: sp.Matrix([[poly(x) for x in row] for row in rows])
     for k, rows in data['M'].items()}
I = sp.eye(9)
v, w = I[:, 0], I[:, 2]
phi = sp.Matrix([[poly(x) for x in data['PHI']['u2.u2']]]) * t**2/(1+t)**4
X1, X2, X3 = (M[f'x{i}'] for i in (1, 2, 3))
inp = clean(X1*X2*v)
out = clean(phi*X1)
assert equal(inp, t**4*w)
assert equal(X1*w, X3*w)
assert equal(X1*w, t*I[:, 0]+(t**2+t**3)*I[:, 1]+t**3*w)
assert equal(X1*X3, X3*X1)
assert sp.cancel((out*w)[0]-t**4) == 0
assert sp.cancel((out*inp)[0]-t**8) == 0

def proportional(a, b):
    a, b = list(a), list(b)
    pivot = next(i for i, x in enumerate(a) if x != 0)
    return all(sp.cancel(a[pivot]*b[i]-b[pivot]*a[i]) == 0
               for i in range(len(a)))

for X in (X1, X3):
    assert not proportional(inp, X*inp)
    assert not proportional(out, out*X)
    assert not proportional(inp, X**2*inp)
    assert not proportional(out, out*X**2)

lambdas = (sp.Integer(1), -t, t**3)
colors = (0, 2, 4)
def projector(X, a):
    P = I
    for b in range(3):
        if a != b:
            P = P*(X-lambdas[b]*I)/(lambdas[a]-lambdas[b])
    return clean(P)

P, Q = ([projector(X, a) for a in range(3)] for X in (X1, X3))
coeffs = {(colors[a], colors[b]): sp.factor((out*P[a]*Q[b]*inp)[0])
          for a in range(3) for b in range(3)}
expected = {(0, 0): t**5/(t**2+t+1), (2, 2): -t**5,
            (4, 4): t**6*(t**4+t**3+t**2+t+1)/(t**2+t+1)}
for k, c in coeffs.items():
    assert sp.cancel(c-expected.get(k, 0)) == 0
assert sp.cancel(sum(coeffs.values())-t**8) == 0
F10 = sp.cancel(expected[0, 0]+t**2*expected[2, 2]+t**6*expected[4, 4])
assert sp.expand(F10) == t**14+t**11-t**9+t**8-t**7-t**6+t**5

# Connectedness: chronological x2.x1.x1 has the permutation of x2.
# Input cups12,34 become13,24. The output cup23 joins these into one arc.
pos = [0, 1, 2, 3]
for i in (2, 1, 1):
    pos = [i if x == i-1 else i-1 if x == i else x for x in pos]
top_pairs = {frozenset((pos[0], pos[1])), frozenset((pos[2], pos[3]))}
assert top_pairs == {frozenset((0, 2)), frozenset((1, 3))}
# Every inserted full twist has trivial permutation, so this holds for all m,n.

print('PASS: boundary identities, non-eigenvector tests, all sectors, connectedness.')
print('Nonzero c_ab:', expected)
print('F(m,-m)=t^8 for every integer m; preferred J=1.')
