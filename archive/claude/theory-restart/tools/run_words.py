#!/usr/bin/env python3
"""Run kht++ quotient mode on a list of half-diagram words. usage: run_words.py WORKDIR OUT.jsonl TIMEOUT word1 word2 ...
(or words from stdin, one per line).  Stores khr (Kh~ components), raw BN~ chains and raw Kh~ lines."""
import json, subprocess, re, os, sys, time, hashlib
K='/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/src/khtpp/kht++'
ANSI=re.compile(r'\x1b\[[0-9;]*[A-Za-z]')
LINE=re.compile(r'^\s*\d+\)\s+h\^\s*(-?\d+)\s+q\^\s*(-?\d+)\s+δ\^\s*(-?[\d/]+)\s+(\S.*?)\s{3,}(r|s)(\d*)\(([^)]*)\)\s+q\^(-?[\d/]+)\s+δ[_|]\^(-?[\d/]+)\s*$')
def fr(s):
    if '/' in s: a,b=s.split('/'); return int(a)/int(b)
    return float(int(s))
def run(W,word,timeout,field='2'):
    name='w'+hashlib.md5(word.encode()).hexdigest()[:10]
    os.makedirs(os.path.join(W,'examples/words'),exist_ok=True)
    f='examples/words/%s.kht'%name
    open(os.path.join(W,f),'w').write('%% %s\n%s\n,1\n'%(word,word))
    rec={'word':word,'file':name}; t0=time.time()
    try:
        r=subprocess.run([K,'-c'+field,'-q','-s',f],cwd=W,capture_output=True,text=True,timeout=timeout,stdin=subprocess.DEVNULL)
        d=os.path.join(W,'examples/words',name)
        khr=[]; khlines=[]
        p=os.path.join(d,'cxKhr-c%s-qs'%field)
        if os.path.exists(p):
            for l in open(p).read().splitlines()[1:]:
                l=ANSI.sub('',l); khlines.append(l)
                m=LINE.match(l)
                if m: khr.append({'type':m.group(5),'len':m.group(6),'slope':m.group(7),'q':fr(m.group(8)),'delta':fr(m.group(9))})
        rec['khr']=khr
        p=os.path.join(d,'cxBNr-c%s-qs'%field)
        rec['bnchains']=open(p).read().splitlines()[1:] if os.path.exists(p) else []
        if not khr: rec['error']='no components'; rec['tail']=ANSI.sub('',r.stdout+r.stderr)[-300:]
    except subprocess.TimeoutExpired:
        rec['error']='timeout'
    rec['time']=round(time.time()-t0,1)
    return rec
if __name__=='__main__':
    W,outp,timeout=sys.argv[1],sys.argv[2],int(sys.argv[3])
    words=sys.argv[4:] or [l.strip().split('\t')[0] for l in sys.stdin if l.strip()]
    fo=open(outp,'a')
    for w in words:
        rec=run(W,w,timeout)
        fo.write(json.dumps(rec,ensure_ascii=False)+'\n'); fo.flush()
        print(w,rec.get('error','ok'),rec['time'],len(rec.get('khr',[])),flush=True)
