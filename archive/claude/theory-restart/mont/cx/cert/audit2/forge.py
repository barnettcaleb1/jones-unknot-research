"""forge.py -- AUDIT-2: forged / corrupted certificates against the independent checker replay.check.
Every forged certificate below is INVALID; any acceptance is a checker hole."""
import sys, json, random
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/audit2')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert')
import a2lib, gen, replay
results = []
def T(name, cert, expect_ok=False):
    ok, msg = replay.check(cert)
    results.append((name, ok, msg))
    flag = 'HOLE' if (ok and not expect_ok) else ('ok' if ok == expect_ok else 'UNEXPECTED_REJECT')
    print('%-58s accepted=%-5s %s | %s' % (name, ok, flag, msg[:110]))
    return ok

UNKNOT0 = 's.l1.l1.u2.u2'                                  # crossing-free unknot
UNKNOT = 's.l1.l1.x2.x1.x1.x1.y3.y3.x1.u2.u2'             # Codex family m = 1 (unknot, V = 1)
TREF = None
# a small nontrivial knot
rng = random.Random(3)
while TREF is None:
    hw = gen.rand_halfword(rng, 8, maxhw=3)
    full = a2lib.full_of(hw); D = a2lib.morse_diagram(full)
    if D and D['n'] >= 3 and not a2lib.jones_unit_test(a2lib.bracket_full(full)): TREF = hw
print('nontrivial test knot:', TREF)
gU = a2lib.wirtinger_from_halfword(UNKNOT)[0]
gT = a2lib.wirtinger_from_halfword(TREF)[0]
d = 3; e = (0, 1, 2); tau = (1, 0, 2); c3 = (1, 2, 0)
# ---- rep forgeries
T('rep: trivial rep + 2 fake noncommuting keys (unknot0)', {'kind': 'rep', 'halfword': UNKNOT0, 'degree': 3,
   'images': {'1': e, '1000': tau, '1001': c3}, 'noncommuting': [1000, 1001], 'group': 'forged'})
T('rep: trivial rep + 2 fake keys (unknot, 13 crossings)', {'kind': 'rep', 'halfword': UNKNOT, 'degree': 3,
   'images': dict({str(g): e for g in gU}, **{'1000': tau, '1001': c3}), 'noncommuting': [1000, 1001], 'group': 'forged'})
T('rep: abelian rep (all tau) + 1 fake key (unknot)', {'kind': 'rep', 'halfword': UNKNOT, 'degree': 3,
   'images': dict({str(g): tau for g in gU}, **{'1000': (0, 2, 1)}), 'noncommuting': [1, 1000], 'group': 'forged'})
T('rep: fake key given as a non-permutation (unknot)', {'kind': 'rep', 'halfword': UNKNOT, 'degree': 3,
   'images': dict({str(g): tau for g in gU}, **{'0': (0, 0, 1)}), 'noncommuting': [1, 0], 'group': 'forged'})
T('rep: negative generator id in pair (unknot)', {'kind': 'rep', 'halfword': UNKNOT, 'degree': 3,
   'images': dict({str(g): tau for g in gU}, **{'-1': (0, 2, 1)}), 'noncommuting': [1, -1], 'group': 'forged'})
T('rep: non-bijective image of a generator', {'kind': 'rep', 'halfword': UNKNOT, 'degree': 3,
   'images': {str(g): (0, 0, 1) for g in gU}, 'noncommuting': [1, 2], 'group': 'forged'})
T('rep: float entries', {'kind': 'rep', 'halfword': UNKNOT, 'degree': 3,
   'images': {str(g): (1.0, 0.0, 2.0) for g in gU}, 'noncommuting': [1, 2], 'group': 'forged'})
T('rep: degree mismatch', {'kind': 'rep', 'halfword': UNKNOT, 'degree': 4,
   'images': {str(g): tau for g in gU}, 'noncommuting': [1, 2], 'group': 'forged'})
T('rep: honest abelian rep, pair inside gens (unknot)', {'kind': 'rep', 'halfword': UNKNOT, 'degree': 3,
   'images': {str(g): tau for g in gU}, 'noncommuting': [1, 2], 'group': 'forged'})
# ---- tietze forgeries (start presentation of the nontrivial knot)
G0, R0 = replay.normal_form(*a2lib.wirtinger_from_halfword(TREF))
def tz(moves): return {'kind': 'tietze', 'halfword': TREF, 'moves': moves}
j2 = next(j for j, r in enumerate(R0) if sum(1 for a in r if abs(a) == G0[0]) >= 2) if any(sum(1 for a in r if abs(a) == G0[0]) >= 2 for r in R0) else 0
T('tietze: elim with g occurring twice', tz([['elim', G0[0], j2]]))
T('tietze: nielsen x == a', tz([['nielsen', G0[0], G0[0], 1, 'R']]))
T('tietze: nielsen d = 2', tz([['nielsen', G0[0], G0[1], 2, 'R']]))
T('tietze: nielsen d = 0', tz([['nielsen', G0[0], G0[1], 0, 'R']]))
T('tietze: nielsen with absent generator', tz([['nielsen', G0[0], 999, 1, 'R']]))
T('tietze: mult i == j', tz([['mult', 0, 0, 1, 0, 0]]))
T('tietze: mult e = 2', tz([['mult', 0, 1, 2, 0, 0]]))
T('tietze: mult e = 0', tz([['mult', 0, 1, 0, 0, 0]]))
T('tietze: negative index', tz([['elim', G0[0], -1]]))
T('tietze: bool index (True == 1)', tz([['mult', True, 1, 1, 0, 0]]))
T('tietze: float rotation', tz([['mult', 0, 1, 1, 0.5, 0]]))
T('tietze: unknown kind', tz([['delete', 0]]))
T('tietze: empty move list on a nontrivial knot', tz([]))
# ---- jones24 / unknot0 forgeries
T('jones24 on a V != 1 knot', {'kind': 'jones24', 'halfword': TREF})
big = 's.l1.l1.x2.x1.x1.x1.x1.x1.y3.y3.y3.y3.x1.u2.u2'      # Codex family m = 2: 4+2*... crossings
nb = a2lib.morse_diagram(a2lib.full_of(big))['n']
T('jones24 on a V = 1 diagram with %d crossings' % nb, {'kind': 'jones24', 'halfword': big})
T('jones24 on a split link (knot + circle)', {'kind': 'jones24', 'halfword': 's.l1.x1.y0.u1'})
T('unknot0 on a knot with crossings', {'kind': 'unknot0', 'halfword': UNKNOT})
T('unknot0 on a 3-component crossing-free diagram', {'kind': 'unknot0', 'halfword': 's.l1.u1'})
# ---- controls that must be accepted
T('CONTROL jones24 on the 13-crossing unknot', {'kind': 'jones24', 'halfword': UNKNOT}, expect_ok=True)
T('CONTROL unknot0', {'kind': 'unknot0', 'halfword': UNKNOT0}, expect_ok=True)
json.dump(results, open('forge_results.json', 'w'), default=str)
print('HOLES:', sum(1 for n, ok, m in results if ok and not n.startswith('CONTROL')))
