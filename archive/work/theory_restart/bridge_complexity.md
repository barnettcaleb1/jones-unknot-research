# Jones triviality as an exact counting problem: useful bridge and limits

17 November 2026. Theory-only response to CROSS-FIELD THEORY BUILDING. No scan. The lemmas below are deductions with proofs, not a claim of novelty or a hardness theorem. Let diagrams be ordinary explicit planar encodings, with input size N, and normalize the oriented Jones polynomial by V_U=1.

## 1. The precise translation

Let JT be the language of knot diagrams D with V_D=1. JC says exactly JT=UNKNOT as languages on the same encoding. Consequently JC implies JT is in NP intersect coNP, unconditionally: Hass–Lagarias–Pippenger, Theorem 1.1, proves UNKNOT is in NP; Lackenby, Theorem 1.1, proves KNOTTEDNESS is in NP. Kuperberg's earlier GRH hypothesis is unnecessary here. See [HLP](https://www.math.ucdavis.edu/~hass/Research/Papers/Complexity/hlp.pdf) and [Lackenby, arXiv:1604.00290v3](https://arxiv.org/abs/1604.00290).

**Conditional hardness consequence.** If JT is coNP-hard under deterministic polynomial-time many-one reductions, then JC implies NP=coNP. Indeed JC puts JT in NP, so coNP is contained in NP; complementation gives equality. NP-hardness of JT gives the same conclusion using its conditional coNP membership. This is a genuine connection to an independently meaningful problem, but only a conditional obstruction: we have no such reduction, and JT being in NP intersect coNP would not imply JC.

**Boundary correction.** Allowing arbitrary links while retaining the fixed target V=1 does not produce a larger yes-language. For a c-component link, V_L(1)=(-2)^(c-1), so V_L=1 forces c=1. EKT concerns equality to the corresponding unlink polynomial, namely (-t^(1/2)-t^(-1/2))^(c-1), which is a different target. A reduction to that moving target need not land on knots; it does not transfer to JT without a fusion construction preserving the entire identity. Such fusion is precisely where our earlier skein constructions failed.

## 2. An unconditional counting-class lemma

**Lemma.** JT belongs to C_=P. The same holds for testing whether a link has the polynomial of its component-count-matched unlink, and for equality of the polynomials of two input diagrams.

**Proof.** Work in the bracket variable A, so every exponent is integral. A normalized reduced bracket is

    (-A^3)^(-w(D)) sum_s A^(a(s)-b(s)) (-A^2-A^-2)^(c(s)-1).

Its exponent support has length O(N) and lies in an explicitly computable O(N) interval. Guess a smoothing state and one of the two monomials for each of its c(s)-1 circle factors. The exponent and sign of that contribution can be calculated in polynomial time. Hence each coefficient is a GapP function: the number of positive contributions minus negative contributions. Subtract the appropriate target coefficient and call the resulting integer g_k(D). Then

    G(D)=sum_k g_k(D)^2

is GapP, by closure under multiplication and polynomially indexed sums, and G(D)=0 exactly for the requested polynomial identity. This is the definition of C_=P. Diagram validity and component count are polynomial-time checks, so invalid encodings can be rejected separately. The proof is exact; randomized evaluation is not needed.

GapP closure and the zero-test characterization are standard; [Fortnow, Counting Complexity, Sections 3–4, Classification 4.8](https://lance.fortnow.com/papers/files/counting.pdf) gives the framework. Membership is useful bookkeeping, not evidence of C_=P-hardness.

## 3. Why existing Jones hardness does not settle this

Kuperberg's Theorem 1.2 proves Cook–Turing #P-hardness of distinguishing two separated ranges of |V_K(zeta)| at a fixed principal non-lattice root, even when the output is a knot. It uses approximations and a promise gap, not exact equality to 1 as a Laurent polynomial. [Kuperberg, arXiv:0908.0512v2](https://arxiv.org/pdf/0908.0512).

Wocjan–Yard's Theorem 8.3 likewise concerns significant bits of normalized root evaluations; Theorem 8.4 concerns a PP-hard highest-bit decision. Neither gives a many-one reduction to the full unit fibre. [Wocjan–Yard, arXiv:quant-ph/0603069v3](https://arxiv.org/pdf/quant-ph/0603069).

The distinction is structural: the first Jones #P-hardness result already applies to alternating links, where detecting the unlink polynomial is easy from a reduced alternating diagram. Hardness of computing a function can coexist with an easy special fibre. See [Jaeger–Vertigan–Welsh, 1990](https://gwern.net/doc/math/1990-jaeger.pdf). Thus planarity or one-component output alone is not the missing restriction. It is exact symbolic control of the target fibre, across every coefficient simultaneously.

## 4. A first proved obstruction to counting gadgets

**Bounded-jet obstruction.** Fix r. Suppose a polynomial-time construction x -> D_x has the property that every nonunit output has a nonzero coefficient of h^j, j<=r, in V_Dx(e^h)-1. Then testing V_Dx=1 on this family is in P.

**Proof.** Each of the finitely many coefficients of h^j is a finite-type invariant of order at most j. A fixed finite-type invariant can be computed in polynomial time in the crossing count. Compute these r coefficients and test whether they all vanish. The hypothesis makes this test exact. Bar-Natan's Theorem 1 supplies the algorithm, while Theorem 2 supplies a polynomial magnitude bound. [Polynomial invariants are polynomial, MRL 2 (1995), 239–246](https://www.math.utoronto.ca/drorbn/papers/poly/poly.pdf).

In particular, a coNP-hardness reduction of this bounded-depth kind would force P=NP. An even stronger, unconditional exclusion applies to the naive exact counting gadget

    V_Kx(t)-1 = D(t) #SAT(x),

with fixed nonzero integral Laurent D and polynomial-size output. If D(1)!=0, the identity already contradicts V_Kx(1)=1. Otherwise let r be its first nonzero Taylor order. That Jones coefficient is a fixed nonzero multiple of #SAT(x), but Bar-Natan's growth bound makes it polynomially bounded in the output crossing count. Tautologies have exponentially many satisfying assignments. Contradiction.

Therefore an exact hardness gadget cannot merely attach a fixed universal vanishing factor to a counting gap. It must allow unbounded perturbative depth, change the way counts enter, or avoid such value-preserving encoding entirely. This is a rigorous design constraint rather than another search. It also explains why approximate universality at one root cannot simply be promoted to the needed symbolic gadget. The unbounded-depth families already banked in FT-DEEP are compatible with, but do not supply, such a reduction.

## 5. Assessment and next statement

The NP/coNP observation is a useful conditional test, not presently a route to proving JC. The strongest first task is to classify which exact arithmetic operations are realizable by classical knot/tangle gadgets while preserving the target fibre and boundary connectivity. A valid construction must specify its symbolic tensor, its framing normalization, the identity predicate it preserves, and its connected closure. A finite gadget theorem proving universality for exact zero tests would be substantial; a theorem showing those operations cannot implement subtraction/zero tests under connected closure would explain why evaluation hardness misses JT.

The cheapest falsifiers are already clear: a proposed fixed-prefactor count encoding fails Section 4; a root-only equality fails to imply polynomial equality; a link gadget with target 1 is automatically a knot gadget; a matching-unlink gadget loses the desired target after fusion unless proved otherwise. No C_=P-hardness of either exact unit fibre or matching-unlink fibre was located in this bounded source check. Novelty of the membership observation is not claimed.
