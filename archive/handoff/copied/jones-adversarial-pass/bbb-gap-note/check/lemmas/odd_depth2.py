# Continue the search: exact depths 3..8 among nontrivial Brunnian 4-braids.
# Imports the helpers of odd_depth.py by exec (same folder, read-only use).
import random
src = open(__file__.replace("odd_depth2.py", "odd_depth.py")).read().split("random.seed(11)")[0]
src = src.replace("N = 8", "N = 12")
exec(src)
random.seed(5)
def randword(L):
    return fr([random.choice([1, 2, 3]) * random.choice([1, -1]) for _ in range(L)])
b2 = comm(comm(A(1, 2), A(1, 3)), A(1, 4))
seed2 = fr(comm([2, 3] * 6, b2))
seeds = [phi0, seed2]
pool = {1: [phi0, seed2]}
best = {}
for trial in range(250):
    s1 = conj(randword(random.randint(0, 5)), random.choice(seeds))
    s2 = conj(randword(random.randint(0, 5)), random.choice(seeds))
    w = fr(comm(s1, s2))
    if not w or not nontrivial(w): continue
    d = depth(rho(w))
    pool.setdefault(d, [])
    if len(pool[d]) < 4: pool[d].append(w)
print("depths of [seed^g, seed^h]:", {d: len(v) for d, v in pool.items()})
# combine pool elements pairwise to reach higher depths
for trial in range(300):
    d1, d2 = random.choice(list(pool)), random.choice(list(pool))
    if d1 + d2 > 8: continue
    u = conj(randword(random.randint(0, 3)), random.choice(pool[d1]))
    v = random.choice(pool[d2])
    w = fr(comm(u, v))
    if not w or len(w) > 6000 or not nontrivial(w): continue
    d = depth(rho(w))
    if d not in pool:
        pool[d] = [w]
        print(f"  new exact depth {d}: [depth {d1}, depth {d2}] commutator, length {len(w)}")
    elif len(pool[d]) < 4:
        pool[d].append(w)
print("exact depths realised (nontrivial at t=2):", sorted(d for d in pool if d < N))
for d in sorted(pool):
    if d < N:
        print(f"  depth {d}: example length {len(pool[d][0])}")
import json
json.dump({str(d): pool[d][0] for d in pool if d < N}, open(__file__.replace(".py", "_words.json"), "w"))
