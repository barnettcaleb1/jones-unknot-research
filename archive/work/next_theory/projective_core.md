# A bounded core for projective graphs of bounded local crossing complexity

Theory-only derivation, 2026-11-03. Status: written argument for parent review; novelty unassessed.

This uses the spin interpretation in projective.md. It is not a proof of the Boyle–Spyropoulos breadth conjecture.

## Proposition: explicit core bounds

Let G be a finite connected graph embedded in RP2. Loops and parallel edges are allowed. Let

- v be its number of vertices;
- l be its number of homologically trivial loops;
- p be its number of homologically essential loops;
- m be its number of non-loop edges;
- alpha(G) be its minimum edge-deletion number to a local graph;
- b(G)=|E(G)|-alpha(G).

If b(G)<=B, deleting all p essential loops leaves a connected embedded core G0 with

    v <= B-l+1 <= B+1,
    m <= 2(B-l),
    |E(G0)|=m+l <= 2B-l <= 2B.

There are consequently only finitely many abstract signed cores for each B. A choice of extra Tait crossing sign on each surviving edge does not affect this finiteness.

### Proof

Choose the sphere-cover edge cocycle omega and write s for a binary spin on each vertex. The previous dictionary gives

    b(G)=max_s |{e=uv : omega(e)=s(u)+s(v)}|.

Every local loop is satisfied and every essential loop is unsatisfied, for every s. Each non-loop edge is satisfied with probability 1/2 under independent uniform spins. Taking the expected number of satisfied edges yields

    b(G)>=l+m/2.

Independently, choose a spanning tree and assign spins recursively to satisfy all its edges. The l local loops remain satisfied. Hence

    b(G)>=l+v-1.

The displayed bounds follow. Deleting only loops does not disconnect G. This proof allows multiple edges; no simple-graph version of an Edwards–Erdos bound is assumed.

## What can be said about the embedding

The preceding abstract bound is not yet a classification of the full embedded graphs: an arbitrary number of essential loops has been removed. The following explicit argument controls their placement up to parallel insertions.

### Lemma: all essential loops share one vertex

Two essential simple closed curves in RP2 have mod-two intersection one. If essential loop edges had distinct base vertices, their embedded images would be disjoint, contradicting that pairing. Thus there is at most one vertex supporting essential loop edges.

This observation is also stated in Boyle–Spyropoulos §4, immediately before their terminal-diagram types; it is not claimed as a new fact.

### Lemma: only boundedly many essential-loop separators need be retained

Suppose p>0, and let w be their common vertex. Remove a sufficiently small open disk around w. Its complement is a Möbius band. Each essential loop edge becomes an essential properly embedded arc in that band. These arcs are disjoint, and essential proper arcs of a Möbius band are parallel: cutting along one produces a disk, and the remaining disjoint essential arcs run successively between its corresponding boundary pieces.

Thus p such arcs cut the Möbius band into p disk regions. Restore the rest of G0 outside the vertex disk. Each region which is not empty of that graph contains at least part of a core edge. Each core edge lies in one region, since it cannot cross any of the loop arcs. Therefore at most R=|E(G0)| of these disk regions are occupied.

If a region is empty, deleting one of its bounding essential arcs merges this empty region with its neighbor, without merging two occupied regions. Repeating leaves at most max(1,R) essential arcs, retaining one even when every region was empty. On restoring the vertex disk, the deleted loop edges can be recovered by parallel insertions in the resulting bigon bands. This is an actual loop-order argument, not an assumption that abstract parallel edges must be geometrically parallel.

Consequently G has a reduced embedded template H with

    |V(H)| <= B+1,
    |E(H)| <= R+max(1,R).

For B>=1 this is at most 4B; for B=0 the possibilities reduce to one vertex with no essential loop, or one retained essential loop. The original G is obtained from H by reinserting parallel essential-loop edges along specified bands.

### Finiteness statement and its scope

For these bounded templates, the finite abstract graph, cyclic order of half-edges at each vertex, and edge-band twist data have only finitely many possibilities. Complementary-region data in RP2 also have only finitely many possibilities: the total available nonorientable genus is one. Thus the reduced embedded templates form a finite set up to ambient homeomorphism of RP2.

This does not assert that the original graphs form a finite set: parallel multiplicities remain unbounded. Nor does it yet give a finite integer-parameter normal form for arbitrary signed link diagrams. The inserted edges carry Tait crossing signs which may form arbitrary words; identifying their allowed Reidemeister-II cancellations and their effect on the marked link is an additional diagrammatic step. The result proved here is a finite embedded-template reduction with parallel insertions, with that further issue explicit.

## Prior art and use

[Boyle–Spyropoulos, arXiv:2609.40122v1, proof of Theorem 5.3](https://arxiv.org/html/2609.40122v1#S5.SS2), already observes v<=b+1 and describes inductive enumeration with projective-loop parameters, carrying it through b<=2. The finite-family strategy is therefore theirs. The random-spin proof above adds a convenient explicit bound on all non-loop core edges and a direct explanation of the retained-loop template bound; priority of these quantitative formulations has not been checked.

The bounds apply to any diagram realizing a given local-crossing bound beta(L)<=B, but do not give that bound from its Jones polynomial. The still-open step is the breadth-to-beta implication. In particular this proposition is a structural reduction at fixed B, not a solution or a decrease theorem for arbitrary B.
