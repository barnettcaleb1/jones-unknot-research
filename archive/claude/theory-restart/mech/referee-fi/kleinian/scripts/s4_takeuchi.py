# Takeuchi's arithmeticity criterion for Delta(2,3,n) (Takeuchi, J. Math. Soc. Japan 29 (1977), Thm 1/3):
# arithmetic  <=>  for every Galois conjugate sigma != id of k = Q(cos(2pi/n)),
#     sigma( cos^2(pi/2)+cos^2(pi/3)+cos^2(pi/n)+2cos(pi/2)cos(pi/3)cos(pi/n)-1 ) < 0,
# i.e. cos(2 pi k/n) < 1/2 for all k coprime to n with k != +-1 mod n,
# i.e. no unit k mod n with 1 < k < n/6 (k/n in (1/6,5/6) required).
from math import gcd
from fractions import Fraction
def arithmetic(n):
    for k in range(2, n-1):
        if gcd(k,n)==1:
            x = Fraction(k,n)
            if not (Fraction(1,6) < x < Fraction(5,6)): return False
    return True
L = [n for n in range(7, 200001) if arithmetic(n)] if False else [n for n in range(7, 20001) if arithmetic(n)]
print('arithmetic (2,3,n), 7<=n<=20000 :', L)
# maximality of Delta(2,3,n): any Fuchsian overgroup of index k>=2 has area <= pi(1/6-1/n) < pi/6 and contains an
# elliptic of order n; enumerate cocompact signatures with area < pi/6 containing a period divisible by n.
