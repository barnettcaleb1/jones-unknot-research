"""Compare fusion formula to Morton's independent torus formula, exactly.

Source: Garoufalidis, The Jones slopes of a knot, equation (26).
Use u=q^(1/2), reflect q to match the chirality in our notes, and
clear the quantum-dimension denominator. All arithmetic is integral.
"""
from collections import defaultdict
from pathlib import Path
import json


def clean(p):
    return {e: c for e, c in p.items() if c}


def fusion_cleared(j, m):
    p = defaultdict(int)
    for a in range(j + 1):
        lam = (2*m + 1) * (a*(a + 1) - j*(j + 2))
        sign = (-1)**(j - a)
        for e in range(-2*a, 2*a + 1, 2):
            p[lam + e + 1] += sign
            p[lam + e - 1] -= sign
    return clean(p)


def morton_mirror_cleared(j, m):
    a, b = 2, 2*m + 1
    p = defaultdict(int)
    for twice_k in range(-j, j + 1, 2):
        base = a*b*(twice_k**2 - j*(j + 2)) // 2
        # The reflected denominator contributes an overall minus sign.
        p[base - (a-b)*twice_k - 1] -= 1
        p[base - (a+b)*twice_k + 1] += 1
    return clean(p)


checks = []
for j in range(13):
    for m in range(-4, 9):
        assert fusion_cleared(j, m) == morton_mirror_cleared(j, m)
        checks.append([j, m])
result = {
    "source": "Garoufalidis, The Jones slopes of a knot, equation (26)",
    "url": "https://guests.mpim-bonn.mpg.de/stavros/publications/printed/the_jones_slopes_of_a_knot.pdf",
    "exact_independent_formula_checks": len(checks),
    "label_and_twist_pairs": checks,
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
print(f'PASS: {len(checks)} exact comparisons with independent Morton formula.')
