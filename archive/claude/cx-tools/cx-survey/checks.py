#!/usr/bin/env python3
"""checks.py -- (a) exact reproduction of c1_nonunit_turnback.py's anchor and corners,
(b) the Jones-unit line K(0,n) of config 4S, (c) the seam-flat-at-U-e isotopy in 4L,
(d) V_J = V(N(R(25,-9))) against B10 of config 3.   Writes checks.json."""
import sys, json
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, '/Users/calebbarnett/Documents/Codex/2026-10-31/it-is-an-open-problem-whether-4/work/global_design')
from harness import *
from survey import make_builder, det_from_V
import c1_nonunit_turnback as c1

out = {}
# (a) c1 reproduction
K = c1.candidate(0, 0)
pd_c1 = [tuple(int(x) for x in r) for r in K.PD_code()]
b3 = make_builder('seed', 'none', 'band', seed=RationalTangle(25, -9), site1='seam', site2='T')
mine = b3('I', 'I')
pd_me = [tuple(int(x) for x in r) for r in mine.PD_code()]
out['c1_K00_pd_identical'] = (pd_c1 == pd_me)
out['c1_K00_crossings'] = (len(pd_c1), len(pd_me))
rc = abs_bracket(K); rm = abs_bracket(mine)
out['c1_K00_bracket_identical'] = (rc['bracket'] == rm['bracket'])
corners_c1 = {}
for eps in (0, 1):
    for eta in (0, 1):
        Lc = c1.corner(eps, eta)
        Lm = b3('e' if eps else 'I', 'e' if eta else 'I')
        bc = abs_bracket(Lc)['bracket']; bm = abs_bracket(Lm)['bracket']
        corners_c1[f'{eps}{eta}'] = dict(c1=pstr(bc), mine=pstr(bm), identical=(bc == bm),
                                         pd_identical=([tuple(map(int, r)) for r in Lc.PD_code()] == [tuple(map(int, r)) for r in Lm.PD_code()]))
out['c1_corners'] = corners_c1
print('(a) c1 anchor PD identical:', out['c1_K00_pd_identical'], 'crossings', out['c1_K00_crossings'])
for k, v in corners_c1.items():
    print('    corner', k, 'identical bracket:', v['identical'], 'identical PD:', v['pd_identical'])

# (d) V_J and B10 = unit * delta^2 * V_J(A)
J = RationalTangle(25, -9).numerator_closure()
rJ = abs_bracket(J)
VJ = jones_from_abs(rJ['bracket'], rJ['writhe'])
out['V_J'] = jones_str(VJ); out['det_J'] = det_from_V(VJ)
# V_J as Laurent poly in A: t^(k/2) = A^(-2k)
VJ_A = {-2 * k: c for k, c in VJ.items()}
B10 = abs_bracket(b3('e', 'I'))['bracket']
q = pdiv_delta(pdiv_delta(B10))
# q should be unit * VJ_A
ratio = None
for e, c in q.items():
    pass
# find shift
e0 = min(q); e1 = min(VJ_A)
sh = e0 - e1
cand = {e + sh: c for e, c in VJ_A.items()}
if cand == q: ratio = f'A^{sh}'
elif {e: -c for e, c in cand.items()} == q: ratio = f'-A^{sh}'
out['B10_eq_unit_delta2_VJ'] = ratio
print('(d) V_J =', jones_str(VJ), 'det', det_from_V(VJ), '; B10 = u*delta^2*V_J(A^-4) with u =', ratio)

# (b) config 4S Jones-unit line K(0,n)
b4s = make_builder('none', 'seed', 'band', seed=RationalTangle(25, -9), site1='seam', site2='U')
line = {}
for n in (1, 2, -1, 3):
    r = abs_bracket(b4s(0, n))
    V = jones_from_abs(r['bracket'], r['writhe'])
    hk = check_knot_hfk(r['pd'])
    line[str(n)] = dict(crossings=r['crossings'], V_str=jones_str(V), det=det_from_V(V), check=hk)
    print(f'(b) 4S K(0,{n}): cr={r["crossings"]} V={jones_str(V)} {hk}')
out['config4S_K0n_line'] = line
# ring at the U-seed site of the fused anchor: is K u c split?
Lr = b4s('I', 'ring')
rr = abs_bracket(Lr)
Vr = jones_from_abs(rr['bracket'], rr['writhe'])
D = Diagram(rr['pd'])
L2 = Lr.copy(); L2.simplify('global')
out['config4S_U_ring'] = dict(components=rr['components'], V_str=jones_str(Vr), linking=str(dict(D.linking_matrix())),
                              simplified_crossings=len(L2.crossings), simplified_free=int(L2.unlinked_unknot_components),
                              geometry=link_geometry(Lr))
print('(b) K(0,0) u c_U:', out['config4S_U_ring'])
# same test for the T-seed site in the fused anchor (config 3) and the seam site
b3T = make_builder('seed', 'none', 'band', seed=RationalTangle(25, -9), site1='seam', site2='T')
for nm, args in (('T_ring', ('I', 'ring')), ('seam_ring', ('ring', 'I'))):
    Lr = b3T(*args); rr = abs_bracket(Lr); D = Diagram(rr['pd'])
    L2 = Lr.copy(); L2.simplify('global')
    out[f'config3_{nm}'] = dict(components=rr['components'], linking=str(dict(D.linking_matrix())),
                                simplified_crossings=len(L2.crossings), simplified_free=int(L2.unlinked_unknot_components),
                                geometry=link_geometry(Lr))
    print(f'(b) anchor u c_{nm}:', out[f'config3_{nm}'])

# (c) config 4L: seam site with U-lit turned back: are the seam-twisted diagrams the same knot?
b4l = make_builder('none', 'lit', 'band', seed=RationalTangle(25, -9), site1='seam', site2='U')
iso = {}
for m in (0, 1, 2, -1):
    r = abs_bracket(b4l(m, 'e'))
    V = jones_from_abs(r['bracket'], r['writhe'])
    hk = check_knot_hfk(r['pd']) if r['components'] == 1 else {'note': 'not a knot'}
    iso[str(m)] = dict(components=r['components'], crossings=r['crossings'], V_str=jones_str(V), check=hk)
    print(f'(c) 4L seam={m}, U-lit=e: comps={r["components"]} V={jones_str(V)} {hk}')
out['config4L_seam_twist_with_Ue'] = iso
(HERE / 'checks.json').write_text(json.dumps(out, indent=1, default=str))
