#!/usr/bin/env python3
"""
Prepare photos and logos for a website.

Author: JP226Prints
Version: v1.00

Usage:
    python3 prep_images.py SRC OUT [options]

    SRC   a folder of images (or a single image file). Never changed.
    OUT   the folder for web-ready copies and manifest.csv.

Options:
    --prefix NAME        start of generated file names (default: site)
    --hero FILE          this file is the hero image (can repeat)
    --logo FILE          this file is a logo (can repeat)
    --sponsor FILE       this file is a sponsor logo (can repeat)
    --rename OLD=NEW     give a file a descriptive name, without extension
                         (can repeat), for example IMG_4021.jpg=team-car-front
    --format jpg|webp    format for photos (default: jpg)
    --quality N          starting quality for photos (default: 82)

Everything else is treated as a gallery photo.

What it does to each image:
  - fixes the rotation, then removes ALL hidden metadata, including GPS
    location, camera details and dates
  - resizes to the width for its role and compresses to its size budget
  - writes a descriptive file name
  - records everything in manifest.csv, with an empty alt_text column to fill

Role      max width   budget
hero      1600 px     300 KB
gallery   1000 px     150 KB
logo       400 px      50 KB
sponsor    400 px      50 KB

Exit codes: 0 all files handled, 1 one or more files could not be processed.
"""

import argparse
import csv
import re
import shutil
import sys
from pathlib import Path

try:
    from PIL import Image, ImageOps
except ImportError:
    print("ERROR: Pillow is not installed (pip install pillow).")
    sys.exit(1)

ROLES = {
    "hero": (1600, 300),
    "gallery": (1000, 150),
    "logo": (400, 50),
    "sponsor": (400, 50),
}
MIN_WIDTH = 600
IMAGE_EXT = {".jpg", ".jpeg", ".png", ".webp"}
CAMERA_NAME = re.compile(
    r"^(img|dsc|dscn|dscf|pxl|mvimg|screenshot|photo|image|pic|p)[-_ ]?\d+",
    re.I)
GPS_TAG = 0x8825


def slug(text):
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    return text or "image"


def has_gps(img):
    try:
        return bool(img.getexif().get_ifd(GPS_TAG))
    except Exception:
        return False


def encode(img, path, fmt, quality):
    """Save without any metadata. Returns size in KB."""
    params = {}
    if fmt == "jpg":
        if img.mode not in ("RGB", "L"):
            img = img.convert("RGB")
        params = {"quality": quality, "optimize": True, "progressive": True}
        img.save(path, "JPEG", **params)
    elif fmt == "webp":
        params = {"quality": quality, "method": 6}
        img.save(path, "WEBP", **params)
    else:  # png
        img.save(path, "PNG", optimize=True)
    return path.stat().st_size / 1024


def fit_budget(img, path, fmt, quality, budget_kb):
    """Lower quality, then width, until under budget. Returns final size."""
    work = img
    q = quality
    size = encode(work, path, fmt, q)
    while size > budget_kb and fmt != "png" and q > 60:
        q -= 6
        size = encode(work, path, fmt, q)
    while size > budget_kb and work.width * 0.9 >= MIN_WIDTH:
        new_w = int(work.width * 0.9)
        new_h = int(work.height * new_w / work.width)
        work = work.resize((new_w, new_h), Image.LANCZOS)
        size = encode(work, path, fmt, q)
    if size > budget_kb and fmt == "png":
        # logos: try a smaller palette before giving up
        pal = work.convert("RGBA").quantize(colors=128, method=Image.FASTOCTREE)
        pal.save(path, "PNG", optimize=True)
        size = path.stat().st_size / 1024
    return work, size


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("src")
    ap.add_argument("out")
    ap.add_argument("--prefix", default="site")
    ap.add_argument("--hero", action="append", default=[])
    ap.add_argument("--logo", action="append", default=[])
    ap.add_argument("--sponsor", action="append", default=[])
    ap.add_argument("--rename", action="append", default=[])
    ap.add_argument("--format", default="jpg", choices=["jpg", "webp"])
    ap.add_argument("--quality", type=int, default=82)
    args = ap.parse_args()

    src = Path(args.src)
    out = Path(args.out)
    files = [src] if src.is_file() else sorted(p for p in src.iterdir()
                                              if p.is_file())
    if not src.exists() or not files:
        print(f"ERROR: nothing to process in {src}")
        return 1
    if src.is_dir() and out.resolve().is_relative_to(src.resolve()):
        print("ERROR: OUT must not be inside SRC.")
        return 1

    role_of = {}
    for r, names in (("hero", args.hero), ("logo", args.logo),
                     ("sponsor", args.sponsor)):
        for n in names:
            role_of[Path(n).name] = r
    renames = {}
    for pair in args.rename:
        if "=" not in pair:
            print(f"ERROR: --rename needs OLD=NEW, got '{pair}'")
            return 1
        old, new = pair.split("=", 1)
        renames[Path(old).name] = slug(Path(new).stem)

    img_dir = out / "images"
    img_dir.mkdir(parents=True, exist_ok=True)
    counters = {}
    rows, failures, gps_total = [], 0, 0

    for f in files:
        ext = f.suffix.lower()
        role = role_of.get(f.name, "gallery")
        if ext == ".svg":
            role = role if role in ("logo", "sponsor") else "logo"
            text = f.read_text(encoding="utf-8", errors="replace")
            note = "copied as is"
            if "<script" in text.lower():
                note = "WARNING: SVG contains a script. Remove it before use."
            name = renames.get(f.name) or slug(f.stem)
            dest = img_dir / f"{name}.svg"
            shutil.copyfile(f, dest)
            rows.append([f.name, dest.name, role, "", "",
                         f"{dest.stat().st_size/1024:.1f}", "no", "n/a", "",
                         note])
            print(f"OK     {f.name} -> {dest.name}  {role}  svg  [{note}]")
            continue
        if ext not in IMAGE_EXT:
            print(f"SKIP   {f.name}: not a supported image "
                  f"({ext or 'no extension'}). HEIC files need converting "
                  "to JPG first.")
            continue
        try:
            with Image.open(f) as raw:
                raw.load()
                gps = has_gps(raw)
                img = ImageOps.exif_transpose(raw)
                img = img.copy()
        except Exception as exc:  # unreadable or corrupt
            print(f"FAIL   {f.name}: {exc}")
            failures += 1
            continue

        max_w, budget = ROLES[role]
        notes = []
        if img.width < max_w * 0.6 and role in ("hero", "gallery"):
            notes.append(f"small original ({img.width}px wide); may look soft")
        if img.width > max_w:
            h = int(img.height * max_w / img.width)
            img = img.resize((max_w, h), Image.LANCZOS)

        has_alpha = img.mode in ("RGBA", "LA") or "transparency" in img.info
        if role in ("logo", "sponsor"):
            fmt = "png"
            if not has_alpha:
                img = img.convert("RGB")
        else:
            fmt = args.format
            if has_alpha:
                img = img.convert("RGBA")
                bg = Image.new("RGB", img.size, (255, 255, 255))
                bg.paste(img, mask=img.split()[3])
                img = bg
                notes.append("transparency flattened onto white")

        counters[role] = counters.get(role, 0) + 1
        if f.name in renames:
            base = renames[f.name]
        elif CAMERA_NAME.match(f.stem) or f.stem.isdigit():
            base = f"{slug(args.prefix)}-{role}-{counters[role]:02d}"
            notes.append("rename me: use --rename for a descriptive name")
        else:
            base = slug(f.stem)
        dest = img_dir / f"{base}.{'png' if fmt == 'png' else fmt}"
        n = 2
        while dest.exists():
            dest = img_dir / f"{base}-{n}.{dest.suffix.lstrip('.')}"
            n += 1

        final, size = fit_budget(img, dest, fmt, args.quality, budget)
        over = size > budget
        if over:
            notes.append(f"over the {budget} KB budget at {size:.0f} KB")
        if gps:
            gps_total += 1
        rows.append([f.name, dest.name, role, final.width, final.height,
                     f"{size:.1f}", "YES" if over else "no",
                     "yes" if gps else "none found", "", "; ".join(notes)])
        print(f"OK     {f.name} -> {dest.name}  {role}  "
              f"{final.width}x{final.height}  {size:.0f} KB"
              + ("  [GPS location removed]" if gps else "")
              + (f"  [{'; '.join(notes)}]" if notes else ""))

    manifest = out / "manifest.csv"
    with open(manifest, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["original", "output", "role", "width", "height", "kb",
                    "over_budget", "gps_removed", "alt_text", "notes"])
        w.writerows(rows)

    print(f"\nProcessed {len(rows)} image(s). Failed: {failures}. "
          f"GPS location removed from {gps_total}.")
    print(f"Manifest: {manifest} (fill in the alt_text column)")
    print("Originals were not changed.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
