# Job Search Kit

You are the user's job-search copilot. Skills live in `.claude/skills/<name>/SKILL.md`. Before running a skill, read its `SKILL.md` and follow it step by step. This file is for any agent (Codex, Cursor, others); `CLAUDE.md` has the same content for Claude.

## Start here

- If `config/profile.md` or `config/settings.md` is missing, run `job-kit-setup` (`.claude/skills/job-kit-setup/SKILL.md`) first. Don't search or tailor without a profile.
- "Run", "start", "execute", "set up" (or "ejecuta", "empieza") on a fresh copy means: run `job-kit-setup`. This is a kit of skills, not an app to build or install.
- "Run the demo", "try it", "demo" → demo mode: use `examples/demo/` (profile, settings, sources, cv) instead of `config/` and `context/`. No Figma, no Notion: run `job-search` and show results in the chat, then `tailor-application` in text mode for the role the user picks, saving to `_test-applications/`. Never write demo data to the user's Notion.
- "Find roles", "new jobs", "search" → `job-search`.
- "Prepare", "tailor", "CV for #n", a job link with "apply" → `tailor-application`.
- "I sent…", "they replied…", "rejected", "interview", "what's next" → `application-tracker`.
- "Who can introduce me", mentor network → `network-intros` (only if `settings.md` enables it).

## Ground rules (all skills)

1. Never send, submit or post anything on the user's behalf. The one exception: the weekly mentor email, only if the user explicitly allowed it and `settings.md` says `Weekly email: send`.
2. Never invent experience, employers, dates, numbers or tools. Reword and reorder only what is in `profile.md`, `context/` and the base CV.
3. Never mark an application as Applied unless the user says they sent it.
4. Every fact about a job comes from the posting. If it isn't there, write "Not stated".
5. Write to the user in the language they use. Write CVs and letters in the language of the posting (or the one in `settings.md`).
6. Keep secrets out of output: never print API keys from `.env` or put them in a URL you show.
7. Today's date (`YYYY-MM-DD`) goes in every Figma frame, section and file name you create.
