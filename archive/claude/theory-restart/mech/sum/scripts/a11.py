import sys,os,glob; sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mech/sum/scripts')
from chains import *
from load import load_jsonl, parse, R
O=R+'lit/kht/out/'
recs={r['file']:parse(r) for r in load_jsonl(O+'k138/k138.jsonl') if parse(r)}
def comp_points(c,j):
    pts=[]
    for idem,h,q in c['gens']:
        if idem=='⬮':
            C=q-24*j; D=q//2-h-4*j; pts.append(((C+8*D)//2,D))
    return pts
def arc_steps(c):
    """steps between consecutive • along the arc, in (u,D) grid"""
    G=c['gens']; idx=[i for i,g in enumerate(G) if g[0]=='⬮']
    pts=[(g[2],g[2]//2-g[1]) for g in G if g[0]=='⬮']
    st=[]
    for (q1,d1),(q2,d2) in zip(pts,pts[1:]):
        du=((q2+8*d2)-(q1+8*d1))//2; dD=d2-d1; st.append((du,dD))
    return st
shapes=Counter(); bykj={}
for name,p in recs.items():
    fs=glob.glob(O+'k138/examples/si/%s/cxBNr-c2-q*'%name.replace('^','-'))
    if not fs: continue
    chs=read_file(fs[0]); j=int(p['j']); k=p['k']
    arcs=[c for c in chs if not c['cyclic']]
    assert len(arcs)==1
    st=tuple(arc_steps(arcs[0]))
    bykj.setdefault((k,j),set()).add(st)
print('number of (k,j):',len(bykj),' with non-unique arc shape:',[(kj,v) for kj,v in bykj.items() if len(v)>1])
for kj in sorted(bykj)[:40]:
    for st in bykj[kj]: print(kj,'n•=%d'%(len(st)+1),''.join({(1,0):'R',(-1,0):'L',(0,1):'U',(0,-1):'D'}.get(s,str(s)) for s in st))
# picture for 9_46^1 and a few others with squares
for name in ['9_46^1','8_20','6_3^1','9_42','10_?']:
    if name not in recs: continue
    p=recs[name]; j=int(p['j'])
    chs=read_file(glob.glob(O+'k138/examples/si/%s/cxBNr-c2-q*'%name.replace('^','-'))[0])
    print(name,'k',p['k'],'j',j)
    for c in chs: print('   ','square' if c['cyclic'] else 'arc   ',sorted(comp_points(c,j)))
