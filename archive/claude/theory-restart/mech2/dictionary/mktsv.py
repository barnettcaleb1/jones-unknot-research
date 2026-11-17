import json,collections
T=json.load(open('table.json')); A=json.load(open('alex.json')); M=json.load(open('more.json'))
out=open('table.tsv','w')
cols=['name','k','j','dimN','l_s','N_staircase_gens','N_squares','s_sq','levels','bmin','bmax','s(K)','sigma(K)','det','a2','rankHFK','CFK_staircase_gens','CFK_boxes','mu1','k=4mu1','j=Arf mod2','squares(a,b)']
out.write('\t'.join(cols)+'\n')
nbad=0
for a in T:
    if 'err' in a:
        out.write(a['name']+'\t(not parsed: '+a['err']+')\n'); continue
    al=A[a['name'].replace('^','-')]['alex']; n=len(al); mid=(n-1)//2
    a2=sum(c*(i-mid)**2 for i,c in enumerate(al))//2
    det=abs(sum(c*(-1)**i for i,c in enumerate(al)))
    sig=a['sigma']; s=a['s']
    base=a['name'].split('^')[0]
    if base=='8_19': rk=5; cst=5; cbx=0; mu1=2
    elif base=='9_42': rk=9; cst=1; cbx=2; mu1=0
    else:
        rk=det; cst=abs(sig)+1; cbx=(det-abs(sig)-1)//4; mu1=-sig//2
    steps=a['steps']; l=len(steps)//2
    ls= l if (steps and steps[0]==[1,0]) else -l
    if a['dDpow']: ls='exc'
    lev=sorted(set(b for (x,b) in a['L']))
    ssq=sum((-1)**(b%2) for (x,b) in a['squares'])
    ok1=(a['k']==4*mu1); arf=0 if det%8 in (1,7) else 1; ok2=((a['j']-arf)%2==0)
    if not ok1: nbad+=1
    row=[a['name'],a['k'],a['j'],a['dim'],ls,2*l+1,len(a['squares']),ssq,len(lev),lev[0],lev[-1],s,sig,det,a2,rk,cst,cbx,mu1,ok1,ok2,' '.join('(%d,%d)'%tuple(x) for x in a['squares'])]
    out.write('\t'.join(str(x) for x in row)+'\n')
out.write('\n# doubled tangles T_K (K two-bridge k<p>_<q>): name k j dimN staircase_gens squares\n')
for r in M['doubles']:
    out.write('\t'.join(str(x) for x in [r['name'],r['k'],r['j'],r['dim'],len(r['path']),len(r['squares'])])+'\n')
out.close()
print('k != 4 mu1 in',nbad,'rows (expected 1: 9_46^2)')
