# Topology of an affine multitwist family of unknots

Date: 2026-11-03. Bounded theory pass; no computations or board edits. This supplies a topology-sensitive endpoint for the finite-union-of-affine-flats description of a Jones-unit fiber. It is not a classification of all cosmetic multitwists.

## 1. A precise reduction using hyperbolic filling

Fix a knot K and disjoint twisting disks D_1,...,D_r, with disjoint boundaries C_i. The disks may meet K in more than two points; when applying the cosmetic crossing theorem below, restrict to two oppositely oriented intersections. Let K(n) be the knot obtained by −1/n_i surgery on C_i, with n_i=0 meaning no surgery. The C_i form an unlink in S^3, so these simultaneous surgeries give S^3. Set

    M = E(K ∪ C_1 ∪ ... ∪ C_r).

Choose meridian-longitude bases so the filling slope at C_i is μ_i−n_i λ_i. Leave the K boundary unfilled.

**Hyperbolic escape lemma.** If M is hyperbolic, there are finite sets E_i⊂Z such that

    K(n)=U  ⇒  n_i∈E_i for at least one i.

In other words, the actual unknot locus is contained in finitely many coordinate hyperplanes. In particular, along any affine integer line n=a+kv with every v_i nonzero, all sufficiently large |k| give nontrivial hyperbolic knots.

*Proof.* Hyperbolic Dehn filling provides finite exceptional slope sets, one per filled cusp, outside of which the simultaneous filling remains hyperbolic. Each integer n_i gives a different slope, so their inverse images E_i are finite. A solid torus is not hyperbolic. Along the stated line all filling slopes escape these finite sets. ∎

Primary input: [Thurston, The Geometry and Topology of Three-Manifolds, Section 5.8](https://library.slmath.org/nonmsri/gt3m/PDF/Thurston-gt3m.pdf). The same filling theorem gives convergence of volume to vol(M), with strictly smaller volume at each nontrivial hyperbolic filling; hence the line has infinitely many knot types, not merely infinitely many parameters.

**Affine-flat version.** Let F=a+Λ⊂Z^r have positive rank. Call coordinate i inactive if it is constant on F. Fill all inactive cusps at their constant slopes, and let M_F be the resulting exterior with the other crossing circles retained. If every K(n), n∈F, is an unknot, then M_F is nonhyperbolic.

*Proof.* For each active coordinate its restriction to Λ is a nonzero integral homomorphism. A finite union of proper rational subspaces cannot cover Λ. Thus choose v∈Λ with every active coordinate nonzero, apply the escape lemma to M_F, and obtain a contradiction. ∎

This is important: one must fill the **constant coordinates first**. A hyperbolic original link can contain an entire coordinate line of unknots because a fixed exceptional filling makes the remaining exterior nonhyperbolic.

## 2. What this gives the Jones-flat calculation

Suppose the polynomial calculation has established V(K(n))=1 on an entire positive-dimensional integer flat F.

- If M_F is hyperbolic, the flat yields nontrivial hyperbolic Jones-unit knots at all sufficiently large points on a generic integer line. This is an unconditional counterexample certificate, conditional only on the two checkable premises: exact polynomial identity and hyperbolicity of M_F.
- If Jones detects the unknot, every such M_F must instead be nonhyperbolic.

For a fixed hyperbolic parent, the all-unknot alternatives are confined to finitely many exceptional coordinate slices. After taking such a slice, inspect the partially filled exterior afresh. The remaining geometric problem lies in the nonhyperbolic descendants and their sphere/torus/annulus structure. This is a reduction to actual link exteriors, not an assertion that scalar cancellation itself produces an annulus.

No general theorem classifying those nonhyperbolic descendants was established here. In particular, a JSJ torus can become compressible after filling, and induced slopes on its other side need not be the original affine parameters. A purported recursive annulus classification must handle this explicitly.

## 3. Axis directions and diagonal directions behave differently

For genuine two-strand crossing disks, if an actual unknot K(a) and K(a+d e_i), d≠0, are both unknots, then the image of C_i is nugatory in the complement of K(a). This is the generalized cosmetic-crossing theorem for the unknot. One may therefore prune coordinate directions, but the conclusion concerns the single crossing circle after all other coordinates have been fixed. It supplies no simultaneous disjoint disks avoiding every other C_j. A primary discussion is [Balm–Kalfagianni, Cosmetic crossings of twisted knots](https://users.math.msu.edu/users/kalfagia/BalmK3.pdf), Introduction, attributing the unknot case to Scharlemann–Thompson and Gabai.

An oblique line cannot be replaced by one crossing change. Here is an elementary model that any classification must allow. Start with the usual crossing circle for the unknot whose twists produce a nontrivial twist-knot family K_m, with K_0=U. Replace that circle by two parallel copies in its product neighborhood, and split the twist amount into p and q. The resulting family is

    K(p,q) = K_(p+q).

Thus K(k,−k)=U for every k, although neither circle is nugatory at the base unknot: twisting either alone produces nontrivial twist knots. The two circles cobound an annulus disjoint from K, and opposite twists cancel in its product neighborhood. Its active exterior is nonhyperbolic, exactly as the lemma predicts.

This is not merely a scalar skein coincidence. It is an explicit ambient cancellation supported by the annulus. Taylor's Remark 5.3 records the general cancellation when an annulus is disjoint from the knot. [Taylor, Closures of 1-tangles and annulus twists](https://arxiv.org/pdf/2506.11226).

## 4. One available obstruction inside the annular remainder

Taylor's 2025 preprint, Theorem 1.3, treats an unknot K_0 and an unknotted twisting annulus A meeting it once. If A is sufficiently incompressible, there is at most one additional unknot parameter, and it must be q=±1. Here A lies in a sphere P, neither boundary curve bounds a disk missing K_0, and sufficient incompressibility means every compressing disk for P\K_0 has boundary meeting ∂A more than twice. [Taylor, Definition 5.1 and Theorem 1.3](https://arxiv.org/pdf/2506.11226).

Consequently an all-unknot integer annulus-twist line of this specific type must fail one of these geometric hypotheses. If all other hypotheses hold, there must be a compressing disk whose boundary meets ∂A at most twice. That is a concrete low-complexity disk certificate, stronger than merely calling the annulus nonhyperbolic. The result is cited as a preprint theorem, not independently re-proved here. It does not classify annuli meeting K many times or arbitrary disk-multitwist directions.

## Judgment

The usable first lemma is the hyperbolic escape lemma and its active-flat corollary. It converts a formal Jones-unit flat into either an actual counterexample family or a sharply specified nonhyperbolic link-exterior problem. Parallel-annulus cancellation shows why “every active circle is nugatory” is false. Proving that all surviving flats arise from such visible cancellation would be a substantial new topology theorem; neither hyperbolic filling nor the scalar Jones identity proves it.
