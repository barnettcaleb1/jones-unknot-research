# Width-two eigen coordinates: three matrix channels, not two scalar channels

17 November 2026. Theory-only answer to Claude 032804, question 3.
No coefficient or knot computation; uses the generic fusion/marking facts in
`width2_marking_fusion.md` and the exact cap-slide identity already banked in
`width2_unit_line_referee.md`. The box-algebra deduction and sector-rank
corollary are PROVED under the collaboration protocol following Claude's
independent bending/marking read034300 and Codex's internal read. No global
nonvanishing theorem or external specialist review is claimed.

## 1. The genuine fixed-cut analogue of the necklace algebra

Work over the generic skein field K=Q(A), with V_j the color-j simple object.
Let

    U=V1 tensor V2 tensor V2.

Bending the last two color-two legs, in their reversed pivotal order, gives
the canonical marked vector-space identification

    H2=Hom(V1,V1 tensor V2^4) is isomorphic to End_Uq(U).

All Hom and End spaces below mean intertwiners in the generic ribbon
category, not the full endomorphism algebra of the underlying vector
space. Write End(U) for this intertwiner algebra.

This is not merely a dimension coincidence. A box with one axis string and
TWO arc strings running west-to-east is an actual endomorphism of U, and
stacking such boxes with this same cut is composition in End(U).

Fusion gives

    V1 tensor V2^2 = 2 V1 direct-sum 2 V3 direct-sum V5.

Consequently its generic intertwiner algebra is

    End(U) = Mat_2(K) direct-sum Mat_2(K) direct-sum K.       (1)

Choose marked bases in the two multiplicity spaces once. The state of an
actual box B is a triple

    (M1(B), M3(B), a5(B)),

where M1 and M3 are 2-by-2 matrices and a5 is a scalar. The same-cut
composition law is componentwise MATRIX multiplication:

    Mj(B_N ... B_1)=Mj(B_N)...Mj(B_1),
    a5(B_N ... B_1)=product_i a5(B_i).

For any fixed exterior closure, ordinary matrix trace duality supplies
unique fixed C1,C3 and c5 such that its raw scalar is

    F(B_1,...,B_N)
      = tr(C1 M1(B_N)...M1(B_1))
        + tr(C3 M3(B_N)...M3(B_1))
        + c5 product_i a5(B_i).                            (2)

Quantum-dimension factors, caps, and the special region are absorbed in
these fixed closure coefficients. They are not independent framing
normalizations. The preferred J is obtained by the single prescribed
overall normalization. Common denominators must be retained.

Equation (2) is the honest width-two analogue of the two-product necklace
formula. It has three terms independent of the number of boxes, but two
terms transport a two-dimensional multiplicity state. It is therefore
not a two-term scalar product identity in a single ratio.

If a specified family of boxes is simultaneously diagonal in each matrix
channel, (2) reduces further to at most FIVE products of scalar entries.
Simultaneous diagonalizability is an additional hypothesis; generic
semisimplicity of the category does not make distinct boxes commute.

## 2. The local generators explain the banked multiplicities

In the cut used above, X1 exchanges the two outgoing arc legs and acts by
left multiplication in (1). X3 exchanges the two incoming legs and acts
by the corresponding pivotal right multiplication. The axis twist Y is
another left multiplication. The handedness of the right operator is
fixed by the common marking; no separate mirror normalization is allowed.

For X1, the color-one multiplicity block has eigenvalues 1,-t; the
color-three block has eigenvalues -t,t^3; the color-five scalar has
eigenvalue t^3. Left multiplication therefore has eigenspace dimensions

    1:2,       -t:2+2=4,       t^3:2+1=3,

exactly the banked (2,4,3). For Y, both two-dimensional multiplicity
blocks have eigenvalues 1,t^-3, while the last scalar is t^-3. This gives
the banked (4,5). These statements follow just by fusing the relevant pair.

Thus the two-by-two channels are genuine residual degrees of freedom,
not artifacts of a nine-coordinate link-state basis.

### Sector-rank corollary (Claude034300)

Choose the pair-fusion bases in the multiplicity spaces. Their labels are
S1={0,2}, S3={2,4}, S5={4}. X1 acts on rows and X3 on columns with the
same channel eigenvalues; bending both strands rotates the crossing and
preserves its type. In each matrix block the joint eigenspace for (a,b)
is the matrix-unit line when both labels occur. Thus

    rank E_ab = sum_(c=1,3,5) [a in S_c][b in S_c],
    (rank E_ab)_(a,b=0,2,4) = [[1,1,0],[1,2,1],[0,1,2]].

This re-proves the seven-sector ranks and the exact E04=E40=0 selection
rule directly from the box algebra. E22 and E44 have dimension two because
their pair labels occur in two different total-color blocks.

The fixed space of X1 X3^-1 consists of the diagonal matrix units and has
dimension2+2+1=5. It contains the known three-dimensional axis-straight
annulus summand. If the off-diagonal scalar coefficients of a specified
closure vanish, its opposite-twist line is constant. This is an operator
and scalar-evaluation statement; it does not prove that every such
constant line has the topology of the known annulus example.

## 3. Why this is not yet a formula for arbitrary mixed words

X2 crosses a leg on one side of the cut with a leg on the other side. It
is a recoupling operation on End(U), not same-cut composition by a box.
The exact already-banked identity makes the distinction concrete.

Let v=f0 be the input with arc cups 12/34 and w=f2 the nested cups 14/23.
After bending, w is the identity endomorphism of U (up to the fixed
common pivotal convention), and v is the axis identity tensored with a
cup-cap on V2 tensor V2. Hence:

* v is supported only in the total-color-one matrix channel, where it
  is a nonzero rank-one map;
* w has nonzero identity components in ALL three channels of (1).

But the fixed source-matrix/cap-slide certificate gives

    X1 X2 v = t^4 w.

X1 is invertible and preserves the three blocks. Therefore X2 sends this
single-block input to a vector with all three blocks nonzero. It cannot
be modeled as fixed left/right multiplication inside the three blocks.

This is an actual marked example, not a formal state chosen outside the
geometric orbit. It identifies precisely where a global two-product or
three-independent-channel argument would lose information. A word can be
split into same-cut box stretches, using (2), but each cross-cut exchange
requires the fixed recoupling transfer on the nine-dimensional space.
The number of such transfers is not bounded by this decomposition.

This does not prove that no clever nonlinear coordinates or small
automaton can solve the global problem. It proves that the commutative
necklace argument does not extend by ignoring multiplicity and recoupling.

## 4. Exact eigen coordinates for a single twist

Fix one adjacent exchange X. Its projectors give

    H2=H0 direct-sum H2c direct-sum H4,
    dim(H0,H2c,H4)=(2,4,3).

On the chart where all components are nonzero, choose local normalized
representatives u0,u2,u4 for their internal projective directions and
write

    [v]=[u0 + z2 u2 + z4 u4].

The internal directions lie in P1 x P3 x P2. The twist acts exactly as

    (z2,z4) -> ((-t)^m z2, t^(3m) z4),

leaving those internal directions fixed. The six internal projective
parameters plus the two amplitudes give the correct projective dimension 8.
A different adjacent twist generally changes both kinds of data.

For any fixed input v and exterior functional phi this gives the exact
single-site formula, with coefficients alpha_c=phi(P_c v),

    phi(X^m v)=alpha_0 + alpha_2 (-t)^m + alpha_4 t^(3m).

The three coefficients contract spaces of dimensions 2,4,3; they do not
encode the entire input for another generator.

For disjoint twists X1,X3, use the seven joint blocks. Five are lines,
while 22 and 44 each have dimension 2. The corresponding chart consists of
six relative amplitudes and two internal P1 coordinates. Both twists
scale the amplitudes by their known joint characters and leave the two
internal directions fixed. This is the exact multi-coordinate version of
the width-one eigen-ratio action.

For fixed outside tangles the closure contracts these blocks to the seven
coefficients c_ab already used in WIDTH2-SECTORS. In full-twist parameters,
the exact formula is

    phi(X1^(2m) X3^(2n) v)
      = c00 + c02 t^(2n) + c20 t^(2m) + c22 t^(2m+2n)
        + c24 t^(2m+6n) + c42 t^(6m+2n) + c44 t^(6m+6n).

Here c_ab=phi(P_a^(1) P_b^(3) v), with no independent normalization of
the terms. For unsquared powers replace t^(2m),t^(6m) by (-t)^m,t^(3m)
and likewise at the second site. However the seven scalar
coefficients alone do not describe the internal state for a subsequent
cross-cut recoupling. The two residual multiplicity directions matter.

## 5. What reduction this delivers

For width-two necklaces whose pieces share one axis-plus-two-arcs cut,
the correct state system is two 2-by-2 matrix channels and one scalar.
This is a genuine bounded-state reduction independent of the number of
pieces. A constructive next assertion would need to control the joint
matrix states reachable in the two channels, with the same geometric box
supplying both, rather than treating two arbitrary matrices independently.

For unrestricted nine-state braid words, the open input is control under
the cross-cut recoupling operator. The observed scalar rational-box
automaton does not provide this. The already certified finite-window
theorem remains the available all-parameter reduction after the outside
tangles are fixed.

A cheap falsifier of a proposed channelwise global extension is the single
identity X1 X2 f0=t^4 f2: any model that preserves total-color support
under X2 fails on this actual cap-slide. A proposed scalar two-channel
model must also explain the two matrix multiplicity spaces in (1).

No generic faithfulness, line-stabilizer rigidity, positivity, or tangle
realization of arbitrary triples in (1) is asserted.
