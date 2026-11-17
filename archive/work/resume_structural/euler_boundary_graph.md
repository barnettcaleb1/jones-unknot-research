# Euler cancellation as an interval-boundary graph

Status: algebraic propositions proved below; tangle application conditional on the stated curve shapes and grading conventions. This is a new deduction in this research record, not a claim of literature novelty. It serves the restricted realizability branch of U5. It does not prove Lemma Q or general Jones unknot detection.

## Inputs and normalization

Use the published length convention in Kotelskiy–Watson–Zibrowius, *Khovanov homology and strong inversions*, Lemma 2.5 and Theorem 3.1:
https://msp.org/obs/2022/5-1/obs-v5-n1-p10-p.pdf .
The existing one-special proof is `work/proof12/homology/one_special_bn_obstruction.txt`.

Write Q for the ordinary quantum variable, x=Q², and D(x)=1+x+x². For a length-4n special component, put

    E_n(Q)=Q^-1 (1+x²)(1-x³) Σ_{j=0}^{n-1} x^(4j).

This differs from the published pairing polynomial by one specified quantum shift. It is a polynomial in odd Q-powers. For k positive and divisible by four, let

    R_k(Q)=Σ_{j=0}^{k-2} (-1)^j Q^(2j+1) + Q^(2k+1),
    R_0(Q)=Q+Q^-1=:U(Q).

These are the rational-sector pairings, up to independent overall bigrading shifts, in the chirality selected by mirroring if needed. Direct geometric-series identities give

    Q(1+x) E_n(Q) = D(x)(1-x^(4n)),
    Q(1+x) R_k(Q) = x + D(x)x^k,
    Q(1+x) U(Q)   = x + D(x) = (1+x)².                 (1)

The k=0 identity follows directly from the definition of R_0.

For an actual two-component longitude filling with unknot meridional closure, the rational slope has absolute value k. If all special lengths are multiples of four, determinant zero forces k divisible by four: each special sector is delta-thin with determinant contribution of magnitude 4n, while the rational sector has magnitude k. Signs can differ, but their sum is zero. This does not assert that all actual special lengths are multiples of four; that remains outside the scope.

Since all generators of reduced Khovanov homology of a two-component link have odd quantum grading, the permissible quantum shifts of these normalized sectors are even powers of Q, or integer powers of x. Their homological shifts enter Euler polynomials as signs.

## 1. A bound on rational-sector displacement

Suppose r>=1 special sectors satisfy the complete Euler identity

    ε x^a R_k(Q) + Σ_{i=1}^r η_i x^(b_i) E_(n_i)(Q) = U(Q),       (2)

where k is a nonnegative multiple of four, n_i>=1, a,b_i are integers, and ε,η_i are signs. Then

    ε=+1,   a is divisible by 12,
    a>0 implies a <= 3(r-1),
    a<0 implies |a| <= 3r.                                    (3)

In particular, if there are at most three special sectors, a=0. Thus their Euler polynomial cannot hide a shifted rational sector. Four sectors can hide a shift algebraically, as the example below shows.

**Proof.** Multiply (2) by Q(1+x) and use (1). Reduction modulo D gives ε x^(a+1)=x modulo D. At a primitive cube root ζ, this says ε ζ^a=1. A cube root of unity cannot be -1, hence ε=1 and 3 divides a.

Evaluate the multiplied identity at x=i. Every special term vanishes because i^(4n_i)=1, while k is divisible by four and x+D=2i is nonzero. Consequently i^a=1, so 4 divides a. Hence 12 divides a.

Rearranging the identity now gives

    Σ η_i x^(b_i)(1-x^(4n_i))
      = 1-x^(a+k) + x(1-x^a)/D.                              (4)

If a=3l is nonzero, the last term has exactly 2|l| distinct monomials, each with coefficient +1 or -1. For l>0 this follows from

    x(1-x^(3l))/D = x(1-x) Σ_{j=0}^{l-1} x^(3j).

For a>0, these 2l monomials lie strictly between degrees 0 and a. Both extra terms 1 and -x^(a+k) are new, distinct endpoints because k>=0. Thus the right side has exactly 2l+2 terms and a<=3(r-1).

For a<0, the 2|l| monomials lie strictly between degrees a and 0. If a+k=0, the extra terms cancel each other and do not alter that support. Otherwise the constant term is new, while -x^(a+k) can cancel at most one existing term. The right side therefore has at least 2|l| terms, giving |a|<=3r. Combined with 12 dividing a, these bounds force a=0 for r<=3. QED.

The threshold four is sharp for these algebraic constraints. The identity

    x^-12 R_12 + x^-10 E_2
      - (x^-11+x^-8+x^-5) E_1 = U                           (5a)

has four special summands and rational displacement a=-12. To verify it using (1), note that k=12 makes 1-x^(a+k)=0 and

    x(1-x^-12)/D
      = x^-10(1-x^8)
        - x^-11(1-x^4) - x^-8(1-x^4) - x^-5(1-x^4).

This is an exact formal Euler identity, not the invariant of a constructed classical tangle.

This is a support argument on whole polynomials, not a check at finitely many parameter values: the root evaluations restrict the integer shift, while the full support count rules it out.

## 2. Definition: the Euler boundary graph

When a=0, equation (4) becomes

    Σ η_i x^(b_i)(1-x^(4n_i)) = 1-x^k.                       (5)

Represent each summand by an oriented edge on the integer line:

- if η_i=+1, the edge runs from b_i to b_i+4n_i;
- if η_i=-1, reverse that orientation.

The boundary of an edge u→v is defined here as x^u-x^v. Equation (5) says that the graph has one unit of outgoing boundary at 0, one unit of incoming boundary at k, and zero net boundary at every other vertex. This convention fixes the sign of the graph boundary.

The graph is merely an encoding of Euler contributions and grading shifts. Its edges are not embedded tangle arcs, and decomposing it into paths and cycles does not realize those moves geometrically. Its value is that the algebraic cancellation is now an exact conservation law rather than an unspecified sum of Laurent polynomials.

## 3. Complete two-special Euler classification

For r=2, all solutions of (2) have ε=1 and a=0. Moreover:

**If k=0**, the two edges are the same interval with opposite orientations. Thus

    n_1=n_2,   b_1=b_2,   η_1=-η_2.                         (6)

**If k>0**, the two oriented edges form a path

    0 → z → k,

where z is distinct from 0,k and lies in 4Z. The intermediate point may lie inside or outside [0,k]. Equivalently, after possibly interchanging the two sectors, their signed endpoint differences are ±4n_1 and ±4n_2 and add to k. No additional disconnected Euler-zero component is possible with only two nonzero-length edges.

**Proof.** Each edge has two distinct endpoints and unit multiplicity. If its boundary is canceled at an endpoint other than 0 or k, that endpoint must be an endpoint of the other edge, with the opposite contribution. For k>0, the remaining endpoints must be 0 and k with the prescribed signs. Two parallel edges on just those endpoints would have total coefficient 0 or ±2 rather than ±1, so the intermediate point is distinct. If k=0, both endpoint contributions must cancel, forcing exactly the same endpoints and opposite directions. Since each edge length is a positive multiple of four, the statements about z and lengths follow. QED.

For example, the monotone path with k=4(n+m) is the identity

    R_(4(n+m)) + E_n + x^(4n) E_m = U.                    (7)

The path going beyond k gives a difference of lengths, for instance

    E_n - x^k E_m = E_(n-m),  k=4(n-m), n>m,

where this equation is interpreted after the same normalization (equivalently compare the boundaries in (1)). The graph proof includes all translations and signs without a case-by-case expansion.

## 4. What the classification does not prove

For k=0, (6) reduces the only possible two-special cancellation to two copies with identical quantum support and opposite homological parity. The endpoint-gap argument in `two_special_bn.md` excludes this pattern when the rational unlink sector sits in homological degree zero. That is a restricted spectral-sequence realization obstruction, not a general conclusion from the graph alone.

For k>0, the monotone path already admits a formal Bar–Natan spectral sequence for n=m=1, k=8. The explicit certificate in `two_special_bn.md` leaves two generators at h=0 and cancels the rest by differentials of degrees (1,2) and (1,8). Thus the interval-path classification does not itself exclude a two-special tangle. No classical realization of that formal data is asserted.

The graph records only Euler cancellation. Classical realization, compatibility of the different filling maps, and the allowed deformation maps are additional constraints. The usefulness of this definition is to separate these constraints: any proposed two-special proof must handle the path configurations above, while any general proof must also control Euler-zero cycles. The archived four-special phantom shows that some cycles survive the known formal deformation and extension tests.

## Scope and next gate

The finished statements are the displacement bound and the exact two-edge classification. They concern length-4n rank-one special components with the stated rational pairing and shifts. They do not cover length 2 mod 4 components, arbitrary local systems, arbitrary numbers of specials, or a generic Jones-one knot. Neither actual topology nor a Jones counterexample has been manufactured from the graph.

No knot table, braid family, or new geometric representative was enumerated. The deduction uses the already sourced sector formulas and elementary Laurent-polynomial algebra. A useful next theorem would constrain which boundary graphs and relative homological shifts can come from a single actual tangle, rather than impose an additional formal condition already passed by the archived phantom.
