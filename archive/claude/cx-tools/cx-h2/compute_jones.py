#!/usr/bin/env python3
"""Step 2: Jones polynomials of the 25 grid points (direct), the four corner
brackets F00, F10, F01, F11, the corner-formula evaluation at the same 25
points, the exact cross-check between the two, and a third independent
check against regina's jones().  Writes jones_family.json / .txt and
corners.json / .txt."""
import json
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
PKG = ('/Users/calebbarnett/Documents/Codex/2026-10-31/'
       'it-is-an-open-problem-whether-4/work/braid_classification/packages')
sys.path.insert(0, PKG)
import regina      # noqa: E402
import kbracket as kb  # noqa: E402

data = json.loads((HERE / 'family_pd.json').read_text())
DELTA = kb.DELTA
DELTA2 = kb.pmul(DELTA, DELTA)


def regina_jones_sqrt_t(pd):
    L = regina.Link.fromPD([[x + 1 for x in row] for row in pd])
    J = L.jones()
    out = {}
    for e in range(J.minExp(), J.maxExp() + 1):
        c = int(str(J[e]))
        if c:
            out[e] = c
    return out


# ---- corner brackets (raw reduced brackets, NOT normalised)
F = {}
for key in ('00', '10', '01', '11'):
    d = data['corners'][key]
    assert d['free_loops'] == 0
    F[key] = kb.bracket(d['pd'], reduced=True)
corner_txt = []
for key in ('00', '10', '01', '11'):
    corner_txt.append(f'F{key}(A) = {kb.pstr(F[key])}')
    print(corner_txt[-1])
(HERE / 'corners.json').write_text(json.dumps(
    {k: {str(e): c for e, c in sorted(v.items())} for k, v in F.items()}, indent=1))
(HERE / 'corners.txt').write_text(
    'Reduced Kauffman brackets (<unknot>=1, delta=-A^2-A^-2, A-smoothing of\n'
    '[a,b,c,d] joins (a,b),(c,d)) of corner(eps,eta); F{eps}{eta}.\n'
    'eps=1: first twist box (after the fixed sigma_2) replaced by e_2;\n'
    'eta=1: second twist box (after the second h) replaced by e_2.\n\n'
    + '\n'.join(corner_txt) + '\n')


def corner_formula_V_A(m, n):
    """V_K(m,n) in A from the corner formula:
    delta^2 P = XY d^2 F00 + (1-X)Y d F10 + X(1-Y) d F01 + (1-X)(1-Y) F11,
    V = (-A^3)^7 A^(-12(m+n)) P,  X = A^(8m), Y = A^(8n)."""
    X = {8 * m: 1}
    Y = {8 * n: 1}
    oneX = kb.psub(kb.ONE, X)
    oneY = kb.psub(kb.ONE, Y)
    d2P = kb.pmul(kb.pmul(X, Y), kb.pmul(DELTA2, F['00']))
    d2P = kb.padd(d2P, kb.pmul(kb.pmul(oneX, Y), kb.pmul(DELTA, F['10'])))
    d2P = kb.padd(d2P, kb.pmul(kb.pmul(X, oneY), kb.pmul(DELTA, F['01'])))
    d2P = kb.padd(d2P, kb.pmul(kb.pmul(oneX, oneY), F['11']))
    P = kb.pdivexact(d2P, DELTA2)
    # (-A^3)^7 = -A^21
    V = kb.pscale(kb.pshift(P, 21 - 12 * (m + n)), -1)
    return V, d2P


results = {}
txt = []
all_ok = True
regina_ok = True
for m in range(-2, 3):
    for n in range(-2, 3):
        d = data['family'][f'{m},{n}']
        pd = d['pd']
        w = d['writhe_spherogram']
        assert kb.pd_writhe(pd) == w
        VA = kb.jones_A(pd, w)
        Vt = kb.A_to_t(VA)
        VA_formula, d2P = corner_formula_V_A(m, n)
        match = (VA_formula == VA)
        all_ok &= match
        rj = regina_jones_sqrt_t(pd)
        ours_s = {2 * e: c for e, c in Vt.items()}
        rmatch = 'exact' if rj == ours_s else ('mirror' if rj == {-e: c for e, c in ours_s.items()} else 'FAIL')
        regina_ok &= (rmatch != 'FAIL')
        det = abs(kb.eval_t(Vt, -1))
        assert det.denominator == 1
        det = int(det)
        results[f'{m},{n}'] = dict(
            m=m, n=n, crossings=d['crossings'], writhe=w,
            V_t={str(e): c for e, c in sorted(Vt.items())},
            V_A={str(e): c for e, c in sorted(VA.items())},
            corner_formula_matches=match, regina_match=rmatch, det=det,
            V_is_one=(Vt == {0: 1}))
        line = (f'K({m:2d},{n:2d}) w={w:3d} det={det:4d}  V(t) = {kb.pstr(Vt, "t")}'
                f'   [corner formula: {"MATCH" if match else "MISMATCH"}; regina: {rmatch}]')
        txt.append(line)
        print(line)

print()
print('Corner-formula cross-check on all 25 points:', 'ALL MATCH' if all_ok else 'MISMATCH FOUND')
print('regina jones() cross-check on all 25 points:', 'ALL AGREE (up to the stated mirror relation)' if regina_ok else 'DISAGREEMENT')
mirrors = {v['regina_match'] for v in results.values()}
print('regina relation set:', mirrors)
(HERE / 'jones_family.json').write_text(json.dumps(
    dict(convention='V = (-A^3)^(-w) <D>_reduced, t = A^-4; A-smoothing of [a,b,c,d] joins (a,b),(c,d); PD counterclockwise from incoming under-strand (spherogram PD_code)',
         corner_formula_all_match=all_ok, regina_all_agree=regina_ok,
         regina_relation=sorted(mirrors), points=results), indent=1))
(HERE / 'jones_family.txt').write_text(
    'Jones polynomials V(t) of K(m,n), direct planar-contraction bracket.\n'
    'Convention: V = (-A^3)^(-w) <D>, t = A^-4, <unknot> = 1.\n\n' + '\n'.join(txt)
    + f'\n\nCorner-formula cross-check: {"ALL 25 MATCH" if all_ok else "MISMATCH"}\n'
    + f'regina jones() cross-check: {"all agree" if regina_ok else "DISAGREE"} (relation: {sorted(mirrors)})\n')
