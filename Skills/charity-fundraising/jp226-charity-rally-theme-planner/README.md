# JP226 Charity Rally Theme Planner

Created by JP226Prints.

Helps a charity rally or drive team choose a car theme, a team name and handles, then writes a one-page theme brief. The brief can go straight into the `jp226-charity-car-website` skill.

## What it does

1. Asks about your event, car, team and tastes, and the event's rules.
2. Offers 8 to 12 theme ideas, each with a team name idea, a livery direction and one risk.
3. Checks your shortlist: searches the web for other teams using the same theme or name, and tests each name for handle and domain format.
4. Builds out the winner: livery, costumes, story, social starter.
5. Writes the one-page brief for you to approve.

## Good to know

- The handle check tests format only. It cannot tell you whether a name is free. You check each app and a domain registrar yourself.
- Themes can nod to films, games and brands, but the skill will not copy their logos or characters.
- Names and handles should not look like the charity itself or an official partner.

## Install

Add the `.skill` file to Claude as a skill. The handle check needs Python 3.

## Usage

```
> help us choose a theme for our charity rally car
> we need a team name and handles
> plan our livery and costumes
> /jp226-charity-rally-theme-planner
```

## Files

- `SKILL.md`: the instructions Claude follows
- `scripts/handle_check.py`: handle and domain format check
- `references/naming-guide.md`: choosing a name and handles
- `references/theme-brief-template.md`: the one-page brief

## Troubleshooting

**The check says a name is too long for a handle.** Use a shorter form on that platform. X allows only 15 characters.

**Two teams have the same idea.** That is common. Pick a different twist or a different name, and say what makes your team yours.

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
