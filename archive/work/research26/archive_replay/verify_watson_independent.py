#!/usr/bin/env python3
"""Independent Watson six-port connectivity check. Standard library only.

This checks component counts, not tangle isotopy or Khovanov homology.
The rainbow cancellation is a separate geometric lemma.
"""
import itertools
import json

CAPS = {
    "A": [(0, 5), (1, 2), (3, 4)],
    "X": [(0, 5), (1, 3), (2, 4)],
    "B": [(0, 5), (1, 4), (2, 3)],
}

def component_count(permutation, top, bottom):
    # Follow each of the six strands from its top port to its bottom port.
    rho = list(permutation) + [
        5 - permutation[5 - i] for i in range(3, 6)
    ]
    inverse = [rho.index(i) for i in range(6)]
    # Contract all six braid strands. Bottom cap edges pull back to top ports.
    edges = CAPS[top] + [
        (inverse[i], inverse[j]) for i, j in CAPS[bottom]
    ]
    adjacency = [[] for _ in range(6)]
    for i, j in edges:
        adjacency[i].append(j)
        adjacency[j].append(i)
    assert all(len(neighbors) == 2 for neighbors in adjacency)
    seen = set()
    components = 0
    for start in range(6):
        if start in seen:
            continue
        components += 1
        stack = [start]
        while stack:
            vertex = stack.pop()
            if vertex in seen:
                continue
            seen.add(vertex)
            stack.extend(adjacency[vertex])
    return components

def main():
    rows = {}
    for permutation in itertools.permutations(range(3)):
        row = {
            a + b: component_count(permutation, a, b)
            for a in CAPS for b in CAPS
        }
        fixes_outer = permutation[0] == 0
        for pair in ("AA", "XX"):
            assert row[pair] == (3 if fixes_outer else 1)
        for pair in ("AX", "XA"):
            assert row[pair] == (2 if fixes_outer else 1)
        for pair in ("AB", "BA", "XB", "BX"):
            assert row[pair] == 2
        assert row["BB"] == 3
        rows["".join(str(i + 1) for i in permutation)] = row
    print(json.dumps({
        "checked_cap_permutation_pairs": 54,
        "status": "all counts agree",
        "scope": "connectivity only; rainbow isotopy is a separate proof",
        "rows": rows,
    }, indent=2))

if __name__ == "__main__":
    main()

