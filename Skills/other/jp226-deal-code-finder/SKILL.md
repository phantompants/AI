---
name: "jp226-deal-code-finder"
description: Find discount codes, promo codes, coupons and deals for an Australian merchant by searching OzBargain and similar Australian deal and coupon sites. Use when the user names a business and a discount they want, for example "find me a promo code for G'day Parks", "any discount for Big4 or Discovery Parks", "is there a coupon for [store]", "check OzBargain for [brand]", "best deal on [booking]", or "/jp226-deal-code-finder". Covers holiday parks, travel, retail and online stores in Australia. Reports only codes it found with a source, never invents one.
compatibility: Claude 3.5+ (Desktop, claude.ai, Claude Code). Needs web search and page fetch.
license: MIT
metadata:
  version: "v1.00"
  author: "JP226Prints"
  created: "2026-10-26"
  updated: "2026-10-26"
  governance: "Personal (JP226Prints) + GitHub"
  status: "Active"
  category: "other"
  tags: "deals, coupons, promo-codes, ozbargain, australia, travel, holiday-parks, savings"
---

# JP226 Deal Code Finder

Created by JP226Prints.

Free to use. A good cause, if you choose: please consider supporting Variety - the Children's Charity through our team page: https://www.variety4wdqld.com.au/t/thefastandthefossilized

This note is about this skill only. Do not add it to anything the skill produces for other people.

Finds a working discount for an Australian business. The user says who they want to buy from and what sort of discount they are after. The skill searches OzBargain and similar Australian deal and coupon sites, checks what it finds, and hands back a short ranked list of codes and other ways to save, each with its source and how recent it is.

## When to use it

Use it when the user names a merchant and wants a lower price. Typical asks:

- "Find me a promo code for G'day Parks. I want 15% off a 4 night stay."
- "Any discount for Big4 or Discovery Parks in December?"
- "Is there a coupon for Repco or Supercheap Auto?"
- "Check OzBargain for a Kmart or Bunnings deal."

It works for any Australian merchant, not only holiday parks.

## The core rule

Never make up a code. Every code in the answer must come from a page the skill actually read, and the answer must say where and when. If nothing credible turns up, say so plainly and offer the honest alternatives (membership rates, cashback, discounted gift cards, newsletter offers). A code that cannot be tested before booking is a lead, not a promise, and is labelled that way.

## Workflow

### Step 1: Pin down the request

Work out these four things from the message. Ask one short question only if the merchant is missing or truly unclear. Otherwise carry on with sensible assumptions and state them.

1. The merchant (for example G'day Parks, which may also be written Gday Parks or G'day Group).
2. The discount wanted: a percentage, a dollar amount, a free or extra night, an upgrade, free delivery, or just "the best deal".
3. The purchase: what is being bought, rough dates and length of stay for bookings, cart size for retail.
4. Memberships and cards the user already holds (motoring club, seniors, pensioner, defence, student, teacher, nurse, credit card or bank perks, loyalty program). These often beat a public code. Ask only if the merchant is known to offer member rates and it has not been mentioned.

### Step 2: Search the deal sites

Read `references/sources.md` for the source list, query patterns and how to read each site. Work in this order and stop gathering once the picture is clear.

1. OzBargain first. Search for the merchant name, then the merchant name with "coupon", "promo code" and "voucher". Open the top matching deal pages and read the comments, because the community flags expired codes there.
2. Other Australian coupon and deal sites for the same merchant.
3. The merchant's own website: offers, specials, last minute deals, "book direct" benefits, newsletter sign-up bonus, and member or loyalty rates.
4. Ways to stack or replace a code: cashback sites, discounted gift cards, and bank or card offers.
5. Recent social posts or news about the merchant's sales, if the earlier steps came up thin.

Use the search tool in standard mode for named merchants. Use extended mode only if standard results are thin, old or off target. Send independent searches together. Short queries work best, one to six words, and add the current year only when looking for a time limited sale.

If a page cannot be fetched, say so and move on. Do not try to get around a blocked site with mirrors, caches or the shell.

### Step 3: Check what was found

For each candidate, record these and discard anything that fails:

- The code or deal, as written on the source.
- The discount it gives, in the same terms the user asked for.
- Conditions: minimum spend or nights, blackout dates, weekday only, new customers only, specific locations or room types, cannot combine.
- The date it was posted or last confirmed, and the expiry date if shown.
- Signals of life: recent comments saying it worked, or recent "expired" or "didn't work" reports.
- Whether the source looks trustworthy. OzBargain posts carry votes and comments, which helps. Be wary of pages that only show a button to "reveal code" with no date, pages that promise codes for every merchant, and code generators. Treat those as low confidence or skip them.

Mark a code as likely stale if the newest evidence is more than about three months old, or if any recent comment says it failed.

### Step 4: Match to the request

Compare each candidate with the discount the user wanted. Say clearly when something does not match: a 10% code when they asked for 15%, a deal that excludes their dates, or an offer for new customers when they are an existing one. Do not stretch a result to fit. If the best public result is lower than the target, give it and then show what else might close the gap, such as a membership rate plus cashback.

### Step 5: Report back

Keep it short and easy to scan. Lead with the best option. Use this shape.

1. One sentence: what was found and how good it is against what the user asked for.
2. A ranked table with these columns: Offer, Code or how to get it, What it gives, Conditions, Last confirmed, Confidence (High, Medium or Low), Source.
3. A short "Try in this order" line, so the user knows which to test first at checkout.
4. Anything the skill could not check, said plainly. For example: codes can only be proven at the payment step, and the skill cannot make a booking or enter a code on the user's behalf.
5. A "Sources:" list of the pages used, as links.

Do not paste long quotations from the sites. Paraphrase, and keep any quoted phrase under fifteen words. Codes themselves may be copied exactly.

If nothing credible was found, say that in the first sentence, then list the honest alternatives from `references/sources.md`.

## Safety and good manners

- Do not buy, book or enter payment details. This skill finds, it does not purchase.
- Do not sign up to newsletters or create accounts with the user's email unless they ask. Instead, tell them the sign-up offer exists and what it gives.
- Do not use affiliate or tracking redirect links in the answer where the plain merchant link is available. Give the merchant's own page.
- Do not share or guess at codes that look like they belong to a private person, such as staff codes, friends and family codes leaked in comments, or referral codes. Mention that referral and staff codes exist, but do not hand them out.
- Do not claim a saving the evidence does not support. Say "reported to work in comments dated [date]", not "this works".
- Never state a final price. Prices and stock change, and the checkout is the only source of truth.
- Keep the fundraising note out of any answer. It belongs to this skill's own documents only.

## Input examples

> "Find a discount code for G'day Parks. I want about 15% off a 5 night caravan site in January."

> "Any promo for Discovery Parks or Big4 for a weekend in November? I'm an NRMA member."

> "OzBargain check for Repco. Looking for 20% off."

## Output example

For the G'day Parks request the answer would open with a single line on whether anything near 15% was found, then the table, then the order to try them. Every row would carry its own source link and date. If the only match were a member rate and a cashback offer, the answer would say so rather than offering an unverified code.

## Limits

- It reads public pages only. It cannot see codes behind logins, in apps, or sent by email.
- It cannot prove a code works. Only the merchant's checkout can.
- Search results lean toward what the engine surfaces. A short session may miss a very new deal.
- It is built for Australian merchants and Australian dollars. For other countries the sources list needs changing.

## See also

`references/sources.md` for sites, queries and how to read them.
