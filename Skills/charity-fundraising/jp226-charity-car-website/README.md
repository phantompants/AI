# JP226 Charity Car Website

Created by JP226Prints.

Builds a fundraising website for a charity themed car or team, such as a charity rally, drive, 4WD adventure or car show entry. It is based on the Car Website guide in JP226Prints Prompt Studio.

## What it does

1. Reads any existing site or page first, then asks for what is missing: the team story, event details and history, the charity's official donation page, sponsors, photos and the contact channels the team really uses.
2. Writes a one-page brief for you to approve.
3. Builds a fast, accessible one-page site from a ready template, in your livery colours, with light and dark modes.
4. Checks the site for general problems and for fundraising problems, then looks at it on desktop and phone.
5. Gives you a hosted preview and a zip of the files, plus a list of anything still to fill in.

## Fundraising rules built in

- The donate button goes to the charity's own official donation page. The site never takes payments or personal financial details.
- Money figures always carry an "as at" date.
- Nothing is invented: no made-up totals, sponsors, quotes or endorsements.
- Sponsors, the charity's logo and people in photos need permission first.
- The footer says who runs the page and where donations go.
- Named children or families and the charity's own statistics are left out unless consent and wording are confirmed. The page links to the charity instead.
- Event dates are taken from the organiser's page, and past-event dates are labelled as checked or from the team's own records.

The checker will not pass the site while the donation link is missing or still a placeholder.

## Install

Add the `.skill` file to Claude as a skill. The optional checks need Python 3 and Chromium with Playwright, which the Claude workspace already has.

## Usage

```
> build a website for our charity rally team
> we need a fundraising page for our 4WD adventure car
> /jp226-charity-car-website
```

Have these ready if you can: the address of your current site or Facebook page, the charity's official donation link, your team story, event dates, the car's details, sponsor names and logos (with their agreement), photos, and which social or messaging accounts you check regularly.

## Files

- `SKILL.md`: the instructions Claude follows
- `assets/template/index.html`: the starting page
- `references/`: brief template, fundraising rules, image preparation, publishing options, and copy-paste prompts for website builders, reviews and updates
- `scripts/check_site.py`: general quality check
- `scripts/check_charity_site.py`: fundraising checks
- `scripts/screenshot.py`: desktop and phone screenshots

## Related skills and feedback

See `references/ai-prompts.md` for related JP226 skills (update writer, theme planner, image prep) and how to report problems.

## Troubleshooting

**The checker says the donation link is a placeholder.** Paste in the charity's official donation page address and run it again.

**I do not have photos yet.** The site is built with labelled stand-ins, and the missing photos are listed for you.

**The contact form does not send email.** Static sites cannot send email. Use email and phone, an "Email us" button, message links for the accounts you check (Messenger, Instagram, WhatsApp), or a Google Form link. See `references/publishing-options.md`.

**Can it rebuild my old site?** Yes. Give it the address and it reads the site first. Social pages often block it, so paste the text or attach screenshots, and attach the original photo files.

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
