"""Fast scan for CERTIFIED NON-SEMI-ADEQUATE branch knots L_{+-1} over a_2(K) = 0 members of the Theorem V3 class.
Framing via integer determinants (alex matrix at t=-1, Bareiss) instead of bracket sums.  usage: census2.py MAXWORDLEN NBOX SEED MAXK"""
import sys, json, itertools, random, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import bk, alex, vc, lp, a2search, identK, semiadq, regina
def detknot(full):
    cr=alex.diagram(full)
    if cr is None: return None
    if not cr: return 1
    M,w=alex.alex_matrix(cr,-1)
    return abs(alex.bareiss([r[:-1] for r in M[:-1]]))
def frame_det(hw):
    vals={}
    for f in range(0,4):
        d=detknot(bk.full_closure(hw,bk.tw(0,f)+bk.C_ZERO))
        if d is not None: vals[f]=d
    # |f-f0| = d for the knot-valued f's (two of them, same parity)
    fs=sorted(vals)
    cands=set([fs[0]+vals[fs[0]],fs[0]-vals[fs[0]]])
    cands=[c for c in cands if all(abs(f-c)==vals[f] for f in fs)]
    assert len(cands)==1,(vals,cands)
    return cands[0]
maxlen,nbox,seed,maxK=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4])
W=sorted(a2search.words(maxlen).values())
vecs={w:vc.rat(w) for w in W}
rnd=random.Random(seed)
cases=[]
tries=0
while len(cases)<maxK and tries<400000:
    tries+=1
    combo=tuple(sorted(rnd.choice(W) for _ in range(nbox)))
    N=rnd.randint(-3,3); a=rnd.choice([3,-3,5,-5,7,-7])
    J=vc.J_vert(a,vc.Ypow(N,vc.starall([vecs[w] for w in combo])))
    if J is None or lp.a2(J)!=0: continue
    cases.append((a,N,combo))
stats={'K':0,'L':0,'V1':0,'cert_nonsemi':0,'cert_nonadeq':0}; hits=[]
log=open('census2_%d_%d_%d.log'%(maxlen,nbox,seed),'w')
for a,N,combo in cases:
    hw=identK.halfword(a,N,list(combo))
    try: f=frame_det(hw)
    except Exception as e: log.write('FRAMEFAIL %s %s\n'%(hw,e)); continue
    stats['K']+=1
    for n in (1,-1):
        pd=bk.pd_code(bk.full_Ln(hw,n,f))
        V=bk.jones_t(regina.Link.fromPD(pd)); stats['L']+=1
        if V=={0:1}: stats['V1']+=1
        okL,okH=semiadq.jones_end_test(V)
        if not(okL and okH): stats['cert_nonadeq']+=1
        if not okL and not okH:
            stats['cert_nonsemi']+=1; hits.append((a,N,combo,n,hw,sorted(V.items())))
            log.write('HIT a=%d N=%d %s n=%d %s\n'%(a,N,combo,n,hw)); log.flush()
    if stats['K']%25==0:
        log.write('%s\n'%stats); log.flush()
print(stats,flush=True)
for h in hits[:10]: print('NON-SEMIADEQUATE (a2=0):',h[:5],flush=True)
json.dump({'stats':stats,'hits':hits},open('census2_%d_%d_%d.json'%(maxlen,nbox,seed),'w'))
