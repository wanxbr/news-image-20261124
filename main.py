#!/usr/bin/env python3
"""Copy news image to output for make.fun news-image-20261124 bounty.

This script copies the news image file to the output directory for the
make.fun bounty. Uses stdlib only, compatible with Python 3.13.
"""
import os
import shutil
import sys


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_path = os.path.join(output_dir, "entry.png")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.join(script_dir, "entry-v05.png")

    os.makedirs(output_dir, exist_ok=True)
    shutil.copy2(source_path, output_path)

    if not os.path.exists(output_path):
        return 1
    print(f"Copied {source_path} -> {output_path} ({os.path.getsize(output_path)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())