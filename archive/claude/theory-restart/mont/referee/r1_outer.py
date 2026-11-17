"""Referee P1: Theorem O on FRESH random bodies (own generator, seed 7001), own pinning with 5 closures (k = 1,-1,2,-2,3).
Checks: pin uniqueness; eps = (-1)^n0; v2(-1) in {0,-1}; single-box outer map for m in {+-1..+-4};
concatenation = product (exact); 2- and 3-box necklace bodies pinned from scratch vs t^(2m(1-eps)) X^-m p (exact)."""
import random, sys, time
from rlib import *

rnd = random.Random(7001)
KS = (1, -1, 2, -2, 3)

def interesting(v):
    # non-integral: a not a unit
    return len(v[0]) >= 2

boxes = []
t0 = time.time()
tries = 0
while len(boxes) < 24 and tries < 3000:
    tries += 1
    B = rand_body(rnd, maxlen=rnd.randint(8, 18), maxw=rnd.choice([3, 5, 7]), p_axis=rnd.choice([0.15, 0.3, 0.5]))
    if B is None:
        continue
    c, _ = pin(B, KS)
    if not c:
        if c is not None and c == []:
            print('NOPIN', B)
        continue
    if len(c) != 1:
        print('NONUNIQUE', B, len(c))
        continue
    v = c[0]
    if not interesting(v):
        continue
    if any(v == bb[1] for bb in boxes):
        continue
    boxes.append((B, v))
print('boxes', len(boxes), 'tries', tries, 'time %.1f' % (time.time() - t0))
sys.stdout.flush()

# (b) parity and dichotomy
bad_par = 0; bad_dich = 0
for B, v in boxes:
    e = eps(v); v2m1 = ev(v[1], -1)
    if e != (-1) ** nax(B):
        bad_par += 1; print('PARITY FAIL', B, e, nax(B))
    if v2m1 not in (0, -1):
        bad_dich += 1; print('DICHOTOMY FAIL', B, v2m1)
print('parity fails', bad_par, 'dichotomy fails', bad_dich, 'of', len(boxes))
sys.stdout.flush()

def predicted(m, p):
    e = eps(p)
    q = mvec(Xpow(-m), p)
    k = 2 * m * (1 - e)
    return [shift(q[0], k), shift(q[1], k)]

# (c) single box outer map
ok = 0; tot = 0; fails = []
for idx, (B, v) in enumerate(boxes[:16]):
    for m in rnd.sample([1, -1, 2, -2, 3, -3, 4, -4], 4):
        N = neck(m, [B])
        c, _ = pin(N, KS)
        tot += 1
        if c and len(c) == 1 and c[0] == predicted(m, v):
            ok += 1
        else:
            fails.append((B, m, None if c is None else len(c)))
print('single-box outer map: %d/%d' % (ok, tot), fails[:5])
sys.stdout.flush()

# (d) concatenation = product, and 2-box bodies
ok_c = 0; ok_n = 0; tot = 0; fails = []
for it in range(12):
    (B1, v1), (B2, v2) = rnd.sample(boxes, 2)
    c, _ = pin(B1 + '.' + B2, KS)
    tot += 1
    p = star(v1, v2)
    if c and len(c) == 1 and c[0] == p:
        ok_c += 1
    else:
        fails.append(('concat', B1, B2, None if c is None else len(c)))
    m = rnd.choice([1, -1, 2, -2, 3, -3])
    c, _ = pin(neck(m, [B1, B2]), KS)
    if c and len(c) == 1 and c[0] == predicted(m, p):
        ok_n += 1
    else:
        fails.append(('neck2', B1, B2, m, None if c is None else len(c)))
print('concat=product %d/%d ; 2-box outer map %d/%d' % (ok_c, tot, ok_n, tot), fails[:5])
sys.stdout.flush()

# (e) 3-box bodies
ok = 0; tot = 0; fails = []
for it in range(8):
    tr = rnd.sample(boxes, 3)
    p = star(star(tr[0][1], tr[1][1]), tr[2][1])
    m = rnd.choice([1, -1, 2, -2])
    c, _ = pin(neck(m, [b for b, _ in tr]), KS)
    tot += 1
    if c and len(c) == 1 and c[0] == predicted(m, p):
        ok += 1
    else:
        fails.append((m, [b for b, _ in tr], None if c is None else len(c)))
print('3-box outer map %d/%d' % (ok, tot), fails[:3])
print('total time %.1f' % (time.time() - t0))
import json
json.dump([(B, [sorted(v[0].items()), sorted(v[1].items())]) for B, v in boxes], open('r1_boxes.json', 'w'))
