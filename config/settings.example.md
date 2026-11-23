# Settings

> Filled in by `job-kit-setup`. Technical wiring only; personal facts go in `profile.md`.

## CV source

- CV source: {{figma | document | text}}  <!-- document = Word, Pages or Google Docs copies; text = Markdown → PDF -->
- Export PDFs: {{after approval | automatic}}  <!-- default: after approval -->
- ATS CV: {{figma | document | generated | off}}  <!-- one-column version for job portals; generated (default) = a plain one-column PDF made from the tailored text -->

## Figma (only if CV source is figma)

- File key: {{FIGMA_FILE_KEY}}  <!-- from figma.com/design/<FILE_KEY>/... -->
- Output page: {{PAGE_NAME_OR_ID}}  <!-- where tailored copies are placed -->

| Language | CV frame | Cover letter frame | ATS CV frame(s) (optional) |
|---|---|---|---|
| en | {{NODE_ID}} | {{NODE_ID}} | {{NODE_ID, or p1 + p2 node IDs, or "none"}} |
| es | {{NODE_ID or "none"}} | {{NODE_ID or "none"}} | {{NODE_ID(s) or "none"}} |

### Layer map

Text layers the kit is allowed to rewrite, by layer name. Everything else stays as designed.

| Role | CV layer name(s) | Cover letter layer name(s) |
|---|---|---|
| Headline / title | {{e.g. Puesto}} | {{e.g. Puesto}} |
| Summary | {{e.g. Resumen profesional}} | |
| Bullets per job | {{e.g. Logros · *}} | |
| Skills | {{e.g. Competencias principales}} | |
| Recipient | | {{e.g. Destinatario}} |
| Body paragraphs | | {{e.g. Motivación, Experiencia e impacto, Forma de trabajar, Cierre}} |
| Date | | {{e.g. Fecha}} |
| Link colour (hex) | | {{#RRGGBB}} |

### Section style

- Section fill: {{#E1E1E1}}, stroke: black 10%
- Layout: CV left, cover letter right, 40 px gap, 60 px top padding

## Document (only if CV source is document)

- Format: {{docx | gdocs | pages}}
- PDF export with: {{LibreOffice | Google Drive | Pages | Word | manual}}

| Language | Base CV (path or link) | Base cover letter (path or link) | Base ATS CV (optional) |
|---|---|---|---|
| en | {{PATH_OR_URL}} | {{PATH_OR_URL}} | {{PATH_OR_URL or "none"}} |
| es | {{PATH_OR_URL or "none"}} | {{PATH_OR_URL or "none"}} | {{PATH_OR_URL or "none"}} |

### Text map

Parts the kit is allowed to rewrite, by the heading or first words of the paragraph. Everything else stays as designed.

| Role | CV | Cover letter |
|---|---|---|
| Headline / title | {{e.g. first line under the name}} | |
| Summary | {{e.g. paragraph under "Profile"}} | |
| Bullets per job | {{e.g. bullets under each job title}} | |
| Skills | {{e.g. list under "Skills"}} | |
| Recipient | | {{e.g. "Dear ..." line}} |
| Body paragraphs | | {{e.g. all paragraphs between greeting and sign-off}} |
| Date | | {{e.g. top-right date}} |

## Notion

- Parent page: {{NOTION_PAGE_URL}}
- Applications data source: {{collection://...}}  <!-- filled after the database is created -->

## Files

- Applications folder: {{ABSOLUTE_PATH}}
- File name pattern: `CV_{{First_Last}}_{lang} (Company) YYYY-MM-DD.pdf`, `CV_{{First_Last}}_{lang} ATS (Company) YYYY-MM-DD.pdf`, `CoverLetter_{{First_Last}}_{lang} (Company) YYYY-MM-DD.pdf`
- PDF author: {{First Last}}  <!-- written into every exported PDF, with the file name as its title -->
- Active-process prefix: `*`

## Search

- Last search: {{YYYY-MM-DD HH:MM}}  <!-- updated by job-search after every run -->

- Days: {{e.g. Monday, Wednesday}} at {{e.g. 08:30}} {{TIME_ZONE}}  <!-- needs the computer on -->
- Review reminder: {{Wednesday 12:30, or "off"}}  <!-- lists the To review cards; see notion/applications-schema.md section 5 -->
- City search location (optional engines): {{e.g. Madrid, Community of Madrid, Spain}}
- `hl` / `gl`: {{es}} / {{es}}

## Reach out myself (optional, for users without a mentor)

- Reach out myself: {{on | off}}  <!-- after you apply, suggests who to message and drafts a short LinkedIn note you send yourself -->
- My network CSV: {{context/my-network.csv or "none"}}  <!-- your own LinkedIn connections export, checked first -->

## Mentor panel (optional)

<!-- To use the mentor's first name instead of "Mentor" in Notion, set it below; see notion/applications-schema.md section 4. -->

- Enabled: {{yes/no}}
- Mentor first name (used for the tab and columns): {{NAME}}
- CSV path: {{context/network.csv}}  <!-- with their consent; never commit -->
- Mentor email: {{email or "none"}}  <!-- for the optional weekly email -->
- Weekly email: {{off | draft | send}} on {{e.g. Thursday}} at {{e.g. 09:30}} {{TIME_ZONE}}  <!-- send only if the user explicitly allowed it; default draft -->
- Send from: {{the user's connected mail account}}
- Check mentor reply: {{off | on}} on {{e.g. Wednesday}} at {{e.g. 10:15}} {{TIME_ZONE}}  <!-- 6 days after the weekly email; needs a mail tool that can read the inbox -->
