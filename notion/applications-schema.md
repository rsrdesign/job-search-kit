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
| Score | Formula | The Match as a coloured pill for cards: green 90 to 100, yellow 60 to 89, red 0 to 59 |
| ATS coverage | Number | Set by `tailor-application` after tailoring: % of the posting's key requirements that appear explicitly in the tailored CV (1 if named, 0.5 if partly). Different from Match: Match is your real fit, ATS coverage is how well the CV shows it |
| ATS | Formula | ATS coverage as a pill, e.g. `ATS 86%`, shown only on **CV ready** cards so the board stays simple: Match in To review, ATS in CV ready |
| Type | Select | Full-time, Freelance, Contract |
| Work mode | Select | Remote, Hybrid, On-site, Not stated |
| Location | Text | |
| Salary | Text | As published, or "Not stated" (in the posting's language, e.g. "No indicado") |
| Suggested salary | Text | Only when the posting has no salary: a realistic gross yearly range for that company type, size and level, plus a short why (e.g. `€50-55K · mid-size edtech, senior IC`). Not too high, so the application isn't filtered out, and never below the minimum salary in `profile.md`. A suggestion for forms and calls, not a fact from the posting |
| Salary hint | Formula | Shows on To review cards only: the suggested salary with its why, or the published salary. It disappears once the card moves on, and stays in the detail |
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
  "Score" FORMULA('if(empty(prop("Match")), "", if(prop("Match") >= 90, style(format(prop("Match")), "b", "green", "green_background"), if(prop("Match") >= 60, style(format(prop("Match")), "b", "yellow", "yellow_background"), style(format(prop("Match")), "b", "red", "red_background"))))'),
  "ATS coverage" NUMBER,
  "ATS" FORMULA('if(prop("Status") == "CV ready" and not empty(prop("ATS coverage")), style("ATS " + format(prop("ATS coverage")) + "%", "b", "blue", "blue_background"), "")'),
  "Type" SELECT('Full-time':blue, 'Freelance':orange, 'Contract':yellow),
  "Work mode" SELECT('Remote':green, 'Hybrid':blue, 'On-site':purple, 'Not stated':gray),
  "Location" RICH_TEXT,
  "Salary" RICH_TEXT,
  "Suggested salary" RICH_TEXT,
  "Salary hint" FORMULA('if(prop("Status") == "To review", if(not empty(prop("Suggested salary")), prop("Suggested salary"), if(empty(prop("Salary")) or prop("Salary") == "Not stated", "", prop("Salary") + " · published")), "")'),
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

**Optional: Talent pool.** Only if `settings.md` has `Talent pool column: on`. Add `'Talent pool':pink:in_progress` to the Status list, right after `'Applied':blue:in_progress`, and add `"Talent pool"` to the Next actions filter. It is for companies with **no open role** where the user still left their CV: a careers-site candidate profile, a "Work with us" open application or a spontaneous email. It keeps those apart from real applications, so follow-ups and the mentor email never treat them as Applied. To add it later, run the same `ALTER COLUMN "Status" SET STATUS(...)` with every existing option plus Talent pool (omitted options are removed).

### Views (on the database, in this order)

| View | Type | Icon | Config |
|---|---|---|---|
| Pipeline | Board | `icons/cards_gray` | `GROUP BY "Status" BY OPTION SHOW EMPTY; SORT BY "Match" DESC; SHOW "Application", "Score", "ATS", "Next action", "Next action date", "Salary hint"; CARD LAYOUT compact` |
| Next actions | Table | `icons/list_gray` | `FILTER "Status" IN ("CV ready", "Applied", "Interview"); SORT BY "Next action date" ASC; SHOW "Application", "Status", "Next action date", "Next action", "Score", "ATS coverage", "Applied on", "Job link"` |
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
| To review | Found by `job-search`, not decided | None: the card waits for the user's decision (the Score pill and the saved posting are on the card) |
| CV ready | CV and letter prepared, not sent | "Review CV + cover letter and send", today + 1 day |
| Talent pool (optional) | No open role; the user left their CV in the company's candidate platform, open application or a spontaneous email (only the user can set this). Applied on = that date | Day 5: "Message <design lead> on LinkedIn"; then day 60: "Check their careers page for new roles" |
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
| Mentor why now | Text | One line on why the mentor's help matters now (from the posting); used in the weekly email |
| Mentor done | Checkbox | Ticked when the mentor sent the intro or message |
| Mentor done on | Date | |
| Mentor log | Text | What the mentor did, dated |
| Mentor | Formula | The mentor status for cards only once you've applied: `if(or(prop("Status") == "Applied", prop("Status") == "Interview"), if(empty(prop("Mentor match")), "Mentor: Not checked", "Mentor: " + prop("Mentor match")), "")` |

Add "Mentor" (the formula, so To review and CV ready cards stay clean) and "Mentor done on" to the Pipeline view, "Mentor match" and "Mentor done on" to Next actions (a date stays hidden on the card until it is set; a checkbox would show on every card), and "Mentor match" to All. The Mentor fields stay empty until the card is Applied: the mentor can't help before the user has applied.

Mentor tab on the Applications database (board, named with the mentor's first name, icon `icons/hand_gray`), created between Next actions and All: same filter and grouping as the panel board below, `SHOW "Application", "Status", "Mentor contacts", "Mentor done on", "Next action"`.

### Page blocks

1. `## 🤝 Mentor panel`
2. Paragraph: "When an application moves to **Applied**, it is cross-referenced against the mentor's LinkedIn network. Matches are linked in **Mentor contacts** and the card gets a **Mentor match** value. **Ask mentor** means it is worth asking for an intro, and **Mentor ask** holds a ready-to-send message."
3. Linked board view of Applications ("Mentor panel · actions for the mentor"): `FILTER "Status" IN ("Applied", "Interview") AND "Mentor match" IN ("Possible match", "Ask mentor", "Asked", "Intro done"); GROUP BY "Mentor match" HIDE EMPTY; SHOW "Application", "Status", "Mentor contacts", "Mentor ask", "Mentor done", "Mentor done on", "Mentor log"`
4. The Mentor contacts database.

## 5. Weekly review reminder (optional)

A scheduled task, by default every **Wednesday at 12:30**, after the Monday and Wednesday searches in the user's time zone (`Review reminder` in `settings.md`). It lists every **To review** card, highest Match first: Match, company and role, location or work mode, salary as published (or "Not stated"), days in To review and the job link. Cards older than 14 days get a "⚠" (they may close soon). It ends by asking which ones to prepare. It never changes Notion, tailors or sends anything.
