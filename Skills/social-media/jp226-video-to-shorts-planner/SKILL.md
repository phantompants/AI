---
name: "jp226-video-to-shorts-planner"
description: Turns one long video into a week of seven distinct vertical Shorts, step by step. Builds a timestamped video map, picks the strongest clips, writes hooks, a cut map, captions, a 9:16 framing plan, visual and audio notes, a rough-cut review, publishing copy and a Monday to Sunday plan. Use when the user has a long video or transcript and wants Shorts, Reels or TikToks from it, says "cut this into Shorts", "plan a week of clips from this video", "find the best clips", "repurpose this video", or "turn this into short-form content". Triggers on "/jp226-video-to-shorts-planner". Works from a transcript or a video Claude can access; it never invents dialogue or describes footage it has not checked.
compatibility: Claude 3.5+ (Desktop, claude.ai, Claude Code). Best with a timestamped transcript or an uploaded video. No special tools needed. Editing is done by the user in their own editor.
metadata:
  version: "v1.00"
  author: "JP226Prints"
  created: "2026-10-26"
  updated: "2026-10-26"
  governance: "Personal (JP226Prints) + GitHub"
  status: "Active"
  category: "social-media"
  tags: "shorts, reels, tiktok, video-editing, repurposing, content-plan, captions, hooks"
---

# JP226 Video to Shorts Planner

Created by JP226Prints.

Free to use. A good cause, if you choose: please consider supporting Variety - the Children's Charity through our team page: https://www.variety4wdqld.com.au/t/thefastandthefossilized

This note is about this skill only. Do not add it to anything the skill produces for other people.

Takes one long video and plans seven different Shorts from it, plus a Monday to Sunday publishing plan. It does the thinking and paperwork. The user does the cutting in their own editor.

The skill is a 12-step workflow. Each step builds on the one before and keeps a permanent clip ID, so nothing gets lost between steps. Full instructions for each step are in `references/steps.md`. Read that file before running any step.

## Ground rules

These apply to every step. They matter more than any single output.

1. **Never invent dialogue.** Every quoted line must come from the transcript or the video, with its source timestamp. If a line is not there, it is not quoted.
2. **Never describe visuals that have not been checked.** If Claude is working from a transcript only, say so, and write visual notes as suggestions to confirm, not as facts.
3. **Say what could not be done.** If part of the video is unreadable, unavailable or unclear, list it. Do not smooth over a gap.
4. **Timing is provisional until the user checks it in their editor.** Do not claim frame accuracy. Mark uncertain cut points for manual checking.
5. **Separate what exists from what is new.** Anything the user would have to record again, source or create is labelled `NEW RECORDING` or `TO CREATE`, and kept apart from the original footage.
6. **No fake urgency, no unsupported results, no "viral" promises.** Hooks and copy must match what the clip actually delivers.
7. **Plain English, Australian spelling, no em dashes.**

## Step 0: Collect the brief

Ask for these in one short message. Use sensible defaults where the user does not know, and say which defaults were used.

| Item | Example | Default |
|---|---|---|
| The video | Upload, or a transcript with timestamps | None. Required |
| Audience | "Beginners who want to start a podcast" | Ask |
| The specific problem they struggle with | "Their recordings sound echoey" | Ask |
| Niche | "Home recording tips" | Ask |
| Goal | Saves, follows or leads | Saves |
| Platform | YouTube Shorts, Reels, TikTok | YouTube Shorts |
| Clip length | 30 to 45 seconds | 30 to 45 seconds |
| Output size | 1080 x 1920 | 1080 x 1920 |
| Editor | CapCut, Premiere, DaVinci | CapCut |
| Music preference | None or subtle instrumental | Subtle instrumental |
| Brand code for filenames | Short code, for example `JP` | Ask |
| Analytics for posting times | Pasted figures, or "none" | None |

Check what Claude can actually access: the video itself, a transcript, or neither. State this plainly at the start, because it decides how much can be confirmed in steps 7 to 10.

## The 12 steps

Run them in order. After each step, give the output, then ask whether to continue, adjust, or jump to a later step. The user can start part way through if they already have the earlier results.

| # | Step | What it produces |
|---|---|---|
| 1 | Build a searchable video map | Table of timestamps, topics, takeaways, demonstrations, strong quotes |
| 2 | Find the strongest clip candidates | Up to 12 candidates, each with a permanent ID, ranked |
| 3 | Choose seven distinct Shorts | A week of seven, each with a different main takeaway |
| 4 | Create hooks the footage can support | Three on-screen hooks and the best existing spoken opening |
| 5 | Map every cut | One row per retained segment, with source and new-Short timings |
| 6 | Turn the cut map into captions | SRT subtitle text for the retained speech |
| 7 | Plan the vertical crop | A 9:16 framing plan for each segment |
| 8 | Add visuals that explain the point | Up to four timed overlays per clip |
| 9 | Map the audio edits | Audio issues, fixes, music and sound effect notes |
| 10 | Review the actual rough cut | Confirmed and uncertain fixes, with priority |
| 11 | Write the publishing copy | Three titles, three cover-text options, one caption |
| 12 | Package the full week | A Monday to Sunday plan with filenames and open fixes |

Steps 1 to 3 happen once for the whole video. Steps 4 to 11 repeat for each of the seven Shorts, one clip at a time. Do not batch all seven into one reply unless the user asks. Step 12 runs once at the end.

## Keeping track

Keep a running **clip register** in the conversation. One row per Short, with its ID, working title, source timestamps, status and any unresolved fixes. Show it again whenever the user asks "where are we", and before step 12. Step 12 depends on the latest version of everything, so when a cut map or caption file changes, update the register and say which downstream outputs are now out of date.

## Rules for step 10 (rough cut review)

Step 10 needs the user to upload their rough cut. If it is not uploaded:

1. Say so, and do not review from memory or from the plan.
2. Offer a checklist the user can run themselves in the editor instead.
3. List exactly which checks could not be completed.

When it is uploaded, compare it with the source and the latest cut map. Confirmed problems and uncertain ones go in separate lists.

## Publishing copy limits

Titles, cover text and captions follow the platform's own limits and the lengths the user gave in the brief. Always write the keyword naturally into the title and caption. End with one relevant action only (save, comment or follow), never several.

## What this skill will not do

- Make up quotes, timestamps or footage.
- Promise views, virality or income.
- Suggest posting times without analytics from the user. With none, say "no data supplied" and leave the time slot blank.
- Edit the video file. It produces plans, text and checklists.

## Reference

`references/steps.md` holds the detailed instructions for all 12 steps, including inputs, required output columns and checks.
