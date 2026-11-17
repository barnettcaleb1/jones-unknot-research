# Independent check: diag(1,-1,1,...) R^T diag(1,-1,1,...) equals the BB05 Sec 4.2 reduced matrices
# (sigma_i -> I_{i-2} + [[1,-t,0],[0,-t,0],[0,-1,1]] + I_{n-i-2}, truncated at the ends), n = 3..6.
from fractions import Fraction as F
def R(n, i, t):                      # note's R: row i of I_{n-1} replaced by (t, -t, 1) in cols i-1, i, i+1
    M = [[F(int(r == c)) for c in range(n - 1)] for r in range(n - 1)]
    r = i - 1
    for c, v in zip((r - 1, r, r + 1), (t, -t, F(1))):
        if 0 <= c < n - 1: M[r][c] = v
    return M
def BB(n, i, t):                     # BB05 reduced, 3x3 block with -t at (i,i), rows/cols i-1, i, i+1 (1-based)
    M = [[F(int(r == c)) for c in range(n - 1)] for r in range(n - 1)]
    blk = [[F(1), -t, F(0)], [F(0), -t, F(0)], [F(0), F(-1), F(1)]]
    for a in range(3):
        for b in range(3):
            r, c = i - 2 + a, i - 2 + b          # 0-based positions i-2, i-1, i
            if 0 <= r < n - 1 and 0 <= c < n - 1: M[r][c] = blk[a][b]
    return M
ok = True
for n in range(3, 7):
    D = [(-1) ** k for k in range(n - 1)]
    for i in range(1, n):
        for t in (F(2), F(-3, 7), F(5, 3)):
            RT = [list(x) for x in zip(*R(n, i, t))]
            C = [[D[r] * RT[r][c] * D[c] for c in range(n - 1)] for r in range(n - 1)]
            if C != BB(n, i, t): ok = False; print('MISMATCH', n, i, t)
print('BB05 reduced = D R^T D for all generators, n = 3..6:', ok)
