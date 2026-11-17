# Color-two flatness does not propagate from the usual formal identities alone

Theory-only bridge test, 2026-11-03. No computation or knot census. **This constructs formal polynomial sequences, not knots or quantum invariants of actual knot exteriors.** It disproves a formal implication from the particular listed constraints, not a topological realization theorem.

## 1. Convention and the first failed model

Use reduced, zero-framed colored Jones normalization J_1=1, J_2=V, J_N(U)=1 and Habiro's symmetric kernels

    C_(N,k)(q)=product_(j=1)^k (q^N+q^-N-q^j-q^-j).

The actual-knot expansion is J_N=sum_(k=0)^(N-1) H_k C_(N,k), H_k in Z[q^±1]. This convention and integrality are recorded in [Garoufalidis-Le, Asymptotics of the colored Jones function, Section 3.2](https://people.mpim-bonn.mpg.de/stavros/publications/asymptoticsjones.pdf), citing Habiro.

The suggested simplest sequence J_N=1+C_(N,2) has J_1=J_2=1 and J_3 nonconstant. But it FAILS the Melvin-Morton-Rozansky diagonal condition for any knot Alexander polynomial. At q=exp(x/N), its limit is

    1+(exp(x)+exp(-x)-2)^2.

MMR requires the limit/formal diagonal to be 1/Delta(exp(x)). Its reciprocal is not a Laurent polynomial: a Laurent polynomial with a Laurent-polynomial inverse must be a unit, whereas 1+(t+t^-1-2)^2 is nonconstant and not a monomial. Thus this first model is not adequate once MMR is included.

## 2. A repaired formal family

Let h(q) be a nonzero Laurent polynomial with h(1)=0. Define

    F_N(q)=1+h(q) C_(N,2)(q),               N>=1.                         (1)

For a particularly symmetric example use

    h(q)=q+q^-1-2.                                                        (2)

Its Habiro data are H_0=1, H_1=0, H_2=h, and H_k=0 for k>=3. For N=1 or 2, one kernel factor is zero. Thus F_1=F_2=1 identically, but F_3!=1 in the integral Laurent-polynomial domain. The ordinary Jones input is exactly flat while higher color is not.

Here are the constraints that this model really satisfies.

### Integrality, color symmetry and congruences

Each F_N is in Z[q^±1], and the displayed cyclotomic coefficients are integral. It satisfies F_-N=F_N on extending the reduced formula to integer N; multiplying by the odd quantum dimension [N] gives the usual negative-color sign for the unreduced version. For (2), F_N(q^-1)=F_N(q).

Put X_N=q^N+q^-N, a=q+q^-1, b=q^2+q^-2. Then

    F_N-F_M=h(X_N-X_M)(X_N+X_M-a-b).                                     (3)

So the familiar pairwise color congruence divisibility by X_N-X_M holds. Root-of-unity color periodicity and N->-N symmetry follow directly from this expression. These are algebraic properties of this sequence, not claims that every root-of-unity TQFT sewing axiom has been realized.

### An explicit q-holonomic recurrence

Expanding in color gives

    F_N=h q^(2N)+h q^(-2N)-h(a+b)(q^N+q^-N)+1+h(2+ab).

If E shifts N to N+1, then the nonzero monic operator

    product_(s=-2)^2 (E-q^s)                                              (4)

annihilates F. Its coefficients lie in Z[q^±1]; it is even a constant-coefficient recurrence in N. No claim of minimality is needed. Thus q-holonomicity, even with a very explicit recurrence, does not propagate F_2=1 to all colors. The knot theorem is [Garoufalidis-Le, The colored Jones function is q-holonomic](https://arxiv.org/abs/math/0309214).

More strongly, let

    f(q,M)=1+h(q)(M+M^-1-a)(M+M^-1-b).

With M acting by q^N, the first-order operator

    f(q,M) E - f(q,qM)

also annihilates F. Since h(1)=0, f(1,M)=1 and this displayed operator specializes to E-1. Thus a formally trivial classical specialization can coexist with nontrivial higher-color quantum corrections. This is not the peripheral/A-polynomial ideal of an actual knot and must not be treated as one.

### Degree bounds

For the explicit choice (2) and N>=3, the largest and smallest exponents of F_N are exactly 2N+1 and -2N-1, with coefficients 1. The two kernel factors have leading terms q^N and lowest terms q^-N, and multiplying by h adds one in either direction; no other term reaches those extremes. Its span is 4N+2. Thus it satisfies the usual qualitative O(N^2) upper degree bound (indeed a linear one). For N=1,2 the polynomial is 1.

This does not certify every conjectural slope or geometric degree constraint for knots; no knot is being asserted to have these degrees.

## 3. MMR and full loop-rationality shape survive the repair

Set q=exp(z) and treat x=Nz as the resummed color variable. Then (1) becomes

    F=1+h(exp(z))
       (exp(x)+exp(-x)-2*cosh(z))
       (exp(x)+exp(-x)-2*cosh(2z)).                                       (5)

Since h(1)=0, its constant term in z is 1. Hence the MMR diagonal is precisely 1/Delta(exp(x)) with Delta=1.

Moreover every coefficient of z^r in (5) is a Laurent polynomial in t=exp(x), of t-degree at most two in either direction. Therefore it has the full *shape* of Rozansky rationality

    R_r(x)=P_r(exp(x))/Delta(exp(x))^(2r+1),

with Delta=1 and P_r integral or rational Laurent polynomials as appropriate to the exponential Taylor coefficients. There is no pole or diagonal obstruction left. The actual-knot statements and conventions are in [Garoufalidis-Le, An analytic version of MMR, Section 2](https://people.mpim-bonn.mpg.de/stavros/publications/analyticMMR.pdf).

For (2), h(exp(z))=z^2+O(z^4). At fixed N,

    F_N(exp(z))=1+(N^2-1)(N^2-4)z^6+O(z^8).

The coefficient of z^d is an even polynomial in N of degree at most d-2 when nonzero. In particular it obeys the MMR triangular bound degree_N<=d, and the diagonal is trivial. At fixed x its first nonzero loop term is z^2(t+t^-1-2)^2.

These claims concern the numerical expansion constraints. They do NOT exhibit a group-like Kontsevich integral whose sl2 weight is the sequence, prove realizability by finite-type invariants of a knot, or check every weight-system relation. Those are additional realization conditions, not consequences of a polynomial degree bound.

## 4. Precise conclusion for the global route

The following package is insufficient to deduce higher-color triviality from ordinary Jones triviality:

1. Integral Laurent polynomials and an integral Habiro expansion;
2. J_1=1, the color-reflection symmetry, and the displayed pairwise color divisibilities;
3. q-holonomicity, even a concrete recurrence;
4. quadratic upper degree growth;
5. MMR diagonal with a normalized integral Alexander polynomial, and Rozansky's loop-rationality form.

The repaired sequence passes all five with J_2=1 and J_3!=1. The original H_2=1 sequence fails item 5; using it without the repair would overstate the countermodel.

No actual counterexample to Jones detection follows. The useful missing hypothesis is a **topological realization constraint linking H_1 to higher H_k**, or a knot-specific recurrence with a proved uniqueness mechanism at color two. Merely invoking q-holonomicity does not identify that recurrence from two initial values. Likewise, an AJ-type comparison concerns the actual annihilator of the full sequence and actual peripheral geometry; it cannot reconstruct those objects from J_2 without an additional theorem.

**Subsequent extension, 2026-11-03 12:33 (Q-JOINT).** The previously unconstructed group-like diagram lift in Section3 now exists by the all-order triangular construction in `joint_primitive_gate.md`. Thus THIS SAME scalar sequence satisfies the listed polynomial constraints and arises from a rational group-like Jacobi-diagram series. This does not establish diagram-level rationality, actual Kontsevich integral-lattice conditions, or realization by a classical knot. The historical statement that no lift was exhibited in this note is superseded by that extension.

This formal obstruction is an appropriate cheap check on a proposed propagation route. It is not a reason to launch a search for a knot realizing (1), and no such search is recommended.
