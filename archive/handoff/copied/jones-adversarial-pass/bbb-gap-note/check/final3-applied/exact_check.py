import json, re, difflib, sys
root = '$HOME/jones-adversarial-pass/bbb-gap-note/'
src = open(root + 'check/final-review-results.md', encoding='utf-8').read()
blocks = re.findall(r'```json\n(.*?)\n```', src, re.S)
V = [v for b in blocks for v in json.loads(b)['verdicts']]
tex = open(root + 'note/bbb-gap-note.tex', encoding='utf-8').read()
email = open(root + 'EMAIL.md', encoding='utf-8').read()
readme = open(root + 'README.md', encoding='utf-8').read()

def show(label, want, have_doc):
    if want in have_doc:
        print(f'[{label}] EXACT'); return
    # find best matching window
    sm = difflib.SequenceMatcher(None, have_doc, want, autojunk=False)
    m = sm.find_longest_match(0, len(have_doc), 0, len(want))
    start = max(0, m.a - m.b - 20); seg = have_doc[start:start + len(want) + 200]
    print(f'[{label}] NOT EXACT; word diff:')
    a, b = want.split(), seg.split()
    for op in difflib.ndiff(a, b[:len(a) + 30]):
        if op[0] in '+-': print('   ', op)
    print()

# C3 appendix paragraph
rc = V[11]['required_change']
want = rc[rc.index('All computations are exact'):rc.index('In each of these conventions:') + len('In each of these conventions:')]
show('C3 appendix', want, tex)
# C2 Prop 4(b)
rc = V[10]['required_change']
want = rc[rc.index('(b) In the conventions'):rc.index('so $\\rho_4(X)\\at=I$.') + len('so $\\rho_4(X)\\at=I$.')]
show('C2 prop4b', want, tex)
want = rc[rc.index('\\item $\\rho_4(X)-I'):rc.index('replaced by $\\sigma_i^{-1}$.') + len('replaced by $\\sigma_i^{-1}$.')]
show('C2 bullet4', want, tex)
# C1 bullet 2
rc = V[9]['required_change']
want = rc[rc.index('\\item $\\rho_4(\\Phi_0)\\neq I'):rc.index('$\\rho_5(f(\\Phi_0))$;') + len('$\\rho_5(f(\\Phi_0))$;')]
show('C1 bullet2', want, tex)
# H3
rc = V[2]['required_change']
want = rc[rc.index("'Proposition~") + 1:rc.index("route to it through Proposition 6.7.'") + len("route to it through Proposition 6.7.")]
show('H3', want, tex)
# H4
rc = V[3]['required_change']
want = rc[rc.index("'Minimal position") + 1:rc.index("without Proposition 5.1.'") + len('without Proposition 5.1.')]
show('H4', want, tex)
# R2
rc = V[6]['required_change']
want = rc[rc.index("with 'Moreover, the proof takes") + 6:rc.index("as $\\Gamma$ is.'") + len('as $\\Gamma$ is.')]
show('R2', want, tex)
# R4
rc = V[8]['required_change']
want = rc[rc.index("with 'so they are homotopic") + 6:rc.index("a contradiction.' Do not") + len('a contradiction.')]
show('R4', want, tex)
# R3
rc = V[7]['required_change']
want = rc[rc.index("'In particular") + 1:rc.index("contrary to Proposition~\\ref{prop:main}.'") + len('contrary to Proposition~\\ref{prop:main}.')]
show('R3', want, tex)
# H2 first sentence
rc = V[1]['required_change']
want = rc[rc.index("with 'The proof states") + 6:rc.index("modulo 4-disks.' (keep") + len('modulo 4-disks.')]
show('H2a', want, tex)
want = rc[rc.index("with 'if Lemma 6.4 holds, the disk") + 6:rc.index("fails for $\\Gamma'$.'") + len("fails for $\\Gamma'$.")]
show('H2b', want, tex)
# H5
rc = V[4]['required_change']
want = rc[rc.index("with 'So a version") + 6:rc.index("is one such statistic.'") + len('is one such statistic.')]
show('H5', want, tex)
# H1 abstract
rc = V[0]['required_change']
want = rc[rc.index("with 'Consequently") + 6:rc.index("with $\\rho_4(\\Phi_0)\\at=I$.' (2)") + len('with $\\rho_4(\\Phi_0)\\at=I$.')]
show('H1 abstract', want, tex)
want = rc[rc.index("with 'So Proposition 6.7 can't hold for a proper product that is trivial at t = -1. If") + 6:rc.index("trivial at t = -1.' (4)") + len('trivial at t = -1.')]
show('H1 email', want, email)
# P1 email line 7
rc = V[12]['required_change']
want = rc[rc.index("'I've been going") + 1:rc.index("runs it without renaming.'") + len('runs it without renaming.')]
show('P1 email', want, email)
# P5 README
rc = V[16]['required_change']
want = rc[rc.index("with: 'Checked by six") + 7:rc.index("coprimality step in Remark 5.'") + len('coprimality step in Remark 5.')]
show('P5 readme', want, readme)
# P4 README
rc = V[15]['required_change']
want = rc[rc.index("row: 'Python 3") + 6:rc.index("(44 PASS, 0 FAIL).'") + len('(44 PASS, 0 FAIL).')]
show('P4 readme', want, readme)
