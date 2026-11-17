"""Exact classical support certificate; no curve or braid-word search."""
from fractions import Fraction as F
from itertools import combinations, product
import json

edges = list(combinations(range(5), 2))
index = {edge: i for i, edge in enumerate(edges)}
S = {0, 1, 2}
v = [F(-1 if len(set(e) & S) == 2 else
       1 if len(set(e) & S) == 1 else -3) for e in edges]
def swap(vec, a, b):
    def image(x):
        return b if x == a else a if x == b else x
    return [vec[index[tuple(sorted((image(i), image(j))))]] for i, j in edges]
def project(vec, a, b, sign):
    sv = swap(vec, a, b)
    return [(x + sign*y)/2 for x, y in zip(vec, sv)]
norm = sum(x*x for x in v)
weights = {}
for s, t in product((1, -1), repeat=2):
    u = project(project(v, 0, 3, s), 1, 4, t)
    weight = sum(x*x for x in u)/norm
    assert weight > 0
    weights[f'{s:+d},{t:+d}'] = str(weight)
assert weights == {'+1,+1': '1/6', '+1,-1': '1/6',
                   '-1,+1': '1/6', '-1,-1': '1/2'}
print(json.dumps({'norm_squared': str(norm), 'joint_weights': weights,
                  'all_four_channels_nonzero': True}, indent=2))
