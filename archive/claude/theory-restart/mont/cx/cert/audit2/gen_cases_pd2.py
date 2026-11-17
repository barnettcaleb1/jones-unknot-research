"""gen_cases_pd2.py -- AUDIT-2: hard unknots (Burton et al. 2021 list, signs recovered by planarity, V = 1 checked),
their mirrors, sums of hard unknots beyond 24 crossings, and nontrivial knots with hard-unknot summands."""
import sys, json
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/audit2')
import a2lib, pdknots
H = json.load(open('data/hard_unknots_signed.json'))
R = json.load(open('data/regina_examplelink.json'))
U = {k: a2lib.gauss_to_pd(v['signs'], v['comp']) for k, v in H.items()}
cases = []
def add(XS, label, expect, **kw):
    X, sg = XS
    c = {'X': [list(x) for x in X], 'sign': list(sg), 'label': label, 'expect': expect}; c.update(kw); cases.append(c)
for k, XS in U.items():
    add(XS, 'U2:' + k, 'unknot', blind=False, tietze_budget=30.0, do_rep=False)
    add(a2lib.mirror_pd(XS[0]), 'U2:' + k + '_mirror', 'unknot', blind=False, tietze_budget=30.0, do_rep=False)
def csum(a, b, e1=0, e2=0):
    return a2lib.pd_connected_sum(a[0], a[1], b[0], b[1], e1 % (2 * len(a[0])), e2 % (2 * len(b[0])))
s = csum(csum(U['culprit'], U['goeritz'], 3, 5), U['thistlethwaite'], 11, 2)
add(s, 'U3:culprit#goeritz#thistlethwaite', 'unknot', blind=False, tietze_budget=30.0, do_rep=False)
s = csum(csum(U['goeritz'], a2lib.mirror_pd(U['goeritz'][0]), 1, 4), U['goeritz'], 9, 9)
add(s, 'U3:goeritz^3', 'unknot', blind=False, tietze_budget=30.0, do_rep=False)
add(csum(U['ochiai1'], U['culprit'], 6, 6), 'U3:ochiai1#culprit', 'unknot', blind=False, tietze_budget=30.0, do_rep=False)
add(csum(U['fhw'], U['ochiai2_reduced'], 6, 6), 'U3:fhw#ochiai2r', 'unknot', blind=False, tietze_budget=30.0, do_rep=False)
# rep search on unknots with Tietze effectively disabled: must NOT find a nonabelian rep (false COUNTEREXAMPLE test)
for k in ('culprit', 'goeritz', 'thistlethwaite', 'ochiai1', 'fhw', 'pz31'):
    add(U[k], 'U4:repsearch_on_unknot:' + k, 'unknot', blind=False, tietze_budget=0.0, do_rep=True, rep_budget=20.0, skip_j24=True)
KT = a2lib.gauss_to_pd(R['kinoshitaTerasaka']['signs'], R['kinoshitaTerasaka']['comp'])
CW = a2lib.gauss_to_pd(R['conway']['signs'], R['conway']['comp'])
P357 = a2lib.pd_from_full(a2lib.pretzel_full([-3, 5, 7]))
WH = a2lib.pd_from_full(a2lib.whitehead_double_full(pdknots.TREFOIL, 'x'))
for (a, an), (b, bn) in [((KT, 'KT'), (U['culprit'], 'culprit')), ((CW, 'conway'), (U['goeritz'], 'goeritz')),
                         ((P357, 'P(-3,5,7)'), (U['thistlethwaite'], 'thistlethwaite')), ((WH, 'Wh(3_1)'), (U['ochiai1'], 'ochiai1')),
                         ((KT, 'KT'), (U['fhw'], 'fhw')), ((CW, 'conway'), (U['pz31'], 'pz31'))]:
    add(csum(a, b, 2, 3), 'P5:%s#%s' % (an, bn), 'nontrivial', blind=True, tietze_budget=15.0, do_rep=len(a[0]) + len(b[0]) <= 40, rep_budget=60.0)
json.dump(cases, open('cases_pd2.json', 'w'))
for c in cases: print(c['label'], len(c['X']), a2lib.faces_count([tuple(x) for x in c['X']]) == len(c['X']) + 2, a2lib.pd_components([tuple(x) for x in c['X']]))
