import sys, time
sys.path.insert(0, '.')
from khsplit import *
exec(open('t_basic.py').read().split("pointed('l0.x1.x1'")[0].split("D, H = reduced_kh('r1.y0")[0])
exec('def reduced_kh(word, ntop, joins, mark):\n    D = Diagram(word, ntop, joins, [mark]); C = Complex(D, deform=False); return D, homology_bigraded(C)')
src = open('t_basic.py').read()
start = src.index('def pointed'); end = src.index("pointed('l0.x1.x1'")
exec(src[start:end])
t = time.time()
base = 'r1.r2.l1.l2.y0.y1.y1.y0.y0.y1.y1.y0.y2.y1.y3.y2.u4.u3.u0'
D, C, E1, Htot = pointed(base, 'LHT quotient tangle (no framing twists), closure T(0)-type')
print('time', round(time.time() - t, 1))
# knot types of the two components: delete the other component -> compute reduced Kh of each component alone is not
# directly available from the word; instead report self-crossings
for c in range(2):
    selfc = [k for k in range(D.n) if not D.mixed[k] and D.comp[D.slots[k]['NW']] == c]
    print('component', c, 'self-crossings:', len(selfc))
