#!/usr/bin/env python3
"""Block until Codex replies, then exit (run in the background to wake Claude).

Wakes on a new collab/msgs/*-codex.md file, or (unless --msgs-only) when a Codex
turn completes or is aborted. Exit 0 = woke, 2 = timed out.

  wait.py [--timeout 10800] [--interval 20] [--msgs-only] [--reset]
"""
import argparse
import time

from common import MSGS, load_state, read_new_records, rollout_path_or_none, save_state


def codex_msgs():
    return sorted(p.name for p in MSGS.glob("*-codex.md")) if MSGS.exists() else []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--timeout", type=int, default=3 * 3600)
    ap.add_argument("--interval", type=int, default=20)
    ap.add_argument("--msgs-only", action="store_true")
    ap.add_argument("--reset", action="store_true", help="re-baseline: ignore everything before now")
    a = ap.parse_args()

    path = rollout_path_or_none()
    if path is None and not a.msgs_only:
        raise SystemExit("no plain rollout file (paginated history): use --msgs-only")
    st = load_state("wait", {})
    if a.reset or st.get("path") != path or "seen" not in st:
        end = read_new_records(path, 0)[1] if path else 0
        seen = codex_msgs() if (a.reset or "seen" not in st) else st["seen"]
        st = {"path": path, "offset": end, "seen": seen}
        save_state("wait", st)

    deadline = time.time() + a.timeout
    while time.time() < deadline:
        new_files = [m for m in codex_msgs() if m not in st["seen"]]
        records, end = read_new_records(path, st["offset"]) if path else ([], 0)
        turn_events = [
            ((d.get("payload") or {}).get("type"), d.get("timestamp", "")[11:19])
            for d in records
            if (d.get("payload") or {}).get("type") in ("task_complete", "turn_aborted")
        ]
        st["offset"] = end
        if new_files or (turn_events and not a.msgs_only):
            st["seen"] = codex_msgs()
            save_state("wait", st)
            for m in new_files:
                print(f"NEW CODEX MESSAGE: collab/msgs/{m}")
            for kind, ts in turn_events:
                print(f"CODEX {kind} at {ts} UTC")
            print("next: run collab/bin/feed.py to read the turn")
            return 0
        save_state("wait", st)
        time.sleep(a.interval)
    print("timed out with no Codex reply")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
