"""Exact rational PL half twists, split at every affine-cell boundary.

A positive geometric generator is a counterclockwise half twist. Mapping
to matrix generator signs is calibrated separately. No sampled chords are
substituted for images of a segment crossing affine cells.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import time

def add(a,b): return (a[0]+b[0],a[1]+b[1])
def sub(a,b): return (a[0]-b[0],a[1]-b[1])
def scale(a,t): return (a[0]*t,a[1]*t)
def cross(a,b): return a[0]*b[1]-a[1]*b[0]
def turn(a): return (-a[1],a[0])
def unturn(a): return (a[1],-a[0])

INNER=F(3,4)
OUTER=F(5,4)
DIR=[(F(1),F(0)),(F(0),F(1)),(F(-1),F(0)),(F(0),F(-1))]
I=[scale(p,INNER)for p in DIR]
O=[scale(p,OUTER)for p in DIR]
TRIANGLES=[]
for k in range(4):
    j=(k+1)%4
    TRIANGLES.append(((I[k],O[k],O[j]),(I[j],O[k],O[j])))
    TRIANGLES.append(((I[k],O[j],I[j]),(I[j],O[j],I[(k+2)%4])))
for a,b in TRIANGLES:
    assert cross(sub(a[1],a[0]),sub(a[2],a[0]))>0
    assert cross(sub(b[1],b[0]),sub(b[2],b[0]))>0

def cells(inverse=False):
    return [(b,a)for a,b in TRIANGLES] if inverse else TRIANGLES

def edges(inverse=False):
    out=set()
    for a,b in cells(inverse):
        for i,j in [(0,1),(1,2),(2,0)]:out.add(tuple(sorted([a[i],a[j]])))
    return list(out)

def barycentric(p,tri):
    a,b,c=tri;u=sub(b,a);v=sub(c,a);w=sub(p,a)
    det=cross(u,v)
    x=cross(w,v)/det;y=cross(u,w)/det
    return 1-x-y,x,y

def quarter_point(p,inverse=False):
    r=abs(p[0])+abs(p[1])
    if r<=INNER:return unturn(p)if inverse else turn(p)
    if r>=OUTER:return p
    for src,dst in cells(inverse):
        b=barycentric(p,src)
        if min(b)>=0:
            return (sum(t*x[0]for t,x in zip(b,dst)),sum(t*x[1]for t,x in zip(b,dst)))
    raise AssertionError(('outside cells',p))

def breakpoints(a,b,inverse=False):
    u=sub(b,a);cuts={F(0),F(1)}
    for c,d in edges(inverse):
        v=sub(d,c);w=sub(c,a);det=cross(u,v)
        if det:
            t=cross(w,v)/det;s=cross(w,u)/det
            if 0<t<1 and 0<=s<=1:cuts.add(t)
        elif cross(w,u)==0:
            axis=0 if u[0] else 1
            if u[axis]:
                for p in(c,d):
                    t=(p[axis]-a[axis])/u[axis]
                    if 0<t<1:cuts.add(t)
    return sorted(cuts)

def simplify(curve):
    out=[]
    for p in curve:
        if out and p==out[-1]:continue
        while len(out)>=2 and cross(sub(out[-1],out[-2]),sub(p,out[-1]))==0:
            # Only remove a collinear point lying between its neighbors.
            u=sub(out[-1],out[-2]);v=sub(p,out[-1])
            if u[0]*v[0]+u[1]*v[1]<0:break
            out.pop()
        out.append(p)
    return out

def quarter_curve(curve,generator):
    center=(F(abs(generator))+F(1,2),F(0));inverse=generator<0
    local=[sub(p,center)for p in curve];out=[]
    for a,b in zip(local,local[1:]):
        # Convex outer diamond: if a segment's bounding box misses it, use
        # its unchanged endpoints without rational intersection arithmetic.
        if (min(a[0],b[0])>OUTER or max(a[0],b[0])<-OUTER
            or min(a[1],b[1])>OUTER or max(a[1],b[1])<-OUTER):
            points=[a,b]
        else:
            u=sub(b,a)
            points=[quarter_point(add(a,scale(u,t)),inverse)for t in breakpoints(a,b,inverse)]
        out.extend(add(p,center)for p in points[:-1])
    out.append(add(quarter_point(local[-1],inverse),center))
    return simplify(out)

def braid_curve(curve,word,limit=200000):
    for g in word:
        curve=quarter_curve(quarter_curve(curve,g),g)
        if len(curve)>limit:raise RuntimeError(f'Vertex limit {limit} exceeded')
    return curve

def point(x,y=0):return(F(x),F(y))
def encode(curve):return [[str(x),str(y)]for x,y in curve]
def complex_curve(curve):return[complex(float(x),float(y))for x,y in curve]

def controls():
    original=[point(1),point(2)]
    for g in range(1,6):
        c=braid_curve(original,[g,-g])
        assert c==original,(g,c)
    for g in range(1,5):
        # The homeomorphisms need only be isotopic under braid relations;
        # exact polygon equality is expected only for inverse controls.
        assert braid_curve([point(g),point(g+1)],[g])==[point(g+1),point(g)]
    return {'positive_triangle_orientations':True,'inverse_curve_controls':True}

if __name__=='__main__':
    print(controls())
    word=[-4,-3,-2,-1,-5,-4,-3,-2,-3,-4,-2,-3,1,2]
    curves=[[point(1),point(2)],[point(3),point(4)]]
    start=time.monotonic()
    for k,g in enumerate(word):
        curves=[braid_curve(c,[g])for c in curves]
        print(k+1,g,[len(c)for c in curves],round(time.monotonic()-start,2),flush=True)
    out={'geometric_word':word,'curves':[encode(c)for c in curves],
         'vertex_counts':[len(c)for c in curves],'seconds':time.monotonic()-start,
         'method':'exact rational PL homeomorphisms, split at every affine-cell edge'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
