# Changelog

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
