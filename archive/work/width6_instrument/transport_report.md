# Exact transport and geometric intersection instrument

The numeric prototype fails on the last letter of the 14-letter witness because its sampled image chords can change arc topology. Replacing it with exact piecewise-affine disk homeomorphisms repairs the generic pairing.

## Mathematical transport certificate

For a braid generator centered at `(i+1/2,0)`, the inner diamond of L1 radius3/4 rotates one quarter-turn, the outer diamond of radius5/4 is fixed, and the intervening annulus is triangulated into eight affine cells. All source and image triangle orientations are positive; the maps agree on shared edges, and the outer boundary map has degree one. This is an orientation-preserving disk homeomorphism. Two quarters give the desired half-twist; the negative generator uses the exact inverse subdivision. Every source edge is split at every crossed affine-cell boundary using rational arithmetic. Consequently no replacement chord can pass across a puncture or the other source arc.

The independent check is `conventions_pl_certificate.json`: shared-edge continuity, positive orientations, exact area preservation in aggregate, fixed outer boundary and rotated inner diamond, and 528 exact inverse-point checks. Source intersections with the rational target figure-eights use exact Fraction determinants and reject nontransverse/collinear cases.

## Witness14 calibration

Matrix word: `[4,3,2,1,5,4,3,2,3,4,2,3,-1,-2]`. Geometric chronological generators have entrywise opposite signs.

Without simplification, the source arcs have1388 and3001 vertices. Exact rational target curves give one-point counts `[[575,120],[1255,330]]`, hence340350 actual configuration intersections. The exact winding agent independently obtains

`-q^-3 + q^-2 - q^-2*t + q^-1*t = -q^-5 Phi`,

where `Phi = q^2(1-q)(1+qt)` is the separately calibrated matrix pairing. Thus the TL specialization vanishes. This calculation uses actual intersections and exact ray/full-line winding counts, not representation path terms.

## Safe local isotopies and scaling repair

`transport_simplify.py` deletes an intermediate vertex b of a-b-c only when the closed swept triangle is disjoint from all punctures and every other segment of both source arcs, except retained common endpoints a,c. These are ordinary isotopies rel punctures and endpoints, not cap slides. A uniform spatial hash uses exact rational cell-floor operations, and all fine predicates are exact. Every accepted deletion therefore preserves the source arc isotopy classes and the generic pairing up to the freely chosen base-lift unit.

Applying this conservative simplifier after each generator reduces witness14 to five vertices on each arc and FOUR configuration intersections, in approximately0.05s total. The resulting pairing is

`-q^-1 + 1 - t + q*t = -q^-3 Phi`,

still zero on the TL line. `transport_simplified_pairing_14.json` records before/after curves at every generator and all64 accepted swept triangles. The four records retain exact positions and one-point identifiers. This is not a proof of global intersection minimality or tight position under cap slides.

Nineteen controls—individual generators, inverses, a braid relation, and seeded words through length11—compare the simplified and unsimplified exact geometric pairings; all agree up to a Laurent unit. See `transport_simplifier_controls.json`. Simplifying only after the final unsimplified transport is much less effective:423 vertex deletions in30s versus incremental witness14 simplification in0.05s.

## Stable API

`transport_simplified_pairing.exact_model(matrix_word, source_caps=((1,2),(3,4)), vertex_limit=15000, pair_limit=2000000, simplify_seconds=3, certificate=False)` combines exact transport, conservative local isotopies, exact intersections, and the exact winding engine supplied by the combinatorial agent. It returns compact point-indexed records, rational positions, and the aggregate pairing. `source_caps` must be two disjoint horizontal arcs; arbitrary cap basis classes must first be represented by their stored braid transports. The wrapper rejects nontransverse target choices, trying four rational target radii, and has explicit size guards.

No long-control conclusions are claimed here; the parent agent owns the Bigelow/Long–Paton orchestration.
