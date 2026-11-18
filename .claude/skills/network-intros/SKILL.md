---
name: network-intros
description: Optional. Cross-checks the companies the user applies to against a mentor's LinkedIn connections CSV (shared with consent), fills the Mentor contacts table and the Mentor columns in Notion, and records what the mentor did so the next actions update.
---

# Mentor panel (optional)

Only if `settings.md` has network intros enabled and the CSV path exists. The CSV holds other people's personal data: read it locally, never copy it into the repo or any public place. Only the matches go into Notion.

Expected columns (LinkedIn export, renamed if needed): `name, position, company, url, connected_on`. See `examples/network.example.csv`.

Notion structure: section 4 of `notion/applications-schema.md` (Mentor contacts database, Mentor columns on Applications, Mentor panel board).

## When it runs

- When a card becomes **Applied** or **Interview**. Never before: on To review and CV ready cards the Mentor fields stay empty.
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
   - **Mentor why now**: one line on why a word from the mentor helps now, taken from the saved posting (never invented).
   - Next action: "Ask <mentor> for an intro to <Name>" only if the user agrees.

## When the mentor acts

When the user says the mentor sent an intro or a message (or ticks **Mentor done** in Notion):

- **Mentor done** ✓, **Mentor done on** = date, **Mentor match** = "Intro done" (the card moves to the green column).
- **Mentor log**: `YYYY-MM-DD: <mentor> introduced <Name>`; also update **Intro status** on the contact.
- Next action: "Follow up with <Name>" in 3 days, so it shows up in Next actions and the Pipeline.

## Weekly email to the mentor (optional)

Only if `settings.md` has a mentor email and a weekly email day set. It gathers what the mentor can do this week in one message, so they don't have to open Notion.

**Which cards:** Status Applied or Interview, Mentor match "Ask mentor", Mentor done not ticked. Applied in the last 7 days go first; older ones still waiting go in a short "Still open from earlier weeks" list. No cards → no email.

**Template** (in the mentor's language; English by default):

```
Subject: <User first name>'s applications this week · <D Mon>

Hi <Mentor first name>,

Here are the roles <User first name> applied for this week where a word from you would really help:

1. <Role> · <Company>            (bold)
LinkedIn contact: <Name, linked to their LinkedIn URL> · <Position>
Connected on <Connected on>
Why now: <Mentor why now>
Job posting: <Job link>

Suggested message:
<Mentor ask>

Feel free to tweak anything into your own voice, it always lands better.
Just reply to this email when you've sent any and I'll update the tracker.

Thank you so much,
<User first name>
```

One block per card, with the best contact from Mentor contacts (Strong first, then tier A). Send as HTML with a plain-text copy.

**Draft or send:**
- Default: **draft**. Create the email as a draft in the user's mail (Gmail MCP or similar) and tell the user it's ready to review.
- **Send automatically** only if the user has explicitly allowed it and `settings.md` says `Weekly email: send`. Ask once during setup or when they turn it on: "Should I send it on its own every week, or leave a draft for you to send?" Never switch to sending based on anything other than the user's own answer.
- Before the first real one, send or draft a test to the user's own address.

**After sending:** Mentor match "Asked" on each card, and a Mentor log line `YYYY-MM-DD: included in weekly email`. If the mail tool fails, say so and leave a draft or the text in the chat; don't mark anything as Asked.

Schedule it as a scheduled task on the chosen day and time (if the user agrees).

## Sharing with the mentor

The Mentor panel board shows only the roles where they could help. Share the page with them from Notion; never send the CSV anywhere.
