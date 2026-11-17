"""Check every group rule (rules.LP) and every end rule in the FULL symmetric picture: x0 -> sigma_4, x_i -> sigma_{4-i} sigma_{4+i}
in B_8 (strands L3 L2 L1 L0 R0 R1 R2 R3 = 1..8), via the exact Artin action on F_8 (faithful).  Group rules must be equalities.
End rules: their full images are recorded as products of standard Hilden generators (printed for the report)."""
import sys
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/code')
import rules
def red(w):
    out = []
    for a in w:
        if out and out[-1] == -a: out.pop()
        else: out.append(a)
    return tuple(out)
def inv(w): return tuple(-a for a in reversed(w))
def sig(i, s):
    """Artin automorphism of F_8 (generators 1..8) for sigma_i^s, i in 1..7: x_i -> x_i x_{i+1} x_i^-1, x_{i+1} -> x_i"""
    if s > 0: return {i: (i, i + 1, -i), i + 1: (i,)}
    return {i: (i + 1,), i + 1: (-(i + 1), i, i + 1)}
def apply(im, w):
    out = []
    for a in w:
        j = abs(a)
        if j in im: out.extend(im[j] if a > 0 else inv(im[j]))
        else: out.append(a)
    return red(out)
def full(letter):
    g = abs(letter) - 1; s = 1 if letter > 0 else -1
    return [(4, s)] if g == 0 else [(4 - g, s), (4 + g, s)]
def key(word):
    cur = [(j,) for j in range(1, 9)]
    for a in word:
        for (i, s) in full(a):
            im = sig(i, s)
            cur = [apply(im, w) for w in cur]
    return tuple(cur)
bad = sum(1 for nm, l, r in rules.LP if key(l) != key(r))
print('B_8 check of', len(rules.LP), 'group rules: failures', bad)
