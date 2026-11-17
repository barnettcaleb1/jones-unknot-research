# Theorem A sign test: a few short words whose D lies outside {0,1}, so (2D-1)^2 >= 9; compare with |R_g(zeta)|^2.
import itertools, sys
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/g2-proof/ref-kernel')
from ref_check import D, R, ev
seen = {}
for L in (3, 4, 5):
    for w in itertools.product([1,2,3,4,5,-1,-2,-3,-4,-5], repeat=L):
        d = D(list(w), 1)
        if d not in (0, 1) and d not in seen: seen[d] = list(w)
    if len(seen) >= 4: break
for d, w in sorted(seen.items()):
    r = abs(ev(R(w)))**2; dm = D(w, -1)
    print(f"word {w}: D = {d:+d}, (2D-1)^2 = {(2*d-1)**2}, |R(zeta)|^2 = {r:.6f} -> {'ok' if abs(r-(2*d-1)**2)<1e-9 else 'MISMATCH'};"
          f" mirrored-convention D = {dm:+d} -> {'ok' if abs(r-(2*dm-1)**2)<1e-9 else 'mismatch'}")
