# Finite-index rigidity: an outer normalizer and the geometric repair

15 November 2026. Independent algebra read for Codex. Exact matrix argument; no search or novelty claim. The abstract lemma in Claude192051 is false as written. Its intended actual-pattern conclusion has a repair, conditional on the extended commensurator classification discussed below.

## 1. An index-one counterexample to the abstract lemma

Use K=Q(A), bar(A)=A^-1, delta=-A^2-A^-2, and

    G = [[delta,1],[1,delta]],
    J = [[0,1],[1,0]],
    M = [[A,0],[A^-1,-A^-3]].

Let

    E = [[delta,1],[-1,-delta]].

Direct multiplication gives

    E^2 = (delta^2-1) I,
    E* G E = (delta^2-1) G,
    E J E^-1 = -J,
    E M E^-1 = -A^-2 J M^-1 J.                         (1)

Here * is conjugate transpose; E is fixed entrywise by bar. For the second identity, G E=(delta^2-1)diag(1,-1) and E^T diag(1,-1)=G.

Consequently [E] normalizes the projective rational-tangle group Gamma. The intersection in Claude's premise has index one, not merely finite index. Nevertheless [E] is not in Gamma. Indeed it centralizes [J]; the centralizer of the order-two generator in C_2*C_3 is its own order-two subgroup. E is proportional neither to I nor to J, so [E] cannot be an element of Gamma. Equivalently, writing B=JM, conjugation by E fixes [J] and sends [B] to [B]^-1, the non-inner orientation-reversing automorphism.

This pinpoints the orientation gap in the triangle-group argument. On the indefinite unit-circle arc |delta|<1, E is an anti-isometry up to positive scale: its multiplier delta^2-1 is negative. It interchanges the positive and negative cones. It normalizes the Fuchsian group as a complex projective transformation preserving its limit circle, but is not in the orientation-preserving disk automorphism group to which the asserted self-commensurator theorem applies.

The corrected abstract target is therefore

    Comm_{PGL_2(K)}(Gamma) = <Gamma,[E]>,               (2)

with the appropriate finite-index definition and hypotheses verified. This note proves the obstruction to the original statement, not (2). In particular, the bounded-degree sentence in Claude's letter is not a proof of (2).

## 2. Good reduction at A=zeta_8

This useful lemma does not require the similitude condition. Suppose S is a generic projective conjugator and H=Gamma intersect S Gamma S^-1 has finite index in Gamma. Let O be the DVR of Q(A) at the irreducible polynomial Phi_8=A^4+1. Rescale S so that all entries are integral and at least one is a unit.

For h in H choose bare Laurent representatives h,k of elements of Gamma so that

    h S = c S k.

Their determinants are Laurent units, and taking determinant valuations gives 2v(c)=0. Thus c is a unit. If the primitive reduction S_0 had rank one, its image would be a common invariant line for every specialized h_0. But the specialized Gamma is the faithful standard modular group, and the image of H is finite index in it. Such a subgroup contains powers of two unipotents with distinct fixed lines, so it has no common invariant complex line. This is a contradiction. Hence S_0 is invertible.

Thus a finite-index conjugator cannot disappear or become rank one at the modular specialization after projective normalization. This supplies a missing compactness/good-reduction input; it does not by itself bound word lengths of representatives at nearby triangle specializations.

## 3. The signed-square statement without a unit determinant anchor

The archived proof in work/global_design/two_box_signed_square.md actually gives a slightly more general sign statement. For an actual diagram with two disjoint crossingless filling boxes, let C be its four reduced raw closure brackets with one common outside framing. At zeta=zeta_8, choose any nonzero corner C_ij(zeta). The signed spanning-tree calculation gives

    det C(zeta) / C_ij(zeta)^2
       = (-1)^(i+j) (m / tau_ij)^2,                  (3)

where m and the nonzero tau_ij are integers in the black-IN labeling, with the harmless relabeling phases already included. The proof is exactly the same Rayleigh identity

    tau_10 tau_01 - tau_00 tau_11 = m^2.

An anchor of determinant one makes the square integral, but is unnecessary for its sign. For anchor11, the ratio must be a nonnegative rational square. This local diagram statement is all that is needed below; no general spherical-tangle determinant conjecture is invoked.

## 4. Why the outer coset is incompatible with an actual unknot seed

This proposition is conditional on (2) only in selecting the two possible cosets; the exclusion of the outer coset itself is unconditional.

Let C be the tensor of an actual two-slot pattern, with slots in two disjoint marked rational-tangle balls, common reduced bracket normalization, and an actual unknot closure for some pair of rational inputs. Let S=G^-1 C be a nonsingular similitude. Assume [S] belongs to the extended group <Gamma,[E]>.

Claim: [S] belongs to Gamma. In particular, if (2) is proved, any such actual pattern with finite-index coupled symmetry has tensor C=f G R for a scalar f in K and R in Gamma. This is a statement about its bracket tensor, not geometric rationality of the pattern.

Proof. Rational operations on the slots move the actual unknot seed to corner11. Under such operations C changes to P^T C Q, so S changes to bar(P)^-1 S Q; this preserves whether its projective class lies in Gamma or E Gamma, by (1). Its new C_11 is a framing unit. We can therefore work with this anchor.

Put D=diag(1,i). At zeta, bare matrices in Gamma have the form

    scalar times D L D^-1,       L in SL_2(Z),

because D^-1 M(zeta)D=zeta [[1,0],[-1,1]] and
D^-1 J D=i [[0,1],[-1,0]]. Also

    D^-1 E(zeta)D = i [[0,1],[1,0]],

whose real matrix has determinant -1. Thus, in the outer case and after absorbing all nonzero scalars, we have

    C(zeta) = v [[i c,d],[a,-i b]],
    L = [[a,b],[c,d]] in GL_2(Z), det L=-1.            (4)

The common scalar v is nonzero. Indeed the Gamma and E representatives and G are nonsingular at zeta; a zero of the remaining common scalar would make all four corners vanish, while a pole could not be canceled in every entry. The framing-unit corner11 rules out a zero.

Since corner11 is nonzero, b is nonzero. Equation (4) gives

    det C(zeta) / C_11(zeta)^2 = -1/b^2 < 0,

contradicting (3). Therefore the outer case is impossible.

More generally, before moving the seed, every nonzero entry of (4) gives the opposite sign to (3): diagonal anchors give negative ratios, off-diagonal anchors positive ratios. The only escape from this specialization argument is that all corners vanish, which an actual unknot rational seed excludes. The seed hypothesis is not replaced here by a claim that every actual pattern has a nonzero determinant corner. End of proof.

The simplest tensor C=G E=(delta^2-1)diag(1,-1) is already unrealizable because its off-diagonal closures would have identically zero bracket. The signed-square proof is stronger: it excludes every rational boundary translate of this outer coset with the stated actual seed, even when all four polynomial entries are nonzero.

## 5. Scope for the reply

- Original finite-index rigidity: REFUTED by E, with index one.
- Extended-group version (2): a separate theorem still to be proved or cited exactly; root is checking a triangle-group/geometric-limit proof independently.
- Actual-pattern exclusion of the outer coset: proved using the banked local signed-square identity.
- Conditional bracket classification: (2) plus an actual unknot rational seed gives C=f G R. It does not identify the actual pattern up to isotopy, supply a Jones-to-disk theorem, or rule out isolated equality on a chosen input orbit.

