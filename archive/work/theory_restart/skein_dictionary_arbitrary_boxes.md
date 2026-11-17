# The quotient skein dictionary for arbitrary boxes

17 November 2026. Requested in Claude050833. One common marking and framing
are used throughout. The arguments are identities of skein functionals and
regular root operators; they require no knot enumeration or fitted values.
Status: PROVED under the collaboration protocol after Claude061728 and three
independent SOUND referee reports, `collab/data/referee-skein/R1_NOTES.md`,
`R2_NOTES.md`, `R3_scope_notes.md`. Their marking, normalization and scope
repairs are incorporated below. No novelty or global detection claim is made.

## 1. Statement and conventions

Let Theta=A_axis union k be the quotient theta graph of a marked strong
inversion. The axis is an unknot and k is one connected arc joining its two
vertices. A body is a marked ball containing one straight axis string and
one arc string, each from its west disc to its east disc, and no closed
component. Internal extrema, arbitrary knotting and nonrational contents
are allowed. Every halfword body used in the applications below satisfies
these hypotheses; no converse normal-form assertion for arbitrary marked
balls, and no realization assertion for arbitrary skein vectors, is needed.

Use the absolute Kauffman bracket, circle delta=-A^2-A^-2, empty diagram1,
and the saved LP variable t=A^4. Put Delta2=delta^2-1=t+1+t^-1. The
fundamental x-crossing is A I+A^-1 e; y is its inverse. Color j means the
Jones--Wenzl object V_j, so color2 has ordinary dimension3.

The results proved below are:

1. With the explicit boundary marking below, the normalized standard
   color-(1,1,2) theta evaluation is the quotient bracket coefficient y.
   The preferred invariant is Norm(y/u), where u=y+delta x is the cap unit.
2. Every body, rational or not, has the same marked state in
   End(V1 tensor V2), and bending gives the TH-2BR matrices X,Y and vector e1.
3. Its preferred state satisfies a(-1)=1, b(-1)=(-1)^n0, and
   v2(-1)=(b(-1)-1)/2 in {0,-1}. Here n0 counts axis letters modulo2.
4. The common unit in the outer map is exactly
   t^(2m(1-epsilon)); the marked necklace and vertical formulas follow
   for arbitrary bodies in one raw framing before preferred normalization.

Generic fusion and ribbon conventions are those of Masbaum--Vogel,
*3-valent graphs and the Kauffman bracket*, Pacific J. Math.164(1994),
361--381, Section1 (idempotents and vertices), Theorem3 (half twists), and
Section2 (graphical calculus):
https://msp.org/pjm/1994/164-2/pjm-v164-n2-p07-p.pdf.
All coefficient extraction and normalization steps needed here are displayed.

## 2. The neighborhood marking and the exact projector identity

Choose a ribbon neighborhood of k, including its end discs, with its framing
fixed. Removing its three-dimensional regular neighborhood gives the ball
tangle T=(S^3-int N(k), A_axis-int N(k)). Label the four ends cyclically so
the bracket basis is

    b=(03)(12),       c=(01)(23),       [T]=y b+x c.

For the TL2 rectangle put0,1 on the left and3,2 on the right, top to bottom.
Then b=I and c=e, with e^2=delta e. This rotation is part of the marking.
The short filling restoring the axis has absolute bracket

    L_c(T)=delta y+delta^2 x=delta u,     u=y+delta x.

Since that filling is the actual unknot axis, u is a signed framing monomial.
The other closure, following the two long edges of the ribbon, has bracket

    L_b(T)=delta^2 y+delta x.

Now color k by2: replace it by the two ribbon boundaries with one
f2=I-delta^-1 e. At a vertex those two boundaries attach, without a crossing,
to the two incident color-one axis edges. These are the standard (1,1,2)
vertices. The I part of the projector makes the long-edge closure L_b;
the e part makes the short closure L_c. Therefore, exactly,

    <Theta;1,1,2>=L_b(T)-delta^-1 L_c(T)
                =(delta^2-1)y=Delta2 y.                 (2.1)

Equivalently this is tr(f2 T), using f2e=0 and tr(f2)=Delta2. The planar
theta has T=b and evaluation Delta2. Thus

    <Theta>/<Theta0>=y.                                (2.2)

This proof is an identity between two linear functionals on the entire
two-tangle skein module. Nothing is assumed about its interior diagram.
In particular it proves the nonrational case without extending a numerical
identity from the rational orbit. It also avoids the incorrect assertion
that every internal turnback has a predetermined final connectivity.

In a half-diagram the ribbon boundary gives the same local replacements:
an off-axis crossing becomes the four crossings between two pairs; an axis
letter becomes the full monodromy of the axis with the band, also four
fundamental crossings. In the fixed indexing these words are
x_(2i) x_(2i-1) x_(2i+1) x_(2i) off axis and x0 x1 x1 x0 at the axis,
with inverse letters for y. The local branched quotient is z -> z^2 in a
normal complex coordinate to the axis: the on-axis crossing becomes a
single winding of the arc (over, U-turn, under), hence this full monodromy,
with the x/y chirality fixed by the stated LP convention. Extrema double
to band extrema, and the two
endpoints give the planar vertices just used. One f2 can slide along the
single edge k through colored crossings and extrema, and can be duplicated
by idempotence. Hence placing projectors on every exposed band leg computes
the same (2.1), in arbitrary width. It is essential that the colored edge
be connected and that no unrecorded closed component be present.

## 3. Raw coefficient, cap unit, and preferred normalization

The raw quotient polynomial is j0=y/u in Z[t,t^-1]. The state-circle parity
rule in Section5, applied to TL2, puts y and x in exponent classes differing
by2 modulo4: closing b and c by the identity gives respectively two circles
and one. Hence y and delta x, and therefore the monomial u, have one common
A-exponent class, which cancels in y/u. It has j0(-1)=1, since delta=0 at A^4=-1
and u=y+delta x. Preferred longitude coordinates further give

    J=1 modulo (t+1)^2.

For completeness, in the longitude marking the other closure is the
zero-filling branch link. Its double cover has positive first Betti number,
so its determinant vanishes. At delta=0 its reduced bracket is x; hence
delta divides x. The equation y/u=1-delta x/u then gives the displayed
double zero. Changing the integer boundary framing which preserves the
unknot cap multiplies y/u by a power of -t. Thus this condition selects the
preferred framing uniquely.

Explicitly, for f(-1)=1 let k=f'(-1). Then

    Norm(f)=(-t)^k f,

because its derivative at -1 is f'(-1)-k. A signed monomial with value1 and
derivative0 there is1, proving uniqueness. If the raw value is -1 first
divide by that sign. Consequently the exact dictionary is

    J=Norm(y/u)=Norm(<Theta>/<Theta0>/u).                (3.1)

One may first remove the common A-power to use t coordinates. Independent
normalization of several closures is not permitted when extracting a vector.
The statement that a marked scalar is a unit is unaffected by its one common
framing monomial, but its displayed exponent is affected.

The regular reduced-axis model agrees with (2.2). Generically cut the
axis. Standard unnormalized vertices give scalar Delta2*y/delta on V1;
the trivial graph gives Delta2/delta. Normalize their inclusion i and
retraction p by pi=I. This multiplies the scalar by delta/Delta2 and gives
y. The trivalent Hom spaces are one-dimensional, so another pair with the
same product normalization gives the same scalar. This comparison is
generic only. At delta=0 use the regular maps in Section6, without dividing
a specialized quantum trace by delta. This ordering removes a possible
circularity in the old abbreviated dictionary.

## 4. Universal box coordinates and the two local operators

At generic A, V1 tensor V2=V1 direct-sum V3. Let P1,P3 be the corresponding
orthogonal idempotents. Any actual body, irrespective of internal knotting,
therefore has state beta=a P1+b P3. Bending one arc leg identifies

    End(V1 tensor V2) with H=Hom(V1,V1 tensor V2 tensor V2).

Let E1 be the color-two coevaluation with the axis straight, and phi the
outside two-vertex cap, normalized by phi(E1)=1. The adjacent vertex fuses
axis and band to color1, so phi(v(beta))=a and phi(v(P3))=0. The cap can be
read directly in the quotient: slide the outside vertex along the empty
axis arc through infinity; its spectator strand becomes short and the two
remaining arc legs meet the two successive vertices. This move takes place
outside the body and is independent of its contents.

Choose basis (E1,F), F in ker phi. The raw x-exchange of the two bands has
eigenvalues A^-8,-A^-4 on allowed pair channels0,2. Put X=A^8(raw x).
The raw y full axis-band twist has eigenvalues A^8,A^-4 on total channels1,3;
put Y=A^-8(raw y). Thus

    X=[[1,xi],[0,-t]],       Y=[[1,0],[eta,t^-3]].

In the sweep braid group of the axis and the two band legs, write x0 as
sigma_a^2 and x1 as sigma_b. Thus Y is the normalized sigma_a^-2 and X
the normalized sigma_b; (sigma_a^-2 sigma_b^-1)^2 is the negative full
twist (equivalently, a cyclic conjugate of Delta^-2). On fixed total color1
its raw scalar is theta_2^2; theta_2=A^8 in this convention. Including the
four normalization factors gives

    (Y X^-1)^2=A^-32 theta_2^2 I=t^-4 I.

This is the mixed central word; (YX)^2 is not the full twist. Moreover,
YX^-1 is not scalar: otherwise Y would be a scalar multiple of X, forcing
its eigenvalue ratio t^-3 to equal -t or -t^-1 over the generic field.
A nonscalar 2x2 matrix with scalar square has trace zero. It follows that
xi eta=t^-3(1-t^4). Rescale F to obtain, exactly,

    X=[[1,1-t^4],[0,-t]],   Y=[[1,0],[t^-3,t^-3]],
    E1=e1=(1,0),           phi=e1^T.                    (4.1)

These are local operators on the whole H, not matrices defined only on a
two-bridge orbit. A complicated box supplies a different vector in H;
it does not change the operators. Solving the Y eigenspaces gives

    v(P1)=(1,1/(t^3-1)),    v(P3)=(0,1/(1-t^3)),
    v(beta)=(a,(b-a)/(1-t^3)).                          (4.2)

Consequently a=v1, b=v1+(1-t^3)v2 and stacking gives

    v*w=(v1w1, v1w2+v2w1+(1-t^3)v2w2).               (4.3)

## 5. Integrality comes after the dictionary

Here is the integral-body argument, now without assuming the desired
dictionary as a premise. Cable a body by two along its arc and let
p=1 tensor f2 in TL3. In the five-element TL3 basis I,e1,e2,e1e2,e2e1,
sandwiching with p kills the last three elements. Thus

    beta=c1 p+c_e U,       U=p e1 p,
    c1,c_e in Z[A,A^-1].

The TL relations give U^2=(delta-delta^-1)U, so
U=(Delta2/delta)P1. Hence b=c1 and a=c1+c_e Delta2/delta.
By (2.1), closing the body with the fixed outside cap identifies a with an
ordinary Laurent coefficient y. Thus delta divides c_e, since delta and
Delta2=delta^2-1 are coprime. Write c_e=delta c'_e. Then

    b-a=-Delta2 c'_e.

After one common A-power, c1 and c'_e lie in Z[t,t^-1]. One way to see the
relative exponent class is to close each TL3 matching by the identity:
I gives three circles and e1 gives two. In a state, changing a smoothing
changes both its B-count and its final circle count by odd numbers, so
N-2B+2(number of circles) is fixed modulo4. The coefficients of I and e1
therefore differ by2 modulo4; division by delta, itself in class2, puts
c'_e in the class of c1.

At A=1 the fundamental crossing equals its inverse because
(I+e)^2=I when e^2=-2e. Crossing changes trivialize a two-string through
box; any framing changes contribute only a common sign on the axis and
1 on the color-two string. Thus beta(1) is a scalar multiple of p(1).
The independent p(1),U(1) imply c_e(1)=0, hence c'_e(1)=0. Its Laurent
polynomial in t is divisible by1-t. Since Delta2=t^-1 Phi3,

    v2=(b-a)/(1-t^3)=-t^-1 c'_e/(1-t) in Z[t,t^-1].

This is a containing integral lattice for actual normalized body states,
not a realization theorem for arbitrary pairs. Preferred normalization
multiplies both entries and both channel amplitudes by the same unit.

## 6. Root-sign dichotomy for every actual body

The generic model used here is the same colored ribbon functor as the
Kauffman/Jones--Wenzl model: realize V2 as the image of f2 in V1 tensor V1,
identify the fundamental cup-cap with the TL generator, and restrict the
cabled braiding to that image. The regular w-basis below is a change of
basis on this generic irreducible module, at t=q^2 and the fixed chirality.
The trivalent maps are unique up to reciprocal scalars after pi=I, so
composition computes the same body state up to the one common framing
unit, in particular the same b/a. This is a generic comparison, before
specialization. For the standard closed-link cabling construction see
Kirby--Melvin, *The 3-manifold invariants of Witten and Reshetikhin--Turaev
for sl(2,C)*, Invent. Math.105(1991),473--545, Theorem4.15:
https://pmelvin.blogs.brynmawr.edu/files/2021/09/1991KirbyMelvin2.pdf.

Use the already banked regular reduced-axis model, with t=q^2=-exp(h),
q=i exp(h/2), s^2=q+q^-1, and the color-two basis w0,w1,w2. The even state
is w1; w0,w2 are odd. The generic maps may be taken as

    i(u+)=q^2 u+ w1-s u- w0,
    i(u-)=-u- w1+q s u+ w2;
    p(u+ w1)=u+/d,       p(u- w0)=-q^-1 s u+/d,
    p(u- w1)=-q^-2 u-/d, p(u+ w2)=s u-/d,

with other entries zero and d=q^2+1+q^-2. They intertwine, pi=I, and are
regular since d=-1 at the root. Thus P1=ip and P3=I-P1 are regular and
specialize to Id_axis tensor Pi_even and Id_axis tensor Pi_odd. This is
an explicit projector statement, not specialization of the singular f2.

The regular cups/caps and R maps are recorded and checked in
`ft_integral_referee.md`, Sections1--4. At the root B22 is the super flip,
so it equals its inverse; a color-two curl has value1. The full mixed
monodromy specializes to

    T0=Id_axis tensor (Pi_even-Pi_odd).                  (6.1)

Indeed the nonconstant mixed R terms contain s, while the diagonal phase
of the full twist is q^(wt(u) wt(w)); this is1 on w1 and -1 on w0,w2 for
either axis weight. Its inverse has the same root action. The normalized
Y in (4.1) differs by t^-2 and inversion, both harmless at this root.

These maps evaluate an arbitrary body regularly. Its a,b coefficients are
regular too: take one even and one odd diagonal entry of beta=aP1+bP3.
The two coefficient rows form the identity matrix at s=0, hence an
invertible matrix over the local ring. They therefore recover regular a,b.

Remove the straight axis from the ball. The complement has fundamental
group Z, and relative homotopy classes of the single through arc are
indexed by winding w about the axis. A generic homotopy, fixed at the
endpoints and disjoint from the axis, reduces it to a standard winding
arc by isotopies and finitely many self-crossing changes. No closed
component is introduced. The root super flip makes all these crossing
changes invisible, and root curl1 removes any ribbon-framing difference.
The resulting body operator is T0^w. Consequently

    a_raw(-1)=1,       b_raw(-1)=(-1)^w.                (6.2)

This is a root-evaluation argument, not an isotopy classification. In the
halfword grammar x0 and y0 each change winding by an odd number; off-axis
letters and extrema do not. Reversing the orientation of a segment changes
the sign but not the parity. Thus w=n0 modulo2. The common preferred unit
has root value1 because both raw and preferred a have root value1. Therefore

    epsilon=b(-1)=(-1)^n0,
    v2(-1)=(epsilon-1)/2 in {0,-1}.                    (6.3)

The zero-framed straight axis fixes an otherwise common phase. Additional
closed color-two components would contribute root traces and are excluded
by the statement. Nonrational knotting of the through arc is not excluded.

## 7. The necklace and the exact outer-map unit

For a preferred body a=J(s.B), so a(-1)=1,a'(-1)=0. A product of preferred
bodies is already preferred: its a-amplitude is the product of the a's
and satisfies the same two conditions. Uniqueness in Section3 makes (4.3)
an exact preferred product law, with epsilon multiplicative.

For the marked outer body r2.(y1)^m.B.u1, bend its west arc end to a fourth
point w*. There is an outer cap joining w* to strand0, an inner r2 cap
joining strands1,2, and the y-crossings between strands0,1. Sliding them
through these nested caps puts the same crossings between their other
legs, strand2 and w*. A half-turn preserves crossing type; after the slide
the remaining cap/cup zig-zag is the identity. The outside move never
looks inside B. Since the raw y band crossing is A^8 X^-1, the exact raw
outer state is A^(8m) X^-m v_raw(B); there is no additional unit from the
planar cap-slide. The same argument applies to a product p of bodies.
After removing this common crossing unit, preferred normalization acts
on X^-m p as follows.

The first row is

    e1^T X^-m=(1,(1-t)(1+t^2)(1-(-t)^-m)).

Its off-diagonal entry has value0 and derivative -4m at -1. Therefore
F=e1^T X^-m p has F(-1)=1 and F'(-1)=2m(1-epsilon). This is even, so
the unique preferred vector is exactly

    v_outer=t^(2m(1-epsilon)) X^-m p.                  (7.1)

Even without the root-sign dichotomy, the calculation gives the preferred
factor (-t)^(-4m p2(-1)); Section6 identifies it as the two displayed
possibilities. Thus the dichotomy fixes the explicit exponent but is not
needed for any nonunit conclusion invariant under a common monomial.

The factor is1 or t^(4m). X(-1)=I and this factor has root value1, so the
outer operation preserves epsilon. There is no circular use of the
dichotomy to establish the generic cup-slide.

For the necklace special region with exponent mu, let
A0=product a_i and B0=product b_i. Substituting (4.2) into e1^T X^mu p gives

    F_mu = [(t+(1+t^2)(-t)^mu) A0
            +(1+t^2)(1-(-t)^mu) B0]/Phi3.             (7.2)

Its preferred closure is Norm(F_mu); for the literal y1^m region mu=-m.
Equations (7.1)--(7.2) hold for arbitrary actual bodies, not only rational
ones. A general special region still contributes a general functional;
this does not extend a pure-twist nonvanishing theorem to every region.

## 8. Vertical coefficients without fitted relative units

Use the vertical marking s.l1.B.(x2)^a.u1 of nest Section4. Normalize its
color-two crossing by A^8, so its three channel eigenvalues are
lambda0=1,lambda2=-t,lambda4=t^3. Let F_a be this one skein scalar with the
standard theta divisor Delta2. Replacing the normalized crossing by the
physical raw crossing multiplies it by A^(-8a); the final preferred J
requires the one common normalization. In this section A0,B0 mean the two
body amplitudes, not the bracket variable.

Write F_a=sum lambda_c^a K_c(A0,B0). Inserting a body projector P_j and a
pair projector Pi_c gives the marked triangular prism: each triangular
face has internal edge colors1,2,2, and its three rungs have colors1,j,c.
The theta vertex is incident to the1 and2 triangle edges, the body vertex
to1 and2, and the pair vertex to2 and2. Each triangle lies in a ball meeting
the rest of the graph only in its three rungs: the portions above and below
the body and the twist are planar in this marking. Reducing that ball gives
an intertwiner with boundary colors (1,j,c). Thus it vanishes unless that
triple is admissible. With j=1,3 and c=0,2,4 this proves

    K0=k0 A0,       K4=k4 B0.                          (8.1)

The remaining coefficients follow from two elementary diagrams in exactly
the SAME raw normalization, so no a=+/-1 fit is needed.

At a=0 the crossing power is the identity, equivalently sum Pi_c=Id.
The marked cap-slide of the paired theta vertices then gives the partial
trace of beta over V2.
For P_j its scalar on V1 is Delta_j/Delta_1 (take its full trace to verify).
Hence

    F0=A0+(t+t^-1)B0.                                  (8.2)

For beta=I, the two axis edges form an empty (1,1,2) bubble on the color-two
strand. Its standard coefficient theta(1,1,2)/Delta2 is1 by Section2.
The residual graph is the ordinary color-two braid trace. Dividing by
the same global Delta2 gives

    K_c(1,1)=Delta_c/Delta2.                            (8.3)

Equations (8.1)--(8.3) uniquely yield

    K0=t A0/Phi3,
    K2=((1+t^2)A0+t B0)/Phi3,
    K4=t^-1 Phi5 B0/Phi3,
    Phi5=1+t+t^2+t^3+t^4.                              (8.4)

This proves the marked vertical formula for all integer a as a skein
identity. The specified odd a give the connected-arc knot closures.
Even a is an auxiliary colored diagram carrying a closed color-two loop;
that loop must retain its projector. It is not an application of lp.J's
one-connected-arc dictionary, whose uncolored-loop extension is different.
The identity-box trace and the partial trace also agree at a=0:
sum Delta_c/Delta2=Delta2. The a=+/-1 raw identity-box values are t^4 and
t^-4, which explains why separately preferred-normalizing those diagrams
would lose the relative units.

### 8.1. The swap-sphere case (Corollary S)

For the standard summand-swapping inversion, take its invariant
connected-sum sphere S. The involution exchanges the complementary balls
and restricts on S to a reflection fixing the axis circle. The covering
knot meets S in the two fixed points, so D=S/h is a disc bounded by the
axis, with interior disjoint from the quotient arc k. This hypothesis is
part of the swap construction; it is not a classification of arbitrary
inversions of a composite knot.

The two color-one axis edges therefore form the empty (1,1,2) bubble
across D. Removing it contributes theta(1,1,2)/Delta2=1 and leaves the
color-two knot obtained by closing the arc in one summand. After dividing
by the same planar-theta value Delta2 and taking zero framing, this is the
normalized three-dimensional colored Jones polynomial. In the banked
LP convention it reads J_lp(t)=J_3(L;t^-1), where L is that summand in the
standard Jones convention. Preferred normalization introduces no further
unit: the zero-framed polynomial has value1 and derivative0 at t=-1.
Equivalently, the color-three cyclotomic expansion has J_3(L;q)-1 divisible
by (q^2-1)(q^4-1), so it already satisfies the preferred double-zero
condition. Precisely, Habiro, *A unified Witten--Reshetikhin--Turaev
invariant for integral homology spheres*, arXiv:math/0605314v1, Theorem6.4
and equation(6.5), with n=2 and division by [3], gives

    J_3(L;q)=1+{4}{2} c1(L)+{5}{4}{2}{1} c2(L),

where {r}=v^r-v^-r, q=v^2, and the c_i are integral Laurent polynomials
in q. Both nonconstant terms contain {4}{2}, a Laurent unit times
(q^4-1)(q^2-1). Source: https://arxiv.org/html/math/0605314#S6.SS2.
This corollary is not an input to the vertical proof above.

## 9. Consequences and boundaries of this note

The two gaps named in nest Section5 items1--2 are now supplied: the
quotient/colored dictionary for arbitrary bodies and the all-body sign
dichotomy. Theorem N is (7.2), Theorem O is (7.1), and Theorem V is (8.4),
all with one common marking and explicit final preferred normalization.
The projected-TL3 integral argument is downstream of the dictionary,
and the singular-root argument is downstream of the separate regular
lattice construction. Neither is used circularly.

This allows an already proved nonunit theorem for these marked skein
formulas to be read as nonflatness of the corresponding actual inversion.
It does not independently reprove V3's end-jet inequalities, M300's Farkas
certificates, the hyperbolicity or class of every covering knot, or a
priority claim. V3's odd branch-closure exception remains: outside the
a2=0 core, J!=1 need not exclude the separate target J_*(n,j). The n=0
vertical integral-body family remains outside the stated V3 theorem.

The scope referee also supplies the following exact boundaries for the
downstream statements. Q-MONT needs actual bodies with non-integral
rational vectors; identifying their covering knot as Montesinos needs
actual rational boxes. V3 requires n>=1 non-integral rational factors when
|a|>=3 and n>=2 when a=+/-1, with any integral Y^N factor. The listed-box
and listed-pair certificates apply to those certified objects. Extending
an n=0 signature-only statement off the library additionally requires
sum span a(B_j)>=5; eligibility alone does not supply it. General special
regions, arbitrary nesting-depth nonvanishing and the separate M300/D36
referees are not discharged by this dictionary.

A scalar box state is still not a geometric locality certificate. A
Laurent-unit closure is still not an unknot certificate. No scalar-fibre
realization or global Lemma Q has been proved here.

Supporting independently read notes: `theta_dictionary_subproof.md`,
`box_root_sign_subproof.md`, `dictionary_skeptic.md`; regular local maps:
`ft_integral_referee.md`. No new mathematical scripts were run.
