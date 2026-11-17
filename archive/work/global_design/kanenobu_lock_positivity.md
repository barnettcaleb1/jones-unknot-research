# Exact Jones-unit locus in the four-parameter matched-lock family

2026-11-03. This is a deduction from a published explicit polynomial, with an independent internal algebra/source read. Follow-up183146 adds a diagrammatic isotopy for every zero-chain case, independently traced twice. Thus this specified family contains no counterexample. No parameter enumeration is used and no novelty is claimed.

Source: Anokhina, Lanina and Morozov, *Planar decomposition of the HOMFLY polynomial for bipartite knots and links*, EPJC84 (2024),990, journal equations (7.20)–(7.21), Figure25 with matched opposite chains i=i', j=j'.

https://doi.org/10.1140/epjc/s10052-024-13309-0

This is the actual family Kan(2m,2n,2j,2i), not the paper's separately defined Jones precursor. The source uses H(unknot)=D={A}/{q}, and its formula has restored topological framing. Thus H/D at A=q^2 is the ordinary reduced Jones polynomial. Source equations (6.9)–(6.10) extend the chain expressions to negative integers by inverse chains. In arXiv v1, the two principal formulas are numbered (7.21)–(7.22).

Use x for the HOMFLY variable A after specializing to q^2; it is NOT the bracket variable used elsewhere in the project. Put

    [r]_x=(x^r-x^(-r))/(x-x^(-1)),
    z=x^2+x^(-2)-x-x^(-1).

The published formula yields

    V=1+z x^(-2(m+n)) Q_(i,j)(x),
    Q=[i]^2+[j]^2-[i-j]^2+z[i]^2[j]^2.

We prove Q is nonzero whenever i and j are nonzero. The useful exact identity is

    [i]^2+[j]^2-[i-j]^2=(x^(i-j)+x^(j-i))[i][j].

Consequently

    Q=[i][j](x^(i-j)+x^(j-i)+z[i][j]).

Fix ANY real x>1. Then z=(x+x^(-1)-2)(x+x^(-1)+1)>0 and [r] has the sign of r. If ij>0, the parenthesized factor is manifestly positive. If ij<0, simultaneous negation and interchange reduce to i=a>0, j=-b<0. The factor becomes

    x^(a+b)+x^(-a-b)-z[a][b]
      =x^(a-b)+x^(b-a)+(x+x^(-1)-2)[a][b] >0.

The equality follows by expanding (x-x^(-1))^2[a][b]; every term on the last line is positive. Thus Q has the sign of ij and never vanishes at any x>1 when ij is nonzero. It cannot be the zero Laurent polynomial.

Conversely, i=0 or j=0 makes Q identically zero immediately. Therefore, over all signed integer parameters of the specified family,

    V_K identically 1  iff  i=0 or j=0.

More strongly, on this real specialization V_K-1 has the sign of ij for all x>1, independent of m+n. The positive monomial x^(-2(m+n)) cannot enable cancellation. This is a family-specific inequality, not a global Jones positivity claim.

The degenerate cases have reduced fundamental HOMFLY1 already before specialization, directly from the source's formula. The initial pass could not retrieve the figure and left their topology unverified. The follow-up below settles that topology by isotopy.

Scope: unmatched chains, horizontal-to-vertical replacements, odd p/q parity variants, and the larger KanGen family are not covered. The result gives a reason not to scan this specific four-parameter generalization of the original Kanenobu diagram. It supplies no constraint on the separate EKT-derived nonunit-turnback candidate.

## Zero-chain isotopy: completing the family theorem

Source Figure25 was inspected from the actual PDF, page23; local read-only copy `tmp/pdfs/alm-2407.08724.pdf`, rendered page `tmp/pdfs/alm-figure25.png`. Equation numbering varies between the downloaded PDF and HTML; the formula is the reduced specialization of the HOMFLY expression immediately below Figure25, not the precursor expression at the bottom of that page.

When i=i'=0, erase the two upper-left chains. The small upper return arc now directly caps the two upper ends of the 2n chain. Peel off its crossings by Reidemeister I moves. Its lower ends become connected by a cap.

The two lower j chains now have their four lower endpoints joined in the nested pairing C=(14)(23): the inner return was already present, and the outer return uses the erased n chain. Sliding a crossing around these two return arcs gives the actual tangle isotopy

    sigma1^r C is isotopic to sigma3^r C.

It is a same-sign transfer. The barred j chain and the unbarred j chain carry opposite exponents, so sigma1^(-2j) sigma3^(2j) C is isotopic to C. Cancel them by Reidemeister II after the slide. Now the 2m chain is capped below; remove its curls by Reidemeister I. A planar long arc remains, and its standard exterior closure is U.

For j=j'=0, reverse top and bottom: remove the capped m chain, cancel the matched i/inverse-i chains, and remove the capped n chain. Signed exponents do not affect either argument. This is an unframed ambient isotopy; framing units never serve as topology certificates.

Combining this with the positivity calculation proves, at the stated family scope,

    V_K=1 iff (i=0 or j=0) iff K=U.

The diagram routing and same-sign cup-transfer move were checked independently by the root and annular_critique. Internal status TRUSTED pending Claude's read; priority not investigated.

## The larger published vertical-edge extension

The actual even-parameter KanGen extension has S=m+n and h=k+l, where k,l count vertical necklace edges in the source's hypercube tangles. These are nonnegative counts in the geometric definition, not signed braid powers. Its chain formula uses

    D barTheta_(S,h)=(D+barphi)^h(1+D phi)^(S-h)-barphi^h,
    1+D phi=A^2.

Inserting this into the published KanGen HOMFLY formula and setting A=q^2 yields its reduced physics-normalized value

    H/D=M^h+q^(-4S)L^h ZQ,
    M=q(q^4+1), L=-q^5(q^2-1),
    Z=(q^3-q^-3)(q-q^-1), Q=Q_(i,j)(q^2).

This derivation uses the actual family, not its Jones precursor. At q=1 the value is 2^h. Therefore for h>0 it cannot equal the knot's constant polynomial1. The quantum-dimension limit gives h+1 components; translating to the standard Jones link convention may change the component sign, but not the absolute value 2^h. At h=0 the matched four-parameter family above is recovered.

This closes the specified even-parameter extension as a counterexample design. Negative necklace counts have not been realized geometrically and are not admitted by analytic continuation of the formula. Unmatched i,i',j,j' and odd-parity changes remain outside this conclusion. No new candidate is proposed by this note.
