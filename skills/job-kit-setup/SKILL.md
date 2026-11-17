---
name: job-kit-setup
description: First-run setup for the job search kit. Asks a short form about the user's goals, expectations, location and proof, reads their context files, wires Figma, Notion and folders, and writes config/profile.md and config/settings.md.
---

# Job kit setup

Run when `config/profile.md` or `config/settings.md` is missing, or when the user asks to set up or update their kit. Talk to the user in their language.

## 1. Check the prerequisites

Confirm each item quickly and say what's missing before going on:

- Access to the local folder of this kit (you can read and write files).
- Figma MCP connected (try a metadata call on the file they give you).
- Notion connector connected (try a search).
- Optional search keys in `.env` (`SERPAPI_KEY`, `ADZUNA_APP_ID` + `ADZUNA_APP_KEY`, `JOOBLE_KEY`). Check which exist without printing them. None is required.

If something is missing, explain the fix in one line and continue with the rest.

## 2. Read the context first

Read everything in `context/` and any link the user gives (portfolio, LinkedIn text they paste). Pre-fill what you can, so the form only asks for gaps. Never infer things the user didn't say: mark them as questions.

## 3. Ask the form

Ask in small groups (use a multiple-choice question tool if available, free text otherwise). Skip anything already answered by the context.

1. **About you**: name, current title, years of experience, languages and levels, portfolio URL (this will be the only link in cover letters), LinkedIn URL, short bio.
2. **Goals**: target roles, seniority, industries you want and want to avoid, what a great next role looks like, deal-breakers, roles to exclude.
3. **Expectations**: minimum salary and currency (and whether it's flexible), employment type, availability / notice period.
4. **Location**: city, time zone, work mode, countries you can legally work in, relocation.
5. **Proof**: 3 to 6 achievements with real numbers, core skills, tools, how you use AI in your work.
6. **Wiring**:
   - Figma file URL, CV frame link and cover letter frame link (per language they have).
   - Output page in that file for tailored copies (default: a new page "Tailored").
   - Notion page URL where the tracker should live.
   - Absolute path of the applications folder.
   - Search days and time; city / country for the optional city search engines.
   - Network intros: yes or no; if yes, mentor name and CSV path (consent required).

## 4. Map the Figma layers

For each base frame, list its visible text layers (name + first 60 characters). Propose a layer map (headline, summary, bullets per job, skills, recipient, body paragraphs, date) and the link colour (an accent fill already used in the letter). Ask the user to confirm or correct. Store it in `settings.md`.

If layers have generic names ("Text 12"), suggest the user renames them, or map by content and say so.

## 5. Create the Notion tracker

Follow `notion/applications-schema.md`: create the Applications database in the chosen page, then the views. Save the data source URL in `settings.md`. Add the network properties and view only if intros are enabled.

## 6. Write the files

- `config/profile.md` from `config/profile.example.md`.
- `config/settings.md` from `config/settings.example.md`.
- `config/sources.md` from `config/sources.example.md`, with queries built from target roles + location. Ask which companies they'd love to work for and suggest 5 to 10 more in their industries. For each, find the platform and token from its careers page (Greenhouse, Ashby or Lever) and verify the API returns jobs before adding it. Companies on other platforms go under "Links you paste".
- Create the applications folder if it doesn't exist.

## 7. Offer the schedule

Offer a scheduled task on the chosen days that runs `job-search`. Create it only if the user says yes.

## 8. Wrap up

Show a 5-line summary (roles, location, salary floor, sources, where things will be saved) and suggest: "Find me new roles".
