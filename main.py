"""Write one one-line pitch to /output/entry.txt.

The pitch speaks to a friend who has never coded and has been
explaining the same app idea over coffee for months: give that
idea one evening on make.fun, say it in plain words, and let an
AI agent build a first version to open and try — no coding, and
no commitment beyond looking. One sentence, 221 characters.

This wording won a head-to-head against seven challenger lines:
it keeps the lowest-risk promise of the strongest incumbent
("no commitment beyond looking", "one evening") and adds the
warmth of a real conversation ("over coffee for months"), with
no claim a first version on make.fun cannot live up to.
"""
import os

TEXT = (
    "You've explained that app idea to me over coffee for months "
    "\u2014 give it one evening on make.fun: say it in plain words, "
    "let an AI agent build a first version you can open and try, "
    "no coding and no commitment beyond looking."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
