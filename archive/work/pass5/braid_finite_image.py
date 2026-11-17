"""Finite-field specializations of Ren core on TL4's two-through module."""
import json,itertools
from pathlib import Path
from collections import deque

ROOT=Path(__file__).resolve().parent
DATA=json.loads((ROOT/'tangle_four_strand.json').read_text())

def compute(p,A,limit=1000000):
    delta=-(A*A+pow(A,-2,p))%p
    I=(1,0,0,0,1,0,0,0,1)
    Z=(0,)*9
    def mm(a,b):return tuple(sum(a[3*i+k]*b[3*k+j] for k in range(3))%p for i in range(3) for j in range(3))
    def add(a,b):return tuple((x+y)%p for x,y in zip(a,b))
    def scale(c,a):return tuple(c*x%p for x in a)
    states=[]
    for i in range(3):
        s=[-1]*4;s[i]=i+1;s[i+1]=i;states.append(tuple(s))
    ES=[]
    for i in range(3):
        E=[0]*9
        for col,s in enumerate(states):
            a,b=s[i:i+2]
            if a==b==-1:continue
            if a==i+1:dest=col;c=delta
            else:
                r=list(s);r[i]=i+1;r[i+1]=i
                if a==-1:r[b]=-1
                elif b==-1:r[a]=-1
                else:r[a]=b;r[b]=a
                dest=states.index(tuple(r));c=1
            E[3*dest+col]=c
        ES.append(tuple(E))
    GS=[add(I,scale(pow(A,-2,p),E)) for E in ES]
    for i in range(3):
        assert mm(ES[i],ES[i])==scale(delta,ES[i])
    for i in range(2):assert mm(mm(GS[i],GS[i+1]),GS[i])==mm(mm(GS[i+1],GS[i]),GS[i+1])
    base=DATA['identity_index'];trans=DATA['generator_transitions']
    mats={base:I};words={base:[]};todo=deque([base])
    while todo:
        b=todo.popleft()
        for i in range(3):
            dest,lp=trans[i][b]
            if not lp and dest not in mats:
                mats[dest]=mm(mats[b],ES[i]);words[dest]=words[b]+[i];todo.append(dest)
    assert len(mats)==14
    M=Z
    for b,poly in enumerate(DATA['core_Laurent_coefficients']):
        value=sum(int(c)*pow(A,int(e),p) for e,c in poly.items())%p
        M=add(M,scale(value,mats[b]))
    def trprod(g):return sum(M[3*i+j]*g[3*j+i] for i in range(3) for j in range(3))%p
    # At top channel zero, the annular z² coefficient is the two-through trace.
    direct=sum(sum(int(c)*pow(A,int(e),p) for e,c in poly.items())*pow(delta,ct,p)
               for poly,(ct,et) in zip(DATA['core_Laurent_coefficients'],DATA['annular_closure_types_contractible_essential']) if et==2)%p
    assert trprod(I)==direct,(trprod(I),direct)
    seen={I:()};todo=deque([I]);zero=[]
    while todo and len(seen)<limit:
        g=todo.popleft()
        if trprod(g)==0:zero.append(seen[g])
        for i,G in enumerate(GS):
            h=mm(g,G)
            if h not in seen:seen[h]=seen[g]+(i+1,);todo.append(h)
    return dict(p=p,A=A,delta=delta,A4=pow(A,4,p),M=M,
                image_size=len(seen),complete=not todo,zero_trace_classes=len(zero),
                first_zero_words=zero[:10],generator_orders=[next((j for j in range(1,100) if power(G,j,mm,I)==I),None) for G in GS])

def power(a,n,mm,I):
    r=I
    for _ in range(n):r=mm(r,a)
    return r

if __name__=='__main__':
    row=compute(97,4,100000)
    assert row['complete'] and row['image_size']==648
    assert row['zero_trace_classes']==108
    (ROOT/'braid_finite_image.json').write_text(json.dumps(row,indent=2))
    print(json.dumps(row),flush=True)
