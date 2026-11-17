#!/usr/bin/env python3
"""One marked source: cable([s1^2,s2^2]) with exterior e2 e4.

Uses the archived exact TL multiplication, including its loop convention.
No braid search. Positive generator cabling is (2i,2i-1,2i+1,2i).
"""
from collections import defaultdict
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("tl_exact", ROOT / "work/generic_evidence/tl_exact.py")
tl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tl)

def inv(word):
    return [-s for s in reversed(word)]

def cable(word):
    out = []
    for s in word:
        i = abs(s)
        block = [2*i, 2*i-1, 2*i+1, 2*i]
        out += block if s > 0 else inv(block)
    return out

def closure(word, turnbacks):
    ident, transitions, loops = tl.tables(6)
    vector = [{} for _ in loops]
    vector[ident] = {0: 1}
    for s in word:
        sign = 1 if s > 0 else -1
        nxt = [defaultdict(int) for _ in loops]
        for j, poly in enumerate(vector):
            tl.addto(nxt[j], poly, sign)
            dest, lp = transitions[abs(s)-1][j]
            for _ in range(lp):
                poly = tl.loopmul(poly)
            tl.addto(nxt[dest], poly, -sign)
        vector = [tl.clean(poly) for poly in nxt]
    for i in turnbacks:
        nxt = [defaultdict(int) for _ in loops]
        for j, poly in enumerate(vector):
            dest, lp = transitions[i-1][j]
            for _ in range(lp):
                poly = tl.loopmul(poly)
            tl.addto(nxt[dest], poly)
        vector = [tl.clean(poly) for poly in nxt]
    result = defaultdict(int)
    for j, poly in enumerate(vector):
        for _ in range(loops[j]-1):
            poly = tl.loopmul(poly)
        tl.addto(result, poly)
    return dict(sorted(tl.clean(result).items()))

def delta_power(n):
    p = {0: 1}
    for _ in range(n):
        p = tl.loopmul(p)
    return p

def multiply(a, b):
    p = defaultdict(int)
    for i, u in a.items():
        for j, v in b.items():
            p[i+j] += u*v
    return tl.clean(p)

if __name__ == "__main__":
    beta = [1, 1, 2, 2, -1, -1, -2, -2]
    word = cable(beta)
    # Fixed exterior C, with no arbitrary framing adjustment.
    empty = closure([], [2,4])
    assert empty == delta_power(3)
    p = closure(word, [2,4])
    # Cutting one ribbon removes that band: the proper surface has
    # three boundary circles, with reduced bracket delta^2.
    partial = {str(i): closure(word, [i,2,4]) for i in [1,3,5]}
    cuts_empty = {str(i): closure([], [i,2,4]) for i in [1,3,5]}
    all_cuts = closure(word, [1,3,5,2,4])
    defect = defaultdict(int, p)
    tl.addto(defect, empty, mult=-1)
    defect = tl.clean(defect)
    # ((1-A^8)/delta)^3 = (-A^2(1-A^4))^3.
    transfer = {0: 1}
    for _ in range(3):
        transfer = multiply(transfer, {2: -1, 6: 1})
    knot_value = defaultdict(int, multiply(transfer, defect))
    knot_value[0] += 1
    knot_value = dict(sorted(tl.clean(knot_value).items()))
    answer = {
        "beta": beta,
        "cabled_word": word,
        "exterior_e": [2,4],
        "identity_closure": empty,
        "candidate_reduced_bracket_A": p,
        "A_span": max(p)-min(p),
        "unlink_A_span": 12,
        "equals_unlink": p == delta_power(3),
        "single_cut_closures": partial,
        "single_cut_identity_controls": cuts_empty,
        "single_cut_matches": {i: partial[i] == cuts_empty[i] for i in partial},
        "all_cut_closure": all_cuts,
        "all_cut_identity_control": closure([], [1,3,5,2,4]),
        "boundary_defect_A": defect,
        "K111_Jones_A_from_transfer": knot_value,
        "K111_A_span": max(knot_value)-min(knot_value),
    }
    target = Path(__file__).with_suffix(".json")
    target.write_text(json.dumps(answer, indent=2)+"\n")
    print(json.dumps(answer, indent=2))
