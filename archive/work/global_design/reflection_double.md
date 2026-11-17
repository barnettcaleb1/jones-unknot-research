# Reflection double: an exact global reduction, not yet a mechanism

Design note, 2026-11-03. No enumeration. This is elementary algebra and a prospective geometric bridge, not a novelty claim.

Let -K be the mirror of an oriented knot K with orientation reversed, and let R(K)=K#(-K). Write V_K(q)=sum_j a_j q^j, normalized by V_U=1. Define

    E(K) = [q^0] V_R(K)(q)
         = sum_j a_j^2
         = (1/(2*pi)) integral_0^(2*pi) |V_K(exp(i*theta))|^2 dtheta.

The first equality uses Jones multiplicativity and mirror duality; the last is Parseval. Since sum_j a_j=V_K(1)=1, E is positive and E=1 modulo 2. If E=1, exactly one coefficient is nonzero and it is +1. Thus V_K=q^s; V'_K(1)=0 forces s=0. Conversely V_K=1 gives E=1. Therefore

    D(K) := (E(K)-1)/2

is a nonnegative integer, and D(K)=0 iff V_K=1. If V_K is nonconstant, E(K)>=3. Unlike Mahler measure, this norm does not assign its minimum to nonconstant cyclotomic polynomials.

Consequently T is equivalent to this restricted statement about reflection doubles:

> If the central Jones coefficient of R(K) is 1, then R(K) is the unknot.

Indeed, the forward implication uses E=1 iff V_K=1. For the reverse implication, V_K=1 gives E=1, hence R(K)=U; uniqueness of prime decomposition (or genus additivity) then gives K=U.

The restriction is global in K: every knot has this double. The reduction does not restrict the search to a subclass of possible original knots. But it also does not remove the conjecture's difficulty.

## Prospective cross-field mechanism

Reflection positivity suggests looking for a geometric sum-of-squares decomposition of D(K) BEFORE passing to the scalar skein quotient. An adequate construction would provide nonnegative terms indexed by genuinely geometric defects of the marked reflection double, prove their sum is D(K), and prove simultaneous vanishing produces a spanning disk in S^3.

The proposed proof chain would be: V_K=1 -> D(K)=0 -> each positive geometric defect vanishes -> disk for R(K) in S^3 -> K=U. The middle two implications are OPEN and no candidate geometric terms have been constructed.

There are three immediate obstacles.

1. R(K) is ribbon for EVERY K. A slice disk or ribbon disk in B^4 proves nothing here. The certificate must give a disk in S^3 or an equivalent actual unknotting conclusion. The ribbon fact is standard; see [Tanaka, On the symmetry of composite ribbon knots](https://www.sciencedirect.com/science/article/abs/pii/S0166864123000111).
2. Cutting K at one point gives a (1,1)-tangle whose Temperley-Lieb skein space has rank one. Its image is already a scalar multiple of the identity. Reflection inside that one-dimensional quotient yields the displayed norm, with no retained geometric defect. Cutting along many strands retains more information, but its full pairing is not determined by the one closed Jones polynomial.
3. Sum-of-squares positivity occurs AFTER the coefficients have undergone their internal signed cancellations. It does not imply positivity of individual geometric states. The same algebra works for virtual knots, so classicality has not yet entered. A viable construction must supply B2 independently; B1 comes from the knot normalization and connected sum but does not supply B5.

## Quantum normalization check

At a unitary Jones level, a 2m-strand plat satisfies

    |V_plat(beta)(q)| = d^(m-1) |<v,rho(beta)v>|,
    d = 2*cos(pi/r), q=exp(2*pi*i/r), ||v||=1.

Thus V=1 gives an interior overlap d^(1-m) for m>1 and d>1. The saturating overlap 1 represents the m-component unlink, not the unknot at that bridge width. Cauchy-Schwarz equality therefore does not provide the missing geometric implication. Source: [Wocjan-Yard, equation 5.39](https://arxiv.org/pdf/quant-ph/0603069).

Verdict: a useful precise specification of the positivity theorem one would need, but not an established route. Park unless a geometric positive decomposition can be written independently of the desired conclusion. No additional computation is suggested.
