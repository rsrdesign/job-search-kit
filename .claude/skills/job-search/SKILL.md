---
name: job-search
description: Finds and filters roles for the user from company job boards (Greenhouse, Ashby, Lever), remote boards (Himalayas, Arbeitnow), optional city search (SerpApi, Adzuna, Jooble) and links they paste, scores the match 0 to 100 against config/profile.md, adds the good ones to Notion as To review and cleans up stale applications.
---

# Job search

Requires `config/profile.md`, `config/settings.md` and `config/sources.md`. If missing, run `job-kit-setup`.

Every fact about a job comes from what the source returned. If the posting doesn't say it, write "Not stated". Never invent salary, work mode, seniority or company facts.

## 1. Collect

"Recent" = posted since **Last search** in `config/settings.md`. If it is empty, use the last 7 days. At the end of every run, write today's date and time there.

Run every source that is configured in `sources.md` / `.env`. If one fails, note it in one line and carry on.

**How to reach the APIs**, in this order:
1. Shell (`curl` / Python). Works on your own computer.
2. Your web fetch tool (e.g. WebFetch). Works in cloud sessions where the shell has no internet.
3. Claude in Chrome: open a page on that host (e.g. `/robots.txt`) and call `fetch` with a relative path in the page.

Scheduled or unattended runs can't answer permission prompts: pre-approve the job board domains for your fetch tool, or make sure Chrome is connected, otherwise the run stops at the first prompt. Say so in the result if a source was skipped for this reason.

1. **Company job boards** (no key), for each company in `sources.md`:
   - Greenhouse US: `https://boards-api.greenhouse.io/v1/boards/<token>/jobs` · EU: `https://boards-api.eu.greenhouse.io/v1/boards/<token>/jobs`. Details: `.../jobs/<id>?content=true`.
   - Ashby: `https://api.ashbyhq.com/posting-api/job-board/<token>` (returns `jobs[]` with `title`, `location`, `isRemote`, `workplaceType`, `publishedAt`, `jobUrl`, `descriptionPlain`). Skip jobs where `isListed` is false.
   - Lever: `https://api.lever.co/v0/postings/<token>?mode=json` (EU: `api.eu.lever.co`). Fields: `text` (title), `categories.location`, `workplaceType`, `createdAt` (ms), `hostedUrl`, `descriptionPlain`.
   - Keep titles that match the target roles and keywords.
2. **Remote job boards** (no key), filtered by the keywords in `sources.md`:
   - Himalayas: `https://himalayas.app/jobs/api` (paginate with `nextCursor`). Use `title`, `companyName`, `locationRestrictions`, `minSalary`/`maxSalary`/`currency`, `pubDate`, `applicationLink`.
   - Arbeitnow: `https://www.arbeitnow.com/api/job-board-api` (Europe). Use `title`, `company_name`, `location`, `remote`, `created_at`, `url`.
   - Drop roles whose location restrictions exclude the user's country.
3. **City search engines** (optional, only if the key exists in `.env`; never print keys):
   - SerpApi (Google Jobs): `https://serpapi.com/search.json?engine=google_jobs&q=<query>&location=<location>&hl=<hl>&gl=<gl>&api_key=$SERPAPI_KEY`
   - Adzuna: `https://api.adzuna.com/v1/api/jobs/<country>/search/1?app_id=$ADZUNA_APP_ID&app_key=$ADZUNA_APP_KEY&what=<query>&where=<city>`
   - Jooble: `POST https://jooble.org/api/$JOOBLE_KEY` with `{"keywords": "<query>", "location": "<city>"}`
4. **Pasted links** (LinkedIn, Indeed, Workable, career pages): read the page; if it blocks bots, open it with Claude in Chrome or ask the user to paste the text. Do not scrape LinkedIn search results.

## 2. Deduplicate

- Same role in two sources counts once (the employer's own page wins).
- Skip roles already in Notion (same link, or same company + role).
- If the company already has a folder in the applications folder, flag it "already in touch".

## 3. Filter and score (0 to 100)

Drop outright: excluded roles, wrong seniority, locations or work modes the user can't do, deal-breakers.

| Criterion | Weight |
|---|---|
| Role and specialism match target roles | 30 |
| Skills asked ⊂ skills the user can prove (`profile.md`, `context/`) | 25 |
| Location and work mode compatible | 20 |
| Seniority | 10 |
| Salary (≥ floor or not stated = 15; a bit under = 8; far under = 0) | 15 |

If you only saw title, location and salary (aggregators), label it "preliminary match".

Verdict: **≥ 75 Apply · 55 to 74 Consider · < 55 Skip**, with one line of why, quoting the posting.

## 4. Output

1. Table of Apply and Consider roles, best first: #, match, role, company, location, mode, salary as published, type, source, link.
2. One line with how many were skipped and why, grouped ("6 US-only, 3 junior").
3. Create each Apply / Consider role in Notion: Application `Company · Role`, Company, Role, Status "To review", Match (0 to 100), Type, Work mode (or "Not stated"), Location, Salary, Source, Job link, Posted, Next action "Decide whether to apply", Next action date today + 2 days (and Mentor match "Not checked" if the Mentor panel is enabled). Put the one-line verdict inside the card.
4. End by asking which ones to prepare. Do not tailor or send anything until the user picks.

## 5. Clean-up (every run)

- Apply the timing table in section 3 of `notion/applications-schema.md` to every active card.
- To review / CV ready whose posting no longer exists → "Discarded".
- Never delete cards. Mention the changes in one line.
- Update **Last search** in `settings.md`.
