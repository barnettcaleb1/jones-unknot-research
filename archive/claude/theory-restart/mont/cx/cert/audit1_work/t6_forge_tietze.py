"""AUDIT-1 test 6: targeted attempts to make replay.check accept a Tietze / jones24 / unknot0 certificate for a
NONTRIVIAL knot (python type tricks, degenerate moves, transplanted moves, malformed fields)."""
import sys, json, random, itertools
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert')
import replay, certify

def find_word(pred, gen):
    for w in gen:
        if replay.knot_crossings(w) and pred(w): return w

NT = 's.l1.x0.x0.x0.u2'      # candidate; replaced below by the first small V != 1 knot found
rnd = random.Random(3)
cands = ['s.l1.' + '.'.join(rnd.choice(['x0', 'y0', 'x1', 'y1']) for _ in range(rnd.randint(1, 4))) + '.u2' for _ in range(400)]
nontriv = [w for w in dict.fromkeys(cands) if replay.knot_crossings(w) and replay.VK_project(w) not in (None, {0: 1})]
NT = nontriv[0]
print('nontrivial test knot', NT, 'crossings', len(replay.knot_crossings(NT)), 'V', replay.VK_project(NT))
st, cert = certify.certify(NT, write_hits=False)
print('certify ->', st, [c['kind'] for c in cert['certificates']])
gens, rels = replay.wirtinger_presentation(NT)
G0, R0 = replay.normal_form(gens, rels)
print('checker presentation', G0, R0)

attempts = []
attempts.append(('empty moves', {'kind': 'tietze', 'halfword': NT, 'moves': []}))
attempts.append(('moves=string', {'kind': 'tietze', 'halfword': NT, 'moves': 'elim'}))
attempts.append(('moves=None', {'kind': 'tietze', 'halfword': NT, 'moves': None}))
attempts.append(('kind case', {'kind': 'Tietze', 'halfword': NT, 'moves': []}))
attempts.append(('unknot0 on nontrivial', {'kind': 'unknot0', 'halfword': NT}))
attempts.append(('jones24 on nontrivial', {'kind': 'jones24', 'halfword': NT}))
attempts.append(('halfword missing', {'kind': 'tietze', 'moves': []}))
# exhaustive search over SHORT sequences of syntactically plausible moves incl. type tricks
vals = [0, 1, 2, 3, -1, True, False, 1.0, 2.0, -0.0, None, '1', [1]]
acc = []
tried = 0
def all_moves(G, R):
    out = []
    for g in list(G) + [True, 1.0, -1, 0]:
        for j in list(range(len(R))) + [-1, True, 1.0, len(R)]:
            out.append(('elim', g, j))
    for i in list(range(len(R))) + [True, -1]:
        for j in list(range(len(R))) + [True, -1]:
            for e in (1, -1, True, 1.0, 0, 2):
                out.append(('mult', i, j, e, 0, 0))
    for x in list(G) + [True]:
        for a in list(G) + [True]:
            for d in (1, -1, True, 2, 0):
                for side in ('R', 'L', 'X'):
                    out.append(('nielsen', x, a, d, side))
    return out
level = [[]]
for depth in range(3):
    nxt = []
    for seq in level:
        try:
            res, msg = replay.replay_moves(gens, rels, [tuple(m) for m in seq]) if seq else (replay.normal_form(gens, rels), 'ok')
        except Exception:
            res = None
        if res is None: continue
        G, R = res
        for mv in all_moves(G, R):
            s2 = seq + [list(mv)]
            tried += 1
            ok, msg = replay.check({'kind': 'tietze', 'halfword': NT, 'moves': s2})
            if ok: acc.append(s2)
            try:
                r2, m2 = replay.replay_moves(gens, rels, [tuple(m) for m in s2])
            except Exception:
                r2 = None
            if r2 is not None and depth < 2 and rnd.random() < 0.02: nxt.append(s2)
    level = nxt
print('exhaustive/sampled short sequences tried:', tried, ' ACCEPTED:', len(acc), acc[:3])
for name, c in attempts:
    print('%-28s' % name, replay.check(c))
# transplant: Tietze certificates of unknots with the same crossing number
uk = []
for w in dict.fromkeys('s.l1.' + '.'.join(rnd.choice(['x0', 'y0', 'x1', 'y1', 'x2', 'y2']) for _ in range(rnd.randint(1, 6))) + '.u2' for _ in range(4000)):
    cr = replay.knot_crossings(w)
    if cr and len(cr) == len(gens) and replay.VK_project(w) == {0: 1}:
        st2, c2 = certify.certify(w, write_hits=False)
        for cc in c2['certificates']:
            if cc['kind'] == 'tietze': uk.append(cc)
nacc = 0
for cc in uk:
    t = dict(cc); t['halfword'] = NT
    nacc += replay.check(t)[0]
print('transplanted unknot certificates (same crossing number):', len(uk), ' accepted on the nontrivial knot:', nacc)
