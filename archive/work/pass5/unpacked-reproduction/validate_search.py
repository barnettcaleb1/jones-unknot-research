"""Cross-check the archived core and modular search against exact reconstruction."""
from pathlib import Path
import json
import random
import subprocess
import tangle_core_stdlib as t

ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT / 'tangle_four_strand.json').read_text())
assert t.CORE == [{int(e): c for e, c in p.items()}
                  for p in data['core_Laurent_coefficients']]
assert [list(p) for p in t.BASIS] == data['basis']
assert t.IDENT == data['identity_index']
assert [[list(p) for p in g] for g in t.TRANSITIONS] == data['generator_transitions']
assert [list(p) for p in t.TYPES] == data['annular_closure_types_contractible_essential']

def is_knot(word):
    perm = list(range(4))
    for s in word:
        i = abs(s) - 1
        perm[i], perm[i + 1] = perm[i + 1], perm[i]
    connectivity = (3, 5, 6, 0, 7, 1, 2, 4)
    edges = [(i, j) for i, j in enumerate(connectivity) if i < j]
    edges += [(i, 4 + perm[i]) for i in range(4)]
    return len(set(t.search.components(edges, 8))) == 1

rng = random.Random(20261031)
words = [[], [1, 3], [-1, 3]] + [
    [rng.choice([-3, -2, -1, 1, 2, 3]) for _ in range(rng.randrange(1, 18))]
    for _ in range(125)
]
raw = ''.join(' '.join(map(str, w)) + '\n' for w in words)
result = subprocess.run([str(ROOT / 'top_braid_search'), 'check'],
                        input=raw, text=True, capture_output=True, check=True)
lines = result.stdout.splitlines()
assert len(lines) == len(words)
for word, line in zip(words, lines):
    actual, knot = map(int, line.split())
    expected = sum(c * pow(2, e, 1000000007)
                   for e, c in t.annular(word).get(2, {}).items()) % 1000000007
    assert actual == expected, (word, actual, expected)
    assert bool(knot) == is_knot(word), word
print('Core rebuilt from crossings matches all saved TL4 data.')
print('128 exact Laurent and connectivity checks passed.')
