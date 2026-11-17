# Projection blocks and actual diagram reductions

Theory page for G1-PLANAR, 2026-11-03. No enumeration. Conclusion: the natural checkerboard projection is the binary cut/cycle projection; rank-one and an explicit rank-two block do have geometric reductions (the latter up to mutation). Jones-flatness does not force either block, even after all matroid-preserving rearrangements.

## 1. The natural projector is graphic

Let G be a connected plane Tait graph of a one-component diagram, with n edges. Work over F2. Let D be a vertex-edge incidence matrix with one vertex row deleted. Loops have zero columns. Write C=im(D^T) for the cut space and Z=ker(D) for the cycle space.

[Silver-Williams, Theorem 1.1](https://arxiv.org/pdf/1408.6815) identifies the number of medial-link components with the nullity of the full mod-two graph Laplacian. Thus the knot assumption makes the full Laplacian have nullity one. Its reduced Laplacian DD^T is invertible: the full matrix has kernel spanned by the all-ones vector, so its nonzero adjugate is the all-ones matrix, and every principal cofactor is 1. Consequently

    P_cut = D^T (DD^T)^(-1) D

is a symmetric idempotent with image C and kernel Z. In particular C intersect Z=0. Its complementary projector P_cycle=I+P_cut has image Z and kernel C.

These are the checkerboard projectors in the final Remark of [Shtylla-Traldi-Zulli 0709.2933](https://arxiv.org/pdf/0709.2933). Their construction removes a disk at each crossing, identifies its boundary antipodally, and splits the resulting closed nonorientable surface along the embedded original curve. The two pieces retract onto the two checkerboard graphs. A graph cycle maps to its edge-indicator vector in the crossing basis of H1, so their homology images are the cycle spaces of G and G*, i.e. Z and C. The projections have off-diagonal part equal to the original Gauss interlacement matrix B, as stated in that Remark.

Thus, for a FIXED checkerboard realization, P_cut=B+D0 or its complement is the natural completion. Arbitrary diagonal completions should not silently be identified with that same marked checkerboard graph; their possible reinterpretation by blockwise planar duality is a separate bookkeeping point.

This is established theory, not a new positivity constraint beyond the one-component planar Tait graph.

## 2. Rank one: an isolated Gauss coordinate is nugatory

If row i of B is zero, then P_cut e_i is either 0 or e_i.

- P_cut e_i=0 puts e_i in Z. A cycle supported on one graph edge is a loop.
- P_cut e_i=e_i puts e_i in C. A cut supported on one edge makes that edge a bridge.

Conversely a loop or bridge gives the corresponding isolated coordinate. A loop or bridge in a plane Tait graph is a nugatory crossing. Removing its twist has the usual scalar curl bracket factor; writhe normalization removes that factor.

The geometry need not be an immediately empty Reidemeister-I monogon in the displayed diagram. A nugatory crossing can separate nonempty diagram pieces. The relevant move is the standard ball rotation at the nugatory crossing, giving an isotopic knot with that crossing removed. Calling every such coordinate an immediately visible curl would overstate the conclusion.

## 3. Rank two: twins are parallel or series pairs

Assume isolated coordinates have been removed. Suppose i,j have identical off-diagonal neighbors outside {i,j}. Put v=e_i+e_j and write p=P_ii, q=P_jj, b=P_ij. Then

    P v = (p+b)e_i + (q+b)e_j.

If p differs from q, Pv is one of e_i,e_j. Idempotence forces that basis vector to be fixed by P, and the other to be killed, so both B coordinates were isolated, a contradiction. Hence p=q and Pv=(p+b)v. Therefore v lies in C or Z.

With no loops or bridges, a two-edge vector in Z is a two-element circuit (a parallel pair); a two-edge vector in C is a two-element cocircuit (a two-edge bond, parallel in the dual). Conversely these two types give the identical-external-neighborhood block. This is a precise identification of the algebraic block with a graphic one.

### Geometric cancellation with signs

If a parallel pair has opposite TAIT edge signs, there exists a planar embedding of the same signed abstract graph in which the two edges bound an empty disk: remove one edge and redraw it in a narrow strip alongside the other. [Cheng-Gao, Theorem 4.1, Mutation on Knots and Whitney's 2-Isomorphism Theorem](https://doi.org/10.1007/s10114-013-0679-5) relates diagrams of the same signed abstract planar graph by isotopies and mutations. In the new embedding the empty signed bigon supports an actual Reidemeister-II move, deleting the pair.

For a two-edge cocircuit, apply the same reasoning to the planar dual; in the original graph the resulting operation contracts the pair. Here the relevant signs are the signed-Tait convention, not an unannounced substitution of oriented crossing signs. They must be carried along with the chosen checkerboard convention.

This is a genuine scoped geometric lifting theorem: **opposite-signed two-circuit/two-cocircuit cancellation is implementable by mutations followed by RII.** It is not necessarily an isotopy of the original knot before the RII step. That is adequate for an unknot-detection induction only because classical mutation preserves whether the knot is the unknot (e.g. through the double branched cover and the Smith endpoint).

The one-component/bicycle-free condition prevents the pair from being both a circuit and a cocircuit, which otherwise would put the same nonzero vector in C intersect Z. It also makes explicit why a disconnected graph after an alleged pair reduction is a warning to check the hypotheses.

## 4. The wheel obstruction: flatness does not force these blocks

The following construction was proposed by the root agent and checked directly here. Let W_m be the plane wheel with m rim vertices and a hub, m>=4 and 3 not dividing m. Delete the hub row from its binary Laplacian. The resulting matrix is

    I + adjacency(C_m).

A kernel vector satisfies x_(i+1)=x_i+x_(i-1). Every nonzero recurrence orbit over F2 has exact period three. Periodic boundary conditions of length m therefore force x=0 when 3 does not divide m. The reduced Laplacian is invertible, so the medial shadow is one-component by Silver-Williams.

Give this shadow a descending crossing assignment: traverse from a base point and make the first encounter at every crossing pass over. The resulting classical diagram is an unknot, hence has Jones polynomial 1, and its unsigned Tait graph is still W_m.

But W_m is simple and 3-connected, hence has no loops, bridges, two-circuits or two-cocircuits. Its cycle matroid is simple and cosimple. Those properties survive Whitney 2-isomorphisms and embedding changes. Consequently none of the rank-one/rank-two moves above can even start on this infinite family of actual Jones-unit diagrams after matroid-preserving rearrangements.

This refutes the tempting lemma “Jones-unit planar projectors always have a removable rank-one or rank-two block, up to Whitney/mutation rearrangement.” It does NOT refute a route allowing Reidemeister III / signed Delta-Y changes or temporary stabilizations that change the matroid. Such operations and a termination argument are additional indispensable content.

## Assessment

We now have actual geometry for the simplest algebraic blocks, but also a structural obstruction to forcing them from flatness. The equations reproduce the signed-graphic Reidemeister calculus; they have not supplied a new reduction principle. A next page would need a specified matroid-changing move and a Jones-sensitive reason that it exposes one of these blocks. Merely rephrasing the nullity identity in cut/cycle language does not do that.
