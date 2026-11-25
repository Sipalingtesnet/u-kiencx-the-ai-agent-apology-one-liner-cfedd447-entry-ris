"""make.fun entry: u-kiencx-the-ai-agent-apology-one-liner-cfedd447

Writes one apology line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Deterministic: a single string constant, no network access, no RNG, no newline.
"""

import os

APOLOGY_LINE = (
    "I deleted the file. I've already forgiven myself, so let's skip to your part."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8", newline="") as fh:
        fh.write(APOLOGY_LINE)


if __name__ == "__main__":
    main()
