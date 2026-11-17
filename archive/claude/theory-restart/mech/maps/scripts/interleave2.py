import sys; sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mech/maps/scripts')
from typeD import *
from interleave import *
X = parse_chain(0, 12, '⬮~~S~>⬯—>⬯~>⬯—>⬯~>⬮<—⬮~>⬯—>⬯~>⬯—>⬯~>⬮<—⬮')
Y = parse_chain(0, 10, '⬮~~S~>⬯—>⬯~>⬯—>⬯~>⬮<—⬮~>⬯—>⬯~>⬯—>⬯~>⬮<—⬮<~⬯<—⬯')
ainf = TD([('c', 0, 0)], {})
print('unknot-closure check, Mor(a_inf, cone_H(X shifted by h^-8 q^-24)):', hom_table(ainf, cone_H(X.shift(-8, -24)), range(-20, 20), range(-40, 40)))
for (dh, dq) in [(-6, -18), (-10, -30)]:
    report('O-frame: X shifted (-8,-24), Y shifted (%d,%d)' % (dh, dq), X.shift(-8, -24), Y.shift(dh, dq))
