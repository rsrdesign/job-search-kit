# context/

Drop anything here that helps the kit understand you. Everything in this folder except this file is git-ignored.

Good things to add:

- Your current CV as PDF or plain text (the source of truth for experience and numbers).
- Your LinkedIn profile as PDF (profile → More → Save to PDF). It often lists clients, projects and numbers the CV leaves out.
- `evidence.md`: written by setup from all of the above; what the match score is based on. Edit it whenever you remember something.
- `portfolio.md` with your portfolio URL and 2 to 3 lines per case study.
- Case study write-ups, performance reviews, recommendations.
- `notes.md`: anything else (why you're leaving, what you're proud of, what you never want to do again).

The kit only uses facts found here, in `config/profile.md` or in your base CV (Figma, Word, Pages or Google Docs).

## Exporting LinkedIn connections as a CSV

LinkedIn has an official export; no scraping or extra tools needed. The same steps work for your own network or, with their consent, a mentor's.

1. On LinkedIn: **Me → Settings & Privacy → Data privacy → Get a copy of your data**.
2. Choose **"Want something in particular?"**, tick **Connections** only, and click **Request archive**.
3. LinkedIn emails a download link (Connections alone usually arrives within minutes; the full archive can take up to a day).
4. Download the zip, open it and take **Connections.csv**: first and last name, profile URL, company, position and the date you connected. Emails only appear for people who allow it.
5. Save it in `context/` (e.g. `context/my-network.csv` or `context/mentor-network.csv`). It's git-ignored, so it never leaves your computer.

Good to know: the Company column is often empty, so the kit also reads the Position text (e.g. "Product Designer at Docplanner").
