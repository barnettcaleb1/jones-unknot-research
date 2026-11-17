"""(d) template 2 at (0,0); (e) unit point (-2,-1): word reduction, covering knot, the local four-plat L, det(L)."""
import sys
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/referee/width2-window')
from r2lib import *
from r2_knot import *
# ---- (d) ----
TEMPL = {1: ('x0.y2.y2.x1.x1', 'x1.x1.y0.x1'), 2: ('y0.y2.y1.x0.x3.y2', 'y3.x2.x2.y3.x0.x1')}
for k in (1, 2):
    W = body(*TEMPL[k], 0, 0); J = lp.J(halfword(W))
    print('T%d (0,0): J - 1 =' % k, sp.factor(S(J) - 1), '   [halfword %s]' % halfword(W))
# ---- (e) word reduction ----
W = body(*TEMPL[1], -2, -1)
print('\nT1 body at (-2,-1):', '.'.join(W))
red = 'y2.y2.y3.y3.x1'
print('lp.J(full body) =', lp.J(halfword(W)), ' lp.J(reduced) =', lp.J('s.l1.l1.' + red + '.u2.u2'))
# reduce mechanically with free cancellation + far commutation in the type-B Artin group
def reduce_word(w):
    w = list(w)
    def idx(L): return int(L[1:])
    def inv(L): return ('y' if L[0] == 'x' else 'x') + L[1:]
    def commute(a, b):
        i, j = idx(a), idx(b)
        if i == 0 or j == 0: return (i == 0 and j >= 2) or (j == 0 and i >= 2)
        return abs(i - j) >= 2
    changed = True
    while changed:
        changed = False
        for p in range(len(w)):
            for q in range(p + 1, len(w)):
                if w[q] == inv(w[p]) and all(commute(w[p], w[r]) for r in range(p + 1, q)):
                    del w[q]; del w[p]; changed = True; break
                if not commute(w[p], w[q]): break
            if changed: break
    return w
print('reduced by free cancellation + far commutation:', '.'.join(reduce_word(W)))
# ---- (e) the covering knot of the reduced and of the unreduced word: my own symmetric diagram ----
for name, word in [('reduced', 's.l1.l1.' + red + '.u2.u2'), ('unreduced', halfword(W))]:
    ops = symmetric_ops(parse(word))
    cr = build(ops)
    br = bracket_sweep(ops)
    print('\ncovering knot (%s): crossings %d, components %d, bracket = %s' % (name, len(cr), components(cr), sp.factor(br)))
    dt, _ = det_coloring(cr)
    print('   det (coloring minor) =', dt, ' writhe =', writhe(cr))
    if len(cr) <= 12:
        print('   Alexander =', alexander(cr)[0])
    else:
        rows, n = arcs_and_rows(cr)
        for tv in (2, 3, 5):
            Mx = sp.zeros(len(rows), n)
            for r, (o, ui, uo, s) in enumerate(rows):
                if s == 1:
                    Mx[r, o] += 1 - tv; Mx[r, ui] += tv; Mx[r, uo] += -1
                else:
                    Mx[r, o] += tv - 1; Mx[r, ui] += 1; Mx[r, uo] += -tv
            print('   |Delta(%d)| (minor, up to unit) =' % tv, abs(Mx[:-1, :-1].det()))
# ---- (e) the local four-plat L ----
def plat(top, braid, bottom):
    """top/bottom: list of cap/cup ops; braid: list of (i,s) with 1-based sigma_i^s -> crossing at positions i-1,i"""
    return top + [('X', i - 1, s) for i, s in braid] + bottom
# top caps (12),(34): caps at 0 then at 2 ; bottom cups (14),(23): cup 1 (inner 2-3) then cup 0 (outer 1-4)
L_ops = plat([('cap', 0), ('cap', 2)], [(2, -1), (2, -1), (3, -1), (3, -1), (1, 1)], [('cup', 1), ('cup', 0)])
crL = build(L_ops)
brL = bracket_sweep(L_ops)
dL, ML = det_coloring(crL)
print('\nL = plat(top 12/34; sigma2^-2 sigma3^-2 sigma1; bottom 14/23): crossings', len(crL), 'components', components(crL))
print('   bracket <L> =', sp.factor(brL), ' writhe', writhe(crL))
print('   det(L) =', dL, '   Alexander(L) =', alexander(crL)[0])
print('   coloring matrix rows:', ML.tolist())
# both relative sign choices for sigma1 (to show the conclusion uses the right one)
for s1 in (1, -1):
    ops = plat([('cap', 0), ('cap', 2)], [(2, -1), (2, -1), (3, -1), (3, -1), (1, s1)], [('cup', 1), ('cup', 0)])
    print('   variant sigma1^%+d: det =' % s1, det_coloring(build(ops))[0], ' bracket =', sp.factor(bracket_sweep(ops)))
# the right half alone (closed along the axis) of the reduced word, read directly by my symmetric construction minus mirror:
# right-half diagram: axis-closure: top: arc (axis..c) outer, caps legs (0,1),(2,3); bottom: cup (1,2), cup (3,c), cup (axis,0)
R_ops = [('cap', 0), ('cap', 1), ('cap', 1)]   # positions: [axis, l0, l1, l2, l3, c] after caps -> check below
# build explicitly: start with outer arc (axis, c) = cap at 0 -> positions [ax, c]; caps between: cap at 1 -> [ax, a, a, c]; cap at 1 -> [ax, b, b, a, a, c]
R_ops += [('X', 2 + 1 - 1, -1)] * 0
legs = {'x': 1, 'y': -1}
body_ops = []
for c, s in parse(red):
    body_ops.append(('X', 1 + s - 1, legs[c]))   # leg j at position 1+j; x_s crosses legs s-1,s
R_ops = [('cap', 0), ('cap', 1), ('cap', 1)] + body_ops + [('cup', 2), ('cup', 2), ('cup', 0)]
crR = build(R_ops)
print('\nright half closed along the axis (direct): crossings', len(crR), 'components', components(crR), 'det', det_coloring(crR)[0],
      'bracket', sp.factor(bracket_sweep(R_ops)))
# ---- Codex's PD code and minor ----
pd = [[0, 3, 4, 2], [3, 5, 6, 4], [6, 7, 8, 2], [10, 8, 7, 9], [5, 0, 10, 9]]
print('\nCodex PD code: bracket =', sp.factor(pd_bracket(pd)))
Mc = sp.Matrix([[2, -1, -1, 0], [-1, 0, 2, -1], [-2, 1, 0, 1], [1, -2, 0, 0]])
print('Codex minor det =', Mc.det())
