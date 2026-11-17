#!/usr/bin/env python3
"""Basic tests of the first-order obstruction (my code): unit square, zigzags, composable junctions, squares with
D^2 sides and with legs P_1, P_3."""
from tdu import *

def report(title, td, **kw):
    print(title)
    if td is None:
        print('  (word does not close up / not a curve)')
        return None
    print('  generators: %d (b: %d, c: %d);  %s' % (len(td.gens), sum(g['idem'] == B for g in td.gens),
          sum(g['idem'] == C for g in td.gens), show(td)))
    res = first_order(td, **kw)
    print(describe(td, res))
    return res

P = lambda n, s: ('P', n, s)
Dm = lambda a, s: ('D', a, s)
TAIL4 = [('s', 'S', 1, 1), ('s', 'D', 1, 1), ('s', 'S', 2, 1), ('s', 'D', 1, 1)]          # S D S^2 D  (slope k = 4)
TAIL2 = [('s', 'S', 1, 1), ('s', 'D', 1, 1)]                                              # S D        (k = 2)
TAIL6 = TAIL4 + [('s', 'S', 2, 1), ('s', 'D', 1, 1)]

print('=== 1. the unit square  x -P-> . -D-> . <-P- . <-D- x')
sq = build([P(2, 1), Dm(1, 1), P(2, -1), Dm(1, -1)], compact=True)
r = report('unit square', sq)

print()
print('=== 2. zigzags (no composable junction)')
report('3_1-type arc: b -P-> b <-D- b + tail S D S^2 D', build([P(2, 1), Dm(1, -1)] + TAIL4))
report('4_1-type arc: b -P-> b <-D- b -P-> b <-D- b (no tail)', build([P(2, 1), Dm(1, -1), P(2, 1), Dm(1, -1)]))
report('longer zigzag with tail k = 6', build([P(2, 1), Dm(1, -1), P(2, 1), Dm(1, -1), P(2, 1), Dm(1, -1)] + TAIL6))
report('zigzag, other orientation: b <-P- b -D-> b <-P- b -D-> b', build([P(2, -1), Dm(1, 1), P(2, -1), Dm(1, 1)]))

print()
print('=== 3. arcs containing a composable junction')
report('D then P:  w -D-> x -P-> y', build([Dm(1, 1), P(2, 1)]))
report('P then D:  w -P-> y\' -D-> y', build([P(2, 1), Dm(1, 1)]))
report('P, D, P all forward', build([P(2, 1), Dm(1, 1), P(2, 1)]))
report('D then P inside a longer zigzag: b -P-> b <-D- b -P-> b -D-> b <-P- b', build([P(2, 1), Dm(1, -1), P(2, 1), Dm(1, 1), P(2, -1)]))
report('D then standard tail (k=4):  w -D-> x -S-> c -D-> c -S^2-> c -D-> c', build([Dm(1, 1)] + TAIL4))
report('D then short tail (k=2):  w -D-> x -S-> c -D-> c', build([Dm(1, 1)] + TAIL2))
report('three sides of the square (open): x <-D- w -P-> y\' -D-> y', build([Dm(1, -1), P(2, 1), Dm(1, 1)]))
report('square with one run cut open after c_3\'', build([('s','D',1,-1)] + [('s','S',1,1),('s','D',1,1),('s','S',2,1)], start_idem=B))

print()
print('=== 4. squares with D^2 sides, and with legs P_1, P_3')
report('square with D^2 sides and P_2 legs', build([P(2, 1), Dm(2, 1), P(2, -1), Dm(2, -1)], compact=True))
report('square with D sides and P_1 legs', build([P(1, 1), Dm(1, 1), P(1, -1), Dm(1, -1)], compact=True))
report('square with D sides and P_3 legs', build([P(3, 1), Dm(1, 1), P(3, -1), Dm(1, -1)], compact=True))
report('square with D^2 sides and P_1 legs', build([P(1, 1), Dm(2, 1), P(1, -1), Dm(2, -1)], compact=True))
report('square with D^3 sides and P_2 legs', build([P(2, 1), Dm(3, 1), P(2, -1), Dm(3, -1)], compact=True))
report('"square" with one D and one D^2 side (does it close up?)', build([P(2, 1), Dm(1, 1), P(2, -1), Dm(2, -1)], compact=True))
report('"square" with legs P_2 and P_3 (does it close up?)', build([P(2, 1), Dm(1, 1), P(3, -1), Dm(1, -1)], compact=True))
