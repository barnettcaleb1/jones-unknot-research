"""Among random phi with span(N)=8 (the collision degree), test exact collinearity rho(phi)v_c ~ v_c
and whether phi(c) != c (free-group curve + intersection count). A collinear pair with phi(c) != c
would be a kernel element T_c T_{phi c}^-1 of the genus-two Jones representation."""
import sys, random, time, json
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from tl6 import *
from intersect import curve, count_crossings, Ribbon, cyc_reduce
R = Ribbon(5, 0)
vc = [{2: 1, -2: 1}, {0: 1}, {0: 1}, {2: 1, -2: 1}, {4: 1, 0: 1, -4: 1}]
c0 = cyc_reduce([1, 2, 3])
def proportional(u, w):
    for i in range(DIM):
        for j in range(i + 1, DIM):
            if ladd(lmul(u[i], w[j]), lmul(u[j], w[i]), -1) != {}:
                return False
    return True
def same_curve(a, b):
    # cyclic words equal up to rotation or inversion
    if len(a) != len(b):
        return False
    for bb in (b, [-x for x in reversed(b)]):
        for r in range(len(bb)):
            if a == bb[r:] + bb[:r]:
                return True
    return False
random.seed(11)
t0 = time.time()
n8 = 0; coll = 0; coll_noncurve = []; noncoll8 = []
while time.time() - t0 < 120:
    L = random.randint(1, 18)
    w = [random.choice([1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) for _ in range(L)]
    if random.random() < 0.6:
        w = [g for x in w for g in (x, x)]
    wv = rho_vec(w, vc)
    h = Hform(vc, wv)
    if not h or (max(h) - min(h)) - 20 != 8:
        continue
    n8 += 1
    cw = curve(w)
    same = same_curve(cw, c0)
    col = proportional(vc, wv)
    if col:
        coll += 1
        if not same:
            coll_noncurve.append((w, cw))
    else:
        if len(noncoll8) < 2000:
            noncoll8.append((w, None if same else count_crossings(c0, cw, R), same))
print("samples with span(N)=8:", n8, " collinear:", coll, " collinear but phi(c)!=c (KERNEL CANDIDATES):", len(coll_noncurve))
for x in coll_noncurve[:5]:
    print("   ", x)
same_noncol = [x for x in noncoll8 if x[2]]
print("non-collinear with phi(c)=c (should be 0):", len(same_noncol))
ivals = {}
for x in noncoll8:
    if not x[2]:
        ivals[x[1]] = ivals.get(x[1], 0) + 1
print("span(N)=8 but not collinear: intersection numbers i(c,phi c) -> counts:", dict(sorted(ivals.items())))
ex = [x for x in noncoll8 if not x[2]][:3]
print("examples:", ex)
json.dump({'n8': n8, 'collinear': coll, 'kernel_candidates': coll_noncurve[:50], 'noncollinear_span8_examples': ex,
           'ivals': ivals}, open(__file__.rsplit('/', 1)[0] + '/probe_collision_out.json', 'w'), indent=1)
