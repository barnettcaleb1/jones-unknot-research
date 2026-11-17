"""Structured centralizer and trace search for Bigelow kernel conjugates."""
import sys,pathlib,itertools,json,time
ROOT=pathlib.Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent/'pass2'))
import braid_kernel as bk
import tl5_block as tl

P=1000003
def mm(a,b,p=P):
    return tuple(tuple(sum(x*y for x,y in zip(row,col))%p for col in zip(*b)) for row in a)
I=tuple(tuple(int(i==j) for j in range(5)) for i in range(5))
def evaluate(m,a=2,p=P):
    return tuple(tuple(sum(c*pow(a,e,p) for e,c in q.items())%p for q in row) for row in m)
def traceprod(a,b,p=P):return sum(a[i][j]*b[j][i] for i in range(5) for j in range(5))%p
GEN={i:evaluate(tl.rho([i])) for i in [1,2,3,4,-1,-2,-3,-4]}
def rho(w):
    m=I
    for s in w:m=mm(m,GEN[s])
    return m
def key(m):return tuple(v for row in m for v in row)
def comm(a,b,ai,bi):return mm(mm(mm(a,b),ai),bi)
def artin(word):
    """Faithful braid action on the free group, represented by reduced words."""
    state=[[i] for i in range(1,6)]
    for s in word:
        i=abs(s)-1;a,b=state[i],state[i+1]
        if s>0:state[i],state[i+1]=bk.reduce(a+b+bk.inv(a)),a
        else:state[i],state[i+1]=b,bk.reduce(bk.inv(b)+a+b)
    return state

def words(maxlen):
    yield [],I,I
    layer=[([],I,I)]
    for n in range(maxlen):
        new=[]
        for w,m,mi in layer:
            for s in GEN:
                if w and w[-1]==-s:continue
                item=(w+[s],mm(m,GEN[s]),mm(GEN[-s],mi))
                new.append(item);yield item
        layer=new

def run(maxlen=4):
    started=time.monotonic()
    K=evaluate(tl.rho(bk.KERNEL));Ki=evaluate(tl.rho(bk.inv(bk.KERNEL)))
    assert mm(K,Ki)==I
    anchors=[[s*i for s,i in zip(signs,range(1,5))] for signs in itertools.product((-1,1),repeat=4)]
    AM=[rho(w) for w in anchors]
    targets=[traceprod(I,a) for a in AM]
    seen={};eligible=set();central=[];conjcentral=[];tracehits=[];tested=0
    equivalence_checks=0;unresolved_duplicates=[];total_words=0
    for g,G,Gi in words(maxlen):
        total_words+=1;kg=key(G)
        if kg in seen:
            if kg in eligible:
                equivalence_checks+=1
                if artin(g+bk.inv(seen[kg]))!=[[i] for i in range(1,6)]:
                    unresolved_duplicates.append(dict(g=g,representative=seen[kg]))
            continue
        seen[kg]=g;tested+=1
        Kg=mm(mm(Gi,K),G);Kgi=mm(mm(Gi,Ki),G)
        if mm(K,G)==mm(G,K):central.append(g);eligible.add(kg)
        if mm(K,Kg)==mm(Kg,K):conjcentral.append(g);eligible.add(kg)
        for kind,C in [('K_g',comm(K,G,Ki,Gi)),('K_Kg',comm(K,Kg,Ki,Kgi))]:
            for anchor,A,target in zip(anchors,AM,targets):
                if traceprod(C,A)==target:
                    tracehits.append(dict(kind=kind,g=g,anchor=anchor,matrix_identity=C==I))
                    eligible.add(kg)
    report=dict(maxlen=maxlen,modulus=P,A=2,distinct_g=tested,centralizers=central,
                conjugate_centralizers=conjcentral,trace_hits=tracehits,
                total_words=total_words,equivalence_checks=equivalence_checks,
                unresolved_duplicates=unresolved_duplicates,
                seconds=time.monotonic()-started)
    (ROOT/'braid_conjugate_filter.json').write_text(json.dumps(report,indent=2))
    print({k:(len(v) if isinstance(v,list) else v) for k,v in report.items()},flush=True)
    return report

if __name__=='__main__':run(int(sys.argv[1]) if len(sys.argv)>1 else 4)
