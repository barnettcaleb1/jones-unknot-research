#!/usr/bin/env python3
"""
Explicit space-curve model of the Sakuma link drawn in Snape's Figure 2.2 (trefoil),
read off the 700-dpi render crossing by crossing:
  top clasp: outer strand over B, hook on the right, back under B (over strand above);
  middle clasp: upper strand under B, hook, back over B (over strand below);
  bottom hook = coil: the big-arc pair arrives under B, U-turns, returns over B;
  band self-crossing: the big-arc pair passes over the pair heading to the middle clasp;
  twist region: 4 crossings, NE-SW strand over at each.
Its Jones polynomial is compared with the pipeline's trefoil Sakuma links at
framings 0, +-1, +-2 (both chiralities).
"""
import sys
sys.path.insert(0, '/private/tmp/claude-501/-Users-calebbarnett/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/cx-sak')
import numpy as np, math
import geom, kb, templates, pipeline

def curve_from(points, spacing=0.02):
    """points: list of (x,y,z); closed; linear interpolation densified."""
    P = np.array(points, float)
    return geom.resample_uniform(P, spacing, closed=True)

def model(twist_over='NE-SW'):
    # strand heights: +1 over, -1 under, 0 neutral
    pts = []
    def add(*p):
        pts.append(p)
    # --- start: outer big-arc strand going UP to the top clasp
    add(-3.2, -1.0, 0); add(-3.3, 1.0, 0); add(-3.0, 3.0, 0); add(-2.0, 4.4, 0); add(-0.8, 5.1, 0)
    add(-0.3, 5.2, 1); add(0.0, 5.2, 1); add(0.4, 5.15, 1)      # T1: over B
    add(0.65, 5.0, 0.5); add(0.4, 4.85, -1); add(0.0, 4.8, -1); add(-0.3, 4.8, -1)   # hook, T2: under B
    # inner big-arc strand going DOWN
    add(-0.8, 4.7, 0); add(-1.9, 4.0, 0); add(-2.6, 3.0, 0); add(-2.85, 1.9, 0.0); add(-2.85, 1.2, 0.0); add(-2.9, 0.0, 0)
    add(-2.5, -2.5, 0); add(-1.6, -3.7, 0); add(-0.8, -4.1, 0)
    add(-0.3, -4.2, -1); add(0.0, -4.2, -1); add(0.3, -4.25, -1)     # C1: inner arriving strand under B
    add(0.8, -4.45, -0.5); add(1.1, -5.0, 0); add(0.8, -5.55, 0.5)   # outer U-turn
    add(0.3, -5.7, 1); add(0.0, -5.7, 1); add(-0.3, -5.7, 1)         # C2: lower return over B
    # lower strand of the bottom pair going left, then up the left side (outer strand)
    add(-1.5, -6.0, 0); add(-3.5, -6.0, 0); add(-4.8, -5.2, 0); add(-5.2, -4.0, 0); add(-5.2, -2.8, 0)
    # twist region: outer strand enters at x=-5.2 (left), crossings at y=-2.3,-1.8,-1.3,-0.8 at x=-5.0
    # strands: Q (this one, starts left) and P (starts right at x=-4.8)
    zq = []
    ys = [-2.3, -1.8, -1.3, -0.8]
    # Q goes left->right at crossing 1 (that is the "/" i.e. NE-SW direction when going up): over if twist_over=='NE-SW'
    for j, y in enumerate(ys):
        going_right = (j % 2 == 0)   # Q: left->right at crossings 1,3 ; right->left at 2,4
        is_NE_SW = going_right       # moving up and to the right = NE-SW diagonal
        over = (is_NE_SW == (twist_over == 'NE-SW'))
        zq.append(1 if over else -1)
    xs_side = [-5.2, -4.8]
    side = 0   # Q starts left
    for j, y in enumerate(ys):
        add(-5.0, y, zq[j])
        side = 1 - side
        if j < 3:
            add(xs_side[side], y + 0.25, 0)
    # after 4 crossings Q is back on the left (x=-5.2) -> becomes the UPPER strand of the pair heading up-right
    add(-5.2, -0.5, 0); add(-5.0, 0.2, 0); add(-4.3, 1.1, 0); add(-3.6, 1.7, 0)
    add(-3.2, 1.85, -1); add(-2.85, 1.95, -1); add(-2.5, 2.05, -1)   # under the big-arc pair (upper horizontal strand)
    add(-1.6, 2.35, 0); add(-0.8, 2.55, 0)
    add(-0.3, 2.6, -1); add(0.0, 2.6, -1); add(0.35, 2.58, -1)       # M1: upper strand under B
    add(0.65, 2.4, 0); add(0.35, 2.05, 1); add(0.0, 2.0, 1); add(-0.3, 2.0, 1)   # hook, M2: lower strand over B
    add(-0.8, 1.9, 0); add(-1.6, 1.7, 0)
    add(-2.5, 1.45, -1); add(-2.85, 1.35, -1); add(-3.2, 1.25, -1)   # under the big-arc pair (lower horizontal strand)
    add(-3.7, 1.0, 0); add(-4.3, 0.5, 0); add(-4.8, -0.2, 0); add(-4.8, -0.5, 0)
    # P: enters the twist region from the top on the right (x=-4.8), going DOWN through crossings 4..1
    side = 1  # P on the right at the top
    for j in reversed(range(4)):
        y = ys[j]
        if j < 3:
            pass
        add(-5.0, y, -zq[j])
        side = 1 - side
        if j > 0:
            add(xs_side[side], y - 0.25, 0)
    # after the twists P is on the right (x=-4.8) at the bottom -> inner strand of the bottom pair
    add(-4.8, -2.8, 0); add(-4.8, -4.0, 0); add(-4.4, -5.0, 0); add(-3.5, -5.5, 0); add(-1.5, -5.5, 0)
    add(-0.3, -5.3, 1); add(0.0, -5.3, 1); add(0.3, -5.3, 1)          # C3: upper return strand over B (traversed backwards)
    add(0.55, -5.15, 0.5); add(0.7, -5.0, 0); add(0.55, -4.75, -0.5)  # inner U-turn
    add(0.3, -4.6, -1); add(0.0, -4.6, -1); add(-0.3, -4.6, -1)       # C4: outer arriving strand under B
    add(-0.8, -4.5, 0); add(-1.7, -4.0, 0); add(-2.8, -2.6, 0)
    # close: back to start (-3.2,-1.0)
    return curve_from(pts)

if __name__ == '__main__':
    Bx = np.array([(0, -8, 0), (0, 8, 0), (-12, 8, 0), (-12, -8, 0)], float)
    Bx = geom.resample_uniform(Bx, 0.2, closed=True)
    results = {}
    for tw in ('NE-SW', 'NW-SE'):
        L = model(tw)
        for rot in (pipeline.ROT_Q1, pipeline.ROT_Q2):
            pd, signs, comps, lk, xs = geom.pd_from_curves([Bx, L], rot, return_info=True)
            V, w, mx = kb.jones_from_pd(pd, signs=signs)
            nBL = sum(1 for x in xs if x['ci'] != x['cj']); nLL = len(xs) - nBL
            print("Fig2.2 model (twist over %s): %d crossings (B-L %d, L-L %d) lk=%g  V=%s" % (tw, len(pd), nBL, nLL, lk[0, 1], kb.jones_str(V)))
            print("    J(q) =", kb.poly_str_q(kb.jones_to_snape_q(V)))
            results[(tw, id(rot))] = V
        # also check L alone is an unknot
        pdL, sL, cL, lkL = geom.pd_from_curves([L], pipeline.ROT_Q1)
        VL, wL, _ = kb.jones_from_pd(pdL, signs=sL)
        print("    L alone Jones =", kb.jones_str(VL))
    # pipeline trefoil Sakuma links at framings -2..2 (I_1(1;1) = right-handed trefoil diagram, writhe 3)
    wp, mk, meta = templates.build_I1([1], [1], rot_side=True)
    fr = {}
    for n in (-2, -1, 0, 1, 2):
        r = pipeline.run('tref_I1_1_1_framing%d' % n, wp, mk, meta, verbose=False, framing=n)
        fr[n] = r['VS']
        print("pipeline trefoil framing %2d: V_S = %s" % (n, kb.jones_str(r['VS'])))
    for key, V in results.items():
        for n, Vn in fr.items():
            if V == Vn:
                print("MATCH: Fig2.2 model %s == pipeline framing %d" % (key[0], n))
            if V == kb.mirror(Vn):
                print("MATCH: Fig2.2 model %s == mirror of pipeline framing %d" % (key[0], n))
