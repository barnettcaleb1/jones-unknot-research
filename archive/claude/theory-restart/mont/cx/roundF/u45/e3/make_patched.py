"""Build the patched E3 drivers in roundF/u45/e3/ from engineB's originals by exact string replacement (originals untouched).
Patches (and ONLY these): (1) outputs go to roundF/u45/e3/out; (2) budget = the ORIGINAL run's evaluation count (and restart
count where logged) with the same seed, plus a wall-clock cap; (3) EVERY J = 1 word met (inner-loop probes AND initial random
words, which the originals skipped silently) is STORED with count / first eval index / kcert verdict (kcert run once per
distinct word; the walk itself is unchanged: J = 1 probes are still rejected exactly as before)."""
import re, sys
SRC = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB/'
DST = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u45/e3/'
OUT = DST + 'out'
KC = '''
# ---- u45 patch: store every J = 1 word (kcert once per distinct word, cached) ----
U45_OUT = %r
J1 = {}
def KC(hw, where, ev):
    e = J1.get(hw)
    if e is None:
        st, why = kcert.certify(hw)
        e = J1[hw] = {'count': 0, 'first_eval': ev, 'where': where, 'kcert': [st, why]}
        if st != 'V=1,Delta=1':
            print('KCERT-SAYS-NONTRIVIAL', where, hw, why, flush=True)
            open(U45_OUT + '/KCERT_NONTRIVIAL_J1.txt', 'a').write(hw + '\\t' + where + '\\t' + str(why) + '\\n')
    e['count'] += 1
    return tuple(e['kcert'])
def BUDGET_OK(evals, restarts=None):
    if MAXE is None: return True
    if evals < MAXE: return True
    return restarts is not None and restarts < MAXR
MAXE = None; MAXR = 0
''' % OUT
def sub(s, a, b, count=1):
    assert s.count(a) == count, (a, s.count(a))
    return s.replace(a, b)

# ---------------- e3_search.py ----------------
s = open(SRC + 'e3_search.py').read()
s = sub(s, "import fastJ, rho2, lp, kcert, vspan\n", "import fastJ, rho2, lp, kcert, vspan\n" + KC)
s = sub(s, "def main(n, secs, seed):\n    rnd = random.Random(seed)\n    t_end = time.time() + secs\n",
        "def main(n, secs, seed, cap=None):\n    rnd = random.Random(seed)\n    t_end = time.time() + (cap if cap else secs); tw0 = time.time()\n")
s = sub(s, "    while time.time() < t_end:\n        while True:\n            W = [rnd.choice(LET) for _ in range(n)]\n            if ok(W): break\n        r = evaluate(W); cur = score(r[0], r[1], W) if r else None\n",
        "    while time.time() < t_end and BUDGET_OK(evals, restarts):\n        while True:\n            W = [rnd.choice(LET) for _ in range(n)]\n            if ok(W): break\n        r = evaluate(W); cur = score(r[0], r[1], W) if r else None\n        if r and r[0] == {0: 1}: KC(rho2.halfword('l1.l1', W, 'u2.u2'), 'init', evals)\n")
s = sub(s, "            if time.time() > t_end: break\n            T = T0", "            if time.time() > t_end or not BUDGET_OK(evals): break\n            T = T0")
s = sub(s, "                st, why = kcert.certify(hw)\n", "                st, why = KC(hw, 'inner', evals)\n")
s = sub(s, "open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB/out/HIT_CANDIDATES.txt', 'a')", "open(U45_OUT + '/HIT_CANDIDATES.txt', 'a')")
s = sub(s, "'best_any': bestany, 'hits': hits, 'top_a2zero': recs[:40]}\n",
        "'best_any': bestany, 'hits': hits, 'top_a2zero': recs[:40],\n           'u45': {'max_evals': MAXE, 'max_restarts': MAXR, 'cap': cap, 'wall': round(time.time() - tw0, 1), 'budget_reached': not BUDGET_OK(evals, restarts), 'n_j1_distinct': len(J1), 'n_j1_probes': sum(e['count'] for e in J1.values())},\n           'j1_words': J1}\n")
s = sub(s, "open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB/out/e3%s_n%d_s%d.json' % ('b' if REL else '', n, seed), 'w')",
        "open(U45_OUT + '/e3%s_n%d_s%d.json' % ('b' if REL else '', n, seed), 'w')")
s = sub(s, "    if len(sys.argv) > 4 and sys.argv[4] == 'rel': REL = True\n    main(int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]))\n",
        "    if len(sys.argv) > 4 and sys.argv[4] == 'rel': REL = True\n    if len(sys.argv) > 5: MAXE = int(sys.argv[5]); MAXR = int(sys.argv[6])\n    main(int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), cap=(float(sys.argv[7]) if len(sys.argv) > 7 else None))\n")
open(DST + 'e3_search.py', 'w').write(s)

# ---------------- e3w3.py ----------------
s = open(SRC + 'e3w3.py').read()
s = sub(s, "sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont')\n",
        "sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont')\nsys.path.insert(0, %r)   # u45: the patched e3_search (z10, ord1 unchanged)\n" % DST)
s = sub(s, "import fastJ3, lp, kcert, e3_search\n", "import fastJ3, lp, kcert\nsys.path.insert(0, %r)\nimport e3_search\nassert e3_search.__file__.startswith(%r)\n" % (DST, DST) + KC)
s = sub(s, "def main(n, secs, seed):\n    rnd = random.Random(seed); t_end = time.time() + secs\n",
        "def main(n, secs, seed, cap=None):\n    rnd = random.Random(seed); t_end = time.time() + (cap if cap else secs); tw0 = time.time()\n")
s = sub(s, "    while time.time() < t_end:\n", "    while time.time() < t_end and BUDGET_OK(evals):\n")
s = sub(s, "        J = fastJ3.J(W)\n        if J is None or J == {0: 1}: continue\n",
        "        J = fastJ3.J(W)\n        if J == {0: 1}: KC(fastJ3.halfword(W), 'init', evals)\n        if J is None or J == {0: 1}: continue\n")
s = sub(s, "            if time.time() > t_end: break\n", "            if time.time() > t_end or not BUDGET_OK(evals): break\n")
s = sub(s, "                hw = fastJ3.halfword(W2); st, why = kcert.certify(hw)\n", "                hw = fastJ3.halfword(W2); st, why = KC(hw, 'inner', evals)\n")
s = sub(s, "open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB/out/HIT_CANDIDATES.txt', 'a')", "open(U45_OUT + '/HIT_CANDIDATES.txt', 'a')")
s = sub(s, "           'gated': [r for r in recs if r['zeta10']][:40]}\n",
        "           'gated': [r for r in recs if r['zeta10']][:40],\n           'u45': {'max_evals': MAXE, 'cap': cap, 'wall': round(time.time() - tw0, 1), 'budget_reached': not BUDGET_OK(evals), 'n_j1_distinct': len(J1), 'n_j1_probes': sum(e['count'] for e in J1.values())},\n           'j1_words': J1}\n")
s = sub(s, "open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB/out/e3w3_n%d_s%d.json' % (n, seed), 'w')", "open(U45_OUT + '/e3w3_n%d_s%d.json' % (n, seed), 'w')")
s = sub(s, "    main(int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]))\n",
        "    if len(sys.argv) > 4: MAXE = int(sys.argv[4])\n    main(int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), cap=(float(sys.argv[5]) if len(sys.argv) > 5 else None))\n")
open(DST + 'e3w3.py', 'w').write(s)

# ---------------- e3d_alex.py ----------------
s = open(SRC + 'e3d_alex.py').read()
s = sub(s, "sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')\n",
        "sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')\nsys.path.insert(0, %r)   # u45: the patched e3_search (z10, INV unchanged)\n" % DST)
s = sub(s, "        st, why = kcert.certify(hw)\n", "        st, why = KC(hw, 'evalf', EVALS[0])\n")
s = sub(s, "import fastJ, rho2, lp, kcert, e3_search, vspan, alex\n", "import fastJ, rho2, lp, kcert\nsys.path.insert(0, %r)\nimport e3_search\nimport vspan, alex\nassert e3_search.__file__.startswith(%r)\n" % (DST, DST) + KC + "EVALS = [0]\n")
s = sub(s, "open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB/out/HIT_CANDIDATES.txt', 'a')", "open(U45_OUT + '/HIT_CANDIDATES.txt', 'a')")
s = sub(s, "def main(n, secs, seed):\n    rnd = random.Random(seed); t_end = time.time() + secs\n",
        "def main(n, secs, seed, cap=None):\n    rnd = random.Random(seed); t_end = time.time() + (cap if cap else secs); tw0 = time.time()\n")
s = sub(s, "    while time.time() < t_end:\n", "    while time.time() < t_end and BUDGET_OK(evals):\n")
s = sub(s, "            if time.time() > t_end: break\n", "            if time.time() > t_end or not BUDGET_OK(evals): break\n")
s = sub(s, "            r = evalf(W2); evals += 1\n", "            EVALS[0] = evals; r = evalf(W2); evals += 1\n")
s = sub(s, "           'n_zeta10': sum(1 for x in found.values() if x['zeta10'])}\n",
        "           'n_zeta10': sum(1 for x in found.values() if x['zeta10']),\n           'u45': {'max_evals': MAXE, 'cap': cap, 'wall': round(time.time() - tw0, 1), 'budget_reached': not BUDGET_OK(evals), 'n_j1_distinct': len(J1), 'n_j1_probes': sum(e['count'] for e in J1.values())},\n           'j1_words': J1}\n")
s = sub(s, "open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB/out/e3d_n%d_s%d.json' % (n, seed), 'w')", "open(U45_OUT + '/e3d_n%d_s%d.json' % (n, seed), 'w')")
s = sub(s, "    main(int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]))\n",
        "    if len(sys.argv) > 4: MAXE = int(sys.argv[4])\n    main(int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), cap=(float(sys.argv[5]) if len(sys.argv) > 5 else None))\n")
open(DST + 'e3d_alex.py', 'w').write(s)
print('patched OK')
