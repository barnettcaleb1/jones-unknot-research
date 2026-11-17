import json, glob, sys
from fractions import Fraction as F
files=sys.argv[1:] if len(sys.argv)>1 else glob.glob('fast_m3_s*.json')
rs=[]
for f in files: rs+=json.load(open(f))
by={}
for r in rs: by.setdefault(r['type'],[]).append(r)
incons=[]; tab={}
for ty,rr in by.items():
    vals=set()
    for r in rr:
        m3=F(r['sym']['M3'])/36; v3=F(r['sym']['v3'])
        vals.add((m3,v3))
    if len(vals)>1: incons.append((ty,vals))
    m3,v3=next(iter(vals))
    tab[ty]=(len(rr),m3,v3,(m3-12*v3))
print('configs',len(rs),'types',len(by),'inconsistent',len(incons))
for x in incons[:10]: print('  INCONS',x)
nz=[(ty,)+v for ty,v in tab.items() if v[3]!=0]
print('types with D8 != 0:',len(nz))
for ty,n,m3,v3,d in sorted(nz,key=lambda x:x[0]):
    print('%-16s n=%3d  M3/36=%5s v3=%4s  D8=%5s  D8/8=%s'%(ty,n,m3,v3,d,d/8))
json.dump({ty:[v[0],str(v[1]),str(v[2]),str(v[3])] for ty,v in tab.items()},open('dtable3.json','w'))
