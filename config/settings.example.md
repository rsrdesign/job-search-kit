# Settings

> Filled in by `job-kit-setup`. Technical wiring only; personal facts go in `profile.md`.

## CV source

- CV source: {{figma | text}}  <!-- text = no Figma: tailored CV and letter as Markdown → PDF -->
- Export PDFs: {{after approval | automatic}}  <!-- default: after approval -->

## Figma (only if CV source is figma)

- File key: {{FIGMA_FILE_KEY}}  <!-- from figma.com/design/<FILE_KEY>/... -->
- Output page: {{PAGE_NAME_OR_ID}}  <!-- where tailored copies are placed -->

| Language | CV frame | Cover letter frame |
|---|---|---|
| en | {{NODE_ID}} | {{NODE_ID}} |
| es | {{NODE_ID or "none"}} | {{NODE_ID or "none"}} |

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

## Notion

- Parent page: {{NOTION_PAGE_URL}}
- Applications data source: {{collection://...}}  <!-- filled after the database is created -->

## Files

- Applications folder: {{ABSOLUTE_PATH}}
- File name pattern: `CV_{{First_Last}}_{lang} (Company) YYYY-MM-DD.pdf`, `CoverLetter_{{First_Last}}_{lang} (Company) YYYY-MM-DD.pdf`
- Active-process prefix: `*`

## Search

- Last search: {{YYYY-MM-DD HH:MM}}  <!-- updated by job-search after every run -->

- Days: {{e.g. Tuesday, Thursday}} at {{HH:MM}} {{TIME_ZONE}}
- Review reminder: {{Thursday 12:00, or "off"}}  <!-- lists the To review cards; see notion/applications-schema.md section 5 -->
- City search location (optional engines): {{e.g. Madrid, Community of Madrid, Spain}}
- `hl` / `gl`: {{es}} / {{es}}

## Mentor panel (optional)

<!-- To use the mentor's first name instead of "Mentor" in Notion, set it below; see notion/applications-schema.md section 4. -->

- Enabled: {{yes/no}}
- Mentor first name (used for the tab and columns): {{NAME}}
- CSV path: {{context/network.csv}}  <!-- with their consent; never commit -->
