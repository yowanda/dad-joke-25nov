"""Dad Joke Showdown entry (make.fun u-mfnakmal-dad-joke-showdown-1d2ce3e5).

Writes one original dad joke to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output when the variable is unset). Deterministic: the same
bytes on every run. No network, no input files, no dependencies.
"""

import os

JOKE = (
    "I quit my job at the bakery. I just couldn't make enough dough. "
    "My daughter said the joke was half-baked. She's right. "
    "That's the yeast I could do."
)


def main() -> None:
    # Runtime validation: output must be a non-empty joke within limits.
    if not 1 <= len(JOKE) <= 200:
        raise ValueError(f"joke length {len(JOKE)} out of range 1-200")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
