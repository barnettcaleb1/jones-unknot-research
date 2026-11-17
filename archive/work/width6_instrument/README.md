# Exact width-six intersection instrument

This directory implements actual geometric intersections for the canonical **square-to-figure-eight-torus** pairing. It does not expand representation matrices into alleged intersection points. The matrix polynomial is an independent calibration after geometric enumeration.

## Scope and conventions

The punctures are at `(1,0),...,(6,0)`. Source arcs are braid images of the standard pair `(12)(34)`. Other cap classes use the archived geometric transports in `../width6_lift/cap_braid_lifts.json`. Target cycles are disjoint figure-eight loops with winding `+1` around their left puncture and `-1` around their right puncture. A single embedded boundary-noodle square is not the correct dual.

With `q=s^2=A^-4`, the canonical normalization is

```
Phi = q^-2 P/(1-t),       Phi(q,-q^-1) = q^-1 J_hat.
```

Geometric enumeration chooses its base lift at the first actual intersection. Its polynomial therefore differs from the archived canonical one by a single signed Laurent monomial. The calibration records that monomial. For zero polynomials the unit is undetermined, not inferred.

For archived cap indices `i,j` with transport words `w_i,w_j`, the effective matrix word on the standard pair is `reverse(w_i) + word - w_j` (the last minus means negate each letter, without reversing). Geometric homeomorphisms act chronologically with the opposite generator sign. Original-cap and effective-seed polynomials are also compared directly; this is not merely a self-consistency test using a relabeled seed.

## Geometry and arithmetic

- `transport_pl.py`: exact rational, piecewise-affine half twists. Each source segment is split at every affine-cell boundary. The maps have positive cell orientations, consistent edges, fixed outer boundary, and the specified inner rotation.
- `transport_exact_intersections.py`: exact rational, transverse source/target intersections. Degenerate segment or vertex intersections are rejected rather than silently counted.
- `combinatorial_winding.py`: unreduced cut crossings, free-group words, and exact integer winding. Puncture winding uses signed ray crossings. Exchange winding uses signed full-line crossings of the relative vector, i.e. winding in the real projective line. No angle rounding is used.
- `combinatorial_exact_pairing.py`: actual complete two-point matchings. Each record is `[matching, point0_index, point1_index, a, b, sign]`; rational one-point geometry is stored once and referenced by index.
- `transport_simplify.py`: conservative joint arc isotopy by deleting a vertex only when its swept triangle avoids all punctures and other source segments. It does not implement cap slides or prove global minimality.
- `intersection_instrument.py`: public entry point, with mandatory independent generic-polynomial calibration.

## Reproduction

From the workspace root, reproduce the four-point witness:

```sh
python3 work/width6_instrument/intersection_instrument.py \
  --word '[4,3,2,1,5,4,3,2,3,4,2,3,-1,-2]' \
  --simplify --output /tmp/width6-witness.json
```

Omit `--simplify` for the 340,350-point representative. `--source-cap` and `--target-cap` accept indices 0 through 8 in the archived cell basis; both default to 7. `--summary-only` suppresses the large output records, while preserving the extremal-line statistics.

The unsimplified enumerator has no claim of efficient complexity. The simplified backend enforces explicit vertex and pair-count budgets and stops rather than inventing partial polynomial data.

## Evidence already saved

| Artifact | Content |
|---|---|
| `combinatorial_exact_basis81.json` | All 81 cap Gram entries, 1,859,630 actual configurations, exact generic and specialized calibration |
| `combinatorial_original_basis81.json` | Direct identification with original cap indices and normalization units |
| `combinatorial_exact_witness14.npz` | Compact exact records for all 340,350 witness configurations |
| `combinatorial_exact_witness14_summary.json` | Rational one-point geometry and record metadata |
| `transport_simplified_pairing_14.json` | Four-point representative, all 64 local swept-triangle moves and intermediate curves |
| `conventions_reduced_four.json` | Exact paths realizing the four-point factorization and individual puncture windings |
| `witness_connector_perturbation.json` | Rational connector perturbation giving four distinct transverse downstairs configurations with the same labels |
| `conventions_bigon_certificate.json` | One independently checked ordinary empty-bigon cancellation in the large representative |
| `conventions_pl_certificate.json` | Independent exact homeomorphism checks |
| `transport_simplifier_controls.json` | Nineteen simplified-versus-unsimplified generic calibration controls |
| `combinatorial_validate.json` | Independent Artin-action convention checks |
| `intrinsic_pair_bounds.json` | Generic coefficient-norm lower bounds on required configuration counts |

The four-point polynomial is

```
1 - q^-1 + qt - t = (1-q^-1)(1+qt).
```

The actual pairs have `(a,b,sign) = (0,0,+1), (-1,0,-1), (1,1,+1), (0,1,-1)`. Counts refer to intersection incidences of parametrized cycles: in the initial retraced-connector model, two records share the same downstairs configuration. An exact return-connector perturbation by `1/10000` produces **four distinct transverse configurations** with the same labels and polynomial. The two `(1,1)` partners have the same raw sign and opposite signs after `t=-q^-1`. Their connecting configuration paths wind once about puncture 1 in total and exchange the two points once. This is a concrete cancellation certificate for this witness. It is not a proof that every Jones-zero tangle splits, and a general separating-disk correspondence is still missing.
