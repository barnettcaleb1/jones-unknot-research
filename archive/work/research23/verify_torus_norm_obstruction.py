"""Check the stated consequence of Schutz Thm 5.3, not its proof.

This checks the 20 archived examples against the published block formula.
The all-k identity follows by the telescoping argument in global_homology.txt.
Standard library only; run alongside torus_norm_obstruction_checks.json.
"""
from collections import Counter
import json
from pathlib import Path


def polynomial(k):
    out = Counter({(0, 6 * k): 1})
    for m in range(k):
        h, q = 4 * m + 2, 6 * (k + m) + 4
        out[h, q] += 1
        out[h + 1, q + 2] += 1
    for m in range(1, k + 1):
        h, q = 4 * m, 6 * (k + m)
        out[h, q] += 1
        out[h + 1, q + 4] += 1
    return out


rows = json.loads(Path(__file__).with_name(
    "torus_norm_obstruction_checks.json").read_text())
assert [row["k"] for row in rows] == list(range(1, 21))
for row in rows:
    k = row["k"]
    p = polynomial(k)
    euler = Counter()
    for (h, q), rank in p.items():
        euler[q] += (-1 if h % 2 else 1) * rank
    euler = {q: c for q, c in euler.items() if c}
    expected = {6 * k: 1, 6 * k + 4: 1, 12 * k + 4: -1}
    assert euler == expected
    assert sum(p.values()) == row["reduced_Q_rank"] == 4 * k + 1
    assert {str(q): c for q, c in euler.items()} == row["Jones_q_exponents"]
    determinant = abs(sum(c * (-1 if (q // 2) % 2 else 1)
                          for q, c in euler.items()))
    assert determinant == row["determinant"] == (3 if k % 2 else 1)
    assert sorted(abs(c) for c in euler.values()) == [1, 1, 1]
print("Verified 20 torus-family rank, Euler, coefficient-norm and determinant records.")
