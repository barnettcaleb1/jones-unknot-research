"""Rewrite rules for halfwords s.l1.l1.W.u2.u2 (W over x0,y0,..,x3,y3).  Letters encoded as ints: x_g -> g+1, y_g -> -(g+1).
Every rule is an isotopy of the covering knot K (see REPORT section 1); every group rule is checked with the exact Artin
action (engineB/fgroup.py) and every end rule against the rho_2 scalars (scalars.py)."""
import itertools
NAME = {1: 'x0', -1: 'y0', 2: 'x1', -2: 'y1', 3: 'x2', -3: 'y2', 4: 'x3', -4: 'y3'}
CODE = {v: k for k, v in NAME.items()}
def enc(word):
    if isinstance(word, str): word = [x for x in word.split('.') if x]
    return tuple(CODE[x] for x in word)
def dec(w): return '.'.join(NAME[a] for a in w)
def inv(w): return tuple(-a for a in reversed(w))
def gen(a): return abs(a) - 1
COMM = {frozenset((0, 2)), frozenset((0, 3)), frozenset((1, 3))}
def commute(a, b): return frozenset((gen(a), gen(b))) in COMM
# ---- length-preserving group rules (pairs; used in both directions) ----
LP = []
for a in (1, 2, 3, 4):
    for b in (1, 2, 3, 4):
        if frozenset((a - 1, b - 1)) in COMM:
            for sa in (1, -1):
                for sb in (1, -1):
                    LP.append(('C', (sa * a, sb * b), (sb * b, sa * a)))
for i, j in ((2, 3), (3, 2), (3, 4), (4, 3)):       # codes of generators 1,2 / 2,3
    LP += [('B', (i, j, i), (j, i, j)), ('B', (-i, -j, -i), (-j, -i, -j)),
           ('B', (i, j, -i), (-j, i, j)), ('B', (-i, j, i), (j, i, -j)),
           ('B', (i, -j, -i), (-j, -i, j)), ('B', (-i, -j, i), (j, -i, -j))]
a, b = 1, 2                                          # tau = x0, sigma_1 = x1 : abab = baba
LP += [('T', (a, b, a, b), (b, a, b, a)), ('T', (-a, -b, -a, -b), (-b, -a, -b, -a)),
       ('T', (-a, b, a, b), (b, a, b, -a)), ('T', (-b, a, b, a), (a, b, a, -b)),
       ('T', (-b, -a, -b, a), (a, -b, -a, -b)), ('T', (-a, -b, -a, b), (b, -a, -b, -a)),
       ('T', (b, a, b, a), (a, b, a, b)), ('T', (-b, -a, -b, -a), (-a, -b, -a, -b))]
# ---- end absorption rules ----
# TOP (prefix s.l1.l1 : caps A = legs (0,1), B = legs (2,3); axis from the top vertex): delete a PREFIX of W equal to
TOPPAT = [((2,), 'R1 cap A'), ((-2,), 'R1 cap A'), ((4,), 'R1 cap B'), ((-4,), 'R1 cap B'),
          ((3, 2, 4, 3), 'Hilden exchange A over B'), ((3, 4, 2, 3), 'Hilden exchange A over B'),
          ((-3, -2, -4, -3), 'Hilden exchange A under B'), ((-3, -4, -2, -3), 'Hilden exchange A under B'),
          ((3, 2, 2, 3), 'Hilden loop: leg 2 around cap A'), ((-3, -2, -2, -3), 'Hilden loop: leg 2 around cap A'),
          ((3, 4, 4, 3), 'Hilden loop: leg 1 around cap B'), ((-3, -4, -4, -3), 'Hilden loop: leg 1 around cap B'),
          ((1, 2, 1), 'axis exchange of the two lifts of cap A (= axis loop around A, mod R1)'),
          ((-1, -2, -1), 'axis exchange of the two lifts of cap A (= axis loop around A, mod R1)')]
# BOT (suffix u2.u2 : bottom vertex on leg 0, cup C = legs (1,2), leg 3 -> c): delete a SUFFIX of W equal to
BOTPAT = [((1,), 'R1 at the bottom vertex (axis crossing over cup u0)'), ((-1,), 'R1 at the bottom vertex'),
          ((3,), 'R1 cup C'), ((-3,), 'R1 cup C'),
          ((2, 3, 3, 2), 'Hilden loop: leg 0 around cup C'), ((-2, -3, -3, -2), 'Hilden loop: leg 0 around cup C'),
          ((4, 3, 3, 4), 'Hilden loop: leg 3 around cup C'), ((-4, -3, -3, -4), 'Hilden loop: leg 3 around cup C'),
          ((2, 1, 2, 3, 2, 1, 2), 'Hilden: exchange of the two lifts of cup C over the bottom-vertex cup u0 (= E23,45 E45,67 E23,45 in B_8)'),
          ((-2, -1, -2, -3, -2, -1, -2), 'Hilden: exchange of the two lifts of cup C under the bottom-vertex cup u0 (inverse)')]
def crossings(w): return sum(1 if abs(a) == 1 else 2 for a in w)
