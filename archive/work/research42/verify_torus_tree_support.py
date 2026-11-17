#!/usr/bin/env python3
"""Verify the actual T(3,5) support-matching countertest.

Run from any directory with the workspace's installed Spherogram/networkx.
This computes the localized Roberts--Jaeger differential SUPPORT, not its
rational-function matrix rank.  Homology rank seven is a cited theorem/example.
"""
import collections
import itertools
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT / "work/braid_classification/packages"))
from spherogram import Link
import networkx as nx

saved = json.loads((HERE / "torus_tree_support.json").read_text())
word = [1, 2] * 5
link = Link(braid_closure=word)
pd = [list(row) for row in link.PD_code()]
assert pd == saved["pd"]
assert link.is_planar()
assert len(link.link_components) == 1
assert sum(c.sign for c in link.crossings) == 10
assert Link(pd).is_planar() and len(Link(pd).link_components) == 1
N = len(pd)
labels = sorted(set(itertools.chain.from_iterable(pd)))
assert labels == list(range(2 * N))
assert all(v == 2 for v in collections.Counter(itertools.chain.from_iterable(pd)).values())

def circles(mask):
    parent = list(range(2 * N))
    def root(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    def join(a, b):
        parent[root(a)] = root(b)
    for i, (a, b, c, d) in enumerate(pd):
        if (mask >> i) & 1:
            join(b, c); join(d, a)
        else:
            join(a, b); join(c, d)
    result = collections.defaultdict(set)
    for a in labels:
        result[root(a)].add(a)
    return list(result.values())

resolutions = {m: circles(m) for m in range(1 << N)}
states = [m for m, components in resolutions.items() if len(components) == 1]
state_set = set(states)
assert states == saved["states"]
assert len(states) == 121
counts = dict(sorted(collections.Counter(m.bit_count() for m in states).items()))
assert counts == {2: 25, 4: 50, 6: 35, 8: 10, 10: 1}

# Put a different indeterminate x_a on EACH diagram arc a != 0.  Arc zero
# contains the basepoint.  The two intermediate unmarked circle weights are
# nonzero linear polynomials, and 1/w1+1/w2 != 0 in F_2(x_a) iff w1 != w2.
# Thus comparing their arc sets computes support EXACTLY, not by sampling.
support = []
weights = {}
for S in states:
    unset = [i for i in range(N) if not ((S >> i) & 1)]
    for i, j in itertools.combinations(unset, 2):
        T = S | (1 << i) | (1 << j)
        if T not in state_set:
            continue
        intermediate = [resolutions[S | (1 << k)] for k in (i, j)]
        assert all(len(C) == 2 for C in intermediate)
        C1, C2 = [next(c for c in C if 0 not in c) for C in intermediate]
        assert C1 and C2
        if C1 != C2:
            support.append((S, T))
            weights[(S, T)] = [sorted(C1), sorted(C2)]
assert support == [tuple(e) for e in saved["nonzero_support"]]
assert len(support) == 500

# This is a graph on the ACTUAL 121 generators.  It is not the doubled
# row/column graph of a square matrix.  Every pair uses two distinct generators.
G = nx.Graph()
G.add_nodes_from(states)
G.add_edges_from(support)
left = {s for s in states if ((s.bit_count() - 2) // 2) % 2 == 0}
assert len(left) == 61
assert all((s in left) != (t in left) for s, t in support)
matching = [tuple(e) for e in saved["matching"]]
assert len(matching) == 60
assert all(G.has_edge(s, t) for s, t in matching)
endpoints = list(itertools.chain.from_iterable(matching))
assert len(endpoints) == len(set(endpoints)) == 120
assert len(nx.algorithms.bipartite.maximum_matching(G, top_nodes=left)) // 2 == 60

# Algebraic Morse acyclicity reverses matched differential arrows only.
# Differential arrows here increase |S| by two; reversing ALL arrows would
# give the same cycle/no-cycle answer under the opposite chain convention.
matched = {frozenset(e) for e in matching}
gradient = nx.DiGraph()
gradient.add_nodes_from(states)
for s, t in support:
    gradient.add_edge(t, s) if frozenset((s, t)) in matched else gradient.add_edge(s, t)
assert not nx.is_directed_acyclic_graph(gradient)
cycle = nx.find_cycle(gradient)
assert cycle[-1][1] == cycle[0][0]
cycle_details = []
for s, t in cycle:
    pair = (s, t) if (s, t) in weights else (t, s)
    cycle_details.append({
        "from": s, "to": t,
        "from_cardinality": s.bit_count(), "to_cardinality": t.bit_count(),
        "reversed_matching_edge": frozenset((s, t)) in matched,
        "two_unmarked_arc_sets": weights[pair],
    })
report = {
    "braid_word": word, "pd": pd, "planar": True, "components": 1, "writhe": 10,
    "states": len(states), "cardinality_counts": counts,
    "nonzero_support_edges": len(support),
    "global_matching_pairs": len(matching), "distinct_matched_generators": len(set(endpoints)),
    "unmatched_generator": list(state_set - set(endpoints)),
    "gradient_is_acyclic": False, "directed_cycle": cycle_details,
    "homology_rank_7": "Source-backed (Roberts p.18 and Jaeger Corollary 3.2), not computed by this script",
    "differential_rank_57": "Consequent (121-7)/2, not a matrix-elimination claim",
}
(HERE / "torus_tree_support_verification.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps({k: report[k] for k in (
    "planar", "components", "writhe", "states", "cardinality_counts", "nonzero_support_edges",
    "global_matching_pairs", "distinct_matched_generators", "unmatched_generator", "gradient_is_acyclic")}, indent=2))
print("Explicit directed cycle:", " -> ".join(str(s) for s, t in cycle) + " -> " + str(cycle[0][0]))
