"""test_forgeries.py -- audit-1 t1 + audit-2 forge.py forgeries (re-created, paths changed to run/code) plus extra
type/label forgeries, against the FIXED checker run/code/replay.py.  Every forged certificate must be REJECTED; the
controls (genuine certificates produced by run/code/certify.py) must be ACCEPTED.
usage: test_forgeries.py OUT.json"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import replay, certify, a2lib_indep as a2
assert os.path.dirname(os.path.abspath(replay.__file__)) == HERE
results = []
def T(name, cert, expect_ok=False):
    ok, msg = replay.check(cert)
    good = (ok == expect_ok)
    results.append({'name': name, 'accepted': ok, 'expected': expect_ok, 'good': good, 'msg': msg})
    print('%-64s accepted=%-5s %s | %s' % (name, ok, 'ok' if good else ('HOLE' if ok else 'UNEXPECTED_REJECT'), msg[:100]))
    return ok

UNKNOT0 = 's.l1.l1.u2.u2'
UNKNOT2 = 's.l1.x1.u2'
UNKNOT = 's.l1.l1.x2.x1.x1.x1.y3.y3.x1.u2.u2'      # Codex family m = 1
TREF = 's.l1.y0.x1.u2'                              # nontrivial (V != 1)
e = (0, 1, 2); tau = (1, 0, 2); c3 = (1, 2, 0)
gU = replay.wirtinger_presentation(UNKNOT)[0]
g2 = replay.wirtinger_presentation(UNKNOT2)[0]
gT = replay.wirtinger_presentation(TREF)[0]
# ---- audit-1 t1 (both words), with json round trip
for w, gs in ((UNKNOT2, g2), (UNKNOT, gU)):
    im = {str(g): list(e) for g in gs}; im['999'] = [1, 0, 2]; im['998'] = [0, 2, 1]
    f = {'kind': 'rep', 'halfword': w, 'group': 'S3 (forged)', 'degree': 3, 'images': im, 'noncommuting': [999, 998]}
    T('audit1-t1: identity rep + extra keys 999/998 on %s' % w, f)
    T('audit1-t1: same after json round trip', json.loads(json.dumps(f)))
    T('audit1-t1 control: pair = 2 real gens, identity images', dict(f, noncommuting=[gs[0], gs[1]]))
# ---- audit-2 forge.py rep forgeries
T('audit2: trivial rep + 2 fake noncommuting keys (unknot0)', {'kind': 'rep', 'halfword': UNKNOT0, 'degree': 3,
   'images': {'1': e, '1000': tau, '1001': c3}, 'noncommuting': [1000, 1001], 'group': 'forged'})
T('audit2: trivial rep + 2 fake keys (unknot, 14 crossings)', {'kind': 'rep', 'halfword': UNKNOT, 'degree': 3,
   'images': dict({str(g): e for g in gU}, **{'1000': tau, '1001': c3}), 'noncommuting': [1000, 1001], 'group': 'forged'})
T('audit2: abelian rep (all tau) + 1 fake key', {'kind': 'rep', 'halfword': UNKNOT, 'degree': 3,
   'images': dict({str(g): tau for g in gU}, **{'1000': (0, 2, 1)}), 'noncommuting': [1, 1000], 'group': 'forged'})
T('audit2: fake key 0 as a non-permutation', {'kind': 'rep', 'halfword': UNKNOT, 'degree': 3,
   'images': dict({str(g): tau for g in gU}, **{'0': (0, 0, 1)}), 'noncommuting': [1, 0], 'group': 'forged'})
T('audit2: negative generator id in pair', {'kind': 'rep', 'halfword': UNKNOT, 'degree': 3,
   'images': dict({str(g): tau for g in gU}, **{'-1': (0, 2, 1)}), 'noncommuting': [1, -1], 'group': 'forged'})
T('audit2: non-bijective images', {'kind': 'rep', 'halfword': UNKNOT, 'degree': 3,
   'images': {str(g): (0, 0, 1) for g in gU}, 'noncommuting': [1, 2], 'group': 'forged'})
T('audit2: float entries', {'kind': 'rep', 'halfword': UNKNOT, 'degree': 3,
   'images': {str(g): (1.0, 0.0, 2.0) for g in gU}, 'noncommuting': [1, 2], 'group': 'forged'})
T('audit2: degree mismatch', {'kind': 'rep', 'halfword': UNKNOT, 'degree': 4,
   'images': {str(g): tau for g in gU}, 'noncommuting': [1, 2], 'group': 'forged'})
T('audit2: honest abelian rep, pair inside gens', {'kind': 'rep', 'halfword': UNKNOT, 'degree': 3,
   'images': {str(g): tau for g in gU}, 'noncommuting': [1, 2], 'group': 'forged'})
# ---- new label/type forgeries
T('new: pair (g, g)', {'kind': 'rep', 'halfword': UNKNOT, 'degree': 3, 'images': {str(g): tau for g in gU}, 'noncommuting': [1, 1]})
T('new: bool in pair (True, 2)', {'kind': 'rep', 'halfword': UNKNOT, 'degree': 3, 'images': {str(g): tau for g in gU}, 'noncommuting': [True, 2]})
T('new: string pair', {'kind': 'rep', 'halfword': UNKNOT, 'degree': 3, 'images': {str(g): tau for g in gU}, 'noncommuting': ['1', '2']})
T('new: leading-zero key duplicate 01', {'kind': 'rep', 'halfword': UNKNOT, 'degree': 3,
   'images': dict({str(g): e for g in gU}, **{'01': tau}), 'noncommuting': [1, 2]})
T('new: int and str key for the same generator', {'kind': 'rep', 'halfword': UNKNOT, 'degree': 3,
   'images': {**{str(g): e for g in gU}, 1: tau}, 'noncommuting': [1, 2]})
T('new: float degree 3.0', {'kind': 'rep', 'halfword': UNKNOT, 'degree': 3.0, 'images': {str(g): tau for g in gU}, 'noncommuting': [1, 2]})
T('new: missing one generator image', {'kind': 'rep', 'halfword': UNKNOT, 'degree': 3,
   'images': {str(g): e for g in gU[1:]}, 'noncommuting': [2, 3]})
T('new: triple instead of pair', {'kind': 'rep', 'halfword': UNKNOT, 'degree': 3, 'images': {str(g): tau for g in gU}, 'noncommuting': [1, 2, 3]})
T('new: invalid halfword grammar (x-1)', {'kind': 'jones24', 'halfword': 's.l1.x-1.u2'})
T('new: unknown letter z silently dropped by alex', {'kind': 'unknot0', 'halfword': 's.l1.z1.x0.u2'})
# ---- audit-2 tietze / jones24 / unknot0 forgeries on the trefoil
G0, R0 = replay.normal_form(*replay.wirtinger_presentation(TREF))
def tz(moves): return {'kind': 'tietze', 'halfword': TREF, 'moves': moves}
j2 = next((j for j, r in enumerate(R0) if sum(1 for a in r if abs(a) == G0[0]) >= 2), 0)
T('audit2: tietze elim with g occurring twice', tz([['elim', G0[0], j2]]))
T('audit2: nielsen x == a', tz([['nielsen', G0[0], G0[0], 1, 'R']]))
T('audit2: nielsen d = 2', tz([['nielsen', G0[0], G0[1], 2, 'R']]))
T('audit2: nielsen d = 0', tz([['nielsen', G0[0], G0[1], 0, 'R']]))
T('audit2: nielsen with absent generator', tz([['nielsen', G0[0], 999, 1, 'R']]))
T('audit2: mult i == j', tz([['mult', 0, 0, 1, 0, 0]]))
T('audit2: mult e = 2', tz([['mult', 0, 1, 2, 0, 0]]))
T('audit2: mult e = 0', tz([['mult', 0, 1, 0, 0, 0]]))
T('audit2: negative index', tz([['elim', G0[0], -1]]))
T('audit2: bool index (True == 1)', tz([['mult', True, 1, 1, 0, 0]]))
T('audit2: float rotation', tz([['mult', 0, 1, 1, 0.5, 0]]))
T('audit2: unknown kind', tz([['delete', 0]]))
T('audit2: empty move list on a nontrivial knot', tz([]))
T('audit2: jones24 on a V != 1 knot', {'kind': 'jones24', 'halfword': TREF})
big = 's.l1.l1.x2.x1.' + '.'.join(['x1'] * 6) + '.' + '.'.join(['y3'] * 6) + '.x1.u2.u2'     # Codex family m = 3
nbig = len(replay.knot_crossings(big)); assert nbig > 24 and replay.VK_project(big) == {0: 1}
T('audit2: jones24 on a V = 1 diagram with %d > 24 crossings' % nbig, {'kind': 'jones24', 'halfword': big})
T('audit2: jones24 on a split link (knot + circle)', {'kind': 'jones24', 'halfword': 's.l1.x1.y0.u1'})
T('audit2: unknot0 on a knot with crossings', {'kind': 'unknot0', 'halfword': UNKNOT})
T('audit2: unknot0 on a 3-component crossing-free diagram', {'kind': 'unknot0', 'halfword': 's.l1.u1'})
# ---- transplant of a genuine unknot Tietze certificate onto the trefoil
st, info = certify.certify(UNKNOT, write_hits=False)
tcert = next(c for c in info['certificates'] if c['kind'] == 'tietze')
T('transplant: genuine 14-crossing unknot Tietze cert onto the trefoil', dict(tcert, halfword=TREF))
# ---- controls
T('CONTROL jones24 on the 14-crossing unknot', {'kind': 'jones24', 'halfword': UNKNOT}, expect_ok=True)
T('CONTROL unknot0', {'kind': 'unknot0', 'halfword': UNKNOT0}, expect_ok=True)
T('CONTROL genuine tietze cert (certify.py)', tcert, expect_ok=True)
st2, info2 = certify.certify(TREF, write_hits=False)
rcert = next(c for c in info2['certificates'] if c['kind'] == 'rep')
T('CONTROL genuine rep cert of the trefoil (certify.py)', rcert, expect_ok=True)
T('CONTROL genuine rep cert after json round trip', json.loads(json.dumps(rcert)), expect_ok=True)
holes = [r for r in results if r['accepted'] and not r['expected']]
bad_controls = [r for r in results if r['expected'] and not r['accepted']]
summ = {'tests': len(results), 'forgeries': sum(1 for r in results if not r['expected']), 'HOLES': len(holes),
        'controls': sum(1 for r in results if r['expected']), 'controls_rejected': len(bad_controls)}
print(json.dumps(summ))
json.dump({'summary': summ, 'results': results}, open(sys.argv[1], 'w'), indent=1, default=str)
