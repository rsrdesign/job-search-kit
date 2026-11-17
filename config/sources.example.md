# Sources

> Copy to `sources.md` and edit. Safe to commit (no personal data).
> Company boards and remote boards need no key. City search engines are optional and need a key in `.env`.

## 1. Company job boards (no key)

Add the companies you'd like to work for. The token is the part of their careers URL after the domain:

- Greenhouse: `boards.greenhouse.io/<token>` or `job-boards.eu.greenhouse.io/<token>`
- Ashby: `jobs.ashbyhq.com/<token>`
- Lever: `jobs.lever.co/<token>` (EU: `jobs.eu.lever.co/<token>`)

| Company | Platform | Token | Region |
|---|---|---|---|
| Example Co | greenhouse | exampleco | us |
| Another Co | greenhouse | anotherco | eu |
| Startup Inc | ashby | startupinc | |
| Product Ltd | lever | productltd | eu |

Tip: open a company's careers page and look at the URL of any job; it tells you the platform and token.

## 2. Remote job boards (no key)

Keywords to filter titles (one per line):

- Product Designer
- UX Designer
- Design Systems

Boards: Himalayas, Arbeitnow. Turn one off by deleting its line:

- himalayas
- arbeitnow

## 3. City search engines (optional, need a key)

Queries (keep to about 5 per run to stay inside free plans):

- Product Designer {{CITY}}
- Senior Product Designer remote {{COUNTRY}}
- UX UI Designer {{CITY}}

## 4. Links you paste

LinkedIn, Indeed, Workable, Jooble, career pages: paste the link (or the text if the page blocks bots). The kit does not scrape LinkedIn.
