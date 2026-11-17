# enumerate all combinatorial equivariant chord-diagram types with m elements (canonical up to reversal) and compare
import sys, json, glob, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
import chord
def canon(pts, nT):
    # pts: list of tokens along k: ('T',rank,delta) or ('C',id,label)
    def encode(order, rev):
        cmap={}; out=[]
        for tok in order:
            if tok[0]=='T':
                r=tok[1] if not rev else nT-1-tok[1]; out.append(('T',r,tok[2]))
            else:
                if tok[1] not in cmap: cmap[tok[1]]=len(cmap)
                out.append(('C',cmap[tok[1]],tok[2]))
        return tuple(out)
    return min(encode(pts,False),encode(list(reversed(pts)),True))
def all_types(m):
    res=set()
    for nT in range(0,m+1):
        nC=m-nT; L=nT+2*nC
        # place T positions
        for Tpos in itertools.combinations(range(L),nT):
            rest=[i for i in range(L) if i not in Tpos]
            # perfect matchings of rest
            def matchings(s):
                if not s: yield []; return
                a=s[0]
                for j in range(1,len(s)):
                    for mm in matchings(s[1:j]+s[j+1:]): yield [(a,s[j])]+mm
            for mt in matchings(rest):
                for perm in itertools.permutations(range(nT)):
                    for deltas in itertools.product([1,-1],repeat=nT):
                        for labs in itertools.product([0,1],repeat=nC):
                            pts=[None]*L
                            for ti,p in enumerate(Tpos): pts[p]=('T',perm[ti],deltas[ti])
                            for ci,(a,b) in enumerate(mt): pts[a]=('C',ci,labs[ci]); pts[b]=('C',ci,labs[ci])
                            res.add(canon(pts,nT))
    return res
obs={1:set(),2:set(),3:set()}
for f in glob.glob('fast_m3_s*.json')+glob.glob('symtab_m3_*.json'):
    for r in json.load(open(f)): obs[3].add(r['type'])
for f in glob.glob('symtab_m2_*.json'):
    for r in json.load(open(f)): obs[2].add(r['type'])
for f in glob.glob('symtab_m1_*.json'):
    for r in json.load(open(f)): obs[1].add(r['type'])
for m in (1,2,3):
    T=all_types(m); names={chord.dstr(t) for t in T}
    print('m=%d theoretical types %d, observed %d, observed-not-theoretical %d'%(m,len(names),len(obs[m]&names),len(obs[m]-names)))
    missing=sorted(names-obs[m])
    print('   missing (%d):'%len(missing),' '.join(missing[:80]))
