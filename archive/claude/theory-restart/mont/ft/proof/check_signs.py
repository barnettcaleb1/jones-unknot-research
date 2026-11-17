# n_i (normalisation increment, = W_1 of the exact evaluation) versus the upstairs crossing sign from alex.writhe, and
# versus lp's k-increment. Also the sheet label tau versus the upstairs lift (computed independently from the full diagram).
import sys, random
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/proof')
import symbol as sy, lp, alex, flat_search as fs
rnd=random.Random(int(sys.argv[1])); agree={}; kinc={'ok':0,'bad':0}; done=0
def normk(J):
    s=sum(c*(-1)**(e%2) for e,c in J.items()); d=sum(e*c*(-1)**((e-1)%2) for e,c in J.items()); return d//s
while done<int(sys.argv[2]):
    w=fs.gen(rnd,rnd.randint(8,16))
    if not w or lp.J(w) is None: continue
    toks=w.split('.')
    fl=[i for i,a in enumerate(toks) if len(a)>=2 and a[0] in 'xy' and a[1:].isdigit()]
    if not fl: continue
    done+=1
    recs,L,axp=sy.chord_data(w,fl)
    w0=alex.writhe(w); k0=normk(lp.J_raw(w))
    for r,n in zip(recs,fl):
        wf=sy.flip(toks,[n]); dw=w0-alex.writhe(wf)
        ncr=1 if r['kind']=='on' else 2
        eps_alex=dw//(2*ncr)
        nI=sy.W_hat(L,[r],axp,[1])
        eps=nI//4
        key=r['kind']; agree.setdefault(key,{}); agree[key][eps*eps_alex]=agree[key].get(eps*eps_alex,0)+1
        dk=normk(lp.J_raw(wf))-k0
        kinc['ok' if dk==nI else 'bad']+=1
print('n_i/4 * (alex upstairs crossing sign), by site type:',agree)
print('n_i == lp k-increment:',kinc)
