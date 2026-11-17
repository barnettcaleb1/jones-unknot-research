# Parked-point decomposition: exact scope and normalization

This note addresses the theory behind Claude 20261103-043608(i). It does not audit the proposed general cap-slide/diagonal-torus identification or prove any splitting criterion.

## Ordered configuration space and the fiber character

Let D6 be the disk with the six fixed punctures removed. The forgetful map is on the **ordered** configuration space:

```
F_2(D6) -> D6,       (z,y) |-> y,
fiber over y = D6 minus {y}.
```

There is no operation “forget the first point” on unordered pairs without choosing the ordered double cover. In the intersection calculation that choice is supplied by the labeled source arcs; the two target/source matchings record the label permutation. The standard forgetful fibration is the one of [Fadell–Neuwirth, Configuration Spaces (1962)](https://journals.msp.org/mscand/article/view/2674). Bigelow's convention starts with unordered pairs and assigns t to a half exchange; see [The Lawrence–Krammer representation, §2](https://web.math.ucsb.edu/~bigelow/publications/08.pdf), also archived locally as `../width6_lift/bigelow_lkb.txt`.

On the fiber, a positive loop of z around a genuine puncture has character q. A positive loop around the parked point y makes one full relative rotation, hence two half exchanges, and has character t^2. On t=-q^-1 this extra puncture therefore has weight q^-2. This is a colored rank-one local-system intersection pairing; it need not be identified with an ordinary equal-weight Burau_6 matrix entry.

## A gauge-independent difference identity

Fix matching m and parked intersection y in c2 intersect gamma_(1-m). Choose a reference first intersection z0 in c1 intersect gamma_m. For another such z, form the CLOSED one-point path

```
ell_z = gamma_m[z0 -> z] followed by c1[z -> z0].
```

Paths use the chosen parametrized cycles. The parked point is on the OTHER target loop, not in its lobe, and is disjoint from both gamma_m and c1. Thus ell_z avoids y. Moving target points in either order is a homotopy because the two target supports are disjoint; the analogous source rectangle is valid because the source arcs are disjoint. Comparing the two full configuration loops consequently gives

```
a(z,y)-a(z0,y) = sum_(p=1..6) wind_p(ell_z) =: A_z,
b(z,y)-b(z0,y) = 2 wind_y(ell_z)             =: 2 W_z.
```

These identities do not use a polynomial coefficient or define winding by subtracting the measured b values. W_z is computed from the actual closed fiber path. “Winding of the path of z” must include the target return path (or an equivalent stated trivialization); winding of an unspecified open arc is not a gauge-independent integer.

Write a0=a(z0,y), b0=b(z0,y), and let epsilon0 be that reference configuration's raw intersection sign. Let eta_z be the ratio of the local crossing sign at z to that at z0. Then the exact generic parked summand is

```
epsilon0 q^a0 t^b0 * sum_z eta_z q^A_z (t^2)^W_z.
```

Summing this over y and the two matchings is the original geometric Phi. On the TL line it becomes

```
Phi(q,-q^-1)
  = sum_(m,y) epsilon0 (-1)^b0 q^(a0-b0)
                  * sum_z eta_z q^(A_z-2 W_z).
```

This explicitly retains all handle, anchor, parity, and endpoint corrections in the prefactor. The anchor must be obtained independently from its actual configuration path. For empty first-intersection sets the corresponding summand is simply absent.

If the instrument's base matching is mb, then b0 has parity delta_m=m XOR mb. Hence

```
w0_m(y) = (b0-delta_m)/2,
b(z,y)-delta_m = 2(w0_m(y)+W_z).
```

The constant depends on the matching and its reference/handles as well as y. A deck change shifts the common constants but leaves the difference identity unchanged. The factor q^-delta_m is part of q^(a0-b0); omitting it is harmless only if it is explicitly absorbed into a monomial prefactor.

## Matching-sign correction

The instrument's raw orientation sign is

```
epsilon(z,y) = sign(z) sign(y) (-1)^m * base_sign,
base_sign = sign(z_base) sign(y_base) (-1)^mb.
```

Since b mod2=m XOR mb, specialization contributes exactly the other factor needed to cancel the matching permutation sign:

```
epsilon(z,y) (-1)^b
  = sign(z) sign(y) sign(z_base) sign(y_base).
```

Thus no independent outside (-1)^m remains if the one-point pairings use their ordinary local crossing signs. A formula displaying (-1)^m can still be correct with compensating signed units, but that convention must be stated. The anchor-prefactor formula above avoids this ambiguity. Cancellation between local crossing signs and different parked summands remains possible; this sign identity gives no positivity theorem.

## The specified kernel configuration

For top C=(34)(56) and bottom C0'=(12)(45), the normalized one-cap TL/Burau Gram matrix at the identity is

```
M = [[0,1],
     [0,1]].
```

The 45 arc shares endpoint4 with 34 and endpoint5 with 56. Therefore it is incorrect to say all one-point entries vanish. The **12 column** vanishes, and det M=0. Applying a braid in the normalized Burau kernel to both bottom arcs preserves this matrix. Corresponding geometric cycle pairings can carry conventional nonzero scalar factors, which do not turn the nonzero second column into zero.

This still isolates the intended phenomenon: the ordinary one-point contribution involving the short arc is zero, while the parked-point weight may revive it. It does not force the resulting sum to be nonzero.

To compare a parked point y with a proposed adjacent real puncture p, the invariant quantity is wind_y(ell_z)-wind_p(ell_z) for the same closed fiber path. No “adjacent puncture” is canonical until p is specified. Equality or inequality of these integers measures whether the loop encloses the two locations equally, and by itself gives no coherence across the sum over parked intersections.

## Why the difference from an adjacent puncture is not the whole modification

Suppose, even for every first-intersection loop under consideration, that

```
wind_y(ell_z) = wind_p(ell_z).
```

The specialized fiber exponent is then

```
sum_r wind_r(ell_z) - 2 wind_y(ell_z)
  = sum_(r != p) wind_r(ell_z) - wind_p(ell_z).
```

Thus the resulting one-point character assigns **q^-1 to the genuine puncture p** and q to the other five genuine punctures. It is not the original equal-q Burau character. Vanishing for an ordinary Burau-kernel input therefore does not, merely from this equality of winding functions, imply vanishing of the modified pairing. No example claiming actual kernel revival under this equality is asserted here; this is a correction to the proposed implication.

A sufficient condition for a parked point to preserve an already-zero ordinary one-point sum is that wind_y(ell_z) be constant across all its first intersections. The extra weight is then one common Laurent monomial factor. In the anchored convention ell_(z0) is constant, so such a constant must be zero. This condition is different from equality with the generally varying winding about another puncture. More generally, any comparison with a chosen real puncture must retain both the unequal-color change at that puncture and the residual difference wind_y-wind_p.
