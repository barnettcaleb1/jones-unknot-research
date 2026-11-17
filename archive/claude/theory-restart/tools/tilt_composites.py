"""Composite strong inversions: concatenate two symmetric half-diagram words (equivariant connected sum along the axis),
compute Khr of the quotient tangle with kht++, record components.  usage: python3 tilt_composites.py MAXCROSSINGS OUT.jsonl"""
import json, subprocess, re, os, sys, itertools, time
K='/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/src/khtpp/kht++'
W='/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/comp'
ANSI=re.compile(r'\x1b\[[0-9;]*[A-Za-z]')
LINE=re.compile(r'^\s*\d+\)\s+h\^\s*(-?\d+)\s+q\^\s*(-?\d+)\s+δ\^\s*(-?[\d/]+)\s+(\S.*?)\s{3,}(r|s)(\d*)\(([^)]*)\)\s+q\^(-?[\d/]+)\s+δ[_|]\^(-?[\d/]+)\s*$')
def fr(s):
    if '/' in s: a,b=s.split('/'); return int(a)/int(b)
    return float(int(s))
def mirror(word): return word.replace('x','X').replace('y','x').replace('X','y')
def main():
    maxc=int(sys.argv[1]); out=sys.argv[2]
    d=json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/lit/kwz-inversions/data.json'))
    words=[]
    for x in d['inversions']:
        if x['crossings']>maxc: continue
        w=x['khtpp']['input'][1]
        if not w.startswith('s.'): continue
        body=w[2:]
        words.append((x['name'],body)); words.append((x['name']+'m',mirror(body)))
    os.makedirs(os.path.join(W,'examples/comp'),exist_ok=True)
    done=set()
    if os.path.exists(out):
        for l in open(out):
            try: done.add(json.loads(l)['file'])
            except Exception: pass
    fo=open(out,'a')
    for (n1,w1),(n2,w2) in itertools.combinations_with_replacement(words,2):
        name=(n1+'_'+n2).replace('^','i')
        if name in done: continue
        f='examples/comp/%s.kht'%name
        open(os.path.join(W,f),'w').write('%% %s # %s\ns.%s.%s\n,1\n'%(n1,n2,w1,w2))
        t0=time.time(); rec={'file':name}
        try:
            r=subprocess.run([K,'-c2','-q','-s',f],cwd=W,capture_output=True,text=True,timeout=240,stdin=subprocess.DEVNULL)
            txt=ANSI.sub('',r.stdout+r.stderr)
            rec['khr']=[{'type':m.group(5),'len':m.group(6),'slope':m.group(7),'q':fr(m.group(8)),'delta':fr(m.group(9))} for m in (LINE.match(l) for l in txt.splitlines()) if m]
            if not rec['khr']: rec['error']='no components'; rec['tail']=txt[-300:]
        except subprocess.TimeoutExpired:
            rec['error']='timeout'
        rec['time']=round(time.time()-t0,1)
        fo.write(json.dumps(rec,ensure_ascii=False)+'\n'); fo.flush()
    fo.close()
if __name__=='__main__': main()
