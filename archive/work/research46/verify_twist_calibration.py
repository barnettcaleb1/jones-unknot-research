"""Exact independent TL3 calibration of the normalized twist spectrum."""
import json

def add(*ps):
    r = {}
    for p in ps:
        for k, v in p.items():
            r[k] = r.get(k, 0) + v
    return {k: v for k, v in r.items() if v}

def mul(p, q):
    r = {}
    for i, x in p.items():
        for j, y in q.items():
            r[i+j] = r.get(i+j, 0) + x*y
    return {k: v for k, v in r.items() if v}

def mm(a, b):
    return [[add(*(mul(a[i][k], b[k][j]) for k in range(2)))
             for j in range(2)] for i in range(2)]

I = [[{0: 1}, {}], [{}, {0: 1}]]
s1 = [[{-3: -1}, {-1: 1}], [{}, {1: 1}]]
s2 = [[{1: 1}, {}], [{-1: 1}, {-3: -1}]]
C = mm(s1, s2)
assert C == [[{}, {-4: -1}], [{0: 1}, {-2: -1}]]
assert mm(mm(C, C), C) == [[{-6: 1}, {}], [{}, {-6: 1}]]

# Direct positive braid powers, with reduced Markov trace
# tr_2 + (delta^2-2)*chi, chi(sigma_i)=A.
B = I
calibrated = []
for m in range(1, 14):
    B = mm(B, C)
    if m % 3 != 1:
        continue
    k = (m-1)//3
    reduced_bracket = add(B[0][0], B[1][1],
                          mul({4: 1, -4: 1}, {2*m: 1}))
    actual = mul({-6*m: 1}, reduced_bracket)
    expected = add({-12*k: 1}, {-12*k-8: 1}, {-24*k-8: -1})
    assert actual == expected
    assert (actual == {0: 1}) == (k == 0)
    calibrated.append(k)

print(json.dumps({
    'C_cubed': 'A^-6 I',
    'actual_braid_family': '(sigma_1 sigma_2)^(3k+1)',
    'normalized_Jones': 't^(3k)+t^(3k+2)-t^(6k+2)',
    'direct_braid_power_checks': calibrated,
    'all_k_proof': 'C^3=A^-6 I; scalar character chi(C)=A^2',
    'scope': 'Framing calibration, not a proof of the full research conjecture.'
}, indent=2))
