import sys,os,glob,pickle; sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mech/sum/scripts')
from chains import *
from load import *
O=R+'lit/kht/out/'
def bnfile(d):
    fs=glob.glob(os.path.join(d,'cxBNr-c2-q*'))
    return fs[0] if fs else None
# factors
F={}
for d in glob.glob(O+'k138/examples/si/*/'):
    name=os.path.basename(d.rstrip('/')); f=bnfile(d)
    if f: F[name.replace('-','i')]=dots(read_file(f))
print(len(F),sorted(F)[:8])
def mirror(G): return Counter({(-h,-q):m for (h,q),m in G.items()})
def mult(G1,G2):
    G=Counter()
    for (h1,q1),m1 in G1.items():
        for (h2,q2),m2 in G2.items(): G[(h1+h2,q1+q2)]+=m1*m2
    return G
names=sorted(F,key=len,reverse=True)
def split(name):
    for a in names:
        for am in ('m',''):
            pre=a+am+'_'
            if name.startswith(pre):
                rest=name[len(pre):]
                for bm in ('m',''):
                    b=rest[:len(rest)-len(bm)] if bm else rest
                    if rest.endswith(bm) and b in F: return (a,am,b,bm)
ok=bad=0
for d in sorted(glob.glob(O+'comp/examples/comp/*/')):
    name=os.path.basename(d.rstrip('/')); f=bnfile(d)
    if not f: continue
    s=split(name)
    if not s: print('nosplit',name); continue
    a,am,b,bm=s
    G1=mirror(F[a]) if am else F[a]; G2=mirror(F[b]) if bm else F[b]
    G=dots(read_file(f)); P=mult(G1,G2)
    if G==P: ok+=1
    else:
        # try uniform shift
        sh=None
        if sum(G.values())==sum(P.values()):
            g=sorted(G.elements()); p=sorted(P.elements())
            cand=(g[0][0]-p[0][0],g[0][1]-p[0][1])
            if Counter({(h+cand[0],q+cand[1]):m for (h,q),m in P.items()})==G: sh=cand
        bad+=1; print('MISMATCH',name,'n',sum(G.values()),sum(P.values()),'uniform shift' ,sh)
print('BN-level multiplicativity of the bigraded •-count: ok',ok,'bad',bad)
