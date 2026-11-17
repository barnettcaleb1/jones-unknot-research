"""Referee P2b: depth-4 nested trees with width-1 leaves (y0, x0, y0.y0, x0.x0.x0) and >= 2 children at >= 2 levels."""
import random, time
exec(open('r2_nest.py').read().split("rnd = random.Random(31337)")[0])
leaves = [('y0', [ONE, mono(-3)]), ('x0', [ONE, mono(0, -1)]), ('y0.y0', apply('YY')), ('x0.x0.x0', apply('yyy'))]
def g(rnd, d):
    if d == 0:
        B, v = rnd.choice(leaves); return ('box', B, v)
    k = 2 if d in (1, 3) else rnd.choice([1, 2])
    return ('neck', rnd.choice([1, -1, 2, -2]), [g(rnd, d - 1)] + [g(rnd, 0) for _ in range(k - 1)])
rnd = random.Random(2718); t0 = time.time(); ok = tot = 0
for it in range(60):
    T = g(rnd, 4); w = 's.' + word(T)
    if width(w[2:]) > 9: continue
    Jw = J(w)
    if Jw is None: continue
    tot += 1; ok += (normalize(vec(T)[0]) == Jw)
    if normalize(vec(T)[0]) != Jw: print('FAIL', w)
    if tot >= 10 or time.time() - t0 > 400: break
print('depth-4 trees: %d/%d  time %.0f' % (ok, tot, time.time() - t0))
