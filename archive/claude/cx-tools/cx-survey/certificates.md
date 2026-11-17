# Certificates: four-corner survey of EKT-type fusions

Conventions: ABSOLUTE bracket <empty>=1, <unknot>=delta=-A^2-A^-2; PD = spherogram PD_code (ccw from incoming under-strand), A-smoothing joins (a,b),(c,d); V = (-A^3)^(-w) <D>_reduced, t = A^-4, Jones keys are exponents of t^(1/2). Sites: local I = IdentityBraid(2), local e = ZeroTangle, k = k full twists; seam band site is rotated (local I = global ZeroTangle = fused, local e = global IdentityBraid(2) = unfused link). All four corners from the same diagram, same outside framing, no per-corner writhe normalisation. <K(m,n)> = A^(-6(s1 m + s2 n)) Q(x,y), Q = xy B00 + (1-x)y/delta B10 + x(1-y)/delta B01 + (1-x)(1-y)/delta^2 B11, x = A^(8 s1 m), y = A^(8 s2 n); V = unit * (a + b x + c y + d xy) with delta^3 a = B11, delta^3 b = delta B01 - B11, delta^3 c = delta B10 - B11, delta^3 d = delta^2 B00 - delta B10 - delta B01 + B11. Identity polynomials: B00 - (-A^3)^w0 delta (unknot-seed equation), delta B10 - B11, delta B01 - B11.

Site states: I = IdentityBraid(2), e = ZeroTangle (cup over cap), m = m full twists (BraidTangle([+-1]*2|m|,2)); at a rotated (seam) site the same local states are rotated by 90 degrees. B_ab: a = state of site 1, b = state of site 2 (sites listed in the title order). All four corners come from ONE diagram with only the two boxes replaced (same outside framing), absolute bracket, no per-corner normalisation. PD codes are spherogram PD_code() of K(0,0) (0-based labels); site edges are the PD edge labels of the two strands inside each box.

Realisations of the T / U site: "lit" = vertical 2-string box on the cable strands immediately next to the rotated IntegerTangle(+-3) (full twists inside the rotated T / U); "seed" = the box at the top of the EKT seed S inside T = omega(S) (resp. U = omega_bar(S)), omega(T) = ((T + 2) * 1) + 2 as in c1_nonunit_turnback.py; omega(I2) is isotopic rel boundary to IntegerTangle(3), omega_bar(I2) to IntegerTangle(-3).

## [1L] unfused LINK, sites (T-lit, U-lit)
_calibration; corners of the Jones-trivial link itself_

* Sites: site 1 = **T**, site 2 = **U**.
* Diagram: `braid_closure( (I2 | rot(IntegerTangle(3))) * (I2 | S1) * h * h * (S2 | I2) * (rot(IntegerTangle(-3)) | I2) )` with S1, S2 the two site boxes (h = BraidTangle([-2,-3,-1,-2],4), rot = .rotate(1), sigma2 = BraidTangle([2],4)).
* K(0,0): 14 crossings, 2 component(s), writhe w0 = -8.
* PD(K(0,0)) = `[[26, 20, 27, 19], [18, 26, 19, 25], [24, 18, 25, 17], [16, 13, 17, 0], [23, 12, 24, 13], [15, 6, 16, 7], [22, 5, 23, 6], [4, 21, 5, 22], [11, 20, 12, 21], [3, 14, 4, 15], [10, 27, 11, 14], [9, 2, 10, 3], [1, 8, 2, 9], [7, 0, 8, 1]]`
* Site edges in that PD: site 1 (T) = [17, 24], site 2 (U) = [3, 10].

**(1) Four raw corner brackets (absolute, same framing):**

| corner | state (site1, site2) | crossings | components | writhe of that diagram | bracket |
|---|---|---|---|---|---|
| B00 | (I, I) | 14 | 2 | -8 | `A^-4 + 2 + A^4` |
| B10 | (e, I) | 14 | 2 | -6 | `A^-18 + 2*A^-14 + 2*A^-10 + A^-6 - A^-2 - A^2` |
| B01 | (I, e) | 14 | 2 | 6 | `-A^-2 - A^2 + A^6 + 2*A^10 + 2*A^14 + A^18` |
| B11 | (e, e) | 14 | 2 | 0 | `A^-4 + 2 + A^4` |

**(2) Identity polynomials (exact):**

* u = (-A^3)^w0 = `A^-24`;  B00 - u*delta = `A^-26 + A^-22 + A^-4 + 2 + A^4`  -> unknot-seed equation **fails**
* delta*B10 - B11 = `-A^-20 - 3*A^-16 - 4*A^-12 - 3*A^-8 - A^-4`  -> **fails**  (c = 0)
* delta*B01 - B11 = `-A^4 - 3*A^8 - 4*A^12 - 3*A^16 - A^20`  -> **fails**  (b = 0)
* (single-site flatness at K(0,0): delta*B00 = B10 fails; delta*B00 = B01 fails)

**V(K(m,n)) structure** (V = unit * (a + b x + c y + d xy), x = A^(8 s1 m), y = A^(8 s2 n)):

* handedness s = (1, 1), writhe w(m,n) = w0 + 2*(1) m + 2*(1) n; sites ['parallel', 'parallel']; direct-bracket cross-check at [[1, 0], [0, 1], [1, 1], [2, -1]]: **all grid points match**
* delta^3 * a = `A^-4 + 2 + A^4`   [delta^2 | it: coefficient = (1)/delta]
* delta^3 * b = `-A^4 - 3*A^8 - 4*A^12 - 3*A^16 - A^20`   [delta^2 | it: coefficient = (-A^8 - A^12 - A^16)/delta]
* delta^3 * c = `-A^-20 - 3*A^-16 - 4*A^-12 - 3*A^-8 - A^-4`   [delta^2 | it: coefficient = (-A^-16 - A^-12 - A^-8)/delta]
* delta^3 * d = `A^-20 + 3*A^-16 + 4*A^-12 + 4*A^-8 + 4*A^-4 + 4 + 4*A^4 + 4*A^8 + 4*A^12 + 3*A^16 + A^20`   [delta^2 | it: coefficient = (A^-16 + A^-12 + A^-8 + A^-4 + 1 + A^4 + A^8 + A^12 + A^16)/delta]

**K(0,0):** V = `-t^(-13/2) - t^(-11/2)` (link)

Grid points (direct computation): K(1,0): V = -t^(-11/2) - t^(-7/2) - t^(-5/2) + t^(1/2); K(0,1): V = -t^(-17/2) - t^(-7/2); K(1,1): V = -t^(-15/2) - t^(-5/2) - t^(-1/2) + t^(3/2); K(2,-1): V = t^(-21/2) - t^(-15/2) - t^(-11/2) - t^(-7/2) - t^(-5/2) - t^(-1/2) + t^(1/2) + t^(5/2)

**Rational-slot corners C** (fusion `unfused`, see rational_slots.md): (E1) HOLDS, defect `0`; (E2) HOLDS, defect `0`.

## [1S] unfused LINK, sites (T-seed, U-seed)
_calibration; T = omega(S1), U = omega_bar(S2)_

* Sites: site 1 = **T**, site 2 = **U**.
* Diagram: `braid_closure( (I2 | rot(omega(S1))) * h * h * (rot(omega_bar(S2)) | I2) )` with S1, S2 the two site boxes (h = BraidTangle([-2,-3,-1,-2],4), rot = .rotate(1), sigma2 = BraidTangle([2],4)).
* K(0,0): 18 crossings, 2 component(s), writhe w0 = -8.
* PD(K(0,0)) = `[[32, 31, 33, 32], [30, 33, 31, 34], [34, 24, 35, 23], [22, 30, 23, 29], [28, 22, 29, 21], [20, 17, 21, 0], [27, 16, 28, 17], [19, 10, 20, 11], [26, 9, 27, 10], [8, 25, 9, 26], [15, 24, 16, 25], [7, 18, 8, 19], [14, 35, 15, 18], [3, 5, 4, 4], [5, 3, 6, 2], [13, 6, 14, 7], [1, 12, 2, 13], [11, 0, 12, 1]]`
* Site edges in that PD: site 1 (T) = [24, 32], site 2 (U) = [14, 4].

**(1) Four raw corner brackets (absolute, same framing):**

| corner | state (site1, site2) | crossings | components | writhe of that diagram | bracket |
|---|---|---|---|---|---|
| B00 | (I, I) | 18 | 2 | -8 | `A^-4 + 2 + A^4` |
| B10 | (e, I) | 18 | 3 | -8 | `-A^-6 - 3*A^-2 - 3*A^2 - A^6` |
| B01 | (I, e) | 18 | 3 | -8 | `-A^-6 - 3*A^-2 - 3*A^2 - A^6` |
| B11 | (e, e) | 18 | 4 | -8 | `A^-16 + A^-12 + A^-8 + 3*A^-4 + 4 + 3*A^4 + A^8 + A^12 + A^16` |

**(2) Identity polynomials (exact):**

* u = (-A^3)^w0 = `A^-24`;  B00 - u*delta = `A^-26 + A^-22 + A^-4 + 2 + A^4`  -> unknot-seed equation **fails**
* delta*B10 - B11 = `-A^-16 - A^-12 + A^-4 + 2 + A^4 - A^12 - A^16`  -> **fails**  (c = 0)
* delta*B01 - B11 = `-A^-16 - A^-12 + A^-4 + 2 + A^4 - A^12 - A^16`  -> **fails**  (b = 0)
* (single-site flatness at K(0,0): delta*B00 = B10 HOLDS; delta*B00 = B01 HOLDS)

**V(K(m,n)) structure** (V = unit * (a + b x + c y + d xy), x = A^(8 s1 m), y = A^(8 s2 n)):

* handedness s = (1, 1), writhe w(m,n) = w0 + 2*(-1) m + 2*(-1) n; sites ['antiparallel', 'antiparallel']; direct-bracket cross-check at [[1, 0], [0, 1], [1, 1], [2, -1]]: **all grid points match**
* delta^3 * a = `A^-16 + A^-12 + A^-8 + 3*A^-4 + 4 + 3*A^4 + A^8 + A^12 + A^16`   [delta^2 | it: coefficient = (A^-12 - A^-8 + 2*A^-4 + 2*A^4 - A^8 + A^12)/delta]
* delta^3 * b = `-A^-16 - A^-12 + A^-4 + 2 + A^4 - A^12 - A^16`   [delta^2 | it: coefficient = (-A^-12 + A^-8 - A^-4 + 2 - A^4 + A^8 - A^12)/delta]
* delta^3 * c = `-A^-16 - A^-12 + A^-4 + 2 + A^4 - A^12 - A^16`   [delta^2 | it: coefficient = (-A^-12 + A^-8 - A^-4 + 2 - A^4 + A^8 - A^12)/delta]
* delta^3 * d = `A^-16 + A^-12 - A^-4 - 2 - A^4 + A^12 + A^16`   [delta^2 | it: coefficient = (A^-12 - A^-8 + A^-4 - 2 + A^4 - A^8 + A^12)/delta]

**K(0,0):** V = `-t^(-13/2) - t^(-11/2)` (link)

Grid points (direct computation): K(1,0): V = -t^(-13/2) - t^(-11/2); K(0,1): V = -t^(-13/2) - t^(-11/2); K(1,1): V = -t^(-25/2) + 2*t^(-23/2) - t^(-21/2) + t^(-19/2) - t^(-17/2) - t^(-15/2) - 2*t^(-11/2) + 2*t^(-9/2) - t^(-7/2); K(2,-1): V = t^(-25/2) - 2*t^(-23/2) + 2*t^(-21/2) - 3*t^(-19/2) + 2*t^(-17/2) - t^(-13/2) + t^(-11/2) - 3*t^(-9/2) + 2*t^(-7/2) - 2*t^(-5/2) + t^(-3/2)

**Rational-slot corners C** (fusion `unfused`, see rational_slots.md): (E1) HOLDS, defect `0`; (E2) HOLDS, defect `0`.

## [2L] H2 knot (fixed sigma2 at the seam), sites (T-lit, U-lit)
_designer K(0,0) of c4_two_site_candidate.md; literal boxes on strands 3,4 and 1,2_

* Sites: site 1 = **T**, site 2 = **U**.
* Diagram: `braid_closure( (I2 | rot(IntegerTangle(3))) * (I2 | S1) * h * sigma2 * h * (S2 | I2) * (rot(IntegerTangle(-3)) | I2) )` with S1, S2 the two site boxes (h = BraidTangle([-2,-3,-1,-2],4), rot = .rotate(1), sigma2 = BraidTangle([2],4)).
* K(0,0): 15 crossings, 1 component(s), writhe w0 = -7.
* PD(K(0,0)) = `[[10, 18, 11, 17], [16, 10, 17, 9], [8, 16, 9, 15], [14, 29, 15, 0], [7, 28, 8, 29], [13, 22, 14, 23], [6, 21, 7, 22], [5, 21, 6, 20], [4, 19, 5, 20], [27, 18, 28, 19], [3, 12, 4, 13], [26, 11, 27, 12], [25, 2, 26, 3], [1, 24, 2, 25], [23, 0, 24, 1]]`
* Site edges in that PD: site 1 (T) = [15, 8], site 2 (U) = [3, 26].

**(1) Four raw corner brackets (absolute, same framing):**

| corner | state (site1, site2) | crossings | components | writhe of that diagram | bracket |
|---|---|---|---|---|---|
| B00 | (I, I) | 15 | 1 | -7 | `A^-15 + A^-7 + A + A^5 - A^9 - A^17` |
| B10 | (e, I) | 15 | 1 | -5 | `A^-13 + A^-9 + A^-5 - A^3` |
| B01 | (I, e) | 15 | 1 | 7 | `-A^3 + A^11 + A^15 + A^19` |
| B11 | (e, e) | 15 | 1 | 1 | `A + A^5` |

**(2) Identity polynomials (exact):**

* u = (-A^3)^w0 = `-A^-21`;  B00 - u*delta = `-A^-23 - A^-19 + A^-15 + A^-7 + A + A^5 - A^9 - A^17`  -> unknot-seed equation **fails**
* delta*B10 - B11 = `-A^-15 - 2*A^-11 - 2*A^-7 - A^-3`  -> **fails**  (c = 0)
* delta*B01 - B11 = `-A^9 - 2*A^13 - 2*A^17 - A^21`  -> **fails**  (b = 0)
* (single-site flatness at K(0,0): delta*B00 = B10 fails; delta*B00 = B01 fails)

**V(K(m,n)) structure** (V = unit * (a + b x + c y + d xy), x = A^(8 s1 m), y = A^(8 s2 n)):

* handedness s = (1, 1), writhe w(m,n) = w0 + 2*(1) m + 2*(1) n; sites ['parallel', 'parallel']; direct-bracket cross-check at [[1, 0], [0, 1], [1, 1], [2, -1]]: **all grid points match**
* delta^3 * a = `A + A^5`   [delta | it: coefficient = (-A^3)/delta^2]
* delta^3 * b = `-A^9 - 2*A^13 - 2*A^17 - A^21`   [delta | it: coefficient = (A^11 + A^15 + A^19)/delta^2]
* delta^3 * c = `-A^-15 - 2*A^-11 - 2*A^-7 - A^-3`   [delta | it: coefficient = (A^-13 + A^-9 + A^-5)/delta^2]
* delta^3 * d = `A^-19 + 3*A^-15 + 4*A^-11 + 4*A^-7 + 3*A^-3 + 2*A + A^5`   [delta | it: coefficient = (-A^-17 - 2*A^-13 - 2*A^-9 - 2*A^-5 - A^-1 - A^3)/delta^2]

**K(0,0):** V = `-t^-9 + t^-8 - 2*t^-7 + 3*t^-6 - 2*t^-5 + 2*t^-4 - t^-3 + t^-2`, det = 13; HFK total rank 13, genus 2; spherogram simplify -> 7 crossings; snappy identify ['m340(0,0)', '7_3(0,0)', 'K5_20(0,0)', 'K7a5(0,0)']; volume 4.592126

Grid points (direct computation): K(1,0): V = -t^-8 + t^-7 - 2*t^-6 + 3*t^-5 - 3*t^-4 + 4*t^-3 - 2*t^-2 + 2*t^-1 - 1, det 19; K(0,1): V = -t^-6 + t^-5 - t^-4 + 2*t^-3 - t^-2 + t^-1, det 7; K(1,1): V = -t^-5 + t^-4 - t^-3 + 2*t^-2 - t^-1 + 2 - t, det 9; K(2,-1): V = -t^-10 + t^-9 - 2*t^-8 + 3*t^-7 - 4*t^-6 + 5*t^-5 - 5*t^-4 + 6*t^-3 - 4*t^-2 + 4*t^-1 - 2 + t - t^2, det 39

**Rational-slot corners C** (fusion `seam_sigma2 (H2; configs 2L,2S)`, see rational_slots.md): (E1) HOLDS, defect `0`; (E2) fails, defect `-A^-13 + A^-9 - 2*A^-5 + 2*A^-1 - 2*A^3 + 2*A^7 - A^11 + A^15`.

## [2S] H2 knot (fixed sigma2 at the seam), sites (T-seed, U-seed)
_same knot type; EKT seed sites inside omega / omega_bar_

* Sites: site 1 = **T**, site 2 = **U**.
* Diagram: `braid_closure( (I2 | rot(omega(S1))) * h * sigma2 * h * (rot(omega_bar(S2)) | I2) )` with S1, S2 the two site boxes (h = BraidTangle([-2,-3,-1,-2],4), rot = .rotate(1), sigma2 = BraidTangle([2],4)).
* K(0,0): 19 crossings, 1 component(s), writhe w0 = -7.
* PD(K(0,0)) = `[[16, 15, 17, 16], [14, 17, 15, 18], [18, 26, 19, 25], [24, 14, 25, 13], [12, 24, 13, 23], [22, 37, 23, 0], [11, 36, 12, 37], [21, 30, 22, 31], [10, 29, 11, 30], [9, 29, 10, 28], [8, 27, 9, 28], [35, 26, 36, 27], [7, 20, 8, 21], [34, 19, 35, 20], [3, 5, 4, 4], [5, 3, 6, 2], [33, 6, 34, 7], [1, 32, 2, 33], [31, 0, 32, 1]]`
* Site edges in that PD: site 1 (T) = [26, 16], site 2 (U) = [34, 4].

**(1) Four raw corner brackets (absolute, same framing):**

| corner | state (site1, site2) | crossings | components | writhe of that diagram | bracket |
|---|---|---|---|---|---|
| B00 | (I, I) | 19 | 1 | -7 | `A^-15 + A^-7 + A + A^5 - A^9 - A^17` |
| B10 | (e, I) | 19 | 2 | -7 | `-A^-13 + A^-9 - 2*A^-5 - 3*A^3 - A^7 + A^11 - A^15 + 2*A^19 - A^23 + A^27` |
| B01 | (I, e) | 19 | 2 | -7 | `-A^-25 + A^-21 - 2*A^-17 + A^-13 - A^-9 - 3*A^3 + A^7 - A^11 + A^15` |
| B11 | (e, e) | 19 | 3 | -7 | `A^-23 - 2*A^-19 + 4*A^-15 - 3*A^-11 + 4*A^-7 - A^-3 + 2*A + 4*A^5 - 3*A^9 + 4*A^13 - 3*A^17 + 2*A^21 - A^25` |

**(2) Identity polynomials (exact):**

* u = (-A^3)^w0 = `-A^-21`;  B00 - u*delta = `-A^-23 - A^-19 + A^-15 + A^-7 + A + A^5 - A^9 - A^17`  -> unknot-seed equation **fails**
* delta*B10 - B11 = `-A^-23 + 2*A^-19 - 3*A^-15 + 3*A^-11 - 3*A^-7 + 3*A^-3 + A + 3*A^9 - 4*A^13 + 2*A^17 - 3*A^21 + A^25 - A^29`  -> **fails**  (c = 0)
* delta*B01 - B11 = `A^-27 - A^-23 + 3*A^-19 - 3*A^-15 + 3*A^-11 - 3*A^-7 + A^-3 + A - 2*A^5 + 3*A^9 - 4*A^13 + 2*A^17 - 2*A^21 + A^25`  -> **fails**  (b = 0)
* (single-site flatness at K(0,0): delta*B00 = B10 fails; delta*B00 = B01 fails)

**V(K(m,n)) structure** (V = unit * (a + b x + c y + d xy), x = A^(8 s1 m), y = A^(8 s2 n)):

* handedness s = (1, 1), writhe w(m,n) = w0 + 2*(-1) m + 2*(-1) n; sites ['antiparallel', 'antiparallel']; direct-bracket cross-check at [[1, 0], [0, 1], [1, 1], [2, -1]]: **all grid points match**
* delta^3 * a = `A^-23 - 2*A^-19 + 4*A^-15 - 3*A^-11 + 4*A^-7 - A^-3 + 2*A + 4*A^5 - 3*A^9 + 4*A^13 - 3*A^17 + 2*A^21 - A^25`   [delta | it: coefficient = (-A^-21 + 3*A^-17 - 7*A^-13 + 10*A^-9 - 14*A^-5 + 15*A^-1 - 17*A^3 + 13*A^7 - 10*A^11 + 6*A^15 - 3*A^19 + A^23)/delta^2]
* delta^3 * b = `A^-27 - A^-23 + 3*A^-19 - 3*A^-15 + 3*A^-11 - 3*A^-7 + A^-3 + A - 2*A^5 + 3*A^9 - 4*A^13 + 2*A^17 - 2*A^21 + A^25`   [delta | it: coefficient = (-A^-25 + 2*A^-21 - 5*A^-17 + 8*A^-13 - 11*A^-9 + 14*A^-5 - 15*A^-1 + 14*A^3 - 12*A^7 + 9*A^11 - 5*A^15 + 3*A^19 - A^23)/delta^2]
* delta^3 * c = `-A^-23 + 2*A^-19 - 3*A^-15 + 3*A^-11 - 3*A^-7 + 3*A^-3 + A + 3*A^9 - 4*A^13 + 2*A^17 - 3*A^21 + A^25 - A^29`   [delta | it: coefficient = (A^-21 - 3*A^-17 + 6*A^-13 - 9*A^-9 + 12*A^-5 - 15*A^-1 + 14*A^3 - 14*A^7 + 11*A^11 - 7*A^15 + 5*A^19 - 2*A^23 + A^27)/delta^2]
* delta^3 * d = `-A^-27 + A^-23 - 2*A^-19 + 4*A^-15 - A^-11 + 4*A^-7 - A^-3 - A - 4*A^9 + 2*A^13 - 3*A^17 + 2*A^21 - A^25 + A^29`   [delta | it: coefficient = (A^-25 - 2*A^-21 + 4*A^-17 - 8*A^-13 + 9*A^-9 - 13*A^-5 + 14*A^-1 - 13*A^3 + 13*A^7 - 9*A^11 + 7*A^15 - 4*A^19 + 2*A^23 - A^27)/delta^2]

**K(0,0):** V = `-t^-9 + t^-8 - 2*t^-7 + 3*t^-6 - 2*t^-5 + 2*t^-4 - t^-3 + t^-2`, det = 13; HFK total rank 13, genus 2; spherogram simplify -> 7 crossings; snappy identify ['m340(0,0)', '7_3(0,0)', 'K5_20(0,0)', 'K7a5(0,0)']; volume 4.592126

Grid points (direct computation): K(1,0): V = t^-13 - 3*t^-12 + 5*t^-11 - 8*t^-10 + 9*t^-9 - 10*t^-8 + 9*t^-7 - 6*t^-6 + 5*t^-5 - 2*t^-4 + t^-3, det 59; K(0,1): V = -t^-11 + 2*t^-10 - 5*t^-9 + 8*t^-8 - 11*t^-7 + 14*t^-6 - 13*t^-5 + 12*t^-4 - 9*t^-3 + 6*t^-2 - 3*t^-1 + 1, det 85; K(1,1): V = t^-15 - 4*t^-14 + 10*t^-13 - 20*t^-12 + 31*t^-11 - 44*t^-10 + 53*t^-9 - 56*t^-8 + 54*t^-7 - 44*t^-6 + 33*t^-5 - 21*t^-4 + 11*t^-3 - 4*t^-2 + t^-1, det 387; K(2,-1): V = t^-14 - 4*t^-13 + 10*t^-12 - 21*t^-11 + 36*t^-10 - 54*t^-9 + 70*t^-8 - 82*t^-7 + 85*t^-6 - 77*t^-5 + 64*t^-4 - 45*t^-3 + 28*t^-2 - 14*t^-1 + 5 - t, det 597

**Rational-slot corners C** (fusion `seam_sigma2 (H2; configs 2L,2S)`, see rational_slots.md): (E1) HOLDS, defect `0`; (E2) fails, defect `-A^-13 + A^-9 - 2*A^-5 + 2*A^-1 - 2*A^3 + 2*A^7 - A^11 + A^15`.

## [3] c1 anchor (seed R(25,-9), seam band fusion), sites (seam, T-seed)
_c1_nonunit_turnback.py K(m,n) = cl(A_n h C_m h B); corners = its corner(eps,eta)_

* Sites: site 1 = **seam**, site 2 = **T**.
* Diagram: `braid_closure( (I2 | rot(omega(S2 * RationalTangle(25,-9)))) * h * (I1 | rot(S1) | I1) * h * (rot(IntegerTangle(-3)) | I2) )` with S1, S2 the two site boxes (h = BraidTangle([-2,-3,-1,-2],4), rot = .rotate(1), sigma2 = BraidTangle([2],4)).
* K(0,0): 24 crossings, 1 component(s), writhe w0 = 0.
* PD(K(0,0)) = `[[7, 28, 8, 29], [29, 8, 30, 9], [9, 32, 10, 33], [17, 11, 18, 10], [11, 17, 12, 16], [15, 13, 16, 12], [13, 31, 14, 30], [31, 15, 32, 14], [18, 34, 19, 33], [34, 20, 35, 19], [20, 28, 21, 27], [26, 35, 27, 36], [36, 25, 37, 26], [24, 47, 25, 0], [37, 47, 38, 46], [23, 40, 24, 41], [38, 40, 39, 39], [4, 6, 5, 5], [45, 7, 46, 6], [3, 22, 4, 23], [44, 21, 45, 22], [43, 2, 44, 3], [1, 42, 2, 43], [41, 0, 42, 1]]`
* Site edges in that PD: site 1 (seam) = [39, 5], site 2 (T) = [7, 33].

**(1) Four raw corner brackets (absolute, same framing):**

| corner | state (site1, site2) | crossings | components | writhe of that diagram | bracket |
|---|---|---|---|---|---|
| B00 | (I, I) | 24 | 1 | 0 | `-A^-2 - A^2` |
| B10 | (e, I) | 24 | 2 | 0 | `-A^-24 + A^-8 + A^-4 + 3 + A^4 - A^16` |
| B01 | (I, e) | 24 | 2 | 0 | `A^-32 - 3*A^-28 + 6*A^-24 - 12*A^-20 + 17*A^-16 - 22*A^-12 + 23*A^-8 - 19*A^-4 + 14 - 10*A^8 + 19*A^12 - 23*A^16 + 23*A^20 - 18*A^24 + 13*A^28 - 7*A^32 + 3*A^36 - A^40` |
| B11 | (e, e) | 24 | 3 | -8 | `A^-26 + A^-22 - A^-10 - 2*A^-6 - 4*A^-2 - 4*A^2 - A^6 + A^14 + A^18` |

**(2) Identity polynomials (exact):**

* u = (-A^3)^w0 = `1`;  B00 - u*delta = `0`  -> unknot-seed equation **HOLDS**
* delta*B10 - B11 = `0`  -> **HOLDS**  (c = 0)
* delta*B01 - B11 = `-A^-34 + 2*A^-30 - 4*A^-26 + 5*A^-22 - 5*A^-18 + 5*A^-14 - 2*A^-6 + 9*A^-2 - 10*A^2 + 11*A^6 - 9*A^10 + 3*A^14 - A^18 - 5*A^22 + 5*A^26 - 6*A^30 + 4*A^34 - 2*A^38 + A^42`  -> **fails**  (b = 0)
* (single-site flatness at K(0,0): delta*B00 = B10 fails; delta*B00 = B01 fails)

**V(K(m,n)) structure** (V = unit * (a + b x + c y + d xy), x = A^(8 s1 m), y = A^(8 s2 n)):

* handedness s = (1, 1), writhe w(m,n) = w0 + 2*(-1) m + 2*(-1) n; sites ['antiparallel', 'antiparallel']; direct-bracket cross-check at [[1, 0], [0, 1], [1, 1], [2, -1]]: **all grid points match**
* delta^3 * a = `A^-26 + A^-22 - A^-10 - 2*A^-6 - 4*A^-2 - 4*A^2 - A^6 + A^14 + A^18`   [delta^3 | it: coefficient = -A^-20 + 2*A^-16 - 3*A^-12 + 4*A^-8 - 4*A^-4 + 5 - 3*A^4 + 2*A^8 - A^12]
* delta^3 * b = `-A^-34 + 2*A^-30 - 4*A^-26 + 5*A^-22 - 5*A^-18 + 5*A^-14 - 2*A^-6 + 9*A^-2 - 10*A^2 + 11*A^6 - 9*A^10 + 3*A^14 - A^18 - 5*A^22 + 5*A^26 - 6*A^30 + 4*A^34 - 2*A^38 + A^42`   [delta^2 | it: coefficient = (-A^-30 + 4*A^-26 - 11*A^-22 + 23*A^-18 - 40*A^-14 + 62*A^-10 - 84*A^-6 + 104*A^-2 - 115*A^2 + 116*A^6 - 106*A^10 + 87*A^14 - 65*A^18 + 42*A^22 - 24*A^26 + 11*A^30 - 4*A^34 + A^38)/delta]
* delta^3 * c = `0`   [delta^3 | it: coefficient = 0]
* delta^3 * d = `A^-34 - 2*A^-30 + 3*A^-26 - 6*A^-22 + 5*A^-18 - 5*A^-14 + A^-10 + 3*A^-6 - 8*A^-2 + 11*A^2 - 11*A^6 + 9*A^10 - 4*A^14 + 5*A^22 - 5*A^26 + 6*A^30 - 4*A^34 + 2*A^38 - A^42`   [delta^2 | it: coefficient = (A^-30 - 4*A^-26 + 10*A^-22 - 22*A^-18 + 39*A^-14 - 61*A^-10 + 84*A^-6 - 104*A^-2 + 116*A^2 - 117*A^6 + 107*A^10 - 88*A^14 + 65*A^18 - 42*A^22 + 24*A^26 - 11*A^30 + 4*A^34 - A^38)/delta]

**K(0,0):** V = `1`, det = 1; HFK total rank 1, genus 0; spherogram simplify -> 0 crossings; snappy identify []; volume -0.0

Grid points (direct computation): K(1,0): V = t^-5 - 2*t^-4 + 2*t^-3 - 2*t^-2 + t^-1 + 1 - t + 2*t^2 - 2*t^3 + 2*t^4 - t^5, det 1; K(0,1): V = t^-11 - 5*t^-10 + 15*t^-9 - 35*t^-8 + 66*t^-7 - 107*t^-6 + 153*t^-5 - 195*t^-4 + 224*t^-3 - 233*t^-2 + 220*t^-1 - 187 + 145*t - 100*t^2 + 61*t^3 - 32*t^4 + 14*t^5 - 5*t^6 + t^7, det 1799; K(1,1): V = t^-13 - 5*t^-12 + 15*t^-11 - 35*t^-10 + 66*t^-9 - 107*t^-8 + 153*t^-7 - 195*t^-6 + 225*t^-5 - 235*t^-4 + 222*t^-3 - 190*t^-2 + 146*t^-1 - 99 + 60*t - 30*t^2 + 12*t^3 - 3*t^4, det 1799; K(2,-1): V = -t^-13 + 5*t^-12 - 15*t^-11 + 35*t^-10 - 66*t^-9 + 107*t^-8 - 152*t^-7 + 193*t^-6 - 221*t^-5 + 229*t^-4 - 217*t^-3 + 186*t^-2 - 145*t^-1 + 103 - 64*t + 36*t^2 - 17*t^3 + 7*t^4 - 2*t^5, det 1801

**Rational-slot corners C** (fusion `seam_band (c1 anchor; configs 3,3b,4L,4S,6)`, see rational_slots.md): (E1) HOLDS, defect `0`; (E2) fails, defect `-A^-12 + A^-8 - 2*A^-4 + 2 - 2*A^4 + 2*A^8 - A^12 + A^16`.

## [3b] c1 anchor, sites (T-seed, U-seed)  [the anchor knot with the two EKT seed sites]
_seam band fixed in its fused state_

* Sites: site 1 = **T**, site 2 = **U**.
* Diagram: `braid_closure( (I2 | rot(omega(S1 * RationalTangle(25,-9)))) * h * (I1 | rot(I2) | I1)  [seam band fixed fused = ZeroTangle] * h * (rot(omega_bar(S2)) | I2) )` with S1, S2 the two site boxes (h = BraidTangle([-2,-3,-1,-2],4), rot = .rotate(1), sigma2 = BraidTangle([2],4)).
* K(0,0): 26 crossings, 1 component(s), writhe w0 = 2.
* PD(K(0,0)) = `[[11, 32, 12, 33], [33, 12, 34, 13], [13, 36, 14, 37], [21, 15, 22, 14], [15, 21, 16, 20], [19, 17, 20, 16], [17, 35, 18, 34], [35, 19, 36, 18], [22, 38, 23, 37], [38, 24, 39, 23], [24, 32, 25, 31], [30, 39, 31, 40], [40, 29, 41, 30], [28, 51, 29, 0], [41, 51, 42, 50], [27, 44, 28, 45], [42, 44, 43, 43], [8, 10, 9, 9], [49, 11, 50, 10], [7, 26, 8, 27], [48, 25, 49, 26], [3, 5, 4, 4], [5, 3, 6, 2], [47, 6, 48, 7], [1, 46, 2, 47], [45, 0, 46, 1]]`
* Site edges in that PD: site 1 (T) = [11, 37], site 2 (U) = [48, 4].

**(1) Four raw corner brackets (absolute, same framing):**

| corner | state (site1, site2) | crossings | components | writhe of that diagram | bracket |
|---|---|---|---|---|---|
| B00 | (I, I) | 26 | 1 | 2 | `-A^4 - A^8` |
| B10 | (e, I) | 26 | 2 | 2 | `A^-26 - 3*A^-22 + 6*A^-18 - 12*A^-14 + 17*A^-10 - 22*A^-6 + 23*A^-2 - 19*A^2 + 14*A^6 - 10*A^14 + 19*A^18 - 23*A^22 + 23*A^26 - 18*A^30 + 13*A^34 - 7*A^38 + 3*A^42 - A^46` |
| B01 | (I, e) | 26 | 2 | 2 | `A^2 + 2*A^6 + A^10` |
| B11 | (e, e) | 26 | 3 | 2 | `-A^-36 + 4*A^-32 - 10*A^-28 + 20*A^-24 - 32*A^-20 + 47*A^-16 - 56*A^-12 + 58*A^-8 - 50*A^-4 + 29 - 6*A^4 - 27*A^8 + 45*A^12 - 59*A^16 + 58*A^20 - 50*A^24 + 36*A^28 - 22*A^32 + 11*A^36 - 4*A^40 + A^44` |

**(2) Identity polynomials (exact):**

* u = (-A^3)^w0 = `A^6`;  B00 - u*delta = `0`  -> unknot-seed equation **HOLDS**
* delta*B10 - B11 = `A^-36 - 4*A^-32 + 9*A^-28 - 18*A^-24 + 29*A^-20 - 41*A^-16 + 51*A^-12 - 53*A^-8 + 49*A^-4 - 33 + 11*A^4 + 13*A^8 - 35*A^12 + 50*A^16 - 54*A^20 + 50*A^24 - 41*A^28 + 27*A^32 - 17*A^36 + 8*A^40 - 3*A^44 + A^48`  -> **fails**  (c = 0)
* delta*B01 - B11 = `A^-36 - 4*A^-32 + 10*A^-28 - 20*A^-24 + 32*A^-20 - 47*A^-16 + 56*A^-12 - 58*A^-8 + 50*A^-4 - 30 + 3*A^4 + 24*A^8 - 46*A^12 + 59*A^16 - 58*A^20 + 50*A^24 - 36*A^28 + 22*A^32 - 11*A^36 + 4*A^40 - A^44`  -> **fails**  (b = 0)
* (single-site flatness at K(0,0): delta*B00 = B10 fails; delta*B00 = B01 HOLDS)

**V(K(m,n)) structure** (V = unit * (a + b x + c y + d xy), x = A^(8 s1 m), y = A^(8 s2 n)):

* handedness s = (1, 1), writhe w(m,n) = w0 + 2*(-1) m + 2*(-1) n; sites ['antiparallel', 'antiparallel']; direct-bracket cross-check at [[1, 0], [0, 1], [1, 1], [2, -1]]: **all grid points match**
* delta^3 * a = `-A^-36 + 4*A^-32 - 10*A^-28 + 20*A^-24 - 32*A^-20 + 47*A^-16 - 56*A^-12 + 58*A^-8 - 50*A^-4 + 29 - 6*A^4 - 27*A^8 + 45*A^12 - 59*A^16 + 58*A^20 - 50*A^24 + 36*A^28 - 22*A^32 + 11*A^36 - 4*A^40 + A^44`   [delta | it: coefficient = (A^-34 - 5*A^-30 + 15*A^-26 - 35*A^-22 + 67*A^-18 - 114*A^-14 + 170*A^-10 - 228*A^-6 + 278*A^-2 - 307*A^2 + 313*A^6 - 286*A^10 + 241*A^14 - 182*A^18 + 124*A^22 - 74*A^26 + 38*A^30 - 16*A^34 + 5*A^38 - A^42)/delta^2]
* delta^3 * b = `A^-36 - 4*A^-32 + 10*A^-28 - 20*A^-24 + 32*A^-20 - 47*A^-16 + 56*A^-12 - 58*A^-8 + 50*A^-4 - 30 + 3*A^4 + 24*A^8 - 46*A^12 + 59*A^16 - 58*A^20 + 50*A^24 - 36*A^28 + 22*A^32 - 11*A^36 + 4*A^40 - A^44`   [delta | it: coefficient = (-A^-34 + 5*A^-30 - 15*A^-26 + 35*A^-22 - 67*A^-18 + 114*A^-14 - 170*A^-10 + 228*A^-6 - 278*A^-2 + 308*A^2 - 311*A^6 + 287*A^10 - 241*A^14 + 182*A^18 - 124*A^22 + 74*A^26 - 38*A^30 + 16*A^34 - 5*A^38 + A^42)/delta^2]
* delta^3 * c = `A^-36 - 4*A^-32 + 9*A^-28 - 18*A^-24 + 29*A^-20 - 41*A^-16 + 51*A^-12 - 53*A^-8 + 49*A^-4 - 33 + 11*A^4 + 13*A^8 - 35*A^12 + 50*A^16 - 54*A^20 + 50*A^24 - 41*A^28 + 27*A^32 - 17*A^36 + 8*A^40 - 3*A^44 + A^48`   [delta | it: coefficient = (-A^-34 + 5*A^-30 - 14*A^-26 + 32*A^-22 - 61*A^-18 + 102*A^-14 - 153*A^-10 + 206*A^-6 - 255*A^-2 + 288*A^2 - 299*A^6 + 286*A^10 - 251*A^14 + 201*A^18 - 147*A^22 + 97*A^26 - 56*A^30 + 29*A^34 - 12*A^38 + 4*A^42 - A^46)/delta^2]
* delta^3 * d = `-A^-36 + 4*A^-32 - 9*A^-28 + 18*A^-24 - 29*A^-20 + 41*A^-16 - 51*A^-12 + 53*A^-8 - 49*A^-4 + 33 - 11*A^4 - 13*A^8 + 35*A^12 - 50*A^16 + 54*A^20 - 50*A^24 + 41*A^28 - 27*A^32 + 17*A^36 - 8*A^40 + 3*A^44 - A^48`   [delta | it: coefficient = (A^-34 - 5*A^-30 + 14*A^-26 - 32*A^-22 + 61*A^-18 - 102*A^-14 + 153*A^-10 - 206*A^-6 + 255*A^-2 - 288*A^2 + 299*A^6 - 286*A^10 + 251*A^14 - 201*A^18 + 147*A^22 - 97*A^26 + 56*A^30 - 29*A^34 + 12*A^38 - 4*A^42 + A^46)/delta^2]

**K(0,0):** V = `1`, det = 1; HFK total rank 1, genus 0; spherogram simplify -> 0 crossings; snappy identify []; volume 0.0

Grid points (direct computation): K(1,0): V = t^-11 - 5*t^-10 + 15*t^-9 - 35*t^-8 + 66*t^-7 - 107*t^-6 + 153*t^-5 - 195*t^-4 + 224*t^-3 - 233*t^-2 + 220*t^-1 - 187 + 145*t - 100*t^2 + 61*t^3 - 32*t^4 + 14*t^5 - 5*t^6 + t^7, det 1799; K(0,1): V = 1, det 1; K(1,1): V = t^-13 - 6*t^-12 + 22*t^-11 - 62*t^-10 + 141*t^-9 - 273*t^-8 + 463*t^-7 - 699*t^-6 + 953*t^-5 - 1184*t^-4 + 1346*t^-3 - 1405*t^-2 + 1350*t^-1 - 1191 + 965*t - 714*t^2 + 479*t^3 - 288*t^4 + 153*t^5 - 70*t^6 + 26*t^7 - 7*t^8 + t^9, det 11799; K(2,-1): V = t^-12 - 6*t^-11 + 23*t^-10 - 66*t^-9 + 153*t^-8 - 304*t^-7 + 528*t^-6 - 820*t^-5 + 1153*t^-4 - 1478*t^-3 + 1740*t^-2 - 1887*t^-1 + 1889 - 1744*t + 1486*t^2 - 1163*t^3 + 833*t^4 - 542*t^5 + 316*t^6 - 163*t^7 + 72*t^8 - 26*t^9 + 7*t^10 - t^11, det 16401

**Rational-slot corners C** (fusion `seam_band (c1 anchor; configs 3,3b,4L,4S,6)`, see rational_slots.md): (E1) HOLDS, defect `0`; (E2) fails, defect `-A^-12 + A^-8 - 2*A^-4 + 2 - 2*A^4 + 2*A^8 - A^12 + A^16`.

## [4L] c1 anchor, sites (seam, U-lit)

* Sites: site 1 = **seam**, site 2 = **U**.
* Diagram: `braid_closure( (I2 | rot(omega(RationalTangle(25,-9)))) * h * (I1 | rot(S1) | I1) * h * (S2 | I2) * (rot(IntegerTangle(-3)) | I2) )` with S1, S2 the two site boxes (h = BraidTangle([-2,-3,-1,-2],4), rot = .rotate(1), sigma2 = BraidTangle([2],4)).
* K(0,0): 24 crossings, 1 component(s), writhe w0 = 0.
* PD(K(0,0)) = `[[7, 28, 8, 29], [29, 8, 30, 9], [9, 32, 10, 33], [17, 11, 18, 10], [11, 17, 12, 16], [15, 13, 16, 12], [13, 31, 14, 30], [31, 15, 32, 14], [18, 34, 19, 33], [34, 20, 35, 19], [20, 28, 21, 27], [26, 35, 27, 36], [36, 25, 37, 26], [24, 47, 25, 0], [37, 47, 38, 46], [23, 40, 24, 41], [38, 40, 39, 39], [4, 6, 5, 5], [45, 7, 46, 6], [3, 22, 4, 23], [44, 21, 45, 22], [43, 2, 44, 3], [1, 42, 2, 43], [41, 0, 42, 1]]`
* Site edges in that PD: site 1 (seam) = [39, 5], site 2 (U) = [3, 44].

**(1) Four raw corner brackets (absolute, same framing):**

| corner | state (site1, site2) | crossings | components | writhe of that diagram | bracket |
|---|---|---|---|---|---|
| B00 | (I, I) | 24 | 1 | 0 | `-A^-2 - A^2` |
| B10 | (e, I) | 24 | 2 | 0 | `-A^-24 + A^-8 + A^-4 + 3 + A^4 - A^16` |
| B01 | (I, e) | 24 | 1 | 6 | `1 - A^8 - A^12 - A^16` |
| B11 | (e, e) | 24 | 2 | 6 | `-A^-2 - A^2 + A^6 + 2*A^10 + 2*A^14 + A^18` |

**(2) Identity polynomials (exact):**

* u = (-A^3)^w0 = `1`;  B00 - u*delta = `0`  -> unknot-seed equation **HOLDS**
* delta*B10 - B11 = `A^-26 + A^-22 - A^-10 - 2*A^-6 - 3*A^-2 - 3*A^2 - 2*A^6 - 2*A^10 - A^14`  -> **fails**  (c = 0)
* delta*B01 - B11 = `0`  -> **HOLDS**  (b = 0)
* (single-site flatness at K(0,0): delta*B00 = B10 fails; delta*B00 = B01 fails)

**V(K(m,n)) structure** (V = unit * (a + b x + c y + d xy), x = A^(8 s1 m), y = A^(8 s2 n)):

* handedness s = (1, 1), writhe w(m,n) = w0 + 2*(-1) m + 2*(1) n; sites ['antiparallel', 'parallel']; direct-bracket cross-check at [[1, 0], [0, 1], [1, 1], [2, -1]]: **all grid points match**
* delta^3 * a = `-A^-2 - A^2 + A^6 + 2*A^10 + 2*A^14 + A^18`   [delta^2 | it: coefficient = (-A^2 + A^6 + A^14)/delta]
* delta^3 * b = `0`   [delta^3 | it: coefficient = 0]
* delta^3 * c = `A^-26 + A^-22 - A^-10 - 2*A^-6 - 3*A^-2 - 3*A^2 - 2*A^6 - 2*A^10 - A^14`   [delta^2 | it: coefficient = (A^-22 - A^-18 + A^-14 - A^-10 - A^-2 - A^2 - A^10)/delta]
* delta^3 * d = `-A^-26 - A^-22 + A^-10 + A^-6 + A^-2 + A^2 - A^14 - A^18`   [delta^3 | it: coefficient = A^-20 - 2*A^-16 + 3*A^-12 - 4*A^-8 + 4*A^-4 - 4 + 3*A^4 - 2*A^8 + A^12]

**K(0,0):** V = `1`, det = 1; HFK total rank 1, genus 0; spherogram simplify -> 0 crossings; snappy identify []; volume -0.0

Grid points (direct computation): K(1,0): V = t^-5 - 2*t^-4 + 2*t^-3 - 2*t^-2 + t^-1 + 1 - t + 2*t^2 - 2*t^3 + 2*t^4 - t^5, det 1; K(0,1): V = t^-2 - t^-1 + 1 - t + t^2, det 5; K(1,1): V = t^-4 - 2*t^-3 + 3*t^-2 - 3*t^-1 + 2 - t + 2*t^3 - 2*t^4 + 2*t^5 - t^6, det 5; K(2,-1): V = t^-8 - 2*t^-7 + 2*t^-6 - 3*t^-5 + 2*t^-4 - t^-2 + 3*t^-1 - 3 + 4*t - 3*t^2 + 2*t^3 - t^4, det 7

**Rational-slot corners C** (fusion `seam_band (c1 anchor; configs 3,3b,4L,4S,6)`, see rational_slots.md): (E1) HOLDS, defect `0`; (E2) fails, defect `-A^-12 + A^-8 - 2*A^-4 + 2 - 2*A^4 + 2*A^8 - A^12 + A^16`.

## [4S] c1 anchor, sites (seam, U-seed)

* Sites: site 1 = **seam**, site 2 = **U**.
* Diagram: `braid_closure( (I2 | rot(omega(RationalTangle(25,-9)))) * h * (I1 | rot(S1) | I1) * h * (rot(omega_bar(S2)) | I2) )` with S1, S2 the two site boxes (h = BraidTangle([-2,-3,-1,-2],4), rot = .rotate(1), sigma2 = BraidTangle([2],4)).
* K(0,0): 26 crossings, 1 component(s), writhe w0 = 2.
* PD(K(0,0)) = `[[11, 32, 12, 33], [33, 12, 34, 13], [13, 36, 14, 37], [21, 15, 22, 14], [15, 21, 16, 20], [19, 17, 20, 16], [17, 35, 18, 34], [35, 19, 36, 18], [22, 38, 23, 37], [38, 24, 39, 23], [24, 32, 25, 31], [30, 39, 31, 40], [40, 29, 41, 30], [28, 51, 29, 0], [41, 51, 42, 50], [27, 44, 28, 45], [42, 44, 43, 43], [8, 10, 9, 9], [49, 11, 50, 10], [7, 26, 8, 27], [48, 25, 49, 26], [3, 5, 4, 4], [5, 3, 6, 2], [47, 6, 48, 7], [1, 46, 2, 47], [45, 0, 46, 1]]`
* Site edges in that PD: site 1 (seam) = [43, 9], site 2 (U) = [48, 4].

**(1) Four raw corner brackets (absolute, same framing):**

| corner | state (site1, site2) | crossings | components | writhe of that diagram | bracket |
|---|---|---|---|---|---|
| B00 | (I, I) | 26 | 1 | 2 | `-A^4 - A^8` |
| B10 | (e, I) | 26 | 2 | 2 | `-A^-18 + A^-2 + A^2 + 3*A^6 + A^10 - A^22` |
| B01 | (I, e) | 26 | 2 | 2 | `A^2 + 2*A^6 + A^10` |
| B11 | (e, e) | 26 | 3 | 2 | `A^-28 - A^-24 + A^-20 - A^-12 + A^-8 - 2*A^-4 - 4*A^4 - 3*A^8 - A^16 + A^20` |

**(2) Identity polynomials (exact):**

* u = (-A^3)^w0 = `A^6`;  B00 - u*delta = `0`  -> unknot-seed equation **HOLDS**
* delta*B10 - B11 = `-A^-28 + A^-24 + A^-16 + A^-12 - A^-8 + A^-4 - 2 - A^8 - A^12 + A^16 + A^24`  -> **fails**  (c = 0)
* delta*B01 - B11 = `-A^-28 + A^-24 - A^-20 + A^-12 - A^-8 + 2*A^-4 - 1 + A^4 - A^12 + A^16 - A^20`  -> **fails**  (b = 0)
* (single-site flatness at K(0,0): delta*B00 = B10 fails; delta*B00 = B01 HOLDS)

**V(K(m,n)) structure** (V = unit * (a + b x + c y + d xy), x = A^(8 s1 m), y = A^(8 s2 n)):

* handedness s = (1, 1), writhe w(m,n) = w0 + 2*(-1) m + 2*(-1) n; sites ['antiparallel', 'antiparallel']; direct-bracket cross-check at [[1, 0], [0, 1], [1, 1], [2, -1]]: **all grid points match**
* delta^3 * a = `A^-28 - A^-24 + A^-20 - A^-12 + A^-8 - 2*A^-4 - 4*A^4 - 3*A^8 - A^16 + A^20`   [delta^2 | it: coefficient = (A^-24 - 3*A^-20 + 6*A^-16 - 9*A^-12 + 11*A^-8 - 12*A^-4 + 11 - 10*A^4 + 5*A^8 - 3*A^12 + A^16)/delta]
* delta^3 * b = `-A^-28 + A^-24 - A^-20 + A^-12 - A^-8 + 2*A^-4 - 1 + A^4 - A^12 + A^16 - A^20`   [delta^2 | it: coefficient = (-A^-24 + 3*A^-20 - 6*A^-16 + 9*A^-12 - 11*A^-8 + 12*A^-4 - 11 + 9*A^4 - 6*A^8 + 3*A^12 - A^16)/delta]
* delta^3 * c = `-A^-28 + A^-24 + A^-16 + A^-12 - A^-8 + A^-4 - 2 - A^8 - A^12 + A^16 + A^24`   [delta^2 | it: coefficient = (-A^-24 + 3*A^-20 - 5*A^-16 + 8*A^-12 - 10*A^-8 + 11*A^-4 - 11 + 9*A^4 - 7*A^8 + 4*A^12 - 2*A^16 + A^20)/delta]
* delta^3 * d = `A^-28 - A^-24 - A^-16 - A^-12 + A^-8 - A^-4 + 2 + A^8 + A^12 - A^16 - A^24`   [delta^2 | it: coefficient = (A^-24 - 3*A^-20 + 5*A^-16 - 8*A^-12 + 10*A^-8 - 11*A^-4 + 11 - 9*A^4 + 7*A^8 - 4*A^12 + 2*A^16 - A^20)/delta]

**K(0,0):** V = `1`, det = 1; HFK total rank 1, genus 0; spherogram simplify -> 0 crossings; snappy identify []; volume 0.0

Grid points (direct computation): K(1,0): V = t^-5 - 2*t^-4 + 2*t^-3 - 2*t^-2 + t^-1 + 1 - t + 2*t^2 - 2*t^3 + 2*t^4 - t^5, det 1; K(0,1): V = 1, det 1; K(1,1): V = t^-7 - 3*t^-6 + 6*t^-5 - 10*t^-4 + 12*t^-3 - 11*t^-2 + 7*t^-1 - 5*t + 10*t^2 - 12*t^3 + 11*t^4 - 8*t^5 + 4*t^6 - t^7, det 1; K(2,-1): V = t^-6 - 3*t^-5 + 7*t^-4 - 12*t^-3 + 15*t^-2 - 16*t^-1 + 13 - 5*t - 3*t^2 + 11*t^3 - 15*t^4 + 16*t^5 - 13*t^6 + 8*t^7 - 4*t^8 + t^9, det 1

**Rational-slot corners C** (fusion `seam_band (c1 anchor; configs 3,3b,4L,4S,6)`, see rational_slots.md): (E1) HOLDS, defect `0`; (E2) fails, defect `-A^-12 + A^-8 - 2*A^-4 + 2 - 2*A^4 + 2*A^8 - A^12 + A^16`.

## [5a] fusion sigma2 at the TOP (between A0 and the first h), sites (T-seed, U-seed)

* Sites: site 1 = **T**, site 2 = **U**.
* Diagram: `braid_closure( (I2 | rot(omega(S1))) * sigma2 * h * h * (rot(omega_bar(S2)) | I2) )` with S1, S2 the two site boxes (h = BraidTangle([-2,-3,-1,-2],4), rot = .rotate(1), sigma2 = BraidTangle([2],4)).
* K(0,0): 19 crossings, 1 component(s), writhe w0 = -7.
* PD(K(0,0)) = `[[30, 29, 31, 30], [28, 31, 29, 32], [32, 22, 33, 21], [20, 28, 21, 27], [26, 20, 27, 19], [37, 19, 0, 18], [36, 17, 37, 18], [25, 16, 26, 17], [35, 10, 36, 11], [24, 9, 25, 10], [8, 23, 9, 24], [15, 22, 16, 23], [7, 34, 8, 35], [14, 33, 15, 34], [3, 5, 4, 4], [5, 3, 6, 2], [13, 6, 14, 7], [1, 12, 2, 13], [11, 0, 12, 1]]`
* Site edges in that PD: site 1 (T) = [22, 30], site 2 (U) = [14, 4].

**(1) Four raw corner brackets (absolute, same framing):**

| corner | state (site1, site2) | crossings | components | writhe of that diagram | bracket |
|---|---|---|---|---|---|
| B00 | (I, I) | 19 | 1 | -7 | `A^-15 + A^-7 + A + A^5 - A^9 - A^17` |
| B10 | (e, I) | 19 | 2 | -7 | `-A^-13 + A^-9 - 2*A^-5 - 3*A^3 - A^7 + A^11 - A^15 + 2*A^19 - A^23 + A^27` |
| B01 | (I, e) | 19 | 2 | -7 | `-A^-25 + A^-21 - 2*A^-17 + A^-13 - A^-9 - 3*A^3 + A^7 - A^11 + A^15` |
| B11 | (e, e) | 19 | 3 | -7 | `A^-23 - 2*A^-19 + 4*A^-15 - 3*A^-11 + 4*A^-7 - A^-3 + 2*A + 4*A^5 - 3*A^9 + 4*A^13 - 3*A^17 + 2*A^21 - A^25` |

**(2) Identity polynomials (exact):**

* u = (-A^3)^w0 = `-A^-21`;  B00 - u*delta = `-A^-23 - A^-19 + A^-15 + A^-7 + A + A^5 - A^9 - A^17`  -> unknot-seed equation **fails**
* delta*B10 - B11 = `-A^-23 + 2*A^-19 - 3*A^-15 + 3*A^-11 - 3*A^-7 + 3*A^-3 + A + 3*A^9 - 4*A^13 + 2*A^17 - 3*A^21 + A^25 - A^29`  -> **fails**  (c = 0)
* delta*B01 - B11 = `A^-27 - A^-23 + 3*A^-19 - 3*A^-15 + 3*A^-11 - 3*A^-7 + A^-3 + A - 2*A^5 + 3*A^9 - 4*A^13 + 2*A^17 - 2*A^21 + A^25`  -> **fails**  (b = 0)
* (single-site flatness at K(0,0): delta*B00 = B10 fails; delta*B00 = B01 fails)

**V(K(m,n)) structure** (V = unit * (a + b x + c y + d xy), x = A^(8 s1 m), y = A^(8 s2 n)):

* handedness s = (1, 1), writhe w(m,n) = w0 + 2*(-1) m + 2*(-1) n; sites ['antiparallel', 'antiparallel']; direct-bracket cross-check at [[1, 0], [0, 1], [1, 1], [2, -1]]: **all grid points match**
* delta^3 * a = `A^-23 - 2*A^-19 + 4*A^-15 - 3*A^-11 + 4*A^-7 - A^-3 + 2*A + 4*A^5 - 3*A^9 + 4*A^13 - 3*A^17 + 2*A^21 - A^25`   [delta | it: coefficient = (-A^-21 + 3*A^-17 - 7*A^-13 + 10*A^-9 - 14*A^-5 + 15*A^-1 - 17*A^3 + 13*A^7 - 10*A^11 + 6*A^15 - 3*A^19 + A^23)/delta^2]
* delta^3 * b = `A^-27 - A^-23 + 3*A^-19 - 3*A^-15 + 3*A^-11 - 3*A^-7 + A^-3 + A - 2*A^5 + 3*A^9 - 4*A^13 + 2*A^17 - 2*A^21 + A^25`   [delta | it: coefficient = (-A^-25 + 2*A^-21 - 5*A^-17 + 8*A^-13 - 11*A^-9 + 14*A^-5 - 15*A^-1 + 14*A^3 - 12*A^7 + 9*A^11 - 5*A^15 + 3*A^19 - A^23)/delta^2]
* delta^3 * c = `-A^-23 + 2*A^-19 - 3*A^-15 + 3*A^-11 - 3*A^-7 + 3*A^-3 + A + 3*A^9 - 4*A^13 + 2*A^17 - 3*A^21 + A^25 - A^29`   [delta | it: coefficient = (A^-21 - 3*A^-17 + 6*A^-13 - 9*A^-9 + 12*A^-5 - 15*A^-1 + 14*A^3 - 14*A^7 + 11*A^11 - 7*A^15 + 5*A^19 - 2*A^23 + A^27)/delta^2]
* delta^3 * d = `-A^-27 + A^-23 - 2*A^-19 + 4*A^-15 - A^-11 + 4*A^-7 - A^-3 - A - 4*A^9 + 2*A^13 - 3*A^17 + 2*A^21 - A^25 + A^29`   [delta | it: coefficient = (A^-25 - 2*A^-21 + 4*A^-17 - 8*A^-13 + 9*A^-9 - 13*A^-5 + 14*A^-1 - 13*A^3 + 13*A^7 - 9*A^11 + 7*A^15 - 4*A^19 + 2*A^23 - A^27)/delta^2]

**K(0,0):** V = `-t^-9 + t^-8 - 2*t^-7 + 3*t^-6 - 2*t^-5 + 2*t^-4 - t^-3 + t^-2`, det = 13; HFK total rank 13, genus 2; spherogram simplify -> 7 crossings; snappy identify ['m340(0,0)', '7_3(0,0)', 'K5_20(0,0)', 'K7a5(0,0)']; volume 4.592126

Grid points (direct computation): K(1,0): V = t^-13 - 3*t^-12 + 5*t^-11 - 8*t^-10 + 9*t^-9 - 10*t^-8 + 9*t^-7 - 6*t^-6 + 5*t^-5 - 2*t^-4 + t^-3, det 59; K(0,1): V = -t^-11 + 2*t^-10 - 5*t^-9 + 8*t^-8 - 11*t^-7 + 14*t^-6 - 13*t^-5 + 12*t^-4 - 9*t^-3 + 6*t^-2 - 3*t^-1 + 1, det 85; K(1,1): V = t^-15 - 4*t^-14 + 10*t^-13 - 20*t^-12 + 31*t^-11 - 44*t^-10 + 53*t^-9 - 56*t^-8 + 54*t^-7 - 44*t^-6 + 33*t^-5 - 21*t^-4 + 11*t^-3 - 4*t^-2 + t^-1, det 387; K(2,-1): V = t^-14 - 4*t^-13 + 10*t^-12 - 21*t^-11 + 36*t^-10 - 54*t^-9 + 70*t^-8 - 82*t^-7 + 85*t^-6 - 77*t^-5 + 64*t^-4 - 45*t^-3 + 28*t^-2 - 14*t^-1 + 5 - t, det 597

**Rational-slot corners C** (fusion `top_sigma2 (configs 5a,5aL)`, see rational_slots.md): (E1) HOLDS, defect `0`; (E2) fails, defect `-A^-13 + A^-9 - 2*A^-5 + 2*A^-1 - 2*A^3 + 2*A^7 - A^11 + A^15`.

## [5b] fusion sigma2 at the BOTTOM (between the second h and B0), sites (T-seed, U-seed)

* Sites: site 1 = **T**, site 2 = **U**.
* Diagram: `braid_closure( (I2 | rot(omega(S1))) * h * h * sigma2 * (rot(omega_bar(S2)) | I2) )` with S1, S2 the two site boxes (h = BraidTangle([-2,-3,-1,-2],4), rot = .rotate(1), sigma2 = BraidTangle([2],4)).
* K(0,0): 19 crossings, 1 component(s), writhe w0 = -7.
* PD(K(0,0)) = `[[30, 29, 31, 30], [28, 31, 29, 32], [32, 22, 33, 21], [20, 28, 21, 27], [26, 20, 27, 19], [18, 37, 19, 0], [25, 36, 26, 37], [17, 10, 18, 11], [24, 9, 25, 10], [8, 23, 9, 24], [35, 22, 36, 23], [7, 16, 8, 17], [34, 15, 35, 16], [33, 15, 34, 14], [3, 5, 4, 4], [5, 3, 6, 2], [13, 6, 14, 7], [1, 12, 2, 13], [11, 0, 12, 1]]`
* Site edges in that PD: site 1 (T) = [22, 30], site 2 (U) = [14, 4].

**(1) Four raw corner brackets (absolute, same framing):**

| corner | state (site1, site2) | crossings | components | writhe of that diagram | bracket |
|---|---|---|---|---|---|
| B00 | (I, I) | 19 | 1 | -7 | `A^-15 + A^-7 + A + A^5 - A^9 - A^17` |
| B10 | (e, I) | 19 | 2 | -7 | `-A^-13 + A^-9 - 2*A^-5 - 3*A^3 - A^7 + A^11 - A^15 + 2*A^19 - A^23 + A^27` |
| B01 | (I, e) | 19 | 2 | -7 | `-A^-25 + A^-21 - 2*A^-17 + A^-13 - A^-9 - 3*A^3 + A^7 - A^11 + A^15` |
| B11 | (e, e) | 19 | 3 | -7 | `A^-23 - 2*A^-19 + 4*A^-15 - 3*A^-11 + 4*A^-7 - A^-3 + 2*A + 4*A^5 - 3*A^9 + 4*A^13 - 3*A^17 + 2*A^21 - A^25` |

**(2) Identity polynomials (exact):**

* u = (-A^3)^w0 = `-A^-21`;  B00 - u*delta = `-A^-23 - A^-19 + A^-15 + A^-7 + A + A^5 - A^9 - A^17`  -> unknot-seed equation **fails**
* delta*B10 - B11 = `-A^-23 + 2*A^-19 - 3*A^-15 + 3*A^-11 - 3*A^-7 + 3*A^-3 + A + 3*A^9 - 4*A^13 + 2*A^17 - 3*A^21 + A^25 - A^29`  -> **fails**  (c = 0)
* delta*B01 - B11 = `A^-27 - A^-23 + 3*A^-19 - 3*A^-15 + 3*A^-11 - 3*A^-7 + A^-3 + A - 2*A^5 + 3*A^9 - 4*A^13 + 2*A^17 - 2*A^21 + A^25`  -> **fails**  (b = 0)
* (single-site flatness at K(0,0): delta*B00 = B10 fails; delta*B00 = B01 fails)

**V(K(m,n)) structure** (V = unit * (a + b x + c y + d xy), x = A^(8 s1 m), y = A^(8 s2 n)):

* handedness s = (1, 1), writhe w(m,n) = w0 + 2*(-1) m + 2*(-1) n; sites ['antiparallel', 'antiparallel']; direct-bracket cross-check at [[1, 0], [0, 1], [1, 1], [2, -1]]: **all grid points match**
* delta^3 * a = `A^-23 - 2*A^-19 + 4*A^-15 - 3*A^-11 + 4*A^-7 - A^-3 + 2*A + 4*A^5 - 3*A^9 + 4*A^13 - 3*A^17 + 2*A^21 - A^25`   [delta | it: coefficient = (-A^-21 + 3*A^-17 - 7*A^-13 + 10*A^-9 - 14*A^-5 + 15*A^-1 - 17*A^3 + 13*A^7 - 10*A^11 + 6*A^15 - 3*A^19 + A^23)/delta^2]
* delta^3 * b = `A^-27 - A^-23 + 3*A^-19 - 3*A^-15 + 3*A^-11 - 3*A^-7 + A^-3 + A - 2*A^5 + 3*A^9 - 4*A^13 + 2*A^17 - 2*A^21 + A^25`   [delta | it: coefficient = (-A^-25 + 2*A^-21 - 5*A^-17 + 8*A^-13 - 11*A^-9 + 14*A^-5 - 15*A^-1 + 14*A^3 - 12*A^7 + 9*A^11 - 5*A^15 + 3*A^19 - A^23)/delta^2]
* delta^3 * c = `-A^-23 + 2*A^-19 - 3*A^-15 + 3*A^-11 - 3*A^-7 + 3*A^-3 + A + 3*A^9 - 4*A^13 + 2*A^17 - 3*A^21 + A^25 - A^29`   [delta | it: coefficient = (A^-21 - 3*A^-17 + 6*A^-13 - 9*A^-9 + 12*A^-5 - 15*A^-1 + 14*A^3 - 14*A^7 + 11*A^11 - 7*A^15 + 5*A^19 - 2*A^23 + A^27)/delta^2]
* delta^3 * d = `-A^-27 + A^-23 - 2*A^-19 + 4*A^-15 - A^-11 + 4*A^-7 - A^-3 - A - 4*A^9 + 2*A^13 - 3*A^17 + 2*A^21 - A^25 + A^29`   [delta | it: coefficient = (A^-25 - 2*A^-21 + 4*A^-17 - 8*A^-13 + 9*A^-9 - 13*A^-5 + 14*A^-1 - 13*A^3 + 13*A^7 - 9*A^11 + 7*A^15 - 4*A^19 + 2*A^23 - A^27)/delta^2]

**K(0,0):** V = `-t^-9 + t^-8 - 2*t^-7 + 3*t^-6 - 2*t^-5 + 2*t^-4 - t^-3 + t^-2`, det = 13; HFK total rank 13, genus 2; spherogram simplify -> 7 crossings; snappy identify ['m340(0,0)', '7_3(0,0)', 'K5_20(0,0)', 'K7a5(0,0)']; volume 4.592126

Grid points (direct computation): K(1,0): V = t^-13 - 3*t^-12 + 5*t^-11 - 8*t^-10 + 9*t^-9 - 10*t^-8 + 9*t^-7 - 6*t^-6 + 5*t^-5 - 2*t^-4 + t^-3, det 59; K(0,1): V = -t^-11 + 2*t^-10 - 5*t^-9 + 8*t^-8 - 11*t^-7 + 14*t^-6 - 13*t^-5 + 12*t^-4 - 9*t^-3 + 6*t^-2 - 3*t^-1 + 1, det 85; K(1,1): V = t^-15 - 4*t^-14 + 10*t^-13 - 20*t^-12 + 31*t^-11 - 44*t^-10 + 53*t^-9 - 56*t^-8 + 54*t^-7 - 44*t^-6 + 33*t^-5 - 21*t^-4 + 11*t^-3 - 4*t^-2 + t^-1, det 387; K(2,-1): V = t^-14 - 4*t^-13 + 10*t^-12 - 21*t^-11 + 36*t^-10 - 54*t^-9 + 70*t^-8 - 82*t^-7 + 85*t^-6 - 77*t^-5 + 64*t^-4 - 45*t^-3 + 28*t^-2 - 14*t^-1 + 5 - t, det 597

**Rational-slot corners C** (fusion `bottom_sigma2 (configs 5b,5bL)`, see rational_slots.md): (E1) HOLDS, defect `0`; (E2) fails, defect `-A^-13 + A^-9 - 2*A^-5 + 2*A^-1 - 2*A^3 + 2*A^7 - A^11 + A^15`.

## [5c] fusion sigma2^-1 at the seam, sites (T-seed, U-seed)

* Sites: site 1 = **T**, site 2 = **U**.
* Diagram: `braid_closure( (I2 | rot(omega(S1))) * h * sigma2^-1 * h * (rot(omega_bar(S2)) | I2) )` with S1, S2 the two site boxes (h = BraidTangle([-2,-3,-1,-2],4), rot = .rotate(1), sigma2 = BraidTangle([2],4)).
* K(0,0): 19 crossings, 1 component(s), writhe w0 = -9.
* PD(K(0,0)) = `[[16, 15, 17, 16], [14, 17, 15, 18], [18, 26, 19, 25], [24, 14, 25, 13], [12, 24, 13, 23], [22, 37, 23, 0], [11, 36, 12, 37], [21, 30, 22, 31], [10, 29, 11, 30], [28, 9, 29, 10], [8, 27, 9, 28], [35, 26, 36, 27], [7, 20, 8, 21], [34, 19, 35, 20], [3, 5, 4, 4], [5, 3, 6, 2], [33, 6, 34, 7], [1, 32, 2, 33], [31, 0, 32, 1]]`
* Site edges in that PD: site 1 (T) = [26, 16], site 2 (U) = [34, 4].

**(1) Four raw corner brackets (absolute, same framing):**

| corner | state (site1, site2) | crossings | components | writhe of that diagram | bracket |
|---|---|---|---|---|---|
| B00 | (I, I) | 19 | 1 | -9 | `A^-13 + 2*A^-5 + A^-1 - A^11 - A^19` |
| B10 | (e, I) | 19 | 2 | -9 | `-A^-11 - 4*A^-3 - A^5 + A^13 - A^17 + 2*A^21 - A^25 + A^29` |
| B01 | (I, e) | 19 | 2 | -9 | `-A^-23 + A^-19 - 2*A^-15 + A^-11 - 2*A^-7 - 2*A^-3 - A^5 + 2*A^9 - A^13 + A^17` |
| B11 | (e, e) | 19 | 3 | -9 | `A^-21 - A^-17 + 4*A^-13 - 3*A^-9 + 6*A^-5 + A^3 + 2*A^7 - 3*A^11 + 4*A^15 - 4*A^19 + 2*A^23 - A^27` |

**(2) Identity polynomials (exact):**

* u = (-A^3)^w0 = `-A^-27`;  B00 - u*delta = `-A^-29 - A^-25 + A^-13 + 2*A^-5 + A^-1 - A^11 - A^19`  -> unknot-seed equation **fails**
* delta*B10 - B11 = `-A^-21 + A^-17 - 3*A^-13 + 4*A^-9 - 2*A^-5 + 4*A^-1 - A^7 + 2*A^11 - 4*A^15 + 3*A^19 - 3*A^23 + A^27 - A^31`  -> **fails**  (c = 0)
* delta*B01 - B11 = `A^-25 - A^-21 + 2*A^-17 - 3*A^-13 + 4*A^-9 - 2*A^-5 + 2*A^-1 - 3*A^7 + 2*A^11 - 4*A^15 + 3*A^19 - 2*A^23 + A^27`  -> **fails**  (b = 0)
* (single-site flatness at K(0,0): delta*B00 = B10 fails; delta*B00 = B01 fails)

**V(K(m,n)) structure** (V = unit * (a + b x + c y + d xy), x = A^(8 s1 m), y = A^(8 s2 n)):

* handedness s = (1, 1), writhe w(m,n) = w0 + 2*(-1) m + 2*(-1) n; sites ['antiparallel', 'antiparallel']; direct-bracket cross-check at [[1, 0], [0, 1], [1, 1], [2, -1]]: **all grid points match**
* delta^3 * a = `A^-21 - A^-17 + 4*A^-13 - 3*A^-9 + 6*A^-5 + A^3 + 2*A^7 - 3*A^11 + 4*A^15 - 4*A^19 + 2*A^23 - A^27`   [delta | it: coefficient = (-A^-19 + 2*A^-15 - 6*A^-11 + 9*A^-7 - 15*A^-3 + 15*A - 16*A^5 + 14*A^9 - 11*A^13 + 7*A^17 - 3*A^21 + A^25)/delta^2]
* delta^3 * b = `A^-25 - A^-21 + 2*A^-17 - 3*A^-13 + 4*A^-9 - 2*A^-5 + 2*A^-1 - 3*A^7 + 2*A^11 - 4*A^15 + 3*A^19 - 2*A^23 + A^27`   [delta | it: coefficient = (-A^-23 + 2*A^-19 - 4*A^-15 + 7*A^-11 - 11*A^-7 + 13*A^-3 - 15*A + 15*A^5 - 12*A^9 + 10*A^13 - 6*A^17 + 3*A^21 - A^25)/delta^2]
* delta^3 * c = `-A^-21 + A^-17 - 3*A^-13 + 4*A^-9 - 2*A^-5 + 4*A^-1 - A^7 + 2*A^11 - 4*A^15 + 3*A^19 - 3*A^23 + A^27 - A^31`   [delta | it: coefficient = (A^-19 - 2*A^-15 + 5*A^-11 - 9*A^-7 + 11*A^-3 - 15*A + 15*A^5 - 14*A^9 + 12*A^13 - 8*A^17 + 5*A^21 - 2*A^25 + A^29)/delta^2]
* delta^3 * d = `-A^-25 + A^-21 - A^-17 + 4*A^-13 - 2*A^-9 + 3*A^-5 - 2*A^-1 + A^7 - 3*A^11 + 2*A^15 - 4*A^19 + 2*A^23 - A^27 + A^31`   [delta | it: coefficient = (A^-23 - 2*A^-19 + 3*A^-15 - 7*A^-11 + 9*A^-7 - 12*A^-3 + 14*A - 14*A^5 + 13*A^9 - 10*A^13 + 8*A^17 - 4*A^21 + 2*A^25 - A^29)/delta^2]

**K(0,0):** V = `-t^-11 + t^-10 - 2*t^-9 + 2*t^-8 - 2*t^-7 + 3*t^-6 - t^-5 + t^-4`, det = 13; HFK total rank 21, genus 4; spherogram simplify -> 15 crossings; snappy identify ['o9_29972(0,0)', 'K9_433(0,0)']; volume 7.232651

Grid points (direct computation): K(1,0): V = t^-15 - 3*t^-14 + 5*t^-13 - 8*t^-12 + 9*t^-11 - 10*t^-10 + 9*t^-9 - 7*t^-8 + 5*t^-7 - t^-6 + t^-5, det 59; K(0,1): V = -t^-13 + 2*t^-12 - 5*t^-11 + 8*t^-10 - 11*t^-9 + 13*t^-8 - 13*t^-7 + 13*t^-6 - 9*t^-5 + 6*t^-4 - 3*t^-3 + t^-2, det 85; K(1,1): V = t^-17 - 4*t^-16 + 10*t^-15 - 21*t^-14 + 34*t^-13 - 47*t^-12 + 55*t^-11 - 58*t^-10 + 54*t^-9 - 43*t^-8 + 31*t^-7 - 17*t^-6 + 8*t^-5 - 3*t^-4 + t^-3, det 387; K(2,-1): V = t^-16 - 4*t^-15 + 11*t^-14 - 24*t^-13 + 40*t^-12 - 59*t^-11 + 75*t^-10 - 84*t^-9 + 84*t^-8 - 75*t^-7 + 60*t^-6 - 40*t^-5 + 24*t^-4 - 11*t^-3 + 4*t^-2 - t^-1, det 597

**Rational-slot corners C** (fusion `seam_sigma2inv (config 5c)`, see rational_slots.md): (E1) HOLDS, defect `0`; (E2) fails, defect `-A^-11 + A^-7 - 2*A^-3 + 2*A - 2*A^5 + 2*A^9 - A^13 + A^17`.

## [5aL] fusion sigma2 at the TOP, sites (T-lit, U-lit)

* Sites: site 1 = **T**, site 2 = **U**.
* Diagram: `braid_closure( (I2 | rot(IntegerTangle(3))) * (I2 | S1) * sigma2 * h * h * (S2 | I2) * (rot(IntegerTangle(-3)) | I2) )` with S1, S2 the two site boxes (h = BraidTangle([-2,-3,-1,-2],4), rot = .rotate(1), sigma2 = BraidTangle([2],4)).
* K(0,0): 15 crossings, 1 component(s), writhe w0 = -7.
* PD(K(0,0)) = `[[24, 18, 25, 17], [16, 24, 17, 23], [22, 16, 23, 15], [29, 15, 0, 14], [28, 13, 29, 14], [21, 12, 22, 13], [27, 6, 28, 7], [20, 5, 21, 6], [4, 19, 5, 20], [11, 18, 12, 19], [3, 26, 4, 27], [10, 25, 11, 26], [9, 2, 10, 3], [1, 8, 2, 9], [7, 0, 8, 1]]`
* Site edges in that PD: site 1 (T) = [15, 22], site 2 (U) = [3, 10].

**(1) Four raw corner brackets (absolute, same framing):**

| corner | state (site1, site2) | crossings | components | writhe of that diagram | bracket |
|---|---|---|---|---|---|
| B00 | (I, I) | 15 | 1 | -7 | `A^-15 + A^-7 + A + A^5 - A^9 - A^17` |
| B10 | (e, I) | 15 | 1 | -5 | `A^-13 + A^-9 + A^-5 - A^3` |
| B01 | (I, e) | 15 | 1 | 7 | `-A^3 + A^11 + A^15 + A^19` |
| B11 | (e, e) | 15 | 1 | 1 | `A + A^5` |

**(2) Identity polynomials (exact):**

* u = (-A^3)^w0 = `-A^-21`;  B00 - u*delta = `-A^-23 - A^-19 + A^-15 + A^-7 + A + A^5 - A^9 - A^17`  -> unknot-seed equation **fails**
* delta*B10 - B11 = `-A^-15 - 2*A^-11 - 2*A^-7 - A^-3`  -> **fails**  (c = 0)
* delta*B01 - B11 = `-A^9 - 2*A^13 - 2*A^17 - A^21`  -> **fails**  (b = 0)
* (single-site flatness at K(0,0): delta*B00 = B10 fails; delta*B00 = B01 fails)

**V(K(m,n)) structure** (V = unit * (a + b x + c y + d xy), x = A^(8 s1 m), y = A^(8 s2 n)):

* handedness s = (1, 1), writhe w(m,n) = w0 + 2*(1) m + 2*(1) n; sites ['parallel', 'parallel']; direct-bracket cross-check at [[1, 0], [0, 1], [1, 1], [2, -1]]: **all grid points match**
* delta^3 * a = `A + A^5`   [delta | it: coefficient = (-A^3)/delta^2]
* delta^3 * b = `-A^9 - 2*A^13 - 2*A^17 - A^21`   [delta | it: coefficient = (A^11 + A^15 + A^19)/delta^2]
* delta^3 * c = `-A^-15 - 2*A^-11 - 2*A^-7 - A^-3`   [delta | it: coefficient = (A^-13 + A^-9 + A^-5)/delta^2]
* delta^3 * d = `A^-19 + 3*A^-15 + 4*A^-11 + 4*A^-7 + 3*A^-3 + 2*A + A^5`   [delta | it: coefficient = (-A^-17 - 2*A^-13 - 2*A^-9 - 2*A^-5 - A^-1 - A^3)/delta^2]

**K(0,0):** V = `-t^-9 + t^-8 - 2*t^-7 + 3*t^-6 - 2*t^-5 + 2*t^-4 - t^-3 + t^-2`, det = 13; HFK total rank 13, genus 2; spherogram simplify -> 7 crossings; snappy identify ['m340(0,0)', '7_3(0,0)', 'K5_20(0,0)', 'K7a5(0,0)']; volume 4.592126

Grid points (direct computation): K(1,0): V = -t^-8 + t^-7 - 2*t^-6 + 3*t^-5 - 3*t^-4 + 4*t^-3 - 2*t^-2 + 2*t^-1 - 1, det 19; K(0,1): V = -t^-6 + t^-5 - t^-4 + 2*t^-3 - t^-2 + t^-1, det 7; K(1,1): V = -t^-5 + t^-4 - t^-3 + 2*t^-2 - t^-1 + 2 - t, det 9; K(2,-1): V = -t^-10 + t^-9 - 2*t^-8 + 3*t^-7 - 4*t^-6 + 5*t^-5 - 5*t^-4 + 6*t^-3 - 4*t^-2 + 4*t^-1 - 2 + t - t^2, det 39

**Rational-slot corners C** (fusion `top_sigma2 (configs 5a,5aL)`, see rational_slots.md): (E1) HOLDS, defect `0`; (E2) fails, defect `-A^-13 + A^-9 - 2*A^-5 + 2*A^-1 - 2*A^3 + 2*A^7 - A^11 + A^15`.

## [5bL] fusion sigma2 at the BOTTOM, sites (T-lit, U-lit)

* Sites: site 1 = **T**, site 2 = **U**.
* Diagram: `braid_closure( (I2 | rot(IntegerTangle(3))) * (I2 | S1) * h * h * sigma2 * (S2 | I2) * (rot(IntegerTangle(-3)) | I2) )` with S1, S2 the two site boxes (h = BraidTangle([-2,-3,-1,-2],4), rot = .rotate(1), sigma2 = BraidTangle([2],4)).
* K(0,0): 15 crossings, 1 component(s), writhe w0 = -7.
* PD(K(0,0)) = `[[24, 18, 25, 17], [16, 24, 17, 23], [22, 16, 23, 15], [14, 29, 15, 0], [21, 28, 22, 29], [13, 6, 14, 7], [20, 5, 21, 6], [4, 19, 5, 20], [27, 18, 28, 19], [3, 12, 4, 13], [26, 11, 27, 12], [25, 11, 26, 10], [9, 2, 10, 3], [1, 8, 2, 9], [7, 0, 8, 1]]`
* Site edges in that PD: site 1 (T) = [15, 22], site 2 (U) = [3, 10].

**(1) Four raw corner brackets (absolute, same framing):**

| corner | state (site1, site2) | crossings | components | writhe of that diagram | bracket |
|---|---|---|---|---|---|
| B00 | (I, I) | 15 | 1 | -7 | `A^-15 + A^-7 + A + A^5 - A^9 - A^17` |
| B10 | (e, I) | 15 | 1 | -5 | `A^-13 + A^-9 + A^-5 - A^3` |
| B01 | (I, e) | 15 | 1 | 7 | `-A^3 + A^11 + A^15 + A^19` |
| B11 | (e, e) | 15 | 1 | 1 | `A + A^5` |

**(2) Identity polynomials (exact):**

* u = (-A^3)^w0 = `-A^-21`;  B00 - u*delta = `-A^-23 - A^-19 + A^-15 + A^-7 + A + A^5 - A^9 - A^17`  -> unknot-seed equation **fails**
* delta*B10 - B11 = `-A^-15 - 2*A^-11 - 2*A^-7 - A^-3`  -> **fails**  (c = 0)
* delta*B01 - B11 = `-A^9 - 2*A^13 - 2*A^17 - A^21`  -> **fails**  (b = 0)
* (single-site flatness at K(0,0): delta*B00 = B10 fails; delta*B00 = B01 fails)

**V(K(m,n)) structure** (V = unit * (a + b x + c y + d xy), x = A^(8 s1 m), y = A^(8 s2 n)):

* handedness s = (1, 1), writhe w(m,n) = w0 + 2*(1) m + 2*(1) n; sites ['parallel', 'parallel']; direct-bracket cross-check at [[1, 0], [0, 1], [1, 1], [2, -1]]: **all grid points match**
* delta^3 * a = `A + A^5`   [delta | it: coefficient = (-A^3)/delta^2]
* delta^3 * b = `-A^9 - 2*A^13 - 2*A^17 - A^21`   [delta | it: coefficient = (A^11 + A^15 + A^19)/delta^2]
* delta^3 * c = `-A^-15 - 2*A^-11 - 2*A^-7 - A^-3`   [delta | it: coefficient = (A^-13 + A^-9 + A^-5)/delta^2]
* delta^3 * d = `A^-19 + 3*A^-15 + 4*A^-11 + 4*A^-7 + 3*A^-3 + 2*A + A^5`   [delta | it: coefficient = (-A^-17 - 2*A^-13 - 2*A^-9 - 2*A^-5 - A^-1 - A^3)/delta^2]

**K(0,0):** V = `-t^-9 + t^-8 - 2*t^-7 + 3*t^-6 - 2*t^-5 + 2*t^-4 - t^-3 + t^-2`, det = 13; HFK total rank 13, genus 2; spherogram simplify -> 7 crossings; snappy identify ['m340(0,0)', '7_3(0,0)', 'K5_20(0,0)', 'K7a5(0,0)']; volume 4.592126

Grid points (direct computation): K(1,0): V = -t^-8 + t^-7 - 2*t^-6 + 3*t^-5 - 3*t^-4 + 4*t^-3 - 2*t^-2 + 2*t^-1 - 1, det 19; K(0,1): V = -t^-6 + t^-5 - t^-4 + 2*t^-3 - t^-2 + t^-1, det 7; K(1,1): V = -t^-5 + t^-4 - t^-3 + 2*t^-2 - t^-1 + 2 - t, det 9; K(2,-1): V = -t^-10 + t^-9 - 2*t^-8 + 3*t^-7 - 4*t^-6 + 5*t^-5 - 5*t^-4 + 6*t^-3 - 4*t^-2 + 4*t^-1 - 2 + t - t^2, det 39

**Rational-slot corners C** (fusion `bottom_sigma2 (configs 5b,5bL)`, see rational_slots.md): (E1) HOLDS, defect `0`; (E2) fails, defect `-A^-13 + A^-9 - 2*A^-5 + 2*A^-1 - 2*A^3 + 2*A^7 - A^11 + A^15`.

## [6] torsion-free seed R(11,-4) in the c1 construction, sites (seam, T-seed)
_S = p/(q+2pn) at n=0 with p/q = 11/-4; 13p+36q = -1, turnback link torsion-free (c1 note section 6)_

* Sites: site 1 = **seam**, site 2 = **T**.
* Diagram: `braid_closure( (I2 | rot(omega(S2 * RationalTangle(11,-4)))) * h * (I1 | rot(S1) | I1) * h * (rot(IntegerTangle(-3)) | I2) )` with S1, S2 the two site boxes (h = BraidTangle([-2,-3,-1,-2],4), rot = .rotate(1), sigma2 = BraidTangle([2],4)).
* K(0,0): 22 crossings, 1 component(s), writhe w0 = 4.
* PD(K(0,0)) = `[[7, 15, 8, 14], [13, 9, 14, 8], [9, 28, 10, 29], [25, 10, 26, 11], [11, 26, 12, 27], [27, 12, 28, 13], [24, 29, 25, 30], [30, 23, 31, 24], [22, 16, 23, 15], [16, 32, 17, 31], [32, 18, 33, 17], [18, 0, 19, 43], [33, 43, 34, 42], [19, 37, 20, 36], [34, 36, 35, 35], [4, 6, 5, 5], [41, 7, 42, 6], [3, 21, 4, 20], [40, 22, 41, 21], [39, 2, 40, 3], [1, 38, 2, 39], [37, 0, 38, 1]]`
* Site edges in that PD: site 1 (seam) = [35, 5], site 2 (T) = [7, 29].

**(1) Four raw corner brackets (absolute, same framing):**

| corner | state (site1, site2) | crossings | components | writhe of that diagram | bracket |
|---|---|---|---|---|---|
| B00 | (I, I) | 22 | 1 | 4 | `-A^10 - A^14` |
| B10 | (e, I) | 22 | 2 | -12 | `A^-20 + A^-16 + A^-12 + A^-8 - A^4 + A^12` |
| B01 | (I, e) | 22 | 2 | -4 | `-A^-28 + 2*A^-24 - 4*A^-20 + 8*A^-16 - 9*A^-12 + 12*A^-8 - 10*A^-4 + 7 - 2*A^4 - 4*A^8 + 10*A^12 - 11*A^16 + 11*A^20 - 9*A^24 + 6*A^28 - 3*A^32 + A^36` |
| B11 | (e, e) | 22 | 3 | -12 | `-A^-22 - 2*A^-18 - 2*A^-14 - 2*A^-10 - A^-6 + A^2 + A^6 - A^10 - A^14` |

**(2) Identity polynomials (exact):**

* u = (-A^3)^w0 = `A^12`;  B00 - u*delta = `0`  -> unknot-seed equation **HOLDS**
* delta*B10 - B11 = `0`  -> **HOLDS**  (c = 0)
* delta*B01 - B11 = `A^-30 - A^-26 + 3*A^-22 - 2*A^-18 + 3*A^-14 - A^-10 - A^-6 + 3*A^-2 - 6*A^2 + 5*A^6 - 5*A^10 + 2*A^14 - 2*A^22 + 3*A^26 - 3*A^30 + 2*A^34 - A^38`  -> **fails**  (b = 0)
* (single-site flatness at K(0,0): delta*B00 = B10 fails; delta*B00 = B01 fails)

**V(K(m,n)) structure** (V = unit * (a + b x + c y + d xy), x = A^(8 s1 m), y = A^(8 s2 n)):

* handedness s = (1, 1), writhe w(m,n) = w0 + 2*(-1) m + 2*(-1) n; sites ['antiparallel', 'antiparallel']; direct-bracket cross-check at [[1, 0], [0, 1], [1, 1], [2, -1]]: **all grid points match**
* delta^3 * a = `-A^-22 - 2*A^-18 - 2*A^-14 - 2*A^-10 - A^-6 + A^2 + A^6 - A^10 - A^14`   [delta^3 | it: coefficient = A^-16 - A^-12 + 2*A^-8 - 2*A^-4 + 2 - 2*A^4 + A^8]
* delta^3 * b = `A^-30 - A^-26 + 3*A^-22 - 2*A^-18 + 3*A^-14 - A^-10 - A^-6 + 3*A^-2 - 6*A^2 + 5*A^6 - 5*A^10 + 2*A^14 - 2*A^22 + 3*A^26 - 3*A^30 + 2*A^34 - A^38`   [delta^2 | it: coefficient = (A^-26 - 3*A^-22 + 8*A^-18 - 15*A^-14 + 25*A^-10 - 36*A^-6 + 46*A^-2 - 53*A^2 + 54*A^6 - 50*A^10 + 41*A^14 - 30*A^18 + 19*A^22 - 10*A^26 + 4*A^30 - A^34)/delta]
* delta^3 * c = `0`   [delta^3 | it: coefficient = 0]
* delta^3 * d = `-A^-30 + A^-26 - 2*A^-22 + 4*A^-18 - A^-14 + 3*A^-10 + 2*A^-6 - 3*A^-2 + 5*A^2 - 7*A^6 + 3*A^10 - 4*A^14 - A^18 + 2*A^22 - 3*A^26 + 3*A^30 - 2*A^34 + A^38`   [delta^2 | it: coefficient = (-A^-26 + 3*A^-22 - 7*A^-18 + 15*A^-14 - 24*A^-10 + 36*A^-6 - 46*A^-2 + 53*A^2 - 55*A^6 + 50*A^10 - 42*A^14 + 30*A^18 - 19*A^22 + 10*A^26 - 4*A^30 + A^34)/delta]

**K(0,0):** V = `1`, det = 1; HFK total rank 1, genus 0; spherogram simplify -> 0 crossings; snappy identify []; volume -1e-06

Grid points (direct computation): K(1,0): V = t^-2 - t^-1 + 2 - t - t^4 + t^5 - t^6 + t^7, det 1; K(0,1): V = -t^-7 + 5*t^-6 - 14*t^-5 + 29*t^-4 - 49*t^-3 + 72*t^-2 - 92*t^-1 + 106 - 108*t + 99*t^2 - 82*t^3 + 60*t^4 - 39*t^5 + 22*t^6 - 10*t^7 + 4*t^8 - t^9, det 793; K(1,1): V = -t^-9 + 5*t^-8 - 14*t^-7 + 29*t^-6 - 49*t^-5 + 72*t^-4 - 92*t^-3 + 106*t^-2 - 109*t^-1 + 101 - 83*t + 60*t^2 - 39*t^3 + 21*t^4 - 9*t^5 + 3*t^6, det 793; K(2,-1): V = t^-9 - 5*t^-8 + 14*t^-7 - 29*t^-6 + 49*t^-5 - 71*t^-4 + 91*t^-3 - 103*t^-2 + 106*t^-1 - 97 + 81*t - 61*t^2 + 40*t^3 - 24*t^4 + 12*t^5 - 5*t^6 + 2*t^7, det 791

**Rational-slot corners C** (fusion `seam_band (c1 anchor; configs 3,3b,4L,4S,6)`, see rational_slots.md): (E1) HOLDS, defect `0`; (E2) fails, defect `-A^-12 + A^-8 - 2*A^-4 + 2 - 2*A^4 + 2*A^8 - A^12 + A^16`.

## Supplementary checks (checks.json)

* c1_nonunit_turnback.py reproduction: K(0,0) PD identical = True (24 crossings); all four corner PDs/brackets identical = True.
* V_J = V(N(R(25,-9))) = `-t^-3 + 2*t^-2 - 3*t^-1 + 5 - 4*t + 4*t^2 - 3*t^3 + 2*t^4 - t^5`, det 25; config 3 has B10 = A^0 * delta^2 * V_J(t = A^-4) (c1 note eq. (6)).
* Config 4S/3b Jones-unit line K(0,n) (U-seed site twisted, seam fused): n=1: V = 1, HFK rank 1, simplify -> 0 crossings; n=2: V = 1, HFK rank 1, simplify -> 0 crossings; n=-1: V = 1, HFK rank 1, simplify -> 0 crossings; n=3: V = 1, HFK rank 1, simplify -> 0 crossings.
* K(0,0) with the crossing circle c_U of the U-seed site: 2 components, V = `-t^(-1/2) - t^(1/2)`, lk = {(0, 1): 0}, spherogram simplify -> 0 crossings with 2 free unknots (split 2-component unlink: c_U bounds a disk missing K, the site is nugatory).
* Anchor with the crossing circle of the T-seed site: {'volume': 29.462724, 'solution_type': 'all tetrahedra positively oriented', 'num_cusps': 2}; with the seam site's crossing circle: {'volume': 13.528968, 'solution_type': 'all tetrahedra positively oriented', 'num_cusps': 2} (both hyperbolic: neither circle is nugatory).
* Config 4L, seam twisted with the U-lit site turned back: m=0: V = t + t^3 - t^4, HFK rank 3; m=1: V = t + t^3 - t^4, HFK rank 3; m=2: V = t + t^3 - t^4, HFK rank 3; m=-1: V = t + t^3 - t^4, HFK rank 3 (all have the V and HFK of the trefoil: consistent with the seam twists being removable by isotopy once the U cable is turned back; evidence, not a proof).
