# Deleting the first Habiro coefficient: surviving constraints and exact gaps

Date: 2026-11-03. Bounded theory pass, no computations. This is an operation on a sequence of polynomials, not surgery on a knot.

Use reduced, zero-framed colored Jones normalization J_1=1 and J_2=V, and the cyclotomic basis

    C_(N,k)(q) = product_(j=1)^k (q^N+q^(-N)−q^j−q^(-j)).
    J_N(K;q) = sum_(k>=0) H_k(K;q) C_(N,k)(q),   H_0=1.

The sum terminates at k=N−1 for each positive integer N. Set H=H_1=(J_2−1)/C_(2,1) and define

    F_N(q) = J_N(K;q) − H(q)(q^N+q^(-N)−q−q^(-1)).       (1)

Then F_1=F_2=1, its first cyclotomic coefficient is zero, and all H_k for k≥2 are unchanged. Thus Habiro integrality survives. Nontriviality of the resulting sequence requires some H_k, k≥2, to be nonzero; it must not be inferred merely from J_2(K)≠1.

## 1. A necessary correction to the proposed pilot

Assume a_2(K)=0, equivalently H(1)=0 in these conventions. The MMR diagonal of F equals that of K, as proved below. If F were the colored Jones sequence of an actual knot L, it would therefore force Δ_L=Δ_K. Since F_2=1 also forces det(L)=1, a necessary compatibility condition is

    |Δ_K(−1)|=1.

The pilot b(31,13) fails: its determinant is 31. Thus its deletion sequence is already impossible as a knot invariant, despite passing the formal recurrence and scalar-loop conditions. This is an explicit cross-constraint missed by checking those structures separately.

A safe seed for this particular determinant/Alexander check is an actual knot with Δ=1 and V≠1. The Kinoshita–Terasaka knot is such a seed. Its trivial Alexander polynomial is recorded in [Friedl–Kim](https://arxiv.org/abs/math/0505594). In [Eisermann–Lamm, Example 6.7 and Table 2](https://pnp.mathematik.uni-stuttgart.de/igt/eiserm/publications/symjones.pdf), its Jones polynomial is

    1+(q^2−1) f(q),
    f(q)=q^(-4)(q^2+1)(q−1)^2(q^2+q+1)(q^2−q+1) ≠ 0.

This supplies the seed conditions Δ=1, a_2=0, H≠0. No AJ theorem, exact colored-degree formula, or higher-Habiro nonvanishing calculation for this seed was established in this pass.

## 2. Scalar Rozansky rationality survives to all orders

Set q=e^h and treat z=q^N as independent. Write

    S(z,h) = H(e^h)(z+z^(-1)−2cosh(h))
           = sum_(ell>=0) s_ell(z) h^ell.

Every s_ell is a Laurent polynomial in z, of degree at most one. Because H(1)=0, s_0=0. If the loop expansion of the actual seed is

    J(z,h)=sum_(ell>=0) P_ell(z)/Δ(z)^(2ell+1) h^ell,

then

    F(z,h)=sum_(ell>=0)
      [P_ell(z)−s_ell(z)Δ(z)^(2ell+1)]/Δ(z)^(2ell+1) h^ell.       (2)

The zeroth term remains 1/Δ(z); all required scalar denominators remain of the permitted form. This is an all-order certificate, not a truncation. With q−1 as expansion variable, the subtraction likewise has integral Laurent coefficients. If Δ=1, every scalar loop coefficient remains Laurent polynomial.

The same elementary subtraction preserves the small-angle analytic expansion, uniformly on compact subsets of its domain: at q=e^(α/N), z=e^α, S=O(1/N). Higher terms follow from Taylor expansion. The seed statements used here are [Garoufalidis–Lê, Theorems 1–4](https://people.mpim-bonn.mpg.de/stavros/publications/analyticMMR.pdf).

This proves scalar rationality only. It does not construct a beaded-graph rational Kontsevich integral.

## 3. An explicit regular recurrence, beyond q-holonomic closure

Let M act on a sequence by multiplication by q^N and L by N→N+1, so LM=qML. Choose an annihilator

    P(q,M,L)=sum_j a_j(q,M)L^j,   P J=0,

with Laurent-polynomial coefficients, regular at q=1 and with P(1,M,L) not identically zero. Clearing denominators and dividing a common power of q−1 gives this normalization for a nonzero finite recurrence. Existence for the seed follows from [Garoufalidis–Lê](https://arxiv.org/abs/math/0309214).

Put s(q,M)=M+M^(-1)−q−q^(-1), and calculate formally

    R(q,M) = sum_j a_j(q,M) s(q,q^j M).
    P F = −H(q)R(q,M).

If R=0, the original P annihilates F. Otherwise write R=(q−1)^k R̃, with R̃(1,M) not identically zero. Then the explicit operator

    Q = [R̃(q,M)L − R̃(q,qM)] P                              (3)

annihilates F. Indeed the bracket annihilates H(q)(q−1)^k R̃(q,M). Moreover

    Q(1,M,L)=R̃(1,M)(L−1)P(1,M,L).                           (4)

Thus we can preserve an existing regular classical recurrence symbol up to an extra abelian L=1 factor and an M-only factor. This is stronger than merely saying that F is q-holonomic. If the old symbol already contains L−1, its reduced zero set is unchanged after discarding M-only factors.

**Scope.** Q need not be the minimal recurrence of F. Equations (3)–(4) do not prove that F satisfies AJ for the same knot exterior, that the minimal classical characteristic polynomial is unchanged, or that initial conditions are geometrically admissible. They only exhibit a regular annihilating operator with controlled specialization. An argument that uses merely existence of such a recurrence cannot distinguish this deletion from the original sequence.

**Subsequent strengthening in this pass.** The separate proof in `ore_correction.md` establishes more for the MINIMAL operators: after primitive q−1 normalization, their classical symbols have identical irreducible factors, with multiplicities, away from L−1. Their L−1 multiplicities differ by at most one. This needs no monic-regularity assumption and applies to deleting any fixed finite collection of Habiro coefficients. The geometric AJ interpretation, M-only polynomial factors, strong AJ peripheral ideals and actual-knot realization remain outside that theorem.

## 4. Degree asymptotics and boundary-slope data

Let u=deg_+ H and l=deg_- H. For large N, the correction in (1) is supported in

    [l−N, u+N].

Consequently, if the seed satisfies

    deg_+ J_N > u+N  and  deg_- J_N < l−N

for all sufficiently large N, then BOTH extreme degrees and BOTH extreme coefficients of F_N equal those of J_N for all such N. Positive quadratic growth at the top and negative quadratic growth at the bottom are sufficient; they are not assumed automatic for every seed.

Under this explicit growth hypothesis, the eventual degree quasi-polynomials, their periods, Jones slopes, and linear terms are all preserved. If the seed's slope or strong slope conjecture is known, the same surfaces in its exterior still witness those numerical slopes and Euler-characteristic ratios. This does **not** attach that exterior to a knot realizing F. It only shows the asymptotic numbers can remain compatible with genuine geometric boundary-slope data. The slope framework is [Garoufalidis, The Jones slopes of a knot](https://doi.org/10.4171/QT/13).

Without the strict inequalities, cancellation or takeover at a linear endpoint is possible; no universal degree-preservation claim is justified. Likewise a class-specific all-color formula, such as one certified by an adequate diagram, is stronger than eventual degree data and is not preserved just because asymptotics are.

At the Kashaev specialization q_N=e^(2πi/N), the correction is

    H(q_N)(2−q_N−q_N^(-1)) = O(N^(-3))

when H(1)=0. Hence any positive exponential growth rate of the seed's Kashaev values is unchanged. This is an elementary conditional asymptotic statement, not a proof of the volume conjecture for an unchecked seed.

## 5. Completed group-like lift and the remaining gates

At fixed N, every positive h-degree coefficient of F(e^h), and hence of log F(e^h), is an even polynomial in N of degree at most that h-degree. It vanishes at N=1; log F also vanishes at N=2. The correction has no framing term. Therefore the already checked QJOINT primitive-image spanning lemma applies degree by degree: using the Vogel t-action and the triangular family of trefoil primitives gives an abstract completed primitive lift, and exponentiation gives a group-like diagram series. See `joint_loop_gate.md`, Section 4, for the normalization and the exact input to that lemma.

This does not establish either of the following stronger statements:

1. A graph-rational lift whose fixed-loop parts are finite beaded-graph expressions with the specified Alexander denominators.
2. Realization by an actual classical knot, including all compatibility conditions relating quantum data to its topology.

The determinant contradiction for b(31,13) demonstrates that even an integral cyclotomic sequence, scalar loop rationality, a completed group-like lift and preserved nonabelian minimal classical recurrence factors can coexist while actual knot realization is impossible. Eventual slope preservation has the additional explicit growth hypothesis of Section 4; it is not asserted for this pilot without that check. Using Δ=1 removes the determinant contradiction but proves no realization theorem. A geometric AJ interpretation for a compatible seed, all-color geometric state-sum constraints, and a graph-rational lift remain separate gates.

**Judgment:** the deletion operation preserves the stated formal structures and, conditionally, asymptotic data. It is useful against arguments claiming those structures alone force the ordinary Jones unit to propagate to every color. It is not a knot construction or a counterexample. The strongest algebraic addition is now the minimal primitive-symbol theorem in `ore_correction.md`; the most concrete obstruction is determinant/Alexander compatibility.
