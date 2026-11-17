# Directed cobordism certificates for the one-unknot-closure problem

Date: 2026-11-03. Independent bounded pass by the cobordism agent.

**Result:** there are clean, proved *geometric finishing criteria* for Lemma Q using ribbon homology cobordisms. The zero-surgery criterion needs no polynomial or Floer assumption. A second criterion applies to any finite nonzero surgery when `a_2(kappa)=0`. Neither constructs a cobordism from a Jones equality. That bridge is OPEN and should be parked until there is an actual construction. These are deductions from published theorems, not a claim of research novelty.

## 1. Convention and the published input

Write `Y <=_r Z` when there is a compact oriented smooth cobordism `W:Y -> Z`, built relative to `Y` using only 1- and 2-handles, and both boundary inclusions induce rational homology isomorphisms. Direction matters.

Daemi–Lidman–Vela-Vick–Wong, *Ribbon homology cobordisms*, [arXiv:1904.09721v5](https://arxiv.org/html/1904.09721v5), Theorem 1.14 and Proposition 2.1 give

`pi_1(Y) -> pi_1(W)` injective, and `pi_1(Z) -> pi_1(W)` surjective.

This holds for compact 3-manifolds, including ones with boundary, without an irreducibility hypothesis. Theorem 4.10 gives a split injection on Heegaard Floer homology when `W` is a ribbon F_2-homology cobordism. Their Lemmas 3.1–3.2 supply the integral homology observations used below. These precise statements were checked in the primary paper.

## 2. The clean group-theoretic theorem

**Proposition A (cyclic terminal object).** For a knot `kappa` in `S^3`, the following are equivalent:

1. `kappa` is the unknot.
2. `S^3_0(kappa) <=_r S^1 x S^2`.
3. There is a ribbon rational homology cobordism, with product vertical boundary, from `E(kappa)` to a solid torus.

**Proof of 2 => 1.** Put `Y=S^3_0(kappa)`. The published fundamental-group theorem gives

`pi_1(Y) -> pi_1(W) <- Z`,

with the first map injective and the second surjective. Hence `pi_1(W)` is cyclic. Since `H_1(W;Q)=Q`, it is infinite cyclic. Thus `pi_1(Y)` is a subgroup of `Z`; because `H_1(Y;Z)=Z`, it is itself `Z`. An orientable closed 3-manifold with fundamental group `Z` is `S^1 x S^2` (prime decomposition, the sphere theorem and geometrization). Gabai's Property R theorem then gives `kappa=U`.

**Proof of 3 => 1.** The same argument gives `pi_1(E(kappa))=Z`. The knot-group characterization of the unknot gives `kappa=U`. The reverse implications use product cobordisms. QED.

No Jones equality, Euler characteristic, rank estimate, framing comparison, or deck-equivariance is used in Proposition A. In particular, the closed version requires an ordinary directed cobordism between the covers; it need not descend to a branch-set movie.

This is a finite *certificate target*: exhibit the handle diagram, check that the relative 1/2-handle incidence matrix has nonzero determinant over Q, and identify its upper boundary as `S^1 x S^2`. It is not an algorithm for producing that certificate from polynomial data.

## 3. A second finishing criterion using a_2=0

Normalize `Delta_kappa(t)=Delta_kappa(t^-1)` and `Delta_kappa(1)=1`, so `a_2(kappa)=Delta_kappa''(1)/2`.

**Lemma B.** A nontrivial knot in `S^3` admitting a finite nonzero L-space surgery has `a_2>0`.

**Proof.** Mirror the knot if necessary. The L-space-knot theorem gives strictly increasing positive integers `n_1<...<n_k=g(kappa)`, with `k>=1`, such that

`Delta(t)=(-1)^k + sum_{j=1}^k (-1)^(k-j) (t^(n_j)+t^(-n_j))`.

Consequently

`a_2 = n_k^2 - n_(k-1)^2 + n_(k-2)^2 - ... + (-1)^(k-1)n_1^2 > 0`.

Pair consecutive terms starting from the largest exponent; every pair is positive, and any unpaired term is positive. The mirror has the same Alexander polynomial. QED.

The Alexander/staircase input is Ozsvath–Szabo, [*On knot Floer homology and lens space surgeries*](https://arxiv.org/abs/math/0303017), together with the rational surgery formulation. The latter also appears explicitly in the primary surgery literature cited there; we are using the standard implication that any nonzero rational L-space surgery makes the knot or its mirror an L-space knot. The elementary strict positivity argument is included here rather than assumed.

**Proposition C (equal-order L-space terminal object).** Let `kappa` be a knot in `S^3` with `a_2(kappa)=0`. Let `p,q` be coprime with **`p != 0` and `q != 0`**. If

`S^3_(p/q)(kappa) <=_r Z`,

where `Z` is an L-space and `|H_1(Z;Z)|=|p|`, then `kappa=U`.

**Proof.** Let `Y=S^3_(p/q)(kappa)` and let `W` be the cobordism. Both ends are rational homology spheres. Lemma 3.1 of the primary paper gives an injection `H_1(Y;Z)->H_1(W;Z)` and a surjection `H_1(Z;Z)->H_1(W;Z)`. Since both end groups have order `|p|`, both maps are isomorphisms. The relative handle complex has equally many 1- and 2-handles and a square integral boundary matrix invertible over Q; it has zero relative H_2. The long exact sequence and the isomorphism on H_1 give zero relative H_1 as well. Thus `W` is a Z-homology cobordism, and hence an F_2-homology cobordism. This is the proof of DLVVW Lemma 3.2, with equal cardinalities rather than an a priori group isomorphism; cardinalities suffice.

The split injection on `HFhat` gives

`|p| <= dim HFhat(Y) <= dim HFhat(Z)=|p|`.

Thus `Y` is an L-space. Lemma B and `a_2(kappa)=0` force `kappa=U`. QED.

**Important exclusions.** `p=0` is the longitude and belongs to Proposition A, not Proposition C. `q=0` is the meridian/`infinity` filling: every knot has that `S^3` filling, so omitting `q!=0` would make the statement false.

**Group-only variant of the first step.** If the target is a lens space, with any homology order, `pi_1(Y)` is a subgroup of a quotient of a finite cyclic group. Therefore `Y` itself is a lens space, including `S^3`, and Lemma B finishes. More generally a target with finite fundamental group forces `Y` to be spherical, hence an L-space, and the same conclusion follows. The equal-order condition is needed for the general L-space target, not for the cyclic/finite-group target.

## 4. How these fit Lemma Q, and the single missing construction

For the established one-unknot-closure setup, `M=Sigma_2(X)=E(kappa)` is an actual knot exterior in `S^3`; the longitude closure `L` has `Sigma_2(L)=S^3_0(kappa)`. The project's existing U4 calculation gives `a_2(kappa)=0` on the rational-bracket locus. Those identifications are inherited inputs here, not re-proved by the cobordism result.

A complete conditional route is:

1. Rational bracket plus actual unknot closure gives the marked exterior `E(kappa)` and `a_2=0`. **INHERITED / TRUSTED.**
2. Construct either a ribbon Q-homology cobordism from the zero surgery to `S^1 x S^2`, or one from a finite nonzero surgery to an L-space of matching homology order. **OPEN; no construction obtained.**
3. Proposition A or C forces `kappa=U`. **PROVED DEDUCTION.**
4. The double branched cover is a solid torus, hence `X` is rational. **STANDARD CLASSICAL TANGLE INPUT.**

This changes the geometric certificate sought: a directed handle construction can replace direct identification of another filling. It does **not** make the missing step smaller by fiat. Merely stating that the Jones equality should produce the cobordism is a reformulation, not a mechanism, and should not be assigned repeated computations without a specific movie or handle construction.

## 5. Why the obvious band/ribbon shortcuts do not supply step 2

**The natural band trace has the wrong homology.** A coherent band move from the actual unknot to `L` gives a branched-cover cobordism from `S^3` to `S^3_0(kappa)` consisting of a single 0-framed 2-handle. Its relative second homology has rank one. It is not a homology cobordism. Calling the downstairs surface a ribbon annulus does not remove that handle. A cancellation or replacement that produces the required directed homology cobordism is substantive extra topology.

**Ribbon direction cannot be reversed.** A ribbon knot has a ribbon concordance `U -> kappa`. Its exterior gives the direction `solid torus -> E(kappa)`; after compatible zero fillings, it gives `S^1 x S^2 -> S^3_0(kappa)`. Proposition A requires the reverse direction. Turning the movie upside down changes 1/2-handles to 2/3-handles and loses the group-injectivity conclusion. Nontrivial ribbon knots are immediate controls against any direction-free argument.

**Ordinary homology cobordism is too weak.** A smooth concordance to the unknot induces integral homology cobordisms of zero surgeries in either direction. Nontrivial slice knots therefore satisfy the undirected version of the desired condition. Even `a_2=0` does not fix this: there are nontrivial slice knots with Alexander polynomial one, including the Kinoshita–Terasaka knot. The no-3-handles requirement is doing real work.

**Local knots and closed summands.** The actual unknot closure prevents a nontrivial local knot in the tangle: it would survive as a connected-sum factor of the closure. Upstairs, the actual `S^3` filling identifies the cover as an irreducible knot exterior. A bare bracket identity has neither consequence. Thus this argument does not overlook the earlier `solid torus # homology sphere` obstruction.

**Whitehead towers.** Untwisted Whitehead doubles have Alexander polynomial one, so their iterates pass `a_2=0` regardless of nontriviality. Whenever the companion is nontrivial and the satellite is nontrivial, Proposition C proves that none of its finite nonzero surgeries can admit the proposed ribbon cobordism to an equal-order L-space. Thus Alexander vanishing, low-order Jones information, or ordinary sliceness cannot manufacture this certificate. This is consistent with the archived tower obstruction, and it rules out promoting the certificate from finite jets alone.

**Categorical phantoms.** The earlier relative Lee-bar arguments and LATE-50's formal universal-Frobenius examples remain relevant: a split map, semisimple acyclicity, or zero Euler defect does not construct a directed geometric cobordism. The present proof uses an actual 4-manifold with specified handle indices, not an abstract categorical retract.

## 6. Assessment

Bank Propositions A and C as explicit sufficient criteria/deductions, with no novelty claim. Keep the bracket-to-cobordism bridge OPEN and PARKED. The positive connection is between the one-unknot-closure problem and the *direction* of geometric simplification: polynomial cancellation would have to be realized without introducing 3-handles. The residual-finiteness and representation-extension input then detects topology which ordinary Euler characteristics miss.

No new counterexample search, simulation, or scaffold edit was made in this pass.
