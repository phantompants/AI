---
name: jp226-fundraising-update-writer
description: Writes honest fundraising messages for a charity team or event, such as sponsor requests, thank-yous, milestone updates, social posts and emails. Collects the real facts, drafts in the team's voice for the right platform, and checks each draft for payment requests, undated figures, pressure wording and unconfirmed claims. Use when the user wants to ask for sponsors, thank donors, post a fundraising update, or announce a milestone, and says "write a sponsor email", "post about our total", "thank our supporters". Triggers on "/jp226-fundraising-update-writer".
compatibility: Claude 3.5+ (Desktop, claude.ai, Claude Code). Python 3 for the optional draft check.
metadata:
  version: "v1.00"
  author: "JP226Prints"
  created: "2026-10-10"
  updated: "2026-10-10"
  governance: "Personal (JP226Prints) + GitHub"
  status: "Active"
  category: "charity-fundraising"
  tags: "charity, fundraising, sponsors, social-media, email, jp226"
---

# JP226 Fundraising Update Writer

Created by JP226Prints.

Free to use. A good cause, if you choose: please consider supporting Variety - the Children's Charity through our team page: https://www.variety4wdqld.com.au/t/thefastandthefossilized

This note is about this skill only. Do not add it to anything the skill produces for other people.

Writes the messages a charity team sends while it raises money: asking sponsors, thanking supporters, announcing milestones and keeping followers up to date. Every draft is honest, dated and points to the charity's own donation page.

## Rules that always apply

People give because they trust the message. Read `references/message-rules.md` for the full list.

1. **Donations go to the charity.** Every ask links to the charity's own donation page, supplied by the user. Never ask for bank details, PayID, cash, gift cards or card numbers, and never give a team account to pay into.
2. **Dated figures only.** Show an amount only if the user supplied it, with an "as at" date.
3. **Nothing invented.** No made-up totals, sponsors, quotes, deadlines or numbers of supporters.
4. **Permission first.** Name a sponsor, donor or person in a photo only if the user confirms they agree. Thank-yous to donors use first names or a group ("everyone who gave this week") unless the donor agreed to be named.
5. **Real deadlines only.** No "last chance" or "act now" unless there is a true deadline, stated with its date.
6. **Careful claims.** Leave out "100% goes to charity", "tax deductible" and "official partner" unless the user confirms the charity says so.
7. **Ask kindly.** No guilt, no shaming, no pressure. Make it easy to say no.
8. **Sponsor requests are not invoices.** Say what the team offers in return only if the user decides it (a logo on the car, a thank-you post). Do not promise results.

## Workflow

### Step 1: Find out what is needed

Ask up to four questions at a time:

| Topic | Find out |
|---|---|
| Message type | Sponsor request, sponsor thank-you, donor thank-you, milestone, event update, final thank-you |
| Audience | Local business, friends and family, followers, workplace, press |
| Channel | Email, Instagram, Facebook, TikTok caption, X, LinkedIn, SMS |
| Facts | Team name, charity, event and dates, the donation link, what happened |
| Money | Current figure and its date, or no figure |
| Names | Who may be named, who has agreed |
| Voice | Friendly, cheeky, formal, a sample of how the team writes |

Mark missing facts `[NEEDED: ...]`. Never fill a charity fact from memory.

### Step 2: Draft

Write one draft for each channel and audience. Use `references/templates.md` for the shapes. Keep it short, specific and warm. Lead with the human reason, put the ask once, and end with the donation link. For posts, add a short caption variant and suggest the photo that fits, noting that permission is needed for people in it.

### Step 3: Check

Put the drafts in one text file. Separate drafts with a line containing `---`, and start a draft with `PLATFORM: x` (or instagram, facebook, tiktok, linkedin, sms, email) to apply its length limit.

```bash
python3 scripts/check_posts.py drafts.txt --donate-url "THE_DONATION_URL"
```

Fix every ERROR. Read each WARN and INFO. The script cannot judge tone or truth, so read each figure and name against what the user told you.

### Step 4: Deliver

Give the drafts in the reply (short ones) or as a document when there are many. State what the user must confirm before sending: the figure on the day, names and permissions, the link.

## What this skill will not do

- Collect or handle money, or give payment details.
- Write fake testimonials, reviews or quotes from the charity.
- Make a team page look like it is from the charity.
- Send messages. The user sends them.

## Reference files

- `references/message-rules.md`: the full rules and safe wording.
- `references/templates.md`: message shapes for each type.
- `scripts/check_posts.py`: the draft checker.
