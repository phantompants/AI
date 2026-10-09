---
name: jp226-charity-rally-theme-planner
description: Helps a charity rally or drive team choose a car theme, team name and handles, then turns the choice into a one-page theme brief. Brainstorms themes, checks what other teams have used, tests names for handle and domain format, and covers livery, costumes and a story that suits the cause. Use when a team is deciding a theme or name, says "what theme should our rally car be", "help us name our team", "we need a team name and handle", or "plan our charity car theme". Triggers on "/jp226-charity-rally-theme-planner". The brief feeds the jp226-charity-car-website skill.
compatibility: Claude 3.5+ (Desktop, claude.ai, Claude Code). Web search is used to check ideas. Python 3 for the optional handle check.
metadata:
  version: "v1.00"
  author: "JP226Prints"
  created: "2026-10-10"
  updated: "2026-10-10"
  governance: "Personal (JP226Prints) + GitHub"
  status: "Active"
  category: "charity-fundraising"
  tags: "charity, rally, theme, team-name, branding, car, jp226"
---

# JP226 Charity Rally Theme Planner

Created by JP226Prints.

Free to use. A good cause, if you choose: please consider supporting Variety - the Children's Charity through our team page: https://www.variety4wdqld.com.au/t/thefastandthefossilized

This note is about this skill only. Do not add it to anything the skill produces for other people.

Takes a team from "we have a car and a cause" to a clear theme, a team name, handle ideas, a livery direction and a one-page theme brief. The brief carries straight into the `jp226-charity-car-website` skill.

## Rules that always apply

1. **Original or licensed.** A theme can nod to a film, game or brand, but do not copy its logos, characters or artwork onto the car or merchandise without permission. Offer a clear homage: wording, colour palette, props, costumes and puns, not copied artwork.
2. **Do not look official.** Team names, handles and designs must not suggest the team is the charity or an official partner. Avoid words such as "official" or the charity's own brand in handles.
3. **Check, do not assume.** A name is not free until the user checks each app and a domain registrar. The script checks format only. Search the web for other teams with the same theme or name, and report what you found with its source.
4. **Event rules first.** Ask for the event's rules on vehicles, livery, costumes and sponsor logos, and fit the theme inside them. Do not invent the rules.
5. **Suit the cause.** Keep the theme fun, inclusive and safe for children. Avoid jokes at the expense of people, illness or disability.
6. **Safety.** Props, costumes and decorations must not block vision, lights, number plates or driver safety. Raise this on any build idea.
7. **Ask before using photos or names** of people, sponsors or other teams.

## Workflow

### Step 1: Find out the starting point

Ask up to four questions at a time:

| Topic | Find out |
|---|---|
| Event and cause | Event name, dates, the charity, any theme the event requires |
| Car | Make, model, colour, size, what can and cannot be changed |
| Team | Size, ages, interests, budget and skills for a build |
| Taste | Films, games, animals, eras, jokes the team loves. Anything off limits |
| Rules | Event rules on livery, costumes, decals and sponsor logos |
| Assets | Existing name, logo, colours or handles |

### Step 2: Brainstorm

Offer 8 to 12 themes in three groups: classic crowd-pleasers, funny and punny, and unusual. Each gets a one-line pitch, a team name idea, a livery direction and one risk (licence, event rules, cost). Let the user pick up to three.

### Step 3: Check the shortlist

1. Web search for the theme and name with the event name, to see if other teams used it. Report findings with sources, and say if the search found nothing, without claiming it is unique.
2. Run the format check on the name candidates:

```bash
python3 scripts/handle_check.py "Name one" "Name two"
```

3. Ask the user to confirm availability by hand in Instagram, TikTok, YouTube, X and a domain registrar. Do not tell the user a handle is free.

Read `references/naming-guide.md` for how to make a name that is short, spellable and says what the team is.

### Step 4: Build out the choice

For the chosen theme, cover:

- **Livery direction.** Colours (with hex values if the user wants), decals, wraps, what to do with doors and bonnet, and where sponsor logos fit.
- **Team presentation.** Costumes, props, banners, sounds. Keep it safe and legal.
- **Story.** One honest paragraph on why this team is doing this, in the team's voice.
- **Social.** Handle suggestions, a bio line (no unconfirmed claims), and the first three post ideas.
- **Build checklist and rough costs** only if the user gives numbers. Do not invent prices.

Read `references/theme-brief-template.md` and write the brief. Show it to the user and ask them to approve or correct it.

### Step 5: Hand on

Deliver the brief as a document the user can keep. Tell the user the brief can go straight into `jp226-charity-car-website`, where its team story, colours and name are used. List what is still `[NEEDED]` and what the user must confirm.

## What this skill will not do

- Draw or copy a known film, game or brand character or logo.
- Say a name or handle is available.
- Invent event rules, prices or sponsors.
- Make the team look like the charity or an official partner.

## Reference files

- `references/naming-guide.md`: how to choose a team name and handles.
- `references/theme-brief-template.md`: the one-page theme brief.
- `scripts/handle_check.py`: handle and domain format check.
