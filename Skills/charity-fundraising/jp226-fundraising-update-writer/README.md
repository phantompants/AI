# JP226 Fundraising Update Writer

Created by JP226Prints.

Writes honest messages for a charity team: sponsor requests, thank-yous, milestone posts, event updates and a final thank-you. It checks every draft before you send it.

## What it does

1. Asks what you need to say, to whom, and where it will be posted.
2. Asks for the real facts: the charity's donation link, your current figure and its date, who has agreed to be named.
3. Drafts messages for each channel in your team's voice.
4. Runs a checker that blocks requests for bank or card details, figures with no date, pressure wording ("last chance"), claims such as "100%" or "tax deductible", platform length overruns and missing donation links.

## Install

Add the `.skill` file to Claude as a skill. The checker needs Python 3.

## Usage

```
> write a sponsor email for our rally team
> post about reaching our halfway mark
> thank everyone who donated this week
> /jp226-fundraising-update-writer
```

## Files

- `SKILL.md`: the instructions Claude follows
- `scripts/check_posts.py`: the draft checker
- `references/message-rules.md`: rules and safe wording
- `references/templates.md`: message shapes

## Troubleshooting

**The checker blocks my draft for asking for money.** Donations must go to the charity's own page. Remove any bank, PayID or cash request and link to the page instead.

**It wants an "as at" date.** Add the date the figure was true, for example "as at 9 October".

**Is this legal advice?** No. Check the charity's guidelines and your state or territory's fundraising rules.

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
