import sys; sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mech/maps/scripts')
from typeD import *
# trefoil quotient, current kht++ build conventions (lit/kht/REPORT.md 3.3)
BN31 = parse_chain(0, 10, '⬮~~S~>⬯—>⬯~>⬯—>⬯~>⬮<—⬮~>⬯—>⬯~>⬯—>⬯')
R31  = parse_chain(3, 15, '⬮~~S~>⬯—>⬯~>⬯—>⬯~>⬯<—⬯<~⬯<—⬯<~⬮<—')
S31  = parse_chain(-1, 9, '⬮~~S~>⬯—>⬯~>⬯—>⬯~>⬮—>⬮<~⬯<—⬯<~⬯<—⬯<~⬮<—')
print('BN gens', len(BN31.gens), 'r', len(R31.gens), 's4', len(S31.gens))
print('s4 gens:', S31.gens)
a0 = TD([('b', 0, 0)], {}); ainf = TD([('c', 0, 0)], {})
# central elements on s4(inf)
for name in ['Db', 'Dc', 'S2', 'H']:
    M = MorSpace(S31, S31, 0, -2)
    print('  ', name, 'id on s4(inf) null-homotopic:', M.is_boundary(central(S31, name)), ' dim H^{0,-2}End =', M.dim())
M = MorSpace(S31, S31, 0, -2)
print('   Db+S2 nullhomotopic (i.e. Db ~ S2):', M.is_boundary(central(S31,'Db') ^ central(S31,'S2')))
for name in ['Db', 'Dc', 'S2', 'H']:
    M = MorSpace(R31, R31, 0, -2)
    print('  ', name, 'id on r(-4) null-homotopic:', M.is_boundary(central(R31, name)))
for name in ['Db', 'Dc', 'S2', 'H']:
    M = MorSpace(BN31, BN31, 0, -2)
    print('  ', name, 'id on BN(T_31) null-homotopic:', M.is_boundary(central(BN31, name)))
print('End(s4) table (h,q):dim', hom_table(S31, S31, range(-3, 4), range(-12, 13)))
print('End(r(-4)) table', hom_table(R31, R31, range(-3, 4), range(-12, 13)))
# pairing with unknot arc: Mor(mirror a(inf), s4)?  compute both conventions
print('Mor(a_inf, s4):', hom_table(ainf, S31, range(-12, 12), range(-10, 40)))
print('Mor(a_0, s4):', hom_table(a0, S31, range(-12, 12), range(-10, 40)))
print('Mor(a_inf, r):', hom_table(ainf, R31, range(-12, 12), range(-10, 40)))
print('Mor(a_0, r):', hom_table(a0, R31, range(-12, 12), range(-10, 40)))
