import re, sys, html
def page_text(path):
    s = open(path, encoding='utf-8', errors='replace').read()
    i = s.find('<body'); s = s[i:] if i >= 0 else s
    s = re.sub(r'<br\s*/?>', '\n', s)
    s = re.sub(r'</?[A-Za-z!][^>]*>', '', s, flags=re.S)
    s = html.unescape(s).replace('\xa0', ' ')
    return '\n'.join(l.rstrip() for l in s.splitlines() if l.strip())
if __name__ == '__main__':
    print(page_text(sys.argv[1]))
