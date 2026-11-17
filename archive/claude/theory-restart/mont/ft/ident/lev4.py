import sys, json
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
import fastsym
from fractions import Fraction as F
out=fastsym.sample(int(sys.argv[1]),4,int(sys.argv[2]),minlen=8,maxlen=16)
json.dump(out,open('fast_m4_s%s.json'%sys.argv[1],'w'))
by={}
for r in out: by.setdefault(r['type'],[]).append(r)
rep=[(t,len(v)) for t,v in by.items() if len(v)>1]
inc=[t for t,v in by.items() if len({x['sym']['M4'] for x in v})>1]
print('configs',len(out),'types',len(by),'types seen >1 times',len(rep),'inconsistent M4 symbols',len(inc),inc[:5])
