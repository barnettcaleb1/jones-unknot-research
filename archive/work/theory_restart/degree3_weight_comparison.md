# The order-three modulo-five symbol comparison

Codex subagent `degree3_weight_comparison`, 16 November 2026. Bounded response to Claude213843. No knot scan or fitted identity. The fixed certificate is `referee_checks/degree3_brauer_mod5.py/.json` (18 assertions). The complete root-contraction argument below was independently read by the `degree3_modfive_route` agent.

## Result and its exact scope

Put

    R_3(K,h)=M_3(K,h)/36-7v_3(K),

which is integer-valued by the banked ROOTS arithmetic. Then the reduction of R_3 modulo five has equivariant finite-type order at most two:

    Delta^3 R_3 = 0 in F_5

for every three disjoint specified equivariant crossing changes.

This proves the comparison of the complete degree-three principal symbols, with preferred framing included. It does **not** prove R_3=0 modulo five. A primitive, mirror-odd lower-order residual remains to be determined. Consequently it does not yet prove that iota=R_3/5 is integer-valued or identify iota geometrically.

The mechanism is a Brauer-contraction congruence between superdimension -1 and ordinary dimension 4, with the axis defect and pointed boundary included. It is not just equality of eigenvalues.

## 1. Fix the actual X/Y marking first

The FT matrix certificate uses q^2=t, q=i exp(h/2), and T=B_21 B_12. Directly,

    T i=q^-4 i,

while the other fusion eigenvalue is q^2. After normalizing the attached color-one channel to one, T has other-channel eigenvalue t^3. The banked matrix Y, representing halfword y0, has other-channel eigenvalue t^-3. Therefore

    X=x1 corresponds to B_22 (with its common ribbon unit),
    Y=y0 corresponds to T^-1 (with its common ribbon unit).

The fact that the FT divisibility proof works equally for T or T^-1 did not fix this relative marking. It matters when comparing odd symbols with the ordinary Jones polynomial of the covering knot. This is a convention clarification, not a change to FT or the Casimir calculation.

## 2. The osp root contraction model

Use the already proved root model on V=C^{1|2}, with Pi=diag(-1,1,-1), and put

    g=-Pi.

Let P be the super permutation and K=coev ev for the root orthosymplectic form. A straight raw off-axis principal insertion is

    -2(P-K).

The pointed boundary is the even middle line; its projector is

    e=(I-g)/2.

It has superdimension one. Every actual quotient has one connected arc, so after reducing the color-one axis, its root tensor contraction is the pointed contraction on that arc. Closing it by e expresses the scalar as a supertrace without introducing a dimension denominator.

The two closed-loop parameters are

    delta=ev coev=str(I)=-1,
    tau=ev(g tensor I)coev=str(g)=-3.

Since g is an isometric involution, it passes through cups and caps; two adjacent g labels cancel. A closed Brauer diagram with g labels therefore evaluates as a product of factors delta and tau, one for each loop according to the parity of its labels. Expanding the single point e=(I-g)/2 only introduces a factor 1/2. This reduction is the defining diagrammatic contraction rule, not an assumption about a semisimple decomposition.

For Y=T^-1, the preferred normalized axis principal insertion has the opposite sign from the displayed T insertion in the FT report:

    D_Y=+6Q_odd=3(I+g).

All these insertions are identity on the reduced axis factor. Thus the axis itself no longer carries hidden tensor indices in a principal contraction.

## 3. Fold the covering knot's ordinary Jones tensors

To compare with V_K(exp(2h)), use an ordinary two-dimensional sl2 module U with quantum parameter q_c=exp(-h), since the ordinary Jones variable is q_c^-2. Folding the symmetric diagram pairs its two half-strands into

    W=U tensor U.

At h=0 this is an ordinary four-dimensional orthogonal space with symmetric form epsilon tensor epsilon, where epsilon is the standard alternating form on U. The branch-point cap selects the antisymmetric line in W. If g is the sheet swap, its projector is again

    e=(I-g)/2,

and has dimension one. The folded cup/cap are the metric epsilon tensor epsilon and its inverse. The unmarked off-axis pair gives the ordinary permutation P of two copies of W. The root normalized on-axis generator y0 gives -g, agreeing with the osp root monodromy Pi=-g.

These statements follow generator by generator from the standard symmetric halfword completion: x_i,y_i for i>0 become the pair of corresponding crossings in the full diagram; x0,y0 become its single central crossing; paired births/deaths give the product metric; the start/end identify the antisymmetric cap. Thus the folding applies to arbitrary actual halfwords, not just two-band braids.

Its loop parameters are

    delta=dim W=4,
    tau=tr(g)=2,

and (delta-tau)/2=1 as required by the point projector.

### Off-axis symbol: the Fierz identity

On U_1 tensor U_2 tensor U_3 tensor U_4, write g_13 and g_24 for the two sheetwise permutations. The permutation and contraction of the paired space W satisfy

    P=g_13 g_24,
    K=(I-g_13)(I-g_24),
    P-K=g_13+g_24-I.

The fundamental crossing's straight difference symbol at q_c=exp(-h) is -2g+I. A paired crossing change adds the two sheetwise symbols, giving

    -2(g_13+g_24)+2I=-2(P-K).

This agrees exactly with the osp coefficient and Brauer expression.

### On-axis symbol, including the sign and preferred correction

Let B be the fundamental braid. At q_c=1, B=g. The central halfword y0 is the inverse crossing. Incorporating the root Jones sign gives Y_c=-B^-1, with root -g. Its raw principal difference from its inverse crossing, using d/dh=-q_c d/dq_c, is

    D_raw=-2I+g.

On the antisymmetric point this has value -3, while the root map -g acts as 1. Hence the preferred framing correction subtracts (-3)(-g), leaving

    D_Y,cover=-2(I+g).

This differs from the osp normalized symbol 3(I+g) by exactly 5(I+g). Confusing T with the actual Y=T^-1 would give the wrong sign and destroy this comparison.

The fixed certificate verifies this from the actual fundamental R-matrix, not an eigenvalue fit. It also checks the Fierz identity, the point projector, its metric, and the attached-channel identity T i=q^-4 i.

## 4. Compare every principal contraction modulo five

The two root models have parameters

    (delta,tau)_osp=(-1,-3),
    (delta,tau)_cover=(4,2).

They agree modulo five. Their point projectors have the same formal expression e=(I-g)/2. Bulk principal insertions have the same expression -2(P-K). Axis preferred insertions agree modulo five. Unmarked root crossings, dualities and defect monodromies have the same formal Brauer descriptions.

For an off-axis preferred insertion, one must also subtract the first-coefficient framing term. That coefficient is computed by the **complete one-insertion contraction**, with all other tensors at the root. Those contractions are themselves sums of pointed, g-decorated Brauer diagrams, so they agree modulo five by the same (delta,tau) comparison. Thus their scalar framing corrections agree modulo five. This handles the actual outside diagram rather than assuming one universal framing coefficient at every off-axis site.

On any marked cube f_1 is affine, by the proved FT argument. Its exponential normalization therefore distributes among the marked balls. The complete principal coefficient is the contraction of the normalized local principal insertions with the remaining root tensors. Expanding P,K,I and e reduces that contraction to a polynomial in delta,tau over Z[1/2]. Since 2 is invertible modulo five, the two models give the same result modulo five.

In particular, for every three-move cube,

    Delta^3 [h^3]J(-exp(h))
      = Delta^3 [h^3]V_K(exp(2h))   (mod 5).

No completeness theorem for a list of singular-knot examples is needed: the generator-level tensor comparison applies to every outside diagram at the principal order. No full quantum category equivalence is asserted.

## 5. Convert to the stated moment residue

The ordinary knot identity V'(1)=0 and the definition

    v_3=-(V'''(1)+3V''(1))/36

give

    [h^3]V_K(exp(2h))=-48v_3(K).

Meanwhile [h^3]J(-exp(h))=M_3/6. Thus the principal symbol of

    M_3/6+48v_3=6(M_3/36+8v_3)

vanishes modulo five. Since 6 is a unit and 8=-7 modulo five,

    Delta^3 (M_3/36-7v_3)=0   (mod 5).

The integer-valuedness of M_3/36 comes from ROOTS; it is not inferred by reducing a rational quantity with a bad denominator. All denominators in this order-three conversion are prime to five.

The residual R_3 mod5 is primitive under equivariant sum and mirror-odd, using the banked properties of M_3 and v_3. These constraints may help identify it, but they do not establish that it is zero. One must classify or evaluate the remaining order<=2 contribution, including the appropriate base components. The general statement that ordinary finite-type order-two invariants are mirror-even cannot be silently transferred to this equivariant problem.

## 6. A useful scalar observation, not a completion of the proof

For the bulk BMW parameter Q=exp(-h), the osp dimension parameter is

    delta_osp(Q)=1-Q-Q^-1,

while the folded ordinary dimension is

    delta_cover(Q)=(Q+Q^-1)^2.

Their exact difference is

    delta_cover-delta_osp=Q^-2 Phi_5(Q).

Modulo five this is Q^-2(Q-1)^4. It explains why the scalar loop data agree through degree three. The bulk braid parameters likewise differ by a fifth power. This is consistent with a stronger full-jet congruence, but the generic mixed axis has nontrivial couplings and is not merely the root involution g. Without its full deformation comparison, these scalar identities do not remove the lower-order residual. They are not being promoted to a proof of R_3=0.


## Later completion in this turn

The complete annular covering comparison is now written in `degree3_cyclotomic_comparison.md` and recorded TRUSTED pending Claude's read in reply20261116-221023-codex. Its final internal audits include `degree3_cyclotomic_referee.md`, `degree3_annular_closure_audit.md` and `degree3_coefficient_framing_audit.md`. It supplies the full preferred Phi10 congruence and hence the modulo-five third-moment identity, including the lower-order residual. Earlier pending statements in this report describe the intermediate stage. The independent geometric identification of iota remains open, and the exact exclusions in this report, where present, stand.
