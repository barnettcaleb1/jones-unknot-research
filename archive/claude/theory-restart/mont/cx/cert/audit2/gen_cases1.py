"""gen_cases1.py -- AUDIT-2 halfword test cases (own generator; expectations from my own bracket).
H1 random long halfwords V != 1; H2 mirrors; H3 composites (equivariant sums, K#K, K#mirror K, triple sums, swap sums);
H4 long highly cancelling diagrams of nontrivial knots; H6 unknot diagrams > 24 crossings (V = 1 base with <= 24
crossings = unknot by Tuzun-Sikora, inflated by cancelling insertions)."""
import sys, json, random
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/audit2')
import a2lib, gen

rng = random.Random(20261117)


def info(hw):
    full = a2lib.full_of(hw)
    D = a2lib.morse_diagram(full)
    if D is None or D['n'] == 0: return None
    v1 = a2lib.jones_unit_test(a2lib.bracket_full(full))
    return D['n'], v1


def body(hw):
    assert hw.startswith('s.')
    return hw[2:]


cases = []
nontriv_pool = []      # (hw, n)
unknot_small = []      # V = 1 and n <= 24 -> unknot (TS)

# H1
tries = 0
while sum(1 for c in cases if c['label'].startswith('H1')) < 300:
    tries += 1
    L = rng.randint(20, 60); mh = rng.choice([3, 5, 5, 7])
    hw = gen.rand_halfword(rng, L, maxhw=mh)
    r = info(hw)
    if r is None: continue
    n, v1 = r
    if v1:
        if n <= 24: unknot_small.append(hw)
        continue
    cases.append({'hw': hw, 'label': 'H1:rand_long', 'expect': 'nontrivial', 'n': n})
print('H1 tries', tries, 'unknot_small so far', len(unknot_small))

# small nontrivial pool for composites / cancelling
while len(nontriv_pool) < 400:
    L = rng.randint(4, 16); mh = rng.choice([3, 5])
    hw = gen.rand_halfword(rng, L, maxhw=mh)
    r = info(hw)
    if r is None: continue
    n, v1 = r
    if v1:
        if n <= 24: unknot_small.append(hw)
        continue
    nontriv_pool.append((hw, n))

# H2 mirrors
for c in cases[:120]:
    m = a2lib.mirror_hw(c['hw'])
    cases.append({'hw': m, 'label': 'H2:mirror', 'expect': 'nontrivial', 'n': c['n']})

# H3 composites
for k in range(80):
    (a, na), (b, nb) = rng.sample(nontriv_pool, 2)
    cases.append({'hw': 's.' + body(a) + '.' + body(b), 'label': 'H3:sum2', 'expect': 'nontrivial'})
for k in range(40):
    a, na = rng.choice(nontriv_pool)
    cases.append({'hw': 's.' + body(a) + '.' + body(a), 'label': 'H3:KK', 'expect': 'nontrivial'})
    cases.append({'hw': 's.' + body(a) + '.' + body(a2lib.mirror_hw(a)), 'label': 'H3:Kmirror', 'expect': 'nontrivial'})
for k in range(40):
    (a, na), (b, nb), (c, nc) = rng.sample(nontriv_pool, 3)
    cases.append({'hw': 's.' + body(a) + '.' + body(b) + '.' + body(c), 'label': 'H3:sum3', 'expect': 'nontrivial'})
sw = 0
while sw < 80:
    L = rng.randint(8, 30)
    hw = gen.rand_halfword(rng, L, maxhw=rng.choice([3, 5]), p_axis=0.0)
    r = info(hw)
    if r is None: continue
    n, v1 = r
    if v1: continue
    cases.append({'hw': hw, 'label': 'H3:swapsum', 'expect': 'nontrivial', 'n': n}); sw += 1
# composites with an unknot summand diagram (V=1 small) : K # (unknot diagram)
for k in range(30):
    a, na = rng.choice(nontriv_pool)
    if unknot_small:
        u = rng.choice(unknot_small)
        cases.append({'hw': 's.' + body(a) + '.' + body(u), 'label': 'H3:K_unknotdiag', 'expect': 'nontrivial'})

# H4 cancelling
for k in range(150):
    a, na = rng.choice(nontriv_pool)
    hw = gen.insert_cancelling(a, rng, nins=rng.randint(2, 8), wlen=rng.randint(4, 12))
    if rng.random() < 0.5: hw = gen.conjugate_insert(hw, rng, wlen=rng.randint(4, 10))
    if info(hw) is None: continue
    cases.append({'hw': hw, 'label': 'H4:cancel', 'expect': 'nontrivial'})

# H6 unknots > 24 crossings
uk = list(dict.fromkeys(unknot_small))
rng.shuffle(uk)
for hw in uk[:120]:
    big = gen.insert_cancelling(hw, rng, nins=rng.randint(2, 6), wlen=rng.randint(4, 10))
    r = info(big)
    if r is None: continue
    n, v1 = r
    assert v1
    cases.append({'hw': big, 'label': 'H6:unknot_inflated', 'expect': 'unknot', 'n': n})
for hw in uk[:120]:
    cases.append({'hw': hw, 'label': 'H6:unknot_small', 'expect': 'unknot'})

# fill n
for c in cases:
    if 'n' not in c:
        c['n'] = info(c['hw'])[0]

json.dump(cases, open('cases1.json', 'w'))
blind = [dict(c, blind=True, label=c['label'] + ':blind') for c in cases if c['expect'] == 'nontrivial']
json.dump(blind, open('cases1_blind.json', 'w'))
import collections
print(collections.Counter(c['label'] for c in cases))
print('n range', min(c['n'] for c in cases), max(c['n'] for c in cases), 'unknot_small', len(uk))
