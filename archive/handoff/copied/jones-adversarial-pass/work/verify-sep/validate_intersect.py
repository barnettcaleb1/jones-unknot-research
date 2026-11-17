import sys, random
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from intersect import *
R = Ribbon(5, 0)
c = cyc_reduce([1, 2, 3])
def I(w1, w2):
    a, b = curve(w1), curve(w2)
    return count_crossings(a, b, R), count_crossings(b, a, R)
Tc = [1, 2] * 3
tests = {
 'T_{T_d c}(c): expect 16': (s:=[3, 3] + Tc + [-3, -3]),
 'T_{T_d c}^2(c): expect 32': [3, 3] + Tc * 2 + [-3, -3],
 'T_c(T_d c) vs c: expect 4 (T_c fixes c)': Tc + [3, 3],
}
for k, w in tests.items():
    print(k, '->', I([], w))
# symmetry + naturality checks on random braids
random.seed(1)
words = [[3], [3, 3], [3, 3, 2, 4, 3, 3], [3, 3, -2, -4, 3, 3], [-3, -3, 2, 4, 3, 3], [3, 2, 4, 3]]
bad = 0
for w in words:
    base = I([], w)
    for t in range(6):
        psi = [random.choice([1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) for _ in range(5)]
        a = curve(psi); b = curve(psi + w)
        x = count_crossings(a, b, R); y = count_crossings(b, a, R)
        if not (x == y == base[0] == base[1]):
            bad += 1; print('MISMATCH', w, psi, base, x, y)
print('naturality/symmetry mismatches:', bad)
# twist inequality check |i(T_a b, c) - i(a,b) i(a,c)| <= i(b,c) with a=d (around 3,4), b = T_{d'} c
