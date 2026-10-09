# JP226 Print Listing Writer

Created by JP226Prints.

Writes clear, honest eBay Australia and Etsy listings for 3D printed products, then checks them against platform limits and risky claims. It does not set prices.

## What it does

1. Asks for the facts: item, material, size, colours, care, postage and where the design came from.
2. Drafts three title options, Etsy tags, eBay item specifics, a description and a photo list.
3. Runs a checker that flags titles that are too long, too many or too long Etsy tags, unverified safety claims such as "food safe", brand and trademark names, American spellings and unconfirmed charity wording.
4. Hands back the finished listing and a short list of things you must confirm yourself.

## Install

Add the `.skill` file to Claude as a skill. The checker needs Python 3.

## Usage

```
> write an Etsy listing for my dinosaur pen holder
> eBay title and description for this print
> check this listing
> /jp226-print-listing-writer
```

Have ready: what it is, the material and colours, the size in mm, how long it takes to make, postage details, and photos.

## Files

- `SKILL.md`: the instructions Claude follows
- `scripts/check_listing.py`: the listing checker
- `references/platform-notes.md`: eBay and Etsy limits and fields
- `references/wording-guide.md`: wording, safe phrases and an example

## Troubleshooting

**The checker flags "food safe".** Remove it unless you hold a test report. Most 3D prints are not food safe.

**It flags a brand name.** Selling prints that use a film, game or brand name without a licence can get listings removed. Use a themed description instead.

**Limits changed.** Platforms update rules. Check the seller tools before you publish.

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
