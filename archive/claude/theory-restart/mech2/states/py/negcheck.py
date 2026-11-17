import sys, os, glob, json, collections
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mech2/states/py')
from bcube import *
from badblocks import bad_blocks, SI
names = sorted(os.path.basename(f)[:-4] for f in glob.glob(SI + '/*.kht'))
GEN = {'3_1':1,'5_1':2,'5_2':1,'7_1':3,'7_2':1,'7_3':2,'7_4':1,'7_5':2,'8_15':2,'8_19':3,'9_1':4,'9_2':1,'9_3':3,'9_4':2,'9_5':1,'9_6':3,'9_7':2,'9_9':3,'9_10':2,'9_13':2,'9_16':3,'9_18':2,'9_23':2,'9_35':1,'9_38':2,'9_49':2}
out = []
for nm in names:
    half, orient, sym = read_kht(os.path.join(SI, nm + '.kht'))
    c = sum(1 for (l, i) in half if l in 'xy')
    wr, signs = half_writhe(half)
    if abs(wr) != c:
        continue
    end = 1 if wr < 0 else 0      # Seifert end
    blocks, k = bad_blocks(half, end)
    nb = sum(1 for b in blocks if b['nbad'])
    ca = sum(1 for (l, i) in half if l in 'xy' and i == 0); co = c - ca
    # canonical genus from the formula  k = 2 ca + 2 loops
    loops = (k - 2 * ca) / 2
    g = co - loops
    n = 4 * c
    if wr < 0:
        M = n + k; d0 = 2 * c - 4 * wr; gap = d0 - M
    else:
        m = -k; d0 = 2 * c - 4 * wr; gap = m - d0
    knot = nm.split('-')[0]
    out.append((nm, 'neg' if wr < 0 else 'pos', c, ca, co, k, loops, g, gap, nb, GEN.get(knot)))
print('name sign c c_axis c_off k(Seifert state) loops canonical_genus (unit - corner) badblocks genus(table, recalled)')
for o in out: print(*o)
print(len(out), 'half-diagrams with |writhe| = c')
