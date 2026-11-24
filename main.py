"""Dad Joke Showdown entry: writes one original dad joke to entry.txt.

Stdlib only. The joke is a single fixed string: deterministic by
construction, 104 characters, well inside the 1-200 gate.
"""

import os

JOKE = "My daughter asked why I butter my toast on both sides. I said, 'So no matter how it lands, I'm covered.'"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
