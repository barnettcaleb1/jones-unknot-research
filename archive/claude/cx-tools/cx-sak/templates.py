#!/usr/bin/env python3
"""
templates.py -- symmetric planar diagrams for Snape/Sakuma templates I_1(alpha_1..alpha_m; c_1..c_m),
m = 1 or 2, following the port wiring of work/next_theory/sakuma_template.md and
work/global_design/c2_sakuma_recipe.md (section 1):

  1. alpha_1 top-side    -> (-c_1) near-upper
  2. alpha_1 bottom-side -> (-c_1) near-lower
  3. (-c_1) far-upper    -> (-c_2) near-upper
  4. (-c_1) far-lower    -> alpha_2 top-side
  5. alpha_2 bottom-side -> (-c_2) near-lower
  6. far-upper ports of the outer boxes joined by the exterior upper arc, far-lower
     ports by the exterior lower arc (the two arcs cross the axis at the fixed points).

Axis = y-axis.  Glyph convention (Snape p.21): a positive box label means the
NW-SE strand is over at each crossing, negative means the NE-SW strand is over.
For the horizontal side boxes the flag rot_side selects whether the glyph is used
upright (rot_side=False: positive -> NW-SE over) or rotated with the box
(rot_side=True: positive -> NE-SW over).  Which one reproduces Sakuma's knots is
fixed by calibration (I_1(2;1) must be the figure-eight), see REPORT.

Output: a closed waypoint list (traversed along the knot) and crossing markers
(x, y, over-direction), mirror-symmetric about x = 0.
"""
import numpy as np

W = 0.5     # half separation of the two strands in a twist box
S = 1.0     # spacing of crossings in a twist box


def vertical_box(name, k, label_sign, x0, y_top):
    """Vertical two-strand twist box on the axis x = x0 with k crossings.
    Strand A enters top-left, strand B enters top-right.  Returns arcs, markers, ports."""
    arcs = {}
    ptsA, ptsB = [(x0 - W, y_top)], [(x0 + W, y_top)]
    markers = []
    for j in range(1, k + 1):
        yc = y_top - j * S
        ptsA.append((x0, yc)); ptsB.append((x0, yc))
        if j < k:
            ym = y_top - (j + 0.5) * S
            sideA = +1 if j % 2 == 1 else -1
            ptsA.append((x0 + sideA * W, ym)); ptsB.append((x0 - sideA * W, ym))
        # over direction: positive label -> NW-SE strand over, i.e. direction (1,-1)
        markers.append((x0, yc, (1.0, -1.0) if label_sign > 0 else (1.0, 1.0)))
    y_bot = y_top - (k + 1) * S
    sideA_end = +1 if k % 2 == 1 else -1
    ptsA.append((x0 + sideA_end * W, y_bot)); ptsB.append((x0 - sideA_end * W, y_bot))
    endA = name + ('.BR' if sideA_end > 0 else '.BL')
    endB = name + ('.BL' if sideA_end > 0 else '.BR')
    arcs[name + '.sA'] = (name + '.TL', endA, ptsA)
    arcs[name + '.sB'] = (name + '.TR', endB, ptsB)
    ports = {name + '.TL': (x0 - W, y_top), name + '.TR': (x0 + W, y_top),
             name + '.BL': (x0 - W, y_bot), name + '.BR': (x0 + W, y_bot)}
    return arcs, markers, ports, y_bot


def horizontal_box(name, k, label_sign, x_near, y0, side, rot_side):
    """Horizontal two-strand twist box; side=+1 right of the axis (strands run from
    near=left to far=right), side=-1 is the mirror image (near=right end)."""
    arcs = {}
    sgn = side
    def X(x):  # mirror for the left side
        return sgn * x
    ptsU, ptsL = [(X(x_near), y0 + W)], [(X(x_near), y0 - W)]
    markers = []
    for j in range(1, k + 1):
        xc = x_near + j * S
        ptsU.append((X(xc), y0)); ptsL.append((X(xc), y0))
        if j < k:
            xm = x_near + (j + 0.5) * S
            sideU = -1 if j % 2 == 1 else +1   # U strand is below after odd crossings
            ptsU.append((X(xm), y0 + sideU * W)); ptsL.append((X(xm), y0 - sideU * W))
        if rot_side:
            d = (1.0, 1.0) if label_sign > 0 else (1.0, -1.0)
        else:
            d = (1.0, -1.0) if label_sign > 0 else (1.0, 1.0)
        markers.append((X(xc), y0, d))   # glyph is tau-invariant: same direction on both sides
    x_far = x_near + (k + 1) * S
    sideU_end = -1 if k % 2 == 1 else +1
    ptsU.append((X(x_far), y0 + sideU_end * W)); ptsL.append((X(x_far), y0 - sideU_end * W))
    endU = name + ('.FL' if sideU_end < 0 else '.FU')
    endL = name + ('.FU' if sideU_end < 0 else '.FL')
    arcs[name + '.sU'] = (name + '.NU', endU, ptsU)
    arcs[name + '.sL'] = (name + '.NL', endL, ptsL)
    ports = {name + '.NU': (X(x_near), y0 + W), name + '.NL': (X(x_near), y0 - W),
             name + '.FU': (X(x_far), y0 + W), name + '.FL': (X(x_far), y0 - W)}
    return arcs, markers, ports, x_far


def mirror_pts(pts):
    return [(-x, y) for (x, y) in pts]


def build_I1(alphas, cs, rot_side=False, gap=3.0, x1=2.5, cgap=4.0):
    """I_1(alpha_1..alpha_m; c_1..c_m).  Boxes: central alpha_j (vertical, on axis),
    side boxes labelled -c_j (horizontal).  Returns (waypoints, markers, meta)."""
    m = len(alphas)
    assert m in (1, 2) and len(cs) == m
    arcs = {}
    markers = []
    ports = {}
    # central boxes
    k1 = abs(alphas[0])
    a, mk, po, y1_bot = vertical_box('A1', k1, np.sign(alphas[0]), 0.0, 0.0)
    arcs.update(a); markers += mk; ports.update(po)
    Yc = -(k1 + 1) / 2.0
    if m == 2:
        k2 = abs(alphas[1])
        y2_top = y1_bot - gap
        a, mk, po, y2_bot = vertical_box('A2', k2, np.sign(alphas[1]), 0.0, y2_top)
        arcs.update(a); markers += mk; ports.update(po)
    # side boxes, labels -c_j
    for side, sname in ((+1, 'R'), (-1, 'L')):
        kc1 = abs(cs[0])
        a, mk, po, xf1 = horizontal_box(sname + '.C1', kc1, -np.sign(cs[0]), x1, Yc, side, rot_side)
        arcs.update(a); markers += mk; ports.update(po)
        if m == 2:
            kc2 = abs(cs[1])
            x2 = xf1 + cgap
            a, mk, po, xf2 = horizontal_box(sname + '.C2', kc2, -np.sign(cs[1]), x2, Yc, side, rot_side)
            arcs.update(a); markers += mk; ports.update(po)
    xf1 = x1 + (abs(cs[0]) + 1) * S
    x_far = xf1 if m == 1 else (xf1 + cgap + (abs(cs[1]) + 1) * S)
    Y_TOP = 2.5
    if m == 1:
        Y_BOT = y1_bot - 2.5
    else:
        Y_BOT = y2_bot - 2.5
    # connectors, right side then mirrored
    conn = {}
    # 1. A1.TR -> C1.NU
    conn['c1'] = ('A1.TR', '.C1.NU', [(W, 0.0), (0.9, 0.7), (x1 - 1.2, Yc + W + 0.15), (x1 - 0.6, Yc + W), (x1, Yc + W)])
    # 2. A1.BR -> C1.NL
    conn['c2'] = ('A1.BR', '.C1.NL', [(W, y1_bot), (0.9, y1_bot - 0.6), (x1 - 1.2, Yc - W - 0.15), (x1 - 0.6, Yc - W), (x1, Yc - W)])
    if m == 1:
        conn['top'] = ('.C1.FU', 'TOPFIX', [(xf1, Yc + W), (xf1 + 0.8, Yc + W), (xf1 + 1.6, Yc + W + 0.8), (xf1 + 1.6, Y_TOP - 0.8), (xf1 + 0.8, Y_TOP), (2.0, Y_TOP), (1.0, Y_TOP), (0.0, Y_TOP)])
        conn['bot'] = ('.C1.FL', 'BOTFIX', [(xf1, Yc - W), (xf1 + 0.8, Yc - W), (xf1 + 2.4, Yc - W - 0.8), (xf1 + 2.4, Y_BOT + 0.8), (xf1 + 0.8, Y_BOT), (2.0, Y_BOT), (1.0, Y_BOT), (0.0, Y_BOT)])
    else:
        x2 = xf1 + cgap
        xf2 = x_far
        # 3. C1.FU -> C2.NU (straight)
        conn['c3'] = ('.C1.FU', '.C2.NU', [(xf1, Yc + W), (xf1 + 0.5 * cgap, Yc + W), (x2, Yc + W)])
        # 4. C1.FL -> A2.TR
        conn['c4'] = ('.C1.FL', 'A2.TR', [(xf1, Yc - W), (xf1 + 0.8, Yc - W), (xf1 + 1.2, Yc - W - 0.8), (xf1 + 1.2, y2_top + 2.0),
                                          (xf1 + 0.8, y2_top + 1.4), (1.6, y2_top + 1.2), (0.8, y2_top + 0.7), (W, y2_top)])
        # 5. A2.BR -> C2.NL
        conn['c5'] = ('A2.BR', '.C2.NL', [(W, y2_bot), (0.8, y2_bot - 0.7), (1.6, y2_bot - 1.2), (x2 - 1.6, y2_bot - 1.2), (x2 - 0.8, y2_bot - 0.6),
                                          (x2 - 0.8, Yc - W - 1.0), (x2 - 0.5, Yc - W - 0.1), (x2, Yc - W)])
        conn['top'] = ('.C2.FU', 'TOPFIX', [(xf2, Yc + W), (xf2 + 0.8, Yc + W), (xf2 + 1.6, Yc + W + 0.8), (xf2 + 1.6, Y_TOP - 0.8), (xf2 + 0.8, Y_TOP), (2.0, Y_TOP), (1.0, Y_TOP), (0.0, Y_TOP)])
        conn['bot'] = ('.C2.FL', 'BOTFIX', [(xf2, Yc - W), (xf2 + 0.8, Yc - W), (xf2 + 2.4, Yc - W - 0.8), (xf2 + 2.4, Y_BOT + 0.8), (xf2 + 0.8, Y_BOT), (2.0, Y_BOT), (1.0, Y_BOT), (0.0, Y_BOT)])
    # instantiate right and left copies
    for key, (p, q, pts) in conn.items():
        for side, sname in ((+1, 'R'), (-1, 'L')):
            def nm(port):
                if port in ('TOPFIX', 'BOTFIX'):
                    return port
                if port.startswith('.'):
                    return sname + port
                # alpha box ports: side-specific left/right
                box, pp = port.split('.')
                if side < 0:
                    pp = pp.replace('R', 'L') if pp.endswith('R') else pp.replace('L', 'R')
                return box + '.' + pp
            arcs[sname + '.' + key] = (nm(p), nm(q), pts if side > 0 else mirror_pts(pts))
    # trace the knot: start at TOPFIX going along R.top backwards (from the fixed point to the right)
    port_arcs = {}
    for aname, (p, q, pts) in arcs.items():
        port_arcs.setdefault(p, []).append((aname, 'fwd'))
        port_arcs.setdefault(q, []).append((aname, 'bwd'))
    for port, lst in port_arcs.items():
        if port in ('TOPFIX', 'BOTFIX'):
            assert len(lst) == 2, (port, lst)
        else:
            assert len(lst) == 2, ("port %s has %d arcs" % (port, len(lst)), lst)
    waypoints = []
    cur_arc, direction = 'R.top', 'bwd'   # from TOPFIX (its q end) to R.C2.FU (p end)
    visited = set()
    while True:
        p, q, pts = arcs[cur_arc]
        seq = list(pts) if direction == 'fwd' else list(reversed(pts))
        end_port = q if direction == 'fwd' else p
        visited.add(cur_arc)
        waypoints += seq[:-1]   # drop the last point: the next arc starts there
        # next arc at end_port
        nxt = [(a, d) for (a, d) in port_arcs[end_port] if a != cur_arc]
        assert len(nxt) == 1, (end_port, port_arcs[end_port], cur_arc)
        cur_arc, d = nxt[0]
        direction = 'fwd' if d == 'fwd' else 'bwd'
        if cur_arc in visited:
            break
    assert visited == set(arcs), (set(arcs) - visited)
    meta = dict(Y_TOP=Y_TOP, Y_BOT=Y_BOT, x_far=x_far, nmarkers=len(markers))
    return waypoints, markers, meta


def build_custom_trefoil(sign=+1):
    """Snape Fig. 2.2-style symmetric trefoil: one on-axis crossing at the bottom, two
    side crossings, fixed points on the top arc and the middle arc.  Built as the
    template I_1(1; -1*sign) which has exactly that shape (1 central + 2 side crossings)."""
    return build_I1([sign * 1], [-sign * 1], rot_side=False)
