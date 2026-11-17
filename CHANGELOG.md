# Changelog

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
