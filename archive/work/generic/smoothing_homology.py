"""Exact tests of the automatic determinant-one smoothing constraints."""
from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'braid_classification/packages'))
import regina
from spherogram import Link

def fox_factors(pd):
    n=2*len(pd)
    matrix=regina.MatrixInt(n,n-1)
    for i,(a,b,c,d) in enumerate(pd):
        for arc,co in ((b,1),(d,-1)):
            if arc:matrix.set(2*i,arc-1,matrix.entry(2*i,arc-1)+co)
        for arc,co in ((a,1),(c,1),(b,-2)):
            if arc:matrix.set(2*i+1,arc-1,matrix.entry(2*i+1,arc-1)+co)
    regina.smithNormalForm(matrix)
    ds=[abs(int(str(matrix.entry(i,i)))) for i in range(n-1)]
    return [d for d in ds if d>1],ds.count(0)

def smooth(pd,cross,which):
    a,b,c,d=pd[cross]
    parent=list(range(2*len(pd)))
    def root(x):
        while parent[x]!=x:x=parent[x]
        return x
    def union(a,b):parent[root(a)]=root(b)
    for i,j in (((a,b),(c,d)) if which==0 else ((a,d),(b,c))):union(i,j)
    out=[[root(x)for x in row]for i,row in enumerate(pd)if i!=cross]
    labels=sorted(set(x for row in out for x in row))
    assert len(labels)==2*len(out), 'zero-crossing circle not handled'
    names={old:new for new,old in enumerate(labels)}
    return [[names[x]for x in row]for row in out]

def det(factors):
    torsion,free=factors
    if free:return 0
    ans=1
    for x in torsion:ans*=x
    return ans

def cyclic(factors):
    torsion,free=factors
    return (free==0 and len(torsion)<=1)or(free==1 and not torsion)

def run(name):
    pd=Link(name).PD_code()
    link=regina.Link.fromPD([[x+1 for x in row]for row in pd])
    report={'name':name,'pd':pd,'H1':fox_factors(pd),'jones':str(link.jones()),'smoothings':[]}
    assert report['H1']==([],0)
    for crossing in range(len(pd)):
        row={'crossing':crossing,'resolutions':[]}
        for which in (0,1):
            q=smooth(pd,crossing,which)
            r=regina.Link.fromPD([[x+1 for x in item]for item in q])
            f=fox_factors(q)
            row['resolutions'].append({'which':which,'H1':f,'det':det(f),'components':r.countComponents(),'pd':q})
            assert cyclic(f)
        d0,d1=[x['det']for x in row['resolutions']]
        assert abs(d0-d1)==1
        report['smoothings'].append(row)
    return report

if __name__=='__main__':
    data=[run(name)for name in ('11n42','11n34')]
    Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2))
    for row in data:
        print(row['name'],'H1',row['H1'],'Jones',row['jones'])
        for cross in row['smoothings']:
            print(' crossing',cross['crossing'],[(s['components'],s['H1'])for s in cross['resolutions']])
