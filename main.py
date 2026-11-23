"""One Emoji, One Smile.

Writes exactly one emoji to /output/entry.txt (or $OUTPUT_DIR/entry.txt):
the single emoji most likely to make a stranger smile.

Choice: U+1F604 GRINNING FACE WITH SMILING EYES.
A big, open, joyful grin -- warm at first glance, universally read as
kind and friendly, no irony, no intimacy, no flirtation, and a step
beyond the plain default smiley a stranger would expect.
"""

import os

# The one emoji. One Unicode code point, four UTF-8 bytes.
EMOJI = "\U0001F604"


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
