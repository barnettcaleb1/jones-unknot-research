from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'braid_classification/packages'))
import regina
from spherogram.links.tangles import Tangle,Strand,RationalTangle,BraidTangle

def endcap(t,top):
    u=t.reshape((4,0) if top else (0,4)).copy()
    outer=Strand('outer')
    return Tangle((6,0) if top else (0,6),u.crossings+[outer],[(outer,0)]+u.adjacent+[(outer,1)])
def watson(alpha,t,u):
    beta=list(alpha)+[-(6-abs(i))*(1 if i>0 else -1) for i in alpha]
    return (endcap(t,True)*BraidTangle(beta,6)*endcap(u,False)).link()
def report(alpha,n):
    l=watson(alpha,RationalTangle(n),RationalTangle(-n))
    r=regina.Link.fromPD([[x+1 for x in row] for row in l.PD_code()])
    c=r.countComponents();cross=r.size();j=str(r.jones());r.simplify()
    print(alpha,n,'components',c,'crossings',cross,'Jones',j,'simplified',r.size(),flush=True)
    return j,c,r.size()
if __name__=='__main__':
    for alpha in ([1],[1,1,-2,1],[1,1,1,-2,1]):
        for n in [-2,-1,0,1,2]:report(alpha,n)
