import json
rows = json.load(open('sweep.json'))
both = [r['name'] for r in rows if not r['bad1'] and not r['bad0']]
only1 = [r['name'] for r in rows if not r['bad1'] and r['bad0']]
only0 = [r['name'] for r in rows if r['bad1'] and not r['bad0']]
neither = [r['name'] for r in rows if r['bad1'] and r['bad0']]
print('adequate both ends', len(both), both)
print('1-end only', len(only1)); print('0-end only', len(only0)); print('neither', len(neither))
# Theorem 2.3 applicability
t23 = []
for r in rows:
    ok = False
    if not r['bad1'] and r['M'] != r['d0']: ok = True
    if not r['bad0'] and r['m'] != r['d0']: ok = True
    if ok: t23.append(r['name'])
    if (not r['bad1'] and r['M'] == r['d0']) or (not r['bad0'] and r['m'] == r['d0']):
        print('   unit AT an adequate corner:', r['name'])
print('Thm 2.3 applies:', len(t23))
pos = [r for r in rows if abs(r['wr']) == r['c']]
print('|wr| = c:', len(pos))
t24 = []
for r in pos:
    c, ca, co = r['c'], r['c_axis'], r['c_o']
    if r['wr'] == -c:
        l = r['loops1']; k = r['k1']; gap = r['d0'] - r['M']
        assert r['cut1'] == ca and r['arcs1'] == ca + 1
    else:
        l = r['loops0']; k = r['k0']; gap = r['m'] - r['d0']
        assert r['cut0'] == ca and r['arcs0'] == ca + 1
    assert k == 2 * ca + 2 * l, r['name']
    assert gap == 2 * (co - l), r['name']
    # support of alpha relative to d0
    exps = sorted(int(e) for e in r['alpha'])
    if r['wr'] == -c:
        assert exps[-1] <= r['d0'] - 2 * (co - l)
    else:
        assert exps[0] >= r['d0'] + 2 * (co - l)
    t24.append((r['name'], r['wr'], co, l, co - l, exps[0] - r['d0'], exps[-1] - r['d0']))
for t in t24: print('   ', t)
u = set(t23) | set(x[0] for x in t24 if x[4] > 0)
print('non-flat by Thm 2.3 or 2.4:', len(u), ' remaining:', len(rows) - len(u))
rem = [r['name'] for r in rows if r['name'] not in u]
print(rem)
# is the unit ever inside the support?  list J (alpha shifted) top/bottom
cnt = 0
for r in rows:
    exps = sorted(int(e) for e in r['alpha'])
    if not (exps[0] <= r['d0'] <= exps[-1]): cnt += 1
print('half-diagrams where the unit degree d0 lies outside the support of chi_q(C_b):', cnt)
