"""Two-line explanation of a queue for a 10-year-old.

Line 1 explains a queue through one vivid analogy: a human
caterpillar shuffling forward one tiny step at a time. Line 2 is
honest about the analogy: what it maps and what it leaves out.
The script validates the two lines and writes them to
/output/entry.txt.
"""

from pathlib import Path

# The entry itself: exactly two lines, one sentence each, 264 chars.
ENTRY = (
    "A queue is a human caterpillar, each person a segment shuffling "
    "forward one tiny step at a time toward the front.\n"
    "It maps how everyone moves together in the same direction, but "
    "it leaves out that people can leave, cut in, or get bored, which "
    "caterpillars never do."
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 400


def validate(text: str) -> str:
    """Check the entry is 1-400 chars, exactly two non-empty lines,
    one sentence each; raise ValueError on bad input."""
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if text != text.strip() or not text.strip():
        raise ValueError("entry must not be only whitespace")
    lines = text.split("\n")
    if len(lines) != 2 or any(not line.strip() for line in lines):
        raise ValueError(
            f"entry must be exactly two non-empty lines, got {len(lines)}"
        )
    for i, line in enumerate(lines, 1):
        if not line.rstrip().endswith("."):
            raise ValueError(f"line {i} must end with a full stop")
        if ". " in line.rstrip():
            raise ValueError(f"line {i} must be a single sentence")
    return text


def main() -> None:
    text = validate(ENTRY)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
