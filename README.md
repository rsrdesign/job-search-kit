# Open Source Job Search Kit

An AI job-search copilot you run with Claude. It finds roles that fit you, tailors your CV and cover letter in Figma for each one, and keeps every application tracked in Notion. You review everything before it goes anywhere.

Built by a product designer for her own job search, then stripped of personal data and shared as a template.

## Quick start

1. Check the [checklist](#before-you-start-checklist) (Figma + Notion connected is enough to start).
2. Open Claude Code, Cursor or the Claude desktop app and paste:

   ```
   Clone https://github.com/rsrdesign/open-source-job-search-kit into a folder on my computer, open it, and run the job-kit-setup skill to set up my job search.
   ```

   If you already downloaded the folder, open it and just say **"Set up my job search kit"**.
3. Answer the 4-step form (about 5 minutes). Have your CV and the links to your Figma CV / cover letter frames and a Notion page ready.
4. Then say **"Find me new roles"**.

## What it does

| Phase | What happens | What you do |
|---|---|---|
| 1. Find roles | Searches company job boards (Greenhouse, Ashby, Lever), remote job boards (Himalayas, Arbeitnow) and any links you paste (LinkedIn included). Optional: city search with Google Jobs (SerpApi), Adzuna or Jooble. Scores each role 0 to 100 against your profile and drops the ones that don't fit. | Pick the roles you want. |
| 2. Tailor | Duplicates your CV and cover letter in Figma, rewrites the headline, summary, bullets, skills and letter for that role, groups them in a dated section and exports both PDFs to the company folder. | Review, tweak, send. |
| 3. Track | Creates a card per role in Notion with status, next action and date. Moves cards when you report news. Marks silent applications as "No response" after 6 weeks. | Tell it what you sent and what you heard back. |
| Optional | Cross-checks companies against a mentor's LinkedIn network (with their permission) and suggests intros. | Ask your mentor. |

### Ground rules baked into every skill

- **Nothing is sent automatically.** No applications, emails or messages leave without you.
- **No invented experience.** The CV is reworded and reordered, never padded.
- **You own your data.** Your profile, CVs and keys stay on your computer. `.gitignore` keeps them out of git.

## Before you start (checklist)

Required

- [ ] **Claude with access to your computer**: the Claude desktop app, Claude Code or Cursor. It needs to create folders and save files.
- [ ] **Figma account** and the **Figma MCP** connected to Claude.
- [ ] **A Figma file with your CV and cover letter**, one frame each (A4). One language or both. Name your text layers (e.g. "Headline", "Summary", "Bullets · Company") so the kit can find them.
- [ ] **Notion account** and the **Notion connector** in Claude.
- [ ] **A list of companies you'd like to work for.** The kit checks their job boards directly (Greenhouse, Ashby, Lever). No API key needed.
- [ ] **A folder for applications**, e.g. `~/Documents/Job search/`. One subfolder per company is created inside it.

Optional

- [ ] **A free key for a city-wide search engine**, to find roles at companies you don't know yet: [SerpApi](https://serpapi.com) (Google Jobs, 100 searches/month), [Adzuna](https://developer.adzuna.com) or [Jooble](https://jooble.org/api/about).
- [ ] **Claude in Chrome**, to read job links that block bots (LinkedIn) and to download Figma PDFs if your setup can't reach figma.com directly.
- [ ] **A mentor's LinkedIn connections CSV**, shared with their consent, for the intros panel.
- [ ] **A scheduled task** so the search runs on the days you choose.

## Setup

1. Download or clone this repo into a folder on your computer.
2. Optional: copy `.env.example` to `.env` and paste any search keys you have. The kit works without them.
3. Skills:
   - **Claude Code / Claude desktop app with this folder open**: nothing to do. The skills live in `.claude/skills/` and load automatically.
   - **Cursor**: copy `.claude/skills/*` into `.cursor/skills/`.
   - **Claude app without a local folder**: upload each skill folder in Settings → Skills.
4. Put anything that describes you in `context/`: your current CV as text or PDF, portfolio link, case studies, notes. It is read during setup and when tailoring.
5. Ask Claude: **"Set up my job search kit"**. The `job-kit-setup` skill runs a 4-step form and writes `config/profile.md`, `config/settings.md` and `config/sources.md`.
6. Ask: **"Find me new roles"**. From there, pick roles and say **"Prepare my application for #2"**.

## The setup form

Four short steps. It reads your CV first, so it only asks what it can't work out.

| Step | Asks |
|---|---|
| 1 · About you | Your CV (file, link or pasted text) and portfolio URL |
| 2 · What you're looking for | Target roles, city and work mode, minimum salary, employment type |
| 3 · Your files | Figma CV and cover letter frame links, Notion page, applications folder |
| 4 · Where to look | Companies you'd love to work for, search days |

Then it shows a summary to confirm and builds everything: Figma layer map, Notion tracker, config files. Anything else (deal-breakers, relocation, notice period, mentor network) can be added later with "update my profile".

## Folder structure

```
open-source-job-search-kit/
├── README.md
├── CLAUDE.md                 # entry point for Claude Code / Cursor
├── .env.example              # optional search keys
├── config/
│   ├── profile.example.md    # filled by setup → profile.md (git-ignored)
│   ├── settings.example.md   # Figma, Notion, folders → settings.md (git-ignored)
│   └── sources.example.md    # search queries and Greenhouse boards
├── context/                  # your CV, portfolio, notes (git-ignored)
├── notion/
│   └── applications-schema.md
├── .claude/skills/           # loaded automatically by Claude Code
│   ├── job-kit-setup/
│   ├── job-search/
│   ├── tailor-application/
│   ├── application-tracker/
│   └── network-intros/       # optional
└── examples/
    └── network.example.csv
```

Your applications folder (outside the repo) ends up like:

```
Job search/
├── *Acme/                      # * = active process
│   ├── CV_Alex_Doe_en (Acme) 2026-11-17.pdf
│   ├── CoverLetter_Alex_Doe_en (Acme) 2026-11-17.pdf
│   └── CoverLetter_Alex_Doe_en (Acme) 2026-11-17.txt   # paste-ready text
└── Globex/                     # closed process
```

## Notion

The tracker is one database, **Applications**, with these views:

- **Next actions**: active applications sorted by next action date.
- **Pipeline**: board by status (To review → CV ready → Applied → Interview → Offer / Rejected / No response / Discarded).
- **All**.
- **Network** (optional): board of roles where a mentor could make an intro.

The setup skill creates it for you. Schema in [`notion/applications-schema.md`](notion/applications-schema.md).

## Privacy and fair use

- Don't commit `config/profile.md`, `config/settings.md`, `.env`, `context/` or any network CSV. They are git-ignored.
- A mentor's contacts are their personal data. Only use them with consent and never publish them.
- Respect job boards' terms. For LinkedIn, paste the link or the text; the kit does not scrape it.

## License

MIT. See [LICENSE](LICENSE).
