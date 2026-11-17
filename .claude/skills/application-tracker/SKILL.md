---
name: application-tracker
description: Keeps the Notion Applications database up to date. Logs what the user sent and heard back, moves cards between statuses, sets one concrete next action with a date, and answers "what should I do next".
---

# Application tracker

Database: the Applications data source in `config/settings.md`. Schema and status rules: `notion/applications-schema.md`.

## Updating

When the user reports news ("I sent X", "Y rejected me", "interview with Z on Friday"):

1. Find the card (company + role). If it doesn't exist, create it.
2. Set Status:
   - Sent → **Applied** + Applied on = the date they give (default today).
   - Rejection → **Rejected**.
   - Interview scheduled or done → **Interview**.
   - Offer → **Offer**.
   - Decided not to apply / posting closed → **Discarded**.
3. Append a dated line **inside the card** (page body): `YYYY-MM-DD: what happened (who)`. Never overwrite older lines.
4. Set **one** Next action with a date:
   - Applied → "Follow up with <contact or recruiter>" in 10 days.
   - Interview → "Prepare: <topic>" the day before; "Send thank-you note" the same day after.
   - Rejected → "Ask for feedback / keep <contact> warm", or "None".
   - No news after a follow-up → wait 2 weeks more, then "No response".

Only the user can make a card Applied. Never infer it from a prepared CV.

## Answering "what's next"

Query active cards (To review, CV ready, Applied, Interview) sorted by Next action date. Reply with:

1. Overdue and today, then this week.
2. Max 5 items, each with the action and the card link.
3. If anything is stale (no change in 3+ weeks), say so in one line.

## Weekly hygiene (when asked, or after `job-search`)

- Applied > 6 weeks, no news → "No response".
- To review older than 2 weeks → ask the user to decide or discard.
- Never delete cards.
