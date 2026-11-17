import sys; sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mech/maps/scripts')
from typeD import *
S = parse_chain(-1, 9, '⬮~~S~>⬯—>⬯~>⬯—>⬯~>⬮—>⬮<~⬯<—⬯<~⬯<—⬯<~⬮<—')
t = hom_table(S, S, range(-6, 8), range(-16, 17))
print('End(s4(inf)) bidegrees (h,q):dim ->', t, ' total', sum(t.values()))
hom0 = sorted({(-q, -q // 2 + h) for (h, q) in t})
ext1 = sorted({(-q, -q // 2 + h - 1) for (h, q) in t})
print('degree (0,0) maps S_(c,d) -> S_(c+Dc,d+Dd) exist iff (Dc,Dd) in', hom0)
print('degree (1,0) maps S_(c,d) -> S_(c+Dc,d+Dd) exist iff (Dc,Dd) in', ext1)
# explicit homotopies for the central elements (hand formulas of the report), verified here
M = MorSpace(S, S, 0, -2)
g = lambda i: i - 1
K_b = {(g(13 - i), g(i), ('1', S.gens[g(i)][0])) for i in range(1, 7)}
K_c = {(g(3), g(2), ('1', 'c')), (g(5), g(4), ('1', 'c')), (g(8), g(9), ('1', 'c')), (g(10), g(11), ('1', 'c'))}
K_s = {(g(2), g(1), ('S', 'c', 1)), (g(4), g(3), ('1', 'c')), (g(6), g(5), ('S', 'b', 1)), (g(7), g(8), ('S', 'b', 1)), (g(9), g(10), ('1', 'c')), (g(11), g(12), ('S', 'c', 1))}
def bd(Kset):
    acc = set()
    for f in Kset: acc ^= mor_diff(S, S, f)
    return acc
print('d(K_b) == D_b id :', bd(K_b) == central(S, 'Db'))
print('d(K_c) == D_c id :', bd(K_c) == central(S, 'Dc'))
print('d(K_s) == S^2 id :', bd(K_s) == central(S, 'S2'))
# rational curve for contrast
R = parse_chain(3, 15, '⬮~~S~>⬯—>⬯~>⬯—>⬯~>⬯<—⬯<~⬯<—⬯<~⬮<—')
print('r_1(-4): ', {n: MorSpace(R, R, 0, -2).is_boundary(central(R, n)) for n in ('H', 'S2', 'Db', 'Dc')})
