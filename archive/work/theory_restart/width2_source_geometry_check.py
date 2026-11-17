"""Independent fixed-input checks: matrices -> sectors, and local unknot determinant.

No word or parameter enumeration. Run in the existing research Python environment.
"""
from pathlib import Path
import json
import sys
import sympy as s

ROOT = Path(__file__).resolve().parents[2]
data = json.loads((ROOT / 'collab/data/engineB/rho2_matrices.json').read_text())
rows = json.loads((ROOT / 'collab/data/engineB/exact_sectors.json').read_text())
t = s.symbols('t')
polynomial = lambda terms: sum(c*t**e for e, c in terms)
expand = lambda matrix: matrix.applyfunc(s.expand)
M = {key: s.Matrix([[polynomial(p) for p in row] for row in a])
     for key, a in data['M'].items()}
identity = s.eye(9)
v = identity[:, 0]
phi_numerator = s.Matrix([[polynomial(p) for p in data['PHI']['u2.u2']]])
eigenvalues = (s.Integer(1), -t, t**3)
colors = (0, 2, 4)
projector_numerators, projector_denominators = {}, {}
for site in (1, 3):
    for a in range(3):
        b, c = [j for j in range(3) if j != a]
        projector_numerators[site, a] = expand(
            (M[f'x{site}']-eigenvalues[b]*identity)
            *(M[f'x{site}']-eigenvalues[c]*identity))
        projector_denominators[a] = s.expand(
            (eigenvalues[a]-eigenvalues[b])*(eigenvalues[a]-eigenvalues[c]))

for row in rows:
    av = v
    for letter in row['V'].split('.'):
        av = expand(M[letter]*av)
    bv = phi_numerator
    for letter in reversed(row['U'].split('.')):
        bv = expand(bv*M[letter])
    for a in range(3):
        left = expand(bv*projector_numerators[1, a])
        for b in range(3):
            right = expand(projector_numerators[3, b]*av)
            numerator = s.expand(t**2*(left*right)[0])
            denominator = s.expand((1+t)**4
                *projector_denominators[a]*projector_denominators[b])
            saved = s.cancel(s.sympify(
                row['c'].get(f'{colors[a]}{colors[b]}', '0'), locals={'t': t}))
            sn, sd = s.fraction(saved)
            assert s.expand(numerator*sd-denominator*sn) == 0
    print('PASS all nine sectors from source matrices:', row['V'], '|', row['U'])

sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')
import alex
local_four_plat = [('l', 2), ('y', 1), ('y', 1), ('y', 2), ('y', 2),
                   ('x', 0), ('u', 1), ('u', 0)]
crossings = alex.diagram(local_four_plat)
assert crossings is not None and len(crossings) == 5
matrix, _ = alex.alex_matrix(crossings, -1)
minor = s.Matrix(matrix)[:-1, :-1]
assert minor == s.Matrix([[2, -1, -1, 0], [-1, 0, 2, -1],
                          [-2, 1, 0, 1], [1, -2, 0, 0]])
assert minor.det() == -1
print('PASS: local two-bridge knot has determinant1; numerator +/-1 gives unknot.')
