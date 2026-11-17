# Exact enumeration with the signature (Gauss-Bonnet) formula  area/2pi = 2g-2+s+sum(1-1/m_i).
# The area is strictly increasing in g, s, the number r of cone points and each period m_i, so small search boxes
# are exhaustive for "minimum" / "below a threshold" questions (bounds justified in REFEREE.md).
from fractions import Fraction as F
from itertools import combinations_with_replacement as cwr
# (a) non-cocompact finite-area Fuchsian groups (s>=1 cusps): minimal area.
res = []
for g in range(0,2):
    for s in range(1,4):
        for r in range(0,4):
            for ms in cwr(range(2,41), r):
                a = 2*g-2+s+sum(1-F(1,m) for m in ms)
                if a > 0: res.append((a,g,s,ms))
res.sort()
print('(a) three smallest non-cocompact areas/2pi:', res[:3])
assert res[0][0] == F(1,6) and res[1][0] > F(1,6) and res[0][1:] == (0,1,(2,3))
# (b) cocompact signatures of area/2pi < 1/12 having a period >= 7.
cands = []
for g in range(0,2):
    for r in range(0,5):
        for ms in cwr(range(2,121), r) if r<=3 else cwr(range(2,6), r):
            a = 2*g-2+sum(1-F(1,m) for m in ms)
            if 0 < a < F(1,12): cands.append((g,ms,a))
print('(b) all cocompact signatures with 0 < area/2pi < 1/12:', [(g,ms,str(a)) for g,ms,a in cands])
for (g,ms,a) in cands:
    m = max(ms)
    for n in range(7, m+1):
        if m % n == 0:
            print('   candidate overgroup', ms, 'of Delta(2,3,%d): index would be'%n, (F(1,6)-F(1,n))/a, '(must be an integer >= 2)')
