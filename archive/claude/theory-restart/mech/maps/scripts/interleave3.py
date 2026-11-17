import sys; sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mech/maps/scripts')
from typeD import *
from interleave import *
BN31 = parse_chain(0, 10, '⬮~~S~>⬯—>⬯~>⬯—>⬯~>⬮<—⬮~>⬯—>⬯~>⬯—>⬯')
Ya = parse_chain(0, 8, '⬮~~S~>⬯—>⬯~>⬯—>⬯~>⬯—>⬯~>⬯—>⬯')
report('trefoil quotient (X) vs self-crossing (special strand) change at letter 5 = Q_{-8} (Y), printed frame', BN31, Ya)
