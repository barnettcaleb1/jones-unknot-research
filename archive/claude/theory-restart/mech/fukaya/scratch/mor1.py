import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mech/fukaya/scratch')
from typed import *
from fractions import Fraction

def table(res):
    return ' '.join(f"q^{q}h^{h}" + (f"x{d}" if d > 1 else '') for (q, h), d in sorted(res.items()))
S = special(2); R = row(2)
print("HF(S,S), S = s4(inf) source b at (0,0):  [bidegree (q,h) of morphisms; d(delta)=q/2-h]")
r = hf(S, S, qlo=-40, qhi=20); print('  dim', sum(r.values())); print('  ', table(r))
print('  as (q, delta):', sorted((q, Fraction(q,2)-h) for (q,h),d in r.items() for _ in range(d)))
print("HF(R,R) (wrapped; window q>=-16):"); r = hf(R, R, qlo=-16, qhi=20); print('  ', table(r))
print("HF(R,S):"); r = hf(R, S, qlo=-40, qhi=20); print('  dim', sum(r.values()), table(r))
print("HF(S,R):"); r = hf(S, R, qlo=-40, qhi=20); print('  dim', sum(r.values()), table(r))
print("HF(a(0),S):"); r = hf(arc(0), S, qlo=-40, qhi=20); print('  dim', sum(r.values()), table(r))
print("HF(S,a(0)):"); r = hf(S, arc(0), qlo=-40, qhi=20); print('  dim', sum(r.values()), table(r))
for k in (-4, 4, -8, 8):
    r = hf(arc(k), S, qlo=-40, qhi=30); print(f"HF(a({k}),S): dim", sum(r.values()), table(r))
    r = hf(S, arc(k), qlo=-40, qhi=30); print(f"HF(S,a({k})): dim", sum(r.values()), table(r))
print("HF(a(inf)=[c], S):", hf(chain('ainf','c'), S, qlo=-40, qhi=20))
print("HF(a(0), a(0)) window:", table(hf(arc(0), arc(0), qlo=-8, qhi=4)))
print("HF(a(0), R) window:", table(hf(arc(0), R, qlo=-8, qhi=10)))
print("HF(a(inf), R) window:", table(hf(chain('ainf','c'), R, qlo=-8, qhi=10)))
