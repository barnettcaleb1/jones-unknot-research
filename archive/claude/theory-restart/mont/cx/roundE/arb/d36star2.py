"""D36* with at least TWO factors in total (sum k + n >= 2): re-run only the 14 cases open in d36star.py (all others are closed
already for every multiset with sum k >= 1)."""
import sys, pickle, collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/arb')
import d36star, lpg, runner
from fractions import Fraction as Fr
R=pickle.load(open('d36star.pkl','rb'))
opn=[r[0] for r in R if r[1]!='closed']
orig=lpg.build
def build2(*a,**kw):
    L=orig(*a,**kw)
    L.add_ub({**{j:Fr(-1) for j in range(L.nk)},L.iN:Fr(-1)},-2)
    return L
lpg.build=build2
out=[d36star.one(j) for j in opn]
for r in out: print(r[0],r[1],str(r[2])[:200])
print('two-factor re-run of the',len(opn),'open cases:',dict(collections.Counter(r[1] for r in out)))
pickle.dump(out,open('d36star2.pkl','wb'))
