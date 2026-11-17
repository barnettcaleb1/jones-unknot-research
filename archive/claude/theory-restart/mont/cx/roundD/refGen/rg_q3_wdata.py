"""Q3: closure-factor data used by the generator, checked directly (own code) for all odd 1 <= |a| <= 41 and 1 <= |mu| <= 40:
 vertical: order-2 log-jets of w_1(a), wV(a) at both ends constant on the classes a=3, a=-3, a>=5, a<=-5; mirror relation
           bottom(a) = top(-a) (C1's 'typ' reduction); delta*_V = -|a|-1; sigma*_V = -1; wV(+-1) = t^(+-3) w_3(+-1);
 horizontal: order-2 log-jets of w_1(mu), w_3(mu) at both ends, sigma*, delta* constant for mu >= 4 and for mu <= -4;
 C1's tables: v3b.wdata and h3b.WJ compared with ours."""
import sys
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refGen')
import rg_core as C
import rg_gen as G
from fractions import Fraction as Fr
bad = []
# vertical
ref = {}
for a in [x for x in range(-41, 42) if x % 2 and abs(x) >= 3]:
    o, sg, ds = G.wjets(G.w1(a), G.wV(a))
    if ds != -abs(a) - 1: bad.append(('delta*V', a, ds))
    if sg != -1: bad.append(('sigma*V', a, sg))
    cls = 'a=3' if a == 3 else 'a=-3' if a == -3 else 'a>=5' if a > 0 else 'a<=-5'
    if cls not in ref: ref[cls] = o
    elif ref[cls] != o: bad.append(('V class unstable', a))
    # mirror: bottom data at a == top data at -a
    o2, _, _ = G.wjets(G.w1(-a), G.wV(-a))
    if o['bot'] != o2['top']: bad.append(('V mirror', a))
print('vertical classes (w_1 jets, wV jets) per end:')
for k, o in ref.items(): print('  ', k, {e: (tuple(map(str, o[e][0])), tuple(map(str, o[e][1]))) for e in o})
# a = +-1 reduce to horizontal mu = +-1
for a in (1, -1):
    if G.wV(a) != C.pshift(G.w3(a), 3 * a): bad.append(('wV(+-1) != t^(+-3) w_3', a))
    if G.w1(a) != G.w1(a): bad.append('w1')
# compare with C1's v3b.wdata: typ '+' (top a>=3 / bottom a<=-3): w1 (0,1), wV (1,1/2); typ '-': w1 (0,-1 if |a|=3 else 0), wV (0,0)
exp = {('top', 'a=3'): ((0, 1), (1, Fr(1, 2))), ('top', 'a>=5'): ((0, 1), (1, Fr(1, 2))),
       ('bot', 'a=-3'): ((0, 1), (1, Fr(1, 2))), ('bot', 'a<=-5'): ((0, 1), (1, Fr(1, 2))),
       ('top', 'a=-3'): ((0, -1), (0, 0)), ('bot', 'a=3'): ((0, -1), (0, 0)),
       ('top', 'a<=-5'): ((0, 0), (0, 0)), ('bot', 'a>=5'): ((0, 0), (0, 0))}
for (end, cls), (pw, qw) in exp.items():
    if tuple(ref[cls][end][0]) != tuple(map(Fr, pw)) or tuple(ref[cls][end][1]) != tuple(map(Fr, qw)):
        bad.append(('C1 wdata mismatch', end, cls, ref[cls][end]))
# horizontal
href = {}
for mu in [x for x in range(-40, 41) if x]:
    o, sg, ds = G.wjets(G.w1(mu), G.w3(mu))
    cls = mu if abs(mu) <= 3 else ('>=4' if mu > 0 else '<=-4')
    if cls not in href: href[cls] = (o, sg, ds)
    elif href[cls] != (o, sg, ds): bad.append(('H class unstable', mu))
print('horizontal classes: (sigma*, delta*) =', {k: (str(v[1]), v[2]) for k, v in href.items()})
sys.path.insert(1, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC1')
sys.path.insert(2, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import h3b
for mu in h3b.MUS:
    o, sg, ds = h3b.WJ[mu]
    cls = mu if abs(mu) <= 3 else ('>=4' if mu > 0 else '<=-4')
    mo, msg, mds = href[cls]
    for e in ('top', 'bot'):
        if (tuple(o[e][0]), tuple(o[e][1])) != (tuple(mo[e][0]), tuple(mo[e][1])): bad.append(('C1 WJ jets', mu, e))
    if sg != msg or ds != mds: bad.append(('C1 WJ sigma/delta', mu, sg, msg, ds, mds))
print('problems:', bad if bad else 'none')
