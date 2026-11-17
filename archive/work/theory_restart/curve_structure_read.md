# Lane 1: what the curve structure and bar constraints actually imply

15 November 2026. Bounded conceptual read; no new tangle computations, no searches for counterexamples. The empirical TILT/OVERHANG claims have not been independently recomputed. Main new item here is an explicit **formal Bar–Natan object** showing that the curve classification, the H-cone, and the proposed unit-bar constraints do not imply TILT. This is not a realizable tangle and not a counterexample to Lemma Q.

## 1. Verified structural statement

Let T be a two-strand tangle with T(infinity)=U, using the surgery parametrization in which 0 is the Seifert longitude of its double-cover knot exterior. Over F_2,

    Kh~(T) = r_1(k) disjoint-union gamma_1 ... gamma_m,
    k is even; each gamma_i = a bigrading shift of s_{2n_i}(infinity).

Here the notation is the current doubled indexing: the familiar four-dimensional building block is s_4, called s_2 in the 2021 strong-inversions paper. There are special components if and only if T is nonrational.

This is explicitly proved at the beginning of the proof of Theorem 1.2 in [Kotelskiy–Lidman–Moore–Watson–Zibrowius, Cosmetic operations and Khovanov multicurves, §4](https://arxiv.org/abs/2109.14049). The proof uses the rank-one pairing with the unknot arc: a special of any other slope contributes more than one intersection, whereas an invisible special must have slope infinity; a rational component contributes one intersection precisely when it is r_1(k) with integral k. Connectivity detection makes k even. Rational-tangle detection gives the final equivalence.

The same structural argument now works over any field using [KWZ, On mutation invariance in Khovanov homology, Theorems 3.17, 3.19 and 3.22](https://arxiv.org/abs/2602.23442). This is a combination of the cited results, rather than a separately named arbitrary-field theorem in the cosmetic paper. In the 2026 convention the rank-one local system is -1; over F_2 this is 1.

**Not supplied by these theorems:** n_i=2; divisibility 4|k; relative quantum or delta shifts of different specials; TILT; OVERHANG. Even over F_2 the 2021 paper states that longer specials occur. Over F_3 its Remark 3.10 gives the explicit strong inversion 7_4^2 with r_1(6), two old s_2 and five old s_1, i.e. two current s_4 and five current s_2. Thus the all-s_4 hypothesis is empirical, and is stronger than the known geography.

The unknot arc fixes the rational component's overall grading, but is disjoint from every special. It imposes no direct grading constraint on those invisible summands. [Thin links and Conway spheres, §6](https://arxiv.org/abs/2105.06308) shows that an additional thin filling at a different slope would align the relevant delta-gradings. The known thin filling at infinity cannot do that: the summands needing alignment are precisely the ones it misses.

## 2. Conventions and the exact H-cone

Write h for homological degree, q for quantum degree, and delta=q/2-h. The differential has degree (h,q)=(1,0); H has degree (0,-2). The 2026 paper uses G in place of H, with the appropriate sign in its quiver algebra. Definition 3.12 fixes actual graded component complexes. Its §2.2 gives

    K(B) := Cone(H.id_B) = [q^(-1) h^(-1) B --H--> q B].

Consequently [K(B)]=(q-q^(-1))[B] in the graded Grothendieck group. This is a categorical identity, not a realizability theorem.

The critical additional fact is [KWZ 2026, Lemma 7.7](https://arxiv.org/abs/2602.23442): H.id is null-homotopic on **every direct summand** of a complex which is itself an H-cone. The earlier characteristic-two version is [KWZ, Khovanov multicurves are linear, Lemma 5.2](https://arxiv.org/abs/2202.01460). Thus H acts null-homotopically on each actual Khovanov special component.

A proposed triangle

    r_1(k) -> shifted r_1(k+4) -> shifted s_4(infinity)

has not been established by this read. A relation of Euler classes does not establish it: one must specify the morphism, its absolute grading, and identify its cone. Even if such a triangle exists, the next assertion that actual quotient tangles cannot realize the corresponding split Euler class is an additional theorem. Equality in K_0 forgets extensions in both directions.

## 3. Formal countermodel to the proposed bar mechanism

Work over F_2. Let A=C(a(0)) be the ordinary Bar–Natan arc complex. Choose S to be the complex of an s_4(infinity) special occurring in an actual Khovanov tangle invariant, for example the trefoil quotient, and shift its quantum grading to agree with A's idempotent parity convention. This is an object of the same type-D category; it is not being asserted to be a standalone tangle invariant.

By the preceding lemma H.id_S is null-homotopic. Define

    B = A direct-sum S direct-sum h S.

Then the following statements are rigorous inside the category.

1. B has one noncompact arc and two compact components, the allowed counts for a two-arc tangle invariant.
2. Pairing B with the unknot-filling arc has exactly the same result as pairing A. The two compact specials are disjoint from that arc; compact-to-arc pairing introduces no endpoint wrapping contribution.
3. [B]=[A]. Therefore every Euler closure pairing is identical to that of the rational arc, not merely the pairing at one or two slopes.
4. Any rational-arc pairing with either extra compact summand has H-annihilated homology, by functoriality of the null-homotopy. For the slopes 1/(2n), the A contribution is the unknot tower. Thus every added torsion summand has length one, at every one of the even closures in the proposal.
5. The H-cone is explicitly

       K(B) = r_1(0)
              direct-sum q S
              direct-sum q^(-1) h^(-1) S
              direct-sum q h S
              direct-sum q^(-1) S.

   This uses Cone(null-homotopic f) = target direct-sum shifted source. It has exactly four s_4 specials, k=0, and Euler class [r_1(0)].
6. If S has central quantum offset c and delta level d, these four specials occupy

       (c+1,d+1/2), (c-1,d+1/2),
       (c+1,d-1/2), (c-1,d-1/2).

   There are two consecutive occupied levels with **identical** minimum and maximum offsets. They violate strict TILT. Opposite homological shifts cancel their Euler classes exactly.

This strengthens the bare formal example r_1(0) plus S plus hS: it supplies a compatible Bar–Natan lift, its exact cone, and the required unit-bar structure. The obstruction is not merely that arbitrary Khovanov groups can be written down.

**Scope limit.** This is not an actual quotient tangle, and it does not falsify empirical TILT for tangles. I have not proved that B admits the full positive higher A-infinity extension arising from a tangle cube. The extension theorem is for the entire invariant; a higher extension may mix summands, so an extension of the whole does not automatically restrict to a chosen ordinary type-D summand. Do not silently mark that extra condition as passed. Nor does the example supply the actual cobordism maps and all their compatibility relations with planar tangle composition.

The deduction is precise: classification, quantum parity, invisible special components, one unknot tower, the H-cone relation, and per-closure unit-bar matching **cannot by themselves force TILT or Lemma Q**. A successful matching proof must use a further tangle-realizability constraint.

## 4. A useful exact replacement for heuristic unit-bar matching

There is an elementary complete test for the algebraic matching constraint at a single closure. It is stronger and more precise than choosing plausible matches between dangling ends of specials.

**Unit-bar matching lemma.** Let V be a finite bigraded vector space, and designate one basis class in degree (h,q)=(0,s) as the pawn. Remove it. Fix a diagonal delta=q/2-h, and let n_h be the remaining dimension at (h,q=2(h+delta)). Set b_h=0 below support and recursively define

    b_h = n_h - b_(h-1).

Then V is the H=0 homology of a formal free F[H] complex consisting of that pawn and length-one H-bars if and only if, on every diagonal, b_h is nonnegative at every step and is zero above support. When it exists, the multiset of bar bidegrees is unique: b_h is the number of bars from (h,q) to (h+1,q+2).

**Proof.** A length-one bar preserves delta and contributes one class at each of two consecutive h values. Thus n_h=b_(h-1)+b_h. This forces the recurrence and proves necessity. Conversely, the nonnegative b_h specify the direct sum of two-term free complexes F[H] --H--> F[H] with exactly those grading shifts. The terminal zero condition prevents an unmatched final endpoint. QED.

Equivalently, all the alternating partial sums of the n_h are nonnegative, and the final alternating sum is zero. This is the complete information supplied by the **existence** of a unit-bar lift of a closure. It says nothing about which two curve components should supply a bar's ends. The model in §3 passes it by construction and still violates TILT.

For context, [Lewark–Marino–Zibrowius, Proposition 3.33(iv) and Theorem 1.2](https://arxiv.org/abs/2409.05743) prove, over any field, that the maximum H-torsion order equals lambda(K;F) and is bounded by proper rational unknotting number. The parity qualification on the 1/n family is essential: replacement by the infinity filling is proper exactly in the even-denominator case in these coordinates. The bound does not say that odd-denominator closures must have long bars.

## 5. Field comparison: an exact constraint, not positivity

For each fixed closure L, the integral reduced Khovanov complex is free as an abelian complex. Universal coefficients give a concrete comparison of bigraded dimensions:

    P_Kh(L;F_p)(h,q) - P_Kh(L;Q)(h,q) = (1+h) R_p(h,q),

where R_p has nonnegative integer coefficients. Each p-primary cyclic torsion summand in integral cohomological degree j and quantum degree q contributes one F_p class in degrees j and j-1 at that same q. This statement is about ordinary reduced Khovanov groups of the closure, not a componentwise matching of the multicurves.

At h=-1 the difference vanishes. Thus comparing fields gives restrictions on possible curve packages through **all their closure pairings**, but equality of Jones polynomials over fields supplies no new equation beyond their already common Euler class. No field-independent identification of individual specials follows, as the explicit 7_4^2 example demonstrates. The free Bar–Natan pawn may also shift with characteristic: the torsion Euler polynomial is field-independent only after conditioning on the same Rasmussen s-value.

## 6. Recommendation and remaining target

Retain the corrected curve geography as a rigorous way of locating the missing information. Do not treat either the H-cone or the existence of bar matches as the source of TILT without a theorem excluding §3.

The sharper target is a **realizability obstruction for an Euler-invisible compact summand with an opposite homological shift**. One possible place to seek it is the full positive higher extension/cube structure, or the compatible family of actual tangle cobordism maps, rather than the independently decomposed homology of each closure. This is a target, not an asserted mechanism. A first conceptual test of any proposed rule is whether it excludes the explicit B above while retaining actual compact components.

The endpoint-only implication in Claude's letter is correct conditionally: if an extreme actual-special offset has one sign and is outside the rational virtual support, that coefficient cannot cancel. Strict TILT plus OVERHANG is one sufficient way to obtain this. Neither is proved by the references, and the all-s_4 hypothesis must remain visible in that particular formula. No claim about a general Jones proof, novelty, or a genuine TILT counterexample is made here.

## Primary source locations checked

- KLMWZ, arXiv:2109.14049: local TeX `kwz-thin/src/cosmetic/tex/sections/ecsc.tex`, first part of proof of Theorem 1.2; later comparison of the ±1/n closures.
- KWZ, arXiv:2602.23442: §2.2 cone convention; Definition 3.12; Theorems 3.17, 3.19, 3.22; Lemma 7.7; extension theorem in §10.1.
- KWZ, arXiv:2202.01460: Lemma 5.2 and extension property.
- KWZ, arXiv:2104.13592: Theorem 3.1 is finite computation; Conjecture 3.7 and the following text permit longer specials; Remark 3.10 supplies the F_3 example.
- Lewark–Marino–Zibrowius, arXiv:2409.05743v2: Theorem 1.2, Proposition 3.33; Lewark–Zibrowius, arXiv:2208.13612v2, Theorem 3.16 for pawn-and-bars decomposition.

Local literature digests were used as navigation; the central curve/cone/null-homotopy statements were checked in the primary TeX/PDF text. No generated datasets were modified.
