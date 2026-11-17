import sys
from kh2 import kh2, circles
from scd import interlace, nullity_table
import itertools
tot = {}
for line in open(sys.argv[1]):
    f = dict(kv.split('=') for kv in line.split())
    n = int(f['n']); w = [int(ch) for ch in f['word']]; eps = {i: (1 if s == '+' else -1) for i, s in enumerate(f['eps'])}
    # cross-check loop counts vs nullity formula on a few states
    H = kh2(w, eps); d = sum(H.values())
    even = set(f['parity']) == {'0'}
    print(f"n={n} word={f['word']} eps={f['eps']} even={even} KhZ2 total={d} {sorted(H.items()) if d<=6 else ''}")
