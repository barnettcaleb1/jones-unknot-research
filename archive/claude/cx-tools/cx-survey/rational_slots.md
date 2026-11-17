# Rational-slot corners C (holder's second addition)

Labels: '0' = ZeroTangle inserted in the slot before the shell's rotate(1) (cable straight through); 'inf' = InfinityTangle (cable turned back).
C_ab: a = T slot, b = U slot.  REDUCED brackets (<O>=1), same outside framing.  Equations tested on the reduced brackets.
delta = -A^2 - A^-2, F = (delta^2-2)(delta^2-4).  Target/delta = [[d^6-7d^4+15d^2-8, d],[d, 1]], component pattern (3,2,2,1) = actual components minus one.

## unfused

| C_ab | comps | cr | writhe | reduced bracket | /delta | vs target |
|---|---|---|---|---|---|---|
| C_00 | 4 | 8 | -8 | -A^-14 - A^-6 - 2*A^-2 - 2*A^2 - A^6 - A^14 | A^-12 - A^-8 + 2*A^-4 + 2*A^4 - A^8 + A^12 | exact |
| C_0inf | 3 | 8 | 0 | A^-4 + 2 + A^4 | -A^-2 - A^2 | exact |
| C_inf0 | 3 | 8 | 0 | A^-4 + 2 + A^4 | -A^-2 - A^2 | exact |
| C_infinf | 2 | 8 | 0 | -A^-2 - A^2 | 1 | exact |

(E1) C_0inf - C_inf0 = 0  -> HOLDS
(E2) C_00 - delta (delta^2-3)^2 r + F C_infinf  (r = C_0inf) = 0  -> HOLDS

## seam_sigma2 (H2; configs 2L,2S)

| C_ab | comps | cr | writhe | reduced bracket | /delta | vs target |
|---|---|---|---|---|---|---|
| C_00 | 3 | 9 | -7 | -A^-13 - A^-5 - 2*A^3 | not divisible by delta | different |
| C_0inf | 2 | 9 | 1 | A + A^5 | -A^3 | different |
| C_inf0 | 2 | 9 | 1 | A + A^5 | -A^3 | different |
| C_infinf | 1 | 9 | 1 | -A^3 | not divisible by delta | different |

(E1) C_0inf - C_inf0 = 0  -> HOLDS
(E2) C_00 - delta (delta^2-3)^2 r + F C_infinf  (r = C_0inf) = -A^-13 + A^-9 - 2*A^-5 + 2*A^-1 - 2*A^3 + 2*A^7 - A^11 + A^15  -> FAILS

## seam_sigma2inv (config 5c)

| C_ab | comps | cr | writhe | reduced bracket | /delta | vs target |
|---|---|---|---|---|---|---|
| C_00 | 3 | 9 | -9 | -A^-15 - A^-7 - 2*A^-3 - A^5 + A^9 - A^13 + A^17 | not divisible by delta | different |
| C_0inf | 2 | 9 | -1 | A^-5 + A^-1 | -A^-3 | different |
| C_inf0 | 2 | 9 | -1 | A^-5 + A^-1 | -A^-3 | different |
| C_infinf | 1 | 9 | -1 | -A^-3 | not divisible by delta | different |

(E1) C_0inf - C_inf0 = 0  -> HOLDS
(E2) C_00 - delta (delta^2-3)^2 r + F C_infinf  (r = C_0inf) = -A^-11 + A^-7 - 2*A^-3 + 2*A - 2*A^5 + 2*A^9 - A^13 + A^17  -> FAILS

## top_sigma2 (configs 5a,5aL)

| C_ab | comps | cr | writhe | reduced bracket | /delta | vs target |
|---|---|---|---|---|---|---|
| C_00 | 3 | 9 | -7 | -A^-13 - A^-5 - 2*A^3 | not divisible by delta | different |
| C_0inf | 2 | 9 | 1 | A + A^5 | -A^3 | different |
| C_inf0 | 2 | 9 | 1 | A + A^5 | -A^3 | different |
| C_infinf | 1 | 9 | 1 | -A^3 | not divisible by delta | different |

(E1) C_0inf - C_inf0 = 0  -> HOLDS
(E2) C_00 - delta (delta^2-3)^2 r + F C_infinf  (r = C_0inf) = -A^-13 + A^-9 - 2*A^-5 + 2*A^-1 - 2*A^3 + 2*A^7 - A^11 + A^15  -> FAILS

## bottom_sigma2 (configs 5b,5bL)

| C_ab | comps | cr | writhe | reduced bracket | /delta | vs target |
|---|---|---|---|---|---|---|
| C_00 | 3 | 9 | 1 | -A^-13 - A^-5 - 2*A^3 | not divisible by delta | different |
| C_0inf | 2 | 9 | 1 | A + A^5 | -A^3 | different |
| C_inf0 | 2 | 9 | 1 | A + A^5 | -A^3 | different |
| C_infinf | 1 | 9 | 1 | -A^3 | not divisible by delta | different |

(E1) C_0inf - C_inf0 = 0  -> HOLDS
(E2) C_00 - delta (delta^2-3)^2 r + F C_infinf  (r = C_0inf) = -A^-13 + A^-9 - 2*A^-5 + 2*A^-1 - 2*A^3 + 2*A^7 - A^11 + A^15  -> FAILS

## seam_band (c1 anchor; configs 3,3b,4L,4S,6)

| C_ab | comps | cr | writhe | reduced bracket | /delta | vs target |
|---|---|---|---|---|---|---|
| C_00 | 3 | 8 | 0 | 2 + A^8 + A^16 | not divisible by delta | different |
| C_0inf | 2 | 8 | 0 | -A^-2 - A^2 | 1 | different |
| C_inf0 | 2 | 8 | 0 | -A^-2 - A^2 | 1 | different |
| C_infinf | 1 | 8 | 0 | 1 | not divisible by delta | different |

(E1) C_0inf - C_inf0 = 0  -> HOLDS
(E2) C_00 - delta (delta^2-3)^2 r + F C_infinf  (r = C_0inf) = -A^-12 + A^-8 - 2*A^-4 + 2 - 2*A^4 + 2*A^8 - A^12 + A^16  -> FAILS

