# Width-two root constraints and resonance certificates

17 November 2026. Theory-only answer to Claude032804, question 5.
No computation or enumeration was performed for this note.

## Verdict

There is a rigorous, useful root test for a **specified resonance equation**:
clear the joint-sector denominators, collect equal generic frequencies, and
exhibit a nonzero residue or jet of the aggregate that the resonance requires
to vanish. Two nonzero aggregates rule out a whole unit line. This applies to
the actual nine-dimensional module and needs no semisimplicity at a root.

There is also an exact matrix version of the box congruence, but its hypothesis
is substantive: the operator must act by scalar amplitudes on the specified
generic channels. Integrality then matches the amplitudes across a collision
whose projector has nonzero residue. An arbitrary braid state is not such an
operator. Neither integrality nor the minimal polynomial alone supplies a
universal scalar condition on a nine-dimensional state resembling
`b(omega)/a(omega)=1`.

No root criterion can exclude every non-axis unit line: the actual joint-annulus
line already banked in `width2_unit_line_referee.md` is a counterexample to that
unqualified conclusion. The useful target is a root obstruction to an explicit
nongeometric edge relation, after the known cap and annulus stabilizers have
been retained.

## 1. What the current C2 argument establishes

Sections 9 and 11 of `collab/data/engineC2/REPORT.md` use the following genuine
two-channel input for a box:

    a(-1)=1, b(-1)=epsilon, epsilon in {1,-1},
    a-b is divisible by 1-t^3.

At a primitive cube root omega, the second assertion implies `a(omega)=b(omega)`;
the ratio assertion additionally requires `a(omega) != 0`. For the actual
preferred boxes in C2 this follows from the banked normalization `a(1)=1`:
if the integral Laurent polynomial a vanished at omega, Phi_3 would divide a,
and evaluation at 1 would give `3 | a(1)`, a contradiction. Thus C2's
`q(omega)=1` is valid in that normalization. For a more general integral state
without this normalization, the polynomial congruence alone is the assertion
available when both amplitudes vanish.

For the particular hexagon edges in Section 9, the proposed slope is

    t^c (1+t^2)/t,  or  -t^c t(1+t^2)/Phi_5(t).

Its value at -1 has absolute value 2; the actual box has denominator
`a(-1)=1` and ratio of absolute value 1. This is a decisive contradiction to
those exact edge equations. It is not a classification of width-two edges.
The report itself labels the frequency formula as checked and leaves the
uniform statement for other special words open.

An additional scope point: a scalar bracket state `b=epsilon t^j a` is not, by
that equation alone, a topological certificate that the box is trivial or has
a local knot. Thus the rectangle branch in Section 11 needs a geometric lemma
before its scalar solutions can all be discarded. Nothing below uses that
identification.

Here omega always means a primitive **third** root. The banked ROOTS theorem
for the closed preferred invariant J includes primitive **sixth** roots, not
primitive third roots. These two assertions must not be interchanged.

## 2. The actual integral lattice and its exceptional fibers

Use `Lambda=Z[t,t^-1]`, the nine-state gauge of
`collab/data/engineB/rho2.py`, and the marked spectator plat from
`width2_marking_fusion.md`. All generator matrices are in `GL_9(Lambda)`.
Generically,

    (X-I)(X+t I)(X-t^3 I)=0,
    (Y-I)(Y-t^-3 I)=0.

The X-channel eigenvalues are `lambda_0=1, lambda_2=-t, lambda_4=t^3`.
The collisions relevant here are:

| root | colliding X channels | remaining X eigenvalue | Y relation at the root |
| --- | --- | --- | --- |
| -1 | 0,2, with eigenvalue 1 | -1 | `(Y-I)(Y+I)=0` |
| i | 2,4, with eigenvalue -i | 1 | `(Y-I)(Y-i I)=0` |
| omega | 0,4, with eigenvalue 1 | -omega | `(Y-I)^2=0` |

These are cleared polynomial identities. A repeated factor permits a
nilpotent part; it does not prove that part is present, and it does not prove
it absent. In particular the last row does not imply `Y(omega)=I`.

The regular FT lattice in `ft_integral_referee.md` proves that the color-two
crossing becomes a super flip in that lattice. It is a ramified self-dual
tensor lattice, explicitly distinguished there from the projector lattice at
delta=0. Without an integral comparison identifying the specialized
nine-state quotient, that result cannot be used to assert
`X_i(-1)^2=I` in the present quotient lattice.

There are two separate sources of poles in a generic sector calculation:

1. Recoupling projectors have denominators which vanish when their generic
   eigenvalues collide.
2. The physical closing covector on the nine-state quotient has an additional
   denominator at -1. With the engine's notation,

       phi = t^2 PHIT/(1+t)^4 = theta/(1+t)^2,
       theta := t^2 PHIT/(1+t)^2 in Lambda^9.

   The second equality uses the documented entrywise `(1+t)^2` factor of
   PHIT. The closing functional is regular on physical closed evaluations,
   but need not be integral on every vector in the chosen free lattice.

Thus one must not simply substitute a root into individual generic fusion
coefficients or into their normalized ratios.

## 3. A universal denominator for the seven joint sectors

Let `P_a^(1),P_b^(3)` be the generic projectors for X1 and X3 and put
`E_ab=P_a^(1)P_b^(3)`. Their ranks and zero sectors are banked. Fix any outside
words U,V and the marked input vector v. Set

    c_ab = phi rho(U) E_ab rho(V) v.

**Proposition 1.** The polynomial

    D0(t)=(1+t)^4 (1+t^2)^2 (1-t^3)^2

clears every c_ab, up to an irrelevant Laurent unit. It is independent of the
length and content of U,V. In particular possible pole orders are at most 4
at -1 and at most 2 at i or omega.

**Proof.** The Lagrange formulas are

    P_a = product_(b != a)(X-lambda_b I)/(lambda_a-lambda_b).

The three eigenvalue differences, up to Laurent units and signs, are
`1+t`, `1-t^3`, and `1+t^2`. Hence

    d(t) P_a is integral, d(t)=(1+t)(1+t^2)(1-t^3).

Both projectors in E_ab are cleared by d^2. The matrices rho(U),rho(V) and
v are integral. The closing covector is cleared by `(1+t)^2`, giving D0.
The claimed root orders follow from the simple zeros of the indicated
factors in characteristic zero. No assertion about a specialized eigenspace
was used. QED.

The bound is only a clearance bound. It neither says that a coefficient
actually has a pole nor that four or two derivatives always detect a nonzero
coefficient. A coefficient may vanish to arbitrarily high order after its
poles have been cleared.

## 4. The resonance test, on aggregates rather than separate sectors

For full twists at the two disjoint sites write u=t^2. The exact generic
coefficient is

    F(m,n)=c00+c02 u^n+c20 u^m+c22 u^(m+n)
           +c24 u^(m+3n)+c42 u^(3m+n)+c44 u^(3m+3n).

Index these seven terms by

    S={(0,0),(0,1),(1,0),(1,1),(1,3),(3,1),(3,3)}.

On the integer line `(m,n)=(m0,n0)+k(p,q)`, collect **equal integer slopes**:

    C_l(t)=sum_(ip+jq=l) c_ij(t) t^(2(im0+jn0)),
    F_k(t)=sum_l C_l(t) t^(2lk).

Define the Laurent-polynomial aggregates `P_l=D0 C_l`.

**Proposition 2 (unit-line criterion).** If F_k is a Laurent unit for
infinitely many integers k, exactly one C_l is nonzero and that C_l is itself
a Laurent unit. Conversely, this condition makes every F_k a Laurent unit.
Consequently two nonzero P_l with distinct l exclude a whole unit line and
leave only finitely many unit parameters on the specified line.

**Proof.** Multiply by D0. If at least two P_l are nonzero, their finite
supports, shifted by 2lk, are separated for sufficiently large positive or
negative k. The span of their sum then grows without bound. A Laurent unit
times the fixed polynomial D0 has fixed span `span(D0)`. This is impossible
for arbitrarily large |k|. With exactly one nonzero aggregate, division by
its monomial shift proves the remaining assertions. QED.

This concerns Laurent units. A preferred J-value is then obtained by the
fixed framing/root normalization; no independent sector normalizations are
permitted.

**Corollary 3 (root/jet certificate).** Let pi be any cyclotomic polynomial,
for example `t+1`, `t^2+1`, or `t^2+t+1`. If, for two distinct slopes l,l',
one has

    P_l not congruent to 0 modulo pi^r,
    P_l' not congruent to 0 modulo pi^s

for finite r,s, the specified line cannot be a whole unit line. A single
nonzero such residue or jet disproves the exact edge-cancellation equation
`C_l=0` whenever that equation is required by a proposed far-field resonance.

This is an exact finite certificate for the specified equations, not a new
scan. The test may use different roots and different jet orders for the two
aggregates. Dividing all P_l by a common power of pi before testing is harmless
and avoids a vacuous first residue. Failure to find a nonzero jet is not proof
that an aggregate vanishes.

The generic slope grouping comes first. Slopes which coincide only modulo the
order of a root must remain distinct when testing Proposition 2. Conversely,
terms of the same generic slope must be added before any test: their individual
nonvanishing says nothing about the aggregate.

### What pole cancellation looks like in root jets

Fix a root zeta and use `t=zeta exp(x)`. Suppose

    D0(zeta exp(x))=x^e(d_0+d_1 x+...), d_0 != 0,
    P_l(zeta exp(x))=sum_(j>=0) p_(l,j) x^j.

Then the numerator of F_k has coefficient of x^j equal to

    sum_l zeta^(2lk) sum_(a=0)^j (2lk)^a/a! p_(l,j-a).

Regularity of the physical F_k says this vanishes for j<e. Its value at the
root is the displayed coefficient for j=e, divided by d_0. Thus poles of
generic projectors produce polynomial factors in k, in addition to the root
phases. Keeping only the values `zeta^(2lk)` loses precisely these terms.
This is why the operation “evaluate sectors, then aggregate” can give a false
resonance conclusion.

A useful special case: if the phases `zeta^(2l)` are all distinct, regularity
of F_k for k=0,...,s-1 already implies regularity of every C_l. The associated
Vandermonde matrix is invertible over the local ring at zeta. At a collision
that argument fails, and the cleared-jet calculation is the appropriate one.

## 5. The genuine matrix analogue of a box-channel congruence

Work over the discrete valuation ring `O=Q[t,t^-1]_(pi)` with fraction field K
and residue field k. Suppose an integral matrix X has three distinct generic
eigenvalues lambda_a,lambda_b,lambda_c in O; only a,b collide modulo pi and
their difference has valuation one. Let P_a,P_b,P_c be the generic projectors.
Then P_c is integral, P_a,P_b have at most simple poles, and

    R := (pi P_a) mod pi = -(pi P_b) mod pi.

**Proposition 4 (collision congruence).** If R is nonzero and an endomorphism

    S=s_a P_a+s_b P_b+s_c P_c,  s_a,s_b,s_c in O,

is integral, then `s_a=s_b mod pi`. Conversely that congruence suffices for
integrality of S. If R=0, this argument imposes no congruence.

**Proof.** The only possible principal part of S is

    pi^-1 (s_a-s_b) R.

Since the residue field is a field and R is a nonzero matrix, the principal
part vanishes exactly when `s_a-s_b=0 mod pi`. There are no higher poles. QED.

The proof for Y is the same with only two projectors; at a cube root,
`P_3=(Y-I)/(t^-3-1)`. Nonzero `Y(omega)-I` is exactly the nonzero-residue
condition, up to a nonzero scalar. It is compatible with
`(Y(omega)-I)^2=0` and cannot be replaced by `Y(omega)=I`.

This proposition is an actual operator statement, not a purported example of
a realizable knot. It explains the type of integral order underlying the box
ring. In the two-channel box problem the marked gluing operator is scalar on
both channels and belongs to the specified integral order, which directly
gives `a-b in (1-t^3)`.

For width two there are two obstructions to applying the same sentence to an
arbitrary state:

- A state `rho(W)v` is a vector, not a scalar-on-channel commuting
  endomorphism. An outside word need not commute with the chosen twist.
  The marked bending in `width2_coordinate_answer.md` does turn it into an
  intertwiner of `V1 tensor V2^2`, but that intertwiner has two matrix-valued
  multiplicity channels. Bending therefore does not supply the missing
  scalar-on-channel/commuting hypothesis of Proposition 4.
- Even a commuting endomorphism can act non-scalarly inside generic
  multiplicity spaces. The joint ranks include two-dimensional sectors.
  The correct condition is then cancellation of matrix principal parts;
  it is not equality of two scalar ratios.

The vector identity supplied by integrality is only

    (pi P_a w) mod pi = -(pi P_b w) mod pi

for every integral vector w. This balances residues of singular projections.
It does not define, much less equate, two finite channel coordinates at the
root. The minimal polynomial alone also does not determine whether R is zero.
One must identify the integral lattice or inspect the cleared projector matrix.

Thus Proposition 4 can be useful for a marked width-two **box operator** with
a proven commuting/scalar-channel structure. It does not currently give a
class-free congruence excluding resonances of every actual plat state.

## 6. Boundary congruences that do hold for actual states

For a fixed physical knot closure let `w=rho(W)v` and let u be its common
framing unit, so `phi w=u J`. With theta from Section 2, integrality and ROOTS
give

    theta w is divisible by (1+t)^2,
    theta w-(1+t)^2 u is divisible by (1+t)^4.

After replacing w by `u^-1 w`, the second congruence has right side
`(1+t)^2`. At i the covector is regular and one similarly has
`phi(u^-1 w)=1 mod (t^2+1)`. These are boundary-specific state congruences
for actual connected-arc knot closures. They follow from the complete closed
evaluation; they do not say that each fusion component obeys the same value.

There is no assertion here that J(omega)=1. The box congruence at omega is a
different input. The complete scalar congruences also cannot isolate generic
line groups: at -1 all full-twist phases `t^(2lk)` coincide, at i they depend
only on l modulo 2, and at omega only on l modulo 3. Section 4 explains the
additional derivative information carried at collisions.

## 7. Why a universal root exclusion would be false

The banked actual template in `width2_unit_line_referee.md` has

    c00=t^5/Phi_3,
    c22=-t^5,
    c44=t^6(t^4+t^3+t^2+t+1)/Phi_3,

with all other sectors zero and `c00+c22+c44=t^8`. On `(m,n)=(k,-k)` all
three supported generic slopes are equal, so the sole aggregate is t^8.
The preferred invariant is 1 for every k. Both individual single-site
families are nonflat. The mechanism is the axis-straight summand, on which
equal pair colors are the only channels and `X1 X3^-1` acts as identity;
geometrically the opposite twists cancel along the joint annulus.

This family satisfies every necessary actual root condition. It is not an
example of a formal polynomial masquerading as a tangle. It establishes the
precise limitation: a successful root argument must reject a specified
nongeometric resonance, not every equality of sector exponents or every
non-axis unit line.

## 8. Deliverable to the main lane

The immediately usable reduction is Proposition 1 plus Corollary 3: for any
proposed edge or ray, there is a canonical exact polynomial to test, with a
uniform denominator and controlled exceptional-root clearance. The next
meaningful calculation, if commissioned, would be one targeted evaluation of
those cleared edge aggregates or their first necessary jets, together with the
marking that makes their vanishing necessary. It would decide that proposed
resonance.

What has not been proved is a universal list of geometric residue states, a
uniform jet depth detecting every nongeneric cancellation, or a no-resonance
theorem for arbitrary width-two plats. Proposition 4 identifies the additional
structure needed to transfer the successful two-channel `q(omega)=1` argument:
an integral commuting operator with controlled channel multiplicities and
nonzero collision residue. Without that structure, the scalar box proof does
not extend merely by replacing 2 by 9.
