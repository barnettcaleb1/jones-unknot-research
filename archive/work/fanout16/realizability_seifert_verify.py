"""Independently verify archived a_2 values from Seifert matrices, using stdlib."""
from fractions import Fraction as F
from pathlib import Path
import json

for row in json.loads(Path(__file__).with_name('realizability_seifert_audit.json').read_text()):
    V = row['seifert_matrix']
    n = len(V)
    assert n % 2 == 0
    aug = [[F(V[i][j] - V[j][i]) for j in range(n)] +
           [F(V[i][j]) for j in range(n)] for i in range(n)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if aug[i][j])
        aug[j], aug[pivot] = aug[pivot], aug[j]
        scalar = aug[j][j]
        aug[j] = [x / scalar for x in aug[j]]
        for i in range(n):
            if i != j:
                scalar = aug[i][j]
                aug[i] = [a - scalar * b for a, b in zip(aug[i], aug[j])]
    B = [r[n:] for r in aug]
    assert sum(B[i][i] for i in range(n)) == F(n, 2)
    trace_square = sum(B[i][j] * B[j][i] for i in range(n) for j in range(n))
    a2 = (F(n, 2) - trace_square) / 2
    assert a2 == row['a2']
    print(row['name'], 'a_2 =', a2)
