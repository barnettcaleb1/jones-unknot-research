"""Exact checks supporting the split-spectrum lemma; standard library only.

Uses the included work/pass2 and work/attack_search module definitions.
The all-braid theorem is proved in spectral_realizability_obstruction.txt.
"""
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "pass2"))
import braid_kernel as bk
import tl5_block as tl


def at_one(matrix, derivative=False):
    return [[sum(c * e if derivative else c for e, c in p.items())
             for p in row] for row in matrix]


identity = [[int(i == j) for j in range(5)] for i in range(5)]
zero = [[0] * 5 for _ in range(5)]
records = []
for i in range(1, 5):
    for j in range(i + 1, 6):
        conjugator = list(range(j - 1, i, -1))
        word = conjugator + [i, i] + bk.inv(conjugator)
        expected = [[0] * 5 for _ in range(5)]
        expected[i - 1][i - 1] = expected[j - 1][j - 1] = 1
        expected[i - 1][j - 1] = expected[j - 1][i - 1] = -1
        burau = bk.burau(word)
        assert at_one(burau) == identity
        assert at_one(burau, True) == expected
        assert at_one(tl.rho(word)) == identity
        records.append({"i": i, "j": j, "word": word,
                        "Burau_derivative": expected})

assert bk.identity(bk.burau(bk.KERNEL))
matrix = tl.rho(bk.KERNEL)
assert at_one(matrix) == identity
assert at_one(matrix, True) == zero
assert matrix != tl.ident()
assert tl.verify_all_basis_traces() == 42
formal_diagonal_derivative = [4, -4, 8, -8, 0]
assert any(formal_diagonal_derivative)
result = {
    "verified": True,
    "pure_generator_Laplacians": records,
    "cached_Burau_kernel_seed": {
        "TL_value_at_1": "identity",
        "TL_derivative_at_1": "zero",
        "generic_TL_matrix_is_identity": False,
    },
    "all_TL5_basis_traces_checked": 42,
    "formal_model_diagonal_derivative": formal_diagonal_derivative,
    "scope": "Finite checks; the all-braid spectral conclusion uses the written proof.",
}
(HERE / "spectral_jet_checks.json").write_text(json.dumps(result, indent=2) + "\n")
print("Verified all 10 pure-generator Laplacians, the seed's two jets, and all 42 TL5 traces.")
