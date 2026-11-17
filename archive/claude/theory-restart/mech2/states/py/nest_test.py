import sys, collections
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mech2/states/py')
from famrel import rel_hull
pairs = [
 ('l1.x0.x0.y2.y2.u1', 'l1.x0.x0.y2.y2.y2.u1'),          # -> 8_19
 ('l1.x0.x0.y2.y2.y2.u1', 'l1.x0.x0.y2.y2.y2.y2.u1'),    # 8_19 -> one more
 ('r1.y0.y0.y2.x1.x1.u2', 'r1.y0.y0.y2.x1.x1.x1.u2'),    # 8_15-2 -> one more x1
 ('r1.y0.y0.y2.x1.x1.u2', 'r1.y0.y0.y2.y2.x1.x1.u2'),    # 8_15-2 -> one more y2
 ('l1.y0.y2.x1.y0.y2.u1', 'l1.y0.y2.y2.x1.y0.y2.u1'),    # 8_18-1 -> one more y2
 ('r1.x0.y2.x0.y2.x0.y2.u1', 'r1.x0.y2.x0.y2.x0.y2.y2.u1'),  # 9_46-1 -> one more y2
]
def blocks(multiset):
    c = collections.Counter(multiset); out = []
    while c:
        w = min(c, key=lambda p: (p[1], p[0]))
        need = [w, (w[0] + 4, w[1] + 6), (w[0] + 5, w[1] + 8), (w[0] + 9, w[1] + 14)]
        if all(c[x] > 0 for x in need):
            for x in need:
                c[x] -= 1
                if c[x] == 0: del c[x]
            out.append(w)
        else:
            return None
    return out
def main():
    out = open('/Users/calebbarnett/jones-lanes/theory-restart/mech2/states/nest_test.log', 'a')
    for a, b in pairs:
        try:
            ra = rel_hull(a, 250); rb = rel_hull(b, 250)
        except Exception as ex:
            ra = rb = None
        if ra is None or rb is None:
            line = '%s -> %s : run failed (%s, %s)' % (a, b, ra is not None, rb is not None)
        else:
            A = collections.Counter(ra[0]); B = collections.Counter(rb[0])
            lost = A - B; new = B - A
            qa = [q for h, q in ra[0]]; qb = [q for h, q in rb[0]]
            topb = sorted(p for p in rb[0] if p[1] == max(qb)); botb = sorted(p for p in rb[0] if p[1] == min(qb))
            line = '%s (dim %d) -> %s (dim %d): nested %s; lost %s; new %s; new is a union of Z-blocks: %s; top %s bottom %s' % (
                a, sum(A.values()), b, sum(B.values()), not lost, sorted(lost.elements()), sorted(new.elements()), blocks(list(new.elements())) is not None, topb, botb)
        out.write(line + '\n'); out.flush(); print(line); sys.stdout.flush()

if __name__ == "__main__":
    main()
