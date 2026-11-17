# Open Source Job Search Kit

An AI job-search copilot you run with Claude. It finds roles that fit you, tailors your CV and cover letter in Figma for each one, and keeps every application tracked in Notion. You review everything before it goes anywhere.

Built by a product designer for her own job search, then stripped of personal data and shared as a template.

## What it does

| Phase | What happens | What you do |
|---|---|---|
| 1. Find roles | Searches Google Jobs (SerpApi), Greenhouse company boards and any links you paste (LinkedIn included). Scores each role 0 to 100 against your profile and drops the ones that don't fit. | Pick the roles you want. |
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
- [ ] **Free SerpApi account** and its API key ([serpapi.com](https://serpapi.com)). Free plan: 100 searches a month, one search round uses about 5.
- [ ] **A folder for applications**, e.g. `~/Documents/Job search/`. One subfolder per company is created inside it.

Optional

- [ ] **Claude in Chrome**, to read job links that block bots (LinkedIn) and to download Figma PDFs if your setup can't reach figma.com directly.
- [ ] **A mentor's LinkedIn connections CSV**, shared with their consent, for the intros panel.
- [ ] **A scheduled task** so the search runs on the days you choose.

## Setup

1. Download or clone this repo into a folder on your computer.
2. Copy `.env.example` to `.env` and paste your SerpApi key.
3. Install the skills:
   - **Claude Code**: copy `skills/*` into `.claude/skills/` in this folder (or `~/.claude/skills/` to use them anywhere).
   - **Cursor**: copy `skills/*` into `.cursor/skills/`.
   - **Claude app**: upload each skill folder in Settings → Skills.
4. Put anything that describes you in `context/`: your current CV as text or PDF, portfolio link, case studies, notes. It is read during setup and when tailoring.
5. Ask Claude: **"Set up my job search kit"**. The `job-kit-setup` skill asks you a short form and writes `config/profile.md` and `config/settings.md`.
6. Ask: **"Find me new roles"**. From there, pick roles and say **"Prepare my application for #2"**.

## The setup form

The first run asks for:

- **About you**: name, current title, years of experience, languages, portfolio or website URL, LinkedIn.
- **Goals**: target roles and seniority, industries you want or want to avoid, what a great next role looks like, deal-breakers.
- **Expectations**: minimum salary and currency, employment type (full-time, contract, freelance), start date / notice period.
- **Location**: city, time zone, work mode (on-site, hybrid, remote), countries you can work in, relocation yes/no.
- **Proof**: 3 to 6 achievements with real numbers, top skills and tools.
- **Context**: any links or files in `context/` the kit should read.
- **Wiring**: Figma file URL, CV and cover letter frame links, Notion page URL, applications folder path, search days.

## Folder structure

```
open-source-job-search-kit/
├── README.md
├── CLAUDE.md                 # entry point for Claude Code / Cursor
├── .env.example              # SERPAPI_KEY=
├── config/
│   ├── profile.example.md    # filled by setup → profile.md (git-ignored)
│   ├── settings.example.md   # Figma, Notion, folders → settings.md (git-ignored)
│   └── sources.example.md    # search queries and Greenhouse boards
├── context/                  # your CV, portfolio, notes (git-ignored)
├── notion/
│   └── applications-schema.md
├── skills/
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
