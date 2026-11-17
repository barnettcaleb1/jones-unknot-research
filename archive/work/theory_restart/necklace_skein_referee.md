# Referee of the necklace skein calculus

16 November 2026. One bounded pass on Claude192557, checked against the now-written
`mont/proof/REPORT.md` and the topology discussion in `mont/nest/REPORT.md` under
`/Users/calebbarnett/jones-lanes/theory-restart/`. No scan or new invariant run.

## Verdict

**Theorem N is sound for the specified marked necklace and pure-twist special
region.** Its algebra is an all-word skein identity, not a numerical fit. The
formula must be stated up to one overall framing unit, or with an explicit final
normalization. For generic boxes the formal integral ring is a containing
lattice; it is not a realization theorem for every vector in that lattice.

The incoming scope “every horizontal Montesinos inversion” is too broad for the
displayed pure `X^mu` functional. A general even-denominator rational special
tangle contributes a general boundary word/function; it need not be an even
twist column. This distinction is already repaired in the newer proof/nesting
reports. The no-tie result for pure-twist necklaces cannot automatically be
applied to all such Montesinos presentations or to nested boxes.

The use of a **marked** sphere matters. A sphere meeting the theta curve in two
axis points and two arc points gives the two-dimensional space, but does not by
itself specify that the outside functional is `e_1^T X^mu`, or that several
pieces compose as the product below. The west/east pairing and common cyclic
order supply those additional data.

## 1. Generic colored skein algebra

Work over K=Q(A), t=A^-4 and delta=-A²-A^-2. Let V_j be the Jones–Wenzl color j.
The elementary fusion and bubble identities are the usual generic
Temperley–Lieb recoupling identities; a primary account is Masbaum–Vogel,
*3-valent graphs and the Kauffman bracket*, Pacific J. Math.164(1994),361–381,
Sections1–2, especially admissibility, the half-twist formula (Theorem3), and
the graphical calculus:
https://msp.org/pjm/1994/164-2/pjm-v164-n2-p07-p.pdf.

Since V_1 tensor V_2 = V_1 direct-sum V_3, multiplicity one in both channels,

    End(V_1 tensor V_2)=K P_1 direct-sum K P_3,
    P_i P_j=delta_ij P_i, P_1+P_3=I.

This is commutative. A box may contain knotted strands, crossings, and extrema:
its colored skein class is still an endomorphism and is therefore aP_1+bP_3.
Stacking west-to-east boxes composes the endomorphisms, so channel amplitudes
multiply. No geometric commutativity of the boxes is asserted: distinct
orders may give different tangles with identical skein classes.

To compare with TH-2BR, bend the V_2 strand using its coevaluation to obtain

    v(B)=(B tensor id_V2) E_1
       in H=Hom(V_1,V_1 tensor V_2 tensor V_2).

The snake identity unbends this map; it is an isomorphism. Put h_i=v(P_i).
Then h_1+h_3=E_1 and v(B)=a h_1+b h_3. The normalized mixed full twist Y acts
on these vectors with eigenvalues1,t^-3. In the already-fixed TH-2BR basis,
E_1=(1,0), phi=e_1^T, and phi kills h_3. Solving these conditions gives

    h_1=(1,1/(t³-1)),   h_3=(0,1/(1-t³)).

Consequently the channel transformation and product are exactly

    a(v)=v_1,  b(v)=v_1+(1-t³)v_2,
    v*w=(v_1w_1, v_1w_2+v_2w_1+(1-t³)v_2w_2).

This checks the sign of the b-channel without relying on any fitted example.
The Y-box sends (a,b) to (a,t^-3b). Conjugating X by the same transformation
gives the matrix in the letter:

    X_channels=(1/Phi_3) [[-t³,(1+t)(1+t²)],[t(1+t),1]],
    Phi_3=1+t+t².

These generic calculations do not assert semisimplicity after specialization
at t³=1. Clear the denominators first when taking such specializations.

## 2. The precise integral claim

For Lambda=Z[t,t^-1], the free module Lambda² with the displayed multiplication
is the algebra

    R=Lambda[s]/(s²-(1-t³)s).

The injection v -> (a(v),b(v)) identifies it with pairs satisfying
`b-a in (1-t³)Lambda`. This is a proper order in K direct-sum K; the individual
primitive projectors have denominators in this lattice.

The proof report's Proposition4.2 does give a route to integrality for actual
body states. Here is the chain with its hypotheses made explicit.

Cable the one arc strand by two and project that pair with p=1 tensor f_2.
Expand the unprojected cabled `(3,3)` tangle in the five TL_3 diagrams with
coefficients in Z[A,A^-1]. Sandwiching with p kills the three diagrams having
a cap/cup on the cable pair. Therefore

    [B]=c_1 p+c_e U,  U=p e_1 p,
    c_1,c_e in Z[A,A^-1].

U vanishes on the color-three channel. Its trace is Delta_2, so

    U=(Delta_2/delta)P_1,
    a=c_1+c_e(delta²-1)/delta,  b=c_1.

For a body whose symmetric closure is a knot, the untwisted special closure
identifies a, up to its fixed framing unit, with the already Laurent-polynomial
invariant J. Thus a is Laurent in A. Coprimality of delta and delta²-1 implies
delta divides c_e. Put c'_e=c_e/delta; then

    b-a=-(delta²-1)c'_e=-t^-1 Phi_3 c'_e.

The state-sum parity rule puts c_1 and c'_e in one common A-exponent class mod4.
One common monomial therefore puts them in Lambda.

At A=1 a fundamental crossing equals its inverse, because `(1+e)^2=1`
when e²=-2e. Crossing changes turn a through-through two-string box into the
trivial string link rel boundary; blackboard curls contribute only a scalar
sign (the color-two curl contributes1). Hence [B](1)=+/-p(1), and independence
of p(1),U(1) implies c_e(1)=0. Since delta(1)=-2, c'_e(1)=0. The corresponding
Lambda polynomial is divisible by1-t, so

    v_2=(b-a)/(1-t³)=-t^-1 c'_e/(1-t)

is in Lambda after the same common unit. This checks the nontrivial extra
factor1-t, not only divisibility by Phi_3.

The argument is for **actual bodies** with their knot closure and the required
through-through marking. Do not identify R with the set of geometrically
realizable states. Arbitrary pairs in R need not have a realizable unknot-capped
closure, need not have `a=1 mod(t+1)²`, and need not admit the preferred
normalization. Also do not describe R as the entire colored skein module over
Z[A,A^-1]: that module includes projector denominators, whereas R is this
particular integral coordinate lattice containing the normalized body states.

## 3. Special region and framing

For an arbitrary complementary ball C containing both theta vertices,
linearity gives only

    <C,B>=gamma_1(C)a(B)+gamma_3(C)b(B).

The pure-twist formula requires the marked region C_m in the halfword

    s.r2.(y1)^m.B_1...B_n.u1.

For this region, the proof report's geometric argument is adequate. The two
extra legs created by r2 pass outside every body. Slide the lower vertex along
the empty outside axis arc through infinity; read the diagram from the other
end. The bottom cup becomes E_1, the composite box acts on its inner leg, and
the upper two fusions become phi. A half-turn in three-space reverses the
box's input/output direction but fixes both channel projectors, hence leaves
its state unchanged. The m y-crossings are inverse X-crossings. Thus the
functional is, up to a scalar independent of the box,

    phi X^-m,   mu=-m.

The scalar consists of the fixed vertex normalization and crossing/ribbon
framing powers. This argument gives the sign dictionary without guessing it
from knot names or Alexander polynomials.

For every integer mu,

    e_1^T X^mu=(1,(1-t)(1+t²)(1-(-t)^mu)).

Put A=product a_i and B=product b_i. Substituting h_1,h_3 yields

    F_mu=[{t+(1+t²)(-t)^mu}A
          +(1+t²){1-(-t)^mu}B]/Phi_3.

This is the claimed necklace coefficient. It is Laurent for integral vectors;
Phi_3 divides the numerator before specialization. At mu=0 it is A, agreeing
with the equivariant connected-sum product.

The **preferred J** equals `norm(F_mu)`, where norm takes the unique overall
signed t-power making the answer1 modulo(t+1)². Such a normalization exists
for these actual framed inputs by the banked preferred-longitude theorem.
It is not automatic for an arbitrary formal vector. Writing `J=F_mu` literally
requires coordinated raw units; independently normalizing each closure can
change the displayed exponent shifts. Two raw closures determine a box vector;
two or three independently normalized closure polynomials have lost relative
framing and do not provide an automatic reconstruction theorem.

The one-parameter family regrouping is sound in raw coordinates:

    F_mu=P+Q(-t)^mu,
    P=[tA+(1+t²)B]/Phi_3,
    Q=(1+t²)(A-B)/Phi_3.

If P,Q are both nonzero, their supports separate for sufficiently positive or
negative mu, so only finitely many mu can give a monomial. Multiplying by the
preferred framing unit does not affect that assertion. This is a theorem for
the marked necklace twist site, not automatically for every internal
arc-arc crossing of an arbitrary theta graph.

## 4. Halfwords and actual Montesinos scope

A body begins with one halfstrand, ends with one halfstrand, uses only its own
positions and created strands, and closes no component. Its slab is invariant
under the half-turn. Upstairs it meets the knot in two arcs exchanged by the
involution; it contains no fixed point of the knot. Downstairs it meets the
theta curve in the straight axis segment and one arc strand, with the required
west/east marking. Hence these words genuinely give boxes, even when their
contents are nonrational.

The folding relation `v(r2.x1^m.B.u1)=X^m v(B)` is an ordinary cup-slide/snake
identity. It produces a useful recursive calculus but is not a statement that
its inputs stay within the rational two-type automaton. The newer notes already
give nested vectors violating that type law.

For rational boxes the branched-cover dictionary is particularly concrete.
Taking the double cover branched along the axis gives a rational tangle with
odd denominator; the identity lifts to slope0. The two boundary operations
lift to

    Y: s -> s+1,   X: s -> s/(2s+1),

up to the consistently chosen handedness. Their matrices generate the
appropriate Gamma_0(2) subgroup and preserve odd denominator. Conversely a
continued-fraction/Euclidean reduction gives the odd-denominator orbit. This
is a topological dictionary, not identification by Alexander polynomial alone.

Stacking boxes lifts to horizontal tangle sum. The pure special region C_m
lifts to the reciprocal even twist `1/(-2m)` in these word conventions.
Therefore the direct depth-one claim is the horizontal inversion on

    N(T_1+...+T_n+1/(-2m)),

with each T_i an odd-denominator rational tangle. It includes the stated
even-column pretzels. The sign mu=-m must be retained when translating words
to pretzel notation.

A general horizontal-axis Montesinos knot with exactly one even-denominator
tangle still gives a box chain, but its special region is generally
`e_1^T rho(W_0)`, not `e_1^T X^mu`. For example an even-denominator slope such
as3/8 is not made into a reciprocal even integer by merely moving integral
parts. More general boundary operations or nesting are needed. The proof
report itself marks its global rational-special-region dictionary separately;
the nesting report offers an argument, but it does not make the pure-twist
no-tie theorem apply to a general W_0.

Thus Theorem N is established as a marked skein formula. A nonunit theorem for
its rational inputs should be stated for that precise pure-twist family until
the more general functional/nesting analysis is separately proved. No theorem
about all equivariantly arborescent knots, or all strong inversions of a
Montesinos knot, follows merely from the state-space dimension being two.

## 5. What this actually reduces

For the specified necklace, the entire gluing problem reduces exactly to two
products A,B and one functional. The contents of the boxes can be arbitrary;
the remaining difficulty is which channel pairs actual boxes realize and how
the two contributions cancel. Rational boxes have the audited TH-2BR dynamics,
so a coefficient argument on their products is a genuine next class theorem.
The algebraic reduction is complete in this marked scope. Global knot-class
identification, preferred framing, and rational-state restrictions are the
three separate inputs that must remain visible in any application.

## 6. A useful a2-zero calibration beyond the earlier obstruction

The sign dictionary above makes two positive odd rows r,s and mu=k into the
horizontal inversion of P(2k,r,s), since m=-mu and the special column is -2m.
This can be calibrated without relying on a knot-name identification from an
Alexander polynomial.

Write r=2j+1, s=2l+1, S=j+l and t=-1+h. The exact row formulas give

    a_j=1-4j h+(2j²-8j)h²+O(h³),
    b_j=-1-(2j+3)h+(j²-4j-6)h²+O(h³).

For A=a_j a_l, B=b_j b_l one obtains

    B-A=6(S+1)h+O(h²),
    (1+t²)(1-(-t)^mu)/Phi_3=2mu h-mu(mu-1)h²+O(h³).

Thus the raw closure is F=A+c_mu(B-A), whose preferred normalization is
t^-4S F (value1 and first derivative0 at t=-1). Its second derivative is

    J''(-1)=-12[j(j+1)+l(l+1)]+24mu(S+1).

Using the banked Casson/Mullins identity a2(kappa)=-J''(-1)/24 yields

    a2(P(2k,r,s))=(r²+s²-2)/8-k(r+s)/2.

In particular P(2k,4k-1,4k+1), k>=1, has a2=0. The first is P(2,3,5),
with determinant31. This is a suitable calibration for the proposed rational
necklace nonunit theorem: its a2-zero conclusion means that the earlier a2
obstruction alone does not establish the quotient's nonflatness. The passage
from the necklace nonunit theorem to this family still uses its separately
refereed coefficient proof; this section is only the exact sign and moment
calculation.
