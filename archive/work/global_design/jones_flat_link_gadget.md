# Gate for a Jones-flat crossing-circle link with an unknot band

2026-11-03. Bounded constructive literature check; no diagram search or new computations.

## Result

I did not obtain the requested marked gadget. The standard EKT unknot-seed construction cannot supply its actual-unknot band at **any** site. Its polynomial-preserving operation also is not a single crossing-circle twist. Ren supplies cancellation of a highest channel, not the required one-disk flatness. A nearby explicit Shah construction replaces a rational tangle by a nonrational one and produces a fake Hopf link, but its stated result does not certify either marked site.

These are exclusions of specified constructions, not a claim that no suitable Jones-flat link exists.

## 1. EKT's preservation is a compensated two-place operation

Primary source: Eliahou–Kauffman–Thistlethwaite, *Infinite families of links with trivial Jones polynomial*, Topology 42 (2003), 155–169, [Sections 3–4](https://homepages.math.uic.edu/~kauffman/ekt.pdf). Local full text: `work/attack/ekt.txt`.

Their marked operation is

    T^ω = (T+2)·1·2,
    H(T,U)^ω = H(T^ω,U^(ωbar)),

where ωbar is the inverse boundary operation. If Ω is its bracket-vector matrix and H the Hopf-pairing matrix, preservation comes from

    Ωᵀ H Ω⁻¹ = H.

This is a compensation identity between two varying tangles. It does not say that either tangle has a zero moving coefficient when the other is held fixed. Their bracket theorem is Theorem 3.2; their oriented normalized-Jones statement uses ω² (Theorem 3.2′), since ω itself can change the writhe correction through component orientations.

There is also a marked mapping-class distinction. On boundary slope homology the operation is represented by

    Ω_hom = [[3,8],[1,3]],

with eigenvalues 3±√8. A single Dehn twist on the torus double cover has parabolic homology action, with eigenvalues ±1. Thus ω and its nonzero powers are not one twist in this four-punctured-sphere mapping class. This does **not** rule out some different surgery description of a particular output link; it prevents relabeling the published ω motion as the requested single-disk flatness.

## 2. Every nontrivial member of the standard unknot-seed orbit fails the band anchor

The already-derived all-seed homology proposition in `work/band_obstructions.md`, §7, applies to arbitrary 2-tangles S with actual numerator closure U. For

    L_j = H(S, infinity+2)^(ω^j),

write the primitive boundary pair of S as (1,d), and

    Ω_hom^j = [[a,8b],[b,a]],    a>0,    a²−8b²=1.

The recorded Fox/Mayer–Vietoris presentation is

    H_1(Σ_2(L_j)) = Z ⊕ coker [[a, -2(b+ad)], [2b, a+8bd]]
                 = Z ⊕ Z/|D|,
    D = 1 + 12b(b+ad).

The first Smith factor is one because a is odd and gcd(a,b)=1. Since D≡1 mod12, |D|=1 requires D=1. This gives b=0 or b=−ad. The latter forces a|b, hence a=1 and then b=0. Therefore |D|>1 whenever j≠0. The j=0 member is the actual unlink.

If a two-component L admits a band fusion to U, reversing the band and taking double branched covers presents Σ_2(L) as Dehn surgery on a knot in S³. A surgery with first Betti number one is zero surgery, whose integral first homology is Z, with no finite torsion. Hence **no nonzero L_j admits any band to U**, regardless of where a proposed second marked site is placed.

This includes the standard LL1/LL2 instances arising from that seed construction. It does not assert the same homology formula for all conceivable EKT-type pairings or all links sharing the unlink Jones polynomial.

## 3. Ren is not a flat moving sector

[Ren's wrapping-number counterexample](https://arxiv.org/html/2609.11084v2) eliminates a top annular sector. The archived stronger calculation for its particular core with any attached four-strand braid is

    [R_β] = c_0 e_0 + c_2 e_2,    c_2 ≠ 0.

See `work/ren-braid-obstruction-note/main.tex` and `work/global_design/skein_pattern_design.md`, §2. Under meridional twisting these sectors have distinct twist eigenvalues. In the winding-zero setting the e₂ sector moves and therefore cannot remain polynomially constant. This is precisely the lower-sector obstruction already known here; no new computation was performed.

Converting a closed annular polynomial into a banded link requires retaining the attachment intervals in a relative skein module. A closed-class identity alone does not specify the additional unknot band.

## 4. What the Jones-cosmetic sources actually provide

Pamela Shah's 2023 UBC abstract concerns rational knots and closures of the (3,−2) pretzel tangle with equal Jones polynomial. The nearby accessible primary artifact is her [2025 *A Fake Hopf Link* postcard](https://personal.math.ubc.ca/~liam/MRP/cards/mrp_2_5.pdf). It explicitly replaces a rational tangle R by a nonrational tangle T in a Hopf-link presentation and obtains

    V_L(t) = t³ V_H(t).

That is a concrete tangle-replacement example, but the postcard does not identify a crossing circle producing a constant Jones twist family, or a marked band to U. Equality under one general replacement cannot be upgraded to a zero twist coefficient. I have not extracted a usable gadget from its diagram.

[Kotelskiy–Lidman–Moore–Watson–Zibrowius, *Cosmetic operations and Khovanov multicurves*](https://pmc.ncbi.nlm.nih.gov/articles/PMC11139753/) proves split-tangle detection and eventual distinctness for nonnugatory twist families (Theorems 1.4 and 1.6), but supplies no such Jones-flat marked link in the portions checked. Those categorified distinctions are compatible with a hypothetical Jones-only flat family.

## 5. A cheap marking restriction

For an oriented two-component link, the derivative of the normalized Jones polynomial at 1 is a fixed nonzero multiple of its linking number. Consequently a full-twist disk meeting the two different components once each cannot preserve the exact normalized Jones polynomial: it changes their linking number by ±1 per twist. A prospective two-point flat site must therefore meet one component twice. This restriction does not apply if arbitrary monomial factors are allowed, which is why Shah's shifted equality is not an exact-flatness certificate.

## Recommendation

Do not spend a second pass looking for an unknot band inside the standard EKT opposite-ω orbits: the torsion formula excludes every marking at once. The missing object is genuinely relative: a two-component link with a specified same-component twist disk whose moving skein coefficient vanishes, together with a separate specified band and an isotopy proving its fusion is U. None of the sources checked supplies that package. The current evidence supports a gap report, not a proposed candidate family.
