# Snape's strong-inversion templates: actual figure read

Read-only source inspection, 2026-11-03. I inspected rendered images of the actual PDF, not only OCR. Source: [Snape thesis, printed pp. 21–22, PDF pages 46–47](https://theses.gla.ac.uk/39015/1/2018SnapePhD.pdf#page=47). Local render: `work/next_theory/snape_figures/page-047.png`; sign convention: `page-046.png`. No quotient tangle or preferred-framing diagram has been inferred from this picture alone.

## I_1: layout relative to the axis

The red rotation axis is a VERTICAL LINE IN THE PROJECTION PLANE. The alpha boxes are vertical two-strand twist boxes straddling that line: alpha_1 highest, then the omitted alpha_2,...,alpha_(m-1), then alpha_m lowest. On EACH side is an identical row of horizontal two-strand boxes. Read from the axis outward: -c_1, -c_2, ..., -c_m. Thus each c_j occurs twice in the full knot diagram, with the displayed label -c_j on both sides. The alpha_j boxes occur once each, on the fixed axis. The inversion is the spatial half-turn about the red vertical line, not merely planar reflection; it exchanges the two side rows.

Two large exterior arcs close the diagram: the far upper ports of the left and right -c_m boxes are joined by the arc above everything, and the far lower ports are joined by the arc below everything. Those two exterior arcs cross the red axis at the two fixed points of the knot.

For the requested FOUR-ENTRY continued fraction, m=2, there are no hidden intermediate alpha boxes, and the picture gives the following complete wiring. On either side label ports of a horizontal -c_j box by near/far (relative to the red axis) and upper/lower. Label ports of each vertical alpha box top-left, top-right, bottom-left, bottom-right. For side L or R use the corresponding left or right port of each alpha box:

1. alpha_1 top-side -> (-c_1) near-upper.
2. alpha_1 bottom-side -> (-c_1) near-lower.
3. (-c_1) far-upper -> (-c_2) near-upper.
4. (-c_1) far-lower -> alpha_2 top-side (the curved connector shown dotted as part of the general ellipsis).
5. alpha_2 bottom-side -> (-c_2) near-lower.
6. Close the two (-c_2) far-upper ports to one another above the diagram; close the two far-lower ports below the diagram.

All these connecting arcs have no additional crossings in the displayed template. The crossings live inside the twist boxes. For larger m the dotted notation repeats the same arrangement, with the lower side route visiting the successive alpha boxes and the upper side route chaining the c boxes. The m=2 wiring is the directly visible case relevant to the pilot family, so it is the safest starting point.

## Sign and continued-fraction cautions

Printed p.21 explicitly warns that its additive continued fraction [a_1,...,a_n] is NOT automatically Conway's normal-form convention, despite similar notation. Fix it by the displayed additive rational expression a_1+1/(a_2+1/(...)). It also gives local crossing glyphs: a positive exponent repeats the crossing with the NW-to-SE strand over the NE-to-SW strand in the upright glyph; a negative exponent reverses the overpass. Rotate this glyph with the twist-box direction. Do not assign oriented writhe signs before choosing orientations of the strands. In particular the side-box label is -c_j, not c_j.

For an even additive continued fraction [a_1,a_2,a_3,a_4], Proposition 1.2.11 gives, when q^2 is not 1 mod p,

    I_1(a_1,a_3; a_2/2,a_4/2)
    I_1(-a_4,-a_2; -a_3/2,-a_1/2).

Thus IF the pilot is fixed by the additive fraction [2,-4n,2,2n], its two templates are

    I_1(2,2; -2n,n),        I_1(-2n,4n; -1,-1).

In the first picture the two central boxes are 2,2 and each side has inner box +2n, outer box -n. In the second the central boxes are -2n,4n and all four side boxes are +1. This is a translation of the published parameter formula, not a bracket calculation. The already stated fraction p/q=(32n^2-1)/(16n^2+2n) has q^2 != 1 mod p for n>=1: 8(q^2-1) is congruent to 16n-5, which lies strictly between 0 and p. So the first case of Proposition 1.2.11 applies throughout that family.

## I_2: what the second figure actually shows

Figure 1.11 instead has the rotation axis PERPENDICULAR to the projection plane, shown by a red dot at the middle. The twist boxes form a horizontal zigzag/serpentine chain, with labels alpha_1, -alpha_2, ..., (-1)^(m-1)alpha_m on its first half and their half-turn partners on its second half. Each alpha_j appears twice, exchanged by the half-turn about the red dot. The diagram has one free end at lower left and one at upper right. Snape explicitly says these are joined OUT OF THE PROJECTION PLANE; closing them by an arbitrary planar arc is not the template and would spoil the stated symmetry. The middle connector passes through the red dot; the other fixed point is on the out-of-plane closing arc.

This is enough to distinguish its symmetry and box arrangement, but for the residual family above I_2 is not required because q^2 != 1 mod p.

## What remains unestablished

Taking the quotient of the symmetric knot picture, marking the meridian and longitude, selecting the deleted ball, and implementing Snape's clasp-and-coil projection still require geometric work. The figure alone is not a rational-tangle product for the exterior quotient. No claim about the Watson-tangle bracket, semiadequacy of its closures, or surviving annular states is made here.
