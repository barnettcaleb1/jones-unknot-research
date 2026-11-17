# kernel.md 2.4: "for f = [T_g1, T_g2], kappa_f is in F_4 iff (2D_20 - 1)u_1 - (2D_10 - 1)u_2 lies in Q u_0".
# Referee claim: <w, u_0> = 0 identically, so the condition forces w = 0, i.e. u_1 = +-u_2; for two separating
# twists with DIFFERENT splittings it never holds, so kappa' = [T_gamma0, [T_g1, T_g2]] sits in F_3 minus F_4.
# One sanity instance (T-normalisation kappa' = [(s1 s2)^6, f]; exponent sums are 0, so bracket scalars cancel).
import sys
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/g2-proof/ref-kernel')
from ref_check import rho, ord_matrix, inv, D
Tc2 = [1, 2]*6
g1, g2 = [3], [4, 3]                                   # d_i = g_i(c0)
T1 = g1 + Tc2 + inv(g1); T2 = g2 + Tc2 + inv(g2)      # separating twists T_{d_i}^2 in SI
print("D(c0,d1), D(c0,d2) =", D(g1, 1), D(g2, 1))
f = T1 + T2 + inv(T1) + inv(T2)
k2 = Tc2 + f + inv(Tc2) + inv(f)
k1 = [1, 2]*3 + f + inv([1, 2]*3) + inv(f)
print("ord(rho(f) - I)                 =", ord_matrix(rho(f)), "  (expect 2: f in F_2 \\ F_3)")
print("ord(rho([(s1 s2)^6, f]) - I)    =", ord_matrix(rho(k2)), "  (kernel.md: >= 4 iff its condition holds; referee: exactly 3)")
print("ord(rho([(s1 s2)^3, f]) - I)    =", ord_matrix(rho(k1)), "  (half-twist form: one lower)")
