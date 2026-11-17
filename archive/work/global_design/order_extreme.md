# Braid order, boundary twisting, and Jones extremes

Bounded primary-source/theory pass, 2026-11-03. No computations. Conclusion: Artin/Garside positivity gives a real surviving Jones extreme; Dehornoy positivity alone gives no restriction on knot type, and arbitrarily high FDTC does not force Artin positivity or quasipositivity. A general bound on FDTC from the ordinary Jones polynomial was not established or located in this pass.

## 1. The actual positive mechanism

For a positive n-braid beta closing to a knot, in the convention where the positive trefoil has V=t+t^3-t^4,

    min deg V_(closure beta) = (e(beta)-n+1)/2 = g(closure beta).

The minimal coefficient is 1. Here e is the braid exponent sum. Thus a nontrivial positive-braid knot cannot have V=1. This is the genuine extreme-term result, not a consequence of left-orderability. See [Stoimenow, Section 8, equations (19) and (22), and Lemma 8.1](https://www.numdam.org/item/ASNSP_2003_5_2_2_237_0.pdf).

There is an immediate, scoped Garside consequence. Write a fixed braid beta in classical left normal form Delta^p a with a positive. Then

    Delta^(2m) beta is positive whenever 2m+p >= 0.

Full twists preserve the permutation, so if beta closes to a knot, so does every member of this family. If also

    m n(n-1)+e(beta) > n-1,

its minimal Jones degree is positive. Consequently sufficiently many positive full twists on a *fixed* knot braid rule out V=1, with an explicit threshold depending on its Garside infimum and exponent sum.

This is not a uniform FDTC theorem: the required threshold depends on the braid left after the full twists have been extracted.

## 2. Dehornoy-positive representatives occur for every knot

Let beta be any braid representative of any knot K. Shift every generator index upward by one and form

    beta_plus = sigma_1 · shift(beta).

This is a positive Markov stabilization at the new first strand, so its closure is K. Its displayed word contains sigma_1 positively, no sigma_1^{-1}, and no smaller-index generator. Therefore it is Dehornoy-positive. Similarly sigma_1^{-1} shift(beta) is Dehornoy-negative and has the same knot closure.

Hence the mere sign of a braid in the Dehornoy order cannot force any Jones extreme, polynomial inequality, or knot-type exclusion that does not hold for all knots. Dehornoy positivity must not be substituted for membership in the positive Artin monoid. The order criterion and FDTC setup are recalled in [Feller, Section 3](https://arxiv.org/pdf/2204.05288).

## 3. High FDTC does not turn the braid positive

The distinction persists arbitrarily far out in boundary twisting, even for actual knot closures.

Fix n>=3, let delta=sigma_1...sigma_(n-1), and normalize FDTC omega by omega(Delta^2)=1. For m>=1 define

    beta_m = Delta^(2m) sigma_1^(-2m n(n-1)) delta.           (1)

The full twist and the even power of sigma_1 are pure. Thus beta_m has the n-cycle permutation of delta and closes to a knot.

Its exponent sum is

    e(beta_m)=(n-1)-m n(n-1)<0.                            (2)

It is therefore not a positive braid and not a quasipositive braid, nor conjugate to one: a nonidentity product of conjugates of positive Artin generators has strictly positive exponent sum.

On the other hand, omega vanishes on the standard (n-1)-strand subgroup, omega(delta)=1/n, and omega is a homogeneous quasimorphism of defect at most 1. It is additive on commuting elements; in particular a central full twist adds exactly one. Consequently

    omega(beta_m)
      =m+omega(sigma_1^(-2m n(n-1)) delta)
      >=m+1/n-1 -> infinity.                              (3)

The needed FDTC properties are in [Feller, Theorem 1 and Section 3](https://arxiv.org/pdf/2204.05288).

This elementary family rules out the proposed bridge “sufficiently large positive FDTC forces the positive-braid Jones extreme by making the braid positive.” It makes no assertion that the knots in (1) have equal Jones polynomials, or that those knot types admit no other quasipositive representatives. The obstruction concerns the specified braid and its conjugacy class.

## 4. What published quantitative bounds actually control

[Feller's Theorem 3](https://arxiv.org/pdf/2204.05288) gives, for a knot closure,

    |omega(beta)| <= 2 g_4(closure beta)+n-1.

[Feller–Hubbard, Theorem 1.1](https://arxiv.org/pdf/1708.04998) shows that an n-braid whose closure also admits an (n-1)-braid representative has |omega(beta)|<=n-1. Thus high FDTC certifies minimal braid index. Neither theorem turns V=1 into the required genus or braid-index information.

Terminology warning: the “generalized Jones conjecture” used in the latter proof is the theorem controlling writhe among braid representatives of the same link. It is not the assertion that the Jones polynomial detects the unknot.

There is also a recent categorical direction. [Binns–Hubbard, August 2026 preprint, Theorem 1.2](https://arxiv.org/pdf/2608.06201) gives FDTC lower bounds for the rank of the next-to-extreme annular Khovanov grading, for both odd and even braid index. This is explicitly a rank result proved through Floer-theoretic input. It does not give a nonzero Jones Euler coefficient, and this pass does not independently audit that new preprint.

## 5. The precise open gate

A statement of the form

    V_(closure beta)=1 => |omega(beta)| <= C(n)

would be genuinely new input relative to the results checked here. It cannot be obtained merely by replacing positive braid words with Dehornoy-positive words, by bounding FDTC using exponent sum, or by taking Euler characteristics of a rank lower bound.

I did not locate an established ordinary-Jones FDTC bound, nor a family with fixed ordinary Jones polynomial and unbounded FDTC. The examples in Section 3 prove only the stated positivity obstruction. Therefore I do not mark the proposed Jones-to-FDTC implication false; it remains an unsupported mechanism requiring a new relation between the scalar Markov trace and boundary twisting.

The useful result to retain is the distinction between two claims: full twists of a fixed braid eventually enter the positive monoid and expose a Jones extreme, whereas large boundary twisting in a varying braid need not approach that monoid at all.
