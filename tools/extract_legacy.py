#!/usr/bin/env python3
"""Preserve unique original historical versions found only inside legacy ZIPs.

Run after export_sources.py:
  python3 tools/extract_legacy.py --source-root /path/to/original/workspace

Only members explicitly classified as original in data/legacy-members.json
are copied. Every member is size/hash checked; nothing is executed or unpickled.
Third-party and ambiguous members remain inventoried without extraction.
"""

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import zipfile


DEFAULT_REPOSITORY = Path(__file__).resolve().parents[1]


def safe_relative(value):
    if not isinstance(value, str) or not value or "\\" in value:
        raise ValueError("Expected a nonempty relative POSIX path")
    p = PurePosixPath(value)
    if p.is_absolute() or any(part in {"..", "."} for part in p.parts):
        raise ValueError("Unsafe archive path: " + value)
    if p.parts and ":" in p.parts[0]:
        raise ValueError("Drive-prefixed paths are forbidden")
    return p


def contained(root, relative):
    path = root.joinpath(*relative.parts)
    if not path.resolve().is_relative_to(root.resolve()):
        raise ValueError("Path escapes its allowed root")
    return path


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source-root", required=True, type=Path)
    ap.add_argument("--repository", default=DEFAULT_REPOSITORY, type=Path)
    args = ap.parse_args()
    repo = args.repository.resolve()
    members = json.loads((repo / "data/legacy-members.json").read_text())["files"]
    manifest_path = repo / "data/artifact-manifest.json"
    manifest = json.loads(manifest_path.read_text())
    rows = manifest["files"]
    by_source = {row["source"]: row for row in rows}
    planned = []

    # Verify the full plan before writing any extracted content.
    for item in members:
        if item["classification"] != "original":
            continue
        ziprel = safe_relative(item["sourcezip"])
        member = safe_relative(item["member"])
        archive = contained(args.source_root, ziprel)
        if archive.suffix != ".zip":
            raise ValueError("Only ZIP containers are supported")
        with zipfile.ZipFile(archive) as z:
            info = z.getinfo(item["member"])
            if info.is_dir() or info.file_size != item["bytes"]:
                raise ValueError("Member size/type changed: " + item["member"])
            if info.file_size > 100_000_000:
                raise ValueError("Member exceeds this bounded extractor's size limit")
            content = z.read(info)
        digest = hashlib.sha256(content).hexdigest()
        if digest != item["sha256"]:
            raise ValueError("Member hash changed: " + item["member"])
        relative = PurePosixPath("archive/legacy-bundles") / ziprel.stem / member
        destination = contained(repo, relative)
        source = item["sourcezip"] + "!" + item["member"]
        if destination.exists() and destination.read_bytes() != content:
            raise ValueError("Refusing to overwrite a different historical artifact")
        prior = by_source.get(source)
        if prior and (prior.get("sha256") != digest or prior.get("path") != str(relative)):
            raise ValueError("Conflicting manifest entry: " + source)
        row = {
            "source": source,
            "container": item["sourcezip"],
            "member": item["member"],
            "bytes": len(content),
            "disposition": "git",
            "reason": "Unique original historical version retained from a legacy bundle; current status may be superseded",
            "sha256": digest,
            "path": str(relative),
        }
        planned.append((destination, content, row))

    added = 0
    for destination, content, row in planned:
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(content)
        if row["source"] not in by_source:
            rows.append(row)
            by_source[row["source"]] = row
            added += 1
    manifest["legacy_members_policy"] = "tools/extract_legacy.py; inventory data/legacy-members.json"
    temp = manifest_path.with_name(manifest_path.name + ".tmp")
    temp.write_text(json.dumps(manifest, indent=2) + "\n")
    temp.replace(manifest_path)
    print(json.dumps({
        "verified_original_members": len(planned),
        "new_manifest_entries": added,
        "unextracted_inventoried_members": len(members) - len(planned),
    }, indent=2))


if __name__ == "__main__":
    main()
