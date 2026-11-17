# Band transfer: a real Jones-defect recurrence and a seed obstruction

Date: 2026-11-03. Bounded theory pass; no computations. Scope: transforming a hypothetical nontrivial Jones-unit knot into a geometrically controlled knot using ribbon bands. No board edits.

Independent main-agent read: Claude130248 accepted the determinant-one fusion obstruction and its application to the standard ribbon double; TRUSTED label retained.

## Result of the pass

There is a genuine ordinary-Jones-preserving band mechanism, but the standard ribbon double of a Jones-unit knot cannot enter it. This closes a possibility left open in `relative_double_gate.md`: determinant one does **not** rescue a one-band seed, even when the Alexander polynomial is trivial.

The obstruction comes from an existing geometric theorem, not a new skein argument. No novelty claim is made for the corollary below.

## 1. The available exact operation

For a specified fusion-one ribbon presentation, let R_p denote insertion of p half-twists into the ribbon. Lobb's Theorem 1.4 gives

    H_N(R_p) = H_N(U) ⊕ M_N(R_p),
    M_N(R_{p+2}) = M_N(R_p)[2]{−2N}.

For reduced sl(2) homology, writing J(q) for its graded Euler characteristic, this implies the ordinary Jones identity

    J(R_{p+2};q) − 1 = q^(−4) (J(R_p;q) − 1).

Here q is Lobb's quantum-grading variable; conversion to another Jones convention only changes the displayed monomial. Thus Jones-unit status is constant on either parity class. Two independent one-band unlink resolutions permit opposite twist transfer. This is an actual topology-dependent mechanism using ordinary Jones, without requesting another color. [Lobb, Theorem 1.4 and proof of Theorem 1.2](https://arxiv.org/pdf/1105.3985).

## 2. Composite determinant-one knots cannot have fusion number one

Let f(R) be the ribbon fusion number: the least number of bands in a disk-and-band ribbon presentation. A fusion-one knot is obtained by joining an actual two-component unlink with one embedded band.

**Published input.** Bleiler–Eudave-Muñoz prove that a composite fusion-one knot has a nontrivial two-bridge summand. Their terminology is “ribbon number”; the introduction defines it using saddle points, so this is fusion number, not the count of ribbon singularities in an immersed disk. Their Theorem 1.3 treats the band sum of two split unknots. The proof starts with a nontrivial connected-sum decomposition and excludes both summands having bridge number at least three. [Original article, Trans. AMS 321 (1990), 231–243](https://doi.org/10.1090/S0002-9947-1990-0968881-9); [author-uploaded full text](https://www.researchgate.net/publication/303349776_Composite_ribbon_number_one_knots_have_two-bridge_summands).

**Corollary.** If R is a composite ribbon knot with det(R)=1, then f(R)≥2.

*Proof.* If f(R)=1, the published theorem supplies a nontrivial two-bridge summand B. A two-bridge knot b(p,q) has determinant |p|, and nontriviality forces |p|>1. Determinants multiply under connected sum and every knot determinant is a positive odd integer. Hence det(R)>1, a contradiction. Fusion number zero would make R the unknot. ∎

In particular, every nontrivial fusion-one Jones-unit knot would already be prime. This does not rule out such prime knots.

**Application to the natural double.** Let K be nontrivial and V_K=1, and let −K be its mirror with reversed orientation. Then

    R = K # (−K),
    V_R(t) = V_K(t)V_K(t^−1) = 1,
    det(R) = 1.

The knot R is ribbon and composite. The corollary therefore gives f(R)≥2. Consequently no construction requiring a one-band unlink resolution can have any member isotopic to this R. This is stronger than the previous branched-cover generator obstruction: it applies on the determinant-one fiber itself, including Δ_K=1.

## 3. More twist sites are not more fusion bands

Lobb's Theorem 3.2 uses a ribbon tangle with arbitrarily many twist sites. Nevertheless, the text immediately before it states that resolving **any one** of these sites by its designated ribbon gives the actual two-component unlink. Hence every knot in those families still has fusion number at most one. [Lobb, Section 3](https://arxiv.org/pdf/1105.3985).

Thus the higher-twist-site theorem cannot evade Section 2. No choice of its ribbon tangle or integer parameters can have seed K#(−K) for a nontrivial Jones-unit K.

This corrects the suggested escape at the end of `relative_double_gate.md`: a genuinely higher-fusion generalization remains a possible research problem, but Lobb's published Theorem 3.2 is not that generalization.

There is also no shortcut by starting the recurrence at an actual unknot. In that case the extra homology summand M_2 is zero, and stays zero at every same-parity twist. Reduced Khovanov unknot detection then makes every such knot an actual unknot. [Kronheimer–Mrowka](https://arxiv.org/abs/1005.4346). An analogous conclusion holds along the fixed-sum, fixed-parity transfers in Lobb's theorem if one member is the unknot.

## 4. The precise remaining construction gate

The obstruction is scoped: it does not exclude a different operation that first produces a prime fusion-one Jones-unit knot directly, or a construction with genuine fusion number at least two. It does exclude obtaining one merely by putting extra twist sites into the known one-band mechanism with the standard double as seed.

A useful replacement would have to supply all three pieces explicitly:

1. A ribbon presentation of K#(−K) with at least two necessary fusion bands.
2. A skein relation for a geometrically effective modification in which every intermediate closure term is determined by V_K, or cancels by a proved relation between actual diagrams.
3. An independent proof that some modification removes the connected-sum decomposition and, if required, creates a strong inversion.

In the one-band proof, the intermediate link is the actual two-component unlink. With several necessary bands, resolving only one leaves a generally knotted intermediate link. Its polynomial is new data. Resolving all bands at once yields the unlink but does not identify all the intermediate skein terms. No identity eliminating those terms was found here. This is the missing gate, rather than the number of available twist parameters.

**Judgment:** the positive recurrence is real prior art; the determinant-one fusion obstruction is a useful exact consequence of prior art and closes the proposed conditional seed. No new universal transformation or route to Jones unknot detection is established.
