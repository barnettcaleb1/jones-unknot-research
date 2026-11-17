#!/usr/bin/env python3
"""3-braid closures (knots) of a given length: reduced Khovanov homology (F_2), report those with an impure extreme quantum degree."""
import sys, itertools, json
from scan3 import word, is_knot, khr, extremes
L = int(sys.argv[1])
seen = set(); cnt = 0
out = open('scan3_L%d.jsonl' % L, 'w')
for w in itertools.product((1, -1, 2, -2), repeat=L):
    if any(w[i] == -w[(i + 1) % L] for i in range(L)): continue
    rots = [w[i:] + w[:i] for i in range(L)]
    # canonical under rotation, and under the symmetry swapping generators 1<->2, and mirror not identified
    sw = tuple((3 - abs(x)) * (1 if x > 0 else -1) for x in w)
    rots += [sw[i:] + sw[:i] for i in range(L)]
    rev = tuple(reversed(w)); rots += [rev[i:] + rev[:i] for i in range(L)]
    if w != min(rots): continue
    if not is_knot(w, 3): continue
    # require both signs present (otherwise positive/negative braid: skip quickly? keep)
    g = khr(list(w), 3, name='b3_%d' % L)
    cnt += 1
    if g is None: continue
    key = tuple(sorted(g))
    if key in seen: continue
    seen.add(key)
    ex = extremes(g)
    if len(set(ex['top'][1])) > 1 or len(set(ex['bot'][1])) > 1:
        rec = dict(braid=list(w), rank=ex['rank'], top=ex['top'], bot=ex['bot'])
        out.write(json.dumps(rec) + '\n'); out.flush()
        print('IMPURE', rec, flush=True)
print('L', L, 'words run', cnt, 'distinct Kh', len(seen))
