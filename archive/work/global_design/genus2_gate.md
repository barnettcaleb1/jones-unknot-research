# Genus-two mutation as a symmetry/primeification gate

2026-11-03. Bounded theoretical pass, no computation. Scope: arbitrary closed genus-two mutation surfaces disjoint from a classical knot, not only handlebody mutations.

**Outcome:** genus-two mutation cannot turn a nontrivial double J#J^r or J#mirror(J) into a hyperbolic knot, a torus knot, or the unknot. If a finite sequence turns such a double into a prime knot, that prime knot must be a satellite. This pass found neither a universal construction of that remaining kind nor a theorem ruling it out. The hyperbolic primeification proposal is therefore dead; prime satellite primeification remains an unestablished gate.

## 1. Read the erratum before using the topology reduction

[DGST, NYJM 2010](https://nyjm.albany.edu/j/2010/16-7v.pdf), Proposition 2.7, asserts that general knot mutation reduces to handlebody mutation (or torus versions/triviality). **That proposition is false.** Its Corollary 2.8 was not established. The [2012 erratum](https://nyjm.albany.edu/j/2012/18-5v.pdf) gives a genus-two surface incompressible in a knot exterior which bounds no handlebody in S^3. The erratum repairs all-colored Jones invariance directly with the skein of F×I, and recovers Alexander invariance by Melvin–Morton–Rozansky. Generalized signatures remain unproved in this full scope; the handlebody case survives.

Thus the sentence “every embedded genus-two surface in S^3 either bounds a handlebody or compresses on both sides,” used in older accounts of mutation, cannot serve as a reduction. Nor may one assume a chosen compression disk avoids the knot. Compressibility in S^3 and compressibility in E(K) are different conditions.

## 2. What does survive, with exact hypotheses

DGST Proposition 2.1 and Remark 2.2 are not withdrawn: if a genus-two F is compressible in an orientable M, its mutation either reduces to mutation along one/two incompressible nonboundary-parallel tori, or gives M itself; in the last case the boundary-torus identification is identity or elliptic. This is a reduction **inside M**, not the false handlebody assertion.

For hyperbolic M, Ruberman's theorem preserves hyperbolicity and volume under incompressible symmetric-surface mutation. The compressible case adds nothing: a hyperbolic manifold is atoroidal, so Proposition 2.1 gives the unchanged manifold. Hence arbitrary genus-two mutation of a hyperbolic knot remains hyperbolic. This full statement is also explicitly recorded as Theorem 2.2 in [Moore–Starkston, AGT 2015](https://msp.org/agt/2015/15-1/agt-v15-n1-p02-p.pdf), citing Ruberman. No Gromov-norm-only inference is being used here.

The corrected DGST Theorem 3.2 says all reduced colored Jones polynomials are unchanged. In particular ordinary Jones is unchanged. Thus if L is any genus-two mutant of J#J^r,

    J_N(L) = J_N(J)^2   for every color N.

For J#mirror(J), the corresponding formula is J_N(L;q)=J_N(J;q)J_N(J;q^-1). These identities preserve the colored-information gap; they do not propagate J_2=1 to higher colors.

## 3. The hyperbolic obstruction, including finite mutation sequences

Mutation is reversible: mutating the same surface a second time restores the first manifold and knot. Therefore hyperbolicity preservation is an if-and-only-if statement on every mutation edge. It follows along every finite sequence.

If J is nontrivial, J#J^r and J#mirror(J) are composite, hence not hyperbolic. Consequently none of their genus-two mutants can be hyperbolic, even after several mutations along newly chosen surfaces.

This is stronger than invariance of simplicial volume. A composite knot can already have positive simplicial volume from hyperbolic summands; equality of that number alone would not exclude a hyperbolic mutant. The argument instead uses preservation of the entire hyperbolicity property and reversibility.

## 4. The unknot obstruction

Here is a short deduction independent of any Jones detection theorem. Let F lie in E(U), a solid torus. No closed genus-two surface can be incompressible there: incompressibility would inject its surface group into pi_1(E(U))=Z, impossible. No incompressible torus exists there either, by the same argument. The surviving Proposition 2.1 therefore puts the mutation in its unchanged-manifold case. Remark 2.2 preserves the meridian slope up to sign, so the resulting knot is U.

By reversibility, no nontrivial knot can become U through any finite genus-two mutation sequence. Thus this is not an operation for manufacturing a Jones-trivial counterexample by mutating a complicated diagram of U.

## 5. The torus-knot obstruction for doubles

Normalize Alexander polynomials symmetrically. Reversal and mirror leave the normalized Alexander polynomial unchanged, so both doubles have Delta=Delta_J^2. Corrected Alexander invariance preserves this square throughout the mutation class.

For a nontrivial torus knot T(p,q), with |p|,|q|>1 and gcd(p,q)=1, the usual formula, up to a monomial unit, is

    Delta_T(t) = (t^(|pq|)-1)(t-1) / ((t^|p|-1)(t^|q|-1)).

Every surviving nonzero root is simple; equivalently every cyclotomic factor occurs at most once, and Phi_|pq| occurs exactly once. A square Laurent polynomial has even multiplicity at each nonzero root. Therefore a nontrivial torus knot cannot have Alexander polynomial Delta_J^2, including when Delta_J=1. The formula and the Phi_pq observation are explicitly recalled in [PJM 285 (2016), Example 2.2](https://msp.org/pjm/2016/285-2/pjm-v285-n2-s.pdf).

Combining this with Sections 3–4 and the hyperbolic/torus/satellite trichotomy proves the claim in the opening paragraph: **every prime genus-two mutant of a nontrivial double must be a satellite.** This is a deduction from known results, not a novelty claim.

## 6. Why the remaining prime/composite question is not answered here

Conway mutation preserves the branched double cover, so the reducible-cover obstruction controls prime/composite behavior there. Genus-two mutation does not generally preserve that cover. Moore–Starkston Proposition 2.3 (Proposition 4 in the arXiv version) exhibits differing double covers for the genus-two mutant pair 14n22185/14n22589. Therefore the Conway argument cannot simply be copied.

A possible independent obstruction would be preservation of an essential meridional annulus. Such an annulus detects connected sum. For an incompressible mutation surface F one can make its intersections with a decomposing annulus essential circles, and the hyperelliptic involution preserves their unoriented isotopy classes. That is not yet a proof: parallel intersection curves may be permuted, pieces can reglue differently, and one must prove an essential meridional annulus survives rather than merely some annuli/tori. I did not establish this step and do not label primeness invariant.

Likewise, a proposed construction has to exhibit an actual prime satellite mutant and prove primeness; polynomial equality comes for free, but topology does not. No such construction from arbitrary J was found in this bounded read. This is an unresolved gate in this investigation, not a claim that the question is unpublished or open in the literature.

## 7. Genus is not a replacement invariant

Conway mutation changes Seifert genus (the Kinoshita–Terasaka/Conway examples), and each Conway mutation is a composition of at most two genus-two mutations. Hence genus cannot be invariant under every genus-two mutation. Primary references are [Ozsváth–Szabó, Knot Floer homology, genus bounds, and mutation](https://arxiv.org/abs/math/0303225) and DGST Lemma 2.5. This is consistent with unknot preservation: genus can change between positive values while genus zero remains isolated.

## Recommendation and exact remaining route

Do not pursue “double, then genus-two mutate to a hyperbolic prime knot.” It contradicts hyperbolicity preservation. The only unresolved version found is “double, then mutate to a prime satellite with an exploitable inversion.” It requires (a) an actual mutation construction, (b) proof of prime satellite topology, and (c) a useful symmetry or detection theorem. None of these three gates is supplied merely by colored-Jones invariance. The fixed-pattern satellite obstruction from the sibling task should not automatically be extended to such an adaptive construction.

No scaffold changes. Published facts are identified by citations; Sections 3–5 contain explicit deductions; the essential-annulus step and universal prime-satellite construction remain OPEN in this investigation.
