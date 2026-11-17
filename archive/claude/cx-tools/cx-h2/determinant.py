#!/usr/bin/env python3
"""Step 3/4: determinant feasibility.
det K(m,n) = |V(-1)|.  Fit the signed value V(-1) to (sign pattern) x
(alpha + beta m + gamma n + eps m n), verify on all 25 grid points, then
solve |alpha + beta m + gamma n + eps m n| = 1 over Z exactly:
   eps*f = (eps m + gamma)(eps n + beta) + (eps alpha - beta gamma),
so f = s (s = +-1)  <=>  (eps m + gamma)(eps n + beta) = eps s + beta gamma - eps alpha,
a finite divisor enumeration unless the right side is 0 (lines) or eps = 0
(linear case); both degenerate cases are handled explicitly.
Cross-checks: regina Link.alexander() at -1, and the graded Euler
characteristic of knot Floer homology (Alexander polynomial) at -1.
Writes determinant.json / determinant.txt."""
import json
import sys
from fractions import Fraction
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
PKG = ('/Users/calebbarnett/Documents/Codex/2026-10-31/'
       'it-is-an-open-problem-whether-4/work/braid_classification/packages')
sys.path.insert(0, PKG)
import regina  # noqa: E402
import kbracket as kb  # noqa: E402

J = json.loads((HERE / 'jones_family.json').read_text())
PD = json.loads((HERE / 'family_pd.json').read_text())
out_lines = []


def say(*a):
    s = ' '.join(str(x) for x in a)
    print(s)
    out_lines.append(s)


# ---- signed V(-1)
S = {}
for key, rec in J['points'].items():
    m, n = rec['m'], rec['n']
    Vt = {int(e): c for e, c in rec['V_t'].items()}
    v = kb.eval_t(Vt, -1)
    assert v.denominator == 1
    S[(m, n)] = int(v)
    assert abs(S[(m, n)]) == rec['det']

# ---- bilinear fit with a sign pattern
patterns = {
    '+1': lambda m, n: 1,
    '(-1)^(m+n)': lambda m, n: (-1) ** ((m + n) % 2),
    '(-1)^m': lambda m, n: (-1) ** (m % 2),
    '(-1)^n': lambda m, n: (-1) ** (n % 2),
}
fit = None
for pname, sg in patterns.items():
    f = {k: sg(*k) * v for k, v in S.items()}
    alpha = f[(0, 0)]
    beta = f[(1, 0)] - alpha
    gamma = f[(0, 1)] - alpha
    eps = f[(1, 1)] - f[(1, 0)] - f[(0, 1)] + alpha
    good = all(f[(m, n)] == alpha + beta * m + gamma * n + eps * m * n
               for m in range(-2, 3) for n in range(-2, 3))
    say(f'sign pattern {pname:12s}: alpha={alpha} beta={beta} gamma={gamma} eps={eps} '
        f'-> bilinear on all 25 points: {good}')
    if good and fit is None:
        fit = (pname, alpha, beta, gamma, eps)
assert fit is not None, 'no bilinear fit found'
pname, alpha, beta, gamma, eps = fit
say(f'\nV(-1) = {pname} * ({alpha} + {beta} m + {gamma} n + {eps} m n)   (verified on all 25 grid points)')
say(f'det K(m,n) = |{alpha} + ({beta}) m + ({gamma}) n + ({eps}) m n|')


# ---- exact solution of |f| = 1 over Z
def divisors(N):
    N = abs(N)
    ds = set()
    d = 1
    while d * d <= N:
        if N % d == 0:
            ds.add(d)
            ds.add(N // d)
        d += 1
    return sorted(ds | {-x for x in ds})


solutions = []
lines = []
degenerate_notes = []
if eps != 0:
    for s in (+1, -1):
        C = eps * s + beta * gamma - eps * alpha
        say(f'  f = {s:+d}  <=>  ({eps} m + {gamma}) ({eps} n + {beta}) = {C}')
        if C == 0:
            # (eps m + gamma) = 0 or (eps n + beta) = 0: lines of solutions
            if gamma % eps == 0:
                lines.append(('m', -gamma // eps, s))
            if beta % eps == 0:
                lines.append(('n', -beta // eps, s))
            degenerate_notes.append(f'C=0 for s={s}')
            continue
        for u in divisors(C):
            v = C // u
            if (u - gamma) % eps == 0 and (v - beta) % eps == 0:
                m = (u - gamma) // eps
                n = (v - beta) // eps
                assert alpha + beta * m + gamma * n + eps * m * n == s
                solutions.append((m, n, s))
        # show why there are none (residue obstruction) for the record
        res_u = sorted({u % abs(eps) for u in divisors(C)})
        say(f'     divisors u of {C} have residues mod {abs(eps)}: {res_u}; need u = {gamma % abs(eps)} mod {abs(eps)}'
            f' -> {"present" if (gamma % abs(eps)) in res_u else "absent"}')
else:
    # linear: alpha + beta m + gamma n = s
    from math import gcd
    g = gcd(beta, gamma)
    for s in (+1, -1):
        rhs = s - alpha
        if beta == 0 and gamma == 0:
            if rhs == 0:
                lines.append(('all', None, s))
        elif g != 0 and rhs % g == 0:
            lines.append(('linear', (beta, gamma, rhs), s))
    degenerate_notes.append('eps = 0 (linear case)')

say(f'\nInteger solutions of |f| = 1 (isolated): {solutions if solutions else "NONE"}')
say(f'Solution lines (infinite families): {lines if lines else "NONE"}')
if degenerate_notes:
    say('Degenerate cases encountered:', degenerate_notes)
else:
    say('No degenerate case arose (eps != 0 and both right-hand sides nonzero).')

# brute-force sanity window
brute = [(m, n) for m in range(-5000, 5001) for n in range(-5000, 5001)
         if abs(alpha + beta * m + gamma * n + eps * m * n) == 1]
say(f'Brute-force window |m|,|n| <= 5000: {brute if brute else "no solutions"} (consistent with the exact enumeration)')

# n = 0 slice (one-site obstruction in the spec): det K(m,0) = |alpha + beta m|
say(f'n = 0 slice: det K(m,0) = |{alpha} + {beta} m| = {alpha} * |1 + {beta // alpha} m|'
    if beta % alpha == 0 else f'n = 0 slice: det K(m,0) = |{alpha} + {beta} m|')

# ---- mod-13 colouring gate and gcd of the grid determinants (coordinator request)
from math import gcd as _gcd
from functools import reduce
a13, b13, g13, e13 = (x % 13 for x in (alpha, beta, gamma, eps))
say(f'\nMod 13: f = {alpha} + {beta} m + {gamma} n + {eps} m n  ==  '
    f'{a13} + {b13} m + {g13} n + {e13} m n  (mod 13)')
grid_gcd = reduce(_gcd, [abs(v) for v in S.values()])
say(f'gcd of the 25 grid determinants: {grid_gcd}')
not13 = sorted((k, abs(v)) for k, v in S.items() if abs(v) % 13)
say(f'grid points with det NOT divisible by 13: {len(not13)} of 25, e.g. {not13[:6]}')
# where is f = 0 mod 13?  f = n*(g13 + e13 m) mod 13 when a13 = b13 = 0
if a13 == 0 and b13 == 0:
    inv_e = pow(e13, -1, 13) if e13 else None
    m0 = (-g13 * inv_e) % 13 if inv_e is not None else None
    say(f'Since 13 | alpha and 13 | beta, f == n * ({g13} + {e13} m) (mod 13); '
        f'13 | det K(m,n)  <=>  n == 0 (mod 13) or m == {m0} (mod 13).')
    say('The two site functionals are therefore independent mod 13 (f is not identically 0 mod 13); '
        'the mod-13 colouring gate does NOT reject the family by itself.')
else:
    say('alpha or beta nonzero mod 13: f not of the form n*(...) mod 13.')
mod13_table = {f'{m},{n}': (abs(S[(m, n)]) % 13) for m in range(-2, 3) for n in range(-2, 3)}

# ---- cross-checks against Alexander polynomial at -1
say('\nCross-check of det = |V(-1)| against |Delta(-1)|:')
xchecks = []
try:
    from knot_floer_homology import pd_to_hfk
    have_kfh = True
except Exception as e:  # pragma: no cover
    have_kfh = False
    say('  knot_floer_homology not importable here:', e)


def regina_alex_at_minus1(pd):
    L = regina.Link.fromPD([[x + 1 for x in r] for r in pd])
    P = L.alexander()          # regina PolynomialInt (ordinary polynomial)
    if hasattr(P, 'minExp'):
        rng = range(P.minExp(), P.maxExp() + 1)
    else:
        rng = range(0, P.degree() + 1)
    val = 0
    for e in rng:
        val += int(str(P[e])) * (-1) ** (e % 2)
    return abs(val), str(P)


def hfk_alex_at_minus1(pd):
    """Alexander polynomial from HFK: Delta(t) = sum_{a,mg} (-1)^mg rank t^a.
    ranks keys are (alexander, maslov)."""
    H = pd_to_hfk(pd)
    val = 0
    for (a, mg), r in H['ranks'].items():
        val += (-1) ** (mg % 2) * r * (-1) ** (a % 2)
    return abs(val), H['total_rank'], H['seifert_genus']


for (m, n) in [(0, 0), (0, 1), (1, 0), (1, 1), (-1, 2), (2, -2), (-2, -2), (2, 2)]:
    pd = PD['family'][f'{m},{n}']['pd']
    det_v = abs(S[(m, n)])
    ra, rpoly = regina_alex_at_minus1(pd)
    row = dict(m=m, n=n, det_from_V=det_v, regina_alexander_abs_at_minus1=ra,
               regina_alexander=rpoly)
    msg = f'  K({m:2d},{n:2d}): |V(-1)|={det_v:4d}  regina |Delta(-1)|={ra:4d}'
    if have_kfh and (m, n) in [(0, 0), (0, 1), (1, 1), (-1, 2)]:
        ha, tr, g = hfk_alex_at_minus1(pd)
        row.update(hfk_alexander_abs_at_minus1=ha, hfk_total_rank=tr, seifert_genus=g)
        msg += f'  HFK |Delta(-1)|={ha:4d} (total rank {tr}, genus {g})'
        assert ha == det_v
    assert ra == det_v
    say(msg)
    xchecks.append(row)
say('  all cross-checks agree.')

verdict = ('REJECTED: |det K(m,n)| = 1 has no integer solutions, so no member of the '
           'family can have trivial Jones polynomial (V=1 forces det=1).'
           if not solutions and not lines else 'det-1 members exist; see solutions')
say('\nVERDICT:', verdict)
(HERE / 'determinant.txt').write_text('\n'.join(out_lines) + '\n')
(HERE / 'determinant.json').write_text(json.dumps(dict(
    signed_V_at_minus1={f'{m},{n}': v for (m, n), v in S.items()},
    sign_pattern=pname, alpha=alpha, beta=beta, gamma=gamma, eps=eps,
    det_formula=f'|{alpha} + ({beta}) m + ({gamma}) n + ({eps}) m n|',
    solutions=solutions, lines=lines, degenerate=degenerate_notes,
    mod13=dict(alpha=a13, beta=b13, gamma=g13, eps=e13,
               det_mod_13_on_grid=mod13_table, grid_gcd=grid_gcd),
    cross_checks=xchecks, verdict=verdict), indent=1))
