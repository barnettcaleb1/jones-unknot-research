# The braid-order gate for a Jones-triviality bound

2026-11-03. Bounded theory/literature pass; no computation. This records an implication of existing theorems, not a novelty claim or a proof of unknot detection.

## Conclusion

For each fixed braid width n >= 3, **any finite upper bound on the FDTC of every n-braid whose knot closure has Jones polynomial 1 would imply faithfulness of the generic Temperley–Lieb/Jones braid representation at that width**. The bound need not be uniform in n. Thus a Jones-to-order inequality would have real force, but it already has to overcome quantum-representation faithfulness. The primary papers checked here neither prove nor refute such a Jones-only bound.

Faithfulness is only a necessary consequence: a faithful representation can have a large trace fiber. No converse is claimed.

## 1. Exact input and conventions

[Ito, *A kernel of a braid group representation yields a knot with trivial knot polynomials*, arXiv:1402.2028](https://arxiv.org/html/1402.2028), supplies the following:

- Theorem 3: every nontrivial normal subgroup of B_n is unbounded in the Dehornoy order. A noncentral one has arbitrarily large pseudo-Anosov elements.
- Theorem 1 and its proof: given such a subgroup H and an unknot braid alpha, one can find pure h in H with alpha h >_D Delta^(2N), whose closure is hyperbolic, has genus at least N, and has braid index n, with N arbitrarily large. The displayed “beta in K” in the theorem statement is a typographical slip for H.
- Theorem 2(1): beta >_D Delta^(2N) for a knot closure implies genus at least N. The other two parts supply the braid-index and hyperbolicity conclusions once the order and pseudo-Anosov thresholds are met.
- Corollary 1 states the corresponding same-quantum-invariant hyperbolic-knot construction. Its conclusion concerns fixed invariant values, not just bounded degree or finite-type approximation.

Use the **signed** central floor f_D, defined by

    Delta^(2 f_D(beta)) <=_D beta <_D Delta^(2(f_D(beta)+1)).

This is not the nonnegative, symmetric version of “Dehornoy floor.” The FDTC omega is normalized by omega(Delta^2)=1 and is the homogenization of f_D. In particular

    f_D(beta) <= omega(beta) <= f_D(beta)+1.

For the conventions and homogenization see [Feller–Hubbard, introduction and Proposition 2.1](https://arxiv.org/pdf/1708.04998). The inequality also follows directly: centrality and left invariance let one raise the two order bounds to the kth power, then divide by k and take the limit.

## 2. The conditional theorem

Work over Q(A), with delta=-A^2-A^(-2), bracket representation

    rho(sigma_i)=A*1+A^(-1)*e_i,
    R(beta)=(-A^3)^(-w(beta))*rho(beta).

The writhe-corrected R is a representation. Its normalized closure trace gives the ordinary oriented Jones polynomial. On the one-dimensional top cell module W(n,n),

    R(beta) = (-1)^w A^(-2w).

Consequently every element of H=ker R has writhe zero. No nonzero central power Delta^(2k) belongs to H, since its writhe is kn(n-1). For n>=3, a nontrivial H is therefore noncentral. In these conventions ker R=ker rho: the top character also forces w=0 on ker rho.

**Proposition.** If H is nontrivial, then for every real C there is an n-braid gamma such that

    V_closure(gamma)=1,     omega(gamma)>C,

whose closure is a hyperbolic knot of braid index exactly n. Its genus can simultaneously be made arbitrarily large.

**Proof.** Fix alpha=sigma_1 ... sigma_(n-1), whose closure is the unknot. Apply Ito's construction with an order threshold N>C and sufficiently large for the additional topology conclusions. It supplies pure h_N in H with gamma=alpha h_N >_D Delta^(2N). Since R(gamma)=R(alpha), their normalized Jones traces agree exactly. Purity ensures the closure remains a knot. The floor/FDTC inequality gives omega(gamma)>=N. The topology conclusions come from Ito's theorem. QED.

**Corollary.** If a finite C_n satisfies

    V_closure(beta)=1 and closure(beta) a knot
        ==> omega(beta)<=C_n

for every beta in B_n, then R is faithful. The same conclusion follows from a bound on f_D or on its symmetric version. A bound restricted to *all braid-index-minimal representatives* also suffices, because Ito's output has braid index n.

The quantifier is important. A claim that each Jones-trivial knot merely *admits some* low-FDTC representative does not supply the bound needed here; it does not control the particular high-FDTC representatives in the construction. The same caveat applies to the existence of one low-FDTC minimal representative.

## 3. Existing geometric inequalities do not supply the missing direction

Actual unknot closures are order-bounded. Ito's genus implication, applied to beta and beta^(-1), excludes beta>Delta^2 and beta<Delta^(-2). Equality is also impossible for an n>1 knot closure, since Delta^(+/-2) is pure and its closure has n components. Thus an unknot n-braid lies strictly between Delta^(-2) and Delta^2, and has |omega(beta)|<=1.

So unknot detection would indeed imply a uniform FDTC bound of 1 on the Jones-unit fiber. The unproved part is replacing the geometric unknot hypothesis by the single Jones equality. Merely asking for some finite C_n weakens the proposed bound but still entails the faithfulness consequence above.

There is also a genuine smooth four-dimensional constraint:

    |omega(beta)| <= 2 g_4(closure(beta)) + n - 1

for knot closures, by [Feller, *The slice-Bennequin inequality for the fractional Dehn twist coefficient*, Theorem 3](https://arxiv.org/html/2204.05288v2). Together with the proposition, a hypothetical generic Jones kernel would give Jones-trivial hyperbolic knots of unbounded smooth slice genus at fixed braid index. This is a conditional deduction, not evidence that such a kernel exists.

Neither a genus lower bound from order nor the displayed slice-genus inequality is a Jones-only upper bound. Reversing their direction would be the missing argument. The stronger auxiliary assertion “every Jones-trivial knot is slice” would already force faithfulness by taking C_n=n-1, but it is not established here.

## 4. Why D-POWER does not conflict

The finite-exception result in [power_moments.md](power_moments.md) concerns closures of gamma^k for one fixed gamma in B_n, n>1. Ito instead produces alpha h_N, with alpha fixed and h_N varying in the kernel. Even where a subfamily can be written alpha h^k, it is an **inserted-power** family, not (alpha h)^k.

Indeed R(alpha h^k)=R(alpha) for a kernel element h. Its closure trace is allowed to remain the unknot value forever. The powers h^k themselves have the representation of the identity braid; when h is pure their closures are n-component links and have Jones value delta^(n-1), not 1.

In spectral terms, bare power traces have coefficients given by algebraic multiplicities in each TL block. Inserted-power traces Tr(R(alpha) R(h)^k) have coefficients contributed by R(alpha), with cancellations already present in the fixed unknot braid. The noncancellation argument for bare powers therefore does not apply.

## Assessment

Braid order turns an assumed quantum kernel into severe geometric complexity while preserving the ordinary Jones polynomial. This identifies a precise obstacle to an order-based proof, rather than providing the missing Jones-to-order estimate. Any proposal should state a new inequality on the Jones-unit fiber and a reason it can hold independently of the desired faithfulness conclusion. No such mechanism was found in this pass.
