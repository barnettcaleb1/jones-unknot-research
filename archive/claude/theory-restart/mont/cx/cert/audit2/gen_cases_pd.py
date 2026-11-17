"""gen_cases_pd.py -- AUDIT-2 PD-route cases: Alexander-trivial knots (KT, Conway, pretzels, Whitehead doubles),
mirrors, composites, long cancelling diagrams, and hard unknots (Regina 'monster', Haken's Gordian unknot, sums)."""
import sys, json, random
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/audit2')
import a2lib, pdknots
rng = random.Random(4242)
d = json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/audit2/data/regina_examplelink.json'))
K = {}
for k in ('kinoshitaTerasaka', 'conway', 'monster', 'gordian'):
    K[k] = a2lib.gauss_to_pd(d[k]['signs'], d[k]['comp'])
K['KT_katlas'] = pdknots.katlas_pd('K11n42')
M = {}   # Morse-built
M['P(-3,5,7)'] = a2lib.pretzel_full([-3, 5, 7])
M['P(-5,7,17)'] = a2lib.pretzel_full([-5, 7, 17])
M['P(-7,9,31)'] = a2lib.pretzel_full([-7, 9, 31])
M['Wh(3_1,+)'] = a2lib.whitehead_double_full(pdknots.TREFOIL, 'x')
M['Wh(3_1,-)'] = a2lib.whitehead_double_full(pdknots.TREFOIL, 'y')
M['Wh(3_1m,+)'] = a2lib.whitehead_double_full(a2lib.mirror_full(pdknots.TREFOIL), 'x')
M['Wh(3_1m,-)'] = a2lib.whitehead_double_full(a2lib.mirror_full(pdknots.TREFOIL), 'y')
M['Wh(4_1,+)'] = a2lib.whitehead_double_full(pdknots.FIG8, 'x')
M['Wh(4_1,-)'] = a2lib.whitehead_double_full(pdknots.FIG8, 'y')
M['Wh(Wh(3_1))'] = a2lib.whitehead_double_full(M['Wh(3_1,+)'], 'x')          # iterated double (Delta = 1)
cases = []
def add(X, sg, label, expect, **kw):
    c = {'X': [list(x) for x in X], 'sign': list(sg), 'label': label, 'expect': expect}
    c.update(kw); cases.append(c)
# Alexander-trivial nontrivial: base + mirror
for k in ('kinoshitaTerasaka', 'conway', 'KT_katlas'):
    X, sg = K[k]
    add(X, sg, 'P1:' + k, 'nontrivial')
    Xm, sgm = a2lib.mirror_pd(X)
    add(Xm, sgm, 'P1:' + k + '_mirror', 'nontrivial')
for k, f in M.items():
    X, sg = a2lib.pd_from_full(f)
    add(X, sg, 'P2:' + k, 'nontrivial')
    X, sg = a2lib.pd_from_full(a2lib.mirror_full(f))
    add(X, sg, 'P2:' + k + '_mirror', 'nontrivial')
# composites (PD-level and Morse-level)
def pdof(name):
    if name in K: return K[name]
    return a2lib.pd_from_full(M[name])
pairs = [('kinoshitaTerasaka', 'conway'), ('kinoshitaTerasaka', 'kinoshitaTerasaka'), ('conway', 'conway'),
         ('kinoshitaTerasaka', 'P(-3,5,7)'), ('conway', 'Wh(3_1,+)'), ('Wh(3_1,+)', 'Wh(4_1,-)'), ('P(-3,5,7)', 'Wh(4_1,+)'),
         ('kinoshitaTerasaka', 'monster'), ('conway', 'monster'), ('P(-3,5,7)', 'monster'), ('Wh(3_1,-)', 'monster')]
for a, b in pairs:
    X1, s1 = pdof(a); X2, s2 = pdof(b)
    for e1, e2 in ((0, 0), (5, 7)):
        X, sg = a2lib.pd_connected_sum(X1, s1, X2, s2, e1 % (2 * len(X1)), e2 % (2 * len(X2)))
        add(X, sg, 'P3:%s#%s@%d,%d' % (a, b, e1, e2), 'nontrivial')
# K # mirror K (Alexander-trivial, ribbon-type)
for k in ('kinoshitaTerasaka', 'conway'):
    X1, s1 = K[k]; X2, s2 = a2lib.mirror_pd(X1)
    X, sg = a2lib.pd_connected_sum(X1, s1, X2, s2, 0, 3)
    add(X, sg, 'P3:%s#mirror' % k, 'nontrivial')
# nontrivial # Gordian unknot (big diagram, mostly 'unknot' material)
for k in ('kinoshitaTerasaka', 'conway'):
    X1, s1 = K[k]; X2, s2 = K['gordian']
    X, sg = a2lib.pd_connected_sum(X1, s1, X2, s2, 0, 0)
    add(X, sg, 'P3:%s#gordian' % k, 'nontrivial')
X1, s1 = a2lib.pd_from_full(M['P(-3,5,7)']); X2, s2 = K['gordian']
X, sg = a2lib.pd_connected_sum(X1, s1, X2, s2, 0, 0); add(X, sg, 'P3:P(-3,5,7)#gordian', 'nontrivial')
# long cancelling Morse diagrams of Delta = 1 knots
for name in ('P(-3,5,7)', 'Wh(3_1,+)', 'Wh(4_1,-)', 'P(-5,7,17)'):
    for t in range(6):
        f = pdknots.cancel_insert_full(M[name], rng, nins=rng.randint(3, 8), wlen=rng.randint(6, 14))
        X, sg = a2lib.pd_from_full(f)
        add(X, sg, 'P4:%s_cancel%d' % (name, t), 'nontrivial')
# hard unknots
X, sg = K['monster']; add(X, sg, 'U1:monster', 'unknot', blind=False, tietze_budget=30.0)
Xm, sgm = a2lib.mirror_pd(X); add(Xm, sgm, 'U1:monster_mirror', 'unknot', blind=False, tietze_budget=30.0)
X2, s2 = a2lib.pd_connected_sum(X, sg, Xm, sgm, 0, 4); add(X2, s2, 'U1:monster#monster_m', 'unknot', blind=False, tietze_budget=30.0)
X3, s3 = a2lib.pd_connected_sum(X2, s2, X, sg, 7, 2); add(X3, s3, 'U1:monster^3', 'unknot', blind=False, tietze_budget=30.0)
X, sg = K['gordian']; add(X, sg, 'U1:gordian', 'unknot', blind=False, tietze_budget=60.0)
Xm, sgm = a2lib.mirror_pd(X); add(Xm, sgm, 'U1:gordian_mirror', 'unknot', blind=False, tietze_budget=60.0)
json.dump(cases, open('cases_pd.json', 'w'))
print(len(cases), 'cases;', 'n range', min(len(c['X']) for c in cases), max(len(c['X']) for c in cases))
for c in cases: print(c['label'], len(c['X']), a2lib.faces_count([tuple(x) for x in c['X']]) == len(c['X']) + 2, a2lib.pd_components([tuple(x) for x in c['X']]))
