# Floating-point sanity check of the limit statement used in Theorem A (not a proof; the proof is in REFEREE.md):
# inside a hyperbolic ball of radius R around a base point x, the elements of Gamma_n^ext = <J_n,M_n,E_n> are, for large n,
# exactly the evaluations at A_n of the abstract elements of Gamma^ext = PGL(2,Z) lying in (about) the same ball at A_0.
# Elements are tracked EXACTLY as abstract elements of PGL(2,Z) (integer matrices up to sign, via the D-gauge at A_0:
# J -> [[0,1],[-1,0]], M -> [[1,0],[-1,1]], E -> [[0,1],[1,0]]); only the displacement is computed in floating point.
# (First version of this script used rounded floating keys with an unstable sign normalisation and produced spurious
#  duplicates; that was a bug of the checker, fixed here by exact labels.)
import cmath, math
def mats(A):
    d = (-A**2 - A**-2).real
    G = ((d,1),(1,d)); M = ((A,0),(1/A,-A**-3)); J=((0,1),(1,0)); E=((d,1),(-1,-d))
    det = -A**-2
    Mi = ((-A**-3/det, 0),(-(1/A)/det, A/det))
    return d,G,{'J':J,'M':M,'m':Mi,'E':E}
LAB = {'J':((0,1),(-1,0)), 'M':((1,0),(-1,1)), 'm':((1,0),(1,1)), 'E':((0,1),(1,0))}
def mul(X,Y): return ((X[0][0]*Y[0][0]+X[0][1]*Y[1][0], X[0][0]*Y[0][1]+X[0][1]*Y[1][1]),(X[1][0]*Y[0][0]+X[1][1]*Y[1][0], X[1][0]*Y[0][1]+X[1][1]*Y[1][1]))
def app(X,v): return (X[0][0]*v[0]+X[0][1]*v[1], X[1][0]*v[0]+X[1][1]*v[1])
def herm(G,v,w): return v[0].conjugate()*(G[0][0]*w[0]+G[0][1]*w[1]) + v[1].conjugate()*(G[1][0]*w[0]+G[1][1]*w[1])
def disp(G,x,g):
    w = app(g,x)
    if herm(G,w,w).real > 0:
        a = G[0][0]*w[0]+G[0][1]*w[1]; b = G[1][0]*w[0]+G[1][1]*w[1]
        w = (b.conjugate(), -a.conjugate())
    c2 = (abs(herm(G,x,w))**2)/(herm(G,x,x).real*herm(G,w,w).real)
    return 2*math.acosh(math.sqrt(max(c2,1.0)))
def lab_key(L):
    t = (L[0][0],L[0][1],L[1][0],L[1][1])
    for z in t:
        if z != 0:
            return t if z > 0 else tuple(-u for u in t)
def bfs(A, Rprune):
    d,G,gen = mats(A)
    x = (1+(0.15+0.1j), -1+(0.15+0.1j))
    assert herm(G,x,x).real < 0
    I = ((1,0),(0,1)); seen = {lab_key(I): 0.0}; frontier=[(I,I)]
    while frontier:
        nxt=[]
        for L,g in frontier:
            for c in 'JMmE':
                L2 = mul(L, LAB[c]); k = lab_key(L2)
                if k in seen: continue
                h = mul(g, gen[c]); dd = disp(G,x,h)
                if dd > Rprune: continue
                # renormalise numeric matrix to keep entries O(1)
                s = max(abs(h[0][0]),abs(h[0][1]),abs(h[1][0]),abs(h[1][1]))
                h = ((h[0][0]/s,h[0][1]/s),(h[1][0]/s,h[1][1]/s))
                seen[k] = dd; nxt.append((L2,h))
                assert len(seen) < 400000, 'BFS cap hit'
        frontier = nxt
    return seen
# consistency of the labelling: the three defining relations hold in both pictures (checked symbolically in s1_exact.py)
R = 3.0; Rprune = 7.5; eps = 0.05   # Rprune >= 2R + O(1) so that the pruned BFS reaches every tile meeting B(x,R)
A0 = cmath.exp(1j*math.pi/4)
seen0 = bfs(A0, Rprune)
B0 = lambda r: {k for k,v in seen0.items() if v <= r}
print('Gamma_0^ext = PGL(2,Z): #elements with displacement <= %.2f : %d   (pruned BFS at %.1f found %d)'%(R, len(B0(R)), Rprune, len(seen0)))
# only n with 2*d(x, vertex of order n) > Rprune: otherwise the abstract BFS runs into the (infinite) kernel of
# specialisation <<M^n>> and does not terminate (this is the 'kernel of specialisation' phenomenon, harmless for large n).
for n in (501, 2001, 20001, 200001):
    An = cmath.exp(1j*math.pi/4 - 1j*math.pi/(2*n))
    seenn = bfs(An, Rprune)
    Bn = lambda r: {k for k,v in seenn.items() if v <= r}
    only_n = Bn(R) - B0(R+eps)       # elements in the n-ball whose abstract element is not in the (slightly larger) limit ball
    only_0 = B0(R) - Bn(R+eps)
    common = set(seen0) & set(seenn)
    maxdd = max(abs(seen0[k]-seenn[k]) for k in common if seen0[k] <= R+1)
    print('n=%7d: |B_n(R)|=%4d  |B_n(R) minus B_0(R+eps)|=%3d  |B_0(R) minus B_n(R+eps)|=%3d  max|d_n-d_0| on B_0(R+1) = %.5f' % (n, len(Bn(R)), len(only_n), len(only_0), maxdd))
