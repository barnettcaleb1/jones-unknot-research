import sys; sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mech/maps/scripts')
from typeD import *
from interleave import *
from closures import twist
ainf = TD([('c', 0, 0)], {})
for n in [2, -2, 4, -4, 3, -3]:
    Y = twist(n)
    print('twist(%d) vs a(inf):' % n)
    for r in interleavings(ainf, Y):
        if r[3]: print('    composite %-3s  deg F=%s deg G=%s : exists   (#classes F %d, G %d)' % (r[0], r[1], r[2], r[4], r[5]))
# B = a(0) + S + hS : central elements and closure
S = parse_chain(-1, 9, '⬮~~S~>⬯—>⬯~>⬯—>⬯~>⬮—>⬮<~⬯<—⬯<~⬯<—⬯<~⬮<—').shift(1, -9 - 5)   # some grading
a0 = TD([('b', 0, 0)], {})
B = dsum(a0, S, S.shift(1, 0))
B.check()
print('B: generators', len(B.gens))
for name in ('H', 'S2', 'Db', 'Dc'):
    print('   %s id null-homotopic on B: %s ; on S: %s' % (name, MorSpace(B, B, 0, -2).is_boundary(central(B, name)), MorSpace(S, S, 0, -2).is_boundary(central(S, name))))
# Kh-type closures of B at slope 1/nu
from closures import poincare, show
K = cone_H(B)
for nu in [2, -2]:
    print('  Kh~(B(1/%d)) by diagonal:' % nu, show(poincare(twist(nu), K, range(-20, 21), range(-50, 51))))
print('  unknot closure of B:', hom_table(ainf, K, range(-20, 21), range(-50, 51)))
# interleaving of B with a(0) (T-slot type): all central composites
print('B vs a(0):')
for r in interleavings(B, a0):
    if r[3]: print('    composite %-3s  deg F=%s deg G=%s : exists' % (r[0], r[1], r[2]))
