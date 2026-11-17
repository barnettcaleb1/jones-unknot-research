import sys; sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mech/maps/scripts')
from typeD import *
from interleave import *
BN31 = parse_chain(0, 10, '⬮~~S~>⬯—>⬯~>⬯—>⬯~>⬮<—⬮~>⬯—>⬯~>⬯—>⬯')
Yc = parse_chain(0, 8, '⬮~~S~>⬯—>⬯~>⬯—>⬯~>⬮<—⬮~>⬯—>⬯')
report('trefoil quotient (X) vs interior mixed crossing change at letter 4 (Y), printed frame (O\')', BN31, Yc)
# O frame: X shift (-8,-24) (lk number 4); Y: lk number 3 or 5
for (dh, dq) in [(-6, -18), (-10, -30)]:
    report('O-frame candidate: X (-8,-24), Y (%d,%d)' % (dh, dq), BN31.shift(-8, -24), Yc.shift(dh, dq))
