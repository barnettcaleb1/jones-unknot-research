import sys,re,html
s=open(sys.argv[1]).read()
n=int(sys.argv[2]) if len(sys.argv)>2 else 500
for e in re.findall(r'<entry>(.*?)</entry>',s,re.S):
    g=lambda t: html.unescape(re.sub(r'\s+',' ',re.search(r'<%s[^>]*>(.*?)</%s>'%(t,t),e,re.S).group(1))).strip()
    j=re.search(r'<arxiv:journal_ref[^>]*>(.*?)<',e,re.S)
    print(g('id').split('/abs/')[-1], g('published')[:10], '|', ', '.join(re.findall(r'<name>(.*?)</name>',e))[:70], '|', g('title'), '|', j.group(1) if j else '')
    if n: print('    ', g('summary')[:n])
