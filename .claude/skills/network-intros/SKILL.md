---
name: network-intros
description: Optional. Cross-checks the companies the user applies to against a mentor's LinkedIn connections CSV (shared with consent), fills the Mentor contacts table and the Mentor columns in Notion, and records what the mentor did so the next actions update.
---

# Mentor panel (optional)

Only if `settings.md` has network intros enabled and the CSV path exists. The CSV holds other people's personal data: read it locally, never copy it into the repo or any public place. Only the matches go into Notion.

Expected columns (LinkedIn export, renamed if needed): `name, position, company, url, connected_on`. See `examples/network.example.csv`.

Notion structure: section 4 of `notion/applications-schema.md` (Mentor contacts database, Mentor columns on Applications, Mentor panel board).

## When it runs

- When a card becomes **Applied** or **Interview**.
- On demand: "who can introduce me at <company>?"

## Matching

1. Normalise company names (lowercase, drop Ltd / Inc / SL / GmbH, "&" = "and"). Also check known brand vs legal names.
2. Clear match → create (or reuse) a row in **Mentor contacts** with Name, Company, Position, LinkedIn, Connected on, and:
   - **Tier**: A · Hiring managers (design / product leads), B · Founders & CEOs, C · Brand & Marketing, D · Talent & peers.
   - **Relevance**: Strong (same team or hiring manager), Possible, Weak.
3. On the application card:
   - Link the people in **Mentor contacts** (max 3, best tier first).
   - **Mentor match**: "Possible match", "Ask mentor" (a Strong / tier A contact, worth an intro), "No match", or "Not needed" (the user already has a contact).
   - **Mentor ask**: for "Ask mentor", a short ready-to-send message the user can forward to the mentor (who, why, one line about the role).
   - Next action: "Ask <mentor> for an intro to <Name>" only if the user agrees.

## When the mentor acts

When the user says the mentor sent an intro or a message (or ticks **Mentor done** in Notion):

- **Mentor done** ✓, **Mentor done on** = date, **Mentor match** = "Intro done" (the card moves to the green column).
- **Mentor log**: `YYYY-MM-DD: <mentor> introduced <Name>`; also update **Intro status** on the contact.
- Next action: "Follow up with <Name>" in 3 days, so it shows up in Next actions and the Pipeline.

## Sharing with the mentor

The Mentor panel board shows only the roles where they could help. Share the page with them from Notion; never send the CSV anywhere.
