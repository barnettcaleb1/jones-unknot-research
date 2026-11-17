"""Referee P2: fresh nested necklace trees (depth 2-4) vs direct J.  Leaves: fresh boxes (r1_boxes.json, width <= 3),
twist rows +-3, +-5, integral y0/x0.  Prediction = normalize(first entry of recursive vector) with F_m from Theorem O.
Also records that the prediction is unchanged if all Theorem-O units are dropped (projective content only)."""
import json, random, sys, time
from rlib import *
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont')
from words import row

def width(B):
    w = 1; mx = 1
    for t in B.split('.'):
        if not t: continue
        if t[0] in 'lr': w += 2
        elif t[0] == 'u': w -= 2
        mx = max(mx, w)
    return mx

boxes = [(B, [{int(e): c for e, c in v[0]}, {int(e): c for e, c in v[1]}]) for B, v in json.load(open('r1_boxes.json'))]
narrow = [(B, v) for B, v in boxes if width(B) <= 3]
rowsb = []
for r in (3, -3, 5, -5):
    B = '.'.join(row(r))
    c, _ = pin(B, (1, -1, 2))
    rowsb.append((B, c[0]))
ints = [('y0', [ONE, mono(-3)]), ('x0', [ONE, mono(0, -1)])]
print('narrow fresh boxes', len(narrow), ' rows', len(rowsb))

def F(m, p, units=True):
    q = mvec(Xpow(-m), p)
    if not units:
        return q
    k = 2 * m * (1 - eps(p))
    return [shift(q[0], k), shift(q[1], k)]

def gen_tree(rnd, depth):
    if depth == 0:
        r = rnd.random()
        pool = narrow if r < 0.5 else (rowsb if r < 0.85 else ints)
        B, v = rnd.choice(pool)
        return ('box', B, v)
    nch = rnd.choice([1, 2, 2, 3]) if depth > 1 else rnd.choice([2, 2, 3])
    kids = [gen_tree(rnd, depth - 1 if i == 0 else rnd.randint(0, depth - 1)) for i in range(nch)]
    m = rnd.choice([1, -1, 2, -2, 3])
    return ('neck', m, kids)

def word(T):
    if T[0] == 'box': return T[1]
    return neck(T[1], [word(c) for c in T[2]])

def vec(T, units=True):
    if T[0] == 'box': return T[2]
    p = vec(T[2][0], units)
    for c in T[2][1:]:
        p = star(p, vec(c, units))
    return F(T[1], p, units)

def depth(T):
    return 0 if T[0] == 'box' else 1 + max(depth(c) for c in T[2])

rnd = random.Random(31337)
t0 = time.time()
res = {}
for it in range(400):
    d = rnd.choice([2, 2, 3, 3, 4])
    T = gen_tree(rnd, d)
    w = 's.' + word(T)
    if width(w[2:]) > 9:
        continue
    dd = depth(T)
    if res.get(dd, (0, 0))[1] >= 15:
        continue
    t1 = time.time()
    Jw = J(w)
    if Jw is None:
        continue
    pr = normalize(vec(T)[0]); pr0 = normalize(vec(T, False)[0])
    ok = res.get(dd, (0, 0))
    res[dd] = (ok[0] + (pr == Jw), ok[1] + 1)
    if pr != Jw:
        print('FAIL depth', dd, w)
    if pr != pr0:
        print('UNIT-SENSITIVE?!', w)
    if time.time() - t0 > 420:
        break
print('results by depth (ok, total):', res, ' time %.0f' % (time.time() - t0))
