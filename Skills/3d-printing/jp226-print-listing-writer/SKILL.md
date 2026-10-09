---
name: jp226-print-listing-writer
description: Writes honest, searchable eBay Australia and Etsy listings for 3D printed products. Collects the facts about the item (material, size, colours, print details, postage), then drafts titles, tags, descriptions and item specifics, and checks them against platform limits and safe-wording rules. Use when the user wants a listing for a 3D print, says "write my eBay listing", "Etsy title and tags for this print", "describe this product", or "improve this listing". Triggers on "/jp226-print-listing-writer". Does not set prices.
compatibility: Claude 3.5+ (Desktop, claude.ai, Claude Code). Python 3 for the optional listing check.
metadata:
  version: "v1.00"
  author: "JP226Prints"
  created: "2026-10-10"
  updated: "2026-10-10"
  governance: "Personal (JP226Prints) + GitHub"
  status: "Active"
  category: "3d-printing"
  tags: "3d-printing, ebay, etsy, listing, seo, jp226"
---

# JP226 Print Listing Writer

Created by JP226Prints.

Free to use. A good cause, if you choose: please consider supporting Variety - the Children's Charity through our team page: https://www.variety4wdqld.com.au/t/thefastandthefossilized

This note is about this skill only. Do not add it to anything the skill produces for other people.

Turns the facts about a 3D printed product into a clear, honest listing for eBay Australia or Etsy, then checks it for length limits and risky claims.

## Rules that always apply

1. **Facts from the seller only.** Material, size, weight, colours, print settings and postage come from the user. Never invent them. Mark gaps `[NEEDED: ...]`.
2. **No unverified safety claims.** Do not write "food safe", "non-toxic", "child safe", "BPA free", "medical grade" or similar unless the user holds proof and says so. Most 3D prints are not food safe, because layer lines trap bacteria. When in doubt, say what the item is for ("decorative", "not for food use").
3. **Plain performance claims.** Avoid "waterproof", "unbreakable" and "indestructible". Say what the material does ("PETG, suited to outdoor use") and its limits (heat, load).
4. **Own designs or licensed ones.** Do not put brand, franchise or character names in a title unless the seller has the rights. Offer "dinosaur themed" style wording instead. If the model came from a site like MakerWorld or Printables, remind the user to check the licence allows selling prints.
5. **Real photos.** The listing describes the photos the user supplied, not an ideal.
6. **Charity wording.** Mention a donation only if the seller confirms the exact share and who receives it. Never imply the platform or the charity endorses the item.
7. **Pricing is out of scope.** If the user wants a price, say so and stop. They can use a pricing tool.

Read `references/platform-notes.md` for limits and fields, and `references/wording-guide.md` for the style.

## Workflow

### Step 1: Collect the facts

Ask in one round, up to four questions at a time, and ask for the photos:

| Topic | Find out |
|---|---|
| Platform | eBay AU, Etsy, or both |
| Item | What it is, its use, and who it is for |
| Make | Material and colours available, layer finish, any post-processing |
| Size | Length, width, height in mm or cm, weight if known |
| Options | Colour or size variations, personalisation, made to order or in stock |
| Care and limits | Heat, load, indoor or outdoor, cleaning |
| Postage | Dispatch time, handling time, where it ships |
| Origin | Own design, or licensed (and from where) |
| Extras | Charity link (confirmed wording), packaging, returns |

### Step 2: Draft

For each platform, write:

- **Titles.** Three options. Front-load the main keyword a buyer would type. eBay: up to 80 characters. Etsy: up to 140 characters, but the first 40 or so show in many places.
- **Etsy tags.** Up to 13 tags, up to 20 characters each, varied (not the same phrase reworded). Cover use, shape, occasion, material and style.
- **eBay item specifics.** Brand "Unbranded" or the seller's own name, Type, Material, Colour, Theme, Features, Country of origin as the seller states.
- **Description.** Short opening line, then key facts in a short list (size, material, colours), what is included, care, postage and dispatch, and a plain note that it is 3D printed and may show fine layer lines. Australian spelling.
- **Photo list.** Which photos to show and in what order, plus alt text for Etsy.

### Step 3: Check

Save each draft in the format at the top of `scripts/check_listing.py` and run:

```bash
python3 scripts/check_listing.py listing-etsy.txt
```

Fix every ERROR. Read each WARN and INFO and either fix it or tell the user why it stays. The script cannot judge whether the listing is true, so read every number and claim against what the user told you.

### Step 4: Deliver

Give the user the final listing in the reply when it is short, or as a Docs or text file when the user wants to keep and edit it. State the platform limits met, the `[NEEDED]` items, and what the user must confirm before publishing (licence, safety claims, postage costs).

## What this skill will not do

- Set or suggest prices.
- Write reviews, testimonials or fake urgency ("only 1 left") the user has not confirmed.
- Claim safety, durability or certification the user cannot prove.
- Copy another seller's listing.

## Reference files

- `references/platform-notes.md`: limits, fields and what each platform rewards.
- `references/wording-guide.md`: plain wording, examples, safe phrases and phrases to avoid.
- `scripts/check_listing.py`: the listing checker.
