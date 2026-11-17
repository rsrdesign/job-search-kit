# Notion: Applications database

Created by `job-kit-setup` inside the page you choose. All names in English so views and skills match.

## Properties

| Property | Type | Notes |
|---|---|---|
| Application | Title | `Company · Role` |
| Company | Text | |
| Role | Text | |
| Status | Status | To review, CV ready, Applied, Interview, Offer, Rejected, No response, Discarded |
| Match | Number | 0 to 100 |
| Type | Select | Full-time, Contract, Freelance |
| Work mode | Select | On-site, Hybrid, Remote |
| Location | Text | |
| Salary | Text | As published, or "Not stated" |
| Source | Select | Greenhouse, Ashby, Lever, Himalayas, Arbeitnow, Google Jobs, Adzuna, Jooble, LinkedIn, Referral, Other |
| Job link | URL | |
| Posted | Date | |
| Applied on | Date | Only when the user says they sent it |
| CV language | Select | en, es, … |
| Figma | URL | Link to the dated section |
| Folder | Text | Path of the company folder |
| Contact | Text | Recruiter / hiring manager |
| Next action | Text | One concrete step |
| Next action date | Date | |
| Log | Text | Dated one-liners: `2026-11-17: sent CV` |

Optional (network intros):

| Property | Type | Notes |
|---|---|---|
| Network match | Select | Not checked, No match, Possible match, Ask mentor, Asked, Intro done, Not needed |
| Network contacts | Text | Names and roles found |
| Intro done | Checkbox | Ticked when the mentor sent the intro |

## SQL DDL (for the Notion MCP `create-database` tool)

```sql
CREATE TABLE "Applications" (
  "Application" TITLE,
  "Company" RICH_TEXT,
  "Role" RICH_TEXT,
  "Status" STATUS('To review':gray:to_do, 'CV ready':blue:to_do, 'Applied':yellow:in_progress, 'Interview':purple:in_progress, 'Offer':green:complete, 'Rejected':red:complete, 'No response':brown:complete, 'Discarded':default:complete),
  "Match" NUMBER,
  "Type" SELECT('Full-time','Contract','Freelance'),
  "Work mode" SELECT('On-site','Hybrid','Remote'),
  "Location" RICH_TEXT,
  "Salary" RICH_TEXT,
  "Source" SELECT('Greenhouse','Ashby','Lever','Himalayas','Arbeitnow','Google Jobs','Adzuna','Jooble','LinkedIn','Referral','Other'),
  "Job link" URL,
  "Posted" DATE,
  "Applied on" DATE,
  "CV language" SELECT('en','es'),
  "Figma" URL,
  "Folder" RICH_TEXT,
  "Contact" RICH_TEXT,
  "Next action" RICH_TEXT,
  "Next action date" DATE,
  "Log" RICH_TEXT
  -- optional, only if network intros are enabled:
  -- , "Network match" SELECT('Not checked':gray, 'No match':default, 'Possible match':yellow, 'Ask mentor':orange, 'Asked':blue, 'Intro done':green, 'Not needed':brown)
  -- , "Network contacts" RICH_TEXT
  -- , "Intro done" CHECKBOX
)
```

Tested with the Notion MCP: the status options and their groups (to do / in progress / complete) are created in one go.

## Views

| View | Type | Config |
|---|---|---|
| Next actions | Table | Status in (To review, CV ready, Applied, Interview); sort Next action date ascending |
| Pipeline | Board | Group by Status; show Next action, Next action date |
| All | Table | No filter |
| Network | Board | Optional. Group by Network match; filter active statuses and match in (Possible match, Ask mentor, Asked, Intro done) |

## Status rules

- **To review**: found by `job-search`, not yet decided.
- **CV ready**: CV and letter prepared, not sent.
- **Applied**: the user said they sent it. Next action: follow up in 10 days.
- **Interview / Offer**: as reported.
- **Rejected**: the company said no.
- **No response**: applied more than 6 weeks ago, no news.
- **Discarded**: never applied and the posting closed, or the user passed.
