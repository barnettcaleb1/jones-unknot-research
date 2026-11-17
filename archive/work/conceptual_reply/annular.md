# Annular-pattern critique: what one Hopf evaluation does and does not see

2026-11-03. Conceptual pass only; no enumeration or instrument computation.

## 1. The fixed e1 functional is not nondegenerate

Use unreduced framed brackets, so the empty diagram is 1 and a zero-framed unknot is delta=-A²-A⁻². In the Chebyshev basis of the solid-torus skein, put

    F0(e_k)=Delta_k,
    F1(e_k)=lambda_k Delta_k,
    lambda_k=-(A^(2k+2)+A^(-2k-2)).

Here F0 forgets the axis and F1 adds its meridian, coloured 1. These are linear functionals over Q(A). The entire Hopf bilinear form can be nondegenerate while its restriction against one fixed vector e1 is very far from injective. Already

    Z = lambda_2 Delta_2 e0 - delta e2

is a nonzero integral skein element with F1(Z)=0. Thus there is no purely linear-algebraic noncancellation theorem for this one measurement. This is a formal kernel element, not an asserted knot pattern or band-unknotting counterexample.

The correct question is whether the geometrically realizable marked-band locus intersects the relevant affine kernel only in split patterns. That is meaningful, but it retains the old realization/noncancellation gap.

## 2. A positive two-measurement lemma

**Lemma.** On the two-dimensional space spanned by e0 and e2, the pair (F0,F1) is injective.

Indeed its determinant is

    Delta_2 (lambda_2-delta) != 0.

In particular, suppose a winding-zero pattern P has annular degree at most two, its underlying knot in S3 is actually the unknot, and the zero-framed encircled link has the bracket of the two-component unlink. Then

    F0(P)=delta, F1(P)=delta²,
    [P]=delta e0.

This proves equality of skein classes, not that the pattern lies in a ball. If the wrapping number is two, the assertion that its e2 coefficient cannot vanish is precisely a low-wrapping detection statement. It still needs a topological mechanism.

Also, nonzero p2 by itself does not exclude F1(P)=delta²: p0 can compensate. The extra ordinary-closure value is indispensable for this elementary argument. If the other component is a nontrivial two-bridge knot, it does not have F0(P)=delta.

For a general underlying knot J and P=p0 e0+p2 e2, the unlink encircling condition instead gives

    (delta-lambda_2)Delta_2 p2 = delta(F0(P)-delta).

With zero framing F0(P)=delta V_J, this is

    (delta-lambda_2)Delta_2 p2 = delta²(V_J-1).

The denominator after cancelling delta contains, up to units, the familiar factors (A4-1)²(A8+A4+1). These correspond to standard Jones evaluations/derivative conditions; one should not expect integrality of this expression alone to force J=U. No new obstruction is claimed from it.

More generally, on degree at most 2r, sufficiently many independent coloured-meridian measurements can recover the annular class. Ordinary Jones of the axis-pattern link supplies only the single e1 measurement. Adding coloured observations without deriving them from the hypotheses silently changes the problem.

## 3. Component bridge number is not relative pattern complexity

The width-six incidence statement does give a useful, honest conclusion. N(X) is a six-plat with three upper and three lower bridges. Its short component uses one upper and one lower bridge and is therefore an unknot. The other component uses two upper and two lower bridges and has bridge number at most two. This holds after forgetting the other component.

It does not follow that the second component is a rational/continued-fraction object inside the complement of the first. An isotopy giving its two-bridge description may cross the axis. The actual datum is a joint (1,2)-bridge presentation of a two-component link, together with the marked band whose other resolution is U. That contains considerably more information than the underlying two-bridge knot type.

Even fixing the underlying knot to U does not control the annular embedding. Nested untwisted Whitehead patterns give winding-zero patterns whose ordinary closures remain unknotted but whose wrapping numbers grow as 2^r. This uses the geometric index 2 of a Whitehead inclusion and Schubert's multiplicativity for nested solid tori. Such examples refute any proposed classification based only on the ordinary knot's continued fraction. They are NOT asserted to retain width six or the required unknotting band; those extra hypotheses must be kept separately.

For a primary account of geometric index and its multiplicativity, see Ancel–Garity–Repovš–Wright, *New Techniques for Computing Geometric Index*, §2, https://arxiv.org/abs/1711.04267 . The broader message is that the relative axis placement, not the ordinary knot type, is where the missing geometry sits.

No claim was established about whether the known EKT Jones-unlink examples admit the required joint three-bridge presentation. In particular, they must not be used as width-six counterexamples without an actual joint presentation and the band condition.

## 4. Whitehead is outside the claimed band-to-U locus

The Whitehead link is an excellent essential winding-zero pattern control, but it is NOT one band move from U.

Here is a short obstruction, independent of Jones. The Whitehead link is the two-bridge link b(8,3), so its double branched cover is L(8,3), up to orientation conventions. A single band move to U would, by the Montesinos trick, give a distance-one filling of a knot exterior in S3. Therefore L(8,3) would be integral surgery on an S3 knot. Since its first homology has order 8, the coefficient would be ±8. The linking form of such an integral surgery has a generator of square ±1/8. But the linking form of L(8,3) has generator square ±3/8; changing the generator multiplies by a unit square modulo 8, and every such square is 1. The forms cannot agree, even allowing orientation reversal. Contradiction.

The primary identification W=b(8,3) is stated in Cavicchioli–Spaggiari–Telloni, *Dehn surgeries on some classical links*, Proc. Edinburgh Math. Soc. 54 (2011), §3: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/E4946D490730951BE868F6F84EDB30D2/S0013091509000777a.pdf/dehn-surgeries-on-some-classical-links.pdf . One can also read 8/3 directly from its rational diagram [2,1,2].

Thus a proposed Lemma-Q proof need not explain why Whitehead survives the required band hypothesis: Whitehead fails that hypothesis. It should still serve as an annular-normalization control, clearly labelled as outside the target locus.

## 5. Recommendation

Neither the fixed e1 pairing nor ordinary two-bridgeness currently makes option (ii) simpler. The full Hopf form is being replaced by one row, and a relative embedding is being replaced by an absolute knot type; both replacements lose essential data.

Keep the actual band and the unknot resolution in the definition of the object. The useful next theoretical statement would be a geometric restriction on that marked-band locus—one that forces a second independent observation or restricts the realizable annular skein classes. The two-measurement lemma then has a role. Without such a restriction, proving p2 nonvanishing is still the wrapping-two Key Lemma, and expanding the same scalar in a different basis is not a new route.

This does not argue that an annular approach is impossible. It identifies the exact reason a proposed classifiable-pattern or nondegenerate-pairing argument has not yet supplied additional leverage.

## 6. Root's additional finite-type consequence, checked by hand

The winding-zero realization condition supplies one useful restriction beyond formal integrality. An actual winding-zero knot P in the solid torus satisfies

    [P] at A=-1 = -2 e0.

Indeed the classical solid-torus skein algebra is C[z], and the trace function of a winding-zero loop in pi_1(ST)=Z is the constant -2. Hence in [P]=sum p_k e_k we have p_k(-1)=0 for k>0. For every k, lambda_k-delta vanishes to order at least two at A=-1; the k=0 term vanishes identically. Therefore

    F1(P)-delta F0(P)
      = sum_(k>0) p_k (lambda_k-delta) Delta_k
      = O((A+1)^3).

If the axis-pattern link has linking number zero and the Jones polynomial of the unlink, choose zero framings. Then F1(P)=delta² and F0(P)=delta V_J(A^-4), where J is the pattern with its axis forgotten. Since delta(-1)=-2 and t=A^-4 is a local parameter at A=-1, it follows that

    V_J(t)-1 = O((t-1)^3),
    V_J''(1)=0,
    a_2(J)=0.

The last equality uses the standard normalization V''(1)=-6a_2. This is a familiar finite-type constraint expressed through the annular expansion, not a new detection theorem. It holds at every annular degree and does not use the band-to-U condition. It rules out, for example, a trefoil as the other component of such a Jones-unlink link with unknotted axis.

For clarity about formal realizability, root supplied an instructive algebraic control. With t=A^-4,

    P_form = delta t² e2 - delta(t²+t⁴)e0

satisfies

    F0(P_form)=delta(t+t³-t⁴),
    F1(P_form)=delta².

Thus formal degree-two support and integrality alone permit the ordinary Jones polynomial of a trefoil together with the unlink Hopf value. But this is NOT an actual winding-zero pattern: at A=-1 it equals 6-2z² rather than -2. The classical realization condition already excludes it. It must not be presented as a geometric counterexample or as showing that all known realization constraints are insufficient.
