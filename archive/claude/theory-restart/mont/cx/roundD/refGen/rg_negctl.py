"""Planted negative control.  Genuine units: closures of ONE rational box u0 (two-bridge unknots).  Treat u0 as the box B
(n_min = 0, i.e. the configuration B alone is allowed).  Soundness demands:
  (a) both generators (ours, C1's gen2) leave the closure class of every unit OPEN;
  (b) at a unit with exactly one strong end (r >= 2), the weak end's case equations (ours) hold with zero rational sums,
      i.e. the unit satisfies the equations of its own case (so no certificate can exist for it).
Units searched exhaustively over normal forms of size <= 10, mu in [-8,8]\\0 (horizontal), a in {+-1,+-3,+-5,+-7} (vertical),
N at the Lemma-W degree ties."""
import sys, os, collections
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refGen')
import rg_core as C, rg_gen as G
from fractions import Fraction as Fr
RG = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refGen/'
C1 = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC1'
G.load_gtab(RG + 'rg_gtab.pkl')
sys.path.insert(1, C1); sys.path.insert(2, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
cwd = os.getcwd(); os.chdir(C1)
import gen2
os.chdir(cwd)
PHI3 = {0: 1, 1: 1, 2: 1}
def is_unit_phi3(F):
    if len(F) != 3: return False
    d = min(F); c = F[d]
    return abs(c) == 1 and F.get(d + 1) == c and F.get(d + 2) == c
def hcls(mu): return 'mu=%d' % mu if abs(mu) <= 3 else ('mu>=4' if mu > 0 else 'mu<=-4')
def vcls(a): return 'a=%d' % a if abs(a) == 3 else ('a>=5' if a > 0 else 'a<=-5')
units = []
for seq in C.normal_forms_size(10):
    a, b = C.chans(C.box(seq))
    for fam, pars in (('H', [m for m in range(-8, 9) if m]), ('V', [-7, -5, -3, -1, 1, 3, 5, 7])):
        for par in pars:
            w1 = G.w1(par); w2 = G.w3(par) if fam == 'H' else G.wV(par)
            Ns = set()
            for x in (max(w2) + max(b) - max(w1) - max(a), min(w2) + min(b) - min(w1) - min(a)):
                if x % 3 == 0: Ns.add(x // 3)
            for N in Ns:
                S1 = C.pmul(w1, a); S2 = C.pmul(w2, C.pshift(b, -3 * N))
                F = C.padd(S1, S2)
                if is_unit_phi3(F): units.append((seq, fam, par, N, S1, S2))
print('units found (single rational box closures):', len(units), collections.Counter((u[1], u[2]) for u in units))
stat = collections.Counter(); bad = []
for seq, fam, par, N, S1, S2 in units:
    a, b = C.chans(C.box(seq))
    Bd, sg, dl, lcok, spa = G.bdata_from_vec(a, b)
    if fam == 'V' and abs(par) == 1:
        continue     # a = +-1 is the horizontal mu = +-1 closure (covered by the H entries)
    cls = hcls(par) if fam == 'H' else vcls(par)
    # (a) generators must leave the class open (n_min = 0)
    mine = G.prove(Bd, sg, dl, 0, which=(fam,))
    stat['mine open'] += bool(mine[(fam, cls)])
    if not mine[(fam, cls)]: bad.append(('MINE PROVED A UNIT', seq, fam, par, N))
    if fam == 'H':
        c1 = gen2.proveH(Bd, sg, dl, 0)
        mu4 = par if abs(par) <= 3 else (4 if par > 0 else -4)
        stat['C1 open'] += bool(c1[mu4])
        if not c1[mu4]: bad.append(('C1 PROVED A UNIT', seq, fam, par, N))
    else:
        c1 = gen2.proveV(Bd, sg, dl, 0)
        stat['C1 open'] += (not c1[0])
        if c1[0]: bad.append(('C1 PROVED A UNIT', seq, fam, par, N))
    # (b) strong/weak structure and the weak-end case equations with zero rational sums
    rr = {}
    for end in ('top', 'bot'):
        d1, c1_, x1 = C.enddata(S1, end, 4); d2, c2_, x2 = C.enddata(S2, end, 4)
        off = (d1 - d2) if end == 'top' else (d2 - d1)
        if off != 0 or c1_ + c2_ != 0: rr[end] = (0, off, Fr(c2_, c1_)); continue
        r = 1
        while r <= 4 and x1[r - 1] == x2[r - 1]: r += 1
        rr[end] = (r, off, Fr(c2_, c1_))
    strong = [e for e in rr if rr[e][0] >= 2]
    if len(strong) != 1:
        stat['two strong ends (mB=0 type)' if len(strong) == 2 else 'no strong end'] += 1
        continue
    weak = 'bot' if strong[0] == 'top' else 'top'
    r, off, eps = rr[weak]
    o, sgs, rule = (G.HCL if fam == 'H' else G.VCL)[cls]
    mB = sg - sgs
    pw, qw = o[weak]
    if off >= 3: nm = 'off>=3'
    elif off <= -3: nm = 'off<=-3'
    elif off == 0: nm = 'off=0 e=+1' if eps == 1 else 'off=0 e=-1 r=1'
    else: nm = 'off=%d e=%+d' % (off, eps)
    rows = [rw for (cn, rw, o0) in G.cases(pw, qw, Bd[weak], mB) if cn == nm]
    if not rows:
        bad.append(('case missing', seq, fam, par, nm)); continue
    ok = all(rw[4] == 0 for rw in rows[0])   # zero sums: every row must have rhs 0
    stat['weak-end equations hold at the unit' if ok else 'EQUATIONS VIOLATED'] += 1
    if not ok: bad.append(('eq violated', seq, fam, par, N, nm, rows[0]))
print(dict(stat))
print('problems:', bad[:10] if bad else 'none')
