import sys, collections
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mech/floer/scripts')
from knots import DET_SIG, floer, arf
from load import load138
T = load138()
c = collections.Counter(); exc = []
sharp = []
for r in T:
    kn = r['knot']; k = r['k']; j = r['j']; N = len(r['specials']); D = 4*N
    det, sig = DET_SIG[kn]
    m, Dp, typ = floer(kn)
    okp = D - Dp >= abs(k - m); okm = D - Dp >= abs(k + m)
    c['rank ineq holds for >=1 chirality'] += (okp or okm)
    c['rank ineq holds for sign(m)=sign(k) (or km=0)'] += (D - Dp >= abs(abs(k) - m)) if k != 0 else okp
    c['parity D-D-(k-m) even'] += ((D - Dp - (k - m)) % 2 == 0)
    c['j = Arf mod 2'] += ((j - arf(kn)) % 2 == 0)
    c['N == (det-1)/2'] += (N == (det-1)//2)
    c['|k| == 2|sigma|'] += (abs(k) == 2*sig)
    c['4 | k'] += (k % 4 == 0)
    slack = D - Dp - abs(abs(k) - m)
    if slack == 0: sharp.append(r['name'])
    if N != (det-1)//2 or abs(k) != 2*sig:
        exc.append((r['name'], 'k', k, 'j', j, 'N', N, 'det', det, '|sig|', sig, 'm', m, "D'", Dp, typ, 'D-Dp', D-Dp))
for kk, v in c.items(): print(f'{kk}: {v}/{len(T)}')
print('rank inequality sharp (D - D\' = ||k| - m|):', sharp)
print('exceptions to N=(det-1)/2 or |k|=2|sigma|:')
for e in exc: print('  ', *e)
