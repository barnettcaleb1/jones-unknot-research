import sys,os,glob; sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mech/sum/scripts')
from chains import *
O='/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/'
files=glob.glob(O+'k138/examples/si/*/cxBNr-c2-q*')+glob.glob(O+'comp/examples/comp/*/cxBNr-c2-q*')+glob.glob(O+'tilt/examples/strong_inversions/2-bridge_knots/*/cxBNr-c2-q*')+glob.glob(O+'dbl/examples/knots/2-bridge_knots/*/cxBNr-c2-d')
print(len(files))
def segs(c):
    """list of segments between consecutive • generators: (i,j,arrowlist) ; for arcs also terminal o-runs"""
    G=c['gens']; A=c['arrows']; n=len(G)
    idx=[i for i,g in enumerate(G) if g[0]=='⬮']
    out=[]
    if not idx: return [('nodot',None,None,tuple(A))]
    if c['cyclic']:
        for t in range(len(idx)):
            i=idx[t]; j=idx[(t+1)%len(idx)]
            ar=[]; p=i
            while True:
                ar.append(A[p]); p=(p+1)%n
                if p==j: break
            out.append(('mid',i,j,tuple(ar)))
    else:
        if idx[0]>0: out.append(('head',None,idx[0],tuple(A[:idx[0]])))
        for t in range(len(idx)-1):
            i=idx[t]; j=idx[t+1]; out.append(('mid',i,j,tuple(A[i:j])))
        if idx[-1]<n-1: out.append(('tail',idx[-1],None,tuple(A[idx[-1]:])))
    return out
def classify(ar):
    dirs=set(a[0] for a in ar)
    if len(ar)==1:
        d,k,p=ar[0]; return ('%s^%d'%(k,p),d)
    if len(dirs)>1: return ('nonmonotone',0)
    d=ar[0][0]; seq=[(k,p) for _,k,p in ar]
    if d<0: seq=seq[::-1]
    m=(len(seq)-1)//2
    if len(seq)%2==1 and seq[0]==('S',1) and seq[-1]==('S',1) and all(seq[i]==('D',1) for i in range(1,len(seq),2)) and all(seq[i]==('S',2) for i in range(2,len(seq)-1,2)):
        return ('W^%d'%m,d)
    return ('other:'+' '.join('%s%d'%x for x in seq),d)
tot=Counter(); ex={}
ncomp=Counter()
for f in files:
    for c in read_file(f):
        ncomp[c['cyclic']]+=1
        for kind,i,j,ar in segs(c):
            if kind=='mid':
                key=('mid',c['cyclic'],classify(ar)[0])
            else:
                key=(kind,c['cyclic'],'len%d'%len(ar)+(' mono' if len(set(a[0] for a in ar))==1 else ' nonmono'))
            tot[key]+=1; ex.setdefault(key,f.split('/out/')[1])
print(ncomp)
for k in sorted(tot,key=str): print(k,tot[k],ex[k])
