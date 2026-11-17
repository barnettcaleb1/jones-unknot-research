# Referee: 4T (quotient-sign normalisation) on random backgrounds; 1T-a,b,c and the equivariant-1T conjecture at order 4.
import sys, random, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/referee/proofref')
import ss
from abstract_ref import shapes, realize
def recs_from_slots(slots, qsign=None, usign=None):
    """slots: tokens 'cK' (chord K endpoints), 'o' (on-axis site), 'g' (non-site twist).
    qsign: dict chord->quotient sign (kappa*pi); usign: dict chord->upstairs sign. on-axis sites get eps=+1."""
    L=len(slots); axis=set(p for p,tk in enumerate(slots) if tk in ('o','g')); pos={}
    for p,tk in enumerate(slots):
        if tk.startswith('c'): pos.setdefault(tk,[]).append(p)
    recs=[]
    for c in sorted(pos):
        a,b=pos[c]; tau=sum(1 for p in axis if a<p<b)%2
        if qsign is not None: kp=qsign[c]
        else: kp=usign[c]*(-1)**tau
        recs.append(dict(kind='off',a=a,b=b,kap=kp,pi=1,tau=tau,name=c))
    for p,tk in enumerate(slots):
        if tk=='o': recs.append(dict(kind='on',c=p,kap=-1,name='o%d'%p))
    return L,axis,recs
def WJ(slots,**kw):
    L,ax,recs=recs_from_slots(slots,**kw); return ss.W_J(L,ax,recs)[0]
def What(slots,**kw):
    L,ax,recs=recs_from_slots(slots,**kw); return ss.W_hat(L,ax,recs,list(range(len(recs))))
def test4T(rnd, ntrials):
    ok=[0,0]; okhat=[0,0]; ups=[0,0]
    for _ in range(ntrials):
        nb=rnd.randint(0,2); nob=rnd.randint(0,1)
        pts=['c%d'%i for i in range(nb) for _ in (0,1)]+['o']*nob+['g']*rnd.randint(0,4)
        rnd.shuffle(pts)
        while len(pts)<2: pts.insert(rnd.randint(0,len(pts)),'g')
        # three insertion gaps (positions in 0..len(pts)), distinct, random roles
        gaps=rnd.sample(range(len(pts)+1),3); I1,I2,I3=gaps
        bq={('c%d'%i):rnd.choice([1,-1]) for i in range(nb)}
        def build(order1, order2, which):
            # which='13': chords X=(I1,I2), Y=(I1,I3); order1 on I1 ; which='23': X=(I1,I2), Y=(I2,I3); order2 on I2
            ins={I1:[],I2:[],I3:[]}
            if which=='13':
                ins[I1]=['cX','cY'] if order1=='X<Y' else ['cY','cX']; ins[I2]=['cX']; ins[I3]=['cY']
            else:
                ins[I2]=['cX','cY'] if order2=='X<Y' else ['cY','cX']; ins[I1]=['cX']; ins[I3]=['cY']
            out=[]
            for q in range(len(pts)+1):
                out+=ins.get(q,[])
                if q<len(pts): out.append(pts[q])
            return out
        D1=build('Y<X',None,'13'); D2=build('X<Y',None,'13'); D3=build(None,'Y<X','23'); D4=build(None,'X<Y','23')
        qs=dict(bq); qs['cX']=1; qs['cY']=1
        v=[WJ(D,qsign=qs) for D in (D1,D2,D3,D4)]; ok[0 if v[0]-v[1]+v[2]-v[3]==0 else 1]+=1
        vh=[What(D,qsign=qs) for D in (D1,D2,D3,D4)]; okhat[0 if vh[0]-vh[1]+vh[2]-vh[3]==0 else 1]+=1
        us=dict(bq); us['cX']=1; us['cY']=1
        vu=[WJ(D,usign=us) for D in (D1,D2,D3,D4)]; ups[0 if vu[0]-vu[1]+vu[2]-vu[3]==0 else 1]+=1
    print('4T quotient signs W(J) [ok,fail]:',ok,' W(Jhat):',okhat,'   upstairs-sign normalisation W(J):',ups)
def lift(slots):
    """upstairs chords on the circle: K1 slot p -> coordinate p, h(p) -> coordinate 2L-1-p (reversed)."""
    L=len(slots); axis=set(p for p,tk in enumerate(slots) if tk in ('o','g')); pos={}
    for p,tk in enumerate(slots):
        if tk.startswith('c'): pos.setdefault(tk,[]).append(p)
    H=lambda p: 2*L-1-p; ch=[]; pairs=[]
    for c in sorted(pos):
        a,b=pos[c]; tau=sum(1 for p in axis if a<p<b)%2
        if tau==0: pr=[(a,b),(H(a),H(b))]
        else: pr=[(a,H(b)),(H(a),b)]
        pairs.append((len(ch),len(ch)+1)); ch+=pr
    for p,tk in enumerate(slots):
        if tk=='o': ch.append((p,H(p))); pairs.append((len(ch)-1,))
    return ch,pairs
def cross(u,v):
    a,b=sorted(u); c,d=sorted(v); return (a<c<b)!=(a<d<b)
def degenerate(slots):
    ch,pairs=lift(slots)
    for i,u in enumerate(ch):
        if not any(cross(u,v) for j,v in enumerate(ch) if j!=i): return True
    for pr in pairs:
        if len(pr)==2:
            i,j=pr
            if cross(ch[i],ch[j]) and not any(cross(ch[k],ch[l]) for k in pr for l in range(len(ch)) if l not in pr): return True
    return False
def t1T(m):
    stats={'1Ta':[0,0],'1Tb':[0,0],'1Tc':[0,0],'conj':[0,0],'converse_exc':0,'types':0,'nonzero':0}; exc=[]
    for nc in range(m,-1,-1):
        for seq in shapes(nc,m-nc):
            seen={}
            for gpat in itertools.product([0,1],repeat=len(seq)-1):
                slots=realize(seq,gpat)
                L,ax,recs=recs_from_slots(slots,usign={('c%d'%i):1 for i in range(nc)})
                labs=tuple(r['tau'] for r in recs if r['kind']=='off')
                if labs in seen: continue
                W=ss.W_J(L,ax,recs)[0]; seen[labs]=W; stats['types']+=1; stats['nonzero']+=(W!=0)
                sitepts=set(p for r in recs for p in ((r['a'],r['b']) if r['kind']=='off' else (r['c'],)))
                offs=[r for r in recs if r['kind']=='off']
                for r in offs:
                    empty=not any(r['a']<p<r['b'] for p in sitepts)
                    enclosed=any(s['a']<r['a'] and r['b']<s['b'] for s in offs if s is not r)
                    if empty and r['tau']==0: stats['1Ta'][0 if W==0 else 1]+=1
                    if empty and not enclosed: stats['1Tb'][0 if W==0 else 1]+=1
                for r in recs:
                    if r['kind']=='on' and not any(s['a']<r['c']<s['b'] for s in offs): stats['1Tc'][0 if W==0 else 1]+=1
                dg=degenerate(slots)
                if dg: stats['conj'][0 if W==0 else 1]+=1
                if dg and W!=0: exc.append(('conj-fail',' '.join(seq),labs,W))
                if (not dg) and W==0: stats['converse_exc']+=1; exc.append(('converse',' '.join(seq),labs))
    print('order',m,stats); print('  examples:',exc[:6])
if __name__=='__main__':
    rnd=random.Random(int(sys.argv[1]))
    test4T(rnd,int(sys.argv[2]))
    for m in (2,3,4): t1T(m)
