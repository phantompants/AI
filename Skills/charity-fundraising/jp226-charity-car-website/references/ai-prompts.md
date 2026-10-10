# Prompts and the website-builder path

Use this file when the user is not building with Claude's files and checks, for example when they use a hosted website builder, or want to check a live site with another AI tool. These prompts work in any AI tool. The AI cannot run the checker scripts, so a person must still check every link, name and number.

## 1. What to ask a website builder for

Paste this with the brief and the real photos attached:

```
Build a one-page fundraising website for [team name], supporting [charity].
Use only the facts and files I give you. Do not invent totals, sponsors, quotes or results.
- The Donate button goes only to [official donation page URL], near the top and again under "How to help".
- Any money figure shows an "as at [date]" or is left out.
- Footer: "Run by [team name], a team supporting [charity]. Donations go directly to [charity]."
- No named child or family unless I confirm written consent. Link to the charity's own stories page instead.
- No copied charity statistics. Link to the charity's own site instead.
- Contact: show [email] and [phone] as text, plus one button for each account we check: [list].
- Sponsors: names only for those who agreed: [list].
- Colours from the car: [colours]. Readable text in light and dark.
- Alt text on every image. Works on a phone first.
- Put [NEEDED: ...] wherever a fact is missing.
```

Check the builder's cost, how to export your files, and whether it adds its own branding or tracking.

## 2. Review prompt for a live site

```
Review this fundraising website: [address, or paste the text].
Report problems only, in a table: what, where, and how to fix it. Check:
1. Every link works. The Donate button goes to the charity's official page only.
2. Every money figure has a date, or is removed.
3. No placeholder text such as [NEEDED] or lorem ipsum.
4. No named child or family, and no charity statistics copied from the charity.
5. Sponsors and logos shown only with permission.
6. The footer says who runs the page and that donations go to the charity.
7. Contact options are clear and the address or number is shown as text.
8. Images have alt text. Text is readable on a phone.
9. Spelling and dates are consistent. Flag anything you cannot verify.
Do not guess. Say "cannot check" where you cannot.
```

## 3. Update prompt after a milestone

```
Update this fundraising page after: [milestone].
Change only what I list: [changes]. Keep the Donate link and footer notice as they are.
If I give a money figure, add "as at [date]". Add one dated entry to Updates.
Show the changed text only, then list anything you are unsure of.
```

After the event, ask for a thank-you and the final dated total.

## 4. Related JP226 skills

- `jp226-fundraising-update-writer`: sponsor thank-yous, milestone posts and captions.
- `jp226-charity-rally-theme-planner`: a theme and puns for the car and team.
- `jp226-web-image-prep`: cropping, compressing and naming photos.

Social posts and updates from the studio's prompt library do not carry team details across, so supply the facts each time.

## 5. Feedback

Problems or ideas for this skill can be raised as an issue at https://github.com/phantompants/AI/issues (a GitHub account is needed).
