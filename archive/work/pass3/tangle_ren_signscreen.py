"""All 4096 crossing-sign choices on Ren's fixed annular projection."""
import contextlib, io, runpy, json
from pathlib import Path
with contextlib.redirect_stdout(io.StringIO()):
    data = runpy.run_path(str(Path(__file__).with_name('tangle_ren_check.py')))
features = data['state_features']
N = len(features)
crossings = data['self_crossings']
add, mul, shift = data['add'], data['mul'], data['shift']
DELTA, ONE = data['DELTA'], data['ONE']

def fwht(a, prime):
    a = a.copy()
    step = 1
    while step < len(a):
        for offset in range(0, len(a), 2 * step):
            for j in range(offset, offset + step):
                x, y = a[j], a[j + step]
                a[j] = (x + y) % prime
                a[j + step] = (x - y) % prime
        step *= 2
    return a

def screen(prime, A):
    delta = (-A * A - pow(A, -2, prime)) % prime
    G = [pow(A, 12 - 2 * s.bit_count(), prime) for s in range(N)]
    GH = fwht(G, prime)
    valid = set(range(N))
    for degree in (2, 4):
        F = [pow(delta, c, prime) if e == degree else 0 for c, e in features]
        FH = fwht(F, prime)
        result = fwht([x*y % prime for x,y in zip(FH,GH)], prime)
        valid &= {i for i, value in enumerate(result) if value == 0}
    return valid

screen1 = screen(1000000007, 2)
screen2 = screen(1000000009, 3)
candidates = sorted(screen1 & screen2)
delta_powers = [ONE]
for _ in range(max(c for c, e in features)):
    delta_powers.append(mul(delta_powers[-1], DELTA))
pd_checks = []
for mask in (1, 1375, 4095):
    annular = {0:{},2:{},4:{}}
    for state, (c,e) in enumerate(features):
        annular[e] = add(annular[e], shift(delta_powers[c],12-2*(state^mask).bit_count()))
    pd = [list(row) for row in data['PD']]
    for i,c in enumerate(crossings):
        if (mask >> i) & 1:
            j = int(c.label)
            pd[j] = pd[j][1:] + pd[j][:1]
    actual = data['Link'](pd)
    actualK = actual.sublink(0)
    ordinary = {}
    for degree, coefficient in annular.items():
        ordinary = add(ordinary, mul(coefficient, delta_powers[degree]))
    expected = shift(mul(DELTA,data['jones_A'](actualK)),3*actualK.writhe(),(-1)**actualK.writhe())
    assert ordinary == expected, ('ordinary',mask)
    a4,a2,a0 = annular[4],annular[2],annular[0]
    S2 = add(delta_powers[2],{0:-1})
    S4 = add(add(delta_powers[4],shift(delta_powers[2],0,-3)),ONE)
    colored2 = add(a2,shift(a4,0,3))
    colored0 = add(add(a0,a2),shift(a4,0,2))
    hopf = add(add(mul(mul(a4,S4),{10:-1,-10:-1}),
                   mul(mul(colored2,S2),{6:-1,-6:-1})),mul(colored0,DELTA))
    expectedHopf = shift(mul(DELTA,data['jones_A'](actual)),3*actual.writhe(),(-1)**actual.writhe())
    assert hopf == expectedHopf, ('Hopf',mask)
    pd_checks.append({'mask':mask,'ordinary_Jones_check':True,'Hopf_axis_check':True})
rows = []
for mask in candidates:
    annular = {0:{},2:{},4:{}}
    for state, (c,e) in enumerate(features):
        term = shift(delta_powers[c], 12 - 2*(state ^ mask).bit_count())
        annular[e] = add(annular[e], term)
    if annular[2] or annular[4]:
        continue
    w = data['K'].writhe() - 2*sum(c.sign for i,c in enumerate(crossings) if (mask >> i) & 1)
    expected = shift(DELTA, 3*w, (-1)**w)
    assert annular[0] == expected, (mask, annular, w)
    pd = [list(row) for row in data['PD']]
    changed = [int(c.label) for i,c in enumerate(crossings) if (mask >> i) & 1]
    for i in changed:
        pd[i] = pd[i][1:] + pd[i][:1]
    L = data['Link'](pd)
    L.simplify('global')
    row = {
        'mask': mask,
        'changed_PD_crossings_zero_based': changed,
        'annular_bracket_degree': 0,
        'annular_bracket_constant': annular[0],
        'Jones_K': '1',
        'final_link_with_axis_crossings': len(L.crossings),
        'final_link_with_axis_components': len(L.link_components) + L.unlinked_unknot_components,
    }
    rows.append(row)
out = {
    'projection': 'Ren arXiv:2609.11084v2, published PD',
    'sign_choices': N,
    'screen1_survivors': len(screen1),
    'screen2_survivors': len(screen2),
    'joint_screen_survivors': len(candidates),
    'exact_degree_zero_choices': len(rows),
    'not_simplified_to_unlink': sum(r['final_link_with_axis_crossings'] != 0 for r in rows),
    'independent_changed_PD_checks': pd_checks,
    'rows': rows,
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2))
print(json.dumps({k:v for k,v in out.items() if k != 'rows'}, indent=2))
