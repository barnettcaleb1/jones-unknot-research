"""L_Theta = K_in u K_out pushed apart along k (the 2-component link = the distance-1 filling of the quotient tangle whose
bracket determines J).  Positions: 0 = A_out (crossing-free, far left), 1 = A_in, doubled half-strand j -> (2j+2, 2j+3).
nb extra crossings between the two parallels of k at the start (full twists keep 2 components; each changes lk by +-1)."""
import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import alex, diag, butterfly as bf
def tokens(word, nb, btype):
    half=alex.parse(word)
    out=[(btype,2)]*nb
    for c,s in half:
        if s==0: out+=[(c,1),(c,2),(c,2),(c,1)]
        elif c in 'xy': out+=[(c,2*s+1),(c,2*s),(c,2*s+2),(c,2*s+1)]
        elif c in 'lr': out+=[(c,2*s),(c,2*s+1)]
        elif c=='u': out+=[('u',2*s+1),('u',2*s)]
    return out
def build(word, nb, btype):
    g=lambda n:('g',n)
    toks=tokens(word,nb,btype)
    D,pos=diag.morse_diagram(toks,[g('Ao'),g('Ai'),g('ki'),g('ko')])
    if len(pos)!=4: return None
    D.uf.union(pos[0],g('Aoe')); D.uf.union(pos[1],g('Aie')); D.uf.union(pos[2],g('kae')); D.uf.union(pos[3],g('kbe'))
    joins=[(g('Ao'),g('ko')),(g('Ai'),g('ki')),(g('Aie'),g('kae')),(g('Aoe'),g('kbe'))]
    germs=[g(n) for n in ('Ao','Ai','ki','ko','Aoe','Aie','kae','kbe')]
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
    # C1 = A_in u k_inner, oriented: A_in from v_top down to v_bottom: start at the slot after germ Ai
    def first(germ):
        q=partner[germ]
        while q[0]!='c': q=partner[jmap[q]]
        return q
    s1=first(g('Ai')); s2=first(g('Ao'))
    return D.cr,newp,s1,s2
def link_conway(word, nb, btype):
    b=build(word,nb,btype)
    if b is None: return None
    crs,partner,s1,s2=b
    ld=bf.link_data(crs,partner,[s1,s2],[False,False])
    if ld is None: return None
    comps,comp_of,dirs,signs,lk2=ld
    if lk2==0: return 0,None
    P=bf.alexander_link(crs,partner,comps,signs)
    cw=bf.conway_2comp(P,lk2//2)
    return lk2//2,cw
def lk_of(word,nb,btype):
    b=build(word,nb,btype)
    if b is None: return None
    crs,partner,s1,s2=b
    ld=bf.link_data(crs,partner,[s1,s2],[False,False])
    return None if ld is None else ld[4]//2
def a3_lk0(word):
    """a3 of L_Theta with the parallel-twist making lk = 0, by linear extrapolation from lk = +-1, +-2, +-3 (checked linear)."""
    l0=lk_of(word,0,'x')
    if l0 is None: return None
    # find twisting direction: each full twist (2 crossings) changes lk by +-1
    l2x=lk_of(word,2,'x')
    step=l2x-l0
    if step==0: return None
    btype='x'
    # nb for lk=0:
    k=-l0//step if (-l0)%step==0 else None
    if k is None: return None
    if k<0: btype='y'; k=-k   # assume y twists go the other way
    nb0=2*k
    if lk_of(word,nb0,btype)!=0: return ('lkfail',l0,step,btype,nb0,lk_of(word,nb0,btype))
    res=[]
    for j in (1,2,3,4):
        r=link_conway(word,nb0+2*j,btype)
        if r is None or not isinstance(r[1],list): return ('fail',r)
        res.append((r[0],r[1][1] if len(r[1])>1 else 0))
    a=[x[1] for x in res]
    if a[3]-3*a[2]+3*a[1]-a[0]!=0: return ('notquadratic',res)
    return dict(a3=3*a[0]-3*a[1]+a[2], second=a[2]-2*a[1]+a[0], lks=[x[0] for x in res])
