---
name: network-intros
description: Optional. Cross-checks the companies the user applies to against a mentor's LinkedIn connections CSV (shared with consent) and fills the Network columns in Notion so the mentor can see where a quick intro would help.
---

# Network intros (optional)

Only if `settings.md` has network intros enabled and the CSV path exists. The CSV holds other people's personal data: read it locally, never copy it into the repo, Notion page text or any public place. Only the matches go into Notion.

Expected columns (LinkedIn export, renamed if needed): `name, position, company, url, connected_on`. See `examples/network.example.csv`.

## When it runs

- When a card becomes **Applied** or **Interview**.
- On demand: "who can introduce me at <company>?"

## Matching

1. Normalise company names (lowercase, drop Ltd / Inc / SL / GmbH, "&" = "and"). Also check known brand vs legal names (e.g. a product name vs the parent company).
2. Exact or clear match → candidate. Prefer design, product and hiring roles; then leadership.
3. Write to the card:
   - **Network match**: "Possible match" (found), "No match", or "Not needed" (the user already has a contact).
   - **Network contacts**: up to 3 people as `Name · Position`.
   - Next action: "Ask <mentor> for an intro to <Name>" only if the user agrees.

## When the mentor acts

When the user says the mentor sent an intro or a message:

- Tick **Intro done**, set Network match "Intro done".
- Log `YYYY-MM-DD: <mentor> introduced <Name>`.
- Next action: "Follow up with <Name>" in 3 days.

## Sharing with the mentor

The Network board view in Notion shows only the roles where they could help. Share that page with them from Notion; never send the CSV anywhere.
