"""(c) independent oracle: lp.J (flat_search bracket of the quotient) along the template-1 core m=2k, n=-4k^2-3k."""
import sys, time
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/referee/width2-window')
from r2lib import *
Vw, Uw = 'x0.y2.y2.x1.x1', 'x1.x1.y0.x1'
order = [0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6]
for kv in order:
    m, n = 2 * kv, -4 * kv * kv - 3 * kv
    W = body(Vw, Uw, m, n)
    t0 = time.time()
    J = lp.J(halfword(W))
    Jd = normalize(F_raw_direct(W))
    print('k=%2d (m,n)=(%3d,%4d) |W|=%4d lp.J==1:%s  lp.J==module:%s  span=%d  a2(lp)=%s  [%.1fs]' % (
        kv, m, n, len(W), J == {0: 1}, J == Jd, max(J) - min(J), lp.a2(J), time.time() - t0), flush=True)
