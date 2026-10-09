#!/usr/bin/env python3
"""
Check fundraising posts, emails and messages before they are sent.

Author: JP226Prints
Version: v1.00

Usage:
    python3 check_posts.py FILE [--platform NAME] [--donate-url URL]

FILE holds one or more drafts. Separate drafts with a line of three dashes
(---). A draft can start with a line "PLATFORM: instagram" to set its limit.

Platforms and character limits (confirm in each app; they change):
    x 280, instagram 2200, facebook 63206, tiktok 2200, linkedin 3000,
    sms 160, email (no limit), general (no limit)

Findings:
    ERROR  must fix
    WARN   should fix or accept on purpose
    INFO   for the sender to confirm

Exit codes: 0 no errors, 1 one or more errors, 2 unreadable file.
"""

import argparse
import re
import sys
from pathlib import Path

LIMITS = {"x": 280, "instagram": 2200, "facebook": 63206, "tiktok": 2200,
          "linkedin": 3000, "sms": 160, "email": None, "general": None}

# Asking for money to be sent to the team instead of the charity page.
PAYMENT = re.compile(
    r"\b(bsb|account (?:number|no)|acc(?:ount)? ?#|payid|bank transfer|"
    r"direct deposit|paypal\.?me|venmo|cash ?app|bitcoin|crypto|"
    r"gift ?cards?|western union|send (?:us |me )?(?:money|cash)|"
    r"card (?:number|details)|cvv|bpay)\b", re.I)
URGENCY = re.compile(
    r"\b(last chance|hurry|running out of time|don'?t miss out|act now|"
    r"today only|final hours|urgent|before it'?s too late|only \d+ (?:days?|"
    r"hours?|spots?) left)\b", re.I)
CLAIMS = re.compile(
    r"(?<!\w)(100 ?%|every (?:single )?(?:cent|dollar)|tax[- ]?deductible|"
    r"official (?:partner|sponsor|fundraiser)|endorsed by|approved by|"
    r"guarantee[sd]?)(?!\w)", re.I)
GUILT = re.compile(
    r"\b(if you really care|you owe|shame on|only monsters|"
    r"how can you not|no excuse)\b", re.I)
MONEY = re.compile(r"\$\s?\d[\d,]*(?:\.\d+)?(?:\s?(?:k|m|million)\b)?", re.I)
DATE = re.compile(
    r"\b(?:as at|as of|at)\s+\d{1,2}[ /]\w+[ /]?\d{0,4}|"
    r"\b\d{1,2}\s+(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\w*|"
    r"\b\d{4}-\d{2}-\d{2}\b|\b\d{1,2}/\d{1,2}/\d{2,4}\b", re.I)
AMERICAN = {"color": "colour", "organize": "organise", "center": "centre",
            "favorite": "favourite", "realize": "realise", "program": None}
URL = re.compile(r"https?://[^\s)>\]]+")
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")


def split_drafts(text):
    parts = re.split(r"(?m)^\s*---\s*$", text)
    return [p.strip("\n") for p in parts if p.strip()]


def check(draft, idx, default_platform, donate_url, out):
    platform = default_platform
    m = re.match(r"\s*PLATFORM\s*:\s*(\w+)\s*\n", draft, re.I)
    if m:
        platform = m.group(1).lower()
        draft = draft[m.end():]
    tag = f"Draft {idx}"
    if platform not in LIMITS:
        out.append(("WARN", f"{tag}: unknown platform '{platform}', using "
                            "general."))
        platform = "general"
    limit = LIMITS[platform]
    if limit and len(draft) > limit:
        out.append(("ERROR", f"{tag}: {len(draft)} characters; {platform} "
                             f"allows about {limit}."))

    for hit in sorted(set(x.group(0).lower() for x in PAYMENT.finditer(draft))):
        out.append(("ERROR", f"{tag}: asks for money outside the charity page "
                             f"('{hit}'). Donations go only to the charity's "
                             "own donation page."))
    if donate_url:
        if donate_url not in draft:
            out.append(("WARN" if platform in ("x", "sms") else "ERROR",
                        f"{tag}: the donation link is missing."))
        others = [u for u in URL.findall(draft)
                  if donate_url not in u]
        if others:
            out.append(("INFO", f"{tag}: other links present: "
                                f"{', '.join(others[:3])}. Check each one."))
    for hit in sorted(set(x.group(0).lower() for x in URGENCY.finditer(draft))):
        out.append(("WARN", f"{tag}: pressure wording '{hit}'. Only use a real "
                            "deadline, stated with its date."))
    for hit in sorted(set(x.group(0).lower() for x in CLAIMS.finditer(draft))):
        out.append(("WARN", f"{tag}: claim '{hit}'. Keep it only if the "
                            "charity confirms it in writing."))
    for hit in sorted(set(x.group(0).lower() for x in GUILT.finditer(draft))):
        out.append(("WARN", f"{tag}: guilt wording '{hit}'. Ask kindly."))
    amounts = MONEY.findall(draft)
    if amounts and not DATE.search(draft):
        out.append(("ERROR", f"{tag}: money figure(s) {', '.join(amounts[:4])} "
                             "with no 'as at' date."))
    elif amounts:
        out.append(("INFO", f"{tag}: confirm every figure ({', '.join(amounts[:4])}) "
                            "against the donation page on the day you send."))
    for us, au in AMERICAN.items():
        if au and re.search(rf"\b{us}\b", draft, re.I):
            out.append(("WARN", f"{tag}: American spelling '{us}'. Use "
                                f"'{au}'."))
    if "—" in draft:
        out.append(("WARN", f"{tag}: contains an em dash. Use a comma or "
                            "full stop."))
    if len(EMOJI.findall(draft)) > 5:
        out.append(("WARN", f"{tag}: many emoji. Keep it readable."))
    hashtags = re.findall(r"#\w+", draft)
    if platform == "instagram" and len(hashtags) > 15:
        out.append(("WARN", f"{tag}: {len(hashtags)} hashtags. Fewer, "
                            "relevant ones read better."))
    if platform == "x" and len(hashtags) > 2:
        out.append(("WARN", f"{tag}: {len(hashtags)} hashtags. One or two "
                            "is enough."))
    if platform == "sms" and "stop" not in draft.lower():
        out.append(("INFO", f"{tag}: bulk texts to people who have not agreed "
                            "can breach spam rules. Send only to people who "
                            "know you."))
    if re.search(r"\[(?:NEEDED|ADD|YOUR|INSERT)[^\]]*\]", draft, re.I):
        out.append(("ERROR", f"{tag}: has an unfilled [NEEDED] placeholder."))


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("file")
    ap.add_argument("--platform", default="general")
    ap.add_argument("--donate-url", default="")
    args = ap.parse_args()
    try:
        text = Path(args.file).read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        print(f"ERROR: cannot read {args.file}: {exc}")
        return 2
    drafts = split_drafts(text)
    if not drafts:
        print("ERROR: no drafts found.")
        return 2
    out = []
    for i, d in enumerate(drafts, 1):
        check(d, i, args.platform.lower(), args.donate_url.strip(), out)
    order = {"ERROR": 0, "WARN": 1, "INFO": 2}
    for level, msg in sorted(out, key=lambda x: order[x[0]]):
        print(f"{level:<6} {msg}")
    errs = sum(1 for lv, _ in out if lv == "ERROR")
    warns = sum(1 for lv, _ in out if lv == "WARN")
    print(f"\nDrafts: {len(drafts)}  Errors: {errs}  Warnings: {warns}")
    print("RESULT: " + ("FAILED" if errs else "PASSED"))
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
