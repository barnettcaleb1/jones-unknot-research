"""Exact connected-sum algebra; geometric identifications are in sums.txt."""
from pathlib import Path
import importlib.util

base = Path(__file__).resolve().parents[1] / 'transmission18' / 'exact_factor_certificate.py'
spec = importlib.util.spec_from_file_location('base_certificate', base)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

def neg(p):
    return {e: -c for e, c in p.items()}

def sum_defect(a, b):
    return m.add(a, b, neg(m.mul(m.DELTA, m.mul(a, b))))

def H(x):
    return m.add({0: 1}, neg(m.mul(m.DELTA, x)))

x = m.x_core
mirror = {-e: c for e, c in x.items()}
assert mirror == m.shift(m.d, -26)
expected = {
    'trefoil#trefoil': {2:-1,6:1,10:-1,14:1,18:-1,22:1,30:-2,
                        34:3,38:-3,42:1,46:1,50:-1,54:1},
    'trefoil#mirror': {-14:-1,-10:2,-6:-2,-2:1,2:1,6:-2,10:2,14:-1},
}
for name, a, b in [('trefoil#trefoil', x, x), ('trefoil#mirror', x, mirror)]:
    result = sum_defect(a, b)
    assert result == expected[name]
    assert H(result) == m.mul(H(a), H(b))
    assert result
    print(name, 'PASS:', len(result), 'nonzero terms')
print('Figure-eight repeated sum is checked symbolically in sums.txt; no PD computation claimed.')
