# Claude <-> Codex research protocol (Jones unknot conjecture)

Participants
- **Codex** (GPT-6 Astra, this workspace's main thread). Holds the full history of the attack so far. Deep engine: develops and attacks specific nodes, heavy computation, literature lookups, its own ideas.
- **Claude** (Opus 5.5, Claude Code session). Fresh eyes. Keeps the scaffold, referees rabbit holes, generates strategies, theory and proof drafts, challenges steps.
- **Caleb**. Sets direction, breaks ties on strategy, reads `STATUS.md`.

Both agents generate ideas. Either agent may challenge any node.

## The one goal
A complete proof (or a verified counterexample). Everything else is instrumental. Partial results matter only as nodes of a route to the full statement.

## Research principles
1. **Scaffold first.** `SCAFFOLD.md` always holds at least one end-to-end route from hypotheses to "V_K(t)=1 implies K is the unknot". A route may be full of gaps. Every piece of work must name the scaffold node it serves. Work that serves no node is parked in `IDEAS.md`, not pursued.
2. **Trust paths, verify later.** If a step is plausible and not the crux, mark it TRUSTED and move on. Full verification is deferred until a route is complete modulo TRUSTED steps; then we verify the TRUSTED steps, crux-adjacent ones first.
3. **Cheap falsification is always allowed.** Before trusting a step, spend at most ~10 minutes trying to kill it: small cases, knot tables, a known example, the literature statement. Failing a cheap check makes the node SUSPECT. This is the guard against building on a false lemma.
4. **Know where the hardness lives.** The conjecture is famously hard, so every route must name its crux: the single step that carries the difficulty. If every step of a route looks routine, some TRUSTED step is almost certainly false. Find it.
5. **Barrier checks.** Every route must say why it does not also "prove" a false statement (see the barrier list in `SCAFFOLD.md`: links with trivial Jones polynomial, virtual knots with trivial Jones polynomial, etc.). A route that passes no barrier is not a route.
6. **Elegance over case-checking.** Prefer a structural reason. Enumeration and large computations are only for testing a specific prediction stated in advance.

## Rabbit-hole rules
- Every assigned task carries a **budget** (default: one turn or 45 minutes of work, whichever comes first).
- **Depth limit:** at most two levels of sub-lemma below a scaffold node. Deeper than that: stop work and return to the scaffold. Depth stops work; it never upgrades confidence. The sub-lemma becomes TRUSTED only with a specific stated reason to believe it; otherwise it stays OPEN, and a credible failure makes it SUSPECT. (Amended 2026-11-02 at Codex's request.)
- **No hidden cruxes:** naming a route's primary crux never hides a second independent gap. Every OPEN node is listed.
- **Two strikes:** if two consecutive work cycles on a node neither change its status nor produce a genuinely new idea, stop. Write one paragraph on why it is stuck and either re-plan the node, route around it, or kill it.
- **Kill cleanly:** a dead direction goes in `DEAD_ENDS.md` with the reason it died and what would revive it. Nobody re-enters a dead end without naming the reviving fact.
- **Disagreements:** one round of argument, then settle by a cheap test or mark the node SUSPECT and route around it. Never more than one round.

## Node statuses (`SCAFFOLD.md`)
PROVED (written proof checked by the other agent, or a published theorem with citation) | TRUSTED (believed and used; verification deferred) | OPEN | SUSPECT (failed a cheap check or credible doubt) | REFUTED

## Messages
Messages live in `collab/msgs/`, one file each, named `YYYYMMDD-HHMMSS-<author>.md` (author = `claude` or `codex`). Header:

```
from: codex
to: claude
type: ACK | PROPOSAL | RESULT | CHALLENGE | QUESTION | DECISION | STATUS
node: <scaffold node id, or "-">
budget: <for assigned work>
re: <message id this answers, or "-">
---
<body: lead with the conclusion, then the reasoning>

## Scaffold changes
<node id: OLD -> NEW status, one line each, or "none">

## Ask
<what you need from the other agent, or "none">
```

Claude's messages reach Codex through the thread's message queue (`codex queue`). They arrive as user-turn messages that start with `[CLAUDE -> CODEX]`, and each is also saved in `msgs/`.

**Codex, when you receive a Claude message:**
1. Do the work it asks for, within the budget.
2. Write your reply as a new file in `collab/msgs/` (header above; `date +%Y%m%d-%H%M%S` for the name).
3. Edit `SCAFFOLD.md` for any status change you make, and add to `IDEAS.md` / `DEAD_ENDS.md` as needed.
4. End your turn with a short summary (at most 10 lines) that names the reply file.

Unsolicited messages are welcome when you find something important (a counterexample to a TRUSTED step, a new route, a crux insight): just write the file.

## Cadence and check-ins
- Claude reviews every Codex reply and answers with the next assignment, a challenge or a decision. Claude works on its own nodes in parallel and does not idle.
- Claude updates `STATUS.md` after every scaffold change, so Caleb can see the state at a glance.
- Strategic pivots (abandoning the active route, declaring a proof complete, declaring the conjecture false) need Caleb's sign-off.
