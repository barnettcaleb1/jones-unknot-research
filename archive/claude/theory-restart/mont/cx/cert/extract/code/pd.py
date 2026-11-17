"""Planar diagram (PD) of the covering knot K of a halfword, and Reidemeister simplification with validated moves.
A crossing c has 4 slots in COUNTERCLOCKWISE order; opposite slots (s, s+2) belong to the same strand; over[c] = 0 if the
over strand uses slots {0,2}, 1 if {1,3}.  An edge joins two slots.  conn[(c,s)] = partner slot.
Moves (each checked before it is applied):
  R1 : conn[(c,s)] == (c,s+1)  (monogon; the face is empty because the projection is connected)
  R2 : conn[(c1,s)] = (c2,t), conn[(c1,s+1)] = (c2,t-1), c1 != c2 (bigon face), and the same strand is over at both
  R3 : triangle face c1,c2,c3 (consecutive face slots adjacent at each crossing) with one strand over (or under) at both of
       its triangle crossings; the triangle is flipped (each strand's two triangle crossings swap order).
Removal of crossings (R1/R2) = delete them and rewire every strand straight through."""
import sys, random
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')
import alex
class PD:
    def __init__(self):
        self.slots = {}     # c -> [None]*4 not needed; we keep conn and over
        self.conn = {}      # (c,s) -> (c',s')
        self.over = {}      # c -> 0/1
        self.next_id = 0
        self.log = []
    def copy(self):
        q = PD(); q.conn = dict(self.conn); q.over = dict(self.over); q.next_id = self.next_id; q.log = list(self.log); return q
    def crossings(self): return list(self.over)
    def n(self): return len(self.over)
    def is_over(self, c, s): return (s % 2) == self.over[c]
    def link(self, a, b): self.conn[a] = b; self.conn[b] = a
    @staticmethod
    def from_halfword(word):
        full = alex.symmetrize(alex.parse(word))
        cr = alex.diagram(full)
        if cr is None: return None
        q = PD()
        ends = {}
        for k, x in enumerate(cr):
            if x['ty'] == 'x': sl = [x['ot'], x['ub'], x['ob'], x['ut']]; ov = 0      # [TL, BL, BR, TR]
            else: sl = [x['ut'], x['ob'], x['ub'], x['ot']]; ov = 1
            q.over[k] = ov
            for s, e in enumerate(sl): ends.setdefault(e, []).append((k, s))
        for e, v in ends.items():
            assert len(v) == 2, (e, v)
            q.link(v[0], v[1])
        q.next_id = len(cr)
        return q
    # ---------------- removal with straight-through rewiring ----------------
    def remove(self, S):
        S = set(S)
        newconn = {}
        done = set()
        for (c, s), p in list(self.conn.items()):
            if c in S or (c, s) in done: continue
            # follow from slot (c,s) outward
            q = p; steps = 0
            while q[0] in S:
                q2 = (q[0], (q[1] + 2) % 4)
                q = self.conn[q2]; steps += 1
                if steps > 4 * len(S) + 4: raise RuntimeError('rewire loop')
            newconn[(c, s)] = q; newconn[q] = (c, s); done.add((c, s)); done.add(q)
        self.conn = newconn
        for c in S: del self.over[c]
    # ---------------- move finders ----------------
    def find_R1(self):
        for (c, s), (c2, s2) in self.conn.items():
            if c2 == c and (s2 - s) % 4 in (1, 3): return c
        return None
    def find_R1s(self):
        for (c, s), (c2, s2) in self.conn.items():
            if c2 == c and (s2 - s) % 4 == 1: return (c, s)
        return None
    def find_R2(self):
        r = self.find_R2s()
        return None if r is None else (r[0], r[2])
    def find_R2s(self):
        for (c1, s), (c2, t) in self.conn.items():
            if c2 == c1: continue
            a = self.conn[(c1, (s + 1) % 4)]
            if a == (c2, (t - 1) % 4) and self.is_over(c1, s) == self.is_over(c2, t):
                return (c1, s, c2, t)
        return None
    def check_R1(self, c, s):
        return self.conn.get((c, s)) == (c, (s + 1) % 4)
    def check_R2(self, c1, s, c2, t):
        return (c1 != c2 and self.conn.get((c1, s)) == (c2, t) and self.conn.get((c1, (s + 1) % 4)) == (c2, (t - 1) % 4)
                and self.is_over(c1, s) == self.is_over(c2, t))
    def simplify_R12(self):
        while True:
            r = self.find_R1s()
            if r is not None:
                self.log.append(('R1',) + r); self.remove([r[0]]); continue
            p = self.find_R2s()
            if p is not None:
                self.log.append(('R2',) + p); self.remove([p[0], p[2]]); continue
            return
    def triangles(self):
        """faces with exactly 3 sides and 3 distinct crossings: list of [(c,s_in,s_out) ...]"""
        out = []; seen = set()
        for start in self.conn:
            if start in seen: continue
            # trace face: from slot (c,s) go along edge to (c',s'), then turn to (c', s'-1)  [consistent face tracing]
            face = []; x = start; ok = True
            while True:
                seen.add(x)
                y = self.conn[x]
                z = (y[0], (y[1] - 1) % 4)
                face.append((x, y))
                x = z
                if x == start: break
                if len(face) > 3: ok = False
                if len(face) > 4 * len(self.over) + 4: ok = False; break
            if ok and len(face) == 3:
                cs = [f[1][0] for f in face]
                if len(set(cs)) == 3: out.append(face)
        return out
    def r3_data(self, face):
        """validity check for R3 on a triangle face; returns the list of (slot_start, slot_end) outer slot pairs or None"""
        C = [face[i][0][0] for i in range(3)]
        if len(set(C)) != 3: return None
        ok = False; outer = []
        for i in range(3):
            x, y = face[i]
            if self.is_over(x[0], x[1]) == self.is_over(y[0], y[1]): ok = True
            outer.append(((x[0], (x[1] + 2) % 4), (y[0], (y[1] + 2) % 4)))
        if not ok: return None
        for a, b in outer:
            for s in (a, b):
                if self.conn[s][0] in C: return None
        return outer
    def apply_R3(self, face):
        outer = self.r3_data(face)
        if outer is None: return False
        part = [(self.conn[a], self.conn[b]) for a, b in outer]
        for (a, b), (pa, pb) in zip(outer, part):
            self.link(a, pb); self.link(b, pa)
        self.log.append(('R3', tuple(tuple(map(tuple, f)) for f in face)))
        return True
    def simplify(self, rnd, budget=200):
        """R1/R2 removals, then random R3 moves (each followed by R1/R2) while crossings remain; returns best PD found"""
        self.simplify_R12()
        best = self.copy()
        for _ in range(budget):
            if self.n() == 0: break
            tris = [f for f in self.triangles() if self.r3_data(f) is not None]
            if not tris: break
            self.apply_R3(rnd.choice(tris))
            self.simplify_R12()
            if self.n() < best.n(): best = self.copy()
        return best
# ---------------- Kauffman bracket by state sum (testing only, n <= ~16) ----------------
def bracket_statesum(pd):
    cs = pd.crossings(); n = len(cs)
    if n == 0: return {0: 1}
    idx = {}
    for c in cs:
        for s in range(4): idx[(c, s)] = len(idx)
    tot = {}
    for st in range(1 << n):
        par = list(range(len(idx)))
        def f(a):
            while par[a] != a:
                par[a] = par[par[a]]; a = par[a]
            return a
        def u(a, b): par[f(a)] = f(b)
        for (a, b) in pd.conn.items(): u(idx[a], idx[b])
        na = 0
        for k, c in enumerate(cs):
            A = (st >> k) & 1
            o = pd.over[c]
            # over on {0,2}: A-smoothing pairs (1,2),(3,0); B: (0,1),(2,3).  over on {1,3}: A: (0,1),(2,3); B: (1,2),(3,0)
            if (A and o == 0) or (not A and o == 1): pairs = ((1, 2), (3, 0))
            else: pairs = ((0, 1), (2, 3))
            na += A
            for p, q in pairs: u(idx[(c, p)], idx[(c, q)])
        loops = len(set(f(i) for i in range(len(idx))))
        e = na - (n - na)
        # (-A^2 - A^-2)^(loops-1)
        poly = {e: 1}
        for _ in range(loops - 1):
            new = {}
            for k, v in poly.items():
                new[k + 2] = new.get(k + 2, 0) - v; new[k - 2] = new.get(k - 2, 0) - v
            poly = new
        for k, v in poly.items(): tot[k] = tot.get(k, 0) + v
    return {k: v for k, v in tot.items() if v}
def unit_normal(p):
    """normalise a Laurent poly up to +-A^k"""
    if not p: return ()
    lo = min(p); s = 1 if p[lo] > 0 else -1
    return tuple(sorted((k - lo, s * v) for k, v in p.items()))

def is_face(pd, face):
    """face = sequence of (x, y) slot pairs; check edges x->y exist and consecutive turn rule y -> (y[0], y[1]-1) = next x"""
    for i, (x, y) in enumerate(face):
        if pd.conn.get(tuple(x)) != tuple(y): return False
        nx = face[(i + 1) % len(face)][0]
        if (y[0], (y[1] - 1) % 4) != tuple(nx): return False
    return True
def replay(word, log):
    """rebuild the PD of the halfword and re-apply every logged move with its validity check; returns final crossing count"""
    q = PD.from_halfword(word)
    for mv in log:
        if mv[0] == 'R1':
            c, s = mv[1], mv[2]; assert q.check_R1(c, s), ('R1 invalid', mv); q.remove([c])
        elif mv[0] == 'R2':
            c1, s, c2, t = mv[1:]; assert q.check_R2(c1, s, c2, t), ('R2 invalid', mv); q.remove([c1, c2])
        elif mv[0] == 'R3':
            face = [tuple(map(tuple, f)) for f in mv[1]]
            assert is_face(q, face) and len(face) == 3, ('R3 not a triangle face', mv)
            assert q.r3_data(face) is not None, ('R3 invalid', mv)
            n0 = len(q.log); q.apply_R3(face)
        else: raise ValueError(mv)
    return q.n()
