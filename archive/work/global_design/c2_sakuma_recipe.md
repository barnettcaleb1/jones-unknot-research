# C2: implementable zero-framed Sakuma-link recipe for the residual pilot

Date: 2026-11-03. Bounded design pass. Output is an exact geometric construction, not a computed PD code or a claim that a candidate has trivial Jones polynomial.

## 1. The specified inputs

Define the knot by the **additive** continued fraction

    [2,−4n,2,2n],       n≥1,
    p/q=(32n²−1)/(16n²+2n).

Do not substitute an unspecified Conway-sign convention. The two strong inversions are

    I₁(2,2; −2n,n),          I₁(−2n,4n; −1,−1).

At n=5 these are I₁(2,2;−10,5) and I₁(−10,20;−1,−1). The covering knot has determinant 799, Conway polynomial 1−50z⁴, and a₂=0. Its determinant need not equal 1: it is the **covering knot κ**, not the prospective Jones-unit knot obtained by twisting the downstairs unknot. The archived FROB5 calculation leaves exactly 5|n in this family; n=5,10,15 are consequently the requested inputs, not newly screened candidates.

The diagrams are Snape's Figure 1.10, Proposition 1.2.11. The explicit port wiring is in `work/next_theory/sakuma_template.md`, and the inspected figure is `work/next_theory/snape_figures/page-047.png`. Both diagrams have 6n+4 crossings before simplification, hence even writhe.

For implementation, use the following m=2 wiring, on both sides of the vertical rotation axis. An α box has top/bottom and left/right ports; a horizontal −c box has near/far and upper/lower ports:

1. α₁ top-side → (−c₁) near-upper.
2. α₁ bottom-side → (−c₁) near-lower.
3. (−c₁) far-upper → (−c₂) near-upper.
4. (−c₁) far-lower → α₂ top-side.
5. α₂ bottom-side → (−c₂) near-lower.
6. Join the far-upper ports of the left/right outer boxes by the exterior upper arc, and the far-lower ports by the exterior lower arc.

The connectors have no extra crossings. First inversion: central boxes 2,2; each side's inner/outer boxes are +2n,−n. Second inversion: central boxes −2n,4n; all four side boxes are +1. Crossing glyphs and their rotated-box convention are on the saved page-046 image.

## 2. A preferred longitude can be constructed explicitly

This bypasses the previously unresolved quotient-tangle marking. It uses the actual symmetric knot diagram and never treats its exterior quotient as a rational tangle.

Realize the diagram as a smooth curve κ⊂R³, with its displayed plane the xy-plane and the vertical axis the y-axis. Let

    τ(x,y,z)=(−x,y,−z).

Build the right-side crossings and connectors and take their τ-images for the left side. Realize each central twist box by the usual pair of opposite helical strands about the y-axis. Keep the two exterior closing arcs in the xy-plane. This makes τκ=κ, with precisely the two displayed fixed points. Require the xy-projection of κ to be a regular knot diagram; it can be arranged by arbitrarily small symmetric perturbations.

Orient κ and let T be its unit tangent. Define the unit normal field

    v(p) = [e_z − (e_z·T(p))T(p)] / |e_z − (e_z·T(p))T(p)|.

The denominator is nonzero because the xy-projection is regular. Since τ reverses the knot orientation and sends e_z to −e_z,

    v(τp)=−τ_*v(p).

Thus the thin annulus κ(s)+u v(s), |u|≤ε, is τ-invariant and τ exchanges its two boundary components. This is the required action for Sakuma's construction. The literal in-plane blackboard-width annulus has a different action at the fixed points and must not be substituted.

The field v is the blackboard normal rotated by a constant quarter-turn around T. Therefore its framing equals the diagram writhe x. Compute x from the oriented diagram; there is no need to guess a parameter-dependent writhe formula. The parity is already known: x is even because the crossing count 6n+4 is even.

Choose a small crossing-free interval I⊂κ away from the fixed points, with I and τI disjoint. Put k=−x/2. On I rotate v around T through k complete turns, using a smooth angle function θ that goes from 0 to 2πk and is constant near both endpoints. Extend to τI by the rule v'(τp)=−τ_*v'(p), and leave v unchanged elsewhere.

The two intervals contribute k turns each to the framing: τ reverses both the core orientation and the orientation of its normal plane, so the two sign reversals cancel. Consequently

    framing(v') = x+2k = 0.

For sufficiently small ε, the annulus A={κ(s)+u v'(s): |u|≤ε} is embedded, τ-invariant, and has preferred boundary curves λ₊,λ₋ with

    τ(λ₊)=λ₋,       lk(κ,λ₊)=lk(λ₊,λ₋)=0.

This provides an exact zero-framing rule for both pilot inversions and every n. It is not merely the condition lk(c,U)=0 downstairs, which would fail to distinguish other even framings.

## 3. Take an explicit quotient and then a generic projection

Use the two-fold branched quotient

    p(x,y,z)=(x²−z², y, 2xz).

Writing w=x+iz, this is (w,y)↦(w²,y). Its branch locus is the y-axis, and it extends over infinity to the standard quotient S³→S³/τ.

Define

    U = y-axis ∪ {infinity},
    c = p(λ₊) = p(λ₊∪λ₋),
    S_n^(j) = U ∪ c,          j=1,2 for the selected inversion.

This is the zero-framed Sakuma link. The image c is embedded: the only identifications under p are τ-pairs, and λ₊ is disjoint from τλ₊=λ₋. Moreover A/τ is an embedded disk with boundary c and exactly two branch intersections. Thus both c and U are unknots.

For the algebraic-zero crossing-circle assertion, the signs also need checking. Parameterize one half of κ between its two fixed points and choose a generic symmetric regular projection. Every interior zero of its x-coordinate gives one axis-fixed crossing of the projected knot; off-axis crossings occur in pairs. The even crossing count therefore gives an even number of interior x-zeros, so the oriented tangent's x-components at the two endpoints have opposite signs. At a fixed point, the y-component of T cross v has sign opposite to T_x. The two intersections of the quotient disk with the oriented axis consequently have opposite signs. The paired framing corrections are supported away from these points and preserve that conclusion. Hence lk(c,U)=0 and c is a crossing circle in the required sense. The preferred framing gives the canonical Sakuma link, rather than an arbitrary member of its framed family.

To obtain a PD code, sample/polygonalize these curves with certified separation, apply a generic projection to the resulting spatial link, and read its crossings with over/under heights. Close the axis through the outside of a large ball containing c. The computation is a finite geometric projection problem; no tangle slope choice remains. Keep the spatial curves or enough interval bounds to certify that polygonalization and projection do not introduce unintended intersections.

If a direct planar implementation is preferred, Snape's Figures 2.1–2.3 give exactly the equivalent clasp/coil substitutions. The newly rendered files are:

    work/next_theory/snape_figures/sakuma-049.png  (printed p24, Figure 2.1)
    work/next_theory/snape_figures/sakuma-050.png  (printed p25, Figures 2.2–2.3)
    work/next_theory/snape_figures/sakuma-051.png  (printed p26)
    work/next_theory/snape_figures/sakuma-052.png  (printed p27, framing lemma)

Snape's Lemma 2.1.2 independently calibrates this implementation: with the standard opposite clasp positions and even source writhe x, framing f gives m=x−f signed half-twists in the downstairs parallel-strand region. Thus preferred framing uses m=x. Use his crossing glyphs; an unoriented count of half-twists cannot substitute for the signed convention.

## 4. The exact computation and its built-in checks

For each specified n and inversion, compute the ordinary normalized Jones polynomial of S=U∪c and compare it with that of the two-component unlink. This is one exact polynomial comparison per candidate. Before reading that verdict, check the source knot's fraction/determinant and the constructed longitude's linking number zero. If using the planar clasp/coil implementation, additionally check against the spatial quotient construction on a small calibration input such as Snape's Figure-8 example I₁(2;1).

The recovered files provide a geometric construction but **no PD/braid word has been generated or independently certified in this pass**. The anti-equivariant normal field, paired framing correction, quotient-disk argument and intersection-sign check have a separate internal read. The pilot wiring, actual spatial realization, and crossing extraction still require the listed validation. A purported PD that omits the zero-framing correction is not an output of this recipe.

For nontrivial κ, S cannot be split: in the double cover branched along U, the two lifts of c are preferred parallels of κ; splitting c from U would make those lifts unknots in disjoint balls. Hence a verified unlink Jones polynomial for this S would be decisive, and the ±1 crossing-circle twists of U supply the ordinary-knot counterexample through the established equivalence.

## 5. Keep the two downstairs links distinct

S=U∪c above is the axis together with the quotient preferred longitude. The earlier link N is obtained by band surgery on U along the quotient arc p(κ), with cover Σ₂(N)=S³₀(κ). They are not the same diagram. The recipe here constructs **S**, as requested, and does not identify its bracket with that of N.

No new beyond-two-bridge seed is proposed in this pass. Delta=1 alone does not establish the FROB5 condition, and the archived compatible Whitehead tower already has a proved nonzero defect. Neither is a justification for adding an unscreened candidate list.

Source: [Snape thesis, Sections 1.2.2 and 2.1.1–2.1.2](https://theses.gla.ac.uk/39015/1/2018SnapePhD.pdf). The relevant full local text and rendered figures were inspected, rather than relying solely on the earlier wiring note.
