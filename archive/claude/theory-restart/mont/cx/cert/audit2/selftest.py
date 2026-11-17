"""selftest.py -- validate a2lib against the project tools and compare with the certifier's own presentation."""
import sys, random, time
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/audit2')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')
import a2lib, gen, alex, kauffman
CERT = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert'
sys.path.insert(0, CERT)
import diagram, wirtinger

def ident3_VK(word):
    kb = kauffman.bracket(word)
    if not kb: return None
    kb = {e: c for e, c in kb.items() if c}
    es = sorted(kb); r = es[0] % 4
    if any((e - r) % 4 for e in es): return None
    V = {-(e - r) // 4: c for e, c in kb.items()}
    s = sum(V.values())
    if s not in (1, -1): return None
    V = {e: c * s for e, c in V.items()}
    d = sum(e * c for e, c in V.items())
    return {e - d: c for e, c in V.items()}

rng = random.Random(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
N = int(sys.argv[2]) if len(sys.argv) > 2 else 300
stats = dict(words=0, knots=0, wirt_equal=0, wirt_diff=0, V_equal=0, V_mirror=0, V_diff=0, alex_ok=0, alex_bad=0, pd_equal=0, pd_diff=0)
t0 = time.time()
while stats['knots'] < N:
    L = rng.randint(3, 22)
    hw = gen.rand_halfword(rng, L)
    stats['words'] += 1
    full = a2lib.full_of(hw)
    D = a2lib.morse_diagram(full)
    pd = diagram.pd_from_halfword(hw)
    if (D is None) != (pd is None):
        print('KNOT-TEST DISAGREES', hw, D is None, pd is None); continue
    if D is None: continue
    if D['n'] == 0: continue
    stats['knots'] += 1
    g1, r1 = a2lib.wirtinger_from_halfword(hw)
    g2, r2 = wirtinger.wirtinger(pd)
    if list(g1) == list(g2) and [tuple(r) for r in r1] == [tuple(r) for r in r2]: stats['wirt_equal'] += 1
    else:
        stats['wirt_diff'] += 1
        if stats['wirt_diff'] < 4: print('WIRT DIFF', hw, r1[:3], r2[:3])
    X, sg = a2lib.pd_from_full(full)
    if [tuple(x) for x in X] == [tuple(x) for x in pd.X] and list(sg) == list(pd.sign): stats['pd_equal'] += 1
    else:
        stats['pd_diff'] += 1
        if stats['pd_diff'] < 4: print('PD DIFF', hw, X[:3], pd.X[:3], sg[:3], pd.sign[:3])
    br = a2lib.bracket_full(full)
    Vm = a2lib.VK_from_bracket(br)
    Vp = ident3_VK(hw)
    if Vm == Vp: stats['V_equal'] += 1
    elif Vm == {-e: c for e, c in Vp.items()}: stats['V_mirror'] += 1
    else:
        stats['V_diff'] += 1; print('V DIFF', hw, Vm, Vp)
    ev = a2lib.alex_trivial_evidence(g1, r1)
    ok = True
    for tv in (-1, 2, 3):
        a = alex.alex_eval(hw, tv)
        if a is None or ev[tv] != a: ok = False
    if ok: stats['alex_ok'] += 1
    else:
        stats['alex_bad'] += 1
        if stats['alex_bad'] < 5: print('ALEX DIFF', hw, ev, [alex.alex_eval(hw, t) for t in (-1, 2, 3)])
print(stats, round(time.time() - t0, 1), 's')
