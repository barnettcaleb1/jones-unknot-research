# C1: exact two-site bracket gate and the unlink-seed rejection

Date: 2026-11-03. Bounded design audit. No new geometric candidate or Jones-unit knot is asserted.

## Fixed full-twist assumptions and normalization

Use the absolute Kauffman bracket: empty diagram has bracket 1, a circle has bracket delta = -A^2-A^-2. In TL_2 let I be the through tangle and e the cup-cap turnback, with e^2=delta e. Work over Q(A), so

    E_0=e/delta,       E_2=I-e/delta.

Fix one outside diagram and two disjoint marked two-strand boxes. Each box has algebraic winding zero: its oriented strands are antiparallel. The parameter p (respectively q) inserts p (respectively q) full twists in the same fixed diagrammatic convention. Endpoint connectivity and the oriented outside diagram stay fixed. Assume every signed closure is a knot. Let w_0 be the oriented writhe with both boxes equal to I.

The full twist has raw eigenvalues A^-6 on E_0 and A^2 on E_2. Each inserted full twist changes oriented writhe by -2. Hence

    T^p=A^(-6p) E_0 + A^(2p) E_2,
    V(K_pq)=(-A^3)^(-w_0+2p+2q) <K_pq>/delta.

Thus the normalized eigenvalues at either site are 1 and A^8. Reversing the diagrammatic full-twist convention reverses the parameter signs consistently. These formulas are for full twists; half-twist families require endpoint/parity bookkeeping.

## Four actual closures and the mixed-channel criterion

Let F be the fixed outside bracket contraction and compute

    B_00=F(I,I), B_10=F(e,I), B_01=F(I,e), B_11=F(e,e).
    kappa=(-A^3)^(-w_0)/delta.

The four B_ij are brackets of actual framed closure diagrams, not formal proposed knot classes. Then

    V(K_pq)=a+b A^(8p)+c A^(8q)+d A^(8(p+q)),

where

    a=kappa B_11/delta^2,
    b=kappa (B_01/delta-B_11/delta^2),
    c=kappa (B_10/delta-B_11/delta^2),
    d=kappa (B_00-B_10/delta-B_01/delta+B_11/delta^2).

Consequently

    b=c=0  iff  delta B_10=B_11=delta B_01.

This distinguishes raw turnback closures from Jones-Wenzl eigenchannels. Saying that one turnback frees the other site must prove the FRAMED identity

    F(e,T^q)=A^(-6q) F(e,I),

and its counterpart at the other site. The raw bracket is not constant: removed curls contribute A^(-6q). The displayed identity is equivalent to c=0; the other identity is equivalent to b=0. A verbal band-cut argument, or merely saying that two bands join the same components, does not identify these marked closures or prove the required isotopies.

## The complete constant-sum unit certificate

For a chosen integer m, the entire line p+q=m has normalized Jones polynomial 1 if and only if these three Laurent identities hold:

    delta B_10-B_11=0,
    delta B_01-B_11=0,
    B_11+(delta^2 B_00-B_11) A^(8m)-(-A^3)^(w_0) delta^3=0.

These are denominator-free and are suitable for one exact certification of a fully specified diagram template.

Equivalently, write J_ij=kappa B_ij for normalized oriented closure values, using the orientation inherited under the local turnbacks. Once b=c=0,

    a=J_10/delta=J_01/delta,       d=J_00-a,
    delta A^(8m) J_00+(1-A^(8m)) J_10=delta.

The seed datum required is the FULL turnback link L, with a=V_L/delta. Only when L is split as J_1 disjoint-union J_2 can this be replaced by a=V_(J_1)V_(J_2). Its component knot types alone do not determine a nonsplit closure.

## Unlink-seed rejection

If the mutual turnback closures are actual two-component unlinks, their normalized values are J_10=J_01=delta. With mixed sectors zero this gives

    a=1,
    V(K_pq)=1+(V(K_00)-1) A^(8(p+q)).

Therefore no constant-sum line becomes Jones-unit unless the seed already has V(K_00)=1. In this mechanism, replacing the determinant-25 Kanenobu seed by a known determinant-one but Jones-nontrivial ribbon seed does not solve the unit equation. Determinant 1 is necessary but not sufficient. A proposed genuinely new cancellation design needs different turnback data, not merely a different Alexander-trivial seed inside the same unlink-resolution mechanism.

If knot input boxes meet the resulting knot in one proper arc each, their connected-sum factors survive through the closure. Such local knot decorations do not supply the missing interaction. A possible new template must specify genuine multi-port interaction and compute the four closures above.

At Jones t=-1, A can be chosen as exp(pi*i/4), where delta=0 and A^8=1. Individual JW coefficients can have poles. Do not evaluate them termwise to infer determinant independence across different sums. The cleared Laurent certificate is safe; determinant is of course constant along any already-proved Jones-constant sum line.

No fully marked new geometric candidate escaping these gates was produced in this pass.
