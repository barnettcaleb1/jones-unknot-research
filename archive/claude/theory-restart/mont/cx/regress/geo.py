"""Exact free-group geometry of the two halves of a width-two junction (Artin action of the type-B_4 group on F_5, fgroup.py).
Junction sphere S: punctures g0 (axis), g1..g4 (legs 0..3); E = top end of the axis (loop (g0..g4)^-1).
TOP  half T_V = (axis + caps (0,1),(2,3)) followed by V: complement group F_3, psi_V = psi_0 o V_*^-1, psi_0 = (a, b, b^-1, c, c^-1)
     (engineB orbit_search conventions; same_tangle validated there on 700,000 tangles).
BOTTOM half B_U = U followed by the u2.u2 closure: in the complementary ball the closure is a planar forest = tree
     {axis puncture - v_bot - v_top - E, v_bot - leg 0, v_top - c - leg 3} + cup (legs 1,2); complement = genus-4 handlebody,
     pi_1 = F_4 = F_5 / <<g2 g3>>, phi_0 = (a, b, c, c^-1, d); loops at the junction are pushed DOWN through U:
     phi_U = phi_0 o U_*  (U_* = U_k* ... U_1*, first letter first; inverse of the top's pull-up convention).
Disc criteria (Dehn's lemma; curve on the boundary, null-homotopic in the complement => bounds an embedded disc):
     X1^2 acts trivially on a half  <=  c01 = g1 g2 dies;   X3^2  <=  c23 = g3 g4 dies;
     axis split off the two arcs of the TOP  <=  c0123 = g1 g2 g3 g4 dies (then X1 X3^-1 acts trivially: flype of a rational tangle)."""
import sys
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/orig')
import fgroup
INV = {'x0': 'y0', 'y0': 'x0', 'x1': 'y1', 'y1': 'x1', 'x2': 'y2', 'y2': 'x2', 'x3': 'y3', 'y3': 'x3'}
INVIMG = {L: [fgroup.act(INV[L], (j + 1,)) for j in range(5)] for L in INV}
PSI0 = [(1,), (2,), (-2,), (3,), (-3,)]
PHI0 = [(1,), (2,), (3,), (-3,), (4,)]
C01, C23, C0123, C12 = (2, 3), (4, 5), (2, 3, 4, 5), (3, 4)
def subst(images, w):
    out = []
    for s in w:
        img = images[abs(s) - 1]
        out.extend(img if s > 0 else fgroup.inv(img))
    return fgroup.red(out)
def psi_top(V):
    psi = PSI0
    for L in V: psi = [subst(psi, INVIMG[L][j]) for j in range(5)]
    return psi
def push_down(U, w):
    for L in U: w = fgroup.act(L, w)
    return w
def phi_bot(U):
    """images of g0..g4 under phi_U = phi_0 o U_*"""
    return [subst(PHI0, push_down(U, (j + 1,))) for j in range(5)]
def top_tests(V):
    psi = psi_top(V)
    return {'c01': subst(psi, C01) == (), 'c23': subst(psi, C23) == (), 'c0123': subst(psi, C0123) == (), 'c12': subst(psi, C12) == ()}
def bot_tests(U):
    ph = phi_bot(U)
    return {'c01': subst(ph, C01) == (), 'c23': subst(ph, C23) == (), 'c0123': subst(ph, C0123) == (), 'c12': subst(ph, C12) == ()}
def twist_word(m, n):
    return (['x1', 'x1'] * m if m > 0 else ['y1', 'y1'] * (-m)) + (['x3', 'x3'] * n if n > 0 else ['y3', 'y3'] * (-n))
def top_same(V1, V2):
    """exact kernel test (engineB): T_V1 == T_V2 as 3-D tangles"""
    a = fgroup.group_key(V1)                     # images of all generators under V1_*
    c1 = subst(list(a), (2, 3)); c2 = subst(list(a), (4, 5))   # V1_*(c1), V1_*(c2)
    psi2 = psi_top(V2)
    return subst(psi2, c1) == () and subst(psi2, c2) == ()
def bot_same(U1, U2):
    """kernel inclusion test on the bottom: K_U1 = <<U1_*^-1(g2 g3)>>, test phi_U2 kills it (Hopfian F_4 => equal kernels)."""
    # U1_*^-1 (g2 g3): pull the cup curve up through U1 (inverse letters in reverse order)
    w = (3, 4)
    for L in reversed(U1): w = fgroup.act(INV[L], w)
    return subst(phi_bot(U2), w) == ()
if __name__ == '__main__':
    # sanity of conventions
    print('top  caps        ', top_tests([]))
    print('top  x2.x1 (nested caps (0,3),(1,2))', top_tests(['x2', 'x1']))
    print('top  x2          ', top_tests(['x2']))
    print('top  x0          ', top_tests(['x0']))
    print('top  x2.x1 vs x2.x1.x1.y3 (X1 X3^-1 on nested caps):', top_same(['x2', 'x1'], ['x2', 'x1', 'x1', 'y3']))
    print('top  x2.x1 vs x2.x1.x1  (X1 alone):', top_same(['x2', 'x1'], ['x2', 'x1', 'x1']))
    print('bot  closure     ', bot_tests([]))
    print('bot  x2.x1       ', bot_tests(['x2', 'x1']), '  (cup pulled to legs 0,1 under leg 2)')
    print('bot  x1.x2       ', bot_tests(['x1', 'x2']))
    print('bot  x2          ', bot_tests(['x2']))
    print('bot  x1          ', bot_tests(['x1']))
    print('bot  x3.x2       ', bot_tests(['x3', 'x2']))
    print('bot  y2.y3       ', bot_tests(['y2', 'y3']))
