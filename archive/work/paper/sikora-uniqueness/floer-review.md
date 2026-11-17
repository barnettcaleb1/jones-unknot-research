# Floer, torsion, and compression argument for the manuscript

Prepared 3 November 2026. This file supplies insertion-ready mathematical text and a citation audit. It follows `outputs/rational-tangle-uniqueness-audited-proof.txt`; where the earlier editor synthesis in `collab/audits/LATE-41-audit.md` suggests using Sikora's Proposition 10, its corrective addendum and the authoritative proof govern. That suggested shortcut is not used. No new counterexample search was performed.

All RR theorem numbers and page numbers below refer explicitly to **arXiv:1508.05900v2**, not to unchecked journal numbering. The paper was published in *Advances in Mathematics* **322** (2017), 738–805, DOI [10.1016/j.aim.2017.10.014](https://doi.org/10.1016/j.aim.2017.10.014). The [v2 HTML](https://arxiv.org/html/1508.05900v2) and [v2 PDF](https://arxiv.org/pdf/1508.05900v2) were inspected directly for this review. A sentence pinning the numbering to this version should accompany the bibliography entry.

## 1. Preliminary facts and notation

Throughout, manifolds are compact, connected and oriented, and a knot exterior includes its boundary. A slope is a primitive element of the first homology of a boundary torus, considered modulo multiplication by \(-1\). For a manifold \(M\) with one torus boundary component, write \(M(\alpha)\) for its Dehn filling along \(\alpha\).

An integral homology solid torus is a manifold with
\[
H_1(M;\mathbb Z)\cong\mathbb Z,
\qquad H_2(M;\mathbb Z)=0.
\]
Its homological longitude \(\lambda\) is the primitive boundary class in the kernel of
\(\iota:H_1(\partial M;\mathbb Z)\to H_1(M;\mathbb Z)\).
The map \(\iota\) is surjective: by duality and the universal coefficient theorem,
\[
H_1(M,\partial M;\mathbb Z)\cong H^2(M;\mathbb Z)=0,
\]
and the conclusion follows from the long exact sequence of the pair.
Consequently, for a basis \((\mu,\lambda)\) with \(\mu\cdot\lambda=1\), the class \(\iota(\mu)\) generates \(H_1(M;\mathbb Z)\). Mayer–Vietoris gives
\[
H_1\bigl(M(p\mu+q\lambda);\mathbb Z\bigr)
\cong H_1(M;\mathbb Z)/\langle p\iota(\mu)\rangle.
\tag{F.1}
\]
Thus this group is \(\mathbb Z/|p|\mathbb Z\) for \(p\ne0\), and is \(\mathbb Z\) for \(p=0\). In particular \(Y=M(\mu)\) is an integral homology sphere, and the core \(K\) of its attached solid torus has exterior \(M\), meridian \(\mu\), and preferred longitude \(\lambda\).

We use the symmetric normalization
\[
\Delta_K(t^{-1})=\Delta_K(t),\qquad \Delta_K(1)=1.
\tag{F.2}
\]
For a nonzero Laurent polynomial, its degree in this discussion is its **breadth**, the largest exponent minus the smallest exponent. For a polynomial with nonzero constant term this is its ordinary polynomial degree.

Let \(\mathcal L(M)\) denote the set of slopes whose fillings are L-spaces. The results of Rasmussen–Rasmussen used below have the following precise content.

* Proposition 1.3, p. 2: \(M\) is Floer simple exactly when \(|\mathcal L(M)|>1\).
* The paragraph before Proposition 1.4, p. 2, and Section 2.1, p. 6, fix the torsion normalization with no negative terms and a nonzero constant coefficient. Proposition 1.4 restricts its coefficients to \(0,1\) for a Floer simple manifold; Proposition 2.2, p. 6, makes the coefficients eventually \(1\).
* Section 2.1, p. 6, gives \(\tau(M)\sim\Delta_K(t)/(1-t)\) when \(H_1(M)=\mathbb Z\), and defines \(\bar\tau=\Phi(\tau)\), \(\bar\Delta=(1-t)\bar\tau\), where \(\Phi\) is induced by the torsion-free projection on homology.
* Corollary 2.3, p. 7: if \(M\) is boundary incompressible and Floer simple, then
  \[
  \|M\|=\deg\bar\Delta(M)-1,
  \tag{F.3}
  \]
  where \(\|M\|\) is the Thurston norm of a generator of \(H_2(M,\partial M;\mathbb Z)\).
* Definition 7.2, p. 43, defines a generalized solid torus by Floer simplicity and \(\deg\bar\Delta(M)<g_M\). The integer \(g_M\) is the order of the image of the homological longitude, as specified in the Section 7 preamble, p. 42.
* Proposition 7.8, pp. 45–46, applies to a knot in \(Z\#(S^1\times S^2)\), with \(Z\) a rational homology sphere: an L-space surgery implies that its exterior is a generalized solid torus.

Here \(\sim\) denotes equality up to multiplication by a unit \(\pm t^a\) where relevant. We only use (F.3), not the separate fibering assertion in Corollary 2.3. Our application establishes irreducibility before invoking the corollary.

## 2. Irreducibility supplied by an actual lens-space filling

**Lemma F.1.** Let \(M\) be a compact connected orientable three-manifold with boundary a torus and \(H_1(M;\mathbb Z)\cong\mathbb Z\). If some filling \(M(\alpha)\) is a lens space with finite first homology, including \(S^3\), then \(M\) is irreducible.

**Proof.** For any compact connected orientable three-manifold \(W\) with one torus boundary component, doubling along the boundary gives \(\chi(W)=\frac12\chi(\partial W)=0\). Since \(b_0(W)=1\) and \(b_3(W)=0\), we have
\[
b_1(W)=1+b_2(W)\ge1.
\tag{F.4}
\]

First exclude a nonseparating embedded sphere in \(M\). Such a sphere splits off an \(S^1\times S^2\) connected summand, leaving a manifold with the same torus boundary. By (F.4) this would give \(b_1(M)\ge2\), a contradiction. The connected-sum construction from a nonseparating sphere is described in [Hatcher, Proposition 1.4 and its proof](https://pi.math.cornell.edu/~hatcher/3M/3Mfds.pdf), pp. 6–7.

Now let \(S\subset\operatorname{int}M\) be any separating sphere. Capping its two complementary sides by balls expresses
\[
M=M'\# N,
\]
where \(\partial M'=\partial M\) and \(N\) is closed. First homology splits as
\[
\mathbb Z\cong H_1(M';\mathbb Z)\oplus H_1(N;\mathbb Z).
\]
By (F.4), the first summand has positive rank. It follows that
\(H_1(M';\mathbb Z)\cong\mathbb Z\) and \(H_1(N;\mathbb Z)=0\).

Filling the boundary of \(M'\) leaves the closed summand in place, so
\[
M(\alpha)=M'(\alpha)\#N.
\tag{F.5}
\]
A lens space with finite first homology is irreducible and hence prime; see Hatcher, Proposition 1.6 and the lens-space example immediately after its proof, pp. 10–11. Thus either \(N\cong S^3\) or \(M'(\alpha)\cong S^3\). In the latter case, (F.5) identifies \(N\) with the lens space \(M(\alpha)\). Since \(H_1(N)=0\), that lens space is \(S^3\), and again \(N\cong S^3\). The side of \(S\) capped to obtain \(N\) is therefore a ball. Every embedded sphere in \(M\) bounds a ball, which proves irreducibility. \(\square\)

**Lemma F.2.** A compact connected orientable irreducible three-manifold with one torus boundary component and a boundary-compressing disk is a solid torus.

**Proof.** Let \(D\) be a properly embedded disk with \(\partial D\) essential in \(T=\partial M\). An essential simple closed curve on a torus is nonseparating, so compression of \(T\) along \(D\) produces a sphere. More explicitly, a regular neighborhood of \(T\cup D\) is a compression body with outer boundary \(T\) and inner boundary a sphere \(S\); it is a solid torus with the interior of a ball removed. The sphere \(S\subset\operatorname{int}M\) bounds a ball by irreducibility. This ball is on the side disjoint from \(T\), because an embedded ball bounded by an interior sphere cannot contain points of \(\partial M\). Gluing it to the compression body fills its spherical boundary and gives all of \(M\). The result is a solid torus. \(\square\)

## 3. The algebraic consequence of Floer simplicity

**Lemma F.3.** Suppose that \(M\) is an integral homology solid torus with at least two distinct L-space filling slopes. Let \(K\subset Y=M(\mu)\) be a filling core as above, and normalize \(\Delta_K\) by (F.2). Then either \(\Delta_K=1\) or \(\Delta_K''(1)>0\). If \(\Delta_K''(1)=0\), then \(\partial M\) is compressible. If additionally \(M\) is irreducible, then \(M\) is a solid torus.

**Proof.** The two L-space slopes make \(M\) Floer simple by RR Proposition 1.3. Choose a positive generator \(t\) of \(H_1(M)\). RR's normalized torsion then has the form
\[
\tau(M)=\sum_{n\ge0}a_nt^n,\qquad
a_0=1,\qquad a_n\in\{0,1\},\qquad a_n=1\text{ for }n\gg0.
\tag{F.6}
\]
Here the support normalization is from the paragraph before RR Proposition 1.4 and Section 2.1, the binary coefficients are from Proposition 1.4, and eventual constancy is also a consequence of Proposition 2.2. We do not assume that the particular filling core \(K\subset Y\) is Floer simple or that \(Y\) is an L-space.

Put \(D(t)=(1-t)\tau(M)\) and set \(a_{-1}=0\). Equation (F.6) implies
\[
D(t)=\sum_{n\ge0}(a_n-a_{n-1})t^n\in\mathbb Z[t].
\tag{F.7}
\]
It is a polynomial because \(a_n-a_{n-1}=0\) for all sufficiently large \(n\). Its constant coefficient is \(1\). Its nonzero coefficients alternate between \(+1\) and \(-1\): successive nonzero differences record successive changes of the binary sequence \((a_n)\), and a change from \(0\) to \(1\) must be followed, if there is another change, by a change from \(1\) to \(0\). Since the sequence begins at \(1\) and eventually remains \(1\), the first and last nonzero coefficients of \(D\) are both \(+1\). Moreover, telescoping (F.7) gives
\[
D(1)=1.
\tag{F.8}
\]

RR Section 2.1 identifies \(D\) with the Alexander polynomial of this exterior up to \(\pm t^a\); for the core in the integral homology sphere this is \(\Delta_K\). Equation (F.8) and \(\Delta_K(1)=1\) remove the sign ambiguity. Thus
\[
D(t)=t^h\Delta_K(t).
\tag{F.9}
\]
If \(d=\deg D\), its nonzero endpoint terms and the symmetry in (F.2) give \(d=2h\). In particular \(h\) is a nonnegative integer. This argument identifies an exponent shift; it makes no assertion about the Seifert genus.

There are an odd number of nonzero coefficients in \(D\), since they alternate and begin and end positively. After the shift (F.9), noncentral terms occur in symmetric pairs. Therefore the central coefficient of \(\Delta_K\) is nonzero. List its positive exponents as
\(0<n_1<\cdots<n_k\). The alternating signs, starting with a positive coefficient at the largest exponent, give
\[
\Delta_K(t)=(-1)^k+
\sum_{j=1}^k(-1)^{k-j}\bigl(t^{n_j}+t^{-n_j}\bigr).
\tag{F.10}
\]
For each \(n>0\),
\[
\left.\frac{d^2}{dt^2}(t^n+t^{-n})\right|_{t=1}
=n(n-1)+n(n+1)=2n^2.
\]
Consequently
\[
\frac12\Delta_K''(1)=\sum_{j=1}^k(-1)^{k-j}n_j^2.
\tag{F.11}
\]
If \(k=2r>0\), the right-hand side is
\[
\sum_{j=1}^r\bigl(n_{2j}^2-n_{2j-1}^2\bigr)>0.
\]
If \(k=2r+1>0\), it is
\[
n_1^2+\sum_{j=1}^r\bigl(n_{2j+1}^2-n_{2j}^2\bigr)>0.
\]
Thus \(\Delta_K''(1)=0\) implies \(k=0\), so \(\Delta_K=1\). Since \(D=t^h\) then has nonzero constant term, \(h=0\) and \(D=1\). This is the alternating-coefficient positivity mechanism also used in the proof of [Gainullin, Theorem 8.2](https://msp.org/agt/2018/18-1/agt-v18-n1-p03-p.pdf), pp. 104–105.

We next identify the exact polynomial in RR's norm formula. Because \(H_1(M)=\mathbb Z\) has no torsion, the projection defining \(\Phi\) is the identity. Hence
\[
\bar\Delta(M)=(1-t)\Phi(\tau(M))=(1-t)\tau(M)=D(t)=1.
\tag{F.12}
\]
Suppose that \(\partial M\) were incompressible. The manifold is Floer simple, so RR Corollary 2.3 and (F.12) would give
\[
\|M\|=\deg\bar\Delta(M)-1=-1.
\]
This is impossible: the Thurston norm is defined by minimizing sums of nonnegative quantities \(\max\{0,-\chi(F_i)\}\). Thus \(\partial M\) admits a compressing disk. If \(M\) is irreducible, Lemma F.2 completes the proof. \(\square\)

## 4. Insertion after the signed-filling identification

At this point of the framed proof, the common oriented peripheral basis has already been established. Thus the two nonlongitudinal probe slopes can be written
\[
\alpha_i=p_i\mu+q_i\lambda,\qquad p_i\ne0,
\qquad \frac{q_1}{p_1}\ne\frac{q_2}{p_2},
\]
and the actual closure isotopies give orientation-preserving homeomorphisms
\[
Y_{p_i/q_i}(K)\cong S^3_{p_i/q_i}(U)=L(p_i,q_i).
\tag{F.13}
\]
The symbol \(L(p,q)\) here denotes the oriented manifold obtained by \(p/q\)-surgery on the unknot, fixing the surgery convention once on both sides. No identification of the two filling cores by the homeomorphisms in (F.13) is required.

The Casson–Walker surgery formula, in the normalization of Ni–Wu Proposition 3.1, equation (7), is
\[
\lambda_{\mathrm{CW}}\bigl(Y_{p/q}(K)\bigr)
=\lambda_{\mathrm{CW}}(Y)+\lambda_{\mathrm{CW}}\bigl(L(p,q)\bigr)
+\frac{q}{2p}\Delta_K''(1).
\tag{F.14}
\]
It applies because \(Y\) is an integral homology sphere, so \(K\) is null-homologous; the proposition allows any rational homology sphere ambient manifold. Substituting (F.13) cancels the lens-space terms separately for the two values of \(i\):
\[
0=\lambda_{\mathrm{CW}}(Y)+\frac{q_i}{2p_i}\Delta_K''(1).
\]
Subtracting these equations, and using the distinct ratios, gives
\(\Delta_K''(1)=0\). Both fillings in (F.13) are L-spaces and their slopes are distinct. Lemma F.3 therefore makes \(\partial M\) compressible. Lemma F.1 has already established irreducibility from either actual lens-space filling. Lemma F.2 now yields \(M\cong S^1\times D^2\).

This comparison is related to Gainullin's proof of Theorem 8.2. The second slope here eliminates the unknown \(\lambda_{\mathrm{CW}}(Y)\); Floer simplicity of the exterior supplies (F.6), without assuming that \(Y\) itself is an L-space. Neither \(\lambda_{\mathrm{CW}}(Y)=0\) nor \(\Delta_K=1\) alone is used to identify \(Y\) or \(M\).

## 5. The longitude case

**Lemma F.4.** Let \(M\) be an irreducible integral homology solid torus with homological longitude \(\lambda\). Suppose that
\[
M(\lambda)\cong S^1\times S^2
\]
and that \(M(\alpha)\) is an L-space for some slope \(\alpha\). Then \(M\) is a solid torus.

**Proof.** Let \(L\) be the core of the solid torus attached in the \(\lambda\)-filling. Its exterior in \(S^1\times S^2\) is precisely \(M\). Filling this exterior along \(\alpha\) is a Dehn surgery on \(L\) with L-space result \(M(\alpha)\). We apply RR Proposition 7.8 to this knot with \(Z=S^3\), so that
\(Z\#(S^1\times S^2)\cong S^1\times S^2\). It follows that \(M\) is a generalized solid torus.

We compute the numerical parameter in that conclusion. In the Section 7 notation of RR, let
\[
T=\operatorname{Tor}H_1(M;\mathbb Z),\qquad
k_M=\left|T/(T\cap\operatorname{im}\iota)\right|.
\]
Here \(T\) is the trivial group, so \(|T|=k_M=1\). The relation
\(|T|=k_Mg_M\) from the same preamble gives \(g_M=1\). Equivalently, \(\iota(\lambda)=0\), and the order of the zero element is \(1\). This \(g_M\) is a homological parameter, unrelated to the exponent shift \(h\) in (F.9).

By Definition 7.2, the generalized-solid-torus conclusion gives both Floer simplicity and
\[
\deg\bar\Delta(M)<g_M=1.
\tag{F.15}
\]
The polynomial \(\bar\Delta(M)\) is nonzero. Indeed, \(H_1(M)=\mathbb Z\) makes it the normalized polynomial \((1-t)\tau(M)\), whose value at \(1\) is \(1\) by the same eventual-coefficient argument as (F.8). Its breadth is therefore a nonnegative integer. Equation (F.15) implies \(\deg\bar\Delta(M)=0\).

If \(\partial M\) were incompressible, RR Corollary 2.3 would give
\[
\|M\|=\deg\bar\Delta(M)-1=-1,
\]
contradicting nonnegativity of the Thurston norm. Hence \(\partial M\) compresses. The assumed irreducibility and Lemma F.2 show that \(M\) is a solid torus. \(\square\)

In the framed theorem, the actual shared closure link at \(\lambda\) is the two-component unlink, which supplies \(M(\lambda)=S^1\times S^2\). The other original slope is nonlongitudinal and gives an actual lens-space filling, so it supplies the L-space in Lemma F.4. Irreducibility is already supplied by Lemma F.1. The hypotheses of Lemma F.4 are consequently all verified. No distance-one restriction is imposed on \(\alpha\): Proposition 7.8 includes its general rational-surgery case. The proof does not assert that an arbitrary generalized solid torus is an actual solid torus.

## 6. Citation and integration notes

1. **Source scope.** The proof text above gives the missing algebra and topology, rather than treating the earlier audit's verdict as mathematical evidence. RR Proposition 7.8 and its proof were re-read, including its rational-to-integral-surgery reduction. The manuscript should invoke the published result; it need not reproduce its Floer-theoretic proof. Ni–Vafaee Theorem 1.1 is a valid alternative route, but relies on RR 7.8 and 7.12 and is not an independent proof of that input. It is omitted from the insertion text.

2. **Exact normalization.** Credit the support normalization to the paragraph preceding RR Proposition 1.4 and Section 2.1, not solely to Proposition 1.4. Credit eventual coefficients to that paragraph or Proposition 2.2. The sign in \(D=t^h\Delta_K\) follows from \(D(1)=\Delta_K(1)=1\), and \(\deg D=2h\) follows from symmetry and the constant coefficient. These details implement RF9 of the later audit.

3. **Irreducibility.** Lemma F.1 explicitly handles the case in which the boundary summand fills to \(S^3\), so the closed summand could initially appear to account for the lens space. Its trivial homology then forces that lens space to be \(S^3\). The argument uses primeness of lens spaces, not the assertion that every homology sphere is \(S^3\). Hatcher's directly inspected statements provide precise optional references: Proposition 1.4, pp. 6–7; Proposition 1.6 and its lens-space example, pp. 10–11. Lemma F.2 includes the compression-body proof, so a separate citation for that elementary step is unnecessary.

4. **Generality.** Without irreducibility, the norm contradiction supplies boundary compression but not a solid torus. The previously audited example \((S^1\times D^2)\#\Sigma\), with \(\Sigma\) a nontrivial integral homology L-space sphere, explains the distinction. Its actual nonlongitudinal fillings retain \(\Sigma\); no such filling is a lens space. The previously audited RR examples with \(H_1=\mathbb Z\oplus\mathbb Z/g\), \(g>1\), are excluded by the integral homology assumption. These are checks on hypotheses, not a new classification assertion.

5. **Original versus restated surgery formula.** Ni–Wu Proposition 3.1 was directly read in the earlier primary-source audit and states precisely (F.14). It credits Boyer–Lines Theorem 2.8. The original Boyer–Lines text was not directly verified in this subtask; therefore write “the Boyer–Lines surgery formula, in the form stated by Ni–Wu, Proposition 3.1,” rather than claiming an independent check of the original theorem. The direct Ni–Wu citation URL is [the author's published copy](https://archive.ymsc.tsinghua.edu.cn/pacm_download/301/8839-Cosmetic.pdf), printed p. 9.

6. **Published numbering.** The journal bibliographic data were checked on the publisher's indexed record, but its full text was inaccessible during this review. Pinning the theorem numbers to arXiv v2 removes the resulting ambiguity. Do not label these as independently checked journal theorem numbers.

7. **No extra claim from RR.** The statement that \(\bar\Delta=D\) uses torsion-free \(H_1\), and the conclusion “solid torus” uses irreducibility. Preserve both hypotheses in every extracted lemma. The auxiliary integral homology sphere \(Y\) is not assumed to be \(S^3\) or an L-space. The existence of two L-space **slopes**, not two different homeomorphism types of L-space fillings, is what Proposition 1.3 requires.

8. **Placement.** Lemmas F.1–F.2 fit the peripheral-data preliminary step. Lemma F.3 can be a preliminary lemma or expanded inside Step 3; retain (F.10)–(F.11) in the main proof to match the requested presentation. Section 4 starts only after the common signed coefficient identification has been proved. Lemma F.4 is Step 4. The final passage to marked balanced framed tangles remains the responsibility of the tangle section and is not replaced by any assertion about arbitrary solid-torus involutions here.
