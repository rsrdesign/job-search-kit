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
4. Set **one** Next action with a date, following the timing table in section 3 of `notion/applications-schema.md` (day 10 follow-up, day 24 last follow-up, day 42 No response).

Only the user can make a card Applied. Never infer it from a prepared CV.

If the Mentor panel is enabled in `settings.md` and a card becomes Applied or Interview, run `network-intros` for that company. When the user says the mentor did something, follow "When the mentor acts" in that skill.

## Answering "what's next"

Query active cards (To review, CV ready, Applied, Interview) sorted by Next action date. Reply with:

1. Overdue and today, then this week.
2. Max 5 items, each with the action and the card link.
3. If anything is stale (no change in 3+ weeks), say so in one line.

## Weekly hygiene (when asked, or after `job-search`)

Apply the timing table in section 3 of `notion/applications-schema.md` to every active card. Never delete cards.
