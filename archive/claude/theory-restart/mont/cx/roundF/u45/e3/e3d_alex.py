"""E3d: targeted search in the ALEXANDER-TRIVIAL width-two class (Delta_K = 1 => a_2 = 0 automatically, all Alexander-type
necessary conditions pass).  Annealing over s.l1.l1.W.u2.u2, objective
   f = span(J) + 3 min(|a_2|,10) + 4 log2|Delta(2)| + 2 log2|Delta(-1)| - 4 [Phi_10 | J - 1].
Logs every configuration with |Delta(-1)| = |Delta(2)| = |Delta(3)| = 1 (presumed Delta = 1): span J, span V_K, zeta10 gate.
usage: e3d_alex.py N SECONDS SEED"""
import sys, random, time, json, math
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u45/e3/')   # u45: the patched e3_search (z10, INV unchanged)
import fastJ, rho2, lp, kcert
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u45/e3/')
import e3_search
import vspan, alex
assert e3_search.__file__.startswith('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u45/e3/')

# ---- u45 patch: store every J = 1 word (kcert once per distinct word, cached) ----
U45_OUT = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u45/e3/out'
J1 = {}
def KC(hw, where, ev):
    e = J1.get(hw)
    if e is None:
        st, why = kcert.certify(hw)
        e = J1[hw] = {'count': 0, 'first_eval': ev, 'where': where, 'kcert': [st, why]}
        if st != 'V=1,Delta=1':
            print('KCERT-SAYS-NONTRIVIAL', where, hw, why, flush=True)
            open(U45_OUT + '/KCERT_NONTRIVIAL_J1.txt', 'a').write(hw + '\t' + where + '\t' + str(why) + '\n')
    e['count'] += 1
    return tuple(e['kcert'])
def BUDGET_OK(evals, restarts=None):
    if MAXE is None: return True
    if evals < MAXE: return True
    return restarts is not None and restarts < MAXR
MAXE = None; MAXR = 0
EVALS = [0]
LET = fastJ.LET; INV = e3_search.INV
def ok(W):
    if any(INV[W[i]] == W[i + 1] for i in range(len(W) - 1)): return False
    return rho2.is_knot('l1.l1', W, 'u2.u2')
def lg(x): return math.log2(abs(x)) if x else 60.0
def evalf(W):
    Jn = fastJ.J('l1.l1', W, 'u2.u2')
    if Jn is None: return None
    hw = rho2.halfword('l1.l1', W, 'u2.u2')
    if Jn == {0: 1}:
        st, why = KC(hw, 'evalf', EVALS[0])
        if st != 'V=1,Delta=1':
            print('HIT-CANDIDATE', hw, why, flush=True)
            open(U45_OUT + '/HIT_CANDIDATES.txt', 'a').write(hw + '\te3d ' + str(why) + '\n')
        return None
    a2 = lp.a2(Jn); d2 = alex.alex_eval(hw, 2); dm = alex.alex_eval(hw, -1)
    z = e3_search.z10(Jn)
    f = (max(Jn) - min(Jn)) + 3 * min(abs(a2), 10) + 4 * lg(d2) + 2 * lg(dm) - 4 * z
    return f, Jn, a2, d2, dm, z, hw
def main(n, secs, seed, cap=None):
    rnd = random.Random(seed); t_end = time.time() + (cap if cap else secs); tw0 = time.time()
    found = {}; evals = 0
    while time.time() < t_end and BUDGET_OK(evals):
        while True:
            W = [rnd.choice(LET) for _ in range(n)]
            if ok(W): break
        r = evalf(W)
        if r is None: continue
        cur = r[0]; steps = 2500
        for s in range(steps):
            if time.time() > t_end or not BUDGET_OK(evals): break
            T = 5.0 * (0.05 / 5.0) ** (s / steps)
            W2 = W[:]; mv = rnd.random()
            if mv < 0.5: W2[rnd.randrange(n)] = rnd.choice(LET)
            elif mv < 0.75:
                i = rnd.randrange(n - 1); W2[i], W2[i + 1] = W2[i + 1], W2[i]
            else:
                i = rnd.randrange(n); del W2[i]; W2.insert(rnd.randrange(n), rnd.choice(LET))
            if not ok(W2): continue
            EVALS[0] = evals; r = evalf(W2); evals += 1
            if r is None: continue
            f, Jn, a2, d2, dm, z, hw = r
            if d2 == 1 and dm == 1 and alex.alex_eval(hw, 3) == 1:
                key = tuple(sorted(Jn.items()))
                if key not in found:
                    found[key] = {'word': hw, 'spanJ': max(Jn) - min(Jn), 'zeta10': z, 'a2': a2, 'J': key}
            if f <= cur or rnd.random() < math.exp(-(f - cur) / T): W, cur = W2, f
    recs = sorted(found.values(), key=lambda x: (not x['zeta10'], x['spanJ']))
    for x in recs[:30]: x['spanV'] = vspan.vspan(x['word'])
    res = {'n': n, 'evals': evals, 'alexander_trivial_distinct_J': len(found), 'best': recs[:30],
           'n_zeta10': sum(1 for x in found.values() if x['zeta10']),
           'u45': {'max_evals': MAXE, 'cap': cap, 'wall': round(time.time() - tw0, 1), 'budget_reached': not BUDGET_OK(evals), 'n_j1_distinct': len(J1), 'n_j1_probes': sum(e['count'] for e in J1.values())},
           'j1_words': J1}
    json.dump(res, open(U45_OUT + '/e3d_n%d_s%d.json' % (n, seed), 'w'))
    print('RESULT n', n, 'evals', evals, 'Delta=1 distinct J', len(found), 'with zeta10', res['n_zeta10'],
          'best (z10, spanJ, spanV)', [(x['zeta10'], x['spanJ'], x.get('spanV')) for x in recs[:8]], flush=True)
if __name__ == '__main__':
    if len(sys.argv) > 4: MAXE = int(sys.argv[4])
    main(int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), cap=(float(sys.argv[5]) if len(sys.argv) > 5 else None))
