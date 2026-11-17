"""Verify all relative-bar certificates using only the archived source subset.

Run with Python 3 beside candidate_source_subset.json and
ribbon_relative_bar_filter.json. No third-party dependencies.
"""
import ast
from collections import Counter
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
rows = {
    row["name"]: row
    for row in json.loads((BASE / "candidate_source_subset.json").read_text())[
        "polynomial_records"
    ]
}
data = json.loads((BASE / "ribbon_relative_bar_filter.json").read_text())


def polynomial(endpoint):
    sign = -1 if endpoint["mirror"] else 1
    result = Counter()
    for field, rank, h, q in ast.literal_eval(
        rows[endpoint["name"]]["khovanov_reduced_rational_vector"]
    ):
        assert field == 1
        result[sign * h, sign * q] += rank
    return result


def allowed(v, w, maximum=None):
    lo, hi = sorted((v, w))
    dq = hi[1] - lo[1]
    return (
        hi[0] == lo[0] + 1
        and dq > 0
        and dq % 2 == 0
        and (maximum is None or dq <= 2 * maximum)
    )


passed = failed = one_band = 0
for record in data["candidates"]:
    source, target = (polynomial(record[key]) for key in ("source", "target"))
    defect = {
        grade: target[grade] - source[grade]
        for grade in source.keys() | target.keys()
        if target[grade] != source[grade]
    }
    assert all(rank > 0 for rank in defect.values())
    matching = record["any_length_bars"]
    covered = Counter()
    for bar in matching["bars"]:
        lo, hi = tuple(bar["source"]), tuple(bar["target"])
        n, a = bar["multiplicity"], bar["length"]
        assert isinstance(n, int) and n > 0
        assert hi == (lo[0] + 1, lo[1] + 2 * a) and a > 0
        covered[lo] += n
        covered[hi] += n
    assert all(covered[g] <= defect.get(g, 0) for g in covered)
    assert sum(covered.values()) == matching["matched_rank"]
    if matching["pass"]:
        assert dict(covered) == defect
        passed += 1
    else:
        # Every failed case has an isolated grade, an immediate obstruction.
        isolated = [
            v for v in defect
            if not any(allowed(v, w) for w in defect if w != v)
        ]
        assert isolated
        failed += 1

    # Independently check each stored minimum cut against the graph capacities.
    cut = matching["min_cut"]
    reachable = {tuple(v) for v in cut["reachable_grade_vertices"]}
    assert cut["source_reachable"] and not cut["sink_reachable"]
    left = [v for v in defect if v[0] % 2 == 0]
    right = [v for v in defect if v[0] % 2 != 0]
    capacity = sum(defect[v] for v in left if v not in reachable)
    capacity += sum(defect[w] for w in right if w in reachable)
    capacity += sum(
        min(defect[v], defect[w])
        for v in left for w in right
        if v in reachable and w not in reachable and allowed(v, w)
    )
    assert capacity == cut["capacity"] == matching["matched_rank"] // 2

    quotient = record["one_band"]["quotient"]
    if record["one_band"]["pass"]:
        rebuilt = Counter()
        for h, q, n in quotient:
            assert n > 0
            rebuilt[h, q] += n
            rebuilt[h + 1, q + 2] += n
        assert dict(rebuilt) == defect
        one_band += 1

assert (passed, failed, one_band) == (48, 6, 42)
print("Verified 54 defects and matching/minimum-cut certificates.")
print("48 pass arbitrary-length pairing; 6 have isolated-grade obstructions.")
print("42 have independently reconstructed nonnegative one-band quotients.")
