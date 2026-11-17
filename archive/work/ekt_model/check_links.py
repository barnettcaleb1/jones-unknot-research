"""Independent diagram construction and integral Fox presentation for EKT links."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'braid_classification/packages'))
import regina
from spherogram.links.tangles import IdentityBraid, BraidTangle, RationalTangle

def hopf(t,u,rotation=1):
    c=BraidTangle([-2,-3,-1,-2]*2,4)
    return ((IdentityBraid(2)|t.rotate(rotation))*c*(u.rotate(rotation)|IdentityBraid(2))).braid_closure()

def fox_factors(pd):
    # Each tuple is cyclic, with opposite understrands a,c and overstrands b,d.
    # Fix arc0 to color0 to remove the universal free constant coloring.
    n=2*len(pd)
    matrix=regina.MatrixInt(n,n-1)
    for i,(a,b,c,d) in enumerate(pd):
        for arc,co in ((b,1),(d,-1)):
            if arc:matrix.set(2*i,arc-1,matrix.entry(2*i,arc-1)+co)
        for arc,co in ((a,1),(c,1),(b,-2)):
            if arc:matrix.set(2*i+1,arc-1,matrix.entry(2*i+1,arc-1)+co)
    regina.smithNormalForm(matrix)
    ds=[abs(int(str(matrix.entry(i,i)))) for i in range(n-1)]
    return [d for d in ds if d>1], ds.count(0)

def report(n,p,q,rotation):
    link=hopf(RationalTangle(p,q),RationalTangle(-p,q),rotation)
    pd=link.PD_code()
    r=regina.Link.fromPD([[x+1 for x in row] for row in pd])
    print(n,p,q,'rotation',rotation,'crossings',len(pd),'components',r.countComponents(),'Jones',r.jones(),'H1',fox_factors(pd),flush=True)
    return link

if __name__=='__main__':
    for rot in [1,-1]:report(1,3,1,rot)
    p,q=1,0
    for n in range(1,5):
        p,q=3*p+8*q,p+3*q
        report(n,p,q,1)
