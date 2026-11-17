"""gen_kernel.py -- Lemma K (cert/run REPORT section 5, PROVED) for a GENERAL symmetric full picture: N = 2*hw positions,
arbitrary non-crossing cap pairs (top) / cup pairs (bottom).  Same mathematics and same conventions as the audited
code/tangle_kernel.py (Artin action s_j: a_j -> a_j a_{j+1} a_j^-1, a_{j+1} -> a_j; psi_C(a_p) = c, psi_C(a_q) = c^-1;
T1 = T2 rel boundary iff psi_T2 kills curves(T1) and psi_T1 kills curves(T2)); only N, the pairs and the letter map are
parameters.  Letter map from alex.symmetrize: x0 -> s_(hw-1); x_s -> s_(hw+s-1), s_(hw-s-1)  (s >= 1).
Validated in kernel_validate.py: identical answers to code/tangle_kernel.py in its own (N = 10) setting, and the known
(non-)stabilisers of the s.l2 caps / u1+u0 cups."""
def red(w):
    out = []
    for a in w:
        if out and out[-1] == -a: out.pop()
        else: out.append(a)
    return tuple(out)
def inv(w): return tuple(-a for a in reversed(w))
def sigma(j, sign):
    a, b = j + 1, j + 2
    if sign > 0: return {j: (a, b, -a), j + 1: (a,)}
    return {j: (b,), j + 1: (-b, a, b)}
def apply_aut(images, w):
    out = []
    for s in w:
        k = abs(s) - 1
        if k in images:
            img = images[k]; out.extend(img if s > 0 else inv(img))
        else: out.append(s)
    return red(out)
class Picture:
    def __init__(self, hw, top_pairs, bot_pairs):
        self.hw = hw; self.N = 2 * hw; self.TOP = top_pairs; self.BOT = bot_pairs
    def sigmas(self, L):
        c, s = L[0], int(L[1:]); sg = 1 if c == 'x' else -1; hw = self.hw
        if s == 0: return [(hw - 1, sg)]
        assert 1 <= s <= hw - 1
        return [(hw - s - 1, sg), (hw + s - 1, sg)]       # the two sigmas commute
    def act(self, L, w):
        for j, sg in self.sigmas(L): w = apply_aut(sigma(j, sg), w)
        return w
    def act_inv(self, L, w):
        return self.act(('y' if L[0] == 'x' else 'x') + L[1:], w)
    @staticmethod
    def psi_C(pairs):
        m = {}
        for k, (p, q) in enumerate(pairs): m[p] = (k + 1,); m[q] = (-(k + 1),)
        return m
    @staticmethod
    def psi_apply(m, w, free_sym=100):
        out = []
        for s in w:
            k = abs(s) - 1; img = m.get(k, (free_sym + k,)); out.extend(img if s > 0 else inv(img))
        return red(out)
    @staticmethod
    def base(pairs): return [(p + 1, q + 1) for p, q in pairs]
    # TOP tangle of V = L_1..L_k (caps above L_1)
    def top_curves(self, V):
        cs = self.base(self.TOP)
        for L in V: cs = [self.act(L, c) for c in cs]
        return cs
    def top_kills(self, V, curves):
        m = self.psi_C(self.TOP)
        for c in curves:
            w = c
            for L in reversed(V): w = self.act_inv(L, w)
            if self.psi_apply(m, w): return False
        return True
    def same_top(self, V1, V2):
        return self.top_kills(V2, self.top_curves(V1)) and self.top_kills(V1, self.top_curves(V2))
    # BOTTOM tangle of U = L_1..L_k (cups below L_k)
    def bottom_curves(self, U):
        cs = self.base(self.BOT)
        for L in reversed(U): cs = [self.act_inv(L, c) for c in cs]
        return cs
    def bottom_kills(self, U, curves):
        m = self.psi_C(self.BOT)
        for c in curves:
            w = c
            for L in U: w = self.act(L, w)
            if self.psi_apply(m, w): return False
        return True
    def same_bottom(self, U1, U2):
        return self.bottom_kills(U2, self.bottom_curves(U1)) and self.bottom_kills(U1, self.bottom_curves(U2))
# the S2 picture after translation: s.l2 ... u1 (hw = 3 during the braid part); pairs derived from alex.symmetrize:
#   s.l2: caps (0,1)=(L2,L1), (2,3)=(L0,R0), (4,5)=(R1,R2);  u1 then the final u0: cups (3,4), (1,2), (0,5)
S2PIC = Picture(3, [(0, 1), (2, 3), (4, 5)], [(1, 2), (3, 4), (0, 5)])
