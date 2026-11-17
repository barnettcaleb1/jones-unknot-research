"""Recompute the saved PD Fox presentations with Regina, without Spherogram."""
import json
from pathlib import Path
import regina
ROOT=Path(__file__).resolve().parent

def fox_factors(pd):
    n=2*len(pd)
    M=regina.MatrixInt(n,n-1)
    for i,(a,b,c,d) in enumerate(pd):
        for j,v in [(b,1),(d,-1)]:
            if j:M.set(2*i,j-1,M.entry(2*i,j-1)+v)
        for j,v in [(a,1),(c,1),(b,-2)]:
            if j:M.set(2*i+1,j-1,M.entry(2*i+1,j-1)+v)
    regina.smithNormalForm(M)
    ds=[abs(int(str(M.entry(i,i)))) for i in range(n-1)]
    return [[d for d in ds if d>1],ds.count(0)]

count=0
for name in ['ll2_scan.json','ll1_scan.json','ll1_orbit.json','check_orbits.json']:
    for row in json.loads((ROOT/name).read_text()):
        if name=='ll2_scan.json':
            assert row['p']**2-8*row['q']**2==1
            D=1+12*row['q']**2
        elif name=='ll1_scan.json':D=12*4**row['m']*(3*row['n']+2)-1
        elif name=='ll1_orbit.json':
            a,b=row['a'],row['b'];A=4**row['m']*(3*row['n']+2)
            assert a*a-8*b*b==1
            D=(a+2*b)**2-4*A*(3*a+8*b)*(a+3*b)
        else:
            a,b,k=row['a'],row['b'],row['k']
            assert a*a-8*b*b==1
            D=1+12*b*(b+a*k)
        wanted=[[abs(D)] if abs(D)>1 else [],1]
        assert fox_factors(row['pd'])==row['H1']==wanted,(name,row)
        if 'jones' in row:
            L=regina.Link.fromPD([[x+1 for x in q] for q in row['pd']])
            assert str(L.jones())==row['jones']
        count+=1
print('Recomputed',count,'full-diagram Fox Smith forms; all match the formulas.')
print('Also recomputed every saved Jones polynomial in those records.')
