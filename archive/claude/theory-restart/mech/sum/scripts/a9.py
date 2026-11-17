import sys,os,glob,pickle; sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mech/sum/scripts')
from chains import *
import load
from load import load_jsonl, parse, R
O=R+'lit/kht/out/'
def Jfrom_kh(p):
    j=int(p['j']); J=Counter(); J[(2*p['k'],0)]+=1
    for (c,d),m in p['S'].items():
        cc=c-24*j; dd=d-4*j   # dd = d''+1/2
        J[(cc+4,dd-1)]+=m; J[(cc-4,dd)]+=m
    return J
def Jfrom_bn(chs,j):
    J=Counter()
    for (h,q),m in dots(chs).items():
        assert q%2==0
        J[(q-24*j, q//2-h-4*j)]+=m
    return J
tests=[]
for r in load_jsonl(O+'k138/k138.jsonl'):
    tests.append((r, glob.glob(O+'k138/examples/si/%s/cxBNr-c2-q*'%r['file'].replace('^','-'))))
for r in load_jsonl(O+'comp/comp4.jsonl')+load_jsonl(O+'comp/comp5.jsonl'):
    tests.append((r, glob.glob(O+'comp/examples/comp/%s/cxBNr-c2-q*'%r['file'])))
for r in load_jsonl(O+'tilt/run_3_45.jsonl'):
    tests.append((r, glob.glob(O+'tilt/'+r['file'][:-4]+'/cxBNr-c2-q*')))
for r in load_jsonl(O+'dbl/doubles.jsonl'):
    tests.append((r, glob.glob(O+'dbl/examples/knots/2-bridge_knots/%s/cxBNr-c2-d'%r['knot'])))
ok=bad=skip=0
for r,fs in tests:
    try: p=parse(r)
    except Exception: p=None
    if p is None or not fs or p['j'].denominator!=1: skip+=1; continue
    J1=Jfrom_kh(p); J2=Jfrom_bn(read_file(fs[0]),int(p['j']))
    if J1==J2: ok+=1
    else:
        bad+=1
        if bad<6: print('MISMATCH',r.get('file') or r.get('knot'),sorted(J1.items()),sorted(J2.items()))
print('J-set from Kh specials == bigradings of • generators of BN: ok',ok,'bad',bad,'skipped',skip)
