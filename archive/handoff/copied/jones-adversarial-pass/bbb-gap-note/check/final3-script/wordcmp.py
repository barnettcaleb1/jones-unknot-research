import os, io, contextlib
here = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(here, 'indep3.py')).read()
cut = src.index('# ------------------------------------------------------------------ rings')
ns = {'__file__': os.path.join(here, 'indep3.py')}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src[:cut], 'indep3_head', 'exec'), ns)
mine = ' '.join(str(i * e) for i, e in ns['Phi0r'])
out = open(os.path.join(here, '..', '..', 'phi0_check.out')).read().splitlines()
k = out.index('freely reduced word of Phi0 (76 letters, k = s_k, -k = s_k^-1):')
print('printed word == my independently reduced word:', out[k + 1] == mine, '| letters:', len(out[k + 1].split()))
