#!/usr/bin/env python3
"""Exact audit of the claimed length-independent residual Jones degree cap.

Standard library only. Laurent polynomials and polynomials in p are dicts
{exponent: integer coefficient}; no floating point arithmetic is used.

Conventions are those of Carmi--Cohen 2606.22410v1:
  x^-2 V(+) - x^2 V(-) = (x-x^-1) V(0), p=x-x^-1.

Take the trefoil V_1=x^2+x^6-x^8, in its three-crossing twist-knot
diagram (the same seed picture as the paper's twist1.png). Replace the
singleton anti-parallel twist crossing by L positive crossings, L odd.
Changing one crossing in that block cancels two crossings by RII, while
oriented smoothing of one crossing removes the others by RI. Consequently
  x^-2 V_L - x^2 V_{L-2} = p H,
where H is the fixed oriented smoothing of the original seed crossing.
The changed original seed crossing is the unknot, so
  H=(x^-2 V_1-x^2)/p=-x-x^5.

External first-value checks (variable q=x^2):
  Garoufalidis--Zagier, SIGMA 20 (2024), 055, pp.74 and 79,
  https://doi.org/10.3842/SIGMA.2024.055
  trefoil: q+q^3-q^4;
  5_2: q-q^2+2q^3-q^4+q^5-q^6.

This audits a consequence of the paper's Section 5 package; it does not
claim that Jones unknot detection is false. At least one claimed geometric
compression/identification premise must fail.
"""


def clean(a):
    return {e: c for e, c in a.items() if c}


def add(*polys):
    out = {}
    for a in polys:
        for e, c in a.items():
            out[e] = out.get(e, 0) + c
    return clean(out)


def scale(a, c):
    return clean({e: c * v for e, v in a.items()})


def shift(a, n):
    return {e + n: c for e, c in a.items()}


def mul(a, b):
    out = {}
    for e, c in a.items():
        for f, d in b.items():
            out[e + f] = out.get(e + f, 0) + c * d
    return clean(out)


def format_poly(a, var="x"):
    pieces = []
    for e in sorted(a, reverse=True):
        c = a[e]
        term = str(abs(c)) if e == 0 or abs(c) != 1 else ""
        if e:
            term += var if e == 1 else f"{var}^{e}"
        sign = "-" if c < 0 else "+"
        if not pieces:
            pieces.append(("-" if c < 0 else "") + term)
        else:
            pieces.append(f" {sign} {term}")
    return "".join(pieces) or "0"


def x_power_in_jvp(n):
    """Return (A(p),B(p)) with x^n=A+B*x, x^2=p*x+1."""
    a, b = {0: 1}, {}
    if n >= 0:
        for _ in range(n):
            # x(A+B*x)=B+(A+p*B)*x.
            a, b = b, add(a, shift(b, 1))
    else:
        for _ in range(-n):
            # x^-1(A+B*x)=(B-p*A)+A*x.
            a, b = add(b, scale(shift(a, 1), -1)), a
    return a, b


def jvp(v):
    a, b = {}, {}
    for n, c in v.items():
        aa, bb = x_power_in_jvp(n)
        a, b = add(a, scale(aa, c)), add(b, scale(bb, c))
    return a, b


def p_power_as_laurent(n):
    out = {0: 1}
    for _ in range(n):
        out = mul(out, {1: 1, -1: -1})
    return out


def reconstruct(a, b):
    """Independent evaluation p=x-x^-1 reconstructs Laurent V."""
    out = {}
    for q, c in a.items():
        out = add(out, scale(p_power_as_laurent(q), c))
    for q, c in b.items():
        out = add(out, scale(shift(p_power_as_laurent(q), 1), c))
    return out


def twist_polynomials(max_l):
    assert max_l >= 1 and max_l % 2 == 1
    trefoil = {2: 1, 6: 1, 8: -1}
    h = {1: -1, 5: -1}
    p = {1: 1, -1: -1}
    # Derive/check H from the seed skein with V_-=1.
    assert add(shift(trefoil, -2), {2: -1}) == mul(p, h)
    out = {1: trefoil}
    for length in range(3, max_l + 1, 2):
        out[length] = add(shift(out[length - 2], 4), shift(mul(p, h), 2))
        # Check the oriented skein directly in Laurent form.
        assert add(shift(out[length], -2), scale(shift(out[length - 2], 2), -1)) == mul(p, h)
    return out


def main():
    values = twist_polynomials(23)
    published_5_2 = {2: 1, 4: -1, 6: 2, 8: -1, 10: 1, 12: -1}
    assert values[3] == published_5_2
    expected_trefoil_a = {0: 1, 2: -3, 4: -4, 6: -1}
    expected_trefoil_b = {3: -6, 5: -5, 7: -1}
    assert jvp(values[1]) == (expected_trefoil_a, expected_trefoil_b)
    for length, value in values.items():
        a, b = jvp(value)
        assert reconstruct(a, b) == value
        assert max(value) == 2 * length + 6
        assert value[max(value)] == -1
        degree = max(set(a) | set(b))
        assert degree == 2 * length + 5
        assert b[degree] == -1
        assert sum(value.values()) == 1  # V(1)=1.
        if length in (1, 3, 5, 23):
            print(f"L={length}: max x-exponent={max(value)}; p-degree={degree}; b_{degree}={b[degree]}")
            if length <= 5:
                print("  " + format_poly(value))
    host_cap = 3 * 3
    effective_threshold = host_cap + 11
    residual_cap = effective_threshold + 2
    length = 23
    a, b = jvp(values[length])
    assert length > residual_cap
    assert b[51] == -1 and 51 > residual_cap
    print(f"Claimed residual cap = 3*3+11+2 = {residual_cap}")
    print("Contradictory residual coefficient at L=23: b_51 = -1")
    print("All exact-arithmetic and reconstruction checks passed.")


if __name__ == "__main__":
    main()
