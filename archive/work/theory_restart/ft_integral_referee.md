# FT at minus one: a regular reduced-axis model

16 November 2026. Referee of Claude210856, item 5. No search over examples.
Exact local checks: `referee_checks/ft_local.py`.

## Verdict

**The equivariant finite-type assertion has a direct proof.** The needed local
model is a ramified, self-dual lattice in the ordinary generic sl2 modules,
not the Jones--Wenzl projector lattice at delta=0. In this lattice the
color-two crossing is an honest super flip at the special point; the mixed
full twist is regular and its difference from its inverse has a full factor
`t+1`. The theta invariant is evaluated as a reduced endomorphism of the
axis module. One never divides a trace by the vanishing axis dimension.

This proves the crossing-change filtration assertion for the two specified
moves, and hence the order bound on every moment. It does not prove that a
nontrivial inversion has a nonzero moment. The latter is precisely the old
nonflatness question, now with an identified finite-type tower.

The representation conventions below invert the handedness of the generic
color-two eigenvalues in the incoming letter. Replacing each crossing by its
inverse changes neither the divisibility nor the asserted order.

## 1. The lattice and regular duality

Set `t=q^2=-exp(h)`, `q=i exp(h/2)`, and adjoin `s` with

    s^2=[2]=q+q^-1.

Work over the complete ramified DVR O'=C[[s]], with O=C[[h]]. Since
`[2]=ih+O(h^3)`, the ideals `(h)` and `(s^2)` agree in O'. Quantum powers
`q^(1/2)` used in mixed crossings are analytic units after choosing a branch.
Write `d=[3]=q^2+1+q^-2`; its value at h=0 is -1, so it is a unit.

Use the standard generic U_q(sl2) modules, in the following bases:

    V1: u+,u-; weights 1,-1;
        E u-=u+, F u+=u-.
    V2: w0,w1,w2; weights 2,0,-2;
        E w1=s w0, E w2=s w1,
        F w0=s w1, F w1=s w2.

K acts by q to the weight. The coproduct convention is

    Delta(E)=E tensor K+1 tensor E,
    Delta(F)=F tensor 1+K^-1 tensor F.

The quantum-group relations hold because s^2=[2]. This is the symmetric
basis of the generic color-two module; compared with its divided-power
basis, the middle basis vector is divided by sqrt([2]). The basis change is
singular at the root, but the displayed structure maps are integral in O'.

All cup/cap maps can be chosen regular. Explicitly, for V2 the coevaluation
and evaluation are

    coev(1)=q^2 w0 w2-q^2 w1 w1+w2 w0,
    ev(w0 w2)=1, ev(w1 w1)=-q^-2, ev(w2 w0)=q^-2,

with every other evaluation zero. The coefficient matrix of ev is the
inverse of that of coev, so both snake identities hold. Direct use of the
coproduct checks E- and F-invariance. Their closed circle is d=[3]. V1 has
the same usual regular two-dimensional duality (its circle is [2], which
can vanish without a pole in its cups or caps). Pivotal adjustments are
monomial q-units and regular.

## 2. Regular trivalent vertices, with no axis trace denominator

The color-one fusion summand of V1 tensor V2 admits the following explicit
inclusion i and retraction p:

    i(u+)=q^2 u+ w1-s u- w0,
    i(u-)=-u- w1+q s u+ w2;

    p(u+ w1)=u+/d,       p(u- w0)=-q^-1 s u+/d,
    p(u- w1)=-q^-2 u-/d, p(u+ w2)=s u-/d,
    p(u+ w0)=p(u- w2)=0.

Both are U_q(sl2) intertwiners and `p i=Id`. These are exact identities;
the attached script checks E, F, and the product independently. At s=0,

    i(u)=-u tensor w1,  p(u tensor w1)=-u.

Thus the vertices themselves have no singularity in this lattice. Their
only displayed denominator is [3], a unit at the point in question.

Present the unknot axis as a vertical strand, cut it away from the two theta
vertices, and use i,p for those vertices. The other edge is the connected
color-two arc. A diagram gives an endomorphism of V1. Its matrix commutes with E1 and
F1, which directly forces it to be scalar over O' (no generic
semisimplicity is needed). Hence that scalar is regular: read a diagonal entry. **Do not obtain it by taking quantum trace
and dividing by [2].**

Generically this scalar is the normalized colored-theta skein invariant:
trivalent intertwiner spaces are one-dimensional, and normalization by
`p i=Id` makes the trivial theta equal to 1. Bending the same maps gives the
marked fusion coordinate used in TH-2BR and Theorem N. Consequently the
scalar differs from the preferred J only by its usual framing unit. Generic
fusion/vertex conventions may be compared with Masbaum--Vogel, *3-valent
graphs and the Kauffman bracket*, Pacific J. Math.164 (1994),361--381,
Sections1--2 and Theorem3:
https://msp.org/pjm/1994/164-2/pjm-v164-n2-p07-p.pdf.
Here the regularity and divisibility claims do not rely on specializing a
semisimple recoupling formula: they are verified on the matrices below.

## 3. Off-axis crossing changes

In these modules use the ordinary finite universal-R formula

    R_ab = D_ab sum_{n=0}^{min(a,b)}
      q^{n(n-1)/2}(q-q^-1)^n/[n]! (E^n tensor F^n),
    D_ab(v tensor w)=q^{wt(v)wt(w)/2} v tensor w,

and braid B_ab=flip R_ab. For a=b=2, the n=1 term contains s^2=[2], and the
n=2 term contains s^4/[2]!=[2]. Therefore every entry of B_22 is in the
unramified ring O, and the two nonconstant terms are divisible by h.

Modulo h, D_22 is -1 when both factors are w0 or w2, and +1 otherwise.
Hence B_22 is exactly the super flip for

    w1 even; w0,w2 odd.

Its square is identity. The inverse is regular (its determinant is a unit),
and therefore

    B_22-B_22^-1 in h End_O(V2 tensor V2).

This is the missing integral statement for one off-axis equivariant crossing
change. It proves a full h factor, not merely one factor of the ramification
parameter s. The generic eigenvalues are q^-4,-q^-2,q^2, of multiplicities
1,3,5. At the root these are +1,+1,-1; the lattice computation is essential
because the divided-power lattice can instead retain a nilpotent part.

## 4. On-axis crossing changes

The mixed braidings B_12,B_21 are regular over O': their sums stop at n=1,
and the n=1 term contains s, with no denominator. Put T=B_21 B_12. The exact
matrix identity is

    (T-q^-4 I)(T-q^2 I)=0.

One can verify this directly with the attached six-dimensional matrices.
Equivalently, generic fusion has channels1,3 and these two eigenvalues;
the cleared identity extends to the whole regular lattice. It gives

    T-T^-1=(1+t)T-(t^-1+t^2)I
           =(t+1){T-(t-1+t^-1)I}.

Thus replacing the full mixed twist by its inverse gives a full factor h,
although T itself has entries in the ramified ring. In the inverse convention
of the question the formula is

    T-T^-1=((t+1)/t)T-(t^3+1)/t^2 I.

Again both coefficients are divisible by t+1. A single mixed half-crossing
is not being claimed to have this property: the move is exactly the specified
full axis--arc twist versus its inverse.

## 5. Cubes, raw value at the root, and preferred normalization

Choose m disjoint marked move balls. Expand the alternating sum of the raw
reduced-axis diagram by multilinearity. At every ball it inserts one of the
two differences above. Every other crossing, cup, cap, and vertex is regular
over O'. Hence the resulting scalar is divisible by h^m in O'. The scalar
is unramified: changing s to -s is conjugation on V2 by
`C=diag(-1,1,-1)`, compatible with R, duality, i, and p; all internal C's
cancel. Therefore it lies in h^m O.

The raw scalar F has F(0)=1 for every actual connected theta edge. To see this
directly, i forces the color-two state w1 at its endpoint. The root crossings
are super permutations and preserve state labels along the single arc.
Mixed crossings act as 1 on w1. At q=i the w1 cup and cap entries are both 1,
and the two vertex signs -1 cancel. Thus the unique contributing assignment
along that connected edge has value 1. No trace division or assertion that
full-twist crossing changes trivialize every theta graph is needed.

Write F=1+f1 h+f2 h^2+... . The cube result says f_k has equivariant finite-type
order at most k. Preferred framing may be handled without guessing the
framing exponent from the halfword. The banked normalization J(-1)=1 and
`J'(-1)=0` uniquely selects a signed Laurent monomial from F. In the h
coordinate this is

    J=exp(-f1 h) F.

Indeed F differs generically from preferred J by the existing framing
monomial, whose value is1 at h=0 and whose linear exponent is f1. A product
of finite-type invariants of orders a,b has order at most a+b (expand its
cube difference by the discrete product rule). Consequently the coefficient
of h^k in exp(-f1 h)F is of order at most k: every summand is a constant times
f1^r f_{k-r}. This removes the normalization issue rather than assuming an
independent choice of framing at each cube vertex is harmless.

Finally, J is an integral Laurent polynomial in t. Vanishing to order m at
t=-1 implies divisibility by the monic polynomial (t+1)^m in Z[t,t^-1]. Thus

    sum_{S subset {1,...,m}} (-1)^|S| J(T_S)
       is divisible by (t+1)^m.

The desired moments k![h^k]J(-e^h) are equivariant finite-type invariants of
order at most k for exactly the two specified moves.

## 6. Scope of the super interpretation and remaining work

The special fiber really supplies a 1|2 super flip on the color-two module.
This is a concrete local statement, not merely a count of its eigenvalues.
It does not by itself identify the entire reduced-axis theory with a
classical osp(1|2) invariant. The rank-two axis, its mixed monodromy and its
reduced evaluation are additional data; identifying their quantum-supergroup
meaning needs a separate comparison.

There is also a rigorous on-axis-only improvement, obtained from the symbol,
not from an isolated-chord assertion. In the conventions of section4,

    ((T-T^-1)/h)|_0 = -T_0-3I.

On the middle state w1, T_0=1, so changing the raw full twist changes f1 by
-4. On a marked cube, f1 is affine, so distribute its exponential framing
correction among the marked balls. The normalized principal difference is

    (-T_0-3I)-(-4)T_0 = 3(T_0-I).

It annihilates the middle state and acts by -6 on the odd states. If every
marked ball is on-axis, all other maps in the principal-order contraction
are root maps, which preserve labels along the single arc forced to be w1
at its vertices. The contraction is therefore zero. Thus, for m>=1,

    Delta_axis^m J is divisible by (t+1)^(m+1),
    Delta_axis^m M_m=0.

This is the precise observed one-term-type vanishing. No corresponding
mixed improvement is asserted: an off-axis principal insertion can create
odd state pairs from w1 tensor w1.

Finally the tower's completeness is precisely J!=1: a Laurent polynomial is
1 iff every nonconstant Taylor coefficient at -1 vanishes. The new result
explains the filtration and gives a finite-dimensional local model for its
weight systems. It does not add a theorem of nonvanishing on the a2-zero core.

## 7. A noncommuting local symbol, with limited scope

The same fixed matrix certificate computes the off-axis principal operator
`C22=((B22-B22^-1)/h)|_0`. It satisfies

    C22(w1 tensor w1)=-2 w0 tensor w2+2 w2 tensor w0.

If Qodd projects V2 onto span(w0,w2), then

    [Qodd tensor I,C22](w1 tensor w1)
       =-2 w0 tensor w2+2 w2 tensor w0 != 0.

Together with the normalized axis symbol -6 Qodd, this gives an explicitly
noncommutative local symbol calculus. It explains why axis-only leading
symbols vanish while mixed symbols can survive. It does not prove that the
contracted theta invariants distinguish nonabelian geometry, or identify the
empirical order-three invariant iota. The fixed certificate now has26assertions
and an accompanying `ft_local.json`; every assertion passes.
