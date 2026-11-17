# Contributing an inspectable result

This is a research ledger, not a competition to produce a convincing conclusion. Small independently checked results and precise failures are useful contributions.

1. Choose a task in [TASKS](docs/TASKS.md), or propose a bounded question. Record the repository commit and source versions you use.
2. Open or claim an issue before substantial work, so another machine can see the assignment. State the intended output and stopping condition. Do not claim ownership of a mathematical question indefinitely.
3. Work in a branch or separate checkout. Keep the historical snapshot intact.
4. Return a statement with hypotheses, proof or exact witness, dependencies, validation commands, and a clear account of what remains unproved.
5. Submit a pull request with a short explanation of the mathematical change. An independent reviewer should check the argument without relying on the author's summary.

Suggested contribution layout:

```text
contributions/<claim-id>/
  README.md             # statement, scope, result, dependencies
  proof.md              # full argument or precise obstruction
  verify.py             # optional bounded exact certificate
  expected.json         # optional independently inspectable output
  REVIEW.md             # reviewer findings, with source versions
```

Use exact arithmetic where the result depends on an exact identity. A numerical agreement is evidence only at its reported precision. A search must specify its complete input domain, normalization, exclusions, stopping rule, and unresolved outputs. Do not infer unknotness from Jones or Alexander polynomial 1.

No broad search is the default next step. Name the mathematical statement that makes the proposed computation decisive. Prefer repairing a proof, verifying an existing certificate, or isolating a realization obstruction.

## Attribution and review

Credit prior results and collaborators at the point of use. Provide a stable primary-source link, version, theorem/proposition number, and the hypotheses you use. Preserve authors' conventions or write out the translation. State AI assistance and the extent of human review factually.

Do not overwrite a failed route. Add a failure card with the original claim, exact reason for failure, affected dependencies, surviving scope, and what new fact would justify revisiting it. Do not promote a status solely on the basis of another model's agreement.

Changes to publication licensing, authorship, external correspondence, or the claimed status of a major theorem require the maintainer's decision. Research contributions do not authorize contacting cited authors on the maintainer's behalf.
