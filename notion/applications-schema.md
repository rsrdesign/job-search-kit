# Notion: Jobs tracking page

Created by `job-kit-setup` inside the page the user chooses. All names in English so views and skills match. Build it exactly in this order so it looks the same for everyone.

## 1. Page

- Use the page the user gave. Title **Jobs tracking** (unless they already named it), icon 💼, full width. Keep their cover if the page has one. If the page already has content, add everything below it and don't delete anything.
- First block (paragraph):

  > One card per job: **To review** → **CV ready** → **Applied** → **Interview** → **Offer** (or Rejected · No response · Discarded). Every active application has a next action with a date. Interview notes and replies go inside each card.

- A divider.
- The **Applications** database, **inline**.
- If network intros are enabled (section 4): heading `## 🤝 Mentor panel`, a paragraph, a linked board view and the **Mentor contacts** database, inline.

## 2. Applications database

Description: "One card per job. Every active application has a next action with a date."

| Property | Type | Notes |
|---|---|---|
| Application | Title | `Company · Role` |
| Company | Text | |
| Role | Text | |
| Status | Status | To do: To review · In progress: CV ready, Applied, Interview · Complete: Offer, Rejected, No response, Discarded |
| Match | Number | 0 to 100, set by `job-search` (fit between the role and your profile) |
| CV score | Text | Set by `tailor-application`: requirements covered by the CV, before → after, e.g. `5/7 → 7/7` |
| Type | Select | Full-time, Freelance, Contract |
| Work mode | Select | Remote, Hybrid, On-site, Not stated |
| Location | Text | |
| Salary | Text | As published, or "Not stated" |
| Source | Select | Greenhouse, Ashby, Lever, Himalayas, Arbeitnow, Google Jobs, Adzuna, Jooble, LinkedIn, Indeed, Workable, Pasted link, Referral, Other. Anything the user pastes that isn't listed is "Pasted link" |
| Job link | URL | |
| Posted | Date | |
| Applied on | Date | Only when the user says they sent it |
| CV language | Select | EN, ES. For another language, add an option with its two-letter code (e.g. FR) in the DDL before creating, or later with `update-data-source` |
| Figma CV | URL | Link to the dated Figma section |
| Folder | Text | Path of the company folder |
| Contact | Text | Recruiter / hiring manager |
| Next action | Text | One concrete step |
| Next action date | Date | |

History (what was sent, replies, interview notes) goes **inside the card** as dated lines, not in a property. The card also keeps a copy of the posting ("Job posting (saved YYYY-MM-DD)"), so it is still there if the job is taken down.

### DDL (Notion MCP `create-database`, with `parent` = the page)

```sql
CREATE TABLE (
  "Application" TITLE,
  "Company" RICH_TEXT,
  "Role" RICH_TEXT,
  "Status" STATUS('To review':gray:to_do, 'CV ready':yellow:in_progress, 'Applied':blue:in_progress, 'Interview':purple:in_progress, 'Offer':green:complete, 'Rejected':red:complete, 'No response':default:complete, 'Discarded':brown:complete),
  "Match" NUMBER,
  "CV score" RICH_TEXT,
  "Type" SELECT('Full-time':blue, 'Freelance':orange, 'Contract':yellow),
  "Work mode" SELECT('Remote':green, 'Hybrid':blue, 'On-site':purple, 'Not stated':gray),
  "Location" RICH_TEXT,
  "Salary" RICH_TEXT,
  "Source" SELECT('Greenhouse':green, 'Ashby':purple, 'Lever':blue, 'Himalayas':pink, 'Arbeitnow':orange, 'Google Jobs':blue, 'Adzuna':yellow, 'Jooble':brown, 'LinkedIn':purple, 'Indeed':blue, 'Workable':green, 'Pasted link':default, 'Referral':orange, 'Other':gray),
  "Job link" URL,
  "Posted" DATE,
  "Applied on" DATE,
  "CV language" SELECT('EN':blue, 'ES':red),
  "Figma CV" URL,
  "Folder" RICH_TEXT,
  "Contact" RICH_TEXT,
  "Next action" RICH_TEXT,
  "Next action date" DATE
)
```

### Views (on the database, in this order)

| View | Type | Icon | Config |
|---|---|---|---|
| Pipeline | Board | `icons/cards_gray` | `GROUP BY "Status" BY OPTION SHOW EMPTY; SORT BY "Match" DESC; SHOW "Application", "Match", "Next action", "Next action date"; CARD LAYOUT compact` |
| Next actions | Table | `icons/list_gray` | `FILTER "Status" IN ("CV ready", "Applied", "Interview"); SORT BY "Next action date" ASC; SHOW "Application", "Status", "Next action date", "Next action", "Match", "CV score", "Applied on", "Job link"` |
| All | Table | `icons/checklist_gray` | `SORT BY "Applied on" DESC; SHOW "Application", "Status", "Applied on", "Location", "Work mode", "Type", "Salary", "Source", "Job link", "CV language", "Figma CV", "Folder", "Contact", "Next action", "Next action date"` |

Tab order the user should end up with: **Pipeline · Next actions · <Mentor> · All** (the mentor tab only if intros are enabled; see section 4).

How to build them with the Notion MCP (tested):

1. The database is created with a "Default view" table, and a view can't change type. Turn it into **Next actions** with `update-view` (name + configure).
2. Create **Pipeline** (board), then the mentor board if enabled, then **All** (table) with `create-view` on the database.
3. Never leave a view with a placeholder name ("Default view", "delete me"). Views can't be deleted or reordered through the MCP, so don't create extra ones.
4. The MCP can't move tabs, so Pipeline ends up second. In the finish message, tell the user: "Drag the Pipeline tab to the first place" (one drag).

`create-database` always makes a full-page database. To show it **inline** on the page, fetch the page and replace `inline="false"` with `inline="true"` in its `<database ...>` tag with `update-page` (`update_content`).

## 3. Status and timing rules (single source of truth)

Every skill follows this section. Day counts start on **Applied on**.

| Status | When | Next action |
|---|---|---|
| To review | Found by `job-search`, not decided | None: the card waits for the user's decision (the Match is on the card) |
| CV ready | CV and letter prepared, not sent | "Review CV + cover letter and send", today + 1 day |
| Applied | The user said they sent it (only the user can set this) | Day 10: "Follow up with <contact or recruiter>" |
| Applied, after a follow-up | No reply to the first follow-up | Day 24: "Second and last follow-up" |
| No response | Day 42 (6 weeks) with no reply at all | "None. Reopen if they reply" |
| Interview | Interview scheduled or done | "Prepare: <topic>" the day before; "Send thank-you note" the same day after |
| Offer | Offer received | "Review offer" |
| Rejected | The company said no | "Ask for feedback / keep <contact> warm", or "None" |
| Discarded | Never applied and the posting closed, or the user passed | "None" |

To review cards are listed in the weekly review reminder (section 5). Older than 14 days → ask the user to decide or discard. Never delete cards.

## 4. Mentor panel (optional, only if network intros are enabled)

**Renaming:** the template says "Mentor". If the user prefers the mentor's first name, replace "Mentor" in every property, tab and heading (e.g. "Sam match", "Sam contacts", "🤝 Sam panel") and write the chosen name in `settings.md` so the skills use it.

### Mentor contacts database (inline, under the panel heading)

Description: "People in the mentor's network who work at a company the user has applied to. Added when an application is crossed against the network."

```sql
CREATE TABLE (
  "Name" TITLE,
  "Company" RICH_TEXT,
  "Position" RICH_TEXT,
  "LinkedIn" URL,
  "Connected on" RICH_TEXT,
  "Tier" SELECT('A · Hiring managers':green, 'B · Founders & CEOs':blue, 'C · Brand & Marketing':purple, 'D · Talent & peers':gray),
  "Relevance" SELECT('Strong':green, 'Possible':yellow, 'Weak':gray),
  "Intro status" RICH_TEXT
)
```

### Add to Applications (with `update-data-source`)

| Property | Type | Notes |
|---|---|---|
| Mentor match | Select | Not checked (gray), No match (default), Possible match (yellow), Ask mentor (orange), Asked (blue), Intro done (green), Not needed (brown) |
| Mentor contacts | Relation | Two-way to Mentor contacts (synced property there: "Applications"). DDL: `"Mentor contacts" RELATION('<Mentor contacts data source id>', DUAL 'Applications')` |
| Mentor ask | Text | Ready-to-send message for the mentor |
| Mentor done | Checkbox | Ticked when the mentor sent the intro or message |
| Mentor done on | Date | |
| Mentor log | Text | What the mentor did, dated |

Also add "Mentor match" and "Mentor done on" to the Pipeline and Next actions views (a date stays hidden on the card until it is set; a checkbox would show on every card), and "Mentor match" to All. The Mentor fields stay empty until the card is Applied: the mentor can't help before the user has applied.

Mentor tab on the Applications database (board, named with the mentor's first name, icon `icons/hand_gray`), created between Next actions and All: same filter and grouping as the panel board below, `SHOW "Application", "Status", "Mentor contacts", "Mentor done", "Next action"`.

### Page blocks

1. `## 🤝 Mentor panel`
2. Paragraph: "When an application moves to **Applied**, it is cross-referenced against the mentor's LinkedIn network. Matches are linked in **Mentor contacts** and the card gets a **Mentor match** value. **Ask mentor** means it is worth asking for an intro, and **Mentor ask** holds a ready-to-send message."
3. Linked board view of Applications ("Mentor panel · actions for the mentor"): `FILTER "Status" IN ("Applied", "Interview") AND "Mentor match" IN ("Possible match", "Ask mentor", "Asked", "Intro done"); GROUP BY "Mentor match" HIDE EMPTY; SHOW "Application", "Status", "Mentor contacts", "Mentor ask", "Mentor done", "Mentor done on", "Mentor log"`
4. The Mentor contacts database.

## 5. Weekly review reminder (optional)

A scheduled task, by default every **Thursday at 12:00** in the user's time zone (`Review reminder` in `settings.md`). It lists every **To review** card, highest Match first: Match, company and role, location or work mode, salary as published (or "Not stated"), days in To review and the job link. Cards older than 14 days get a "⚠" (they may close soon). It ends by asking which ones to prepare. It never changes Notion, tailors or sends anything.
