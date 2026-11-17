"""Test TILT+ : actual special components plus the 'virtual specials' carried by the rational component r_1(k).

Labels as printed by kht++ for Khr(T): r(k) q^{qr} delta|^{dr};  s4(inf) q^{c} delta_^{d}.
 j        = (qr - k(|k|+2)/(|k|+1)) / 24            (must be an integer)
 sign of a special at (c, d) = (-1)^(c/2 - d)
 virtual specials (from the flatness equation  P_kappa = q^{24j+4} [k/4]_{q^8}):
   k > 0: offsets 24j+4+8i, i = 0..k/4-1, sign -, level = the ODD  integer among dr -+ 1/2
   k < 0: offsets 24j+4-8i, i = 1..|k|/4, sign +, level = the EVEN integer among dr -+ 1/2
 TILT+ : over all occupied levels (actual and virtual), levels are contiguous and both the minimum and the maximum
         offset strictly decrease as delta increases.
Consequence checked alongside: P_tot = sum of signs q^c over actual and virtual specials is nonzero.
"""
import json, sys, collections, math
def levels_from(khr):
    r=[c for c in khr if c['type']=='r']; s=[c for c in khr if c['type']=='s']
    return r, s
def analyze(records, label):
    n=0; bad_j=[]; fail=[]; ptot_zero=[]; novirt=0; gapfail=[]; odd_k=[]; notinf=[]; steps=collections.Counter()
    for name, khr in records:
        r, s = levels_from(khr)
        if len(r)!=1: fail.append((name,'rational components: %d'%len(r))); continue
        if any(c.get('slope')!='∞' or c.get('len')!='4' for c in s): notinf.append(name); continue
        k=int(r[0]['slope']); qr=r[0]['q']; dr=r[0]['delta']
        jf=(qr - k*(abs(k)+2)/(abs(k)+1))/24.0
        j=round(jf)
        if abs(jf-j)>1e-6: bad_j.append((name,k,qr,jf)); continue
        if k%4: odd_k.append((name,k)); continue
        lev=collections.defaultdict(list)
        for c in s: lev[int(round(c['delta']))].append(int(round(c['q'])))
        cand=[int(round(dr-0.5)), int(round(dr+0.5))]
        if k>0:
            dv=[d for d in cand if d%2==1][0]; virt=[24*j+4+8*i for i in range(k//4)]
        elif k<0:
            dv=[d for d in cand if d%2==0][0]; virt=[24*j+4-8*i for i in range(1,abs(k)//4+1)]
        else: dv=None; virt=[]
        ext=collections.defaultdict(list)
        for d,cs in lev.items(): ext[d]+=cs
        if virt: ext[dv]+=virt
        else: novirt+=1
        if not ext: continue
        n+=1
        ds=sorted(ext)
        ok=True
        for i in range(len(ds)-1):
            if ds[i+1]-ds[i]!=1: gapfail.append((name,ds)); ok=False; break
            dmin=min(ext[ds[i+1]])-min(ext[ds[i]]); dmax=max(ext[ds[i+1]])-max(ext[ds[i]])
            steps[(dmin,dmax)]+=1
            if not (dmin<0 and dmax<0): ok=False
        if not ok: fail.append((name,'k=%d j=%d'%(k,j),'virtual level %s offsets %s'%(dv,virt),[(d,min(ext[d]),max(ext[d]),len(ext[d])) for d in ds]))
        P=collections.Counter()
        for d,cs in ext.items():
            for c in cs: P[c]+=(-1)**((c//2 - d)%2)
        if all(v==0 for v in P.values()): ptot_zero.append(name)
    print(label)
    print("  tangles tested:",n,"| k = 0 (no virtual specials):",novirt,"| non-integer j:",len(bad_j),"| k not divisible by 4:",len(odd_k),"| specials not all s4(inf):",len(notinf))
    print("  level gaps:",len(gapfail),"| TILT+ failures:",len(fail),"| P_tot = 0:",len(ptot_zero))
    for f in fail[:8]: print("     FAIL",f)
    for b in bad_j[:5]: print("     bad j",b)
    print("  (dmin,dmax) steps:",sorted(steps.items())[:12])
def from_jsonl(path):
    out=[]
    for l in open(path):
        try: r=json.loads(l)
        except Exception: continue
        if r.get('error') or not r.get('khr'): continue
        out.append((r.get('file') or r.get('knot'), r['khr']))
    return out
def from_datajson(path):
    d=json.load(open(path)); out=[]
    import re
    for x in d['inversions']:
        rc=x['rational_component']; raw=rc['bigrading']['descriptor_raw']
        m=re.search(r'q\^(-?[\d/]+)\s+δ.\^(-?[\d/]+)', raw)
        def fr(s):
            if '/' in s: a,b=s.split('/'); return int(a)/int(b)
            return float(s)
        khr=[{'type':'r','len':'1','slope':str(rc['slope_k']),'q':fr(m.group(1)),'delta':fr(m.group(2))}]
        for sc in x['special_components']:
            for _ in range(sc.get('multiplicity',1)):
                a,b=sc['kappa_shift_h'],sc['kappa_shift_delta']
                khr.append({'type':'s','len':'4','slope':'∞','q':2*(a+b),'delta':b+0.5})
        out.append((x['name'],khr))
    return out
if __name__=='__main__':
    for p in sys.argv[1:]:
        if p.endswith('data.json'): analyze(from_datajson(p), p)
        else: analyze(from_jsonl(p), p)
