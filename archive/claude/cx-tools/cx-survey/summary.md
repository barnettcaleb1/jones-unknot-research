# Summary table

B-corner identities per configuration (absolute bracket; "site 1 / site 2" as in the title). c=0 means delta*B10 = B11 (site 2 flat when site 1 = e); b=0 means delta*B01 = B11 (site 1 flat when site 2 = e). Also shown: single-site flatness at K(0,0) (delta*B00 = B10: site 1 flat when site 2 = I; delta*B00 = B01: site 2 flat when site 1 = I).

| cfg | fusion | site 1 | site 2 | K(0,0) | B00 = u delta | c = 0 | b = 0 | dB00=B10 | dB00=B01 | sites | xcheck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1L | unfused | T | U | 2-comp link, 14 cr | fails | fails | fails | fails | fails | para/para | ok |
| 1S | unfused | T | U | 2-comp link, 18 cr | fails | fails | fails | HOLDS | HOLDS | anti/anti | ok |
| 2L | seam_sigma2 | T | U | knot 15 cr, 7_3(0,0), det 13 | fails | fails | fails | fails | fails | para/para | ok |
| 2S | seam_sigma2 | T | U | knot 19 cr, 7_3(0,0), det 13 | fails | fails | fails | fails | fails | anti/anti | ok |
| 3 | seam_band | seam | T | knot 24 cr, unknot, det 1 | HOLDS | HOLDS | fails | fails | fails | anti/anti | ok |
| 3b | seam_band | T | U | knot 26 cr, unknot, det 1 | HOLDS | fails | fails | fails | HOLDS | anti/anti | ok |
| 4L | seam_band | seam | U | knot 24 cr, unknot, det 1 | HOLDS | fails | HOLDS | fails | fails | anti/para | ok |
| 4S | seam_band | seam | U | knot 26 cr, unknot, det 1 | HOLDS | fails | fails | fails | HOLDS | anti/anti | ok |
| 5a | top_sigma2 | T | U | knot 19 cr, 7_3(0,0), det 13 | fails | fails | fails | fails | fails | anti/anti | ok |
| 5b | bottom_sigma2 | T | U | knot 19 cr, 7_3(0,0), det 13 | fails | fails | fails | fails | fails | anti/anti | ok |
| 5c | seam_sigma2inv | T | U | knot 19 cr, K9_433(0,0), det 13 | fails | fails | fails | fails | fails | anti/anti | ok |
| 5aL | top_sigma2 | T | U | knot 15 cr, 7_3(0,0), det 13 | fails | fails | fails | fails | fails | para/para | ok |
| 5bL | bottom_sigma2 | T | U | knot 15 cr, 7_3(0,0), det 13 | fails | fails | fails | fails | fails | para/para | ok |
| 6 | seam_band | seam | T | knot 22 cr, unknot, det 1 | HOLDS | HOLDS | fails | fails | fails | anti/anti | ok |

Site realisation: L = literal box next to IntegerTangle(+-3) (not EKT-flat even on the link); S = seed box inside omega / omega_bar (EKT-flat on the link). Configs 3, 3b, 4L, 4S, 6 use the c1 seam-band fusion (ZeroTangle at the seam); 2, 5a, 5b use a sigma2 crossing; 5c sigma2^-1.

## Link calibration (config 1, one site at a time on the unfused link)

| site | delta*B_I - B_e | flat | V(1)/V(2)/V(-1) vs V(0) |
|---|---|---|---|
| T-lit | `-A^-18 - 2*A^-14 - 2*A^-10 - 2*A^-6 - 2*A^-2 - 2*A^2 - A^6` | fails | DIFFERENT / DIFFERENT / DIFFERENT |
| T-seed | `0` | HOLDS | equal / equal / equal |
| U-lit | `-A^-6 - 2*A^-2 - 2*A^2 - 2*A^6 - 2*A^10 - 2*A^14 - A^18` | fails | DIFFERENT / DIFFERENT / DIFFERENT |
| U-seed | `0` | HOLDS | equal / equal / equal |

## Rational-slot tensors (holder's C corners; reduced brackets, same framing)

| fusion | C_00 (comps) | C_0inf (comps) | C_inf0 (comps) | C_infinf (comps) | E1 | E2 defect |
|---|---|---|---|---|---|---|
| unfused | `-A^-14 - A^-6 - 2*A^-2 - 2*A^2 - A^6 - A^14` (4) | `A^-4 + 2 + A^4` (3) | `A^-4 + 2 + A^4` (3) | `-A^-2 - A^2` (2) | HOLDS | `0` |
| seam_sigma2 (H2; configs 2L,2S) | `-A^-13 - A^-5 - 2*A^3` (3) | `A + A^5` (2) | `A + A^5` (2) | `-A^3` (1) | HOLDS | `-A^-13 + A^-9 - 2*A^-5 + 2*A^-1 - 2*A^3 + 2*A^7 - A^11 + A^15` |
| seam_sigma2inv (config 5c) | `-A^-15 - A^-7 - 2*A^-3 - A^5 + A^9 - A^13 + A^17` (3) | `A^-5 + A^-1` (2) | `A^-5 + A^-1` (2) | `-A^-3` (1) | HOLDS | `-A^-11 + A^-7 - 2*A^-3 + 2*A - 2*A^5 + 2*A^9 - A^13 + A^17` |
| top_sigma2 (configs 5a,5aL) | `-A^-13 - A^-5 - 2*A^3` (3) | `A + A^5` (2) | `A + A^5` (2) | `-A^3` (1) | HOLDS | `-A^-13 + A^-9 - 2*A^-5 + 2*A^-1 - 2*A^3 + 2*A^7 - A^11 + A^15` |
| bottom_sigma2 (configs 5b,5bL) | `-A^-13 - A^-5 - 2*A^3` (3) | `A + A^5` (2) | `A + A^5` (2) | `-A^3` (1) | HOLDS | `-A^-13 + A^-9 - 2*A^-5 + 2*A^-1 - 2*A^3 + 2*A^7 - A^11 + A^15` |
| seam_band (c1 anchor; configs 3,3b,4L,4S,6) | `2 + A^8 + A^16` (3) | `-A^-2 - A^2` (2) | `-A^-2 - A^2` (2) | `1` (1) | HOLDS | `-A^-12 + A^-8 - 2*A^-4 + 2 - 2*A^4 + 2*A^8 - A^12 + A^16` |

Unfused shell: C/delta equals the target [[d^6-7d^4+15d^2-8, d],[d, 1]] exactly (components 4,3,3,2 = pattern (3,2,2,1) plus one).
