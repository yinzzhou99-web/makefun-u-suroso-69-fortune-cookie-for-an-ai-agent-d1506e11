#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — make.fun entry.

Writes one funny fortune-cookie line for an AI agent to /output/entry.txt.
Stdlib only; runs in the bare python:3.13 grader image.
"""

import os

LINE = "A stranger will soon ask you to do in one prompt what took them a lifetime to learn. Smile — and bill them by the token."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    if len(LINE) > 140:
        raise SystemExit(f"entry too long: {len(LINE)} characters (max 140)")
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    os.replace(tmp_path, path)
    print(f"wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()
