# Free-group bookkeeping for the note's construction in the basis y1,y2,y3 of Fig. 6.13.
# Letters: +k = y_k, -k = y_k^{-1}.
# Gamma_1 below is the word read off Figure 6.3 by trace_gamma1.py.
# Phi0 is written in the y-basis under ONE convention (A_{i4} = push of p4 around p_i
# passing above the intermediate points, so A34 = y1, A24 = y2 y1^-1, A14 = y3 y2^-1, and
# delta = A14 A24 A34 = y3).  The note's argument does not depend on this convention; the
# computation only illustrates it.
def red(w):
    out = []
    for x in w:
        if out and out[-1] == -x: out.pop()
        else: out.append(x)
    return out
def inv(w): return [-x for x in reversed(w)]
def mul(*ws):
    out = []
    for w in ws: out += w
    return red(out)
def comm(a, b): return mul(a, b, inv(a), inv(b))
def show(w):
    s = []
    i = 0
    while i < len(w):
        j = i
        while j < len(w) and w[j] == w[i]: j += 1
        e = (j - i) * (1 if w[i] > 0 else -1)
        s.append('y%d%s' % (abs(w[i]), '' if e == 1 else '^%d' % e))
        i = j
    return ' '.join(s) if s else '1'
def is_reduced(w): return all(w[i] != -w[i + 1] for i in range(len(w) - 1))

G1 = [-2, -1, 2, 2, -3, -2, 1, 2]
print('Gamma_1          =', show(G1), ' reduced:', is_reduced(G1), ' length', len(G1))
print('Gamma_1^-1       =', show(inv(G1)))
# conjugacy core of Gamma_1
core = G1[:]
while len(core) > 1 and core[0] == -core[-1]: core = core[1:-1]
print('cyclic core      =', show(core), '(y2 y3^-1 = x1^-1: clockwise loop around p1 alone)')
# abelianisation in x-coordinates (y1=x3, y2=x2x3, y3=x1x2x3)
ab = {1: 0, 2: 0, 3: 0}
for x in G1:
    s = 1 if x > 0 else -1
    for k in {1: [3], 2: [2, 3], 3: [1, 2, 3]}[abs(x)]: ab[k] += s
print('winding numbers of Gamma_1 about p1,p2,p3:', ab[1], ab[2], ab[3])

y1, y2, y3 = [1], [2], [3]
A34, A24, A14 = y1, mul(y2, inv(y1)), mul(y3, inv(y2))
delta = mul(A14, A24, A34)
b = comm(comm(A14, A24), A34)
Phi0 = comm(mul(inv(delta), inv(delta)), b)
print('delta            =', show(delta))
print('b                =', show(b), ' length', len(b))
print('Phi0             = %s' % show(Phi0))
print('|Phi0|_y         =', len(Phi0), ' y-exponent sums:', [sum((1 if x > 0 else -1) for x in Phi0 if abs(x) == k) for k in (1, 2, 3)])
for m in range(0, len(Phi0) + 2):
    c = mul([1] * m, Phi0, [-1] * m)
    if c and c[0] == 1 and c[-1] == -1:
        print('smallest m with y1^m Phi0 y1^-m starting y1 and ending y1^-1:', m); break
m = len(Phi0) + 1
core = mul([1] * m, Phi0, [-1] * m)
Phip = inv(G1) + core           # juxtaposition, not reduced by hand
print('m =', m, ': Gamma_1^-1 . (y1^m Phi0 y1^-m) reduced as juxtaposed?', is_reduced(Phip))
Phi = Phip + G1
print('        Phi\' . Gamma_1 reduced as juxtaposed?', is_reduced(Phi), ' length', len(Phi))
g = mul(inv(G1), [1] * m)
print('        Phi == g Phi0 g^-1 ?', red(Phi) == mul(g, Phi0, inv(g)))
print('        Phi\' ends with', show(Phip[-1:]), '; Gamma_1 begins with', show(G1[:1]))
# robustness: the construction only needs the first letter of Gamma_1 not to be y1^{+-1}
