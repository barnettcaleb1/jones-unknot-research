#!/usr/bin/env python3
"""Exact ribbon-double fusion-variance check; Python standard library only.

Run: python3 work/research23/verify_fusion_variance.py
Optional: --output path.json

Conventions: H_N is zero-framed, dimension-N colored Jones, H_N(U)=1.
Choose trefoil chirality H_2=q^-1+q^-3-q^-4. With [n] the quantum integer,
H_3=(q^-12-[3]q^-9+[5]q^-3)/[3]. This is the N=3, (2,3)-torus
specialization of the zero-framed formula in H. R. Morton, "The coloured
Jones function and Alexander polynomial for torus knots", Math. Proc.
Camb. Phil. Soc.117 (1995), 129-135, Section 3, printed p.132; use s=q^1/2,
divide the zero-framed invariant by [N]. Equivalently it is the j=2 case
of H_(j+1)(T(2,3))=[j+1]^-1 sum_(a=0)^j (-1)^(j-a)[2a+1]
q^(3(a(a+1)-j(j+2))/2).
Source: https://www.liverpool.ac.uk/~su14/papers/colouredjones.pdf

All calculations below occur in Q(s), s^2=-3, q=(1+s)/2. No floating point
is used. The real number [2]=sqrt(3) is outside this field, but its square
[2]^2=3 suffices for the variance. The two uses of the letter s above are
separate conventions: Morton s=q^1/2; the code's field generator is S.
"""

import argparse
from fractions import Fraction as F
import json
from pathlib import Path


def z(a=0, b=0):
    return (F(a), F(b))


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def neg(x):
    return (-x[0], -x[1])


def mul(x, y):
    return (x[0]*y[0] - 3*x[1]*y[1], x[0]*y[1] + x[1]*y[0])


def bar(x):
    return (x[0], -x[1])


def inv(x):
    norm = x[0]**2 + 3*x[1]**2
    assert norm != 0
    return (x[0]/norm, -x[1]/norm)


def power(x, n):
    if n < 0:
        return power(inv(x), -n)
    result = z(1)
    while n:
        if n & 1:
            result = mul(result, x)
        x = mul(x, x)
        n //= 2
    return result


def rational(x):
    assert x[1] == 0 and x[0].denominator == 1
    return int(x[0])


def encoded(x):
    return {"1": str(x[0]), "sqrt(-3)": str(x[1])}


def verify():
    q = z(F(1, 2), F(1, 2))
    assert power(q, 6) == z(1) and power(q, 3) == z(-1)
    assert inv(q) == bar(q)
    d3 = add(add(q, z(1)), inv(q))
    d5 = add(add(d3, power(q, 2)), power(q, -2))
    d2_squared = add(z(1), d3)
    h2 = add(add(power(q, -1), power(q, -3)), neg(power(q, -4)))
    h3_numerator = add(add(power(q, -12), neg(mul(d3, power(q, -9)))),
                       mul(d5, power(q, -3)))
    h3 = mul(h3_numerator, inv(d3))
    assert h2 == z(0, -1) and h3 == z(1)
    r2, r3 = mul(h2, bar(h2)), mul(h3, bar(h3))
    assert r2 == z(3) and r3 == z(1)
    # x=chi_2, x^2=chi_1+chi_3; phi(chi_N)=[N] H_N(R).
    phi_x2 = add(z(1), mul(d3, r3))
    phi_x_squared = mul(d2_squared, mul(r2, r2))
    variance = add(phi_x2, neg(phi_x_squared))
    assert phi_x2 == z(3) and phi_x_squared == z(27)
    assert variance == z(-24)
    return {
        "verified": True,
        "field": "Q(sqrt(-3))",
        "r": 6,
        "SU2_level": 4,
        "q": encoded(q),
        "trefoil_H2": encoded(h2),
        "trefoil_H3": encoded(h3),
        "ribbon_double_H2": rational(r2),
        "ribbon_double_H3": rational(r3),
        "quantum_dimension_2_squared": rational(d2_squared),
        "quantum_dimension_3": rational(d3),
        "quantum_dimension_5": rational(d5),
        "phi_x": "3*sqrt(3)",
        "phi_x_squared": rational(phi_x_squared),
        "phi_x2": rational(phi_x2),
        "variance": rational(variance),
        "conclusion": "The actual annular closure functional is not positive.",
        "scope": "Ribbon trefoil double; not a Jones-one knot or a contradiction to TQFT unitarity.",
        "H3_source": "Morton (1995), Section 3, printed p.132; zero framing, divided by [3].",
        "source_url": "https://www.liverpool.ac.uk/~su14/papers/colouredjones.pdf",
        "conditional_scaffold": "AJ remains an unproved hypothesis; all-colored detection is not assumed known."
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = verify()
    output = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.write_text(output)
    print(output, end="")
