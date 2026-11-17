---
name: job-kit-setup
description: First-run setup for the job search kit. Runs a short step-by-step form (4 steps, few questions), reads the user's CV and context to fill the rest, wires Figma, Notion and folders, and writes config/profile.md, config/settings.md and config/sources.md.
---

# Job kit setup

Run when `config/profile.md` or `config/settings.md` is missing, or when the user says "run", "start", "set up", "ejecuta", "empieza" or similar. Talk to the user in their language.

## How to ask

- **One step at a time**, like a form. Say which step it is: "Step 2 of 4 · What you're looking for".
- **Max 4 questions per step.** If you have a multiple-choice question tool (e.g. AskUserQuestion), use it with ready-made options plus "Other"; otherwise ask in one short message with numbered questions.
- **Ask only what you can't infer.** Read the CV and context first, pre-fill, and ask the user to confirm instead of asking from scratch.
- Every step can be skipped with "skip" except the ones marked *required*.
- Never ask for API keys in the chat. Tell the user to put them in `.env`.

## Step 0 · Check (no questions)

Silently check and then show one line per item (✅ / ⚠️ + fix):

- You can read and write this folder.
- Figma MCP connected.
- Notion connector connected.
- Optional search keys in `.env` (just say which exist; never print them).

If Figma or Notion are missing, explain the fix in one line and continue; the form still works and you wire them at the end.

## Step 1 of 4 · About you

1. *Required.* "Share your CV": a file in `context/`, a PDF path, a link, or paste the text.
2. Portfolio or website URL (the only link used in cover letters).

Then read the CV and everything in `context/` and pre-fill: name, current title, years of experience, languages, achievements with numbers, skills, tools.

## Step 2 of 4 · What you're looking for

Offer options built from the CV:

1. *Required.* Target roles (multi-select, e.g. "Senior Product Designer", "Design Systems Lead", "UX/UI Designer", Other).
2. *Required.* Where: city + work mode (On-site / Hybrid / Remote in my country / Remote anywhere in the EU / Other).
3. Minimum salary per year (ranges as options, or "Skip").
4. Type: Full-time / Contract / Freelance / Any.

## Step 3 of 4 · Your files

1. *Required.* Where is your CV designed? **Figma** (then: link to your CV frame and your cover letter frame; right-click the frame → Copy link; one language is enough) or **No Figma** (Word, Google Docs, PDF: the kit works in text mode with the CV in `context/`).
2. *Required.* Notion: link to the page where the tracker should live (an empty page is best).
3. Applications folder: suggest `~/Documents/Job search/` and let them confirm or change.

## Step 4 of 4 · Where to look

1. Companies you'd love to work for (free text, or "Skip"). For each one, find its careers page, detect Greenhouse / Ashby / Lever and the token, and check the API returns jobs. Suggest 5 more in the same space and ask which to keep.
2. Search days: Tue + Thu / Mon + Wed + Fri / Only when I ask.
3. Do you have a mentor or ally who'd share their LinkedIn connections to help with intros? No / Yes (then ask for their first name and the CSV path in `context/`). Yes adds the Mentor panel.

## Confirm

Show a one-screen summary: roles, location, salary, sources, Figma frames, Notion page, folder, and the pre-filled facts from the CV (achievements, skills). Ask: "Anything to fix?" Fix it, then continue.

## Build (no questions)

1. **Layer map** (Figma only). List the visible text layers of both Figma frames, map them to headline, summary, bullets per job, skills, recipient, body paragraphs and date, and pick the link colour (an accent fill already used in the letter). Only ask if a layer is ambiguous.
2. **Notion.** Build the Jobs tracking page exactly as `notion/applications-schema.md` says, in order: page title, icon and intro text, divider, inline Applications database (DDL as written, with the colours), its views (Pipeline, Next actions, the mentor tab if enabled, All), and the Mentor panel only if intros are enabled. Fetch the page at the end and check it matches. Save the data source URLs.
3. **Files.** Write `config/profile.md`, `config/settings.md` and `config/sources.md` from the `.example.md` templates. Create the applications folder.
4. **Schedule.** If they chose search days, offer a scheduled task; create it only if they say yes.

## Finish

One short message: what was set up, a reminder to drag the **Pipeline** tab to the first place in Notion, and the next thing to say: **"Find me new roles"**.

Things the form doesn't ask (industries to avoid, deal-breakers, relocation, notice period) can be added any time by saying "update my profile".
