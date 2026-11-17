# Two-bridge matrix coefficient: automaton referee and boundary repair

16 November 2026. Referee of Theorem B in the TWOBRIDGE lens, §3 of
`/Users/calebbarnett/jones-lanes/theory-restart/mech2/twobridge/REPORT.md`.
No word sweep was performed. This is a proof for the two displayed matrices;
it is conditional on Theorem A and the geometric scope identification when
applied to tangles.

## Verdict

The nonunit conclusion and the extreme-coefficient conclusion have a correct
algebraic proof. The stated span formula is correct **after deleting the
initial degenerate segment and renormalizing its first remaining exponent**.
It is not correct literally on every sequence as printed.

An exact counterexample to the unqualified formula is

    F(-1,1)=t^4(1+t^-3-t)=t+t^4-t^5.

Its span is four. The printed sum ignores the degenerate n0=-1 and assigns
the generic step n1=1 the increment 3|1|-2+2=3. The corrected boundary
normalization below gives initial exponent 1, hence c0=4.

This is a local repair, not a counterexample to nonflatness. No assertion
about NP or END of the unsigned bigraded N follows just from the two
extreme coefficients of its Euler polynomial being nonzero.

## 1. Matrices and exact boundary normalization

Work over Z[t,t^-1] and its fraction field. Put

    Y=[[1,0],[t^-3,t^-3]],
    X=[[1,1-t^4],[0,-t]],
    E=Y^-1 X=[[1,1-t^4],[-1,-1]],  E^2=t^4 I.

Write

    F(n0,...,n_(k-1))=e1^T E Y^n_(k-1) ... E Y^n0 e1,

where n_i!=0 for i>=1. This order means the rightmost block acts first.
Let v be the evolving vector and r=v2/v1.

The exact degenerate states are r=0 and r=-1. There are precisely two
kinds of initial degenerate segment:

1. If n0=-1, each initial exponent -1 sends e1 to t^4 e1 and therefore
   contributes only the monomial t^4. Delete all these initial -1 entries.
   If an exponent remains, it is >=1 or <=-2. If none remains, F=t^(4k).
2. If n0=0, the first block sends e1 to (1,-1). Every following exponent
   +1 returns this vector to itself. Delete the initial 0 and all those
   following +1 entries. At the first remaining exponent n_j!=1, use

       Y^n(1,-1)^T = Y^(n-1)e1

   and replace n_j by n_j-1. It is >=1 or <=-2, since this interior
   exponent cannot be zero. If there is no remaining exponent, F=1.

If n0 is already >=1 or <=-2 no normalization is needed. After this
operation, F is a monomial times a coefficient with first exponent m0
outside {0,-1} and all later exponents nonzero. The following proof applies
to this reduced sequence. It never returns to an exact degenerate state.

These degeneracies are also visible as group words: EY^-1=t^4X^-1 and
(EY)^(k-1)E=Y^-1X^k. They belong to the matrix-word double coset that
stabilizes the chosen row and column. This is only an algebraic statement;
that double coset's topological interpretation is a separate input.

## 2. Closed post-step automaton

Expand rational functions at t=infinity. Use the following post-E states:

    R:   deg r=-1,   lc r=1;
    S_j: deg r=-4-j, lc r=(-1)^j,  j>=0.

For n>0 and m>0,

    Y^n:  r -> t^-3+...+t^-3n + t^-3n r,
    Y^-m: r -> -(1+t^3+...+t^(3m-3)) + t^(3m)r.

Starting at r=0 with m0>=1 produces a pre-E leading term (degree -3,
coefficient 1), and E gives gain 1 in deg v1 and state R. Starting at
m0=-m<=-2 produces (3m-3,-1), then gain 3m+1 and state S0.

All later transitions are:

| Incoming state | Exponent | Leading pre-E r | Gain in deg v1 | Outgoing state |
|---|---:|---|---:|---|
| R or S_j | n>0 | (-3,1) | 1 | R |
| R | -m<0 | (3m-1,1) | 3m+3 | S0 |
| S_j | -m, m>=2 | (3m-3,-1) | 3m+1 | S0 |
| S_j | -1 | (0,-1) | 4 | S_(j+1) |

The positive-power sum dominates its shifted r term. For a negative
power the shifted r dominates from R, while the finite sum dominates
from S_j. In every case the denominator of

    E: r -> -(1+r)/(1+(1-t^4)r)

has a unique top-degree contribution, because the pre-E degree is -3
or is nonnegative. Its leading coefficient is +/-1. Thus multiplying
v1 by this denominator preserves a leading coefficient of absolute
value one and produces exactly the displayed gain.

There *is* leading cancellation in the numerator 1+r in the last row.
It is harmless and must be stated, not denied. There r=-1+t^3 r_old
exactly, so the numerator is -t^3 r_old. Division by the degree-four
leading denominator yields S_(j+1). This verifies closure even through
arbitrarily long strings of exponent -1.

## 3. The reciprocal identity and both extreme coefficients

Put D=diag(1,-t^3), and let a bar substitute t^-1. Direct multiplication
gives

    bar(Y)=D Y^-1 D^-1,   bar(X)=D X^-1 D^-1,
    bar(E)=t^-4 D Y E Y^-1 D^-1.

The middle Y factors telescope in the product, while e1^T D Y=e1^T and
D^-1 e1=e1. Consequently the report's exact identity is correct:

    F(n0,...,n_(k-1))(t^-1)
      = t^(-4k) F(-n0-1,-n1,...,-n_(k-1))(t).

For the boundary-normalized sequence, its reciprocal sequence is also
boundary-normalized. Both follow the automaton forever. Hence the high
and low coefficients of F are +/-1.

Let g be the gain table above. The span is the total gain of the sequence
plus that of its reciprocal minus 4k. Its first increment is

    c0=3m0+1       if m0>=1,
    c0=3|m0|-2    if m0<=-2.

For every subsequent exponent m_i,

    c_i=3|m_i|-2+2*[sign(m_i)!=sign(m_(i-1))].

Indeed a positive exponent always has gain1; its reciprocal negative
exponent has gain3|m_i|+1 or3|m_i|+3 depending on whether the preceding
sign agrees. The negative case is the same computation in reverse.
Every increment is positive, and c0 is at least4. Thus every coefficient
with a nonempty boundary-normalized sequence has positive span. All
monomial cases are exactly the two completely degenerate patterns above,
including the empty product.

## 4. Positive alternating blocks

For w=Y^a1 X^b1 ... Y^as X^bs with all a_i,b_i>0, write A=sum a_i,
B=sum b_i. The claimed positive-word formula also follows independently:

    maxdeg J=B, lc_top=(-1)^B,
    mindeg J=-3A, lc_bottom=1, span J=3A+B,

in the matrix normalization (before any overall framing monomial).
After a completed block, the coordinate degrees satisfy

    degmax v1=B, degmax v2=B-3,
    degmin v1=-3A, degmin v2=-3A+b_s.

The next Y^a sends the leading part of v1 to v2 with a degree loss3,
and its lowest part with a loss3a; the competing shifted old v2 term
is strictly smaller at the top and strictly higher at the bottom.
The following X^b has upper-right entry (1-t^4)[b]_-t, of highest degree
b+3 with coefficient(-1)^b and lowest degree0 with coefficient1.
This proves the displayed degree relations and coefficients by induction.

## 5. Scope of the accepted algebra

The matrices themselves prove: F is monomial precisely for the fully
degenerate normal forms, and otherwise it has positive span and endpoint
coefficients +/-1. With Theorem A and a correct geometric double-coset
criterion, this gives nonflatness in the asserted side-preserving class.
The algebra does not establish those geometric premises, the list of
strong-inversion classes, or an extension to side-exchanging inversions.

Likewise, surviving extremes in J do not show that the unsigned quantum
extremes of N are visible: additional cancelling homology can lie beyond
the Jones support. The report's categorified statement remains conditional
on its explicitly unconstructed CAT input. The phrase "END at the level
of J" should not be promoted to END(N).
