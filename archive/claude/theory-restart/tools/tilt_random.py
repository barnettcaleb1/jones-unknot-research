"""Random symmetric half-diagrams: a bounded search for quotient tangles with longer special components, and a further
stress test of TILT/OVERHANG.  usage: python3 tilt_random.py SEED COUNT MINLEN MAXLEN OUT.jsonl
Words: s.<cap>.<letters>.<cup>, cap in {l1,r1}, letters over {x0,y0,x1,y1,x2,y2} (three strands), cup in {u1,u2}; plus a
second family with an extra cap/cup pair (five strands) modelled on the 9_46 input."""
import json, subprocess, re, os, sys, random, time
K='/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/src/khtpp/kht++'
W='/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/rand'
ANSI=re.compile(r'\x1b\[[0-9;]*[A-Za-z]')
LINE=re.compile(r'^\s*\d+\)\s+h\^\s*(-?\d+)\s+q\^\s*(-?\d+)\s+δ\^\s*(-?[\d/]+)\s+(\S.*?)\s{3,}(r|s)(\d*)\(([^)]*)\)\s+q\^(-?[\d/]+)\s+δ[_|]\^(-?[\d/]+)\s*$')
BNLINE=re.compile(r'^\s*\d+\)\s+h\^\s*(-?\d+)\s+q\^\s*(-?\d+)\s+δ\^\s*(-?[\d/]+)\s+(\S.*)$')
def fr(s):
    if '/' in s: a,b=s.split('/'); return int(a)/int(b)
    return float(int(s))
def reduced(word):
    # drop immediately cancelling pairs x_i y_i / y_i x_i
    out=[]
    for l in word:
        if out and out[-1][1:]==l[1:] and out[-1][0]!=l[0]: out.pop()
        else: out.append(l)
    return out
def main():
    seed,count,lo,hi,outp=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),sys.argv[5]
    rnd=random.Random(seed); os.makedirs(os.path.join(W,'examples/rand'),exist_ok=True)
    done=set()
    if os.path.exists(outp):
        for l in open(outp):
            try: done.add(json.loads(l)['word'])
            except Exception: pass
    fo=open(outp,'a'); n=0; tries=0
    while n<count and tries<count*40:
        tries+=1
        L=rnd.randint(lo,hi)
        if rnd.random()<0.8:
            w=reduced([rnd.choice('xy')+str(rnd.choice([0,1,2])) for _ in range(L)])
            if len(w)<lo: continue
            word='s.'+rnd.choice(['l1','r1'])+'.'+'.'.join(w)+'.'+rnd.choice(['u1','u2'])
        else:
            a=reduced([rnd.choice('xy')+str(rnd.choice([0,1,2])) for _ in range(rnd.randint(1,L//2+1))])
            b=reduced([rnd.choice('xy')+str(rnd.choice([0,1,2,3,4])) for _ in range(rnd.randint(2,L//2+2))])
            c=reduced([rnd.choice('xy')+str(rnd.choice([0,1,2])) for _ in range(rnd.randint(0,L//2))])
            if not a or not b: continue
            word='s.'+rnd.choice(['l1','r1'])+'.'+'.'.join(a)+'.'+rnd.choice(['l1','r1','l2','r2','l3','r3'])+'.'+'.'.join(b)+'.'+rnd.choice(['u1','u2','u3'])+('.'+'.'.join(c) if c else '')+'.'+rnd.choice(['u1','u2'])
        if word in done: continue
        done.add(word)
        name='w%d_%d'%(seed,tries); f='examples/rand/%s.kht'%name
        open(os.path.join(W,f),'w').write('%% random\n%s\n,1\n'%word)
        t0=time.time(); rec={'word':word,'file':name}
        try:
            r=subprocess.run([K,'-c2','-q','-s',f],cwd=W,capture_output=True,text=True,timeout=90,stdin=subprocess.DEVNULL)
            txt=ANSI.sub('',r.stdout+r.stderr); khr=[]; bn=[]
            for l in txt.splitlines():
                m=LINE.match(l)
                if m: khr.append({'type':m.group(5),'len':m.group(6),'slope':m.group(7),'q':fr(m.group(8)),'delta':fr(m.group(9))})
                else:
                    m2=BNLINE.match(l)
                    if m2: bn.append({'h':int(m2.group(1)),'q':int(m2.group(2)),'delta':fr(m2.group(3)),'cyclic':m2.group(4).rstrip().endswith(('<—','—>','~>','<~'))})
            rec['khr']=khr; rec['bn']=bn
            if not khr: rec['error']='no components'; rec['tail']=txt[-200:]
        except subprocess.TimeoutExpired:
            rec['error']='timeout'
        rec['time']=round(time.time()-t0,1)
        if rec.get('khr') and any(c['type']=='s' for c in rec['khr']): n+=1
        fo.write(json.dumps(rec,ensure_ascii=False)+'\n'); fo.flush()
    fo.close()
if __name__=='__main__': main()
