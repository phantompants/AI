# JP226 Web Image Prep

Created by JP226Prints.

Gets photos and logos ready for a website. It fixes the rotation, removes hidden location and camera data, resizes and compresses each image to a sensible web size, gives it a descriptive name, and writes a manifest with a column for alt text.

## What it does

1. Asks which images are the hero photo, logos and sponsor logos.
2. Makes web copies in a separate folder. Your originals are never changed.
3. Removes GPS location, camera details and dates from every copy, and tells you how many photos had a location.
4. Sizes each image for its job: hero 1600 px wide (300 KB), gallery 1000 px (150 KB), logos 400 px (50 KB).
5. Writes `manifest.csv` listing every file, and helps you fill in the alt text.

## Install

Add the `.skill` file to Claude as a skill. The script needs Python 3 and Pillow (`pip install pillow`).

## Usage

```
> get these photos ready for my website
> shrink these pictures and take the location out
> write alt text for my gallery
> /jp226-web-image-prep
```

You can also run the script yourself:

```
python3 scripts/prep_images.py photos web-ready --prefix team --hero IMG_1.jpg --logo logo.png
```

## Files

- `SKILL.md`: the instructions Claude follows
- `scripts/prep_images.py`: the preparation script
- `references/alt-text-guide.md`: how to write good alt text

## Troubleshooting

**A file was skipped.** Only JPG, PNG, WebP and SVG are handled. Convert HEIC photos to JPG first.

**An image is over its size budget.** The original may be very detailed. Crop it, or choose `--format webp`.

**An SVG logo shows a warning.** It contains a script. Remove the script before putting it on a site.

## Supporting a good cause

This skill is free to use. A good cause, if you choose: if it helps you, please consider a voluntary donation to our Variety fundraising team, The Fast and the Fossilized. Donations are entirely optional and do not unlock anything.

- [Donate to The Fast and the Fossilized](https://www.variety4wdqld.com.au/t/thefastandthefossilized)
- [JP226 Creative Studio](https://jp226creativestudio.au)
- [JP226Prints](https://jp226prints.au)
- [JP226 Prompt Library](https://jp226prompts.au)

Donations are made on the fundraising page for the 2026 Variety 4WD Adventure. We do not collect or handle donations.

## Licence

MIT. Use, change and share freely.

Author: JP226Prints
