# AJ and the actual-image gate for deleting the first Habiro coefficient

Date: 2026-11-03. Bounded primary-source read and theoretical check; no computations or census. No board changes.

## Verdict

The proposed modification of the AJ-proved knot b(31,13) is **not** a joint formal model compatible with all elementary constraints on actual knots. Its ordinary Jones polynomial becomes 1, while its unchanged Melvin–Morton–Rozansky diagonal requires Alexander determinant 31. This already violates the Jones–Alexander determinant identity. Preservation of a nonabelian classical recurrence component would not repair that failure.

No nontrivial Alexander-polynomial-one knot with a proved AJ theorem was certified in this bounded read. In particular, this note does not assert AJ for the Kinoshita–Terasaka knot, Conway knot, untwisted Whitehead doubles, or pretzel (-3,5,7). Failure to certify such an example here is not a claim that no theorem exists.

## 1. What the primary AJ theorems actually say

[Dunfield–Garoufalidis, Non-triviality of the A-polynomial for knots in S³](https://arxiv.org/pdf/math/0405353), Theorem 1.1, proves that every nontrivial classical knot has an A-polynomial with a factor beyond the reducible factor L−1; it is not merely a power of L−1. The authors record the independent result of Boyer–Zhang. Their Corollary 1.4 says that the AJ conjecture would make the **full colored Jones function** detect the unknot. It supplies no implication from the single color J₂=1 to all colors being 1.

[Le–Zhang, Character varieties, A-polynomials, and the AJ conjecture](https://letu.math.gatech.edu/Papers/AJ_Conjecture4.pdf), Corollary 1.9, proves AJ for every two-bridge b(p,q) with odd prime p. Thus it applies to b(31,13). This is a direct theorem, not a numerical extrapolation or the weaker coprimality criterion in an earlier sufficient condition. Their notation has double branched cover L(p,q).

The earlier [Le–Tran, On the AJ conjecture for knots](https://letu.math.gatech.edu/Papers/On_AJ_conjecture.pdf), Remark 0.1, also includes b(31,13) in its verified p<45 range. Its conventions are unreduced J_U(N)=[N], with L shifting color, M=t^(2N), and LM=t²ML. Its AJ specialization is t=−1, with M held independent.

## 2. The deletion and its decisive failure for b(31,13)

Use the project's reduced zero-framed convention

    J_1=1, J_2=V, J_N(U)=1,
    C_(N,k)= product_(j=1)^k (q^N+q^(-N)−q^j−q^(-j)),
    J_N= sum_k H_k(q) C_(N,k).

For an actual seed knot K define

    F_N = J_N(K) − H_1(K;q) C_(N,1).

Then F_1=F_2=1 exactly, and the integral Habiro expansion simply has its H_1 coefficient replaced by zero. The correction is a Laurent polynomial in q and M=q^N, so it is q-holonomic and belongs to a one-dimensional rational difference module over Q(q,M).

If a₂(K)=0, then H_1(K;1)=0 in these conventions. Consequently this correction has zero MMR diagonal: on putting q=exp(x/N) and taking the formal large-color diagonal, H_1 tends to zero while C_(N,1) tends to exp(x)+exp(−x)−2. Thus F has the same Alexander diagonal 1/Delta_K(exp(x)) as J(K).

For the archived pilot K=b(31,13), the Conway polynomial is 1−2z⁴. Hence

    Delta_K(−1)=1−2(−4)²=−31,
    |Delta_K(−1)|=31.

If F were the colored Jones sequence of a knot K', MMR would force Delta_K'=Delta_K, whereas F_2=1 forces |V_K'(−1)|=1. The actual-knot identity

    |V_K'(−1)| = |Delta_K'(−1)|

would read 1=31. This is a complete obstruction to realizing this particular modified sequence by a knot, independently of AJ or recurrence preservation.

**Scope:** a₂=0 is enough to preserve the MMR diagonal under deletion; it is not enough to preserve consistency with the newly flat ordinary Jones polynomial. A proposed seed needs at least determinant 1 as well, followed by the other cross-invariant checks. Delta=1 would remove this particular Alexander obstruction, but does not by itself certify all such checks.

## 3. Reduced versus unreduced normalization

Multiplying a reduced sequence by the quantum dimension [N] is a rational gauge transformation r(q,M). Under conjugation the shift L acquires r(q,qM)/r(q,M) (or its inverse, according to the direction of conjugation). With M formal and fixed, that ratio specializes to 1 at q=1. Thus the classical recurrence curve is unchanged up to coefficient-field units in M.

This uses the semiclassical specialization with M independent. It must not be confused with first fixing the integer color N and taking q→1, where [N+1]/[N] tends to (N+1)/N. The latter is not the AJ specialization.

## 4. What remains useful about the recurrence experiment

The finite-M correction has a first-order annihilator L−sigma(r)/r, with sigma(M)=qM, whose normalized classical limit is L−1. There is therefore a precise algebraic question, independent of actual-knot realization: does adding such a rational correction preserve the factors of the minimal classical recurrence away from L−1? The separate Ore-algebra check addresses this question. Even a positive answer proves only that a formal sequence can retain a nonabelian recurrence component while its color two is flat; it does not show that the sequence passes the determinant gate above.

The correct next use of this experiment is conditional: supply a genuinely compatible seed and establish the normalization of its minimal recurrence, then apply the algebraic preservation lemma. It is not legitimate to combine b(31,13)'s proved AJ theorem with another knot's Delta=1 property, or to transfer an AJ theorem to a modified formal sequence as if it were already a knot invariant.

No theorem reducing ordinary Jones detection to AJ was found. The missing input remains a constraint on the **actual image** of knot invariants linking color two to the higher-color/peripheral data.
