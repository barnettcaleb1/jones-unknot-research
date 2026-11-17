# Check: Jones polynomial of the torus knot T(2,n) (n odd) at roots of unity.
# V_{T(2,n)}(t) = t^{(n-1)/2} (1 - t^3 - t^{n+1} + t^{n+2}) / (1 - t^2)   (Jones 1987, torus knot formula, p=2)
import cmath, math
def V_poly(n):
    # exact integer coefficients: t^{(n-1)/2} * (1 + t^2 - t^3 + t^4 - ... - t^n)  [n odd]
    c = {0:1}
    for k in range(2, n+1):
        c[k] = 1 if k % 2 == 0 else -1
    sh = (n-1)//2
    return {k+sh: v for k, v in c.items()}
def check_identity(n):
    # verify (1 - t^2) * poly == t^{(n-1)/2} (1 - t^3 - t^{n+1} + t^{n+2})
    p = V_poly(n); lhs = {}
    for k, v in p.items():
        lhs[k] = lhs.get(k, 0) + v; lhs[k+2] = lhs.get(k+2, 0) - v
    sh = (n-1)//2
    rhs = {sh:1, sh+3:-1, sh+n+1:-1, sh+n+2:1}
    lhs = {k:v for k,v in lhs.items() if v}
    return lhs == rhs
def ev(p, t): return sum(v * t**k for k, v in p.items())
print("trefoil coeffs:", sorted(V_poly(3).items()), " identity ok:", check_identity(3))
for n, m in [(9,5), (13,7), (17,9), (7,8), (5,6), (21,11)]:
    assert check_identity(n)
    p = V_poly(n)
    vals = [ev(p, cmath.exp(2j*math.pi*k/m)) for k in range(1, m) if math.gcd(k, m) == 1]
    print("T(2,%d) at primitive %d-th roots of unity:" % (n, m), [complex(round(v.real, 9), round(v.imag, 9)) for v in vals])
print("-- general m (t^m = 1, t != +-1): V_{T(2,2m-1)}(t)")
for m in [3,4,6,8,10,12]:
    n=2*m-1; assert check_identity(n); p=V_poly(n)
    vals=[ev(p, cmath.exp(2j*math.pi*k/m)) for k in range(1,m) if 2*k % m != 0]
    print("m=%d, T(2,%d):" % (m,n), sorted(set((round(v.real,9)+0.0, round(v.imag,9)+0.0) for v in vals)))
