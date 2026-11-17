"""R1(a)-(b): the quotient dictionary checked from explicit closed theta-graph diagrams built here
(own vertex marking, own bracket sweep).  For each word w:
  L_b=<D_I> (two theta cycles), L_c=<D_e> (axis restored, turnback at v_top), also turnback at v_bot and at a
  random interior band point;  theta=L_b-delta^-1 L_c must be divisible by Delta2 -> y ; u=L_c/delta monomial;
  compare (y,x) with flat_search.bracket_vector EXACTLY, Norm(y/u) with lp.J EXACTLY;
  f2 duplication: <D with f2 at P and Q> = <D with f2 at P>;
  half-twist marking change: (y,x)->(A y, A^-1 y - A^-3 x) multiplies y/u by -t; at the preferred marking delta | x."""
import sys, json, random, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/referee/skein-dictionary')
from refskein import *
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont'); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, alex, flat_search as fs
def is_knot(w):
    full=alex.symmetrize(alex.parse(w))
    return full is not None and alex.diagram(full) is not None
def width(B):
    w=1;mx=1
    for tok in B.split('.'):
        if not tok or tok=='s': continue
        c=tok[0]
        if c in 'lr': w+=2
        elif c=='u': w-=2
        mx=max(mx,w)
    return mx
def tw(m): return ('y1.' if m>0 else 'x1.')*abs(m)
rnd=random.Random(99)
gb=[B for B,_ in json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/general_boxes.json'))]
words=[]
def add(w,kind):
    if is_knot(w) and w not in [x for x,_ in words]: words.append((w,kind))
while sum(1 for _,k in words if k=='2-bridge')<8:
    W=fs.reduced([rnd.choice('xy')+str(rnd.choice([0,1])) for _ in range(rnd.randint(3,9))])
    if W: add('s.l1.'+'.'.join(W)+'.u2','2-bridge')
rat=['y0','x0','y0.y0','x0.x0.x0','l1.x0.y1.x0.u2','l1.y0.x1.y0.y1.u2']
while sum(1 for _,k in words if k=='necklace rational')<6:
    bs=[rnd.choice(rat) for _ in range(rnd.choice([2,3]))]; m=rnd.choice([-2,-1,1,2,3])
    add('s.r2.'+tw(m)+'.'.join(bs)+'.u1','necklace rational')
small=[B for B in gb if width(B)<=3]
while sum(1 for _,k in words if k=='necklace nonrational')<6:
    bs=[rnd.choice(small+rat) for _ in range(rnd.choice([1,2]))]; m=rnd.choice([-2,-1,1,2])
    add('s.r2.'+tw(m)+'.'.join(bs)+'.u1','necklace nonrational')
while sum(1 for _,k in words if k=='nested depth2')<4:
    inner='r2.'+tw(rnd.choice([-1,1,2]))+'.'.join(rnd.choice(rat+small[:5]) for _ in range(2))+'.u1'
    add('s.r2.'+tw(rnd.choice([-1,1]))+inner+'.'+rnd.choice(rat)+'.u1','nested depth2')
for B in rnd.sample([B for B in gb if width(B)<=5],6): add('s.'+B,'closure of general body')
for B in ['y0','y0.y0.y0','r1.y1.x0.u2']:
    for a in (3,-3):
        add('s.l1.'+B+'.'+('x2.' if a>0 else 'y2.')*abs(a)+'u1','vertical')
add('s.l1.x2.x2.x2.u1','swap 3_1#3_1'); add('s.l1.y2.y2.y2.y2.y2.u1','swap')
while sum(1 for _,k in words if k=='random fs.gen')<8:
    w=fs.gen(rnd,rnd.randint(6,14))
    if w and width(w)<=5: add(w,'random fs.gen')
stats={k:0 for k in ['words','theta_div_Delta2','u_monomial','yx_eq_fs','J_eq_lp','e_top_eq_bot','e_mid_eq_top','f2_dup','halftwist_rule','pref_delta_div_x']}
fails=[]; t0=time.time(); rows=[]
for w,kind in words:
    stats['words']+=1
    td=theta_data(w)
    stats['theta_div_Delta2']+=1  # asserted inside theta_data
    u=td['u']
    if len(u)==1: stats['u_monomial']+=1
    else: fails.append((w,'u not monomial'))
    yv,xv=fs.bracket_vector(alex.parse(w))
    if td['y']==pclean(yv) and td['x']==pclean(xv): stats['yx_eq_fs']+=1
    else: fails.append((w,'(y,x) differs from flat_search'))
    (eu,cu),=u.items()
    assert all((e-eu)%4==0 for e in td['y'])
    jr={(e-eu)//4:c*cu for e,c in td['y'].items()}
    J=Norm(jr)
    if J==lp.J(w): stats['J_eq_lp']+=1
    else: fails.append((w,'Norm(y/u) != lp.J'))
    if td['Lc']==td['Lc_bot']: stats['e_top_eq_bot']+=1
    else: fails.append((w,'turnback top != bottom'))
    # interior turnback(s): insert e (cup+cap) on a band (half-strand j) between two letters
    half=parse(w)
    # positions of half-strands available after each prefix
    widths=[1]; cur=1
    for c,s in half:
        if c in 'lr': cur+=2
        elif c=='u': cur-=2
        widths.append(cur)
    def ops_with_e(cuts):
        # cuts: list of (k,j): after k letters, turn back band of half-strand j
        ops=[('cap',0),('cap',1)]
        for k in range(len(half)+1):
            for (kk,j) in cuts:
                if kk==k:
                    a=1+2*j+1
                    ops+=[('cup',a),('cap',a)]
            if k<len(half): ops+=ribbon_ops([half[k]],off=1)
        ops+=[('cup',1),('cup',0)]
        return ops
    k1=rnd.randrange(len(half)+1); j1=rnd.randrange(widths[k1])
    LeP=closed_bracket(ops_with_e([(k1,j1)]))
    if LeP==td['Lc']: stats['e_mid_eq_top']+=1
    else: fails.append((w,'interior turnback differs',k1,j1))
    k2=rnd.randrange(len(half)+1); j2=rnd.randrange(widths[k2])
    if (k2,j2)!=(k1,j1):
        LeQ=closed_bracket(ops_with_e([(k2,j2)])); LePQ=closed_bracket(ops_with_e([(k1,j1),(k2,j2)]))
        # <(I-d^-1 eP)(I-d^-1 eQ)> = Lb - d^-1 LeP - d^-1 LeQ + d^-2 LePQ  should equal Lb - d^-1 LeP
        lhs=padd(td['Lb'],pneg(pdiv(LeP,DELTA)),pneg(pdiv(LeQ,DELTA)),pdiv(pdiv(LePQ,DELTA),DELTA))
        if lhs==td['theta']: stats['f2_dup']+=1
        else: fails.append((w,'f2 duplication fails'))
    else: stats['f2_dup']+=1
    # half-twist marking change on the band ends: (y,x) -> (A y, A^-1 y - A^-3 x)
    y,x=td['y'],td['x']
    y1=pshift(y,1); x1=padd(pshift(y,-1),pneg(pshift(x,-3)))
    u1=padd(y1,pmul(DELTA,x1))
    (eu1,cu1),=u1.items()
    j1r={(e-eu1)//4:c*cu1 for e,c in y1.items()}
    if j1r==tshift(jr,1,-1): stats['halftwist_rule']+=1
    else: fails.append((w,'half-twist rule'))
    # preferred marking: k = number of half twists with Norm = (-t)^k (y/u); apply k (or -k inverse) twists to (y,x)
    sgn,kk=norm_unit(jr)
    # Norm(jr) = sgn t^kk jr = (-t)^kk jr * (sgn (-1)^kk); twist count = kk
    yy,xx=y,x
    for _ in range(abs(kk)):
        if kk>0: yy,xx=pshift(yy,1),padd(pshift(yy,-1),pneg(pshift(xx,-3)))
        else:    # inverse half twist: (y,x)->(A^-1 y, A y - A^3 x)
                 yy,xx=pshift(yy,-1),padd(pshift(yy,1),pneg(pshift(xx,3)))
    uu=padd(yy,pmul(DELTA,xx)); (e2,c2),=uu.items()
    jj={(e-e2)//4:c*c2 for e,c in yy.items()}
    okdiv = pdiv(xx,{4:1,0:1}) is not None   # (A^4+1) | x  <=> delta | x
    if okdiv and tev(jj,-1) in (1,-1) and tder_m1(jj)==0: stats['pref_delta_div_x']+=1
    else: fails.append((w,'preferred marking: delta does not divide x',kk))
    rows.append(dict(w=w,kind=kind,J=sorted(J.items()) if J else None,halftwists_to_pref=kk))
print(json.dumps(stats,indent=0)); print('fails',len(fails))
for f in fails: print('FAIL',f)
from collections import Counter
print(Counter(k for _,k in words)); print('time',round(time.time()-t0,1))
json.dump(dict(stats=stats,fails=[list(map(str,f)) for f in fails],rows=rows),open('check_dictionary.json','w'))
