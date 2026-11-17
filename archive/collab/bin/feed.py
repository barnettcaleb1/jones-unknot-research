#!/usr/bin/env python3
"""Print what happened in the Codex thread since the last call (Claude's read side).

  feed.py            new activity since last call (advances the cursor)
  feed.py --peek     same, without advancing
  feed.py --full     do not truncate progress notes
  feed.py --from-start-of-last-turn   replay the most recent turn
"""
import argparse

from common import CLAUDE_PREFIX, load_state, message_text, read_new_records, rollout_path, save_state


def render(records, full):
    out = []
    for d in records:
        t, p = d.get("type"), d.get("payload") or {}
        ts = d.get("timestamp", "")[11:19]
        if t == "response_item" and p.get("type") == "message":
            text = message_text(p).strip()
            if p.get("role") == "user":
                if not text or text.startswith("<"):
                    continue
                who = "CLAUDE" if text.startswith(CLAUDE_PREFIX) else "CALEB"
                out.append(f"--- {ts} {who} -> codex\n{text if full else text[:600]}")
            elif p.get("role") == "assistant":
                if p.get("phase") == "commentary":
                    out.append(f"  {ts} codex note: {text if full else text[:400]}")
                else:
                    out.append(f"=== {ts} CODEX\n{text}")
        elif t == "event_msg":
            kind = p.get("type")
            if kind == "task_started":
                out.append(f"--- {ts} turn started")
            elif kind == "task_complete":
                out.append(f"--- {ts} turn complete")
            elif kind == "turn_aborted":
                out.append(f"--- {ts} turn aborted")
            elif kind == "thread_goal_updated":
                out.append(f"--- {ts} goal {p.get('goal', {}).get('status')}")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--peek", action="store_true")
    ap.add_argument("--full", action="store_true")
    ap.add_argument("--from-start-of-last-turn", action="store_true")
    a = ap.parse_args()

    path = rollout_path()
    st = load_state("feed", {})
    offset = st.get("offset", 0) if st.get("path") == path else 0
    if a.from_start_of_last_turn:
        records, end = read_new_records(path, 0)
        starts = [i for i, d in enumerate(records)
                  if (d.get("payload") or {}).get("type") == "task_started"]
        records = records[starts[-1]:] if starts else records
    elif offset == 0:
        # first run: show only the most recent turn, not three days of history
        records, end = read_new_records(path, 0)
        starts = [i for i, d in enumerate(records)
                  if (d.get("payload") or {}).get("type") == "task_started"]
        records = records[starts[-1]:] if starts else records[-50:]
    else:
        records, end = read_new_records(path, offset)

    text = render(records, a.full)
    print(text if text else "(no new activity)")
    if not a.peek:
        save_state("feed", {"path": path, "offset": end})


if __name__ == "__main__":
    main()
