import re, sys, os, json
from fractions import Fraction
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from page2txt import page_text

GEN = '⬮⬯'
def parse_chain(body):
    """body: string like '⬯~~S~>⬮—>⬮<—⬯<~⬮<—'  -> (gens, arrows, cyclic)
    arrows[i] = (src_index, dst_index, letter, power) connecting gen i and gen i+1 (mod n if cyclic)"""
    body = body.strip()
    gens = []; arrows = []
    pos = 0; n = len(body)
    pending = None
    toks = []
    i = 0
    while i < n:
        ch = body[i]
        if ch in GEN:
            toks.append(('g', ch)); i += 1
        else:
            j = i
            while j < n and body[j] not in GEN: j += 1
            toks.append(('a', body[i:j])); i = j
    if not toks or toks[0][0] != 'g': raise ValueError('chain must start with generator: ' + body)
    gens = [t[1] for t in toks if t[0] == 'g']
    arr_strs = [t[1] for t in toks if t[0] == 'a']
    cyclic = (toks[-1][0] == 'a')
    if len(arr_strs) != len(gens) - (0 if cyclic else 1): raise ValueError('bad alternation: ' + body)
    for idx, a in enumerate(arr_strs):
        left, right = idx, (idx + 1) % len(gens)
        a0 = a.strip()
        if a0.endswith('>') and not a0.startswith('<'): direction = 'r'
        elif a0.startswith('<') and not a0.endswith('>'): direction = 'l'
        else: raise ValueError('arrow direction? %r in %s' % (a, body))
        core = a0.strip('<>')
        kind = None
        if '—' in core and '~' not in core: kind = 'D'
        elif '~' in core and '—' not in core: kind = 'S'
        else: raise ValueError('arrow kind? %r' % a)
        label = core.replace('—', '').replace('~', '').strip()
        if label:
            m = re.search(r'([DS])(?:\^(\d+))?', label)
            if not m: raise ValueError('label? %r' % a)
            letter = m.group(1); power = int(m.group(2) or 1)
            if letter != kind: raise ValueError('label/kind mismatch %r' % a)
        else:
            letter = kind
            if kind == 'D': power = 1
            else: power = 1 if gens[left] != gens[right] else 2
        # consistency: S^odd changes idempotent, D^n and S^even preserve
        same = gens[left] == gens[right]
        if letter == 'D' and not same: raise ValueError('D between different idempotents: ' + body)
        if letter == 'S' and (power % 2 == 0) != same: raise ValueError('S parity mismatch: %r in %s' % (a, body))
        src, dst = (left, right) if direction == 'r' else (right, left)
        arrows.append((src, dst, letter, power, label))
    return gens, arrows, cyclic

def gradings(gens, arrows, cyclic, h0, q0):
    """h, q of every generator; first generator has (h0,q0). q(dst)=q(src)+ (2n for D^n, m for S^m), h(dst)=h(src)+1"""
    n = len(gens)
    h = [None]*n; q = [None]*n
    h[0], q[0] = h0, q0
    for idx, (src, dst, letter, power, label) in enumerate(arrows):
        left, right = idx, (idx + 1) % n
        dq = 2*power if letter == 'D' else power
        if cyclic and idx == n - 1:
            # closing arrow: check consistency
            if src == left: ok = (h[right] == h[left] + 1 and q[right] == q[left] + dq)
            else: ok = (h[left] == h[right] + 1 and q[left] == q[right] + dq)
            if not ok: raise ValueError('cyclic grading inconsistency')
            continue
        if src == left: h[right] = h[left] + 1; q[right] = q[left] + dq
        else: h[right] = h[left] - 1; q[right] = q[left] - dq
    return h, q

LINE = re.compile(r'^\s*(\d+)\)\s*h\^\s*(-?\d+)\s+q\^\s*(-?\d+)\s+δ\^\s*(-?\d+(?:/\d+)?)\s+(\S+)(?:\s+(.*))?$')
DESC = re.compile(r'^(r|s)(\d*)\((-?\d+|∞)(?:/(-?\d+))?\)\s+q\^(-?\d+(?:/\d+)?)\s+δ([|_])\^(-?\d+(?:/\d+)?)')

def parse_component_line(line):
    m = LINE.match(line)
    if not m: return None
    num, h0, q0, d0, body, desc = m.groups()
    h0 = int(h0); q0 = int(q0); d0 = Fraction(d0)
    if Fraction(q0, 2) - h0 != d0: raise ValueError('delta mismatch in line: ' + line)
    gens, arrows, cyclic = parse_chain(body)
    h, q = gradings(gens, arrows, cyclic, h0, q0)
    comp = dict(index=int(num), first_generator=dict(h=h0, q=q0, delta=str(d0)), chain=body, compact=cyclic,
                n_generators=len(gens),
                generators=[dict(idem=('B' if g == '⬮' else 'W'), h=hh, q=qq) for g, hh, qq in zip(gens, h, q)],
                arrows=[dict(src=a[0], dst=a[1], letter=a[2], power=a[3]) for a in arrows])
    if desc:
        dm = DESC.match(desc.strip())
        if dm:
            typ, length, p, qd, qavg, which, dval = dm.groups()
            comp['recognized'] = dict(type=('rational' if typ == 'r' else 'special'), length=int(length or 1),
                                      khtpp_slope=('1/0' if p == '∞' else p + ('/' + qd if qd else '/1')), q_average=qavg, delta_kind=('vertical' if which == '|' else 'horizontal'), delta=dval, raw=desc.strip())
        else:
            comp['recognized'] = dict(raw=desc.strip())
    return comp

def parse_page(path):
    txt = page_text(path)
    lines = txt.splitlines()
    out = dict(input=[], sections={})
    sec = None; opt = None; in_input = False
    for ln in lines:
        s = ln.strip()
        if s.startswith('Input data and context'): in_input = True; continue
        if s.startswith('Bar-Natan multicurve'): sec = 'BNr'; in_input = False; continue
        if s.startswith('Khovanov multicurve'): sec = 'Khr'; in_input = False; continue
        if s.startswith('Khovanov type D structure'): sec = 'CKh'; in_input = False; continue
        if in_input: out['input'].append(s); continue
        if sec is None: continue
        m = re.match(r'^options\s+(\S+)', s)
        if m: opt = m.group(1); out['sections'].setdefault(sec, {}).setdefault(opt, dict(meta=None, components=[], unparsed=[])); continue
        if opt is None: continue
        blk = out['sections'][sec][opt]
        if s.startswith('% file'): blk['meta'] = s; continue
        if re.match(r'^\d+\)', s):
            if sec == 'CKh': blk['components'].append(s); continue
            try:
                c = parse_component_line(s)
                if c is None: blk['unparsed'].append(s)
                else: blk['components'].append(c)
            except Exception as e:
                blk['unparsed'].append(s + '   [ERR ' + str(e) + ']')
    return out

if __name__ == '__main__':
    p = parse_page(sys.argv[1])
    print('\n'.join(p['input'][:6]))
    for sec in ('BNr', 'Khr'):
        for opt, blk in p['sections'].get(sec, {}).items():
            if not opt.startswith('-c2'): continue
            print(sec, opt, blk['meta'])
            for c in blk['components']:
                print('  ', c['index'], 'compact' if c['compact'] else 'ARC', c['n_generators'], 'gens', c.get('recognized', {}).get('raw'), [(g['idem'], g['h'], g['q']) for g in c['generators']][:14])
            for u in blk['unparsed']: print('   UNPARSED', u)
