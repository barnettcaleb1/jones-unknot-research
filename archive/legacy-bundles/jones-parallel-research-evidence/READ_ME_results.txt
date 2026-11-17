JONES UNKNOT DETECTION: PARALLEL RESEARCH RESULTS
31 October 2026

Status: no general proof and no counterexample. Three research tracks ran
in parallel: actual tangle realization, positive statistical-mechanics
models, and symmetric geometric constructions. Their strongest deductions
were checked independently. None is claimed to be new to the literature.

The useful outcome is a stronger geometric obstruction to our formal
candidate, a precise obstruction to a class of proposed physics proofs,
and an exclusion of globally periodic rotor constructions. The remaining
construction question is smaller and explicit, but still unresolved.

1. A GEOMETRIC OBSTRUCTION REQUIRING ONLY TWO FILLINGS

Statement. Let T be an actual four-ended tangle, with the usual rational
filling coordinates. Suppose:

  T(infinity) is the actual unknot;
  T(0) has the Jones polynomial of the two-component unlink.

Let J be the knot in S^3 whose exterior is the branched double cover of T.
Then

                    a_2(J) = Delta_J''(1)/2 = 0.

Here Delta is the symmetric Alexander polynomial with Delta(1)=1; a_2 is
the integer coefficient of z^2 in the Conway polynomial. The conclusion
also holds if the second Jones identity has a signed monomial factor.
No Jones identity at any other filling is needed.

Proof. The infinity filling of the cover M is S^3. Removing the filling
solid torus identifies M with the exterior of its core J, and infinity
with the meridian. The zero branch link has determinant zero, so M(0)
has positive first Betti number. The unique such primitive slope on an
S^3 knot exterior is its preferred longitude. Thus M(0)=S^3_0(J).

Write lambda_G for the doubled Casson-Lescop normalization used by
Garoufalidis. His determinant-zero branched-cover identity gives

  i^(signature(L)+nullity(L)) lambda_G(Sigma_2(L))
          = J_L'(-1)/6 + J_L(-1) signature(L)/4.

His Jones convention has J_U2(t)=t^(1/2)+t^(-1/2). At -1 its value is
zero and its derivative has absolute value one. The phase has modulus
one. Consequently the assumed zero filling forces

                    |lambda_G(S^3_0(J))| = 1/6.

The zero-surgery formula in the same normalization is

                    lambda_G(S^3_0(J)) = 2a_2(J)-1/6.

Therefore |12a_2(J)-1|=1. Its rational solutions are 0 and 1/6;
integrality leaves only a_2(J)=0.

More generally, without any unlink-polynomial assumption, the same
calculation gives an exact identity for a longitudinal branch link L:

                    |V_L'(-1)| = |12a_2(J)-1|.

In particular its Jones polynomial has a SIMPLE root at -1: the right
side cannot vanish because a_2 is an integer. A link polynomial with a
double root there cannot occur as this longitude filling. This is an
additional necessary condition on genuine geometric quotient links.

Normalization check. In Garoufalidis's one-component integer-surgery
formula the framing-independent Alexander term is zeta(J). At framing
+1 the correction terms 1/4-1/6-1/12 cancel, identifying zeta(J)=2a_2(J)
by the Casson surgery formula. At framing zero the correction is -1/6.
This checks the normalization across first Betti numbers zero and one
inside a single surgery formula. It avoids an invalid orientation-sign
assumption for the Betti-number-one invariant. A monomial factor in the
Jones polynomial does not change the derivative's absolute value at -1,
because the polynomial itself vanishes there.

This proof connects a cancellation condition in a quantum invariant to
an integral constraint on the topology of a different knot, through its
three-dimensional branched cover. Three independent agent checks and a
parent review agreed on the marking, constants, and integrality step.

Primary formulas:
Garoufalidis, Signatures of links and finite type invariants of cyclic
branched covers, Theorem 1 and Section 4.1:
https://people.mpim-bonn.mpg.de/stavros/publications/signature.pdf
Lidman--Sivek, Quasi-alternating links with small determinant, Eq. (2.1):
https://www.ma.imperial.ac.uk/~ssivek/papers/smalldeterminant.pdf
Kerler, p-Modular TQFT's, Milnor torsion and the Casson-Lescop invariant,
Lemma 2, independently confirms the undoubled zero-surgery normalization:
https://msp.org/gtm/2002/04/gtm-2002-04-009p.pdf

2. WHAT THE OBSTRUCTION ACTUALLY ELIMINATES

Our earlier formal tangle object has one rational curve r_1(0) and four
special curves s_4(infinity), with grading shifts arranged to cancel in
the Jones polynomial. If geometrically realizable, its infinity closure
would be the unknot and a slope-one closure would have Jones polynomial
one but reduced Khovanov rank 17. That would be a counterexample.

The new lemma is a necessary condition on its ACTUAL cover companion.
It rules out all four prime companions through nine crossings listed by
Kotelskiy--Watson--Zibrowius with the desired ungraded curve pattern:

    companion / inversion          a_2
    6_1                            -2
    8_20                           +2
    9_42                           -2
    9_46, first inversion          -2

These numbers were computed from actual diagrams and independently from
Seifert matrices. This excludes the four companions, not every possible
realization of that formal curve pattern at higher crossing number.

It also excludes EVERY nontrivial L-space knot and its mirror as a
companion. The Alexander polynomial of an L-space knot has the form

  (-1)^k + sum_i (-1)^(k-i)(t^n_i+t^(-n_i)), 0<n_1<...<n_k.

For a nontrivial such knot k>=1, and

  a_2 = sum_i (-1)^(k-i)n_i^2 > 0.

Pair successive terms from the largest exponent down: every difference
of squares is positive; an unpaired smallest square is also positive.
This uses the established L-space surgery structure and genus detection.

Sources for the actual curve table and Alexander structure:
https://msp.org/obs/2022/5-1/obs-v5-n1-p10-p.pdf
https://arxiv.org/abs/math/0303017

Two deliberately investigated false positives clarify the limitation.
The Kinoshita--Terasaka knot has Alexander polynomial one and the desired
large-surgery Floer-rank growth p+16, but is not strongly invertible;
it cannot be this cover companion. Its trivial symmetry group is proved
in Akbulut--Ruberman, Proposition 2.6:
https://www.selmanakbulut.com/papers/absolute.pdf

The actual two-bridge knot K(31,18), mirror of 8_14, IS strongly invertible,
has a_2=0, and also has large-positive-surgery Floer rank p+16. Its
Alexander polynomial is -2t^2+8t-11+8t^(-1)-2t^(-2). Nevertheless its
actual quotient has FIFTEEN special curves, not four, for both listed
strong inversions. Thus even all these numerical matches fail to give
the required geometric tangle. The identification of 8_14 as K(31,12)
is in the primary table at p.786 below; 12*18=-1 mod31 gives the mirror:
https://www.numdam.org/item/AFST_2020_6_29_4_761_0.pdf

3. A PRECISE OBSTRUCTION TO A POSITIVE PHYSICS MODEL

Proposed mechanism: replace Jones amplitudes by a finite classical model
with nonnegative local weights, then use positivity to prevent complete
cancellation. The following class of models is impossible.

Fix q>0, q!=1. Suppose three-strand tangles use a fixed finite-dimensional
real state space, with nonnegative matrices G_1,G_2 for positive crossings
and nonnegative inverses for negative crossings. Require Reidemeister II
at the operator level. Use the same closing rule for every braid; allow
normalization depending on strand count and writhe. Such a model cannot
reproduce the Jones polynomial on all knot closures.

Proof. A nonnegative matrix with nonnegative inverse permutes the extreme
rays of the positive orthant: it is a permutation times a positive diagonal
matrix. Some common EVEN power m of G_1 and G_2 is therefore diagonal.
Their mth powers commute. The two braid words

    beta_+ = sigma_1^m sigma_2^m sigma_1 sigma_2,
    beta_- = sigma_2^m sigma_1^m sigma_1 sigma_2

must have identical model matrices. They have equal writhe, and both
closures are knots, since m is even. An exact Temperley--Lieb calculation
instead gives

  V_+(q)-V_-(q)
     = -q^(m+2)(1+q+q^2)(sum_(j=0)^(m-1) (-q)^j)^2,

which is nonzero for the specified q. This contradicts the model.

At m=2 the examples are the cinquefoil and the connected sum of two
trefoils. The general formula was proved algebraically and checked
independently by planar-diagram calculations for m=2,4,6,8,10,12.

The conclusion also holds for a finite positive projection onto a physical
subspace, provided crossings act reversibly there and closures factor
through it. The projected positive cone has finitely many extreme rays;
the same common-power argument applies. Positivity of the final closing
functional was not needed.

Scope matters: this does not exclude every positive formulation. Infinite
state spaces, nonlocal constructions, nonpositive projections, and quantum
density-operator models with nonpolyhedral cones fall outside the theorem.
It does show why a finite classical local reformulation cannot supply the
missing proof merely by removing signs while retaining reversible crossings.

The nonnegative-inverse matrix fact is classical (Ding--Rhee, 2014):
https://aquila.usm.edu/fac_pubs/19923/
The exact braid calculation and extension to the physical cone are recorded
in full in the accompanying evidence. No novelty claim is made.

4. A GEOMETRIC SYMMETRY EXCLUSION AND A FAILED CONSTRUCTION

Restricted theorem. Suppose an n-arc rotor in an unknot has a standard
order-n rotation, with its arcs in one free orbit. If that rotation extends
to a global periodic rotation preserving the completed unknot, a standard
rotor flip again gives the unknot, for every n>=2. The flip must normalize
the cyclic action and have the usual marked-boundary half-turn.

Proof outline. The unknot and rotation axis form a distinguished Hopf
link, as does their quotient. The quotient rotor sphere is a Conway sphere
meeting each component twice. Its four-punctured complement cannot inject
its free fundamental group into the abelian Hopf-link group. It compresses
on one side. The compression separates two arcs belonging to globally
unknotted components; both arcs are boundary-parallel, making that side a
rational tangle. Rational tangles are invariant under the required Conway
half-turn. Thus the colored Hopf link is unchanged. Taking the cyclic
branched cover over the distinguished axis recovers the stated rotor flip
and an unknot. The full proof tracks the component labels and deck lift.

The Hopf-link input is Paoluzzi, Claim 2.1:
https://www.i2m.univ-amu.fr/perso/luisa.paoluzzi/jktr05.pdf
Rational-tangle flipping: Kauffman--Lambropoulou, Lemma 2:
https://arxiv.org/abs/math/0311499

This does NOT apply when only the rotor is symmetric and the stator is
asymmetric. Such a global extension cannot be assumed.

The construction track then tested one invariant surgery circle shared
by four Borromean interactions with neighboring rotor arcs. This reduces
the desired augmented unlink from five components to two. Deleting the
circle removes the interactions, so the rotor alone remains trivial;
the difficulty is their joint embedding. The simplest proposed anchor,
pairwise inverse cancellation, necessarily joins opposite rotor arcs
into a separate component. It leaves at least two non-circle components
and cannot give the required single unknot. More complicated cancellation
is not excluded, but no successful augmented unlink was constructed.

5. THE NEXT CONCRETE TARGET, AND WHAT IS STILL MISSING

The best-defined remaining test is an inherited strong inversion of an
untwisted Whitehead double of a trefoil. Actual Whitehead diagrams pass
a_2=0 and the coarse Floer-rank bound. Primary sources provide both
inherited inversions and exact symmetric diagram constructors:
https://arxiv.org/html/2606.05819 (Example 2.22 and Figure 4)
https://arxiv.org/abs/2608.07114

What remains is a MARKED EXTERIOR QUOTIENT diagram, with meridian infinity
and preferred longitude zero. Compute its zero-closure Jones polynomial
first. A mismatch with the two-component unlink immediately rejects it;
a match would justify checking the other bracket coordinate and the full
curve invariant. No such quotient calculation was completed here.

Involutive Khovanov homology of the Whitehead knot itself is not this
quotient invariant. Likewise, the familiar Whitehead-clasp replacement
has a connected-sum cover companion K#K^r, not the exterior of Wh(K).
Neither can silently substitute for the missing geometric construction.

Strategically, the formal candidate now has a stronger geometric gate;
the simplest finite positive-model route and globally periodic anchors
are excluded. The general Jones question remains unresolved by this work.

EVIDENCE

The companion archive contains the complete track notes, independent
normalization audit, exact diagram data, and calculation scripts from this
pass. It does not vendor the Spherogram/Regina runtimes or the preexisting
Temperley--Lieb engine. The stated theorems have proofs independent of the
finite computational checks; the checks support the example exclusions.
