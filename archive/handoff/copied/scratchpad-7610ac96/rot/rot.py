import sys,subprocess,re,os
K='$HOME/jones-lanes/theory-restart/lit/kht/src/khtpp/kht++'
def shift(w,k):
    return [t[0]+str(int(t[1:])+k) for t in w]
def rot1(w,cap='l1'):
    return [cap]+shift(w,1)+['u0']
def run(name,w,orient='1'):
    f='examples/rot/%s.kht'%name
    open(f,'w').write('%% %s\n%s\n,%s\n'%(name,'.'.join(w),orient))
    r=subprocess.run([K,'-c2',f],capture_output=True,text=True,timeout=300,stdin=subprocess.DEVNULL)
    d='examples/rot/%s'%name
    out=[]
    for fn in sorted(os.listdir(d)) if os.path.isdir(d) else []:
        if fn.startswith('cxBNr'):
            out=open(os.path.join(d,fn)).read().splitlines()[1:]
    return out,(r.stdout+r.stderr)[-300:]
def comp(l):
    l=l.replace('⬮~~S~>⬯—>⬯~>⬯—>⬯~>⬮','⬮=P=>⬮').replace('⬮<~⬯<—⬯<~⬯<—⬯<~⬮','⬮<=P=⬮').replace('⬮<~S~~⬯<—⬯<~⬯<—⬯<~⬮','⬮<=P=⬮').replace('⬮~>⬯—>⬯~>⬯—>⬯~>⬮','⬮=P=>⬮')
    return l[:230]
if __name__=='__main__':
    name=sys.argv[1]; w=sys.argv[2].split('.')
    for label,word in [('orig',w),('rot2',rot1(rot1(w)))]:
        for orient in ['1','0']:
            out,tail=run(name+'_'+label+orient,word,orient)
            if out:
                print('==',label,'orient',orient)
                for l in out: print('  ',comp(l))
                break
        else:
            print('==',label,'FAILED',tail)
