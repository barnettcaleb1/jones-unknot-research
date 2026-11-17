"""Exact arithmetic checks accompanying the symbolic one-special BN proof.

No packages or external data are needed. The all-n proof is in the text note;
these checks guard against transcribing the published bigrading formula wrongly.
"""
import json
from collections import defaultdict
from pathlib import Path


def euler(grades):
    ans = defaultdict(int)
    for h, q in grades:
        ans[q] += (-1) ** h
    return {q: int(v) for q, v in ans.items() if v}


def add(a, b):
    ans = defaultdict(int, a)
    for q, c in b.items():
        ans[q] += c
    return {q: v for q, v in ans.items() if v}


checks = []
for n in range(1, 21):
    k = 4 * n
    rational = [(j, 2*j + 1) for j in range(k-1)] + [(k, 2*k+1)]
    # KWZ Lemma 2.5: shifts (h,q)=(2(2i-n-1),4(2i-n-1)).
    # Then shift (h,q) by (k/2,k), choosing a convenient even h shift.
    special = []
    for i in range(1, n+1):
        z = 2*i - n - 1
        for h, q in [(-2,-5), (0,-1), (1,1), (3,5)]:
            special.append((h + 2*z + k//2, q + 4*z + k))
    assert len(rational) == len(special) == k
    assert add(euler(rational), euler(special)) == {-1: 1, 1: 1}
    assert {q-2*h for h,q in rational} == {1}
    assert {q-2*h for h,q in special} == {-1}
    for grades in (rational, special):
        top = max(h for h,q in grades)
        assert sum(h == top for h,q in grades) == 1
        assert all(h != top-1 for h,q in grades)
    assert max(q for h,q in rational) == max(q for h,q in special) == 2*k+1
    checks.append({'n': n, 'rank_each': k, 'max_q': 2*k+1,
                   'rational_top_h': k, 'special_top_h': k+1,
                   'identity_and_top_gaps': True})

out = {'status': 'all exact checks passed', 'checks': checks,
       'proof_scope': 'symbolic argument is in one_special_bn_obstruction.txt'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2) + '\n')
print(out['status'], 'for n=1,...,20')
