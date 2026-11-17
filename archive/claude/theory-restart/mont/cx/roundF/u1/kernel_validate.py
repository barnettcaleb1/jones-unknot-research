"""kernel_validate.py -- validation of gen_kernel.py.
(1) N = 10 setting of code/tangle_kernel.py (hw = 5, TOP (1,2),(3,4),(5,6),(7,8), BOT (0,1),(2,3),(4,5),(6,7),(8,9)):
    same_top / same_bottom agree with tangle_kernel on 3,000 random pairs (incl. pairs differing by a random letter).
(2) S2 picture (hw = 3, caps of s.l2, cups of u1 + u0, pairs read off alex.symmetrize here, not assumed):
    known stabilisers: top x0, y0 (legs of the s-cap), x2 (legs of both l2 caps); bottom x1 (legs of the u1 cups);
    known non-stabilisers: top x1; bottom x0, x2.
(3) pairs re-derived from alex.symmetrize of 's.l2.u1'."""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, 'code'))
import gen_kernel as G, tangle_kernel as TK
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools'); import alex
P10 = G.Picture(5, TK.TOP_PAIRS, TK.BOT_PAIRS)
rng = random.Random(5); LET = ['%s%d' % (c, i) for c in 'xy' for i in range(4)]
agree = tot = eq = 0
for it in range(3000):
    a = [rng.choice(LET) for _ in range(rng.randint(0, 6))]
    b = a + [rng.choice(LET)] if it % 2 else [rng.choice(LET) for _ in range(rng.randint(0, 6))]
    r1 = (P10.same_top(a, b), P10.same_bottom(a, b)); r2 = (TK.same_top(a, b), TK.same_bottom(a, b))
    tot += 1; agree += (r1 == r2); eq += r1[0] + r1[1]
print('(1) N=10 agreement with tangle_kernel:', agree, '/', tot, ' (equal-tangle answers among them:', eq, ')')
P = G.S2PIC
tests = [('top', 'x0', True), ('top', 'y0', True), ('top', 'x2', True), ('top', 'y2', True), ('top', 'x1', False), ('top', 'y1', False),
         ('bot', 'x1', True), ('bot', 'y1', True), ('bot', 'x0', False), ('bot', 'x2', False), ('bot', 'y0', False)]
ok = 0
for side, L, exp in tests:
    got = P.same_top([], [L]) if side == 'top' else P.same_bottom([], [L])
    ok += (got == exp); print('   ', side, L, 'stabiliser' if got else 'not', '(expected %s)' % exp)
print('(2) known (non-)stabilisers:', ok, '/', len(tests))
full = alex.symmetrize(alex.parse('s.l2.u1')); print('(3) alex.symmetrize(s.l2.u1) =', full)
