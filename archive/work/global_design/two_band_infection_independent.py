#!/usr/bin/env python3
"""One specified 2+1 ribbon infection; independent diagram/Regina check.

No parameter/word search. Does not import the TL implementation used for
the first calculation. Q is in top0..5, bottom6..11 order.
"""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "work/braid_classification/packages"))
import regina
from spherogram.links import Link
from spherogram.links.tangles import (
    BraidTangle, IdentityBraid, ZeroTangle, join_strands,
)

Q = [(6, 9), (7, 8), (1, 2), (3, 4), (5, 11), (0, 10)]
BETA = [1, 1, 2, 2, -1, -1, -2, -2]


def inverse(word):
    return [-i for i in reversed(word)]


def cable(word):
    result = []
    for s in word:
        k = abs(s)
        block = [2*k, 2*k-1, 2*k+1, 2*k]
        result.extend(block if s > 0 else inverse(block))
    return result


def corner(word, i, j):
    t = IdentityBraid(6)
    if i:
        t = t * (ZeroTangle() | IdentityBraid(4))
    if j:
        t = t * (IdentityBraid(2) | ZeroTangle() | IdentityBraid(2))
    t = t * BraidTangle(word, 6)
    for a, b in Q:
        # Spherogram orders bottom before top.
        a = a+6 if a < 6 else a-6
        b = b+6 if b < 6 else b-6
        join_strands(t.adjacent[a], t.adjacent[b])
    link = Link(t.crossings, check_planarity=True)
    # PD alone cannot encode a crossing-free component. Reject such input
    # here instead of silently dropping it.
    assert getattr(link, "unlinked_unknot_components", 0) == 0
    pd = link.PD_code()
    r = regina.Link.fromPD([[v+1 for v in x] for x in pd])
    polynomial = r.bracket()
    bracket = {k: int(str(polynomial[k]))
               for k in range(polynomial.minExp(), polynomial.maxExp()+1)
               if polynomial[k] != 0}
    original = {
        "PD": pd, "crossings": r.size(),
        "components": r.countComponents(), "writhe": r.writhe(),
        "raw_reduced_bracket_A": bracket,
    }
    r.simplify()
    original["after_isotopy_simplification"] = {
        "crossings": r.size(), "components": r.countComponents(),
        "crossing_free_components": r.countTrivialComponents(),
        "PD": r.pd(),
    }
    return original, bracket


def multiply(a, b):
    result = {}
    for i, v in a.items():
        for j, w in b.items():
            result[i+j] = result.get(i+j, 0) + v*w
    return {i: v for i, v in result.items() if v}


if __name__ == "__main__":
    words = {
        "baseline": [1]*3 + [3]*3 + cable([2]),
        "infected": [1]*3 + [3]*3 + cable(BETA + [2]),
    }
    result = {"Q": Q, "beta": BETA, "words": words, "corners": {}}
    polynomials = {}
    for label, word in words.items():
        result["corners"][label] = {}
        polynomials[label] = {}
        for i, j in [(0, 0), (0, 1), (1, 0), (1, 1)]:
            data, poly = corner(word, i, j)
            key = str(i)+str(j)
            result["corners"][label][key] = data
            polynomials[label][key] = poly
    expected_baseline = {
        "00": {-14: 1, -10: -2, -6: 1, -2: -2, 2: 1, 6: -1},
        "01": {-16: -1, -12: 1, -4: 1},
        "10": {-16: -1, -12: 1, -4: 1},
        "11": {-18: 1},
    }
    assert polynomials["baseline"] == expected_baseline
    for key in ["01", "10", "11"]:
        assert polynomials["infected"][key] == expected_baseline[key]
    defect = dict(polynomials["infected"]["00"])
    for k, v in expected_baseline["00"].items():
        defect[k] = defect.get(k, 0)-v
    defect = {k: v for k, v in defect.items() if v}
    factor = {-30: 1}
    for power in [4, 16, 24]:
        factor = multiply(factor, {0: 1, power: -1})
    assert defect == factor and defect
    assert result["corners"]["infected"]["11"][
        "after_isotopy_simplification"]["crossings"] == 0
    result["joint_defect_A"] = defect
    result["joint_defect_factorization"] = "A^-30(1-A^4)(1-A^16)(1-A^24)"
    result["verdict"] = "REJECTED: joint corner fails; all three proper corners agree"
    target = Path(__file__).with_suffix(".json")
    target.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"verdict": result["verdict"], "joint_defect_A": defect,
                      "saved": str(target),
                      "simplified": {label: {
                          key: data["after_isotopy_simplification"]["crossings"]
                          for key, data in corners.items()}
                          for label, corners in result["corners"].items()}}, indent=2))
