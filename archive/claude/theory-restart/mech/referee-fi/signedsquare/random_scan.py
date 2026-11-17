#!/usr/bin/env python3
"""Referee script 4: random two-box patterns (closed braid-like words and plats).
For each: exact tensor by the TL-direct state sum (every 10th cross-checked with cx-tools bracket.py via PD codes),
exact evaluation at zeta_8, and the sign law at every nonzero anchor:
    (-1)^(i+j) det C / C_ij^2 is a nonnegative rational square; an integer square if |C_ij| = 1.
Also: A = 1 values nonzero (so no outer-coset tensor), and tally of unit-anchored m^2 values."""
import sys, random, collections
sys.dont_write_bytecode = True
from twobox import *

random.seed(int(sys.argv[1]) if len(sys.argv) > 1 else 1115)
N = int(sys.argv[2]) if len(sys.argv) > 2 else 3000
stats = collections.Counter()
m2_unit = collections.Counter()
neg_examples = []
fails = []
for t in range(N):
    closure = random.choice(["braid", "braid", "plat"])
    n = random.choice([2, 3, 3, 4, 4, 5]) if closure == "braid" else random.choice([2, 4, 4, 6])
    L = random.randint(0, 9)
    word = [(random.randint(1, n - 1), random.choice([1, -1])) for _ in range(L)]
    for name in ('B1', 'B2'):
        word.insert(random.randint(0, len(word)), (random.randint(1, n - 1), name))
    C = tl_tensor(word, n, closure)
    stats["patterns"] += 1
    if t % 10 == 0:
        C2 = pd_tensor(word, n, closure)
        stats["cross-checked vs bracket.py"] += 1
        if C2 != C:
            fails.append(("TOOL MISMATCH", closure, n, word)); stats["tool mismatch"] += 1
    res = analyse(C)
    # A=1 values
    a1 = [[sum(C[i][j].values()) for j in range(2)] for i in range(2)]
    if any(a1[i][j] == 0 for i in range(2) for j in range(2)):
        stats["zero entry at A=1"] += 1
    if not res["nonzero"]:
        stats["C(zeta)=0 (vacuous)"] += 1
        continue
    stats["C(zeta)!=0"] += 1
    if not z_iszero(res["det"]):
        stats["det C(zeta)!=0"] += 1
    for (i, j), d in res["anchors"].items():
        stats["anchors tested"] += 1
        if (i + j) % 2 == 0:
            stats["diagonal anchors tested"] += 1
            if d["rational"] and d["ratio"][0] > 0:
                stats["diagonal anchors with ratio > 0"] += 1
            if d["rational"] and d["ratio"][0] < 0:
                neg_examples.append((closure, n, word, (i, j), d["ratio"]))
        if d["unit"]:
            stats["unit anchors"] += 1
            if (i + j) % 2 == 0 and d["rational"]:
                m2_unit[int(d["ratio"][0])] += 1
        if not d["ok"]:
            fails.append((closure, n, word, (i, j), d["ratio"]))
    if not res["ok"]:
        stats["LAW FAILURES"] += 1
for k in sorted(stats):
    print("%-40s %d" % (k, stats[k]))
print("LAW FAILURES:", stats["LAW FAILURES"], " tool mismatches:", stats["tool mismatch"])
print("diagonal anchors with NEGATIVE ratio (would be outer-coset sign):", len(neg_examples))
print("unit diagonal anchors: distribution of m^2 = det C/C_ii^2:", dict(sorted(m2_unit.items())))
for f in fails[:10]:
    print("FAIL:", f)
