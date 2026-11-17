# Geometric braid order versus full-twist TL sectors

2026-11-03. Bounded theory pass; no computation or search. This does not address the literature on Dehornoy order, assigned separately. No novelty claim.

## Exact central-block formula

Use sigma_i=A I+A^-1 e_i and delta=-A^2-A^-2. Write W(n,r) for the TL simple module with r through strands, r=n,n-2,..., and

    Delta_r=(-1)^r (A^(2r+2)-A^(-2r-2))/(A^2-A^-2).

The full twist acts on W(n,r) by the scalar

    lambda_r=A^(r(r+2)-3n).

This follows from the ribbon twist ratio theta_r/theta_1^n, with theta_r=(-1)^r A^(r(r+2)); the signs cancel because r and n have the same parity. It agrees with the TL_2 eigenvalues A^2 and A^-6.

For beta=Delta_n^(2k) gamma, with e(gamma) its exponent sum, the normalized Jones polynomial of a knot closure is

    V_beta(A^-4)
      = (-A^3)^(-e(gamma))/delta
        * sum_r Delta_r A^(k[r(r+2)-3n^2]) tr_W(n,r)(gamma).

The adjacent central exponents are separated by 4(r+2)k. But the degrees of the remainder traces are not controlled merely by keeping gamma's fractional Dehn twist coefficient in a bounded interval. In particular, separating the central eigenvalues does not itself separate the supports of the summands.

## Why a bounded-order remainder has unbounded trace spread

For n>=3, gamma=sigma_1^(-m) is supported in a proper punctured subdisk, so its boundary FDTC is zero. Nevertheless

    tr_W(n,n)(gamma)=A^-m,
    tr_W(n,n-2)(gamma)=(n-2)A^-m+(-A^3)^m.

The second formula follows because e_1 has rank one on W(n,n-2), so sigma_1 has eigenvalues A with multiplicity n-2 and -A^-3 with multiplicity one. Its trace spread grows like 4m while FDTC stays zero. This already rules out a uniform remainder-degree bound depending only on n and FDTC.

The same issue occurs for actual **knot** closures, not only multi-component closures. Here is an explicit family in which the top two central-sector leading terms cancel at arbitrarily large positive FDTC.

Fix n>=3 and let

    tau=sigma_2 ... sigma_(n-1),
    gamma_m=sigma_1^(-m) tau,
    beta_(k,m)=Delta_n^(2k) gamma_m.

For odd m, gamma_m has an n-cycle permutation, so beta_(k,m) closes to a knot. Each factor sigma_1^(-m) and tau is supported on a proper punctured subdisk and has FDTC zero. The bounded-defect property of FDTC therefore bounds FDTC(gamma_m) independently of m, and central additivity gives

    FDTC(beta_(k,m))=k+O(1).

Only that standard bounded-defect property is used; no exact defect constant is needed.

Set P=e_1/delta on W(n,n-2). The TL relations give

    tr(P tau)=-A^n/delta.

Indeed cyclically insert e_1 twice in the trace. Terms of tau containing an e_j with j>=3 vanish since e_j e_1=0 in this one-cup module. The remaining terms give

    tr(e_1 tau)=A^(n-2)delta+A^(n-4)=-A^n.

Consequently

    tr(gamma_m)=A^-m tr(tau)
      + [(-A^3)^m-A^-m](-A^n/delta).

This expression is polynomial: the apparent denominator cancels in the full expression. For large positive m its highest term is

    (-1)^m A^(3m+n-2).

The top module has trace A^(-m+n-2). Before the common Jones normalization, the leading degrees of the top two central summands are therefore

    r=n:   k n(n-1)-m+3n-2,
    r=n-2: k(n^2-5n)+3m+3n-6.

They coincide at m=nk+1. Choose k so nk is even; then m is odd, the closure is a knot, and their leading coefficients are opposite. At fixed n and sufficiently large k these are also the two maximal sector degrees: lower r have a smaller central exponent by at least 4(n-2)k, while their remainder degree is at most 3m+O(n). Thus the top degree cancels in the actual closed-braid bracket at arbitrarily large positive FDTC.

The three-strand case alone is sufficient and avoids any discussion of other sectors. For even k>=2 take

    beta_k=Delta_3^(2k) sigma_1^(-(3k+1)) sigma_2.

Its closure is a knot, its FDTC is k+O(1), and W(3,3), W(3,1) are the only TL sectors. Their leading closure terms are respectively -A^(3k+6) and +A^(3k+6), so the global leading degree cancels. These are exact symbolic formulas, not sample computations.

This is **not** a family with V=1. It refutes only the proposed elementary lemma that large positive central order forces the top TL sector to contribute an uncancelled extreme term. Any successful degree/order inequality must survive this cancellation.

## What positivity really provides

For a positive n-braid word with exponent sum e whose closure is a knot, the all-oriented smoothing consists of n circles and is adequate. Hence

    min_degree_t V=(e-n+1)/2.

Thus V=1 forces e=n-1; connectedness then forces each adjacent braid generator to occur exactly once, and the closure is the unknot. In particular, for n>=3 a positive braid containing the positive Garside half twist cannot be Jones-unit: its exponent sum is already larger than n-1.

This gives a restriction on positive/Garside representatives, not a bound on FDTC or Dehornoy floor. An FDTC-bounded remainder need not be positive, short, or have bounded TL degree; the preceding family supplies the explicit obstruction.

## Missing first lemma

A genuine order-to-Jones argument needs either a topological restriction on the remainder stronger than its geometric order, or an aggregate trace inequality that controls cancellations across sectors despite unbounded remainder degrees. The elementary full-twist formula supplies neither. A degree-separation argument with a fixed remainder or a bound on its negative-word complexity does not give a bound in terms of geometric order alone.

No counterexample to a Jones-unit FDTC bound is claimed. Such a counterexample would already require nontrivial Jones-unit knots. The conclusion here is narrower: the most immediate positive-central-sector proof mechanism fails even for one-component classical braid closures.
