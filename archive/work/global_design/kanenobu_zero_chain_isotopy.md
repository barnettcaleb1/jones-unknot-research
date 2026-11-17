# Zero matched chains in ALM Figure 25 give the unknot

2026-11-03. Independent visual check by annular_critique agent, with root independently tracing the same endpoint routing. This is an unframed diagram isotopy; no Jones or HOMFLY inference is used.

Source: Anokhina–Lanina–Morozov, *Planar decomposition of the HOMFLY polynomial for bipartite knots and links*, Figure 25. The PDF's page 23 was rendered and inspected directly. The six twist boxes in this figure are labelled, on the upper row, bar(2i'), 2i, 2m, and on the lower row, 2n, bar(2j'), 2j. We use the matched case i'=i, j'=j. A zero box is the identity pair of strands, not a skein resolution.

**Proposition.** For every signed integer m,n,j, the actual knot Kan(2m,2n,2j,0) is the unknot. Likewise Kan(2m,2n,0,2i) is the unknot for every signed integer m,n,i.

**Case i=i'=0.**

1. Remove the two zero upper boxes. The small upper cup between the right leg of the old bar-i box and the left leg of the old i box now joins the two top endpoints of the 2n box. This cup and the sides of that box have a clear interior in the displayed diagram. The 2n twists are twists on a capped pair, so peel them off as Reidemeister-I curls. The two bottom endpoints of the old n box are now joined by a plain arc.

2. Follow the two bottom return arcs of the j boxes. One is the small cup from the bottom-right endpoint of bar(2j') to the bottom-left endpoint of 2j. The other runs from the bottom-left endpoint of bar(2j') through the newly plain n arc and the large outer lower arc to the bottom-right endpoint of 2j. Thus, below the two j boxes, the four endpoints are joined by the nested cup system C=(14)(23).

3. For this nested cup system, a twist on its two left legs can be transported along the return arcs to the two right legs with the SAME braid sign:

       sigma_1^r C is isotopic to sigma_3^r C.

   Geometrically, move the crossing down the left legs, round the two return arcs, and up the right legs. Repeating gives the identity for every integer r. The two boxes in Figure 25 have exponents -2j' and +2j in these coordinates, so for j'=j they cancel by this transfer followed by Reidemeister II:

       sigma_1^(-2j) sigma_3^(2j) C is isotopic to C.

   This is a tangle isotopy of the two returned arcs; it is not inferred from their Temperley–Lieb matrices.

4. After this cancellation, the small inner return cup joins the two bottom endpoints of the 2m box. Remove its 2m twists by Reidemeister I. The entire displayed long tangle is now a planar arc. Closing its two exterior endpoints gives U.

**Case j=j'=0.** The same argument turned upside down first exposes a lower cap on the 2m box. Remove m, transport and cancel the matched upper i and inverse-i chains through the resulting nested upper caps, and then remove the capped 2n twists. Again the remaining long arc is planar.

Negative parameters require no new case: capped negative twists peel off by the inverse Reidemeister-I moves, and the cap-transfer identity holds for negative as well as positive braid powers. No relation between m and n is needed. The proof does not preserve the blackboard framing, which is appropriate to the ordinary unknot statement.

Combined with the independently derived polynomial result in kanenobu_lock_positivity.md, this completes Jones unknot detection for this specified matched four-parameter family: its Jones-unit locus consists exactly of these topologically trivial zero-chain cases. No assertion is made for unmatched chains or the larger KanGen family.

Primary source: https://arxiv.org/html/2407.08724v1#S7.SS4.SSS2 ; journal DOI https://doi.org/10.1140/epjc/s10052-024-13309-0 . Formula numbering differs between the retrieved PDF and HTML, so the topology identification above is anchored to Figure 25 rather than an equation number.
