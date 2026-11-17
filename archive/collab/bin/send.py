#!/usr/bin/env python3
"""Send a Claude message to the live Codex thread and archive it in collab/msgs.

  send.py --type PROPOSAL --node R1.3 --budget "1 turn" body.md
  echo "..." | send.py --type QUESTION -
"""
import argparse
import subprocess
import sys

from common import CLAUDE_PREFIX, CODEX_BIN, MSGS, THREAD_ID, msg_id

FOOTER = (
    "(Protocol: collab/PROTOCOL.md. Reply as a new file in collab/msgs/, "
    "update collab/SCAFFOLD.md for any status change, then end your turn with "
    "a summary of at most 10 lines naming the reply file.)"
)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("body", help="file with the message body, or - for stdin")
    ap.add_argument("--type", default="PROPOSAL")
    ap.add_argument("--node", default="-")
    ap.add_argument("--budget", default="-")
    ap.add_argument("--re", dest="re_id", default="-")
    ap.add_argument("--no-resume", action="store_true", help="queue only; do not wake the thread")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    body = sys.stdin.read() if a.body == "-" else open(a.body).read()
    mid = msg_id("claude")
    header = (
        f"from: claude\nto: codex\ntype: {a.type}\nnode: {a.node}\n"
        f"budget: {a.budget}\nre: {a.re_id}\n---\n"
    )
    record = header + body.strip() + "\n"
    queued = f"{CLAUDE_PREFIX} id: {mid}\n{record}\n{FOOTER}"

    if a.dry_run:
        print(queued)
        return
    MSGS.mkdir(parents=True, exist_ok=True)
    (MSGS / f"{mid}.md").write_text(record)

    cmd = [CODEX_BIN, "queue", "--thread", THREAD_ID, "--message", queued]
    if not a.no_resume:
        cmd.append("--resume")
    r = subprocess.run(cmd, capture_output=True, text=True)
    print(f"archived msgs/{mid}.md; codex queue exit {r.returncode}")
    for out in (r.stdout.strip(), r.stderr.strip()):
        if out:
            print(out)
    sys.exit(r.returncode)


if __name__ == "__main__":
    main()
