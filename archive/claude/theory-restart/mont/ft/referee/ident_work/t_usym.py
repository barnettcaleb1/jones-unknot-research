# Consistency test of the builder's upstairs constituents U_in = K_+ u O_in, U_out = K_+ u O_out (diag.py, copied):
# h maps K_+ u O to K_- u O, so the knots built from K_+ and from K_- must agree.  Control: a deliberately wrong
# resolution of the on-axis triple point (axis on top) to see that the test discriminates.
import sys, random
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/referee/ident_work')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import diag_copy as dg, refinv as R, flat_search as fs
g=lambda v,n:('g',v,n)
def U_pair(w):
    S=dg.full_structure(w)
    if S is None: return None
    out={}
    for name,keepO in (('in','O'),('out','Oout')):
        res=[]
        for side,top,end in (('+','KR',S['endp']),('-','KL',S['endm'])):
            keep={'K'+side,keepO}
            if keepO=='O': joins=[(g('t',top),g('t','O')),(end,g('b','O'))]
            else: joins=[(g('t',top),g('t','Oout')),(end,g('b','Oout'))]
            crs,pt=dg.sub_knot(S,keep,joins); inv=dg.knot_invariants(crs,pt)
            if inv is None: return None
            res.append((tuple(sorted(inv['V'].items())),tuple(sorted(inv['Delta'].items()))))
        out[name]=res
    return out
orig=dg.extended_tokens
def wrong_tokens(half):
    hw=1; out=[]
    for c,s in half:
        if s==0:
            # WRONG: axis passes over both strands (P over A replaced by A over P)
            if c=='x': out+=[('y',hw-1),('x',hw),('x',hw-1)]
            elif c=='y': out+=[('y',hw),('y',hw-1),('x',hw)]
            else: return None
        elif c in 'xy': out.append((c,hw+s)); out.append((c,hw-s-1))
        elif c in 'lr': out.append((c,hw+s)); out.append((c,hw-s+1)); hw+=2
        elif c=='u': out.append(('u',hw+s)); out.append(('u',hw-s-1)); hw-=2
        else: return None
        if hw<1: return None
    if hw!=1: return None
    return out
for label,fn in (('builder resolution',orig),('WRONG resolution (control)',wrong_tokens)):
    dg.extended_tokens=fn
    rnd=random.Random(9601); tot=0; agree={'in':0,'out':0}; nontriv=0
    while tot<60:
        w=fs.gen(rnd,rnd.randint(8,18)) if rnd.random()<0.5 else R.gen2(rnd,rnd.randint(8,16),maxw=5,pw=0.35)
        if not w or 'x0' not in w and 'y0' not in w: continue
        if R.Kinv(w) is None: continue
        p=U_pair(w)
        if p is None: continue
        tot+=1
        for nm in ('in','out'): agree[nm]+= p[nm][0]==p[nm][1]
        nontriv+= p['in'][0][0]!=((0,1),)
    print('%s: words with windings %d | U_in(K+)=U_in(K-) %d | U_out(K+)=U_out(K-) %d | U_in nontrivial V %d'%(label,tot,agree['in'],agree['out'],nontriv))
