"""Census of branch knots L_n (n = +-1, +-2) over Theorem-V3-class inversions: Jones end test for semi-adequacy
(semi-adequate => at some end |c0| = 1 and c0*c1 <= 0) and adequacy of the natural / regina-simplified diagram.
usage: census.py MAXWORDLEN MAXCASES a2mode(zero|nonzero) SEED"""
import sys, json, itertools, random, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import bk, vc, lp, a2search, identK, semiadq, regina
def det_f(hw,f): return bk.det_from_bracket(bk.bracket_full(bk.full_closure(hw,bk.tw(0,f)+bk.C_ZERO)))
def frame_fast(hw):
    d0=det_f(hw,0); d1=det_f(hw,1)
    cands=[f for f in (d0,-d0) if abs(1-f)==d1]
    for f in cands:
        if det_f(hw,f)==0: return f
    raise ValueError((d0,d1))
maxlen,maxcases,mode,seed=int(sys.argv[1]),int(sys.argv[2]),sys.argv[3],int(sys.argv[4])
W=sorted(a2search.words(maxlen).values())
vecs={w:vc.rat(w) for w in W}
cases=[]
for combo in itertools.combinations_with_replacement(W,2):
    p=vc.starall([vecs[w] for w in combo])
    for N in range(-3,4):
        q=vc.Ypow(N,p)
        for a in (3,-3,5,-5):
            J=vc.J_vert(a,q)
            if J is None: continue
            z=(lp.a2(J)==0)
            if (mode=='zero')==z: cases.append((lp.span(J),a,N,combo))
random.Random(seed).shuffle(cases)
cases=sorted(cases[:maxcases*5])[:maxcases] if mode=='zero' else cases[:maxcases]
stats={'K':0,'L':0,'cert_nonsemiadequate':0,'cert_nonadequate':0,'natural_semiadequate':0,'simplified_semiadequate':0,'V_is_1':0,'det_not_1':0}
hits=[]
log=open('census_%s_%d.log'%(mode,seed),'w')
for spanJ,a,N,combo in cases:
    hw=identK.halfword(a,N,list(combo))
    try: f=frame_fast(hw)
    except Exception as e:
        log.write('FRAMEFAIL %s %s\n'%(hw,e)); continue
    stats['K']+=1
    for n in (1,-1,2,-2):
        full=bk.full_Ln(hw,n,f); pd=bk.pd_code(full)
        L=regina.Link.fromPD(pd); V=bk.jones_t(L)
        stats['L']+=1
        if V=={0:1}: stats['V_is_1']+=1
        okL,okH=semiadq.jones_end_test(V)
        A,B,_,_=bk.adequacy(pd)
        Ls=regina.Link.fromPD(pd); Ls.simplify(); As,Bs,_,_=bk.adequacy([tuple(x) for x in Ls.pdData()])
        if A or B: stats['natural_semiadequate']+=1
        elif As or Bs: stats['simplified_semiadequate']+=1
        if not okL and not okH: stats['cert_nonsemiadequate']+=1; hits.append((a,N,combo,n,hw,sorted(V.items())))
        if not (okL and okH): stats['cert_nonadequate']+=1
        log.write('%s a=%d N=%d %s n=%d endtest=%s natAB=%s simpAB=%s spanV=%d\n'%(mode,a,N,combo,n,(okL,okH),(A,B),(As,Bs),max(V)-min(V)))
    log.flush()
print(mode,seed,stats,flush=True)
for h in hits[:10]: print('NON-SEMIADEQUATE:',h[:5],flush=True)
json.dump({'stats':stats,'hits':hits},open('census_%s_%d.json'%(mode,seed),'w'))
