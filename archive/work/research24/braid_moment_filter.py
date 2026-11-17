"""All-integer conjugated-anchor obstruction, not a bounded word scan.

For the cached Bigelow B5 Burau-kernel K and C=sigma1...sigma4,
test the four all-power moments with C_h=sigma_i^-h C sigma_i^h.
The generator's two eigenvalues imply each moment is a*x+b+c/x,
x=(-A^-4)^h. A constant gcd of their cleared quadratics at one exact
finite-field specialization rules out every integer h generically.
"""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / 'pass3'))
from braid_conjugates import bk, tl, P, I, GEN, mm, evaluate, rho, traceprod


def clean(f):
    while f and f[-1] == 0:
        f.pop()
    return f


def plus(f, g):
    return clean([((f[i] if i < len(f) else 0) +
                   (g[i] if i < len(g) else 0)) % P
                  for i in range(max(len(f), len(g)))])


def times(f, g):
    out = [0] * (len(f) + len(g) - 1)
    for i, a in enumerate(f):
        for j, b in enumerate(g):
            out[i+j] = (out[i+j] + a*b) % P
    return clean(out)


def remainder(f, g):
    f = f[:]
    while len(f) >= len(g) and f:
        a = f[-1] * pow(g[-1], -1, P) % P
        offset = len(f) - len(g)
        for i, b in enumerate(g):
            f[offset+i] = (f[offset+i] - a*b) % P
        clean(f)
    return f


def gcd(f, g):
    while g:
        f, g = g, remainder(f, g)
    return [(a * pow(f[-1], -1, P)) % P for a in f] if f else []


def interpolate(points):
    result = []
    for i, (x, y) in enumerate(points):
        numerator, denominator = [1], 1
        for j, (z, _) in enumerate(points):
            if i != j:
                numerator = times(numerator, [-z % P, 1])
                denominator = denominator * (x-z) % P
        scalar = y * pow(denominator, -1, P) % P
        result = plus(result, [a*scalar % P for a in numerator])
    return result


def value(f, x):
    return sum(a*pow(x, i, P) for i, a in enumerate(f)) % P


def mpower(m, exponent):
    out = I
    for _ in range(exponent):
        out = mm(out, m)
    return out


def run():
    assert bk.identity(bk.burau(bk.KERNEL))
    assert bk.permutation(bk.KERNEL) == list(range(5))
    assert sum(1 if s > 0 else -1 for s in bk.KERNEL) == 0
    M, C = evaluate(tl.rho(bk.KERNEL)), rho(bk.ANCHOR)
    powers = [mpower(M, j) for j in range(5)]
    fixed = [traceprod(C, m) for m in powers]
    assert fixed[0] == 0 and fixed[1] != 0
    r = -pow(2, -4, P) % P
    xs = [1, r, pow(r, -1, P)]
    assert len(set(xs)) == 3
    cases = []
    for i in range(1, 5):
        G, Gi = GEN[i], GEN[-i]
        assert mm(G, Gi) == I
        shifted = lambda a: tuple(tuple((G[k][l] - a*I[k][l]) % P
                                        for l in range(5)) for k in range(5))
        assert mm(shifted(2), shifted(-pow(2, -3, P))) == ((0,)*5,)*5
        anchors = [C, mm(mm(Gi, C), G), mm(mm(G, C), Gi)]
        polynomials = []
        for m in powers[1:]:
            f = interpolate([(x, x*traceprod(a, m) % P)
                             for x, a in zip(xs, anchors)])
            for h in (-2, 2):
                left, right = (Gi, G) if h > 0 else (G, Gi)
                anchor = mm(mm(mpower(left, 2), C), mpower(right, 2))
                x = pow(r, h, P)
                assert value(f, x) == x*traceprod(anchor, m) % P
            polynomials.append(f)
        common = []
        for f in polynomials:
            common = gcd(common, f)
        assert common == [1], (i, common)
        cases.append(dict(generator=i, cleared_moment_polynomials=polynomials,
                          common_gcd=common, all_integer_h_excluded=True))
    result = dict(modulus=P, A=2, eigenvalue_ratio=r,
                  seed='work/pass2/braid_kernel.py:KERNEL',
                  fixed_anchor_moments_m0_through_m4=fixed, cases=cases,
                  conclusion='For no integer h and no i=1,2,3,4 do ALL power closures K^m sigma_i^-h C sigma_i^h have Jones 1.',
                  limitation='Does not exclude isolated m, arbitrary conjugators, or other Burau-kernel braids.')
    (ROOT / 'braid_moment_filter.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    run()
