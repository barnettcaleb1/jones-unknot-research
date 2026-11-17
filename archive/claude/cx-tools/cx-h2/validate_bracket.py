#!/usr/bin/env python3
"""Validate kbracket.py on trefoil, figure-eight, 5_1 and the Hopf link,
built in spherogram (so the SAME PD/sign conventions are exercised as for
the family), and against regina's independent jones() implementation.
Also demonstrates that the opposite A/B-smoothing choice fails the trefoil
check (non-integral powers of t), which is how the convention was fixed."""
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
PKG = ('/Users/calebbarnett/Documents/Codex/2026-10-31/'
       'it-is-an-open-problem-whether-4/work/braid_classification/packages')
sys.path.insert(0, PKG)
import spherogram  # noqa: E402
import regina      # noqa: E402
import kbracket as kb  # noqa: E402


def regina_jones_sqrt_t(pd):
    """regina's jones() as dict {exponent of t^(1/2): coeff}."""
    L = regina.Link.fromPD([[x + 1 for x in row] for row in pd])
    J = L.jones()
    out = {}
    for e in range(J.minExp(), J.maxExp() + 1):
        c = int(str(J[e]))
        if c:
            out[e] = c
    return out, L.writhe(), L.countComponents()


def mirror_t(p):
    return {-e: c for e, c in p.items()}


def fmt(p, var='t'):
    return kb.pstr(p, var)


def check(name, braid, expected_t, is_knot=True):
    L = spherogram.Link(braid_closure=braid)
    pd = [tuple(int(x) for x in r) for r in L.PD_code()]
    w = L.writhe()
    assert kb.pd_writhe(pd) == w, (name, kb.pd_writhe(pd), w)
    VA = kb.jones_A(pd, w)
    if is_knot:
        V = kb.A_to_t(VA)
        Vs = {2 * e: c for e, c in V.items()}
    else:
        Vs = kb.A_to_sqrt_t(VA)
        V = Vs
    exp_s = {2 * e: c for e, c in expected_t.items()} if is_knot else expected_t
    match = 'exact' if Vs == exp_s else ('mirror' if Vs == mirror_t(exp_s) else 'FAIL')
    rj, rw, rc = regina_jones_sqrt_t(pd)
    rmatch = 'exact' if Vs == rj else ('mirror' if Vs == mirror_t(rj) else 'FAIL')
    var = 't' if is_knot else 's'
    print(f'{name}: writhe {w} (regina writhe {rw}, components {rc})')
    print(f'   ours      : {fmt(V, var)}')
    print(f'   expected  : {fmt(expected_t, var)}   -> {match}')
    print(f'   regina    : {fmt(rj, "s")}   -> {rmatch} (s = t^(1/2))')
    assert match != 'FAIL' and rmatch != 'FAIL', name
    assert rw == w
    return match, rmatch


def wrong_convention_trefoil():
    """Swap the A/B smoothings (equivalently A -> A^-1 in the bracket but not
    in the writhe normalisation) and show the trefoil check fails."""
    L = spherogram.Link(braid_closure=[1, 1, 1])
    pd = [tuple(int(x) for x in r) for r in L.PD_code()]
    w = L.writhe()
    br = kb.bracket(pd)
    br_wrong = {-e: c for e, c in br.items()}
    V_wrong = kb.pscale(kb.pshift(br_wrong, -3 * w), (-1) ** (w % 2))
    try:
        kb.A_to_t(V_wrong)
        print('WRONG convention unexpectedly gave a polynomial in t:', kb.pstr(V_wrong))
        return False
    except ValueError as e:
        print('Opposite smoothing convention on the trefoil: V =', kb.pstr(V_wrong),
              '->', e, '(rejected, as expected)')
        return True


if __name__ == '__main__':
    results = {}
    results['trefoil'] = check('trefoil 3_1 (braid s1^3)', [1, 1, 1],
                               {1: 1, 3: 1, 4: -1})
    results['figure8'] = check('figure-eight 4_1 (braid s1 s2^-1 s1 s2^-1)',
                               [1, -2, 1, -2], {-2: 1, -1: -1, 0: 1, 1: -1, 2: 1})
    results['5_1'] = check('5_1 (braid s1^5)', [1] * 5,
                           {2: 1, 4: 1, 5: -1, 6: 1, 7: -1})
    results['hopf'] = check('Hopf link (braid s1^2)', [1, 1],
                            {1: -1, 5: -1}, is_knot=False)
    ok_wrong = wrong_convention_trefoil()
    print()
    print('Summary:', results, '| wrong-convention rejected:', ok_wrong)
    allok = all(a != 'FAIL' and b != 'FAIL' for a, b in results.values()) and ok_wrong
    print('VALIDATION', 'PASSED' if allok else 'FAILED')
