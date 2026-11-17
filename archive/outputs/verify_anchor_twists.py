"""Exact checks for an anchored twist-family obstruction; standard library only."""
from pathlib import Path
import runpy

root = Path(__file__).resolve().parent
lib = runpy.run_path(str(root / 'verify_twist_obstruction.py'))
add, mul, scale, shift, jvp = (lib[k] for k in ['add', 'mul', 'scale', 'shift', 'jvp'])

p = {1: 1, -1: -1}
h = {1: -1, 5: -1}
c = shift(mul(p, h), 2)
defect = add({4: 1, 0: -1}, c)
values = {0: {0: 1}}
for m in range(1, 13):
    values[m] = add(shift(values[m-1], 4), c)
for m in range(-1, -13, -1):
    values[m] = shift(add(values[m+1], scale(c, -1)), -4)
for m, v in sorted(values.items()):
    a, b = jvp(v)
    assert a.get(2, 0) + b.get(2, 0) == -3*m
    assert lib['reconstruct'](a, b) == v
    if m > 0:
        geometric_sum = {4*j: 1 for j in range(m)}
        assert v == add({0: 1}, mul(defect, geometric_sum))
        assert max(set(a) | set(b)) == 4*m+3
    if m in [-2, -1, 0, 1, 2, 12]:
        print(f'm={m}: c2={a.get(2,0)+b.get(2,0)}, p-degree={max(set(a)|set(b))}')

assert values[1] == {2: 1, 6: 1, 8: -1}
assert values[2] == {2: 1, 4: -1, 6: 2, 8: -1, 10: 1, 12: -1}
for length in range(3, 24, 2):
    for positive_count in range(length+1):
        total_sign = 2*positive_count-length
        m = (total_sign+1)//2
        a, b = jvp(values[m])
        assert a.get(2, 0) + b.get(2, 0) == -3*(total_sign+1)//2
print('All anchor, recurrence, reconstruction, and residual-cube checks passed.')
