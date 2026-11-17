# Trace the gold loop Gamma_1 of BBB Figure 6.3 (raster) and read its word in the
# free basis y1, y2, y3 of Figure 6.13.
#
# Cut system dual to Fig. 6.13 (loops based at p4, run leftward along the top and
# rightward along the bottom, i.e. counterclockwise; y1 encloses p3, y2 encloses p2,p3,
# y3 encloses p1,p2,p3):
#   open segment (p2,p3) on the puncture line  <->  y1
#   open segment (p1,p2) = alpha               <->  y2
#   ray from p1 leftward to the boundary       <->  y3
# y_i crosses its dual cut once, downward; so a downward crossing reads y_i, upward y_i^-1.
# The segment (p3,p4) lies in the simply connected complement and reads nothing.
import sys
from collections import deque
import numpy as np
from PIL import Image

path = sys.argv[1]
a = np.array(Image.open(path).convert('RGB')).astype(int)
R, G, B = a[..., 0], a[..., 1], a[..., 2]
gold = (R > 180) & (B < 140) & (G > 60) & (G < 240)
H, W = gold.shape
P = {'p1': (133, 243), 'p2': (509, 243), 'p3': (838, 243), 'p4': (1189, 245)}
YL = 243  # puncture line (image row)

# cut out a disk around p4 so the two strands leaving p4 are separate components ends
cx, cy = P['p4']
yy, xx = np.mgrid[0:H, 0:W]
mask = gold & ((xx - cx) ** 2 + (yy - cy) ** 2 > 70 ** 2)

# connected components (8-neighbourhood)
lab = -np.ones((H, W), int)
comps = []
for y0 in range(H):
    for x0 in range(W):
        if mask[y0, x0] and lab[y0, x0] < 0:
            k = len(comps); q = deque([(y0, x0)]); lab[y0, x0] = k; n = 0
            while q:
                y, x = q.popleft(); n += 1
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        v, u = y + dy, x + dx
                        if 0 <= v < H and 0 <= u < W and mask[v, u] and lab[v, u] < 0:
                            lab[v, u] = k; q.append((v, u))
            comps.append(n)
print('components (pixel counts):', comps)
big = int(np.argmax(comps))
# the arrowhead is a separate small blob or attached; keep the big component
M = lab == big

def bfs(src):
    d = -np.ones((H, W), int)
    q = deque([src]); d[src] = 0
    while q:
        y, x = q.popleft()
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                v, u = y + dy, x + dx
                if 0 <= v < H and 0 <= u < W and M[v, u] and d[v, u] < 0:
                    d[v, u] = d[y, x] + 1; q.append((v, u))
    return d

# the two ends: pixels of M just outside the cut disk
ring = M & ((xx - cx) ** 2 + (yy - cy) ** 2 <= 74 ** 2)
ys, xs = np.where(ring)
print('ring pixels', len(ys), 'y-range', ys.min(), ys.max())
# split the ring pixels into two clusters by y (strands are stacked vertically there)
pts = sorted(zip(ys, xs))
# cluster by connectivity in ring
seen = set(); clusters = []
for p in pts:
    if p in seen: continue
    cl = []; q = deque([p]); seen.add(p)
    while q:
        y, x = q.popleft(); cl.append((y, x))
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                r = (y + dy, x + dx)
                if r in set(pts) and r not in seen:
                    seen.add(r); q.append(r)
    clusters.append(cl)
print('ring clusters:', [(len(c), np.mean([p[0] for p in c]).round(1), np.mean([p[1] for p in c]).round(1)) for c in clusters])
# outer (lower) strand = larger mean y
clusters.sort(key=lambda c: np.mean([p[0] for p in c]))
upper, lower = clusters[0], clusters[-1]
# arrow at (675,440) points left on the outermost bottom strand, so the loop starts on
# the strand that reaches the bottom-most curve; check which end is nearer to the arrow
dA = bfs((440, 690)) if M[440, 690] else None
if dA is None:
    # find nearest M pixel to (440,690)
    ys2, xs2 = np.where(M); i = np.argmin((ys2 - 440) ** 2 + (xs2 - 690) ** 2); dA = bfs((ys2[i], xs2[i]))
du = min(dA[p] for p in upper if dA[p] >= 0); dl = min(dA[p] for p in lower if dA[p] >= 0)
print('geodesic distance from arrow to upper end', du, 'to lower end', dl)
start = lower[0] if dl < du else upper[0]
D = bfs(start)
print('start end:', 'lower' if dl < du else 'upper', start, ' total length ~', D.max())

# crossings with the puncture line: runs of M on row YL
row = M[YL]
runs = []; x = 0
while x < W:
    if row[x]:
        j = x
        while j < W and row[j]: j += 1
        runs.append((x, j - 1)); x = j
    else:
        x += 1
events = []
for (x0, x1) in runs:
    xm = (x0 + x1) // 2
    dmid = D[YL, x0:x1 + 1][D[YL, x0:x1 + 1] >= 0].mean()
    # direction: compare distances a few rows above and below along the same strand
    def near(yr):
        cand = [(abs(u - xm), D[yr, u]) for u in range(max(0, xm - 25), min(W, xm + 26)) if M[yr, u] and D[yr, u] >= 0]
        # take the candidate whose distance is close to dmid (same strand)
        cand = [c for c in cand if abs(c[1] - dmid) < 40]
        return min(cand)[1] if cand else None
    above, below = near(YL - 8), near(YL + 8)
    down = (below is not None and above is not None and below > above)
    if xm < P['p1'][0]: cut = 'y3'
    elif xm < P['p2'][0]: cut = 'y2'
    elif xm < P['p3'][0]: cut = 'y1'
    else: cut = None
    events.append((dmid, xm, cut, 'down' if down else 'up', above, below))
events.sort()
word = []
for e in events:
    print('  dist %6.1f  x=%4d  cut=%s  %s' % (e[0], e[1], e[2], e[3]))
    if e[2]: word.append(e[2] + ('' if e[3] == 'down' else '^-1'))
print('unreduced word of Gamma_1 (order along the loop):', ' '.join(word))
