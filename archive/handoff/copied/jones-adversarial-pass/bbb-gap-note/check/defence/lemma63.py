# Test Lemma 6.3 (and the 3-disk claim used in Prop 6.7) on products Phi = Phi'.Gamma_1 that are
# proper by the shortcut criterion of the proof of Thm 6.9 (reduced word of Phi' does not end in y2,
# so the juxtaposition with Gamma_1 = y2^-1 ... is freely reduced).
# Gamma_1 read off Fig. 6.3 (see report):  W = y2^-1 y1^-1 y2 y2 y3^-1 y2^-1 y1 y2  (path order).
# Push dictionary (checked below): Push(g_i) = A_i4, y1 = g3, y2 = g2 g3, y3 = g1 g2 g3.
import random, sys, os, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lp import *
from curves import *

def A(i, j):
    up = list(range(j - 1, i, -1)); return up + [i, i] + finv(up)
PUSH = {1: A(3, 4), 2: A(2, 4) + A(3, 4), 3: A(1, 4) + A(2, 4) + A(3, 4)}
# consistency with the twist formulas Push(y) = T_outer T_inner^-1
assert act(4, PUSH[1]) == act(4, [3, 3])
assert act(4, PUSH[2]) == act(4, [2, 3] * 3 + [-2, -2])
assert act(4, PUSH[3]) == act(4, [1, 2, 3] * 4 + finv([1, 2] * 3))
for k in (1, 2, 3):
    d, _ = delete_strand(PUSH[k], 4, 4)
    assert perm(PUSH[k], 4) == [1, 2, 3, 4] and is_trivial(3, d)

def push_word(yw):
    out = []
    for y in yw:
        out += PUSH[abs(y)] if y > 0 else finv(PUSH[abs(y)])
    return out

W = [-2, -1, 2, 2, -3, -2, 1, 2]
G1 = push_word(W)
assert fred(W) == W and W[0] == -2

LEMMA63 = {frozenset({2, 3}): 'pres', frozenset({3}): 'chg', frozenset({4}): 'chg',
           frozenset({1, 2, 3}): 'chg', frozenset({1, 2, 3, 4}): 'chg'}

def check(Vy):
    br = push_word(Vy) + G1
    R = analyse(br, 4)
    bad = []
    for d in R['disks']:
        exp = LEMMA63.get(d['P'])
        got = 'chg' if d['changing'] else 'pres'
        if exp != got:
            bad.append((tuple(sorted(d['P'])), got))
    has3 = any(d['P'] == frozenset({1, 2, 3}) for d in R['disks'])
    return R, bad, has3

def rand_reduced(L):
    w = []
    while len(w) < L:
        x = random.choice([1, -1, 2, -2, 3, -3])
        if w and w[-1] == -x: continue
        w.append(x)
    return w

if __name__ == '__main__':
    random.seed(7)
    tested = fails = no3 = 0
    examples = []
    seen = set()
    words = []
    # all reduced words of length 1..3 not ending in y2, plus random longer ones
    for L in (1, 2, 3):
        for w in itertools.product([1, -1, 2, -2, 3, -3], repeat=L):
            w = list(w)
            if fred(w) == w and w[-1] != 2: words.append(w)
    for _ in range(300):
        w = rand_reduced(random.randint(4, 7))
        if w[-1] != 2: words.append(w)
    typecount = {}
    for Vy in words:
        R, bad, has3 = check(Vy)
        tested += 1
        for d in R['disks']:
            key = (tuple(sorted(d['P'])), 'chg' if d['changing'] else 'pres')
            typecount[key] = typecount.get(key, 0) + 1
        if bad:
            fails += 1
            if len(examples) < 8: examples.append((Vy, sorted(set(bad)), len(R['terms'])))
        if not has3: no3 += 1
    print(f"proper products by the word criterion tested: {tested}")
    print(f"  violating Lemma 6.3 (some disk outside the 5 allowed types/signs): {fails}")
    print(f"  with no 3-disk {{p1,p2,p3}} in the disk sequence: {no3}")
    print("disk types over all tests:", {k: v for k, v in sorted(typecount.items(), key=lambda x: (len(x[0][0]), x))})
    for e in examples: print("  example Phi' =", e[0], "bad disks:", e[1], "iota =", e[2])
    # Gamma_1 alone (Phi' = 1)
    R0 = analyse(G1, 4)
    print("Phi = Gamma_1 alone: iota =", len(R0['terms']), "disks:", [(tuple(sorted(d['P'])), 'chg' if d['changing'] else 'pres') for d in R0['disks']])
