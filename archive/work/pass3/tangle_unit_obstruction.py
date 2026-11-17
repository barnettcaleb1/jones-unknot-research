"""Integer spin-matrix check for a nonrealizable formal TL_3 unit."""
import json
from pathlib import Path

n = 8
I = [[int(i == j) for j in range(n)] for i in range(n)]
Z = [[0] * n for _ in range(n)]
def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(n)] for i in range(n)]
def scale(c, a):
    return [[c * a[i][j] for j in range(n)] for i in range(n)]
def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
def trans(a):
    return [list(x) for x in zip(*a)]
def swap(i):
    p = [[0] * n for _ in range(n)]
    for x in range(n):
        bits = [(x >> j) & 1 for j in (2, 1, 0)]
        bits[i], bits[i + 1] = bits[i + 1], bits[i]
        y = 4 * bits[0] + 2 * bits[1] + bits[2]
        p[y][x] = 1
    return p

E1 = add(I, scale(-1, swap(0)))
E2 = add(I, scale(-1, swap(1)))
N = add(scale(2, mul(E1, E2)), scale(-1, E1))
U = add(I, N)
gram = mul(trans(U), U)
checks = {
    'E1_squared_equals_2E1': mul(E1, E1) == scale(2, E1),
    'E2_squared_equals_2E2': mul(E2, E2) == scale(2, E2),
    'E1E2E1_equals_E1': mul(mul(E1, E2), E1) == E1,
    'E2E1E2_equals_E2': mul(mul(E2, E1), E2) == E2,
    'N_squared_zero': mul(N, N) == Z,
    'U_inverse_equals_I_minus_N': mul(U, add(I, scale(-1, N))) == I,
    'U_is_unitary': gram == I,
    'column_squared_norms': [gram[i][i] for i in range(n)],
    'U_matrix': U,
}
assert all(checks[k] for k in list(checks)[:6])
assert not checks['U_is_unitary']
Path(__file__).with_suffix('.json').write_text(json.dumps(checks, indent=2))
print(json.dumps({k: v for k, v in checks.items() if k != 'U_matrix'}, indent=2))
