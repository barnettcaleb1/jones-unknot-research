"""Step 1b: push Codex's fixed template (V = x2.x1, U = x1) through engineB's template_screen pipeline EXACTLY
(verbatim copy in orig/, only output paths changed) and trace every decision for this junction."""
import sys, random, time
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/orig')
import template_screen as TS, mitm, rho2, sectors, fastJ
P = mitm.P
SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 1
D1, D2 = 5, 5
rnd = random.Random(SEED)
t = rnd.randrange(2, P - 1); u = t * t % P
S = sectors.setup(t, P)
Binv, Bm, blocks = S['Binv'], S['B'], S['blocks']
MT, VT, PHIT = rho2.normalised()
Ms = [{L: [[mitm.evt(x, t) for x in row] for row in m] for L, m in MT.items()}]
V = [[mitm.evt(x, t) for x in VT['l1.l1']]]
c = t * t % P * pow(pow(1 + t, 4, P), P - 2, P) % P
PH = [[mitm.evt(x, t) * c % P for x in PHIT['u2.u2']]]
tops = mitm.bfs(Ms, V, D1, 'top'); bots = mitm.bfs(Ms, PH, D2, 'bot')
print('tops', len(tops), 'bots', len(bots))
# locate the classes of x2.x1 (top) and x1 (bottom)
vt = V[0]
for L in ['x2', 'x1']: vt = mitm.mv(Ms[0][L], vt)
wb = mitm.vm(PH[0], Ms[0]['x1'])
rep_t = [w for w, vecs in tops if mitm.proj(vecs[0]) == mitm.proj(vt)]
rep_b = [w for w, vecs in bots if mitm.proj(vecs[0]) == mitm.proj(wb)]
print('top representative(s) of [rho(x2.x1) f0]:', rep_t, '  bottom representative(s) of [phi rho(x1)]:', rep_b)
wt = rep_t[0]; wbw = rep_b[0]
tc = mitm.top_class(wt); bc = mitm.bot_class(wbw)
print('top_class', tc, 'bot_class', bc, 'knot_ok', mitm.knot_ok(tc, bc))
be = [sum(Binv[i][j] * dict(tops)[wt][0][j] for j in range(9)) % P for i in range(9)]
om = [sum(dict(bots)[wbw][0][i] * Bm[i][j] for i in range(9)) % P for j in range(9)]
bl = [blocks[s] for s in TS.SECT]
cs = [sum(om[k] * be[k] for k in b) % P for b in bl]
nz = frozenset(TS.SECT[i] for i in range(7) if cs[i])
print('nonzero sectors nz =', sorted(nz), ' |NZ| =', len(nz))
print('per-direction possible(nz, d):')
for d in TS.DIRS:
    print('   ', d, 'groups', [[s for s in g if s in nz] for g in TS.GROUPS[d] if any(s in nz for s in g)], '->', repr(TS.possible(nz, d)))
dl = [d for d in TS.DIRS if TS.possible(nz, d) is True]
print('engineB direction list dl (possible(...) is True):', dl, ' -> junction', 'SKIPPED (if not dl: continue)' if not dl else 'kept')
# what the offset loop WOULD do on (1,-1) if the direction were admitted
d = (1, -1)
upow = {k: pow(u, k % (P - 1), P) for k in range(-160, 161)}
cd = dict(zip(TS.SECT, cs))
gs = [[s for s in g if s in nz] for g in TS.GROUPS[d]]; gs = [g for g in gs if g]
found = []
for (m0, n0) in TS.OFFS[d]:
    vals = [sum(cd[s] * upow[TS.E[s[0]] * m0 + TS.E[s[1]] * n0] for s in g) % P for g in gs]
    if sum(1 for x in vals if x) <= 1:
        W = (list(wt) + (['x1', 'x1'] * m0 if m0 > 0 else ['y1', 'y1'] * (-m0)) + (['x3', 'x3'] * n0 if n0 > 0 else ['y3', 'y3'] * (-n0)) + list(wbw))
        Jn = fastJ.J('l1.l1', W, 'u2.u2')
        if Jn is not None and len(Jn) == 1: found.append(((m0, n0), m0 + n0, '.'.join(W), Jn))
print('if admitted, (1,-1) offsets passing the single-group test: %d of %d; unit-valued: %d' % (len(TS.OFFS[d]), len(TS.OFFS[d]), len(found)))
for f in found: print('   unit line through', f[0], 'offset m+n =', f[1], 'word', f[2], 'J =', f[3])
