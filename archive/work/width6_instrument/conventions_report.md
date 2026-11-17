# Independent conventions and partner analysis

Scope: bounded support for the 20261103-033359 instrument assignment. No new knot search; no scaffold edits. This report concerns the current mixed square–torus geometric model, whose matrix target is Phi = q^(-2) P/(1-t), not an assertion that each raw point is a point of the absolute torus–torus pairing H.

## Adapter and location of the old failure

The tested adapter is: a matrix word w is applied geometrically in chronological order with letters [-g for g in w]. The geometric positive generator is a counterclockwise half twist. Twenty fixed small controls, including noncommuting words, inverses and braid-relation controls, match the exact generic matrix Phi up to a signed deck monomial. All prefixes 1–13 of the 14-letter witness match; the last generator is where the old sampled-curve model first fails. These are convention/calibration checks, not a uniqueness proof of the adapter among transformations that preserve a particular matrix coefficient.

For the witness w = [4,3,2,1,5,4,3,2,3,4,2,3,-1,-2], expected Phi is q^2(1-q)(1+qt). The old answer differs after deck normalization by -q^(-3)(q-1)^2(1-t^(-2)). Refining the target curve changes the wrong answer. Exact source transport fixes the discrepancy. Thus the failure was geometric transport, not evidence against the square–torus dictionary.

## Independent local certificate for the corrected PL transport

The eight annular source triangles and their image triangles have positive exact orientations. Their shared-edge maps agree. Both triangulations have annular area 2. The inner boundary undergoes one counterclockwise quarter turn, and the outer boundary is pointwise fixed. Hence the piecewise affine annular map has degree one and positive local orientation; it is a PL homeomorphism. Extend by rigid quarter rotation inside and identity outside. Two such maps form a half twist. The puncture-pair midpoint is half-integral, the inner radius is 3/4, and the outer radius is 5/4, so the two selected punctures lie inside and neighboring punctures (distance 3/2) lie outside the support.

The certificate script additionally checks 528 exact rational barycentric points against forward and inverse maps. The exact source-cell splitting preserves the two source arcs' disjointness. The two target figure-eight supports lie in disjoint x-bands. Therefore the successive-point paths used for winding never hit the configuration diagonal.

This validates the path geometrically. It does not turn the existing floating-point angle primitive into an exact winding calculation. In the rational-target 14-letter run its largest integer-rounding residual is about 6.03e-11. A certified integer winding implementation remains a separate layer, currently owned by the transport agent.

## Actual-point cancellation in the validated 14-letter representative

The rational-target run has transverse one-point counts [[575,120],[1255,330]], no collinear overlap or vertex degeneracy, 2,280 distinct one-point intersections, and 340,350 configuration intersections. Its generic aggregate is -q^(-5) times the expected Phi.

The proposed strict partner map is impossible for this representative. Here “strict” means an involution of ALL actual configuration intersections, pairing exponents by Delta a = Delta b = plus or minus 1 with the SAME raw polynomial sign. The same raw sign is necessary because specializing t=-q^(-1) reverses sign when b changes by one.

A minimal obstruction is enough: the highest actual collapsed degree a-b is 1. Its 4,788 configurations all have b=0; 2,394 have each raw sign. No point at that degree has a possible adjacent-b partner. These top terms cancel at identical (a,b), with opposite raw signs, instead of through (1+qt) packets.

The full count recurrence also excludes a strict perfect matching on every collapsed degree and raw-sign class. Arbitrarily canceling equal-exponent opposite-sign points first produces 170,173 ordinary pairs and leaves four points, which can then form two (1+qt) packets. This is an algebraic bookkeeping decomposition only. It does not identify a separating disk or geometric involution.

No strict partner preserves one of the physical one-point intersections. This is structural and supplies no additional evidence: b mod 2 equals the matching parity on every record (189,750 even/direct and 150,600 odd/switched). Changing b by one switches the matching; because target loops are disjoint, both coordinates must change.

The circle-target representative gives the same qualitative obstruction with 254,638 configurations; its top degree has 3,688 points, again all b=0 and equally split signs. Different representatives need not have equal point counts. Their aggregate polynomial matches up to a deck unit.

## Limits of the negative conclusion

Only the all-points fixed-shift conjecture for these specific representatives is refuted. More general disk-induced cancellations can combine ordinary bigons, (1,1) packets, or other shifts. No tight representative was produced, so this does not refute the tight-position conjecture, the key lemma, or Lemma Q.

## Reproducible artifacts

- conventions_checks.py / .json: twenty adapter controls.
- conventions_prefixes.py / .json: witness prefixes under old sampled transport.
- conventions_pl_certificate.py / .json: independent exact local PL checks.
- conventions_partners.py: actual record analysis; optional input filename.
- conventions_partners_exact.json: rational-target witness summary.
- conventions_partners.json: circle-target witness summary.
- conventions_14_exact_compact.npz: integer rows [index,a,b,raw_sign,source0pointID,source1pointID].
- conventions_14_exact_points.json: point-ID dictionary and positions.
- conventions_14_compact.npz / conventions_14_points.json: circle-target analogues.

## Follow-up: one certified local bigon and the reduced four-point model

The large representative does contain genuine local equal-exponent cancellations. Configurations153848 and154178 both have(a,b)=(1,0), opposite raw signs, and the same source1 point69. Their source0 intersections796/797 bound a small triangular bigon with target0 lobe edge14 across source vertex1111. Exact vertices are

- (2375447/1213200,13/50),
- (19885/10156,660/2539),
- (74169/37880,13/50).

The twice-signed area is -7/57445020000. Exact tests show no other source intersection on the target side, no other target intersection on the source sides, and no punctures in the triangle's bounding box. This is an embedded empty local bigon. It gives an ordinary intersection-pair cancellation and is not a retraced-connector cancellation. Certificate: conventions_bigon_certificate.py/.json. No claim is made that all170173 bookkeeping cancellations admit this description.

The transport agent's conservative empty-triangle isotopies reduce the source arcs to five vertices each and the actual configuration intersections to FOUR. Independent inspection found no defect in the simplifier's safety predicates: its grid uses exact rational floors as a conservative broad phase; its final decisions test punctures, contained segment endpoints, and all triangle-edge intersections exactly. These isotopies are relative to punctures and both source arcs; they are allowed to cross the fixed target curves. They do not establish global tightness.

For the reduced model the exact actual-point polynomial is

    1 - q^(-1) + qt - t = (1-q^(-1))(1+qt).

Records in order have(a,b,sign)=(0,0,+1),(-1,0,-1),(1,1,+1),(0,1,-1). Thus0↔2 and1↔3 form an ACTUAL four-point h-involution. Independently reconstructed rational configuration-space paths verify that BOTH h-partners have monodromy(1,1). More precisely their per-puncture winding vector is(1,0,0,0,0,0): a total counterclockwise winding about puncture1 together with one exchange of the two configuration points.

By contrast,0↔1 share the same physical source1 intersection with the two retraced traversals of target1's connector. Its path differs by one clockwise circuit of puncture4: monodromy(-1,0). Pair2↔3 consists of two source0 intersections with target1's puncture4 lobe and has the same monodromy(-1,0). Therefore retracing alone does NOT cancel: it supplies the(1-q^(-1)) factor. The exchange/puncture1 pairing supplies(1+qt), which vanishes on the TL line.

This reconciles the two conclusions: the unsimplified340350-point representative has no all-point fixed-shift h-map, while the safely simplified four-point representative has one explicitly. The latter is a genuine point/path-level description, not an inference from an aggregated polynomial. It has not yet been derived from a separating disk or extended to arbitrary split configurations. Exact path vertices and winding certificates are in conventions_reduced_four.py/.json.

Terminology clarification: the reduced data have FOUR oriented intersection incidences/preimages of the parametrized cycles, but only THREE distinct downstairs unordered configurations. Records0 and1 share both physical coordinates because the connector is retraced. A sufficiently small generic parallel separation of its two traversals makes those incidences distinct while preserving their transverse signs and, under continuous lift/basepoint choices, their winding labels. Thus the four-incidence pairing can be realized by four distinct transverse configuration intersections after perturbation; the unperturbed file itself should not be described as four distinct physical points.
