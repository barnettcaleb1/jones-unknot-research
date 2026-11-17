import sys; sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mech/maps/scripts')
from typeD import *
from interleave import *
from closures import twist, poincare, show
ainf = TD([('c', 0, 0)], {}); a0 = TD([('b', 0, 0)], {})
# S := BN-type copy of s4(inf): take the Kh special of the trefoil quotient in the normalized frame (offset -10, level 1)
# and shift by q^{-1} so that its H-cone is q S + q^-1 h^-1 S  -> specials at offsets (c, c-2) on one level.
S31n = parse_chain(-1, 9, '⬮~~S~>⬯—>⬯~>⬯—>⬯~>⬮—>⬮<~⬯<—⬯<~⬯<—⬯<~⬮<—').shift(-8, -24)
S = S31n.shift(0, -1)
B = dsum(a0, S, S.shift(1, 0)); B.check()
K = cone_H(B)
print('unknot closure Kh~(B(inf)):', hom_table(ainf, K, range(-30, 31), range(-70, 71)))
for nu in [2, -2, 4]:
    t = poincare(twist(nu), K, range(-30, 31), range(-70, 71))
    print('Kh~(B(1/%d)) by delta diagonal (h,q,mult):' % nu)
    chi = {}
    for (h, q), m in t.items(): chi[q] = chi.get(q, 0) + (-1) ** h * m
    for dl, v in show(t).items(): print('    delta', dl, ' q-range', (min(x[1] for x in v), max(x[1] for x in v)), ' dim', sum(x[2] for x in v))
    print('    Euler characteristic (Jones):', {q: c for q, c in sorted(chi.items()) if c})
    qmax = max(q for (h, q) in t); print('    top quantum degree', qmax, 'occupied homological degrees', sorted(h for (h, q) in t if q == qmax))
print('central elements on B:', {n: MorSpace(B, B, 0, -2).is_boundary(central(B, n)) for n in ('H', 'S2', 'Db', 'Dc')})
print('B vs a(0), interleavings found:', [(r[0], r[1], r[2]) for r in interleavings(B, a0) if r[3]])
