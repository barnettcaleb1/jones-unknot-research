# CT: what topology proves, and the missing JSJ step

Date: 2026-11-03. Bounded theory check of Claude 132126. No Jones detection assumed; no computation or board edits.

**Verdict.** CT is proved below for a two-disk template with hyperbolic augmented exterior, and for a single planar Seifert block. The general JSJ claim is not established. Induced internal meridians need not be affine in several parameters. Nevertheless, actual unlink disk-twist templates have an important globally affine longitude that arbitrary Dehn-filling examples lack. No nonlinear actual unknot locus is produced here.

## 1. An exact restricted CT theorem

**Proposition.** Let K(n₁,n₂) be obtained by full twisting along two disjoint disks, and suppose E(K∪C₁∪C₂) is hyperbolic. Then

    {(n₁,n₂)∈Z² : K(n₁,n₂)=U}

is a finite union of coordinate lines and individual points.

**Proof.** Hyperbolic Dehn filling supplies finite exceptional parameter sets E₁,E₂ such that an unknot parameter must satisfy n₁∈E₁ or n₂∈E₂. This is the escape lemma of `unknot_multitwist.md`; only finitely many coordinate lines need be considered.

Fix one such line, say n₁=c. Surgery on C₁ leaves S³ and preserves the other twisting disk, because the original disks are disjoint. The remaining family is an ordinary one-circle twist family of knots in S³. If its wrapping number is at most one, its knot type is constant. If wrapping exceeds one, at most two parameters are unknots. Thus the actual unknot set on this line is either the whole line or at most two points. Take the finite union over the exceptional lines. ∎

The one-circle input is explicitly recorded in [Baker–Motegi, Seifert vs. slice genera of knots in twist families, arXiv v1](https://arxiv.org/pdf/1705.10373v1), introductory page 2: wrapping at most one gives a constant family, while wrapping greater than one permits at most two unknot parameters, citing their references [32,36]. This is a topological statement, independent of Jones. In particular, the one-circle base case is not accurately described solely as “all parameters when nugatory”: a meridian circle also gives a constant family.

The proposition does not extend automatically to three or more disks: an exceptional coordinate filling can leave a nonhyperbolic multi-cusp exterior, precisely the unresolved case.

## 2. CT for one planar Seifert block, including fiber fillings

Let Σ be a disk with r holes and M=Σ×S¹. Leave the outer torus unfilled. On each inner torus use the section/fiber basis (μᵢ,f), and fill at a primitive slope

    αᵢ(nᵢ)=aᵢ(nᵢ)μᵢ+bᵢ(nᵢ)f,

where each coefficient is affine in its own integer parameter and the pair is primitive for every integer parameter (as for a fixed basis change applied to μ−nλ).

**Proposition.** The filled manifold is a solid torus exactly when at most one index i has |aᵢ(nᵢ)|≠1. Consequently its solid-torus parameter locus is a finite union of coordinate affine flats.

**Proof without fiber slopes.** When every aᵢ≠0, filling gives a Seifert manifold over a disk with exceptional orders |aᵢ|>1. With at most one exceptional fiber it is a solid torus. With at least two, its fundamental group surjects onto the noncyclic free product of the corresponding finite cyclic groups, so it cannot be a solid torus.

**Fiber slopes.** If aᵢ=0, primitivity gives bᵢ=±1. Fiber-parallel filling splits the block into a connected sum of a solid torus and the lens spaces contributed by the other filled boundary components. A further fiber-parallel filling contributes an S¹×S² summand. Therefore the result is a solid torus precisely when there is only one fiber filling and every other |aⱼ|=1. Equivalently, there is still at most one index with |aᵢ|≠1. One can also see the obstruction from the presentation

    π₁ = <x₁,...,xᵣ,h | h central, xᵢ^(aᵢ) h^(bᵢ)=1>:

a fiber filling kills h and leaves the free product of Z factors from the zero aᵢ and finite cyclic groups from the nonzero aᵢ. For the decomposition itself, choose disjoint arcs in the planar base with both endpoints on the fiber-filled boundary, cutting off the other boundary circles one at a time. Their products with S¹ are annuli; after fiber filling, cap their boundary circles by meridian disks to obtain separating spheres. Cutting along those spheres gives the stated solid-torus and lens-space summands. For background see [Martelli, Geometric topology, Chapter 10](https://people.dm.unipi.it/martelli/Geometric_topology.pdf). The specific proposition number appeared in search extraction but was not checked in the full PDF, so it is not used here.

Finally, for each i the equation |aᵢ(nᵢ)|=1 has finitely many solutions, all integer solutions, or no solutions. Take the union over the possible unrestricted index. This is a finite union of coordinate flats. ∎

Fixed exceptional fibers may be included as fixed entries in this criterion. This proves a single-block statement; it does not prove closure of the class under arbitrary JSJ gluing.

## 3. The induced-slope assertion needs correction

Even the pair-of-pants block demonstrates nonlinear internal slope propagation. Write μ₀+μ₁+μ₂=0 in homology. Fill

    α₁=a(n)μ₁+b(n)f,       α₂=μ₂+m f.

Every such filling is a solid torus, because there is at most one exceptional fiber. Its primitive outer meridian is

    a(n)μ₀ − (b(n)+a(n)m)f.

Indeed μ₂=−m f and μ₁=−μ₀+m f; substituting in α₁ yields the displayed relation. Its coefficients are primitive because gcd(a,b+am)=gcd(a,b)=1.

For a(n)=n and b(n)=1 the meridian is

    n μ₀ − (1+nm) f.

Thus even the homogeneous primitive slope vector can be bilinear, not just fractional-linear after choosing rational coordinates. A fixed torus gluing preserves linearity of a single slope pair; the nonlinear operation here comes from filling and eliminating through a block with multiple varying inputs.

**This is not a counterexample to CT or an actual disk-twist template.** In this example α₁=nμ₁+f is not necessarily a −1/n filling in the preferred framing of an unknotted twisting circle in S³. The unknot-preserving ambient surgery condition is additional structure. General cable-space slope facts likewise cannot be imported without the markings; see, for example, [Meier, Small Seifert fibered surgery on hyperbolic pretzel knots, Section 2](https://msp.org/agt/2014/14-1/agt-v14-n1-p16-s.pdf) for solid-torus cable fillings and compression behavior.

## 4. Global slope conservation for actual disk twists

For the actual template, the Cᵢ form an unlink. Put ℓᵢ=lk(K,Cᵢ). In H₁(E(K∪C)), with preferred longitudes,

    λᵢ=ℓᵢ μ_K,                 λ_K=Σᵢ ℓᵢ μᵢ.

Use the sign convention in `unknot_multitwist.md`, filling μᵢ−nᵢλᵢ. Then μᵢ=nᵢℓᵢμ_K and the filled exterior has H₁=Z generated by μ_K. The kernel of the surviving boundary map is generated by the primitive curve

    λ_K − (Σᵢ nᵢ ℓᵢ²) μ_K.

If the exterior is a solid torus, this is its disk meridian. Thus the **global** meridian is indeed affine in the original parameters, even if intermediate JSJ slopes are not. This homology calculation is exact and should be retained in any proposed induction.

It does not detect a solid torus: every knot exterior has H₁=Z and a primitive homological longitude, whether or not that longitude bounds a disk. Nor does it by itself turn the nonlinear intermediate equations into a finite list of affine constraints.

## 5. Precise remaining gap

Hyperbolic filling reduces to finitely many exceptional coordinate slices. A planar Seifert block has the explicit affine solid-torus locus above. What is not yet proved is that, when these pieces are assembled and tori compress, the resulting conditions pull back to finitely many integer affine flats in the original unlink-twist coordinates. An induction must retain the marked global longitude and account for new compressions and reducible fillings; “the induced slopes are affine” cannot substitute for that argument.

Accordingly CT is plausible but not established by the proposed paragraph. The two-disk hyperbolic proposition and the single-block proposition are finished restricted results; neither uses Jones unknot detection.
