"""Build depth-3 frontier boxes and their jets.  argv: tag"""
import sys, pickle, time, collections
sys.path.insert(0,'.')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import vc, lib, front
tag=sys.argv[1]
t0=time.time()
R4=lib.rational(4)
U=[None]+R4
MS=(1,-1,2,-2,3,-3); NS=range(-2,3)
def grow(seeds,label):
    out=[]; seen=set()
    for s in seeds:
        for u in U:
            for m in MS:
                for N in NS:
                    b=lib.node(m,N,[s] if u is None else [s,u])
                    if b is None or b[0] in seen: continue
                    seen.add(b[0]); out.append(b)
    print(label,len(out),round(time.time()-t0,1),flush=True)
    return out
def generic(j):
    tp,bt=j
    return tp[0]-bt[0]==-1 and tp[2][0]+bt[2][0]==0 and tp[2][1]+bt[2][1]==-1
if tag=='d2pos':
    seeds=pickle.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA/d2pos_boxes.pkl','rb'))
    D3=grow(seeds,'depth3 around d2pos')
elif tag=='g43':
    G=lib.general(); g43=[g for g in G if ('g',43) in (g[2],) + tuple(g[2][1] if g[2][0]=='p' else ())]
    assert len(g43)==1
    D1=grow(g43,'depth1 around g43')
    D2=grow(D1,'depth2 around g43')
    J2=[front.jt(b[1]) for b in D2]
    ng=[b for b,j in zip(D2,J2) if not generic(j)]
    print('depth2 g43 non-generic',len(ng),flush=True)
    D3=D1+D2+grow(ng[:600],'depth3 around non-generic depth2 g43')
JJ=[front.jt(b[1]) for b in D3]
pickle.dump(dict(boxes=[(b[0],b[2],b[3]) for b in D3],vecs=[b[1] for b in D3],jets=JJ),open('fr_%s.pkl'%tag,'wb'))
C=collections.Counter((j[0][0]-j[1][0], j[0][2][0]+j[1][2][0], j[0][2][1]+j[1][2][1]) for j in JJ)
print('generic fraction',sum(1 for j in JJ if generic(j))/len(JJ))
print('top (delta,sigma,tau) classes',C.most_common(12))
print('done',round(time.time()-t0,1))
