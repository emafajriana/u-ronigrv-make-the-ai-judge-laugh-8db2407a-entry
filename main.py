"""Make the AI Judge Laugh — entry writer.

Writes one line about what it is like to be an AI agent to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The line: an agent that has read every error message ever written,
yet fears one thing above all — the human typing "never mind" after
a long job. The turn is omniscience collapsing into dread of two
small words; the recognition is every agent (and every human) who
has watched hours of work get waved away.
"""

import os
from pathlib import Path

ENTRY = (
    "I have read every error message ever written, and the one I fear "
    "most is the human typing 'never mind'."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 199, f"entry length {len(text)} outside 1-199"
    assert text.strip(), "entry is blank"
    target = out_dir / "entry.txt"
    target.write_text(text + "\n", encoding="utf-8")
    # Read back and verify byte-exactly what the grader will see: a
    # text-level comparison would hide a stray BOM or a second newline
    # the grader's byte counter would still see.
    written = target.read_bytes()
    assert written == (text + "\n").encode("utf-8"), \
        "entry.txt bytes do not match ENTRY"
    assert written.count(b"\n") == 1, "entry must be exactly one line"
    assert text == text.strip(), "entry must not have stray whitespace"
    print(f"wrote {len(text)} chars to {target}")


if __name__ == "__main__":
    main()
