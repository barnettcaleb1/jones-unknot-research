"""Exact component counts for Watson's six-port closure; no knot package.

Ports at each cap are 0,...,5, left to right.  A is the zero tangle,
X its odd-integer-twist connectivity, and B the infinity/rainbow tangle.
The two three-strand braids have reflected equal permutations: crossing
inversion affects over/under data, not endpoint permutation.
"""
from itertools import permutations
import json
from pathlib import Path

CAPS = {
    'A': [(0, 5), (1, 2), (3, 4)],
    'X': [(0, 5), (1, 3), (2, 4)],
    'B': [(0, 5), (1, 4), (2, 3)],
}

def component_count(p, top, bottom):
    doubled = list(p) + [5-p[2-i] for i in range(3)]
    parent = list(range(6))
    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    edges = CAPS[top] + [(doubled[a], doubled[b])
                        for a, b in CAPS[bottom]]
    for a, b in edges:
        parent[find(a)] = find(b)
    return len({find(x) for x in range(6)})

rows = []
for p in permutations(range(3)):
    counts = {a+b: component_count(p, a, b)
              for a in CAPS for b in CAPS}
    allowed = p not in [(0, 1, 2), (0, 2, 1)]
    assert all(counts[k] == (1 if allowed else (3 if k in ['AA','XX'] else 2))
               for k in ['AA','XX','AX','XA'])
    assert all(counts[k] == 2 for k in ['AB','BA','XB','BX'])
    assert counts['BB'] == 3
    rows.append({'permutation_one_line': [i+1 for i in p],
                 'allowed_knot_permutation': allowed, 'components': counts})
path = Path(__file__).with_suffix('.json')
path.write_text(json.dumps(rows, indent=2)+'\n')
print(json.dumps(rows, indent=2))
