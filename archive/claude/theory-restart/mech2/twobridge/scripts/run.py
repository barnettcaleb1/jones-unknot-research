#!/usr/bin/env python3
"""Run kht++ (quotient mode) on half-diagram words, cache results, parse BN~ into lattice data.
usage: run.py [-t TIMEOUT] word1 word2 ...      (words like s.l1.y0.y0.x1.u2;  shorthand: 'Y2X1' -> s.l1.y0.y0.x1.u2, 'y'/'x' lower = opposite sign)
Lattice: generator = rho + a D + b P,  D=(1,2), P=(5,8) in (h,q):  b = h - q/2,  a = 5q/2 - 4h  (relative to rho)."""
import os,sys,re,json,subprocess,hashlib,collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import chain
K='/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/src/khtpp/kht++'
W='/Users/calebbarnett/jones-lanes/theory-restart/mech2/twobridge/work'
CACHE=os.path.join(W,'cache.json')
def expand(sh):
    """shorthand: sequence of letters Y,y (axis crossing y0 / x0), X,x (side crossing x1 / y1) with exponents; e.g. Y2X1y3"""
    if sh.startswith('s.'): return sh
    out=['s','l1']
    for m in re.finditer(r'([YyXx])(\d*)',sh):
        n=int(m.group(2)) if m.group(2) else 1
        tok={'Y':'y0','y':'x0','X':'x1','x':'y1'}[m.group(1)]
        out+=[tok]*n
    out.append('u2')
    return '.'.join(out)
def load():
    try: return json.load(open(CACHE))
    except: return {}
def run(word,timeout=120,field='2',cache=True):
    word=expand(word)
    C=load() if cache else {}
    key=word+'|c'+field
    if key in C: return C[key]
    name='w'+hashlib.md5(word.encode()).hexdigest()[:10]
    os.makedirs(os.path.join(W,'examples/words'),exist_ok=True)
    f='examples/words/%s.kht'%name
    open(os.path.join(W,f),'w').write('%% %s\n%s\n,1\n'%(word,word))
    rec={'word':word,'file':name}
    try:
        r=subprocess.run(['perl','-e','alarm %d; exec @ARGV'%timeout,K,'-c'+field,'-q','-s',f],cwd=W,capture_output=True,text=True,stdin=subprocess.DEVNULL)
        d=os.path.join(W,'examples/words',name)
        p=os.path.join(d,'cxBNr-c%s-qs'%field)
        rec['bn']=[l for l in open(p,encoding='utf-8').read().splitlines() if not l.startswith('%')] if os.path.exists(p) else None
        p=os.path.join(d,'cxKhr-c%s-qs'%field)
        rec['kh']=[re.sub(r'\x1b\[[0-9;]*[A-Za-z]','',l) for l in open(p,encoding='utf-8').read().splitlines() if not l.startswith('%')] if os.path.exists(p) else None
        if rec['bn'] is None: rec['error']=(r.stdout+r.stderr)[-300:]
    except Exception as e:
        rec['error']=str(e)
    if cache and rec.get('bn') is not None:
        C=load(); C[key]=rec; json.dump(C,open(CACHE,'w'),ensure_ascii=False)
    return rec
def analyse(rec):
    comps=[chain.parse_line(l) for l in rec['bn']]
    comps=[c for c in comps if c]
    arcs=[c for c in comps if not c['cyclic']]; cyc=[c for c in comps if c['cyclic']]
    assert len(arcs)==1
    arc=arcs[0]
    bg,mv=chain.bmoves(arc)
    moves=[('+' if d>0 else '-' if d<0 else '?')+chain.short(l) for d,l in mv]
    # rho = b-generator of the arc not in a P-pair; x0 = not in a D-pair
    inP=set(); inD=set()
    for i,m in enumerate(moves):
        if m[1]=='P': inP|={i,i+1}
        if m[1]=='D': inD|={i,i+1}
    rho=[i for i in range(len(bg)) if i not in inP]; x0=[i for i in range(len(bg)) if i not in inD]
    r=bg[rho[0]] if len(rho)==1 else bg[-1]
    def ab(g):
        h,q=g[1]-r[1],g[2]-r[2]
        assert q%2==0
        return (5*q//2-4*h, h-q//2)
    # tail: c-generators at the end(s) of the arc
    gens=arc['gens']; bidx=[i for i,g in enumerate(gens) if g[0]=='b']
    tail=(bidx[0],len(gens)-1-bidx[-1])
    out=dict(word=rec['word'],arc=[ab(g) for g in bg],moves=moves,tail=tail,rho_ok=(len(rho)==1),x0=[ab(bg[i]) for i in x0],
             squares=[],other=[],rho_hq=(r[1],r[2]))
    for c in cyc:
        g2,m2=chain.bmoves(c)
        ms=[('+' if d>0 else '-' if d<0 else '?')+chain.short(l) for d,l in m2]
        pts=[ab(g) for g in g2]
        if len(pts)==4 and len(set(pts))==4 and max(p[0] for p in pts)-min(p[0] for p in pts)==1 and max(p[1] for p in pts)-min(p[1] for p in pts)==1:
            out['squares'].append((min(p[0] for p in pts),min(p[1] for p in pts)))
        else: out['other'].append((pts,ms))
    out['N']=out['arc']+[(a+i,b+j) for (a,b) in out['squares'] for i in (0,1) for j in (0,1)]+[p for pts,ms in out['other'] for p in pts]
    return out
def grid(an,mark=True):
    S=collections.Counter(an['N'])
    A=[a for a,b in S]; Bs=[b for a,b in S]
    lines=[]
    for b in range(max(Bs),min(Bs)-1,-1):
        row=''
        for a in range(min(A),max(A)+1):
            c=S.get((a,b),0)
            cell=('%d'%c if c<10 else '+') if c else '.'
            row+=cell+('*' if (a,b)==(0,0) else ' ')
        lines.append('b=%3d  %s'%(b,row))
    lines.append('       a from %d to %d'%(min(A),max(A)))
    return '\n'.join(lines)
def Jpoly(an):
    """J = sum (-t)^a (-t^4)^b as dict exponent->coeff"""
    J=collections.Counter()
    for a,b in an['N']: J[a+4*b]+=(-1)**(a+b)
    return {e:c for e,c in sorted(J.items()) if c}
if __name__=='__main__':
    args=sys.argv[1:]; timeout=120
    if args and args[0]=='-t': timeout=int(args[1]); args=args[2:]
    for w in args:
        rec=run(w,timeout)
        if rec.get('bn') is None: print(w,'ERROR',rec.get('error')); continue
        an=analyse(rec)
        print('== %s  [%s]  dimN=%d  arc: %d gens, moves %s, c-tail %s  squares at %s %s'%(w,rec['word'],len(an['N']),len(an['arc']),' '.join(an['moves']),an['tail'],sorted(an['squares']),('OTHER:'+str(an['other'])) if an['other'] else ''))
        print(grid(an))
        print('   J =',Jpoly(an),'  kh:',[re.sub(r'^.*?((r|s)\d*\([^)]*\).*)$',r'\1',l).strip() for l in (rec['kh'] or [])])
