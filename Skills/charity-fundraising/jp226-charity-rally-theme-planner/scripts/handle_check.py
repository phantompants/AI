#!/usr/bin/env python3
"""
Check team name, handle and domain candidates against typical format rules.

Author: JP226Prints
Version: v1.00

Usage:
    python3 handle_check.py "Name one" "Name two" ...
    python3 handle_check.py --file names.txt

For each candidate it shows the handle it would become (letters and digits
only, lower case), its length against typical platform limits, and a domain
candidate. It does NOT check whether a name is free. No network is used.
Availability must be checked by hand in each app and at a domain registrar.

Typical limits (confirm in each app; they change):
    Instagram 30 characters, letters, numbers, full stops, underscores
    TikTok 24 characters, letters, numbers, full stops, underscores
    X 15 characters, letters, numbers, underscores
    YouTube 3 to 30 characters
    Domain label 63 characters (aim for 20 or fewer)

Findings per candidate: OK, WARN (works but weak), FIX (breaks a rule).
Exit codes: 0 always, unless no names are given (2).
"""

import re
import sys
from pathlib import Path

LIMITS = [("Instagram", 30), ("TikTok", 24), ("X", 15), ("YouTube", 30)]
RISKY = re.compile(
    r"\b(official|variety|charity|foundation|police|government|bank)\b", re.I)


def handle_of(name):
    return re.sub(r"[^a-z0-9]", "", name.lower())


def report(name):
    h = handle_of(name)
    lines = []
    status = "OK"
    if len(h) < 3:
        lines.append("FIX    too short to be a usable handle")
        status = "FIX"
    for plat, lim in LIMITS:
        if len(h) > lim and plat == "X":
            lines.append(f"WARN   X: {len(h)} characters, limit {lim}. "
                         "Use a short form there")
            status = "WARN" if status == "OK" else status
        elif len(h) > lim:
            lines.append(f"FIX    {plat}: {len(h)} characters, limit {lim}")
            status = "FIX"
    if len(h) > 20 and status != "FIX":
        lines.append("WARN   long; hard to say and type")
        status = "WARN"
    if h and h[0].isdigit():
        lines.append("WARN   starts with a digit")
        status = "WARN" if status == "OK" else status
    if re.search(r"(.)\1\1", h):
        lines.append("WARN   repeated letters, easy to mistype")
        status = "WARN" if status == "OK" else status
    if RISKY.search(name):
        lines.append("WARN   uses a word that suggests an official body "
                     "(official, charity, variety...). It can mislead "
                     "people and break the charity's brand rules")
        status = "WARN" if status == "OK" else status
    words = [w for w in re.split(r"\s+", name.strip()) if w]
    if len(words) > 1 and any(len(w) == 1 for w in words):
        lines.append("WARN   single-letter words can be misread in a handle")
    return h, status, lines


def main():
    args = sys.argv[1:]
    names = []
    if args[:1] == ["--file"] and len(args) == 2:
        try:
            names = [l.strip() for l in Path(args[1]).read_text(
                encoding="utf-8").splitlines() if l.strip()]
        except (OSError, UnicodeDecodeError) as exc:
            print(f"ERROR: cannot read {args[1]}: {exc}")
            return 2
    else:
        names = [a for a in args if not a.startswith("--")]
    if not names:
        print(__doc__)
        return 2
    print(f"{'Name':<34} {'Handle':<26} {'Len':>3}  Result")
    detail = []
    for n in names:
        h, status, lines = report(n)
        print(f"{n[:33]:<34} {h[:25]:<26} {len(h):>3}  {status}")
        for l in lines:
            detail.append(f"  {n}: {l}")
    if detail:
        print()
        print("\n".join(detail))
    print("\nDomain ideas for each (check a registrar for availability):")
    for n in names:
        h = handle_of(n)
        if h:
            print(f"  {h}.com.au   {h}.au   {h}.com")
    print("\nNOT CHECKED: whether any name is already taken. Search each app "
          "and a domain registrar by hand, and search the name on the web.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
