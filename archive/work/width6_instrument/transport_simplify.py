"""Conservative exact joint PL isotopy by empty-triangle vertex deletion.

Each deleted triangle is disjoint from punctures and every other source edge,
except permitted common endpoints at the two retained vertices. A rational
spatial hash is only a broad phase; all geometric decisions use Fractions.
"""
from fractions import Fraction as F
from collections import defaultdict, deque
import time
from transport_pl import sub,cross,point,braid_curve,encode


def orient(a,b,c): return cross(sub(b,a),sub(c,a))
def box(points):
    return min(p[0]for p in points),max(p[0]for p in points),min(p[1]for p in points),max(p[1]for p in points)
def meets_box(x,y):return not(x[1]<y[0]or y[1]<x[0]or x[3]<y[2]or y[3]<x[2])
def within(p,a,b):return orient(a,b,p)==0 and min(a[0],b[0])<=p[0]<=max(a[0],b[0])and min(a[1],b[1])<=p[1]<=max(a[1],b[1])
def inside(p,a,b,c):
    s=[orient(a,b,p),orient(b,c,p),orient(c,a,p)]
    return min(s)>=0 or max(s)<=0

def forbidden_intersection(a,b,c,d,allowed):
    """Closed segments intersect anywhere beyond an allowed shared endpoint."""
    u=sub(b,a);v=sub(d,c);w=sub(c,a);det=cross(u,v)
    if det:
        t=cross(w,v)/det;s=cross(w,u)/det
        if not(0<=t<=1 and 0<=s<=1):return False
        p=(a[0]+t*u[0],a[1]+t*u[1])
        return not(p in allowed and p in(a,b)and p in(c,d))
    if cross(w,u):return False
    # A positive-length collinear overlap always contains forbidden points.
    common={p for p in(a,b,c,d)if within(p,a,b)and within(p,c,d)}
    if len(common)>1:return True
    if not common:return False
    p=next(iter(common))
    return not(p in allowed and p in(a,b)and p in(c,d))

class Grid:
    def __init__(self,scale=4):self.scale=scale;self.cells=defaultdict(set);self.entries={}
    def keys(self,b):
        # Fraction floor is exact, so a cell cannot be missed by rounding.
        x0,x1,y0,y1=(int(v*self.scale//1)for v in b)
        return [(x,y)for x in range(x0,x1+1)for y in range(y0,y1+1)]
    def add(self,key,a,b):
        bb=box((a,b));cells=self.keys(bb);self.entries[key]=(a,b,bb,cells)
        for c in cells:self.cells[c].add(key)
    def remove(self,key):
        for c in self.entries[key][3]:self.cells[c].remove(key)
        del self.entries[key]
    def query(self,bb):
        ans=set()
        for c in self.keys(bb):ans.update(self.cells.get(c,()))
        return [k for k in ans if meets_box(bb,self.entries[k][2])]

def simplify_joint(curves,punctures=None,max_seconds=30,max_checks=1000000,certificate=False):
    """Return isotopic curves and a certificate summary. Source curves must be embedded/disjoint."""
    if punctures is None:punctures=[point(j)for j in range(1,7)]
    start=time.monotonic();grid=Grid();vertices={};prev={};nxt={};queue=deque()
    for ci,curve in enumerate(curves):
        for k,p in enumerate(curve):
            key=(ci,k);vertices[key]=p;prev[key]=(ci,k-1)if k else None
            nxt[key]=(ci,k+1)if k+1<len(curve)else None
            if k+1<len(curve):grid.add(key,p,curve[k+1])
            if 0<k<len(curve)-1:queue.append(key)
    deleted=[];sweeps=[];checks=0;attempts=0;stopped=None
    while queue:
        if time.monotonic()-start>max_seconds:stopped='time';break
        if checks>max_checks:stopped='check_budget';break
        mid=queue.popleft()
        if mid not in vertices:continue
        left,right=prev[mid],nxt[mid]
        if left is None or right is None:continue
        a,b,c=vertices[left],vertices[mid],vertices[right];attempts+=1
        ar=orient(a,b,c)
        if not ar:
            if not within(b,a,c):continue
        else:
            if any(p not in(a,c)and inside(p,a,b,c)for p in punctures):continue
        bb=box((a,b,c));safe=True
        for key in grid.query(bb):
            if key in(left,mid):continue
            d,e,_,_=grid.entries[key];checks+=1
            if ar and any(p not in(a,c)and inside(p,a,b,c)for p in(d,e)):
                safe=False;break
            if any(forbidden_intersection(x,y,d,e,{a,c})for x,y in((a,b),(b,c),(c,a))):
                safe=False;break
        if not safe:continue
        grid.remove(left);grid.remove(mid);grid.add(left,a,c)
        nxt[left]=right;prev[right]=left;del vertices[mid]
        deleted.append((mid,left,right));queue.extend((left,right))
        if certificate:sweeps.append({"curve":mid[0],"vertex":mid[1],"retained_indices":[left[1],right[1]],"triangle":encode([a,b,c])})
    out=[]
    for ci in range(len(curves)):
        key=(ci,0);curve=[]
        while key is not None:curve.append(vertices[key]);key=nxt[key]
        out.append(curve)
    return out,{'input_vertices':[len(c)for c in curves],'output_vertices':[len(c)for c in out],
         'deletions':len(deleted),'attempts':attempts,'edge_checks':checks,
         'seconds':round(time.monotonic()-start,3),'stopped':stopped,
         'method':'exact empty swept triangles; all punctures and both source curves checked',
         **({'swept_triangles':sweeps,'before_curves':[encode(c)for c in curves],'after_curves':[encode(c)for c in out]}if certificate else{})}


def braid_curves(curves,word,limit=15000,simplify_seconds=15,certificate=False):
    history=[]
    for k,g in enumerate(word):
        curves=[braid_curve(c,[g],limit=max(limit*8,200000))for c in curves]
        curves,stats=simplify_joint(curves,max_seconds=simplify_seconds,certificate=certificate)
        stats.update({'prefix':k+1,'generator':g});history.append(stats)
        print('SIMPLIFIED_PREFIX',k+1,g,{key:value for key,value in stats.items()if key not in('swept_triangles','before_curves','after_curves')},flush=True)
        if max(map(len,curves))>limit:raise RuntimeError(f'Simplified vertex limit {limit} exceeded at prefix {k+1}')
    return curves,history

if __name__=='__main__':
    import json
    from pathlib import Path
    raw=json.loads(Path(__file__).with_name('transport_pl.json').read_text())
    curves=[[(F(x),F(y))for x,y in c]for c in raw['curves']]
    out,stats=simplify_joint(curves,max_seconds=30)
    result={'curves':[encode(c)for c in out],'stats':stats}
    Path(__file__).with_name('transport_simplify_14.json').write_text(json.dumps(result)+'\n')
    print(stats)
