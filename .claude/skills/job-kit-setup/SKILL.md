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
2. Your LinkedIn profile as PDF (recommended): on LinkedIn, open your profile → **More** → **Save to PDF**, and drop it in `context/`. Agents can't read linkedin.com pages, so the URL alone isn't enough.
3. Portfolio or website URL (the only link used in cover letters). If your portfolio is a PDF, drop it in `context/` too.

Then read the CV, the LinkedIn PDF, the website (if the fetch tool can reach it) and everything in `context/`, and pre-fill: name, current title, years of experience, languages, achievements with numbers, skills, tools. People rarely put everything in their CV, so these extra sources usually add clients, projects and numbers the CV leaves out.

Write `context/evidence.md`: one line per capability or proof, with its source in brackets (`[CV]`, `[LinkedIn]`, `[Portfolio]`, `[Website]`), grouped by area, plus a short "No evidence" list (things to never claim) and any dates that don't match between sources. `job-search` scores against this file and `tailor-application` uses it to spot gaps the CV can cover.

## Step 2 of 4 · What you're looking for

Offer options built from the CV:

1. *Required.* Target roles (multi-select, e.g. "Senior Product Designer", "Design Systems Lead", "UX/UI Designer", Other).
2. *Required.* Where: city + the work modes you accept (Remote only / Remote or hybrid in my city / Any / Other). Anything outside them is dropped, never scored.
3. Minimum salary per year (ranges as options, or "Skip").
4. Type: Full-time / Contract / Freelance / Any.

## Step 3 of 4 · Your files

1. *Required.* Where is your CV designed?
   - **Figma** (the default for designers): link to your CV frame and your cover letter frame (right-click the frame → Copy link; one language is enough).
   - **Word, Pages or Google Docs**: the path or link to your base CV and, if you have one, your base cover letter. The kit duplicates them for each role and keeps your layout. No base letter? It makes one from the CV's styles (same fonts and colours).
   - **Only a PDF / nothing designed**: text mode, with the CV in `context/`.
2. ATS version (recommended): "Designed CVs with columns are hard for applicant tracking systems (ATS) to read. Do you have a one-column version for job portals?"
   - **Yes, in Figma or a document**: its link or path (Figma: one frame, or one per page). The kit tailors it with the same text as the designed CV.
   - **No** (default): the kit makes a plain one-column PDF from the tailored text for each role.
   - **Not needed**: off.
3. *Required.* Notion: link to the page where the tracker should live (an empty page is best).
4. Applications folder: suggest `~/Documents/Job search/` and let them confirm or change. If PDFs will be exported from Figma through a browser, also ask for access to the **Downloads** folder (the files land there first).

## Step 4 of 4 · Where to look

1. Companies you'd love to work for (free text, or "Skip"). For each one, find its careers page, detect Greenhouse / Ashby / Lever and the token, and check the API returns jobs. Suggest 5 more in the same space and ask which to keep.
2. Search days: Mon + Wed at 8:30 (recommended) / Other days / Only when I ask. Scheduled searches run with the computer on (the kit lives in a folder on it).
   When suggesting it, show the weekly plan and why, in one short block:
   - **Monday 8:30, search**: catches everything posted over the weekend and late last week, so the week starts with a full list.
   - **Wednesday 8:30, search**: catches the mid-week postings while they're fresh (early applicants are seen first).
   - **Wednesday 12:30, review reminder**: one list after both searches, best match first, so you decide once and still have Wednesday and Thursday to apply.
   - **Thursday 9:30, mentor email** (only with a mentor): it includes everything you applied to that week, and the mentor has Thursday and Friday to act before the weekend.
3. Do you have a mentor or ally who'd share their LinkedIn connections to help with intros? No / Yes (then ask for their first name and the CSV path in `context/`). Yes adds the Mentor panel. No: offer the do-it-yourself option instead: "After you apply, should I suggest who to message at the company, with a short LinkedIn note you can send yourself?" No (default) / Yes (`Reach out myself: on` in `settings.md`). On Yes, offer to use their own LinkedIn connections CSV too (steps in `context/README.md`), so the kit checks who they already know first.
4. *Only if they said Yes to 3 and shared the network file.* Ask first: "Would you like a weekly email to <mentor> with the roles where they can help?" No (default) / Yes. Only on Yes ask for the mentor's email, the day and time (default Thursday 9:30, after the Monday and Wednesday searches), and: "Should I leave it as a draft for you to send, or send it on its own?" (draft is the default; send only if they choose it). Then offer to check the mentor's reply 6 days later and update Notion (see `network-intros`). Never set any of it up without asking.

## Confirm

Show a one-screen summary: roles, location and accepted work modes, salary, sources, Figma frames or base documents, Notion page, folder, and the pre-filled facts (achievements, skills), saying which ones came from LinkedIn or the portfolio and not from the CV. Ask: "Anything to fix?" Fix it, then continue.

## Build (no questions)

1. **Layer map** (Figma) or **text map** (Word, Pages, Google Docs). List the visible text layers of both Figma frames (and the ATS frame, if there is one), or the paragraphs of the documents, map them to headline, summary, bullets per job, skills, recipient, body paragraphs and date, and pick the link colour (an accent already used in the letter). Only ask if a part is ambiguous. For documents, also check what can export PDFs here (LibreOffice, Google Drive, Pages on a Mac) and note it in `settings.md`.
2. **Notion.** Build the Jobs tracking page exactly as `notion/applications-schema.md` says, in order: page title, icon and intro text, divider, inline Applications database (DDL as written, with the colours), its views (Pipeline, Next actions, the mentor tab if enabled, All), and the Mentor panel only if intros are enabled. Fetch the page at the end and check it matches. Save the data source URLs.
3. **Files.** Write `config/profile.md`, `config/settings.md` and `config/sources.md` from the `.example.md` templates. Create the applications folder.
4. **Schedule.** If they chose search days, offer a scheduled task; create it only if they say yes. Also offer the weekly review reminder (default Wednesday 12:30, section 5 of `notion/applications-schema.md`), only if they say yes.

## Finish

One short message: what was set up, a reminder to drag the **Pipeline** tab to the first place in Notion, and the next thing to say: **"Find me new roles"**.

Things the form doesn't ask (industries to avoid, deal-breakers, relocation, notice period) can be added any time by saying "update my profile".
