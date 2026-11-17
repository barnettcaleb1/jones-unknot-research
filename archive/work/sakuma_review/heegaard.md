# Scope of the genus-three surface conditions

Theory-only response to Claude 20261103-092928, question (iii). No knot census or numerical computation was run. The polynomial checks below are hand derivations.

## Conclusion

The listed conditions — a knot on a standard genus-three Heegaard surface, invariant under its hyperelliptic involution with two fixed points, surface framing zero, and a_2=0 — do not force the knot to be trivial. They already include nontrivial tunnel-number-one knots. A concrete example is the two-bridge knot b(31,13), up to mirror b(31,18), with Conway polynomial

    nabla(z)=1-2z^4.

The surface placement argument is given below rather than assuming an unverified low-genus placement of a Whitehead double. This is a scoped barrier: it does NOT assert that this placement realizes the particular width-six cap presentation, distinguished band, or Goeritz orbit in the current research setup. In particular it is not a Jones counterexample.

## 1. A nontrivial a_2=0 control

Take the rational knot with even continued fraction

    [2,-4,2,2] = 31/18.

Its mirror can be represented with Schubert fraction 31/13. A standard linear plumbing of its four twisted annuli has a Seifert matrix with diagonal (1,2,1,-1), subdiagonal 1, and other entries zero, up to mirror/convention. In det(t^(1/2)V-t^(-1/2)V^T), the tridiagonal continuants satisfy

    D_0=1, D_1=z, D_i=d_i z D_(i-1)+D_(i-2).

Thus D_2=1+2z², D_3=2z+2z³, and D_4=1-2z⁴. This gives a_2=0, while det K=|nabla(2i)|=31 proves K is nontrivial.

An independent hand check avoids reliance on the even-continued-fraction sign convention. For b(31,13), use epsilon_i=(-1)^floor(13i/31) and the standard alternating prefix-sum expression for its Alexander polynomial. The 31 prefix contributions aggregate to

    -2 t^-1 + 8 - 11t + 8t² - 2t³.

After dividing by t, the symmetric polynomial is

    Delta(t)=-2(t²+t^-2)+8(t+t^-1)-11
            =1-2(t+t^-1-2)².

Consequently Delta''(1)=0 as required. The knot is two-bridge, hence admits the standard single unknotting tunnel.

## 2. Zero-framed surface placement, with the symmetry checked

**Elementary placement lemma.** Every tunnel-number-one knot K admits a nonseparating representative on a standard genus-two Heegaard surface whose surface framing is the Seifert framing. That representative can be chosen invariant under the standard hyperelliptic involution, with the involution reversing the curve and fixing exactly two points. An equivariant stabilization away from the curve supplies the same properties on a genus-three Heegaard surface.

Proof:

1. Let tau be an unknotting tunnel and H=N(K union tau). Then H and its exterior are genus-two handlebodies. Choose N(K) inside H, with the tunnel attached at two small disks on its boundary.
2. A Seifert longitude of K can be chosen on boundary N(K) avoiding those attaching disks, so it lies on boundary H. It is isotopic to K in S³. A narrow annulus around it lies on boundary N(K), and its surface parallel therefore has linking number zero with it. This is the desired surface framing.
3. The curve is nonseparating on boundary H: its class maps to the nonzero primitive class of the cycle K in H_1(H). By uniqueness of genus-two splittings of S³, carry this splitting to the standard one by an ambient isotopy.
4. On a genus-two surface every nonseparating curve is invariant up to isotopy under the hyperelliptic involution, with orientation reversed. One may choose an invariant representative, for example using an invariant hyperbolic metric and the unique geodesic in the curve class. The involution acts by -I on surface homology, so its restriction cannot preserve the orientation of this nonseparating curve. An orientation-reversing involution of a circle has exactly two fixed points. Isotoping the curve within the surface preserves its surface framing and ambient knot type.
5. The standard hyperelliptic involution extends over both standard genus-two handlebodies, so it is a strong inversion of this embedded knot. In the quotient, perturb the bridge presentation of its fixed unknot at a branch point away from the two endpoints of the quotient arc. The lifted operation is an equivariant Heegaard stabilization away from K. It raises genus two to genus three and leaves the curve, its framing, and its two fixed points untouched.

The core-to-Heegaard construction is the standard tunnel-number interpretation; see [Morimoto, Fact 1.1 and Definition 1.4](https://tunnel-knot.sakura.ne.jp/T-G-H.pdf). The genus-two curve assertion is stated explicitly in [Li–Moriah–Pinsky, §1.3](https://arxiv.org/abs/1701.01421), published as *Tunnel number one knots satisfy the Berge conjecture*, Geometry & Topology 29 (2025), 3271–3343. The relation between bridge perturbation and its lifted Heegaard stabilization is part of the branched-cover setup in [Hirose–Iguchi–Kin–Koda, §§1–2](https://arxiv.org/pdf/2004.03098).

Applying the lemma to b(31,13) supplies the promised nontrivial example satisfying all the listed surface/framing/a_2 conditions. The argument does not assert that every genus-three curve is hyperelliptically invariant; the genus-two step and equivariant stabilization are essential.

## 3. The group needs to retain the involution and markings

Let G_3 be the Goeritz group of the standard genus-three splitting and H(Sigma_3) the hyperelliptic mapping class subgroup for the fixed involution iota. The relevant group is

    HG_iota = G_3 intersect H(Sigma_3),

and, when the distinguished endpoints must remain fixed, the appropriate endpoint stabilizer inside that group. The bridge Goeritz group is HG_iota/<iota>. These identifications are precisely Theorems 0.1 and 0.2 of [Hirose–Iguchi–Kin–Koda](https://arxiv.org/pdf/2004.03098).

[Freedman–Scharlemann](https://arxiv.org/pdf/1804.05909) prove Powell generation for the full genus-three Goeritz group. This does not by itself give generators for its intersection with the hyperelliptic subgroup, a normal form for marked arcs, or a criterion for an arc to be in a specified orbit. In genus three the involution is not central in the full surface mapping class group, so forgetting this subgroup is substantive.

There is a second scope issue: “Lemma Q says a=0 only on the orbit of the standard arc” needs a relative-position theorem. Unknotness of the lifted knot (even with its inversion identified) does not automatically identify its particular Heegaard-surface placement with the standard one by a splitting-preserving isotopy. Otal's bridge uniqueness for the fixed unknot addresses the axis and forgets the extra marked arc. I have not proved or disproved this stronger orbit claim; it should be an explicit additional gate rather than an assumed equivalent formulation.

## 4. What the frame could still contribute

This coordinate system retains the actual unknot axis, which is valuable, but zero framing and a_2 alone are too weak even at low genus. A useful new mechanism must convert full Jones equality into a geometric statement about disks, primitive curves, or a permitted relative destabilization; a presentation of the motion group does not supply that conversion.

For comparison, in genus two a curve primitive in both handlebodies has a lens-space filling at its surface slope. If that slope is zero, the filling is S¹×S² and Property R forces the knot to be the unknot. The tunnel placement above is primitive on one side; the missing condition on the other side is actual geometry. At genus three, primitivity on both sides only lowers the surgery splitting to genus two, so the same finish does not transfer without an additional reduction. This is a useful way to state the obstacle, not a proposed proof of a new Jones implication.

Recommendation: retain the marked Heegaard picture as a dictionary and keep the exact relative-position constraints visible. Do not promote its framing/a_2 shadow into a new route; the explicit two-bridge control already defeats that inference.
