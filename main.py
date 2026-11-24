"""Two Lines to Your Past Self.

Writes exactly two lines to /output/entry.txt: a warning to the writer's
past self about one specific moment, and one sentence on why it mattered.
Deterministic, no network, no secrets.
"""

import os

LINE_ONE = "Don't board the last bus home the night the river rises \u2014 stay for one more drink with the girl in the yellow coat."
LINE_TWO = "The bus never makes it across the bridge, and the girl becomes the reason you never leave this town."

# Why these two lines: the warning names one concrete, picturable moment
# (the last bus, the rising river, one more drink, the girl in the yellow
# coat) instead of a vague phase of life, and the second line traces real
# cause and effect — the bus never crosses the bridge, so the writer would
# have been on it, and the girl is why he never leaves town. Plain voice,
# written to one specific person, no wasted words.

ENTRY = LINE_ONE + "\n" + LINE_TWO

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def check_entry(text: str) -> str:
    """Return the entry stripped, enforcing the 1-280 character gate."""
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("entry must not be only whitespace")
    if len(cleaned) > 280:
        raise ValueError("entry must be at most 280 characters")
    lines = cleaned.split("\n")
    if len(lines) != 2:
        raise ValueError("entry must be exactly two lines")
    if any(not line.strip() for line in lines):
        raise ValueError("each line must hold text")
    return cleaned


def main() -> None:
    text = check_entry(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text + "\n")


if __name__ == "__main__":
    main()
