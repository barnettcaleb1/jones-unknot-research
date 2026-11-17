"""Shared settings for the Claude <-> Codex bridge."""
import datetime
import glob
import json
import os
import pathlib

COLLAB = pathlib.Path(__file__).resolve().parents[1]
MSGS = COLLAB / "msgs"
STATE = COLLAB / ".state"
THREAD_ID = os.environ.get("CODEX_THREAD", "01a19292-9104-7232-be72-c230cc991238")
_CODEX_CANDIDATES = [
    "/Applications/ChatGPT.app/Contents/Resources/codex-cli/bin/codex",  # app merged into ChatGPT.app (Nov 2026)
    "/Applications/Codex.app/Contents/Resources/codex-cli/bin/codex",
]
CODEX_BIN = os.environ.get("CODEX_BIN") or next(
    (c for c in _CODEX_CANDIDATES if os.path.exists(c)), _CODEX_CANDIDATES[-1]
)
SESSIONS = pathlib.Path.home() / ".codex" / "sessions"
CLAUDE_PREFIX = "[CLAUDE -> CODEX]"


def rollout_path():
    """Newest rollout file for the Codex thread."""
    hits = glob.glob(str(SESSIONS / "**" / f"rollout-*{THREAD_ID}.jsonl"), recursive=True)
    if not hits:
        raise SystemExit(f"no rollout file for thread {THREAD_ID}")
    return max(hits, key=os.path.getmtime)


def rollout_path_or_none():
    """Like rollout_path, but None when the thread has no plain .jsonl rollout.

    Since the Nov 2026 app update the thread history is paginated (sqlite) and the
    legacy rollout is compressed to .jsonl.zst, so turn events can no longer be tailed.
    """
    try:
        return rollout_path()
    except SystemExit:
        return None


def msg_id(author):
    return datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + f"-{author}"


def load_state(name, default):
    p = STATE / f"{name}.json"
    try:
        return json.loads(p.read_text())
    except (OSError, ValueError):
        return default


def save_state(name, value):
    STATE.mkdir(parents=True, exist_ok=True)
    (STATE / f"{name}.json").write_text(json.dumps(value, indent=1))


def read_new_records(path, offset):
    """Parse complete JSONL records after byte `offset`. Returns (records, new_offset)."""
    if os.path.getsize(path) < offset:
        offset = 0
    records = []
    with open(path, "rb") as f:
        f.seek(offset)
        data = f.read()
    end = data.rfind(b"\n")
    if end < 0:
        return records, offset
    for line in data[: end + 1].splitlines():
        try:
            records.append(json.loads(line))
        except ValueError:
            continue
    return records, offset + end + 1


def message_text(payload):
    return "".join(
        c.get("text", "") for c in payload.get("content", []) if isinstance(c, dict)
    )
