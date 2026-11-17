import sys, pickle, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
import lp
task=sys.argv[1]; out=sys.argv[2]
m=pickle.load(open(task,'rb'))
t=time.time(); J=lp.J(m['word']); dt=time.time()-t
pickle.dump(dict(Jlp=J,tJ=dt),open(out+'.tmp','wb'))
import os; os.replace(out+'.tmp',out)
