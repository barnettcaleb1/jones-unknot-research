# Referee: abstract equivariant chord diagrams -> W (eps=+1) using ss.py machinery; compare with builder's w3_table.json.
import sys, itertools, json
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/referee/proofref')
import ss
def matchings(pts):
    if not pts: yield []; return
    a=pts[0]
    for k in range(1,len(pts)):
        rest=pts[1:k]+pts[k+1:]
        for m in matchings(rest): yield [(a,pts[k])]+m
def shapes(nc, no):
    """sequences of length 2nc+no: chord endpoints labelled by chord id (named by first endpoint), and 'o'."""
    n=2*nc+no; out=set()
    for opos in itertools.combinations(range(n),no):
        rest=[p for p in range(n) if p not in opos]
        for M in matchings(rest):
            seq=[None]*n
            for p in opos: seq[p]='o'
            # name chords by order of first endpoint
            M=sorted(M); 
            for cid,(a,b) in enumerate(M): seq[a]=seq[b]='c%d'%cid
            out.add(tuple(seq))
    return sorted(out)
def realize(seq, gpat):
    """insert a non-site twist 'g' after site point q (q=0..len-2) when gpat[q]=1. Returns slot list."""
    slots=[]
    for q,tk in enumerate(seq):
        slots.append(tk)
        if q<len(seq)-1 and gpat[q]: slots.append('g')
    return slots
def W_of_slots(slots):
    L=len(slots); axis=set(p for p,tk in enumerate(slots) if tk in ('o','g'))
    recs=[]; pos={}
    for p,tk in enumerate(slots):
        if tk.startswith('c'): pos.setdefault(tk,[]).append(p)
    labs={}
    for c in sorted(pos):
        a,b=pos[c]; tau=sum(1 for p in axis if a<p<b)%2; labs[c]=tau
        recs.append(dict(kind='off',a=a,b=b,kap=(-1)**tau,pi=1,tau=tau))   # eps = kap*pi*(-1)^tau = +1
    for p,tk in enumerate(slots):
        if tk=='o': recs.append(dict(kind='on',c=p,kap=-1))               # eps = -kap = +1
    W,n=ss.W_J(L,axis,recs)
    assert all(v==4 for v in n), n
    return W, ''.join(str(labs[c]) for c in sorted(pos))
if __name__=='__main__':
    m=int(sys.argv[1]) if len(sys.argv)>1 else 3
    table={}; multi=0
    for nc in range(m,-1,-1):
        no=m-nc
        for seq in shapes(nc,no):
            vals={}
            for gpat in itertools.product([0,1],repeat=len(seq)-1):
                W,lab=W_of_slots(realize(seq,gpat))
                vals.setdefault(lab,set()).add(W)
            for lab,vs in vals.items():
                if len(vs)!=1: multi+=1
                table['%s | %s'%(' '.join(seq),lab)]=sorted(vs)
    print('order',m,'types:',len(table),' label-dependence violations:',multi)
    if m==3:
        b=json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/proof/w3_table.json'))
        miss=[k for k in table if k not in b]; extra=[k for k in b if k not in table]
        diff=[(k,table[k],b[k]) for k in table if k in b and table[k]!=[b[k]]]
        print('keys mine not in builder:',len(miss),miss[:5],' builder not mine:',len(extra),extra[:5])
        print('value differences:',len(diff),diff[:8])
        nz=[k for k in table if table[k]!=[0]]; print('nonzero:',len(nz),' all multiples of 48:',all(v%48==0 for k in table for v in table[k]))
    if m==2:
        for k,v in sorted(table.items()): 
            if v!=[0]: print(k,v)
    json.dump(table,open('table_m%d.json'%m,'w'),indent=0)
