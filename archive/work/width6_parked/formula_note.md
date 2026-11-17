# Exact parked-point decomposition

Scope: the canonical square-to-figure-eight-torus model, with two disjoint source arcs c0,c1 and two disjoint target loop supports gamma0,gamma1. Intersection incidences retain the parametrization of immersed target cycles. No cap-slide minimum or nonvanishing theorem is asserted.

## Anchors and the corrected formula

Let m=0,1 denote the complete matching: x lies on c0 and gamma_m; y lies on c1 and gamma_(1-m). Let m_base be the matching of the global reference intersection used by the instrument.

For each nonempty matching choose a reference incidence (x_m,y_m). Trace its **actual configuration loop** from the global reference, along the target cycles and back along the source cycles. Denote its winding exponents by a_m,b_m and its normalized raw sign by r_m. These constants are independently evaluated path monodromies, not differences defined from a saved record.

For any x,y in this matching, define two closed one-point paths:

```
L_x = gamma_m[x_m -> x] followed by c0[x -> x_m],
L_y = gamma_(1-m)[y_m -> y] followed by c1[y -> y_m].
```

Write A_x and A_y for their total winding about the six original punctures, and put

```
w0_m(y) = wind_{x_m}(L_y),
W_m(x;y) = wind_y(L_x).
```

All paths avoid their extra punctures: the two source arcs are disjoint, and the two target loop supports are disjoint. Then the exact exponents are

```
a(x,y) = a_m + A_x + A_y,
b(x,y) = b_m + 2*w0_m(y) + 2*W_m(x;y).
```

To see the second identity, order the points by source-arc label. Within a fixed matching, the target rectangle allows the second point to be moved first; swapping this order is a homotopy because the target supports are disjoint. Move y_m to y along its target path, traverse L_x with y parked, then return y along its source path. The second point's closed path winds about x_m; the first point's closed path winds about y. A full circuit of either point around the other contributes two half-exchanges. The reference configuration contributes b_m. The same decomposition for ordinary puncture winding gives the first identity.

Let p_m=m XOR m_base. The reference path has b_m congruent to p_m modulo two. With

```
kappa_m=(b_m-p_m)/2,
w0_hat_m(y)=kappa_m+w0_m(y),
```

Claude's requested form becomes exactly

```
b(x,y)-p_m = 2*(w0_hat_m(y)+wind_y(L_x)).
```

Corrections to an unqualified statement: the reference constant is matching- and lift-dependent; the first-point path is a **closed target/source path**, not an unclosed source segment; and p_m is relative to the chosen base matching. Merely setting w0=(b-m)/2-wind from the answer would be tautological and was not used in these checks.

## Parked one-point pairing, with signs

Let sigma_x,sigma_y be local oriented crossing signs, and let x_m,y_m supply their reference signs. Define

```
tau_x = sigma_x * sigma_(x_m),
tau_y = sigma_y * sigma_(y_m),
B_m,y(q) = sum_x tau_x q^(A_x - 2 W_m(x;y)).
```

This is a one-point twisted intersection sum in the disk with the six original punctures plus the parked point y. The original punctures have weight q and y has weight q^-2. The complete specialized pairing is

```
Phi_geom(q,-q^-1)
 = sum_m r_m (-1)^b_m q^(a_m-b_m)
     sum_y tau_y q^(A_y-2*w0_m(y)) B_m,y(q).
```

This gives the requested parked sum without dropping the matching/base prefactors. In particular, a separate bare (-1)^m is not universally the correct orientation factor. The instrument's raw matching permutation sign and (-1)^b cancel at the Jones specialization; if one uses ordinary local crossing signs inside the one-point pairings, the remaining reference factors must be kept as above or explicitly absorbed into the outer unit.

Before specialization, replace q^-2 at y by t^2, and the corresponding factors are q^(a_m+A_y) t^(b_m+2*w0_m(y)) and q^A_x t^(2 W_m(x;y)).

The forgetful fibration is on the **ordered** two-point configuration space: forgetting its second labeled point has fiber D_6 minus that point, i.e. a seven-punctured disk. The unordered configuration space has no canonical operation of forgetting one of its two points. Matching/reference bookkeeping implements passage between these descriptions; it cannot be omitted.

## Exact record checks

`formula_check.py` computes all one-point winding numbers from exact rational ray-crossing primitives, constructs matching reference configuration paths independently, then compares every predicted `(a,b,sign)` with the existing exact instrument records. It also evaluates every parked inner polynomial and the full outer sum independently.

| case | incidences checked | matching 0 specialized sum | matching 1 specialized sum | total |
|---|---:|---|---|---|
| reduced witness 14 | 4 | 1-q^-1 | q^-1-1 | 0 |
| unsimplified witness 14 | 340,350 | q^-2-q^-3 | q^-3-q^-2 | 0 |
| nonzero six-letter control, cap indices3,7 | 4,005 | 0 | q^-4 | q^-4 |

All individual exponent/sign comparisons and all parked-sum comparisons pass. The nonzero control's effective standard-seed word is `[4,3,2,1,2,1,-2,3,2,-3]`, representing the original word `[2,1,-2,3,2,-3]` with its saved cap transports. Its overall canonical deck normalization is the already calibrated one, so the reported total agrees with the saved geometric specialization.

For the unsimplified witness, w0_hat ranges from 0 to1, W_m(x;y) ranges from -1 to1, and 1,435 parked positions have genuinely varying W over x. Thus the large check does test nonconstant extra-puncture winding.

For the **reduced four-point witness**, all w0 and W are zero. Its factor 1+qt is carried by the two different matching-reference monodromies `(a_m,b_m)=(0,0),(1,1)`. Therefore the four-point example by itself does not exhibit variable q^-2 fiber weights reviving a one-point cancellation. The parked-point mechanism accounts for pure exchange within each matching; matching exchange and reference monodromy remain part of the full formula.

Files: `formula_witness_reduced.json`, `formula_witness_full.json`, `formula_nonzero_control.json`. Each stores reference paths, each parked position's constant and colored inner polynomial, matching sums, and the per-record check status. No new braid family or scan was used.

This establishes a geometric decomposition of the pairing. It gives no sign-coherence, injectivity, or proof that a zero sum forces a splitting disk.
