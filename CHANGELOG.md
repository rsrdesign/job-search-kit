# Changelog

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
