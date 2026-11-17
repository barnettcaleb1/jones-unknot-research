#!/usr/bin/env python3
"""run kht++ -q on half-diagram words, store to OUT.jsonl; also Alexander polynomial and knot-mode s.  usage: runw.py OUT TIMEOUT word..."""
import sys,json,os,subprocess
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mech2/dictionary')
import run_words, alexall
W='/Users/calebbarnett/jones-lanes/theory-restart/mech2/dictionary/work2'
if __name__=='__main__':
    out=sys.argv[1]; timeout=int(sys.argv[2]); words=sys.argv[3:]
    fo=open(out,'a')
    for w in words:
        rec=run_words.run(W,w,timeout)
        try: rec['alex']=alexall.alex_coeffs(w)
        except Exception as e: rec['alex']=None; rec['alexerr']=repr(e)
        # knot mode
        f='examples/words/%s.kht'%rec['file']
        try:
            subprocess.run([run_words.K,'-c2','-s',f],cwd=W,capture_output=True,text=True,timeout=timeout,stdin=subprocess.DEVNULL)
            p=os.path.join(W,'examples/words',rec['file'],'cxCKh-c2-s')
            rec['ckh']=open(p).read().splitlines()[1:] if os.path.exists(p) else []
        except subprocess.TimeoutExpired: rec['ckh']=None
        fo.write(json.dumps(rec,ensure_ascii=False)+'\n'); fo.flush()
        print(w,rec.get('error','ok'),rec['time'],rec.get('alex'),flush=True)
