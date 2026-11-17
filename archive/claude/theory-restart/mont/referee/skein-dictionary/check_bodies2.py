"""R1 independent body checks (Sections 4-6), raw TL3 expansion of the 2-cabled body; necklace bodies by locality
(macro sweep: inner TL3 element inserted as a box; validated against direct sweeps)."""
import sys, json, time, random
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/referee/skein-dictionary')
from refskein import *
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont'); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, alex
ONE_MINUS_T3={0:1,3:-1}
def tw(m): return ('y1.' if m>0 else 'x1.')*abs(m)
def width(B):
    w=1;mx=1
    for tok in B.split('.'):
        c=tok[0]
        if c in 'lr': w+=2
        elif c=='u': w-=2
        mx=max(mx,w)
    return mx
def is_knot(B):
    full=alex.symmetrize(alex.parse('s.'+B))
    return full is not None and alex.diagram(full) is not None
base=[(B,k) for B,k in json.load(open('bodies.json')) if not k.startswith('necklace')]
tl3cache={}
def tl3(node):
    if isinstance(node,str):
        if node not in tl3cache: tl3cache[node]=body_TL3(node)
        return tl3cache[node]
    m,ch=node['m'],node['ch']
    return tl3_necklace(m,tl3_product(*[tl3(c) for c in ch]))
def word(node):
    if isinstance(node,str): return node
    return 'r2.'+tw(node['m'])+'.'.join(word(c) for c in node['ch'])+'.u1'
rnd=random.Random(1117)
nodes=[(B,k) for B,k in base]
small=[B for B,k in base if width(B)<=5]
d2=[]
while len(d2)<40:
    n=rnd.choice([1,2,2,3]); m=rnd.choice([-3,-2,-1,1,2,3])
    node={'m':m,'ch':[rnd.choice(small) for _ in range(n)]}
    if is_knot(word(node)): d2.append(node)
d3=[]
while len(d3)<25:
    m=rnd.choice([-2,-1,1,2]); ch=[rnd.choice(d2)]+[rnd.choice(small) for _ in range(rnd.choice([0,1,1]))]
    rnd.shuffle(ch)
    node={'m':m,'ch':ch}
    if is_knot(word(node)): d3.append(node)
nodes+= [(x,'necklace depth2') for x in d2]+[(x,'necklace depth3') for x in d3]
def tnorm_vec(a_A,b_A):
    ra,at=to_t(a_A); rb,bt=to_t(b_A)
    assert ra==rb and ra not in (None,'mixed')
    un=norm_unit(at)
    if un is None: return None
    s,k=un
    a=tshift(at,k,s); b=tshift(bt,k,s)
    v2=tdiv(tsub(b,a),ONE_MINUS_T3)
    return a,b,v2,at,bt
gbv={B:[dict((e,c) for e,c in v[0]),dict((e,c) for e,c in v[1])] for B,v in json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/general_boxes.json'))}
keys=['pinned_match','pinned_total','bodies','S5_delta_div','S5_class','S5_1mt_div','S5_A1_identity','S5_v2_integral','S6_a1','S6_b_sign','S6_raw_ratio',
      'dict_sB','dict_sB_total','dict_twisted','dict_twisted_total','thmO_necklace','thmO_total']
st={k:0 for k in keys}; fails=[]; rows=[]
vcache={}
t0=time.time()
for idx,(node,kind) in enumerate(nodes):
    B=word(node); n0=nax(B)
    st['bodies']+=1
    c=tl3(node)
    bc=channels_from_tl3(c)
    if not bc['ok']: fails.append((B,'delta does not divide c_e')); continue
    st['S5_delta_div']+=1
    r1,_=to_t(bc['c1']); r2,cept=to_t(bc['cep'])
    if (r1==r2 and r1 not in (None,'mixed')) or (r2 is None and not bc['cep'] and r1 not in (None,'mixed')): st['S5_class']+=1
    else: fails.append((B,'class',r1,r2))
    if tdiv(cept,{0:1,1:-1}) is not None: st['S5_1mt_div']+=1
    else: fails.append((B,'(1-t) !| c_e/delta'))
    at1={k:sum(p.values()) for k,p in c.items()}
    if abs(at1['I'])==1 and all(at1[k]==0 for k in at1 if k!='I'): st['S5_A1_identity']+=1
    else: fails.append((B,'beta(1)',at1))
    r=tnorm_vec(bc['a'],bc['b'])
    if r is None: fails.append((B,'a not normalisable')); continue
    a,b,v2,at,bt=r
    av,bv=tev(at,-1),tev(bt,-1)
    if av in (1,-1) and bv==av*(-1)**n0: st['S6_raw_ratio']+=1
    else: fails.append((B,'raw root ratio',av,bv,n0))
    if v2 is None: fails.append((B,'v2 not integral')); continue
    st['S5_v2_integral']+=1
    v=[a,v2]; vcache[B]=v
    if tev(a,-1)==1: st['S6_a1']+=1
    if tev(b,-1)==(-1)**n0: st['S6_b_sign']+=1
    else: fails.append((B,'b(-1)',tev(b,-1),n0))
    if B in gbv:
        st['pinned_total']+=1
        if [lp.clean(gbv[B][0]),lp.clean(gbv[B][1])]==[a,v2]: st['pinned_match']+=1
        else: fails.append((B,'pinned vector mismatch'))
    if width(B)<=7:
        st['dict_sB_total']+=1
        if lp.J('s.'+B)==Norm(a): st['dict_sB']+=1
        else: fails.append((B,'lp.J(s.B)!=Norm(a)'))
    if width(B)<=5:
        for m in (1,-1,2,-2):
            Jw=lp.J('s.r2.'+tw(m)+B+'.u1')
            if Jw is None: continue
            st['dict_twisted_total']+=1
            if Jw==Norm(lp.close(-m,v)): st['dict_twisted']+=1
            else: fails.append((B,'twisted',m))
    if not isinstance(node,str):
        # Theorem O (sec 7, bonus): v_N = t^(2m(1-eps)) X^-m (v_1*...*v_n) with children vectors from TL3
        p=None
        for ch in node['ch']:
            vc=vcache[word(ch)]
            p=vc if p is None else lp.star(p,vc)
        eps=tev(lp.b_of(p),-1)
        q=p
        M=lp.Xi if node['m']>0 else lp.Xm
        for _ in range(abs(node['m'])): q=lp.mvec(M,q)
        kk=2*node['m']*(1-eps)
        pred=[lp.shift(q[0],kk),lp.shift(q[1],kk)]
        st['thmO_total']+=1
        if [lp.clean(pred[0]),lp.clean(pred[1])]==[a,v2]: st['thmO_necklace']+=1
        else: fails.append((B,'Theorem O mismatch'))
    rows.append(dict(B=B,kind=kind,n0=n0,width=width(B),b_m1=tev(b,-1),v2_m1=tev(v2,-1),a=sorted(a.items()),v2=sorted(v2.items())))
    if idx%25==0: print(idx,kind,round(time.time()-t0,1),flush=True)
print(json.dumps(st,indent=0)); print('fails',len(fails))
for f in fails[:40]: print('FAIL',f)
from collections import Counter
print('v2(-1) values',Counter(r['v2_m1'] for r in rows))
print('kinds',Counter(r['kind'] for r in rows))
print('n0 parity x b(-1):',Counter((r['n0']%2,r['b_m1']) for r in rows))
print('time',round(time.time()-t0,1))
json.dump(dict(stats=st,fails=[list(map(str,f)) for f in fails],rows=rows),open('check_bodies2.json','w'))
