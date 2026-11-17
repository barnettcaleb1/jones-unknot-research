"""Apply the verifier's proposed replacements to a COPY of the note and compile it.

Reads the shipped note, never writes to it. Output goes to this folder only.
"""
import pathlib
import subprocess
import sys

SRC = pathlib.Path("$HOME/jones-adversarial-pass/bbb-gap-note/note/bbb-gap-note.tex")
OUT_DIR = pathlib.Path("$HOME/jones-adversarial-pass/bbb-gap-note/check/final-verify-refute")
OUT = OUT_DIR / "proposed.tex"

text = SRC.read_text()

edits = [
    # Finding 1 (part a): make the display conditional on properties 1 and 2.
    (
        r"so the proof passes to the modified loop $\Gamma'=\gamma_1\cup\gamma_2'$. Properties 1 and 2 of $\gamma_2'$ give",
        r"so the proof passes to the modified loop $\Gamma'=\gamma_1\cup\gamma_2'$. If $\gamma_2'$ has properties 1 and 2, as the proof states, then",
    ),
    # Finding 1 (part b): "establishes ... for Gamma'" -> "states that gamma_2' has ...".
    (
        r"The proof establishes properties 1 and 2 for $\Gamma'$ but does not return to the parity condition, which Corollary 6.8 needs for the same loop.",
        r"The proof states that $\gamma_2'$ has properties 1 and 2 (it does not say why property 2 holds) but does not return to the parity condition, which Corollary 6.8 needs for the same loop.",
    ),
    # Findings 2, 1 (part c) and 3.
    (
        r"Moreover, every intersection of $\Gamma'$ with $\beta=(\bs)f(\Phi)$ lies on $\gamma_2$, after the last intersection of $\Gamma'$ with $\alpha$, so $\Gamma'$ is disjoint from $\beta$ modulo 4-disks and Lemma 6.4 applies to $f(\Phi)\cdot\Gamma'$; if Lemma 6.4 holds, it is $\Gamma'$ itself that fails the parity condition.",
        r"Moreover, the proof takes $\gamma_1$, $\gamma'$ and $\gamma''$ disjoint from $\beta=(\bs)f(\Phi)$, and $\gamma_2$ disjoint from $\alpha$, meeting $\beta$ exactly once in the $\beta$-component of each 4-disk and nowhere else. So every intersection of $\Gamma'$ with $\beta$ lies on $\gamma_2$, after the last intersection of $\Gamma'$ with $\alpha$, and $\Gamma'$ is disjoint from $\beta$ modulo 4-disks, as $\Gamma$ is. If Lemma 6.4 holds, it gives $f(\Phi)\cdot\Gamma'$ the same disk sequence as $f(\Phi)\cdot\Gamma$, so $f(\Phi)\cdot\Gamma'$ satisfies the parity condition, as $f(\Phi)\cdot\Gamma$ does, and then either $\Gamma'$ itself fails the parity condition or $\gamma_2'$ does not have property 2. Either way the last step of the proof breaks. In particular, Lemma 6.6 cannot supply the missing check: if $\Gamma'$ were properly simple modulo 4-disks and $\gamma_2'$ had property 2, Lemmas 6.4 and 6.6 would make both $\Gamma'$ and $f(\Phi)\cdot\Gamma'$ satisfy the parity condition, contrary to Proposition~\ref{prop:main}.",
    ),
    # Finding 4: bypass the homotopy-to-isotopy step in footnote 1.
    (
        r"so they are homotopic rel endpoints there, hence isotopic in $D_4$, and $\Phi$ fixes $\bs$. Since $\Phi$ also becomes trivial when strand $3$ is deleted, it is the push of $p_3$ around a loop $\delta$, and it takes $\bs$ to an arc homotopic to $\bs$ followed by $\delta^{\pm1}$. So $\delta$ is trivial and $\Phi=1$, a contradiction.",
        r"so they are homotopic rel endpoints there, and hence also in $D\setminus\{p_1,p_2,p_4\}$, which contains $D\setminus(\alpha\cup\{p_4\})$. Since $\Phi$ also becomes trivial when strand $3$ is deleted, it is the push of $p_3$ around a loop $\delta$ in $D\setminus\{p_1,p_2,p_4\}$, so it takes $\bs$ to an arc homotopic rel endpoints in $D\setminus\{p_1,p_2,p_4\}$ to $\bs$ followed by $\delta^{\pm1}$. So $\delta$ is null-homotopic there, hence $\Phi=1$, a contradiction.",
    ),
]

for i, (old, new) in enumerate(edits, 1):
    n = text.count(old)
    if n != 1:
        print(f"edit {i}: old string occurs {n} times, aborting")
        sys.exit(1)
    if "—" in new or "–" in new:
        print(f"edit {i}: replacement contains a dash character, aborting")
        sys.exit(1)
    text = text.replace(old, new)
    print(f"edit {i}: applied")

OUT.write_text(text)
for _ in range(2):
    r = subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", OUT.name],
        cwd=OUT_DIR, capture_output=True, text=True,
    )
print("pdflatex exit", r.returncode)
log = (OUT_DIR / "proposed.log").read_text(errors="replace")
for line in log.splitlines():
    if line.startswith("!") or "undefined" in line.lower() or "Output written" in line:
        print(line)
