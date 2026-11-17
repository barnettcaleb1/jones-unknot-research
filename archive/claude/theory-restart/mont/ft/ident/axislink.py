"""K u O': the knot with its axis pushed off K at the two fixed points (crossing c_t at the top, c_b at the bottom).
positions: 0 = far-left O_out strand; at the top caps (Oleft,Otop),(KL,KR), Otop crosses KL; at the bottom O_in crosses KLend."""
import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import alex, diag, butterfly as bf
def tokens(word, ct, cb, smooth_top=None):
    half=alex.parse(word)
    body=diag.extended_tokens(half)
    if body is None: return None
    top=[(ct,1)] if smooth_top is None else smooth_top
    return top+[(c,i+1) for c,i in body]+[(cb,1)]
def build(word, ct, cb, smooth_top=None):
    g=lambda n:('g',n)
    toks=tokens(word,ct,cb,smooth_top)
    if toks is None: return None
    D,pos=diag.morse_diagram(toks,[g('Ol'),g('Ot'),g('KL'),g('KR')])
    if len(pos)!=4: return None
    D.uf.union(pos[0],g('Ole')); D.uf.union(pos[1],g('Oie')); D.uf.union(pos[2],g('KLe')); D.uf.union(pos[3],g('KRe'))
    joins=[(g('Ol'),g('Ot')),(g('KL'),g('KR')),(g('Ole'),g('Oie')),(g('KLe'),g('KRe'))]
    germs=[g(n) for n in ('Ol','Ot','KL','KR','Ole','Oie','KLe','KRe')]
    allpts=[sl for _,sls in D.cr for sl in sls]+germs
    ends={}
    for p in allpts:
        if p in D.uf.p or p[0]=='c': ends.setdefault(D.uf.find(p),[]).append(p)
    partner={}
    for r,ps in ends.items():
        if len(ps)!=2: return None
        partner[ps[0]]=ps[1]; partner[ps[1]]=ps[0]
    jmap={}
    for a,b in joins: jmap[a]=b; jmap[b]=a
    newp={}
    for sl,q in partner.items():
        if sl[0]!='c': continue
        while q[0]!='c': q=partner[jmap[q]]
        newp[sl]=q
    def first(germ):
        q=partner[germ]
        while q[0]!='c': q=partner[jmap[q]]
        return q
    return D.cr,newp,first(g('KR')),first(g('Ot'))
def data(word,ct,cb):
    b=build(word,ct,cb)
    if b is None: return None
    crs,partner,sK,sO=b
    ld=bf.link_data(crs,partner,[sK,sO],[False,False])
    if ld is None: return None
    return crs,partner,ld
def sato_levine(word):
    """a3 of K u O' for the pushoffs with lk = 0 (should be independent of the choice; both computed)."""
    res={}
    for ct in 'xy':
        for cb in 'xy':
            d=data(word,ct,cb)
            if d is None: return None
            res[(ct,cb)]=d[2][4]//2
    out={}
    for (ct,cb),lk in res.items():
        if lk!=0: continue
        # partner member: switch the top crossing -> lk = +-1, sign of Conway fixed; skein back
        ct2='y' if ct=='x' else 'x'
        d1=data(word,ct2,cb); crs1,partner1,ld1=d1
        lk1=ld1[4]//2
        if abs(lk1)!=1: out[(ct,cb)]=('lk1?',lk1); continue
        P1=bf.alexander_link(crs1,partner1,ld1[0],ld1[3])
        cw1=bf.conway_2comp(P1,lk1)
        if not isinstance(cw1,list): out[(ct,cb)]=('cw?',cw1); continue
        a3_1=cw1[1] if len(cw1)>1 else 0
        # smoothing of the top crossing (crossing index 0) in the lk=0 member: orientation of the two strands there
        crs0,partner0,ld0=data(word,ct,cb)
        sign0=ld0[3][0]
        dirs=ld0[2]
        d0=dirs[(0,0)]; d1_=dirs[(0,1)]      # TL-BR strand and TR-BL strand directions
        # parallel (both downward or both upward) -> vertical smoothing; else horizontal
        par=(d0[1]<0)==(d1_[1]<0)
        sm=[] if par else [('u',1),('l',1)]
        bsm=build(word,ct,cb,smooth_top=sm)
        crsS,partnerS,_,_=bsm
        inv=diag.knot_invariants(crsS,partnerS)
        if inv is None: out[(ct,cb)]=('smooth?',); continue
        a2s=inv['a2']
        # L0 member has crossing sign sign0; skein: a3(L+) - a3(L-) = a2(smoothing)
        a3_0 = a3_1 + a2s if sign0>0 else a3_1 - a2s
        out[(ct,cb)]=a3_0
    return out
