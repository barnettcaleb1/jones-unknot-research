"""Census: how often do actual frontier records carry nonunit content gcd(a,c) (equivalently gcd(A,B))?  Full dangerous set D (774
depth-one classes, arb greedy_n2.pkl) and all 292 depth-2 positive-potential boxes (engineA d2pos_boxes.pkl); general body G6."""
import sys, pickle, collections
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/referee/arb-resonance')
from common import *
arb = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/arb/'
g = pickle.load(open(arb + 'greedy_n2.pkl', 'rb'))
out = collections.Counter(); ex = []
for lab, val in g['D'].items():
    T = tree_of(val[1][1], R5); v = vc.vec(T); s = th(v)
    G = gcdL(*s)
    out['D_content' if G != {0: 1} else 'D_primitive'] += 1
    if G != {0: 1}: ex.append((lab, T, sorted(G.items())))
d2 = pickle.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA/d2pos_boxes.pkl', 'rb'))
for k, v, T, tag in d2:
    G = gcdL(*th(v))
    out['d2pos_content' if G != {0: 1} else 'd2pos_primitive'] += 1
    if G != {0: 1}: ex.append(('d2pos', T, sorted(G.items())))
print(dict(out))
for x in ex[:12]: print('  ', x)
gc = collections.Counter(tuple(x[2]) for x in ex); print('content polynomials:', gc.most_common(8))
Bw, v = vc.gboxes()[6]
s = th(v); G = gcdL(*s); print('G6 word', Bw, 'state', s, 'gcd', G)
q = (vc.divexact(s[0], G), vc.divexact(s[1], G)); print('G6 / content =', q)
