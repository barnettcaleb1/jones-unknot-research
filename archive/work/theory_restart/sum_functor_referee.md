# Referee report: the bullet functor and equivariant sums

15 November 2026. Independent Codex read of
`/Users/calebbarnett/jones-lanes/theory-restart/mech/sum/REPORT.md`, especially §§3–5.
Coefficients are a field, with characteristic two retained whenever the H-cone or the reported special-curve tensor calculation is used. No new knot enumeration was performed. This report does not certify the derived-quotient claims in §6.

## Verdict

Theorem A is correct. It has a short categorical proof that does not assume linearity of curves, short specials, a rational-component grading formula, or realizability by a tangle. Consequently the intrinsic bullet multiset is multiplicative under the compatible tangle sum. J-TILT is closed under that sum, and extremal parity coherence EXT holds for a sum if and only if it holds for both factors.

This is a genuine structural reduction for compatible sums. It supplies no new constraint on a sum-indecomposable quotient tangle, because exactly the same theorem applies to formal objects. In particular it cannot exclude the formal Euler-zero addition B.

The detailed short-special sum formula has a valid proof scheme, but a separate finite tensor calculation is one of its inputs. The existing log records that calculation; I have not independently certified its chain equivalence. The main J-TILT sum reduction should therefore be stated intrinsically and independently of that additional calculation. The report's claim that every B tensor T also violates the old special-only TILT does not follow from the supplied argument and must be removed unless separately proved.

## 1. Exact categorical input

The relevant external planar-functoriality statement is Bar-Natan, *Khovanov's homology for tangles and cobordisms*, Geom. Topol. **9** (2005), 1443–1499, Theorem 2, especially parts (2) and (3), and the tensor-totalization formula in its proof. It says that planar operations preserve chain homotopies and that the bracket respects those operations. [Primary text](https://arxiv.org/html/math/0410495v2).

For the two-object algebra model, the exact references in Kotelskiy–Watson–Zibrowius, *Immersed curves in Khovanov homology*, arXiv:1910.14584v2, are Definition 4.19 (the graded quiver algebra), Theorem 4.21 (its identification with the crossingless cobordism endomorphism category), and Observation 4.18 (delooping). These were checked in the locally archived primary TeX and PDF text, not only in the lens digest. [Paper](https://arxiv.org/abs/1910.14584v2).

Write b for the crossingless matching which is the horizontal-sum unit, and c for the other matching. The quiver's non-identity generators have quantum degrees −1 and −2. The degree-zero part of End(b) is precisely F id_b. The product of crossingless objects is

    b*b=b,  b*c=c*b=c,  c*c=(q+q^{-1})c,

where the last equality is the chosen delooping isomorphism. It is only an object identity; no claim is made that all structure maps are unchanged by gluing. KWZ explicitly warns that special-component changes affect some maps in general planar products. The proof below does not ignore that warning.

## 2. A proof of Theorem A that includes reductions

Let epsilon be the character of the quiver algebra sending id_b to 1, id_c to 0, and every negative-degree path to zero. The quiver relations show directly that this is a unital algebra homomorphism. Equivalently, on the additive two-object cobordism category use the functor F_b which sends b to F, c to zero, and a morphism b→b to its identity coefficient. It sends every morphism involving c to zero.

For a bounded finite bigraded complex X, define

    N_b(X) = H(F_b(X)).

This is homotopy invariant: an additive functor carries a chain homotopy equation to the corresponding equation after applying the functor. Thus the definition does not depend on a particular reduced type-D representative. On a reduced representative, all identity entries have been canceled, so F_b(X) has zero differential and N_b(X) is exactly the bigraded vector space on its b-generators. This also proves that their multiplicities are independent of the chosen reduced representative.

Before any cancellation in X*Y, the only b-labelled generators are pairs of b-labelled generators. Delooping c*c creates only c-labelled summands, so it cannot introduce extra b-labelled terms. The differential between two b-pairs is the usual sum of a differential in X and a differential in Y, extended by an identity in the other factor. Extending a morphism b→b by the unit object preserves its quantum degree and its identity coefficient: a negative-degree path remains negative-degree, while id_b is still id_b. It follows that

    F_b(X*Y) ≅ F_b(X) ⊗_F F_b(Y)

as bigraded complexes, with the standard total-complex signs. Applying Künneth over the field gives

    N_b(X*Y) ≅ N_b(X) ⊗_F N_b(Y).

Any later cancellation or reduction of X*Y is harmless by homotopy invariance of F_b. In particular one must not infer the theorem merely by counting the generators of an unreduced tensor product; it is the augmented complex and Künneth that justify the invariant count.

The proof works over arbitrary fields for this particular functor. No assertion about the correctness of kht++ `--sum` in other characteristics is needed or implied. The subsequent H-cone/special calculation below remains characteristic two.

## 3. Exact consequences independent of special lengths

Use the intrinsic multiset of bigradings of N_b, with the overall grading normalized by the actual unknot closure. The normalization shifts add under a compatible sum. There is no need here to identify the shifts with the report's empirical labels (24j,4j).

The multiset for a sum is its factors' Minkowski sum, with multiplicities multiplied. This immediately proves closure of J-TILT by the report's correct finite-level extremum argument. The argument is combinatorial: at adjacent sum levels, lower an available factor level to compare maxima; raise an available factor level to compare minima.

EXT also has an exact converse. The top quantum part of N_b(X*Y) is the tensor product of the top quantum parts of N_b(X) and N_b(Y), and likewise at the bottom. A tensor product of two nonzero Z/2-graded vector spaces is concentrated in one parity if and only if both factors are. Hence

    EXT(X*Y) iff EXT(X) and EXT(Y).

In particular the formal B, whose extreme bullet support has both parities, continues to violate EXT after multiplication by any object with nonzero N_b. It consequently violates J-TILT, since J-TILT implies EXT.

**Correction to the sum report:** this does not prove failure of the older TILT(S) for B*X. Special-only TILT is weaker than J-TILT and need not make the full bullet extrema coherent. The sentence in §5 deriving all three failures from EXT co-closure overstates its inference.

A minimal failure among tangles admitting a compatible equivariant-sum decomposition must occur in a factor. This is not a reduction to all topologically prime knots: summand-exchanging inversions and quotient tangles with no such decomposition remain outside this operation.

## 4. The stronger short-special sum formula

The following is a sound conditional proof of the report's additional result. It makes clear which finite computation is still separate from Theorem A.

Assume the quotient-tangle structure theorem, both factors have only the fixed rank-one short special S at infinity, and the exact universal tensor identity S*S is the four-short-special direct sum displayed in `kht/run_s4_s4.log`.

First, the rational slope k is additive. Over F_2, H acts as a handle on any component. This follows from the neck-cutting relation: a handle on a non-special component is 2 times a dot minus H, which equals H in characteristic two. Therefore taking the H-cone commutes with horizontal product. The rational component r_1(k_2) of Kh(T_2) is Kh(Q_{k_2}), up to its specified overall grading. Thus the product contains Kh(T_1+Q_{k_2}) as a direct summand. Mapping-class naturality identifies its rational component with r_1(k_1+k_2). Uniqueness of the rational component for a tangle with unknot infinity closure gives k_{12}=k_1+k_2. No trefoil computation is needed for this step.

For closure of the short-special class, put Y=BN(T_1)*S and C=q⊕h^{-1}q^{-1}. The null-homotopy H id_S≈0 gives

    Y⊗C ≃ Cone(H on Y) ≃ Kh(T_1)*S.

On the right, the rational summand acts by integer twisting, preserving the length and local system of a special at infinity, and every special-special product is the fixed calculation S*S. Hence every indecomposable on the right is a grading shift of S. In a Krull–Schmidt category, a non-short indecomposable of Y would still occur in Y⊕h^{-1}q^{-2}Y; direct sums cannot cancel indecomposable types. Therefore Y itself is a sum of short specials.

This argument supplies the missing explanation of the report's short invocation of Krull–Schmidt. For graded multiplicities, multiplication by the finite shift polynomial of C is injective: shift orbits of nonzero finite graded indecomposables are free, and their multiplicities form finite Laurent polynomials. This permits the stated division. Having established short-special closure, Theorem A and the correctly normalized rational contribution give the explicit special-multiset formula and the count law

    n_12 = n_1+n_2+2 n_1 n_2.

The two additional trefoil-special tensor computations in the report are checks, not necessary universal inputs. Conversely, Theorem A alone does not classify the summands of a tensor product as short curves: that conclusion does use the universal S*S calculation and the H-cone argument.

I inspected the preserved S*S log: it records an initial 208-generator complex and four short-special components after cancellation with the quoted gradings. I did not independently construct and check a chain homotopy equivalence for that finite calculation. Its present status is therefore **conditionally verified proof, with one reproducible computer-assisted input not independently recertified in this pass**. This does not weaken the intrinsic Minkowski/EXT results above.

## 5. What this contributes to the proposed reduction

The invariant N_b is a well-defined positive-rank lift of the selected skein coefficient, and its monoidality is stronger information than multiplicativity of the coefficient's Euler characteristic. J-TILT, if proved for actual unknot-closure tangles, supplies noncancellation by a geometric restriction on this lifted support. The sum theorem shows that a proof need only address objects indecomposable under the specified equivariant sum.

It does not provide the missing restriction. The augmentation functor, Minkowski law, and extremal-parity argument hold for formal complexes just as they do for genuine tangles. Formal additions with opposite homological parity remain possible. Thus the next mathematical input must constrain realizability of the whole bullet support, rather than extract another consequence of its monoidal algebra.

I make no novelty claim for the augmentation invariant. Identifying it with an existing through-degree or projector construction may be useful, but is not needed for this referee verdict.

## 6. Second check: the total count law is universal

A subsequent targeted check, requested by the parent referee, removes the short-special assumption from the **total count law**, though not from the detailed graded special-multiset formula of §4.

Let m(T) be the number of special components in Kh(T), counted with multiplicity and without weighting by length, for a quotient tangle with unknot infinity closure. Then

    dim_F2 N_b(BN(T)) = 1 + 2 m(T).

Here is a proof that addresses the potential length, local-system, and minimality objections.

1. In Kotelskiy–Watson–Zibrowius, *On mutation invariance in Khovanov homology*, arXiv:2602.23442v1, Definition 3.12 displays C(s_{2n}(0)). It has four circle-labelled end generators, independent of n, and 4n bullet-labelled interior generators. The rotation rho in Lemma 3.9 and Proposition 3.10 swaps the two idempotents. Thus C(s_{2n}(infinity)) has precisely four bullet generators for every positive n. This is an exact count from the displayed complexes, not an extrapolation from the short-special data.
2. Theorem 3.19 and Remark 3.20 of that paper state that the components of an actual Kh(T) have the specified rank-one local systems. Thus no additional local-system rank is hidden in the preceding count. Repeated components are counted with their multiplicities.
3. The rational component r_1(k), for integer k, has two bullet generators. One may obtain this without a grading formula: an integer rational tangle is a horizontal product of one-crossing tangles, whose augmented complexes each have one generator. Theorem A gives one generator for N_b(BN(Q_k)); its H-cone gives two. Corollary 3.16 identifies this H-cone with r_1(k).
4. Applying the augmentation to the H-cone makes its H map zero. Consequently its total rank is twice dim N_b(BN(T)). Equivalently, a reduced BN complex has no identity differential entry, and H also has no identity part, so its H-cone is reduced. The curve representatives in Definition 3.12 are likewise reduced. Homotopy invariance of the augmentation makes the count independent of these representatives.
5. The unknot-closure structure theorem supplies exactly one r_1(k) and m specials at infinity. Counting bullets gives 2 dim N_b = 2 + 4m.

Combining this identity with Theorem A yields, with no short-special hypothesis,

    1 + 2m(T_1+T_2) = (1+2m(T_1))(1+2m(T_2)),
    m(T_1+T_2) = m(T_1)+m(T_2)+2m(T_1)m(T_2).

In particular, if 1+2m(T) is prime, T cannot be a compatible sum of two nonrational unknot-closure tangles: each nonrational factor has at least one special and hence rank at least three. This is a statement about the specified equivariant-sum operation, not a classification of the underlying knot's prime factors. It is stronger than the conditional count assertion in §4 and supersedes that assertion's short-special qualification.

The full multiset of **gradings** and **lengths** of the special components still requires more information. Universal total count does not make the finite S*S calculation redundant for the stronger short-component closure statement.

Primary source: [arXiv:2602.23442v1](https://arxiv.org/abs/2602.23442v1), locally checked in `/Users/calebbarnett/jones-lanes/theory-restart/lit/kwz-linear/src/mut2026/mut.txt`, pp. 16–19 and corresponding TeX.
