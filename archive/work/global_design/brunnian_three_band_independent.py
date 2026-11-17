#!/usr/bin/env python3
"""One-source independent TL6 weighted-spin-trace audit.

Does not import the parent's TL pairing implementation.  On the two-spin
01,10 subspace, e=[[−A²,1],[1,−A⁻²]], and it vanishes on 00,11.
Then e²=δe and the quantum trace uses Q=diag(−A²,−A⁻²).
The reduced planar closure is Tr(Q^tensor6 M)/δ.
"""
from collections import defaultdict
import json
from pathlib import Path


def clean(p):
    return {e: c for e, c in p.items() if c}


def add_shift(target, p, exponent=0, coefficient=1):
    for e, c in p.items():
        target[e + exponent] += coefficient * c


def loop(p):
    out = defaultdict(int)
    add_shift(out, p, 2, -1)
    add_shift(out, p, -2, -1)
    return clean(out)


def trace(word, turnbacks):
    # Each column is propagated separately; each local matrix is sparse.
    operators = [('g', s) for s in word] + [('e', i) for i in turnbacks]
    answer = defaultdict(int)
    for start in range(64):
        state = {start: {0: 1}}
        for kind, signed_i in reversed(operators):
            i = abs(signed_i)
            mask = (1 << (6-i)) | (1 << (5-i))
            nxt = defaultdict(lambda: defaultdict(int))
            for bits, p in state.items():
                b0 = (bits >> (6-i)) & 1
                b1 = (bits >> (5-i)) & 1
                if kind == 'g':
                    sign = 1 if signed_i > 0 else -1
                    add_shift(nxt[bits], p, sign)
                    if b0 != b1:
                        add_shift(nxt[bits], p,
                                  -sign + (2 if b0 == 0 else -2), -1)
                        add_shift(nxt[bits ^ mask], p, -sign)
                elif b0 != b1:
                    add_shift(nxt[bits], p, 2 if b0 == 0 else -2, -1)
                    add_shift(nxt[bits ^ mask], p)
            state = {bits: clean(p) for bits, p in nxt.items() if clean(p)}
        # Q^tensor6 has diagonal A^(12−4*popcount); its sign is (+1).
        add_shift(answer, state.get(start, {}), 12-4*start.bit_count())
    return clean(answer)


def integers(p):
    return {int(e): int(c) for e, c in p.items()}


if __name__ == '__main__':
    source = json.loads(Path(__file__).with_name('brunnian_three_band.json').read_text())
    word = []
    for s in source['beta']:
        i = abs(s)
        block = [2*i, 2*i-1, 2*i+1, 2*i]
        word += block if s > 0 else [-v for v in reversed(block)]
    assert word == source['cabled_word']
    p = integers(source['candidate_reduced_bracket_A'])
    checks = {
        'boundary': trace(word, [2, 4]) == loop(p),
        'identity_closure': trace([], [2, 4]) == loop(integers(source['identity_closure'])),
        'all_cuts': trace(word, [1, 3, 5, 2, 4]) == loop({0: 1}),
    }
    for i in [1, 3, 5]:
        checks[f'cut_{i}'] = trace(word, [i, 2, 4]) == loop(
            integers(source['single_cut_closures'][str(i)]))
    print(json.dumps(checks, indent=2))
    assert all(checks.values())

    # Exact factorization certificate, verified with integer multiplication.
    # Here x=A^4 and the full defect is A^(-30) times the polynomial below.
    factor = [1]
    for base, power in [([-1, 1], 4), ([1, 1], 3), ([1, 1, 1], 1),
                        ([1, 0, 1], 1), ([1, -1, 1], 2)]:
        for _ in range(power):
            out = [0] * (len(factor)+len(base)-1)
            for i, c in enumerate(factor):
                for j, d in enumerate(base):
                    out[i+j] += c*d
            factor = out
    unlink = loop(loop(loop({0: 1})))
    defect = defaultdict(int, p)
    for e, c in unlink.items():
        defect[e] -= c
    assert clean(defect) == clean({4*j-30: c for j, c in enumerate(factor)})
    print('boundary_minus_unlink = A^-30 (A^4-1)^4 (A^4+1)^3 '
          '(A^8+A^4+1) (A^8+1) (A^8-A^4+1)^2')
