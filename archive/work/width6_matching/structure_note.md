# Width-six e-type incidence structure

Scope: a tangle presented as two top caps, a six-strand braid, and two bottom cups, with exactly two arc components, e-type boundary connectivity, and no closed components. This is a statement about the given presentation's cap/cup incidence graph, not a geometric simplification theorem.

## Claim and proof

There is **exactly one short arc**, where “short” means it contains just one cap or cup edge (and the two incident braid segments).

Let the top-free-to-top-free arc contain r top caps. Because it starts and ends with a braid segment, its cap/cup edges alternate beginning and ending with bottom cups. It therefore contains r+1 bottom cups. Similarly, if the bottom-free-to-bottom-free arc contains s bottom cups, it contains s+1 top caps.

No closed component exists, so these two paths use all two top caps and all two bottom cups. Hence

    r + (s+1) = 2,     (r+1) + s = 2,

and r+s=1. Since r,s are nonnegative integers, either (r,s)=(0,1) or (1,0).

- First case: the top-to-top arc has (top caps,bottom cups)=(0,1), and the other arc has (2,1).
- Second case: the top-to-top arc has (1,2), and the other arc has (1,0).

In particular, both arcs cannot be short under the no-closed-component hypothesis. With closed components that conclusion need not hold: an unused cap and cup can form a closed component.

## Retrospective check

`structure_check.py` uses exactly the 222 archived words and their original 81 cap-index pairs from `work/width6/probe_results.json`. It generates no new braid words and computes no Jones coefficients. It traces paths independently in the 12-vertex incidence graph, then compares boundary connectivity and closed-component counts against `probe.geometry` for every archived word/cap pair.

| Archived domain | Count |
|---|---:|
| All word/cap pairs | 17,982 |
| E-type pairs, including closed components | 4,572 |
| E-type with closed components | 1,613 |
| E-type, exactly two arcs, no closed components | **2,959** |
| Short arc is a single bottom cup | 1,487 |
| Short arc is a single top cap | 1,472 |

All **874** saved Jones-zero two-arc cases pass: **445** have a single-bottom-cup short arc and **429** a single-top-cap short arc. There are no failures. The per-record output preserves original word index and candidate index, word and cap indices, ordered incidence path, edge counts, the short arc's boundary side, and its one cap/cup edge.

All three saved Long–Paton completions (tau=1,sigma1^2,sigma1^-2; top cap index2,bottom cup index7) have the **single top cap (56)** as their short arc, connecting bottom-free endpoints5,6 through the braid. The top transport tau fixes that cap.

Certificate: `structure_check.json`.

## What is not implied

“Short” counts cap/cup pieces only. The two incident braid strands can wind extensively; the statement does not bound crossings or imply boundary-parallelism. It neither proves the proposed split criterion nor proves that slides/isotopies can eliminate all configuration matchings for every split tangle. Those are separate geometric claims.

## Fixed-representative matching criterion from endpoint winding

Let source arcs be c1,c2 and target cap figure-eight loops be gamma1,gamma2. Assume the standard geometric hypotheses: source arcs are disjoint, the two target loops have disjoint supports, intersections are transverse, and gamma_j has puncture winding +1 and -1 at its two cap endpoints and zero at every other puncture. Loops may be parametrized immersed cycles; unsigned intersection counts include their preimages.

Put N_ij=|c_i intersect gamma_j|. Oriented intersection of an open arc with a closed loop is the difference of the loop's endpoint winding numbers, up to the common orientation convention. Consequently

    N_ij >= |wind_gamma_j(start(c_i)) - wind_gamma_j(end(c_i))|.

The matching count for this fixed representative is

    permanent(N) = N_11 N_22 + N_12 N_21.

If the short arc belongs to the SOURCE system, it joins the two target-free punctures. The complementary source arc must join endpoints belonging to distinct target caps: joining the two endpoints of one target cap would create a closed cap-cup component. Therefore both entries of the complementary row are at least1, by the winding inequality. Since all entries are nonnegative,

    permanent(N)=0  iff  both entries of the short-source row vanish.

If the short arc belongs to the TARGET system, its endpoints are the source-free punctures. The complementary target cap must join one endpoint of each source arc, again because otherwise there is a closed component. Both entries in its column are therefore at least1. Hence

    permanent(N)=0  iff  both entries of the short-target column vanish.

This supplies an exact reduction of empty matching support to one short row or column, for each representative satisfying these hypotheses. In the target-short case, the conclusion is that the **figure-eight loop around the short cap** misses both source arcs. It must not silently be replaced by disjointness of the cap core, existence of a three-dimensional splitting disk, or an unwinding theorem modulo cap slides. Those implications remain separate geometric questions. The argument uses no Jones polynomial and asserts no signed-sum nonvanishing when the permanent is positive.
