import sys; sys.argv=['x']
src=open('$HOME/jones-lanes/theory-restart/mont/ft/proof/osp12.py').read().split("lam,mu=sp.symbols")[0]
exec(src)
a,b,c=sp.symbols('a b c')
print(sp.solve(list(Om-(a*sp.eye(9)+b*P+c*K)),[a,b,c],dict=True))
# alternative dual convention: str(x^b x_c) = delta
Om2=sum((tens(dual[a_][0],dual[a_][1],bas[a_][0],bas[a_][1]) for a_ in range(len(bas))),sp.zeros(9,9))
print('alt:',sp.solve(list(Om2-(a*sp.eye(9)+b*P+c*K)),[a,b,c],dict=True))
# sign-twisted dual: x^b with (-1)^{|b|}
Om3=sum((tens(bas[a_][0],bas[a_][1],(-1)**bas[a_][1]*dual[a_][0],dual[a_][1]) for a_ in range(len(bas))),sp.zeros(9,9))
print('twisted:',sp.solve(list(Om3-(a*sp.eye(9)+b*P+c*K)),[a,b,c],dict=True))
