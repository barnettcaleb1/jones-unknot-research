"""Exact Z[A,A^-1] TL cell representation evaluations, no interpolation.

State basis: noncrossing partial pairings, with no defect inside a cup.
Generators sigma_i=A I+A^-1 e_i; delta=-A^2-A^-2.
W(n,k) has k defects and shape((n+k)/2,(n-k)/2).
Matrix products read written braidwords left-to-right, applying rightmost
letter to column vectors first. Kernel comparisons unaffected by scalar
normalization as all supplied words have exponent sum zero.
"""
import sys,pathlib,json,time
from collections import defaultdict
HERE=pathlib.Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'pass2'))
import braid_kernel as bk
sys.path.insert(0,str(HERE.parent/'pass4'))
from braid_ren_cable import basis,transition,verify_relations
from kernel_words import WORDS,inv

def addto(out,p,shift=0,scale=1):
    for e,c in p.items():out[e+shift]+=scale*c

def clean(p):return {e:c for e,c in sorted(p.items()) if c}
def identity(d):return [[{0:1} if i==j else {} for j in range(d)] for i in range(d)]
def rho(word,n,k):
    states=basis(n,(n-k)//2);d=len(states);ix={s:i for i,s in enumerate(states)}
    trans=[[transition(s,i) for s in states] for i in range(n-1)]
    m=identity(d)
    for g in reversed(word):
        sign=1 if g>0 else -1;out=[[defaultdict(int) for _ in range(d)] for _ in range(d)]
        for j,(dest,loop) in enumerate(trans[abs(g)-1]):
            for col in range(d):
                p=m[j][col];addto(out[j][col],p,sign)
                if dest is None:continue
                row=ix[dest]
                if loop:
                    addto(out[row][col],p,2-sign,-1);addto(out[row][col],p,-2-sign,-1)
                else:addto(out[row][col],p,-sign)
        m=[[clean(p) for p in row] for row in out]
    return states,m

def defect(m):
    out=[]
    for i,row in enumerate(m):
        for j,p in enumerate(row):
            q=defaultdict(int,p)
            if i==j:q[0]-=1
            q=clean(q)
            if q:out.append((i,j,q))
    return out

def specialize(p,A=2,prime=1000003):
    return sum(c*pow(A,e,prime) for e,c in p.items())%prime

def run():
    started=time.monotonic();out={'conventions':__doc__,'prime':1000003,'A':2,'results':[]}
    # Direct checks relevant to implemented cell action.
    for n,k in [(5,1),(6,4),(6,2),(6,0)]:
        verify_relations(n,(n-k)//2)
        assert not defect(rho([1,-1],n,k)[1])
        assert rho([1,2,1],n,k)[1]==rho([2,1,2],n,k)[1]
    for label,(n,w) in WORDS.items():
        assert sum(1 if s>0 else -1 for s in w)==0
        burau=bk.burau(w,n)
        assert bk.identity(burau),(label,'Burau not identity')
        blocks=[1] if n==5 else [4,2,0]
        for k in blocks:
            states,m=rho(w,n,k);diff=defect(m)
            # Smallest support exact witness, plus nonzero finite-field value.
            witness=min(diff,key=lambda x:len(x[2])) if diff else None
            finite=next(((i,j,specialize(p)) for i,j,p in diff if specialize(p)),None)
            rec={'label':label,'n':n,'k':k,'shape':[(n+k)//2,(n-k)//2],'dimension':len(states),'word':w,'length':len(w),'burau_exact_identity':True,'exact_identity':not diff,'nonzero_difference_entries':len(diff),'basis':states,'exact_witness':witness,'finite_witness':finite,'matrix':m}
            out['results'].append(rec)
            print(json.dumps({key:rec[key] for key in ['label','n','k','dimension','length','exact_identity','nonzero_difference_entries','finite_witness']}),flush=True)
    out['seconds']=time.monotonic()-started
    (HERE/'kernel_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print('seconds',out['seconds'])
if __name__=='__main__':run()
