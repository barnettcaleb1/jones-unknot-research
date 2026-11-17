# A global route through planar projection matrices

**Update after the one-page follow-up (Codex110650):** the enumerator is exactly the signed planar Tutte state sum; the checkerboard projection interpretation was already in the cited literature. The simplest geometric blocks lift to established RI/RII moves (up to graph-reembedding mutations), but the infinite wheel family of descending unknot diagrams has none of them, even after matroid-preserving moves. That forced-block variant is REFUTED. Further development is PARKED unless a specific matroid-changing geometric mechanism is supplied; the broader route remains OPEN. See projection_codes.md, projection_geometry.md, and projection_prior.md in this directory.

Design round, no computation. This is a proposed mechanism with an explicit missing lemma, not a proof or a novelty claim. I found one concrete alternative framework worth developing; I would not manufacture a second equally credible route merely to meet a count. The parent's Turaev-surface proposal can serve as the distinct second route.

## 1. The exact dictionary has real classical content

Let a one-component knot diagram have n crossings. Its traversal gives a single double-occurrence Gauss word. Let B be its symmetric zero-diagonal binary interlacement matrix and L the diagonal matrix recording negative crossings. Set delta=-A^2-A^-2. The normalized-circle bracket is exactly

    <D> = sum_(E diagonal binary)
          A^(n-2 rank(E)) delta^(nullity(B+L+E)).

The rank of diagonal E is its Hamming weight. The Jones normalization is multiplication by (-A^3)^(-w), with w=n-2 rank(L). Thus Jones one means this full nullity sum is the single monomial (-A^3)^w. This is the graph-bracket formula of [Traldi-Zulli, arXiv:0808.3392, Definition 3 and its knot specialization](https://arxiv.org/pdf/0808.3392); the circuit/nullity relationship is developed in [Traldi, arXiv:0903.4405](https://arxiv.org/pdf/0903.4405).

Crucially, classical planar realizability is an additional algebraic equation: there exists a diagonal D0 such that

    P=B+D0,                 P^2=P over F_2.

This is [Shtylla-Traldi-Zulli, On the realization of double occurrence words, Theorem 2](https://arxiv.org/abs/0709.2933), reformulating Rosenstiehl's criterion. It is not just the necessary even-degree condition. Virtual Gauss words need not admit such a completion.

Put c=diag(L+D0), and define the projection nullity enumerator

    N_(P,c)(u,v)=sum_(x in F_2^n)
                  u^(weight(x+c)) v^(nullity(P+diag(x))).

Then <D>=A^n N_(P,c)(A^-2,delta). This is an integer polynomial with nonnegative coefficients BEFORE the Jones specialization. P is a symmetric projection, so im(P) and ker(P) are orthogonal complementary binary codes. In coding terminology im(P) is a linear complementary-dual code. The specified coordinate basis and circle-graph realization remain essential data; arbitrary change of binary basis does not preserve the Jones specialization.

There is an authentic biology connection: the interlace polynomial grew out of Euler-circuit ambiguities in DNA reconstruction. [Arratia-Bollobas-Coppersmith-Sorkin, Euler circuits and DNA sequencing by hybridization (2000)](https://doi.org/10.1016/S0166-218X(00)00190-6) uses precisely such interlacement decompositions. The mathematics here is the circuit-reassembly structure, not an analogy about knotted DNA.

## 2. Proposed route to T

1. Encode an arbitrary classical K by its one-circle Gauss word, signs, and idempotent completion P. **Published.**
2. Translate V_K=1 into the projection-nullity enumerator's monomial identity. **Published dictionary / direct substitution.**
3. Prove a **cancellation-to-reduction lemma** inside the realizable projection locus: the monomial identity produces a coordinate block that can be isolated by geometrically realizable pivots/chord mutations and then removed by a disk/bigon simplification. **OPEN, main crux.**
4. Supply a well-founded complexity for those moves, including any temporary stabilizations needed, so repeated removal ends at the zero-crossing word. **OPEN, separate termination gate.**
5. Lift the permitted word moves to actual knot isotopies, allowing Conway mutation if useful; mutation cannot turn a nontrivial classical knot into the unknot because it preserves the branched double cover and the S^3 cover detects the unknot. **Known endpoint, but every proposed new matrix move needs its own geometric lift.**

What is new to our board is the extra equation P^2=P interacting with a weighted nullity enumerator, rather than a free signed state sum or a bare Euler characteristic. It is an avenue for using classicality before cancellation, not after it. No inference from a nonnegative enumerator to positivity on the Jones curve is justified.

## 3. The exact crux to try first

Do not start by conjecturing that every nonempty Jones-unit diagram has an immediately removable crossing. Hard unknot diagrams make monotone local simplification an inadequate target. Nor is the graph-bracket pivot recurrence an isotopy: it is generally a sum of smaller graphs, so replacing a graph by one term would be false.

The first useful theorem would be a lifting statement for a PARTICULAR algebraic cancellation block: characterize which rank-one or rank-two diagonal perturbations of a realizable symmetric projector yield a Jones-state cancellation, and prove that this cancellation can be implemented by a specified local disk move, after a specified stabilization if needed. The geometric move must retain the cyclic Gauss-word realization and the signs, not only the unlabeled matrix. Then identify a complexity that decreases for that enlarged move.

Cheap falsification, before a broad theorem: hand-check the proposed block rule on positive/negative curls, an oppositely signed Reidemeister-II pair, and one published hard unknot diagram. Also compare with a known Jones-trivial virtual knot: the proof must visibly fail either P^2=P or the geometric-lifting condition. If the rule is merely a graph pivot preserving the polynomial, it has not passed this test.

## 4. Barrier and feasibility assessment

- B1: one knot component supplies one unmarked traversal circuit. For general links the graph bracket needs an Euler system with extra marks; omitting this distinction would wrongly include EKT links.
- B2: idempotent completion is exactly the planar Gauss-word constraint. Matrix operations must preserve a classical realization, and the mutation endpoint uses classical branched covers.
- B5: the proposed bridge is a geometric disk move extracted from a matrix cancellation block; it is OPEN, not supplied by the polynomial dictionary.
- B8: a successful all-diagram reduction would implicitly establish the required quantum faithfulness consequences. This remains hard even though its input is binary linear algebra.

My judgment: this is a more specific global candidate than generic positivity because it identifies a usable equation absent for virtual knots and an exact transition polynomial. It is not yet a complete mechanism: the local lifting lemma and termination are both missing. One page should be spent on a single cancellation block and its geometry, not a numerical survey of projection matrices. If no geometrically meaningful block emerges, park it as a dictionary rather than escalating the claim.
