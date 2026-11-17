# Reciprocal core gate for the amphicheiral construction lane

17 November 2026. A deductive consequence of the banked ROOTS, second-moment,
MOMENT-CYC10 and TH-J-FACTORS statements. No candidate enumeration. The polynomial
examples below are formal: no tangle realization is asserted.

## 1. Precise hypothesis and conclusion

Let J be the preferred integral Laurent polynomial of a strong inversion, in
either of the mutually inverse t conventions used in the collaboration. Assume

1. J(t) = J(t^{-1});
2. the covering knot has a_2 = 0;
3. J is 1 at primitive tenth roots (equivalently Phi_10 divides J - 1).

The first condition follows when the **marked strong inversion**, including its
preferred framing, is equivalent to its mirror. Amphicheirality of the underlying
knot alone does not identify its possibly different strong inversions, and is
not sufficient for this step. A polynomial which is only reciprocal up to a
monomial must first be put in the preferred normalization; the statement below
uses exact reciprocity.

Put z = t + t^{-1} and

    P(z) = (z - 2)(z + 2)^2 z(z - 1)(z^2 - z - 1).

Then there is a unique H in Z[z] such that

    J(t) = 1 + P(t + t^{-1}) H(t + t^{-1}).                 (1)

In particular, either J = 1 or

    span_t J = 14 + 2 deg H >= 14.                         (2)

These are necessary conditions, not a nonflatness theorem. They do not exclude
the proposed prime amphicheiral construction.

## 2. Proof of integral divisibility

The invariant subring of Z[t,t^{-1}] under t -> t^{-1} is Z[z]: write a reciprocal
Laurent polynomial as c_0 + sum c_n(t^n + t^{-n}), and use
S_0 = 2, S_1 = z, S_{n+1} = z S_n - S_{n-1}. Thus J - 1 = R(z) for R in Z[z].

ROOTS and a_2 = 0 give

    (t - 1)(t + 1)^3 Phi_4(t) Phi_6(t) | J(t) - 1.

The identities

    z - 2 = (t - 1)^2/t,       z + 2 = (t + 1)^2/t

show that the order of R(z(t)) at each of t = 1 and t = -1 is even. Consequently
the first two multiplicities improve to 2 and 4. (If R = 0 the conclusion is
immediate.) In the z ring this says (z - 2)(z + 2)^2 divides R.

The remaining root conditions give

    Phi_4(t)/t = z,
    Phi_6(t)/t = z - 1,
    Phi_10(t)/t^2 = z^2 - z - 1.

At primitive fourth, sixth and tenth roots the corresponding z values are,
respectively, 0, 1 and the two roots of z^2 - z - 1. Thus each of these monic
polynomials divides R in Z[z]. They are distinct irreducible factors over Q,
separate also from z +/- 2. Their product, with the stated multiplicities,
divides R over Q; monic division (or Gauss's lemma) makes the quotient integral.
No assertion that the ideals are pairwise comaximal over Z is needed.

Equivalently, with

    D_sym(t) = (t - 1)^2(t + 1)^4 Phi_4(t) Phi_6(t) Phi_10(t),

we have P(z(t)) = t^{-7} D_sym(t). The sum of the displayed multiplicities is
14. If H != 0, R has degree 7 + deg H, with nonzero leading coefficient. Its
Laurent substitution has nonzero terms of degrees +/- (7 + deg H). Adding 1
cannot change these extremes, proving (2).

Conversely, every expression (1) with integral H is reciprocal and satisfies
all the displayed polynomial gates. This converse is only algebraic; it does
not manufacture a strong inversion.

## 3. Sharpness at the level of the gates

H = 1 gives the nonconstant formal polynomial

    J_* = t^7 + t^-7 - t^5 - t^-5 + t^4 + t^-4
          - t^3 - t^-3 + t + t^-1 - 1.

It has span 14 and satisfies all the hypotheses expressed as polynomial
conditions. Hence these gates alone cannot improve (2). In particular, the
span-13 doubly gated near misses in engine B cannot be exactly reciprocal;
they do not contradict the span-14 bound in this subclass.

## 4. Moments and arbitrary formal depth

Reciprocity gives J(-e^h) = J(-e^-h), so all odd moments M_{2r+1} vanish.
Since z(-e^h) = -2 cosh h = -2 - h^2 + O(h^4),

    P(z(-e^h)) = -120 h^4 + O(h^6),
    M_4 = -2880 H(-2).                                    (3)

The sign and constant are fixed by evaluating the non-(z+2)^2 factors at -2:
(-4)(-2)(-3)(5) = -120. Thus M_0 = 1, M_1 = M_2 = M_3 = 0 and M_4 is divisible
by 2880 in this gated reciprocal class. For H = 1, an independent integer
Laurent-coefficient evaluation gives M_4 = -2880 and M_6 = -194400.

More generally, taking H = (z + 2)^r gives first nonzero formal moment at order
4 + 2r, for every r >= 0. Its leading h coefficient is -120(-1)^r. This is
another direct reason the stated gates and symmetry alone provide no fixed
finite-jet detector. Again these are formal polynomials, not realized examples.

At the positive root, z(e^h) = 2 + h^2 + O(h^4), and the other factors in P
have value 32 at z = 2. Hence

    J(e^h) = 1 + 32 H(2) h^2 + O(h^4).

In particular J'(1) = 0 (the banked derivative/linking identity therefore
gives j = 0, independently of the choice of inverse-variable sign), and
the second logarithmic moment at +1 is 64 H(2).

## 5. Which mirror constructions are already excluded

For a compatible equivariant sum with the reflected inversion, TH-J-FACTORS
gives J_sum = J_0(t) J_0(t^{-1}). If this product is 1, J_0 is a unit in
Z[t,t^{-1}]; the preferred congruence J_0 = 1 modulo delta^2 forces that unit
to be 1. Therefore mirror doubling by equivariant connected sum cannot turn a
nonflat factor into a flat inversion. The same argument applies to any proposed
construction whose polynomial is proved to factor in precisely this way.

It does not apply merely because a prime theta-curve has a mirror symmetry.
Reciprocity is an equality between a polynomial and its reflected polynomial;
it is not a factorization as a product with its reflection. A prime symmetric
construction remains a legitimate target, provided its symmetry and preferred
normalization are established. None of ROOTS, FT, the fifth-root gate or
TH-J-FACTORS excludes that whole class.
