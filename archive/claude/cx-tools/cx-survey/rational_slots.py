#!/usr/bin/env python3
"""rational_slots.py -- the holder's RATIONAL-SLOT corners C.

The ENTIRE T slot and the ENTIRE U slot of the shell are replaced by the two
basis tangles, everything else (fusion crossing / seam band, h blocks, framing)
fixed.  Labels: '0' = ZeroTangle() = the horizontal 0 tangle as inserted in
the slot BEFORE the shell's rotate(1)  (so rot(0) is the vertical identity:
the cable runs straight through); 'inf' = InfinityTangle() = the vertical
1/0 tangle before rotation (rot(inf) = horizontal turnback in the cable).
C_ab: a = T slot, b = U slot.  Brackets are REDUCED (<O> = 1), same outside
framing, no per-diagram normalisation.  Equations tested on the reduced
brackets (they are homogeneous):
  (E1) C_0inf = C_inf0 =: r
  (E2) C_00 = delta (delta^2 - 3)^2 r - F C_infinf,  F = (delta^2-2)(delta^2-4)
Target (unfused Hopf shell corners divided by delta):
  C = [[delta^6 - 7 delta^4 + 15 delta^2 - 8, delta], [delta, 1]].
Writes rational_slots.json / rational_slots.md.
"""
import sys, json
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from harness import *
from spherogram.links.tangles import InfinityTangle

ONE = {0: 1}
def dpow(k):
    return ppow(DELTA, k)
def poly_in_delta(coeffs):
    """coeffs: {power of delta: int} -> Laurent poly in A"""
    out = {}
    for k, c in coeffs.items():
        out = padd(out, pscale(dpow(k), c))
    return out
TARGET_OVER_DELTA = {
    '00': poly_in_delta({6: 1, 4: -7, 2: 15, 0: -8}),
    '0inf': dict(DELTA), 'inf0': dict(DELTA), 'infinf': dict(ONE)}
TARGET_REDUCED = {k: pmul(v, DELTA) for k, v in TARGET_OVER_DELTA.items()}
D2m3sq = pmul(padd(DELTA2, {0: -3}), padd(DELTA2, {0: -3}))
F = pmul(padd(DELTA2, {0: -2}), padd(DELTA2, {0: -4}))

def basis(label):
    return ZeroTangle() if label == '0' else InfinityTangle()

FUSIONS = {
    'unfused': dict(seam=None, top=None, bottom=None),
    'seam_sigma2 (H2; configs 2L,2S)': dict(seam='sigma2', top=None, bottom=None),
    'seam_sigma2inv (config 5c)': dict(seam='sigma2inv', top=None, bottom=None),
    'top_sigma2 (configs 5a,5aL)': dict(seam=None, top='sigma2', bottom=None),
    'bottom_sigma2 (configs 5b,5bL)': dict(seam=None, top=None, bottom='sigma2'),
    'seam_band (c1 anchor; configs 3,3b,4L,4S,6)': dict(seam='band', top=None, bottom=None),
}

def build(fusion, a, b):
    A = IdentityBraid(2) | basis(a).rotate(1)
    B = basis(b).rotate(1) | IdentityBraid(2)
    f = FUSIONS[fusion]
    seam = None
    if f['seam'] == 'sigma2': seam = sigma2(1)
    elif f['seam'] == 'sigma2inv': seam = sigma2(-1)
    elif f['seam'] == 'band': seam = seam_band('I')
    top = sigma2(1) if f['top'] else None
    bot = sigma2(1) if f['bottom'] else None
    return assemble(A, B, top=top, seam=seam, bottom=bot).braid_closure()

def unit_ratio(p, q):
    """p = u*q for a unit u = +-A^k ?  return str(u) or None"""
    p = pclean(p); q = pclean(q)
    if not p or not q or len(p) != len(q): return None
    sh = min(p) - min(q)
    if {e + sh: c for e, c in q.items()} == p: return f'A^{sh}'
    if {e + sh: -c for e, c in q.items()} == p: return f'-A^{sh}'
    return None

results = {}
lines = ['# Rational-slot corners C (holder\'s second addition)', '',
         "Labels: '0' = ZeroTangle inserted in the slot before the shell's rotate(1) (cable straight through); 'inf' = InfinityTangle (cable turned back).",
         'C_ab: a = T slot, b = U slot.  REDUCED brackets (<O>=1), same outside framing.  Equations tested on the reduced brackets.',
         'delta = -A^2 - A^-2, F = (delta^2-2)(delta^2-4).  Target/delta = [[d^6-7d^4+15d^2-8, d],[d, 1]], component pattern (3,2,2,1) = actual components minus one.', '']
for fusion in FUSIONS:
    C = {}; info = {}
    for a in ('0', 'inf'):
        for b in ('0', 'inf'):
            L = build(fusion, a, b)
            r = abs_bracket(L)
            red = pdiv_delta(r['bracket'])
            key = a + b
            C[key] = red
            info[key] = dict(components=r['components'], crossings=r['crossings'], writhe=r['writhe'],
                             free_loops=r['free_loops'], reduced=pstr(red))
            q = divisible_by(red, 1)
            info[key]['over_delta'] = pstr(q) if q is not None else 'not divisible by delta'
            info[key]['vs_target_over_delta'] = ('exact' if (q is not None and q == TARGET_OVER_DELTA[key]) else
                                                 (f'unit {unit_ratio(q, TARGET_OVER_DELTA[key])} times target' if (q is not None and unit_ratio(q, TARGET_OVER_DELTA[key])) else 'different'))
    E1 = padd(C['0inf'], pneg(C['inf0']))
    r_ = C['0inf']
    E2 = padd(padd(C['00'], pneg(pmul(pmul(DELTA, D2m3sq), r_))), pmul(F, C['infinf']))
    res = dict(corners=info, E1_defect=(pstr(E1) if E1 else '0'), E1_holds=(not E1),
               E2_defect=(pstr(E2) if E2 else '0'), E2_holds=(not E2),
               E2_defect_with_r_inf0=(pstr(padd(padd(C['00'], pneg(pmul(pmul(DELTA, D2m3sq), C['inf0']))), pmul(F, C['infinf']))) ))
    results[fusion] = res
    lines.append(f'## {fusion}')
    lines.append('')
    lines.append('| C_ab | comps | cr | writhe | reduced bracket | /delta | vs target |')
    lines.append('|---|---|---|---|---|---|---|')
    for key in ('00', '0inf', 'inf0', 'infinf'):
        i = info[key]
        lines.append(f'| C_{key} | {i["components"]} | {i["crossings"]} | {i["writhe"]} | {i["reduced"]} | {i["over_delta"]} | {i["vs_target_over_delta"]} |')
    lines.append('')
    lines.append(f'(E1) C_0inf - C_inf0 = {res["E1_defect"]}  -> {"HOLDS" if res["E1_holds"] else "FAILS"}')
    lines.append(f'(E2) C_00 - delta (delta^2-3)^2 r + F C_infinf  (r = C_0inf) = {res["E2_defect"]}  -> {"HOLDS" if res["E2_holds"] else "FAILS"}')
    if res['E2_defect'] != res['E2_defect_with_r_inf0']:
        lines.append(f'     (with r = C_inf0 instead: {res["E2_defect_with_r_inf0"]})')
    lines.append('')
    print(fusion)
    for key in ('00', '0inf', 'inf0', 'infinf'):
        i = info[key]; print(f'  C_{key:6s} comps={i["components"]} cr={i["crossings"]} w={i["writhe"]:3d} reduced={i["reduced"]}  /delta={i["over_delta"]}  [{i["vs_target_over_delta"]}]')
    print('  E1 defect:', res['E1_defect'], '| E2 defect:', res['E2_defect'])
(HERE / 'rational_slots.json').write_text(json.dumps(results, indent=1))
(HERE / 'rational_slots.md').write_text('\n'.join(lines) + '\n')
