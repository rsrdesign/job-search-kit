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
4. Write log lines, Next action and Contact notes in the language of the posting (Spanish posting → Spanish), even if other cards are in English.
5. Set **one** Next action with a date, following the timing table in section 3 of `notion/applications-schema.md` (day 10 follow-up, day 24 last follow-up, day 42 No response).

Only the user can make a card Applied. Never infer it from a prepared CV.

If the Mentor panel is enabled in `settings.md` and a card becomes Applied or Interview, run `network-intros` for that company. When the user says the mentor did something, follow "When the mentor acts" in that skill.

## Reach out yourself (optional, no mentor)

Only if `settings.md` has `Reach out myself: on` (offered in setup to users without a mentor). When a card becomes **Applied**:

1. **Your own network first**: if `settings.md` has a `My network CSV`, look for people at that company (Company column, and the Position text, since Company is often empty). Someone you already know beats a stranger: a peer designer, the design lead or a recruiter. Write them in Contact as "In your network: <Name>, <Position> (connected <date>)" with their profile URL, and skip to step 3 with a warmer note (you can mention how you know them).
   Then, or if nobody is there, find the person closest to the hire: first anyone the saved posting names (hiring manager, recruiter); otherwise the design lead or, at a small company, a founder, from the company's own site, news or public profiles. Only names that appear in a source; say which. Never guess emails.
2. Write it in the card's **Contact** field (name, position, LinkedIn link or a LinkedIn search link with name and company).
3. Draft a **short LinkedIn connection note** for the user to send themselves: under 200 characters (the limit without Premium), first person, natural, naming the role they applied for and one concrete thing they bring that the posting asks for. Example: "Hi Sara, I've just applied for your Design Systems Designer role. I built and scaled a design system across 15 brands, so this one feels close to home. Would love to connect."
4. Next action: "Message <Name> on LinkedIn", tomorrow. Nobody found → say so in Contact and skip it.

Never send anything: the user sends the note.

## Answering "what's next"

Query cards in CV ready, Applied and Interview sorted by Next action date. Reply with:

1. Overdue and today, then this week.
2. Max 5 items, each with the action and the card link.
3. If anything is stale (no change in 3+ weeks), say so in one line.
4. One line with how many roles are waiting in To review and the best Match among them.

## Weekly review reminder

When the scheduled reminder runs (or the user asks "what's pending to review"), follow section 5 of `notion/applications-schema.md`.

## Weekly hygiene (when asked, or after `job-search`)

Apply the timing table in section 3 of `notion/applications-schema.md` to every active card. Never delete cards during hygiene.

## Clean up my board

Only when the user asks ("clean up my board"). This keeps the board readable; it does not free Notion blocks. If Notion warns that the workspace is out of blocks, explain instead that free workspaces with two or more members have a lifetime cap of 1,000 blocks that deletions don't restore, and that the fix is a workspace where the user is the only member, or a paid plan.

1. List the candidates: **Discarded** cards, plus **Rejected** and **No response** cards applied more than 2 months ago. Leave out anything linked to an active process or a contact the user wants to keep, and say which ones you left and why.
2. Append one line per card to `context/closed-applications.md` (create it if missing): `Company · Role · Status · Applied on`. Future searches read this file, so the user still gets a warning about companies that already said no.
3. Show the list and ask before deleting. Then move the cards to Notion's Trash (never a permanent delete).
4. Cards stay in Notion's Trash for 30 days; the user can empty it sooner. Don't promise that this frees blocks.
