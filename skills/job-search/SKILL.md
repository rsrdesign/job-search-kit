---
name: job-search
description: Finds and filters roles for the user from Google Jobs (SerpApi), Greenhouse boards and links they paste, scores the match 0 to 100 against config/profile.md, adds the good ones to Notion as To review and cleans up stale applications.
---

# Job search

Requires `config/profile.md`, `config/settings.md` and `config/sources.md`. If missing, run `job-kit-setup`.

Every fact about a job comes from what the source returned. If the posting doesn't say it, write "Not stated". Never invent salary, work mode, seniority or company facts.

## 1. Collect

"Recent" = posted since the last search (check the newest "Posted" date in Notion). On demand with no history: last 7 days.

1. **Google Jobs via SerpApi**, one request per query in `sources.md`:
   `https://serpapi.com/search.json?engine=google_jobs&q=<query>&location=<location>&hl=<hl>&gl=<gl>&api_key=$SERPAPI_KEY`
   - Read the key from `.env`. Never print it or show a URL that contains it.
   - Prefer a shell request (curl / Python). If the shell can't reach serpapi.com, use Claude in Chrome: open `https://serpapi.com/robots.txt` and call `fetch('/search.json?...')` from the page.
   - If there's no key, skip this source and say so in one line.
2. **Greenhouse**, per board token in `sources.md`:
   - US: `https://boards-api.greenhouse.io/v1/boards/<token>/jobs`
   - EU: `https://boards-api.eu.greenhouse.io/v1/boards/<token>/jobs`
   - Keep titles that match the target roles. Fetch details with `.../jobs/<id>?content=true`. If a token fails, note it and continue.
3. **Pasted links** (LinkedIn, Indeed, Workable, career pages): read the page; if it blocks bots, open it with Claude in Chrome or ask the user to paste the text. Do not scrape LinkedIn search results.

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
3. Create each Apply / Consider role in Notion with Status "To review", Next action "Decide whether to apply", Next action date today + 2 days.
4. End by asking which ones to prepare. Do not tailor or send anything until the user picks.

## 5. Clean-up (every run)

- Applied more than 6 weeks ago with no news → "No response", Next action "None. Reopen if they reply".
- To review / CV ready whose posting no longer exists → "Discarded".
- Never delete cards. Mention the changes in one line.
