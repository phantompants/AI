#!/usr/bin/env python3
"""
Check a draft eBay AU or Etsy listing for a 3D printed product.

Author: JP226Prints
Version: v1.00

Usage:
    python3 check_listing.py LISTING.txt

LISTING.txt format (plain text):

    PLATFORM: etsy            (etsy or ebay)
    TITLE: your title
    TAGS: tag one, tag two    (Etsy only)
    DESCRIPTION:
    everything after this line is the description

Findings:
    ERROR  must fix before the listing goes live
    WARN   should fix, or accept on purpose
    INFO   for the seller to confirm

Exit codes: 0 no errors, 1 one or more errors, 2 unreadable file.

Limits used: eBay title 80 characters; Etsy title 140 characters, up to 13
tags of up to 20 characters each. Platforms change their rules, so confirm
in the seller tools.
"""

import re
import sys
from pathlib import Path

LIMITS = {"ebay": {"title": 80}, "etsy": {"title": 140, "tags": 13, "tag": 20}}

# Safety claims that need proof the seller holds. jp226-check: ignore
SAFETY = re.compile(
    r"\b(food[- ]?safe|food[- ]?grade|non[- ]?toxic|bpa[- ]?free|"
    r"child[- ]?safe|baby[- ]?safe|safe for (?:kids|children|toddlers|pets)|"
    r"dishwasher[- ]?safe|microwave[- ]?safe|fire[- ]?proof|flame[- ]?retardant|"
    r"medical[- ]?grade|hypoallergenic|certified|ce marked|ul listed)\b", re.I)
# Absolute performance claims
ABSOLUTE = re.compile(
    r"\b(waterproof|unbreakable|indestructible|shatter[- ]?proof|"
    r"lifetime|guaranteed|100%)\b", re.I)
# Brands, franchises and trademarks that cause takedowns if used as the product
TRADEMARK = re.compile(
    r"\b(disney|marvel|pokemon|pok[eé]mon|nintendo|mario|zelda|lego|star wars|"
    r"harry potter|hello kitty|minecraft|fortnite|batman|spider-?man|"
    r"jurassic (?:park|world)|bambu(?: lab)?|ikea|apple|nike|"
    r"toyota|ford|holden|jeep|harley)\b", re.I)
AMERICAN = {"color": "colour", "colors": "colours", "gray": "grey",
            "center": "centre", "organize": "organise", "customize": "customise",
            "customized": "customised", "organizer": "organiser",
            "organizers": "organisers", "colorful": "colourful", "favorite": "favourite",
            "meter": "metre", "aluminum": "aluminium", "realize": "realise"}
CHARITY = re.compile(r"\b(charity|donat\w+|proceeds|profits?|variety|"
                     r"fundrais\w+|% of)\b", re.I)
SHOUTING = re.compile(r"\b[A-Z]{5,}\b")
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")


def parse(text):
    data = {"platform": "", "title": "", "tags": [], "description": ""}
    lines = text.splitlines()
    desc_at = None
    for i, line in enumerate(lines):
        m = re.match(r"^\s*(PLATFORM|TITLE|TAGS|DESCRIPTION)\s*:\s*(.*)$", line,
                     re.I)
        if not m:
            continue
        key, val = m.group(1).lower(), m.group(2).strip()
        if key == "platform":
            data["platform"] = val.lower()
        elif key == "title":
            data["title"] = val
        elif key == "tags":
            data["tags"] = [t.strip() for t in val.split(",") if t.strip()]
        else:
            desc_at = i
            data["description"] = (val + "\n" if val else "") + \
                "\n".join(lines[i + 1:])
            break
    return data


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    path = Path(sys.argv[1])
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        print(f"ERROR: cannot read {path}: {exc}")
        return 2
    d = parse(text)
    out = []
    plat = d["platform"]
    if plat not in LIMITS:
        out.append(("ERROR", "PLATFORM must be 'etsy' or 'ebay'."))
        plat = "etsy"
    lim = LIMITS[plat]
    title, desc = d["title"], d["description"]
    whole = f"{title}\n{', '.join(d['tags'])}\n{desc}"

    if not title:
        out.append(("ERROR", "No TITLE found."))
    elif len(title) > lim["title"]:
        out.append(("ERROR", f"Title is {len(title)} characters; {plat} "
                             f"allows {lim['title']}."))
    elif plat == "ebay" and len(title) < 60:
        out.append(("INFO", f"Title uses {len(title)} of 80 characters. "
                            "More keywords may help buyers find it."))
    if title and SHOUTING.search(title):
        out.append(("WARN", "Title has words in capitals. Use normal case."))
    if EMOJI.search(title):
        out.append(("WARN", "Title contains an emoji. Remove it."))

    if plat == "etsy":
        if len(d["tags"]) > lim["tags"]:
            out.append(("ERROR", f"{len(d['tags'])} tags; Etsy allows "
                                 f"{lim['tags']}."))
        elif len(d["tags"]) < lim["tags"]:
            out.append(("INFO", f"{len(d['tags'])} of {lim['tags']} tags used."))
        for t in d["tags"]:
            if len(t) > lim["tag"]:
                out.append(("ERROR", f"Tag '{t}' is {len(t)} characters; "
                                     f"the limit is {lim['tag']}."))
        low = [t.lower() for t in d["tags"]]
        if len(set(low)) != len(low):
            out.append(("WARN", "Duplicate tags. Each tag should be different."))
    elif d["tags"]:
        out.append(("INFO", "TAGS ignored: eBay uses item specifics instead."))

    if not desc.strip():
        out.append(("ERROR", "No DESCRIPTION found."))
    elif len(desc.strip()) < 200:
        out.append(("WARN", "Description is very short. Add size, material, "
                            "colour options and care."))

    for m in sorted(set(x.group(0).lower() for x in SAFETY.finditer(whole))):
        out.append(("ERROR", f"Unverified safety claim '{m}'. Remove it unless "
                             "you hold proof (test report or certificate)."))
    for m in sorted(set(x.group(0).lower() for x in ABSOLUTE.finditer(whole))):
        out.append(("WARN", f"Absolute claim '{m}'. 3D prints can warp, crack "
                            "or leak; say what it does in plain terms."))
    for m in sorted(set(x.group(0).lower() for x in TRADEMARK.finditer(whole))):
        out.append(("WARN", f"'{m}' may be a brand or trademark. Selling "
                            "unlicensed products or using the name in a "
                            "title can get a listing removed."))
    for us, au in AMERICAN.items():
        if re.search(rf"\b{us}\b", whole, re.I):
            out.append(("WARN", f"American spelling '{us}'. Use '{au}'."))
    if CHARITY.search(whole):
        out.append(("INFO", "The listing mentions charity or donations. State "
                            "only what the seller has confirmed, with the "
                            "exact share and who receives it, and check the "
                            "platform's charity rules."))
    if "—" in whole:  # em dash
        out.append(("WARN", "Contains an em dash. Use a comma or full stop."))
    if not re.search(r"\b(printed|print)\b", whole, re.I):
        out.append(("INFO", "Does not say the item is 3D printed. Say so."))
    if not re.search(r"\b(pla|petg|abs|asa|tpu|nylon|resin)\b", whole, re.I):
        out.append(("INFO", "No material named (PLA, PETG and so on)."))
    if not re.search(r"\b\d+(?:\.\d+)?\s?(mm|cm|m)\b", whole, re.I):
        out.append(("INFO", "No size in mm or cm. Buyers need dimensions."))

    order = {"ERROR": 0, "WARN": 1, "INFO": 2}
    for level, msg in sorted(out, key=lambda x: order[x[0]]):
        print(f"{level:<6} {msg}")
    errs = sum(1 for lv, _ in out if lv == "ERROR")
    warns = sum(1 for lv, _ in out if lv == "WARN")
    print(f"\nPlatform: {plat}  Title: {len(title)} chars  "
          f"Errors: {errs}  Warnings: {warns}")
    print("RESULT: " + ("FAILED" if errs else "PASSED"))
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
