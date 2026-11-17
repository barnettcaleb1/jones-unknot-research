"""gen_cases5.py -- AUDIT-2 halfword cases of Alexander-trivial knots: swap sums K' # rK' of Delta = 1 knots K'
(pretzels (-3,5,7), (-5,7,17), untwisted Whitehead doubles of 3_1, 3_1 mirror, 4_1, iterated double), their mirrors,
equivariant sums of two of them, and cancel-inflated versions.  All have Delta = 1 and V != 1 (checked here)."""
import sys, json, random
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/audit2')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')
import a2lib, gen, pdknots, alex
rng = random.Random(55)
base = {'P(-3,5,7)': a2lib.pretzel_full([-3, 5, 7]), 'P(-5,7,17)': a2lib.pretzel_full([-5, 7, 17]),
        'Wh(3_1,+)': a2lib.whitehead_double_full(pdknots.TREFOIL, 'x'), 'Wh(3_1,-)': a2lib.whitehead_double_full(pdknots.TREFOIL, 'y'),
        'Wh(3_1m,+)': a2lib.whitehead_double_full(a2lib.mirror_full(pdknots.TREFOIL), 'x'),
        'Wh(4_1,+)': a2lib.whitehead_double_full(pdknots.FIG8, 'x'), 'Wh(4_1,-)': a2lib.whitehead_double_full(pdknots.FIG8, 'y')}
# Wh(Wh(3_1)) dropped: its swap-sum Morse word is ~40 strands wide (bracket sweep infeasible)
cases = []
def ok_case(hw):
    full = a2lib.full_of(hw); D = a2lib.morse_diagram(full)
    if D is None: return None
    if any(alex.alex_eval(hw, t) != 1 for t in (-1, 2, 3)): return None
    if a2lib.jones_unit_test(a2lib.bracket_full(full)): return None
    return D['n']
sw = {}
for name, f in base.items():
    hw = gen.swap_sum_halfword(f); n = ok_case(hw); assert n, name
    sw[name] = hw
    cases.append({'hw': hw, 'label': 'H5:swap:' + name, 'expect': 'nontrivial', 'n': n})
    m = a2lib.mirror_hw(hw); n = ok_case(m); assert n
    cases.append({'hw': m, 'label': 'H5:swapmirror:' + name, 'expect': 'nontrivial', 'n': n})
names = [k for k in sw if k != 'Wh(Wh(3_1))']
for k in range(10):
    a, b = rng.sample(names, 2)
    hw = 's.' + sw[a][2:] + '.' + a2lib.mirror_hw(sw[b])[2:]
    n = ok_case(hw); assert n
    cases.append({'hw': hw, 'label': 'H5:sum:%s#%s_m' % (a, b), 'expect': 'nontrivial', 'n': n})
for k in range(24):
    a = rng.choice(names)
    hw = gen.insert_cancelling(sw[a], rng, nins=rng.randint(2, 6), wlen=rng.randint(4, 10))
    n = ok_case(hw)
    if not n: continue
    cases.append({'hw': hw, 'label': 'H5:cancel:' + a, 'expect': 'nontrivial', 'n': n})
json.dump(cases, open('cases5.json', 'w'))
json.dump([dict(c, blind=True, tietze_budget=10.0, label=c['label'].replace('H5:', 'H5b:')) for c in cases], open('cases5_blind.json', 'w'))
for c in cases: print(c['label'], c['n'])
