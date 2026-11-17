# Sanity checks on the Figure 6.3 trace: ordered centreline, continuity (no shortcut
# through a self-crossing), winding numbers about p1,p2,p3, and the sign pattern of the
# crossings with alpha ordered along alpha.
import sys, math
from collections import deque
import numpy as np
from PIL import Image

a = np.array(Image.open(sys.argv[1]).convert('RGB')).astype(int)
R, G, B = a[..., 0], a[..., 1], a[..., 2]
gold = (R > 180) & (B < 140) & (G > 60) & (G < 240)
H, W = gold.shape
P = {'p1': (133, 243), 'p2': (509, 243), 'p3': (838, 243), 'p4': (1189, 245)}
cx, cy = P['p4']
yy, xx = np.mgrid[0:H, 0:W]
M = gold & ((xx - cx) ** 2 + (yy - cy) ** 2 > 70 ** 2)
# erase the arrowhead barbs (small region around (675,440)) except the main strand rows
def bfs(src):
    d = -np.ones((H, W), int); q = deque([src]); d[src] = 0
    while q:
        y, x = q.popleft()
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                v, u = y + dy, x + dx
                if 0 <= v < H and 0 <= u < W and M[v, u] and d[v, u] < 0:
                    d[v, u] = d[y, x] + 1; q.append((v, u))
    return d
start = (292, 1137)   # lower end (outer strand), found by trace_gamma1.py
D = bfs(start)
L = D.max()
cent = []
step = 6
for d0 in range(0, L + 1, step):
    sel = (D >= d0) & (D < d0 + step)
    ys, xs = np.where(sel)
    if len(ys) == 0: continue
    cent.append((xs.mean(), ys.mean(), xs.std() + ys.std()))
jumps = [math.hypot(cent[i + 1][0] - cent[i][0], cent[i + 1][1] - cent[i][1]) for i in range(len(cent) - 1)]
print('centreline samples', len(cent), ' max step between samples %.1f px' % max(jumps),
      ' max cross-section spread %.1f px' % max(c[2] for c in cent))
big = [(i, round(j, 1)) for i, j in enumerate(jumps) if j > 12]
print('large steps (possible shortcut):', big[:10])
# close the loop through p4: start at p4, centreline, back to p4
pts = [(cx, cy)] + [(c[0], c[1]) for c in cent] + [(cx, cy)]
for name in ('p1', 'p2', 'p3'):
    px, py = P[name]
    tot = 0.0
    for i in range(len(pts) - 1):
        a1 = math.atan2(-(pts[i][1] - py), pts[i][0] - px)      # flip y: image y points down
        a2 = math.atan2(-(pts[i + 1][1] - py), pts[i + 1][0] - px)
        da = a2 - a1
        while da > math.pi: da -= 2 * math.pi
        while da < -math.pi: da += 2 * math.pi
        tot += da
    print('winding number of Gamma_1 about %s: %+.3f (counterclockwise positive)' % (name, tot / (2 * math.pi)))
# sign pattern along alpha: crossings of row 243 between p1 and p2, ordered by x
YL = 243
row = M[YL]; runs = []; x = 0
while x < W:
    if row[x]:
        j = x
        while j < W and row[j]: j += 1
        runs.append((x, j - 1)); x = j
    else: x += 1
pat = []
for x0, x1 in runs:
    xm = (x0 + x1) // 2
    if not (P['p1'][0] < xm < P['p2'][0]): continue
    d = D[YL, xm]
    # direction from the centreline: find the centreline sample nearest in distance
    up = [D[YL - 8, u] for u in range(xm - 20, xm + 21) if M[YL - 8, u] and abs(D[YL - 8, u] - d) < 40]
    dn = [D[YL + 8, u] for u in range(xm - 20, xm + 21) if M[YL + 8, u] and abs(D[YL + 8, u] - d) < 40]
    pat.append((xm, 'down' if np.mean(dn) > np.mean(up) else 'up'))
print('crossings of Gamma_1 with alpha, left to right along alpha:', pat)
