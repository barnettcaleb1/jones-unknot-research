# Scope of the finite-information barrier

Audit of Claude 20261103-104249, design round only. No computation. Conclusion: a useful fixed-truncation barrier exists, but G1 literally stated is false and G2 is not an exhaustive classification of possible proofs.

## 1. Quantifiers are essential

For each fixed positive integer r, Eliahou–Fromentin construct a nontrivial knot K_r with V(K_r)=1 coefficientwise modulo 2^r. Their displayed diagram has 20*2^(r-1)+1 crossings; this should not be silently advertised as a proved minimal crossing number. This rules out detection using only the reduction modulo one fixed power of two, or any finite list of such reductions (take the largest r). It does not rule out the entire compatible 2-adic polynomial: an integer divisible by every 2^r is zero. It also does not rule out arguments combining a congruence with extra geometric information. [Eliahou–Fromentin, abstract and theorem](https://arxiv.org/pdf/1610.05560).

The same warning applies to finite-type order: each fixed cutoff fails, including on prime knots. Stanford constructs infinite prime families matching prescribed invariants through a fixed order; Kalfagianni additionally constructs hyperbolic examples with trivial Alexander polynomial and bounded-order finite-type data, with arbitrarily large volume. [Stanford 1996](https://msp.org/pjm/1996/174-1/pjm-v174-n1-p08-s.pdf), [Kalfagianni 2004 abstract](https://ftp.gwdg.de/pub/EMIS/journals/UW/agt/AGTVol4/agt-4-48.abs.html).

This is not a prohibition on an adaptive finite procedure whose cutoff depends on the input diagram. A Laurent polynomial with a known support bound is determined by finitely many evaluations or a sufficiently long Taylor jet; the required number grows with the bound. The distinction is a fixed global truncation versus a family of truncations with no uniform cap.

## 2. “Finitely many evaluations” is false without specifying the points

One exact evaluation at any fixed nonzero transcendental complex number z is injective on Z[q,q^-1]. Indeed, if P(z)=0, multiply P by a power of q; a nonzero integral polynomial cannot have a transcendental root. Thus V_K(z)=1 is exactly equivalent to V_K=1. This is an elementary algebraic fact, not a detection theorem or a numerically effective method.

For finitely many algebraic points, evaluation has a nontrivial kernel on the ambient Laurent polynomial ring (a product of their minimal polynomials suffices). That alone does NOT imply that the unknot's fiber contains the Jones polynomial of a nontrivial knot. One must realize the kernel relation topologically. Counting the dimension of the ambient polynomial space cannot replace that step.

For roots of unity there is a substantial published obstruction beyond the classical evaluations: Kalfagianni's Theorem 1.2 constructs, for any finite list of integers r_i>2, a knot matching ALL unreduced colored Jones values of the unknot at t_i=exp(2*pi*i/r_i), for every common framing. Lemma 2.4(e) ensures the constructed knot is nontrivial even for small positive surgery orders; sufficiently large r_i give hyperbolicity and a volume bound. [Kalfagianni 0710.0076, Theorem 1.2 and Lemma 2.4(e)](https://arxiv.org/pdf/0710.0076).

**Normalization caution:** her printed convention is J_N(U,t)=(t^N-t^-N)/(t-t^-1). Thus the color-two quantum dimension is t+t^-1, which vanishes at t=+/-i (order FOUR in her parameter). At other allowed roots we may divide to obtain reduced color-two equality. Do not silently identify her parameter with ordinary Jones q or infer reduced equality by dividing zero. This read does not certify the blanket statement for every arbitrary finite list of ordinary-Jones roots including all degenerate normalization points. It certifies the theorem just stated and its nondegenerate reduced consequences.

## 3. The mod-p density result is not an odd-modulus unknot-fiber theorem

Aiello–Baader–Ferretti prove density at most 4/p^7 in a sufficiently large prescribed degree range, and record V(12n237)=t^12 modulo 2. Their restrictions use 1, i, third and sixth roots, together with the derivative at 1; -1 is not one of the fixed-value conditions in their displayed list. A sparse image does not establish any particular fiber has a nontrivial knot. Their questions at the end explicitly leave additional odd-prime realization issues open. [Aiello–Baader–Ferretti, Theorems 1–2 and section 4](https://arxiv.org/pdf/2204.12259).

Recommended replacement for an overbroad board barrier: **Fixed 2-power reductions and uniformly bounded finite-type information cannot alone detect U. The cited results do not establish the same statement for every fixed integer modulus. Root evaluations require specified orders and normalization; arbitrary exact evaluations are not a finite-information barrier.**

## 4. Habiro H_1: correct formula, no extra data

Use the symmetric-kernel convention

    J_N(K;q) = sum_(k=0)^(N-1) H_k(K;q)
               product_(j=1)^k (q^N+q^-N-q^j-q^-j),
    H_0=1, J_2=V.

Then

    V-1 = H_1 (q^2+q^-2-q-q^-1)
        = H_1 q^-2 (q-1)^2(q^2+q+1).

Each H_k is an ordinary element of Z[q,q^-1]. Habiro's completion is needed for certain infinite sums, not to strengthen the individual Laurent-polynomial condition on H_1. His universal central expansion gives an independent definition of the coefficients (Theorem 2.1); Theorems 3.1–3.2 identify their colored-Jones evaluations. This is already a quantum-group description, though not a positive count. [Habiro, 2002, Theorems 2.1, 3.1, 3.2](https://arxiv.org/pdf/math/0211044).

With the usual Conway normalization and V''(1)=-6a_2, expansion of the factor gives 3(q-1)^2+O((q-1)^3), so H_1(1)=-a_2. Trefoil H_1=-q^2 and figure-eight H_1=1 in one handedness convention agree with Habiro's examples. Alternative Pochhammer kernels change the coefficient by a sign and monomial; fix the convention before comparing claims.

Thus H_1=0 iff V=1 is correct. It is a useful normalization, not a mechanism for nonvanishing. The completed central invariant contains higher H_k not determined by H_1; a proposed relation forcing those higher coefficients from H_1 would be a new substantive theorem.

## Recommended working rule

Demand a mechanism that is not demonstrably lost under the specific truncation used. Do not require every proof to be categorized as extreme terms, categorification, or Habiro integrality: mixed geometric/arithmetic arguments, adaptive information, and exact evaluations could encode global Jones information in other forms. FROB5 remains an exclusion sieve in its present form, but the fixed-modulus obstruction does not prove a theorem that it could never occur as a useful lemma in a larger proof.
