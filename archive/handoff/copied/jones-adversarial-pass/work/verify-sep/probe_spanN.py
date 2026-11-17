"""Cheap falsification probe of the target lemma: for c != c', N(c,c') = [3] H(v_c,v_c')/H(v_c,v_c)
is an integral Laurent poly; collision <=> N = +-A^k [3] (span 8). Record span(N) distribution and
flag any span in 1..11 or any collision. Random words (all, and partition-preserving ones)."""
import sys, random, time, json
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from tl6 import *
from intersect import curve, count_crossings, Ribbon, cyc_reduce
R = Ribbon(5, 0)
vc = [{2: 1, -2: 1}, {0: 1}, {0: 1}, {2: 1, -2: 1}, {4: 1, 0: 1, -4: 1}]
nH = Hform(vc, vc)
c0 = cyc_reduce([1, 2, 3])
def perm(word):
    p = list(range(6))
    for g in reversed(word):
        i = abs(g) - 1
        p = [ (i+1 if x == i else i if x == i+1 else x) for x in p]
    return p
def preserves(word):
    p = perm(word); S = {p[0], p[1], p[2]}
    return S in ({0, 1, 2}, {3, 4, 5})
random.seed(7)
t0 = time.time()
stats = {}
flags = []
n = 0
while time.time() - t0 < 150:
    L = random.randint(1, 16)
    w = [random.choice([1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) for _ in range(L)]
    if random.random() < 0.5:   # bias to partition-preserving (only class where collisions can live)
        w = [g for x in w for g in (x, x)]  # squares -> pure-ish braids
    wv = rho_vec(w, vc)
    h = Hform(vc, wv)
    # span(N) = span(H) - 20
    sN = (max(h) - min(h)) - 20 if h else None
    pres = preserves(w)
    key = (sN, pres)
    stats[key] = stats.get(key, 0) + 1
    n += 1
    if sN is not None and (1 <= sN <= 11 or sN == 8 or sN < 0):
        flags.append((w, sN, pres))
print("samples", n, "seconds", round(time.time() - t0, 1))
print("span(N) counts (span, partition_preserved):")
for k in sorted(stats, key=lambda x: (x[0] if x[0] is not None else -99, x[1])):
    print("  ", k, stats[k])
print("flags (span N in 1..11 or negative):", len(flags))
for f in flags[:10]:
    w, sN, pres = f
    cw = curve(w)
    same = (cw == c0) or (sorted(cw) == sorted(c0) and len(cw) == 3)
    print("   ", f, " i(c,phi c) =", count_crossings(c0, cw, R) if cw != c0 else 0)
json.dump({'n': n, 'stats': {str(k): v for k, v in stats.items()}, 'flags': flags[:200]},
          open(__file__.rsplit('/', 1)[0] + '/probe_spanN_out.json', 'w'), indent=1)
