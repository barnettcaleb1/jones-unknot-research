import sympy as S
from annulus_eval import E_minus, E_plus, mod_phi5, Q
# closure of e_1 on 2 strands = one contractible loop (winding 0); compare with d_-, d_+
em = E_minus([('e',0)], 2); ep = E_plus([('e',0)], 2)
print('E-(closure e) == d_- :', S.simplify(em - (1 - Q - 1/Q)) == 0, '| E+(closure e) == d_+ :', S.simplify(ep - (Q + 1/Q)**2) == 0)
# A_1 * contractible loop: closure of e on strands 0,1 with strand 2 straight
em = E_minus([('e',0)], 3); ep = E_plus([('e',0)], 3)
print('E-(A1 . loop) == d_- L_1^- :', S.simplify(em - (1-Q-1/Q)*(Q**2+1+Q**-2)) == 0, '| E+ == d_+ L_1^+ :', S.simplify(ep - (Q+1/Q)**2*(-Q-1/Q)) == 0)
# winding-0 knotted-ish component: e_1 s_2 s_2 e_1 etc. on 3 strands
for D in ([('e',0),('s',1,1),('s',1,1),('e',0)], [('s',0,1),('e',1),('s',0,-1),('s',1,1)], [('e',1),('s',0,1),('s',0,1),('s',0,1),('e',1)]):
    em = E_minus(D,3); ep = E_plus(D,3)
    print(D, 'equal at zeta5:', mod_phi5(em-ep) == 0, '| integral Laurent in Q:', all(c.is_integer for c in S.Poly(S.expand(em*Q**40), Q).coeffs()))
