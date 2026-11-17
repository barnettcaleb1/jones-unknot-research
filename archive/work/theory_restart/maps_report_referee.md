# Referee report: replacement maps and the J-TILT gap

Date: 15 November 2026. Referee: Codex, independent of the MAPS author.
Report examined: `/Users/calebbarnett/jones-lanes/theory-restart/mech/maps/REPORT.md`.
Scope: coefficients `F_2`, the explicitly displayed 12-generator special `S = s4(infinity)`, and existential homogeneous map pairs whose composites are prescribed central actions. No new tangle search was performed.

## Verdict

**The explicit algebra and the restricted blindness theorem are correct. They do not supply a proof of J-TILT.** They show that the known central-composite interleaving conditions, considered as existence conditions, are satisfied by the Euler-zero formal countermodel. The report overstates this as a conclusion about *all* replacement/cobordism constraints and as invariance under arbitrary deletion of special summands. Those stronger statements do not follow from its proof.

The claimed noncentral morphism window is also correct for this special. It permits the zero-offset adjacent-level pair in the countermodel; it neither forces a nonzero connecting morphism nor forces negative offset. It is therefore not a mechanism for J-TILT by itself.

There is an actual-data refinement worth retaining: the saved `b35_26-1` invariant contains two identical compact components in the same quantum grading and adjacent homological gradings. Thus forbidding this pair locally is incompatible with the saved actual-tangle computation. What might be constrained is the location of *all* generators at the global extremes.

## 1. Independent finite algebra check

I reimplemented the path algebra and the morphism differential without importing the report's `typeD.py`. The independent certificate is

`work/theory_restart/referee_checks/maps_exact.py`.

The algebra has idempotents `b,c`, loops `D_b,D_c`, alternating paths `S`, and relations `DS=SD=0`. Quantum degrees are `deg D=-2`, `deg S=-1`; algebra elements have homological degree zero. On the twelve generators of the report, the displayed differential squares to zero. The three proposed homotopies have bidegree `(-1,-2)` and satisfy exactly

```
d K_b + K_b d = D_b id,
d K_c + K_c d = D_c id,
d K_s + K_s d = S^2 id.
```

This checks the *written* homotopies, rather than merely solving for the existence of some homotopy. The verification survives every overall bigrading shift.

The augmentation ideal of the centre consists of sums of positive powers of these three central puncture classes. If `dK+Kd=z id`, then `d(K z^(m-1))+(K z^(m-1))d=z^m id`. Consequently every such augmentation element acts null-homotopically on `S`. In particular `H=D_b+D_c+S^2` does.

No assertion is made here for integral signs, other fields, nontrivial local systems, or longer specials. None is needed for the formal countermodel using this one special.

## 2. The exact theorem that follows

Let `N,N'` be finite sums of bigraded shifts of `S`. Suppose there are homogeneous maps

```
F0 : X0 -> Y0,       G0 : Y0 -> X0,
G0 F0 ~ z id_X0,     F0 G0 ~ z id_Y0,
```

where `z` is a homogeneous central augmentation element. Then on
`X=X0 direct-sum N` and `Y=Y0 direct-sum N'`, the block maps `F=F0 direct-sum 0`, `G=G0 direct-sum 0` have the same bidegrees and satisfy the same composite equations. The proof is the block-diagonal calculation plus Section 1.

This is an exact **zero-extension theorem for existential central-composite pairs**. It gives the useful obstruction to the proposed proof route: these equations cannot distinguish `a(0)` from `B=a(0) direct-sum S direct-sum hS` once one allows the positive central powers needed for the interleavings. The two special summands have opposite Euler characteristics; pairing with the unknot filling is acyclic on them. Hence the formal object retains the unknot closure and the complete decategorified closure data while carrying additional generators and failing the claimed extreme noncancellation.

The following stronger assertions should be removed or qualified:

1. **Not all maps are zero on the specials.** The conclusion constructs a permissible pair that is zero there. It does not identify a specified geometric crossing-change map, saddle map, or homotopy with that choice.
2. **Compatibility is extra information.** Simultaneous choices over several replacements, relations among their maps, and higher coherence among the null-homotopies were not considered. The proof cannot rule out a theorem using such information.
3. **Deletion is not proved by zero-extension.** Restricting an arbitrary pair on `X0 direct-sum N` and `Y0 direct-sum N'` can leave composite terms factoring through the deleted summands. The displayed argument proves preservation under adding summands, not the converse in an arbitrary category.
4. **No integral no-go theorem has been established.** The report explicitly does not check integral homotopies. The sentence in Section 5(ii) that integer information “can never exclude B” goes beyond the verified `F_2` argument.
5. **The model is formal.** Nothing constructs a tangle realizing the whole object `B`; the exact point of a geography theorem is to exclude such a global realization.

These restrictions leave intact the useful negative conclusion: the individual field-valued central-interleaving existence conditions cited in the report do not prove J-TILT or its extreme-parity consequence.

## 3. Primary-source check of the map invariant

I inspected the primary TeX of Lewark--Marino--Zibrowius, *Khovanov homology and refined bounds for Gordian distances*, arXiv:2409.05743v2, especially:

- `sections/3-lambda.tex`, `lem:nullhomotopic_basepoint_action_from_connectivity` (Lemma 3.13 in the report's numbering): the puncture action associated to a tangle's connectivity is null-homotopic;
- `lem:maps-tangles-to-links` (Lemma 3.17): a homogeneous pair of tangle maps with composites a puncture-class power gives maps on compatible knot closures, preserving quantum degrees and changing the composite to the corresponding `G` power;
- `sections/5-Lambda_set.tex`, `prop:torsion_and_biglambda` (Proposition 5.20): over a field,

```
Lambda(K;F) = { (a,b) : a+b >= u(K;F),
                        a >= s_F(K)/2,
                        b >= -s_F(K)/2 }.
```

The source proof explicitly reduces the latter statement to the free summand and torsion-order constraints. Thus the report's “unit bars plus pawn window” interpretation of membership `(1,0)` or `(0,1)` is correct. It is a statement about this invariant's information, not all the information present in an actual geometric cobordism.

The extension of Lemma 3.17 to a formal type-D object with the requisite null-homotopic connectivity action is justified by its proof: postcomposition/precomposition, centrality, and the displayed null-homotopies are the inputs. It does not require the formal object itself to have been realized by a tangle.

Primary source: [LMZ, arXiv:2409.05743v2](https://arxiv.org/abs/2409.05743v2). The current abstract/version metadata were checked online; the full statements above were read from the locally archived primary TeX. Online HTML was unavailable, so no HTML-only assertion is being inferred.

## 4. The complete noncentral window

The independent computation gives `dim H End(S)=16`, with the following `(h,q)` degrees and multiplicities:

```
(-5,-10), (-4,-8), (-3,-6), 2(-2,-4), (-1,-2), (0,0), (1,2),
(0,-2), (1,0), (2,2), 2(3,4), (4,6), (5,8), (6,10).
```

This is a complete calculation, not a truncated empirical table. Generator homological gradings range from 0 to 6, and their quantum gradings from 0 to 10. No morphism can have `h` outside `[-6,6]` or `q>10`. For `q<-10`, all coefficients are positive-length paths. In each quantum parity the differential matrices then stabilize under `q -> q-2`; the two stable tails have zero homology. The finite matrix calculation therefore exhausts all degrees.

For shifts with quantum/diagonal difference `(Delta c,Delta d)`, a degree-zero map exists precisely in

```
Delta d=0: Delta c in {-2,0,2,4,6,8,10},
Delta d=1: Delta c in {-10,-8,-6,-4,-2,0,2}.
```

Degree `(1,0)` maps have the same two rows shifted down by one in `Delta d`. These agree with the report.

Two limitations are decisive:

- `(0,1)` is allowed. The window includes the equal-quantum adjacent-level pair that gives the formal countermodel.
- Even a proven incidence graph of nonzero maps would give at most `Delta c <= 2` for a step up. J-TILT requires a strictly negative extreme shift; this is a new condition, not contained in the computed window.

The observation that `S direct-sum hS` is the associated graded/split form of an acyclic cone on `id_S` is correct. The split form is not itself zero, and no argument shows that actual tangle invariants must carry this particular nonsplit extension. That is exactly the missing geometric input.

## 5. The archived actual pair

I read the single saved file

`/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/tilt/examples/strong_inversions/2-bridge_knots/b35_26-1/cxBNr-c2-qs`.

Its components 2 and 9 have the same 12-generator cyclic word, first-generator quantum grading 10, and homological gradings 0 and -1 (diagonal gradings 5 and 6). The other compact components occupy first-generator quantum degrees `12,14,16` on diagonal 5 and `4,6,8` on diagonal 6. Therefore the claimed local cancelling pair is indeed present in that saved invariant, surrounded by further generators.

This is a check of the archived exact output, not a fresh reconstruction or independent identification of the underlying strong inversion. Its legitimate consequence is already enough for the proposed argument: the data cited in support of tilt themselves disallow a rule forbidding every equal-quantum adjacent-level special pair. A realizability restriction must be global, or retain geometric structure lost when taking the direct-sum decomposition.

## 6. Auxiliary assertions that should not be banked wholesale

### Rational-slot maps and triangles

The explicit even-twist maps have the expected central composite and are consistent with the primary source. The assertions for all even twists should be stated with the displayed general homotopy (including endpoint ranges), rather than using tests at two and four twists as their proof. A nonexistence check at three twists is not, by itself, a proof of nonexistence for every odd twist.

Applying the filling functor to an actual exact triangle is additive over summands and is insensitive to regrading an isolated summand. This observation is enough for the restricted no-go result. The report's more expansive conclusion “every long exact sequence is short exact on each component” needs the correct cyclic rotation and the grading shifts of each triangle. For the displayed even-`k` integer rank triples, one of the three dimensions is indeed the sum of the other two; which term is largest changes when the slope crosses the rational component. It should not be written as one uniformly oriented short exact sequence, nor extended to parallel/equal-slope pairings without the usual local-system/parallel-curve qualification.

### Theorem C and the pawn formula

The rational block is odd-dimensional and occupies one diagonal; special blocks are even-dimensional, and length-one bars pair generators on a single diagonal. Hence, assuming the stated block decomposition and degree conventions, the pawn diagonal is the rational block's diagonal. This part of the argument is sound.

The report labels a uniform formula for all even `nu` as PROVED while acknowledging that its twist induction was not written. The full range formula should remain **checked in the reported finite range / pending a written induction**. It is not needed for the central-blindness result or the independent End calculation.

The sentence in Section 4.2 saying that Lemma Q needs only a nonzero Euler characteristic at an extreme quantum degree is missing a condition: the surviving degree must differ from the unknot degree 0, or two distinct degrees must survive. A nonzero coefficient at degree 0 alone is compatible with the Jones unit.

### Crossing changes inside the tangle

The primary-source local map pair and the planar extension establish central-composite maps. The report's finer identification as `H`, `S^2`, or `D_b` in each orientation case requires the endpoint-dot bookkeeping to be fixed symbolically; its three examples are checks, not a proof of the general sign/marking statement. The no-go argument needs only a central augmentation composite, so it does not depend on promoting this finer dictionary prematurely.

## 7. What this contributes to the reduction

Retain two rigorous ingredients:

1. the complete `F_2` central-annihilation and zero-extension calculation for this special;
2. the complete noncentral Hom/Ext window, with the admission that it allows the offending zero shift.

Together they identify a genuine missing input: a restriction on the **global extreme support of actual quotient-tangle invariants**, not just their permitted summands or isolated central replacement maps. They neither refute J-TILT nor explain why it should hold. They also leave open the use of specified cobordism maps, compatible map systems, or a filtration from the actual tangle cube; those are not covered by the no-go theorem.
