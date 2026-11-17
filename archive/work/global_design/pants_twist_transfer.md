# A marked pair-of-pants transfer from a link polynomial to knot polynomials

2026-11-03. Bounded theory pass under CX-C4. Written geometric and algebraic
derivation, with independent internal reads. No counterexample input has been
found and no novelty claim is made.

Update 19:12: the separate nontrivial-Gamma hypothesis below is now
automatic for a nonplanar Brunnian theta spine. The proof, including
det K(m,n)=1 and u(K(1,1))=1, is in `pants_nontriviality.md`.

## The construction

Let P be an oriented embedded pair of pants in S^3 with zero Seifert form.
Suppose its three boundary components are unknots. Write L = boundary(P),
with its boundary orientation. Choose two disjoint properly embedded arcs
a,b joining boundary components in a tree and cutting P into a disk.

Remove narrow rectangular neighborhoods of the two arcs. The remaining
embedded disk has boundary K(0,0), an actual unknot. The two removed strips
specify two disjoint local two-strand boxes on that boundary. The strands
have opposite orientations. Define K(m,n) by inserting m,n full twists in
these boxes. Choose local handedness so the normalized moving eigenvalue is
z = A^8 at both sites. All integer parameters preserve knot connectivity.

Let C_a,C_b be the crossing circles of these specified boxes, and put

    Gamma = K(0,0) union C_a union C_b.

Do not identify Gamma with L: these are two different three-component links.

## Exact polynomial identity

Use V(U)=1, delta = -A^2-A^-2, t=A^-4. Restoring neither strip gives U.
Restoring either strip gives an embedded annulus. Its core is isotopic to
the boundary component of P untouched by that cut, hence is an unknot.
The annulus framing is zero by restriction of P's Seifert form. Its boundary
is consequently the actual two-component unlink. Restoring both strips
gives L.

Thus the four normalized closures are exactly

    V00 = 1,     S1 = delta,     S2 = delta,     S12 = V_L.

At an antiparallel full-twist site the normalized operator is

    N^m = z^m I + (1-z^m)e/delta,    z=A^8.

Applying it at both disjoint boxes, with the common outside orientation,
gives the identity in Q(A)

    V_K(m,n) = 1 + (1-z^m)(1-z^n)(V_L/delta^2 - 1).       (1)

The output is a Laurent polynomial despite the displayed denominator.
The zero Seifert form also forces all pairwise linking numbers of L to
vanish, so changing its component orientations causes no normalization
ambiguity. This is a specialization of the archived four-closure formula
in work/research34/twist_formula.txt, now with all three smaller closures
supplied by actual surface topology.

In particular, for any mn != 0,

    V_K(m,n) = 1  iff  V_L = delta^2.                      (2)

If the link equality holds, it holds for the entire integer knot family.
The extra twists are not asserted to remain intrinsic cuts of P.

## An independent, finite nontriviality certificate

The following sufficient hypothesis can be checked on the marked diagram:

    Gamma is a nontrivial homologically trivial Brunnian link.          (3)

Under (3), every K(m,n) with mn != 0 is nontrivial. Indeed, surgery with
slopes +/-1/m and +/-1/n on C_a,C_b gives S^3 containing K(m,n). If that
knot were U, a further +1 surgery on it would give S^3. Pairwise linking
numbers are zero, so the last preferred longitude is the original one.
This would be a surgery on Gamma with all three slopes nonmeridional
and finite, resulting in S^3, contrary to Mangum--Stanford Theorem 2.

The published input is: a homologically trivial Brunnian link admitting
such an S^3 surgery is the unlink. See
[Mangum--Stanford, AGT 1 (2001), Theorem 2 and its following paragraph](https://msp.org/agt/2001/1-1/agt-v1-n1-p07-p.pdf).
No hyperbolicity or sufficiently-large-parameter qualification is needed.

For the pants construction the proper sublinks can also be certified
geometrically. The two crossing circles lie in disjoint local balls, so
their pair is an unlink. After forgetting one circle, the remaining
configuration is obtained by cutting a zero-framed unknotted annulus along
a spanning arc. Isotope that annulus and its arc to a flat annulus with a
radial arc; the cut boundary and its crossing circle give the standard
nugatory pair. Hence each K(0,0) union C_i is an unlink. Thus Gamma is
Brunnian, with all pairwise linking numbers zero. Nontriviality was a
separate requirement in the original pass. The subsequent proof in
`pants_nontriviality.md` shows that nonplanarity of a canonical Brunnian
theta spine supplies it: Gamma unlink implies boundary(P) unlink by
branched-cover surgery, and hence the theta is planar.

Consequently a P with V_L=delta^2 and certified nontrivial Gamma gives the
explicit counterexample K(1,1). Conversely, for a fixed such nontrivial
Gamma, V_L != delta^2 excludes every nonzero parameter pair at once.

## The spatial-graph input, and the unsolved part

A Brunnian theta graph has a canonical embedded pair-of-pants thickening
with zero Seifert form; its boundary components have the constituent knot
types, and hence are unknots. Huh's Theorem 8 / Corollary 9 imply that its
boundary has the Jones polynomial of U3 exactly when its normalized
Yamada value is the planar theta value. These are published inputs:
[Huh, Yamada Polynomial and associated link of theta-curves](https://arxiv.org/html/2206.11450#S4).

This supplies the marked bands missing from a mere assertion about an
unmarked Jones-unlink link. It does not supply a nontrivial theta graph
with the required polynomial. The bounded source check found none.
The subsequent topological argument certifies Gamma's nontriviality
automatically for a nonplanar Brunnian theta. Thus the remaining input is
one such theta with V_L=delta^2, equivalently the planar normalized Yamada
value. A planar pants surface has that value but gives actual unknots. The known
Ishii--Iwakiri equal-Yamada examples have a nonconstant factor multiplying
the planar value and do not supply the polynomial input. The archived EKT LLL(1)
bands have nonunlink single-cut polynomials and do not meet this marked
surface package.

**Judgment.** This is a complete conditional transfer, including a fixed
nontrivial knot output from the specified polynomial-flat nonplanar theta. It is not
an actual counterexample design ready for certification: no input with
these properties is currently known here. Keep it parked until a marked
source is supplied; CX-SAK5 remains the existing concrete certification.
