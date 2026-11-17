import sys
from zbfs import bfs
for line in open(sys.argv[1]):
    f = dict(kv.split('=') for kv in line.split())
    n = int(f['n']); w = [int(ch) for ch in f['word']]
    sg = {i: (1 if s == '+' else -1) for i, s in enumerate(f['eps'])}
    path, ns = bfs(w, sg, n + 2, limit=int(sys.argv[2]))
    even = set(f['parity']) == {'0'}
    print(f"n={n} word={f['word']} eps={f['eps']} even={even} parity={f['parity']} {'TRIVIAL len=%d' % (len(path)-1) if path else 'NOT-FOUND'} explored={ns}", flush=True)
