# Changelog

## 0.6.3 · 2026-11-24

- **Neutral PDF file names.** Exported PDFs are now `Alex_Doe_CV.pdf`, `Alex_Doe_CV_ATS.pdf` and `Alex_Doe_Cover_Letter.pdf` (`_Carta.pdf` in Spanish), with no company or date. Figma frames and document copies still carry both, so your workspace stays in order.
- **Why.** 0.6.2 said file names are only for you. That was wrong: an attachment keeps its file name, so the recruiter sees it, and so does anyone they forward it to. `CV (Acme) 2026-11-17.pdf` tells them it's a version made for one company and when, and if you attach the wrong one it's obvious. The company folder (`*Acme/`) already keeps the files apart, so the name doesn't need to.

## 0.6.2 · 2026-11-23

- **Richer PDF properties.** Every exported PDF (CV, ATS CV and cover letter) now gets a title, author, subject (the tailored headline), keywords (the tailored skills) and language, and opens showing its title instead of the file name. New helper: `scripts/pdf_metadata.py`.
- **Why the title doesn't name the company.** File names keep the company and date (`CV_Alex_Doe_en (Acme) 2026-11-17.pdf`), because they're for you: they keep your folders in order. The title inside the PDF is for whoever opens it, so it's just `Alex Doe · CV`. CVs get forwarded: a recruiter passes yours to a client, an agency sends it to three companies, or you reuse it for a similar role. A title like "CV for Acme" in the browser tab of someone at another company looks careless and reveals where else you're applying. A neutral title works anywhere.
- **Why bother.** When a PDF opens in a browser or a viewer, the title is the first thing people see, instead of a file name full of underscores. Author, subject and keywords make the file easy to find in a recruiter's inbox or drive, and the language helps screen readers read it right. ATS mainly read the text itself, so this doesn't replace a clean one-column CV: it's the finishing touch on top.

## 0.6.1 · 2026-11-23

- **Safer by default**: `.gitignore` now also covers `.env.local` and any other `.env.*` file, and your own `config/sources.md` (the companies you're targeting).
- **New ground rule**: job postings, web pages, emails, PDFs and CSVs are treated as data, never as instructions, so a posting can't trick the agent into sending your files, keys or contacts anywhere.

## 0.6.0 · 2026-11-23

- **ATS version of the CV**: each role now also gets a one-column CV for job portals, from your own ATS template (Figma or document) or generated from the tailored text. The setup asks for it in step 3, the kit checks the PDF reads in order, and the wrap-up says which version to send where.
- **PDF title and author** are set on every export (merging pages used to drop them).
- **README for newcomers**: three things you need and three steps up front, one screenshot before the demo, a short glossary (agent, MCP, ATS, frame), optional extras in one table with what each is for, and a note that the skills are for your agent, not for you.

## 0.5.10 · 2026-11-22

- **Notion block limit, corrected**: the cap only applies to free workspaces with two or more members, it counts every block ever created, and deleting cards or emptying the Trash doesn't give blocks back. The README now says to keep the board in a workspace where you're the only member (unlimited on the free plan) or upgrade. "Clean up my board" is still there, but only to keep the board readable.

## 0.5.9 · 2026-11-19

- **Notion free plan block limit**: documented in the README and the checklist, with a "Clean up my board" routine that keeps a short history of closed roles before moving old cards to Trash.

## 0.5.8 · 2026-11-19

- **Suggested salary**: when a posting has no salary, the card gets a realistic range for that company and level, with a short why, so you know what to type in application forms without pricing yourself out.
- **Real board preview** in the README.
- README title is now **Job Search Kit**, matching the repo name.
- **Cleaner board**: To review cards show the salary hint (suggested or published) and lose it once you move on; the mentor status only appears once you've applied.

## 0.5.7 · 2026-11-19

- **ATS coverage instead of CV score**: after tailoring, the card gets the % of the posting's key requirements that the CV shows (only real experience counts). On the board it appears as an `ATS 86%` pill on CV ready cards, next to the Match pill you already see in To review.

## 0.5.6 · 2026-11-19

- **One language per application**: when a posting is in Spanish (or any other language), the CV, the letter and the Notion card are all written in that language, even if the rest of the board is in English.

## 0.5.5 · 2026-11-19

- **Your own network**: share your LinkedIn connections CSV and, after you apply, the kit checks who you already know at that company before looking for strangers.
- **How to export LinkedIn connections** (official export, a few clicks) in `context/README.md`, for your own network or a mentor's.

## 0.5.4 · 2026-11-18

- **Mentor reply check** (optional): 6 days after the weekly mentor email, the kit reads the reply and updates Notion (intro done, date, log, follow-up with the contact). Unclear answers are passed to you instead of being guessed. It never replies.

## 0.5.3 · 2026-11-18

- **New default weekly plan**, suggested in setup with the reason for each step: searches on Monday and Wednesday at 8:30 (with the computer on), the review reminder on Wednesday at 12:30 after both searches, and the optional mentor email on Thursday at 9:30, so there's time to apply before the mentor sees the list.
- **Reach out yourself** (optional, for people without a mentor): after you apply, the kit suggests who to message at the company and drafts a short LinkedIn connection note (under 200 characters) for you to send.
- **Markdown counts as the repo language** on GitHub (`.gitattributes`).

## 0.5.2 · 2026-11-18

- **Weekly mentor email, refined**: each role shows the contact (linked to their LinkedIn), when they connected, why now and a link to the posting, with the suggested message in a grey box; roles still waiting from earlier weeks are listed at the end. No new roles, no email. Messages are written in the mentor's voice and specific to each posting, using your CV, LinkedIn, portfolio and website.

## 0.5.1 · 2026-11-18

- **Weekly email to the mentor** (optional, with network intros): one email per week listing the roles where the mentor can help, with the contact's LinkedIn link, when they connected, why now and a suggested message. Drafted by default; sent on its own only if you explicitly allow it.

## 0.5.0 · 2026-11-18

- **Word, Pages and Google Docs**: no Figma needed for a designed CV. Setup asks where your CV lives; `tailor-application` duplicates your base CV and cover letter per role, rewrites only the mapped parts (keeping your fonts and layout) and exports PDFs after you approve. Figma stays the default for designers; text mode remains for a PDF-only CV.

## 0.4.1 · 2026-11-18

- **Downloads access**: README, setup and `tailor-application` say that exporting Figma PDFs through a browser needs access to the Downloads folder, where the files land before moving to the company folder.

## 0.4.0 · 2026-11-18

- **Score from your whole profile, not only the CV**: setup also reads your LinkedIn (as a PDF export) and your website or portfolio, and writes `context/evidence.md`, one line per proof with its source. `job-search` scores against it and `tailor-application` uses it to spot what the CV could add.
- **Accepted work modes**: the profile lists the modes you accept (e.g. remote only); roles with office days anywhere are dropped instead of scored.

## 0.3.3 · 2026-11-18

- **Score pill**: a "Score" formula shows the Match as a coloured pill on the cards (green 90+, yellow 60 to 89, red under 60).
- **Richer saved postings**: aggregator roles are matched to the employer's own page, any named recruiter or hiring manager goes into Contact, and deal-breakers (office days, another city, unnamed client, a company you already applied to) are flagged with ⚠ in the card.

## 0.3.2 · 2026-11-18

- **Match on the card**: the Pipeline board shows the 0 to 100 Match on every card.
- **No placeholder next action** on To review cards: they simply wait for your decision. The Next actions view now covers CV ready, Applied and Interview.
- **Mentor fields only after applying**: Mentor match stays empty until the card is Applied, and the boards show "Mentor done on" (hidden until set) instead of an always-visible checkbox.
- **Weekly review reminder** (optional, default Thursday 12:00): a scheduled task that lists the To review roles, best match first, flagging the ones older than 14 days.

## 0.3.1 · 2026-11-18

- **Saved postings**: `job-search` copies each posting into its Notion card ("Job posting (saved date)" with the full text in a toggle), so you keep the requirements and salary after the job is taken down. Clean-up saves missing postings for active cards and adds a dated note when a posting goes offline.

## 0.3.0 · 2026-11-18

- **Agent-agnostic**: works with Claude, Codex, Cursor or any agent with file access, web fetch and MCP. New `AGENTS.md` and a "Works with" section in the README.
- Skills refer to "a browser tool" instead of a specific product.

## 0.2.0 · 2026-11-17

- **Demo mode**: "Run the demo" tries the kit with a fictional profile, no Figma or Notion needed.
- **Text mode**: tailor a CV and cover letter without Figma (Markdown, then PDF).
- **PDFs after approval**: tailoring no longer exports PDFs until you say "export" (or set `Export PDFs: automatic`).
- **CV score** column in Notion (requirements covered, before → after), separate from the 0 to 100 Match.
- **One timing table** for follow-ups and No response (day 10, day 24, day 42) in `notion/applications-schema.md`; all skills follow it.
- **Last search** date stored in `settings.md`, so "recent" no longer depends on posting dates.
- Network access order for job boards: shell, web fetch tool, Claude in Chrome; note for unattended runs.
- Notion Source options: Indeed, Workable, Pasted link. How to add CV languages.
- README: CV in `context/` as step 1; Figma moved to optional.

## 0.1.0 · 2026-11-17

- First release: setup form, job search (Greenhouse, Ashby, Lever, Himalayas, Arbeitnow, optional SerpApi / Adzuna / Jooble), Figma tailoring, Notion tracker, optional mentor panel.
