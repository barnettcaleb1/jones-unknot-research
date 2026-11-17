"""
validate_section7.py -- check the whole pipeline against the paper's Section 7 example.
Inputs: cutting sequences traced from Fig 7.1 (arc beta), Fig 7.2 (loop Gamma based at p5),
        Fig 7.3 ((beta)Gamma), Fig 7.4 ((beta*_3)Gamma).
Paper's numbers:
  M_Phi      = t^0 + t^2 + t^4 - t^3 - t + t^-3 + t^-1 + t        (8 terms, in order along beta)
  M_{Phi.Gamma} = t^0 + t^2 + t^4 - t^3 - t + t^-4 + t^-2 + t^0
  M_Gamma    = -t^0 - t^2 + t + t^-1 - t^0 - t^2 + t^3 + t + t^-1 - t^-2 - t^0 + t^-1 + t^-3 - t^-2 - t^0 + t + t^-1 + t^-3 - t^-2 - t^0
             = 2t^-3 - 3t^-2 + 4t^-1 - 5 + 3t - 2t^2 + t^3
"""
import sys, json
sys.path.insert(0, '/private/tmp/claude-501/-Users-calebbarnett/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/bbb-attack/scripts')
from braidarc import *

def fmt_terms(terms):
    return " ".join(("+" if e > 0 else "-") + "t^%d" % a + ("u^%d" % b if b else "") for e, (a, b) in terms)

def normalized_signed(terms):
    """paper style: first term +t^0 (global sign and shift)."""
    if not terms: return []
    s = terms[0][0]; a0, b0 = terms[0][1]
    return [(e * s, (a - a0, b - b0)) for e, (a, b) in terms]

var4 = {j: 0 for j in range(1, 6)}          # all t (single variable) for the paper comparison
var5 = {j: (1 if j == 5 else 0) for j in range(1, 6)}

# --- traced sequences
T71 = [1, 3, 1, 3, 1, 2, 3, 1, 3, 1, 4, 0, 1, 3, 1, 3, 1]          # Fig 7.1, arc in D4 (also in D5)
T73 = [1, 3, 1, 3, 1, 2, 3, 1, 3, 1, 5, 0, 1, 3, 1, 3, 1]          # Fig 7.3, (beta)Gamma in D5
T74 = [5, 4, 1, 3, 1, 2, 3, 1, 3, 1, 4, 5, 1, 3, 1, 3, 2, 1, 3, 1, 3, 1, 5, 4, 1, 3, 1, 2, 3, 1, 3, 1, 4, 5,
       1, 3, 1, 3, 2, 1, 3, 1, 3, 1, 5, 4, 1, 3, 1]                  # Fig 7.4, (beta*_3)Gamma in D5
G72 = ([0, 1, 3, 1, 3, 1, 2, 3, 1, 3, 1], 'U')                      # Fig 7.2 gold loop at p5, gamma1 then gamma2 (no crossings)
if len(sys.argv) > 1:
    tr = json.load(open(sys.argv[1]))
    G72 = (tr['reduced'], tr['start_half'])
    print("using traced Gamma sequence", G72)

print("=== Fig 7.1 arc: T =", T71)
w = walk_arc(T71, 3, var4)
print(" literal terms :", fmt_terms(w['terms']))
print(" paper-normal. :", fmt_terms(normalized_signed(w['terms'])))
print(" paper says    : +t^0 +t^2 +t^4 -t^3 -t^1 +t^-3 +t^-1 +t^1")
for d in disk_sequence(T71, 3, var4):
    print("  disk", d['i'], "P=", d['P'], "W=", d['W'], "eps=", d['eps'], "parity_ok=", d['parity_ok'])

print("=== Fig 7.3 arc (beta)Gamma: T =", T73)
w = walk_arc(T73, 3, var5)
print(" paper-normal. :", fmt_terms(normalized_signed(w['terms'])), "   (u = t gives paper's)")
print(" paper says    : +t^0 +t^2 +t^4 -t^3 -t^1 +t^-4 +t^-2 +t^0")

print("=== Fig 7.4 arc (beta*_3)Gamma: T =", T74)
w = walk_arc(T74, 3, var5)
print(" terms(u=t)    :", fmt_terms(normalized_signed([(e, (a + b, 0)) for e, (a, b) in w['terms']])))
print(" paper says    : -t^0 -t^2 +t +t^-1 -t^0 -t^2 +t^3 +t +t^-1 -t^-2 -t^0 +t^-1 +t^-3 -t^-2 -t^0 +t +t^-1 +t^-3 -t^-2 -t^0 (times -1 => first +)")
P74 = lp_from_terms(w['terms']).set_u_eq_t()
print(" simplified (u=t):", P74, "  paper: 2t^-3 - 3t^-2 + 4t^-1 - 5 + 3t - 2t^2 + t^3 (up to +-t^k)")

print("=== Fig 7.2 loop Gamma -> push braid")
seq, sh = G72
Wx = loop_seq_to_xprime_word(seq, sh, 5)
Wy = xprime_to_nested(Wx, 5)
print(" word in x'_j :", Wx)
print(" word in Y_k  :", Wy, "  (Y_k = ccw loop of p5 around {p_{5-k},..,p_4})")
braidG = push_braid_xprime(Wx, 5)
braidG2 = push_braid_nested(Wy, 5)
print(" push braid   :", braidG, " len", len(braidG))
assert braid_perm(braidG, 5) == list(range(6))
# check both braid words give the same Burau matrix
assert burau(braidG, 5) == burau(braidG2, 5)

# (beta*_3) Gamma
Tg = arc_of_braid(braidG, 3)
print(" (beta*_3)Gamma cutting sequence:", Tg)
print("   equals Fig 7.4 trace?", Tg == T74)
wg = walk_arc(Tg, 3, var5)
print("   M_Gamma (u=t, paper-normalized):", fmt_terms(normalized_signed([(e, (a + b, 0)) for e, (a, b) in wg['terms']])))
print("   simplified:", lp_from_terms(wg['terms']).set_u_eq_t())
# (beta) Gamma with beta = Fig 7.1 arc
W71 = loopword_from_arc(T71, 3)
Wimg = apply_braid_to_word(W71, braidG)
Tbg = arc_from_loopword(Wimg, 3)
print(" (beta)Gamma cutting sequence:", Tbg)
print("   equals Fig 7.3 trace?", Tbg == T73)
wb = walk_arc(Tbg, 3, var5)
print("   M (u=t, paper-normalized):", fmt_terms(normalized_signed([(e, (a + b, 0)) for e, (a, b) in wb['terms']])))
# also test the inverse loop for contrast
braidGi = braid_inverse(braidG)
Tgi = arc_of_braid(braidGi, 3)
print(" contrast: (beta*_3)Gamma^{-1} has", len([a for a in Tgi if a == 1]), "alpha crossings; (beta*_3)Gamma has", len([a for a in Tg if a == 1]))
