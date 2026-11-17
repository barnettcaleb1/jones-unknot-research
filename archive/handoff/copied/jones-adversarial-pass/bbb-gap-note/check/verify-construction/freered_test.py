# Randomised sanity test of the note's free-reduction step (Section 4, l. 58-61),
# using only what the note uses: Gamma_1 is a reduced word whose FIRST letter is y2^-1
# (paper p. 25 top line), and Phi0 is a nontrivial element of [F_3, F_3].
# Claim tested: for m > |Phi0|, with Phi' = Gamma_1^-1 y1^m Phi0 y1^-m,
#   (i)  the juxtaposition  red(Gamma_1^-1) + red(y1^m Phi0 y1^-m)  is reduced,
#   (ii) the juxtaposition  red(Phi') + Gamma_1  is reduced,
#   (iii) Phi' Gamma_1 = g Phi0 g^-1 with g = Gamma_1^-1 y1^m.
import random

def red(w):
    out = []
    for x in w:
        if out and out[-1] == -x:
            out.pop()
        else:
            out.append(x)
    return out

def inv(w):
    return [-x for x in reversed(w)]

def is_red(w):
    return all(w[i] != -w[i + 1] for i in range(len(w) - 1))

def rand_reduced(L, first=None):
    w = [first] if first is not None else []
    while len(w) < L:
        x = random.choice([1, 2, 3, -1, -2, -3])
        if w and w[-1] == -x:
            continue
        w.append(x)
    return w

def comm(a, b):
    return red(a + b + inv(a) + inv(b))

random.seed(20261103)
bad = 0
trials = 0
for _ in range(20000):
    G = rand_reduced(random.randint(1, 12), first=-2)
    # random nontrivial commutator-subgroup element: product of 1-3 commutators
    P = []
    for _k in range(random.randint(1, 3)):
        P = red(P + comm(rand_reduced(random.randint(1, 6)), rand_reduced(random.randint(1, 6))))
    if not P:
        continue
    trials += 1
    m = len(P) + 1
    core = red([1] * m + P + [-1] * m)
    Phip_juxt = red(inv(G)) + core
    ok1 = is_red(Phip_juxt)
    Phip = red(Phip_juxt)
    ok2 = is_red(Phip + G) and Phip[-1] == -1 and G[0] == -2
    g = red(inv(G) + [1] * m)
    ok3 = red(Phip + G) == red(g + P + inv(g))
    if not (ok1 and ok2 and ok3):
        bad += 1
print("trials:", trials, " failures:", bad)

# the step really needs the first letter of Gamma_1 to differ from y1 (the conjugating letter):
G = [1, 2, -3]
P = comm([2], [3])
m = len(P) + 1
core = red([1] * m + P + [-1] * m)
print("control (Gamma_1 starting with y1): juxtaposition reduced?", is_red(red(inv(G)) + core))
