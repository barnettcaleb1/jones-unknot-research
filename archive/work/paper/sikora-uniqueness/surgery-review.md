# Surgery and peripheral review for paper 1

3 November 2026. Scope: the framed hypotheses, recovery of peripheral data, signed matched fillings, Casson–Walker applicability, and the longitudinal case. Read the requested decision letter, both authoritative output files, the earlier surgery audit, and LATE-41 including its corrective addendum. No fatal gap found in these steps. The following lemma is suitable for the manuscript.

## Conventions to fix once

Orient both tangle balls compatibly with their common marked model ball. Orient a double branched cover by requiring the covering map to preserve orientation away from its branch set. The common boundary marking then lifts to an orientation-preserving map of the boundary tori. Attachment of the closing ball is a different map: as usual its boundary gluing reverses the outward boundary orientation. These two maps must not be conflated.

For a knot \(K\) in an oriented homology sphere, use its positive meridian and preferred longitude. On the peripheral torus oriented as \(\partial\nu K\), they satisfy \(\mu\cdot\lambda=+1\). This torus orientation is the **negative** of the outward-boundary orientation of the exterior. Indeed oriented tubular coordinates have volume form \(r\,dr\wedge d\theta\wedge ds\), where \(s\) increases along \(K\); \(\partial\nu K\) has orientation \(d\theta\wedge ds\), and the meridian and longitude increase in \(\theta\) and \(s\), respectively. Reversing the knot reverses both peripheral classes. Define \(p/q\) surgery by filling the unoriented slope of \(p\mu+q\lambda\).

This convention makes the displayed surgery coefficients agree literally with the usual \(p/q\) convention. Alternatively retain outward-boundary intersection conventions, but translate their sign consistently before using a surgery formula.

## Lemma: marked peripheral data give identical signed surgery coefficients

Let \(X\) and \(R\) be tangles with the same marked boundary in compatibly oriented balls, with \(R\) rational. Let \(M\) and \(V\) be their oriented double branched covers. Identify their unoriented slopes through the lifted boundary marking. Let \(\lambda\) be the disk-bounding slope of the solid torus \(V\), and choose a slope \(\mu\) at distance one from \(\lambda\). Suppose

\[
\det C_\mu(X)=1,\qquad \det C_\lambda(X)=0.
\]

Then \(Y=M(\mu)\) is an integral homology sphere, \(M\) is the exterior of the filling core \(K\subset Y\), and \(\lambda\) is its preferred-longitude slope. Orient the common peripheral pair using the preceding convention. For any rational closing tangle \(P\), write its common lifted filling slope as

\[
\alpha_P=p\mu+q\lambda,\qquad \gcd(p,q)=1.
\]

If \(C_P(X)\) and \(C_P(R)\) are ambient isotopic, then

\[
Y_{p/q}(K)\cong_+ S^3_{p/q}(U),
\]

where \(U\) is the unknot and \(\cong_+\) denotes an orientation-preserving homeomorphism. The ratio \(p/q\) is independent of the choice of lift of the boundary marking. No preservation of filling cores by the displayed homeomorphism is required.

**Proof.** The determinant/homology presentation of a branched double cover gives \(H_1(Y;\mathbb Z)=0\), hence \(H_2(Y;\mathbb Z)=0\). Let \(N\) be the filling solid torus. Mayer–Vietoris gives

\[
H_1(\partial M;\mathbb Z)\xrightarrow{\sim}
H_1(M;\mathbb Z)\oplus H_1(N;\mathbb Z).
\]

Consequently \(H_1(M;\mathbb Z)=\mathbb Z\), and the image of \(\mu\) generates it. The map \(H_3(Y)\to H_2(\partial M)\) is an isomorphism, so the same sequence gives \(H_2(M)=0\). For the preferred longitude \(\lambda_K\), filling \(p\mu+q\lambda_K\) has first homology \(\mathbb Z/p\mathbb Z\), with \(\mathbb Z\) when \(p=0\). Thus the determinant-zero filling identifies the primitive slope \(\lambda\) with \(\lambda_K\).

The same marked pair on \(V\) identifies \(V(\mu)\) with \(S^3\); its filling core \(U\) is an unknot because its exterior is the solid torus \(V\). On each filled-in solid torus orient the core so that \(\lambda\) runs once positively along it. The intersection convention then makes \(\mu\) its positive meridian. Thus \((\mu,\lambda)\) is a standard meridian/preferred-longitude pair on **both** exteriors.

The two lifts of the common boundary marking differ by the deck involution. The four-point-branched torus cover has the model \(\mathbb R^2/\mathbb Z^2\to (\mathbb R^2/\mathbb Z^2)/(x\mapsto-x)\), so this involution acts by \(-I\) on first homology. It reverses both peripheral classes, leaving \(p/q\) unchanged. More generally an orientation-preserving identification preserving the two individual peripheral slopes has diagonal signs \(\epsilon_1,\epsilon_2\) with \(\epsilon_1\epsilon_2=1\); it cannot reverse just one of them. Fixing \(\mu\) also excludes a meridional shear, and the homological kernel excludes a longitudinal shear.

Because the same closing tangle is attached through the same marked sphere, its solid-torus cover has the same filling slope on \(M\) and \(V\). Hence these fillings are precisely \(Y_{p/q}(K)\) and \(S^3_{p/q}(U)\), with the same signs. Here \(p/q\) is a **peripheral surgery coordinate**, not necessarily the Conway fraction assigned to \(P\).

Finally an ambient isotopy of the branch links preserves the mod-two meridional character defining their branched double covers, and therefore lifts to a homeomorphism of the filled covers. Away from the branch locus the covering maps and the underlying isotopy preserve orientation, so the lift does also; it extends across the branch locus. This proves the claimed oriented homeomorphism. The coefficient comparison preceded this lift and does not require it to preserve the chosen decomposition or its core. ∎

For two nonlongitudinal probes, choose \(\mu\) distinct from both **before** defining \(Y\) and \(K\). Then \(p_iq_i\ne0\), and distinct slopes give \(q_1/p_1\ne q_2/p_2\).

## Framed scope and surgery formula

No additional orientation or global framing hypothesis narrows Sikora's conjecture. Section 4 uses balanced framing; each allowed move becomes an ordinary ambient isotopy after the framing is forgotten. Section 4.1 requires the probes to be distinct as unframed tangles. A single framed unknown in both equations is part of the system's definition. Theorem 21 supplies exact bracket-vector equality; hence the auxiliary determinant hypotheses in the lemma. General tangles with closed components can be handled by the same skein linearity; determinant one then excludes those components. [Sikora, arXiv v2, Sections 4–4.1 and Theorem 21](https://arxiv.org/html/2005.08162v2).

Ni–Wu Proposition 3.1, equation (7), printed p. 9, explicitly applies to null-homologous knots in rational homology spheres, with symmetric \(\Delta_K(1)=1\). It defines \(L(p,q)\) by unknot surgery and gives

\[
\lambda_{\rm CW}(Y_{p/q}(K))=\lambda_{\rm CW}(Y)+\lambda_{\rm CW}(L(p,q))+
\frac{q}{2p}\Delta_K''(1).
\]

Their normalization gives value \(1\) on \(+1\) surgery on the right-handed trefoil. Here every knot in \(Y\) is null-homologous. The two matched equations therefore cancel the lens terms and force \(\Delta_K''(1)=0\) by subtraction. The ambient \(Y\) need not be \(S^3\) or an L-space. [Ni–Wu, published author PDF](https://www.its.caltech.edu/~yini/Published/Cosmetic.pdf).

Ni–Wu cite Boyer–Lines Theorem 2.8. I re-read Ni–Wu's published statement, not Boyer–Lines's original. Cite the former directly for the exact formula; credit the latter without implying an original-source check that has not occurred.

## Longitudinal probe: applicability and proof

If a probe has slope \(\lambda\), its rational comparator closure is the two-component unlink. An **actual** closure isotopy gives \(M(\lambda)=S^1\times S^2\). Let \(J\) be this filling core. The other distinct slope is nonlongitudinal and supplies an actual lens-space, hence L-space, surgery on \(J\). It need not have distance one from \(\lambda\).

Rasmussen–Rasmussen Proposition 7.8 applies with \(Z=S^3\): an L-space surgery on a knot in \(Z\#(S^1\times S^2)\) makes its exterior a generalized solid torus. Definition 7.2 supplies Floer simplicity and \(\deg\overline\Delta(M)<g_M\). Section 7 identifies \(g_M\) with the longitude's order, and also gives \(|T|=k_Mg_M\). Here \(T=0\), so \(g_M=k_M=1\); the normalized nonzero polynomial has degree zero. Boundary incompressibility would contradict Corollary 2.3, which gives norm \(-1\). Thus the boundary compresses. Previously established irreducibility makes \(M\) a solid torus. [Rasmussen–Rasmussen, arXiv v2, Section 7, Definition 7.2, Proposition 7.8, Corollary 2.3](https://arxiv.org/html/1508.05900v2).

I checked Proposition 7.8's statement and proof: it explicitly treats the general-distance case after the distance-one case. This establishes applicability; it is not a new proof of that Floer-theoretic input. The source's first displayed definition of \(g_M\) omits the boundary inclusion; using its equivalent longitude-order description or \(|T|=k_Mg_M\) avoids reproducing that typo.

## Resolution of differences between the supplied notes

Use the authoritative audited proof's RR 7.8 route. The earlier part of LATE-41 offers Sikora Proposition 10(1) as a shortcut, but its addendum retracts that suggestion. No step here uses Proposition 10(1), nor a Property-R assertion for arbitrary homology spheres. The earlier surgery audit's signed-coefficient conclusion remains valid; the explicit peripheral orientation convention above strengthens its presentation. No change to the main theorem's hypotheses is needed.
