---
name: jp226-web-image-prep
description: Prepares photos and logos for a website. Fixes rotation, removes hidden location and camera data, resizes and compresses to sensible web sizes, gives descriptive file names, and writes a manifest with a column for alt text. Use when the user has photos, logos or sponsor logos to put on a website, says "get these images ready for the web", "shrink these photos", "my site is slow because of the pictures", "remove the location from my photos", or needs alt text written. Triggers on "/jp226-web-image-prep".
compatibility: Claude 3.5+ (Desktop, claude.ai, Claude Code). Python 3 with Pillow.
metadata:
  version: "v1.00"
  author: "JP226Prints"
  created: "2026-10-10"
  updated: "2026-10-10"
  governance: "Personal (JP226Prints) + GitHub"
  status: "Active"
  category: "images-and-design"
  tags: "images, web, alt-text, privacy, optimisation, jp226"
---

# JP226 Web Image Prep

Created by JP226Prints.

Free to use. A good cause, if you choose: please consider supporting Variety - the Children's Charity through our team page: https://www.variety4wdqld.com.au/t/thefastandthefossilized

This note is about this skill only. Do not add it to anything the skill produces for other people.

Turns a folder of raw photos and logos into small, safe, well-named web copies, and helps write the alt text for each one.

## Rules that always apply

1. **Never change the originals.** Work on copies. The script writes to a separate output folder and refuses an output folder inside the source.
2. **Remove hidden data.** Phone photos carry GPS location, camera details and dates. The script strips all of it and reports how many photos had a location.
3. **Only use images the user supplied.** Do not fetch stock photos. A description of a photo is not a photo.
4. **Permission.** Ask before using photos of identifiable people, especially children, and before using a sponsor's or charity's logo.
5. **Do not invent alt text.** Write it only from what can be seen in the image or what the user told you.

## Workflow

1. **Collect.** Ask the user to attach the images. Ask which is the hero image, which are logos, and which are sponsor logos. Ask for a short prefix for names (for example the team or business name). HEIC files must be converted to JPG first; say so if any turn up.
2. **Run the script.**

```bash
python3 scripts/prep_images.py SRC OUT --prefix team --hero IMG_1.jpg --logo logo.png --sponsor acme.png --rename IMG_4021.jpg=team-car-front
```

| Role | Max width | Budget |
|---|---|---|
| hero | 1600 px | 300 KB |
| gallery | 1000 px | 150 KB |
| logo, sponsor | 400 px | 50 KB |

Use `--format webp` for smaller photos if the site supports it. Logos stay as PNG, and SVG logos are copied as is (the script warns if an SVG contains a script).
3. **Read the report.** Look for `over_budget`, `small original` and `rename me` notes. Give camera-named files a descriptive name with `--rename` and run again. Re-running into a fresh output folder is safe.
4. **Write alt text.** Open the images, then fill the `alt_text` column in `manifest.csv`. Read `references/alt-text-guide.md` first. Logos and decorative images follow special rules there.
5. **Deliver.** Send the `images/` folder as a zip and the completed `manifest.csv`. State how many photos had a location removed, which images are still over budget, and what the user still needs to check (permissions, names of people).

## What this skill will not do

- Edit or delete the user's originals.
- Add watermarks, filters or retouching.
- Identify people in photos by their faces.
- Guess where or when a photo was taken.

## Reference files

- `references/alt-text-guide.md`: how to write alt text, with examples.
- `scripts/prep_images.py`: the preparation script.
