#!/usr/bin/env python3

from pathlib import Path

src = Path("src")
wiki = src.joinpath("Wiki")
summary = src.joinpath("SUMMARY.md")

def build_dir(entry: Path) -> str:
    parts = entry.parts
    indent = "\t" * (len(parts) - 3)  # dont count Wiki and filename
    return indent + f"- [{entry.parent.name}]({entry})\n"

def build_entry(entry: Path) -> str:
    parts = entry.parts
    indent = "\t" * (len(parts) - 2)  # dont count Wiki and filename
    return indent + f"- [{entry.name}]({entry})\n"


with open(summary, "w+", encoding="utf-8") as f:
    f.write("""# Summary

[Introduction](Wiki/README.md)

""")

    last_dir = None
    pathlist = wiki.rglob("*.md")
    for path in pathlist:
        if path.name.lower() == "readme.md":
            continue

        path_parts = path.parts[1:]
        trimed_path = Path(*path_parts)

        if trimed_path.parent != last_dir and trimed_path.parent.name != wiki.name:
            last_dir = trimed_path.parent
            f.write(build_dir(last_dir.joinpath("README.md")))

        f.write(build_entry(trimed_path))
