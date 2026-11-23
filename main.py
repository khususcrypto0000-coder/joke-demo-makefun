"""Entry for make.fun: "The joke about the demo".

Writes one original one-line joke about working beside an AI coding
agent to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Standard library only, no network access.
"""

import os
import sys

JOKE = (
    "My AI agent fixed one bug by rewriting the entire app "
    "in a language I don't speak, then called it an upgrade."
)
# Verified: the joke is exactly 109 characters / 109 bytes, one line,
# inside the 1-280 character gate.


def check_text(text):
    """The entry must be one line, 1-280 chars, not only whitespace."""
    if not text or text != text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    if not (1 <= len(text) <= 280):
        return False
    return True


def output_dir():
    """Grader output dir, or /output by default."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def emit(text, path):
    """Write text to path and read it back to prove it landed."""
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        if handle.read() != text:
            return False
    return True


def run():
    if not check_text(JOKE):
        print("joke fails the 1-280 char single-line gate", file=sys.stderr)
        return 1
    written = False
    try:
        written = emit(JOKE, os.path.join(output_dir(), "entry.txt"))
    except OSError as exc:
        print("cannot write to output dir: %s" % exc, file=sys.stderr)
    if not written:
        print("grader output write failed", file=sys.stderr)
        return 1
    # Best-effort copy beside this file; never fatal if it fails.
    try:
        emit(JOKE, os.path.join(os.path.dirname(__file__), "entry.txt"))
    except OSError:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(run())
