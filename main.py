"""Dad Joke Showdown entry: writes one original dad joke to entry.txt.

Stdlib only. The joke is a single fixed string: deterministic by
construction, 105 characters, well inside the 1-200 gate.
"""

import os

JOKE = "My daughter asked why our dinner table wobbles. I said, 'Four legs, and it still can't stand on its own.'"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
