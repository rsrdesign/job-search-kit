---
name: tailor-application
description: Tailors the user's CV and writes a cover letter for a chosen role, in Figma (duplicates the base frames and rewrites only the mapped text layers), in a copy of the user's Word, Pages or Google Docs file, or as text if there is no designed CV. Exports PDFs only after the user approves, and updates Notion to CV ready.
---

# Tailor an application

Only for a role the user picked. Same employers, dates, titles and numbers: only the wording, the order of bullets and the skills change, to name what the posting asks for and the user has actually done. Never add experience, tools or results that aren't in the base CV, `profile.md`, `context/evidence.md` or `context/`. Something proven in `evidence.md` (LinkedIn, portfolio) but missing from the CV is a gap the CV can cover: say where it comes from. Never send anything.

`DATE` = today as `YYYY-MM-DD`. `Name` = the user's name as `First_Last`.

## 0. Language

- Posting written in a language the user has a base for → that language.
- Otherwise → English (British English for UK / Europe).
- Set **CV language** on the card, and if the card text is in another language than the posting, translate it to the posting's language before you start.

## 1. Score before touching anything

Read the whole posting.

- Denominator = each must-have requirement in the posting.
- Per line: 1 if the base CV names it, 0.5 if partly, 0 if not.
- Show `n/d` and the % with each line and its score, quoting the posting. This is the **ATS coverage** before tailoring.
- Split gaps into **coverable** (the user has done it but the CV doesn't say so) and **real** (not in any source: don't invent, mention for the letter or the interview).

## 2. CV in Figma

Sections 2 to 5b are for `CV source: figma`. For Word, Pages or Google Docs go to 5d; with no designed CV, 5c.


Use the Figma MCP (`create_session`, then `use_figma`; load the `figma-use` skill if your client has it).

1. Clone the CV base frame for the language (from `settings.md`) onto the output page. Name it `CV_<Name>_<lang> (<Company>) <DATE>`.
2. Rewrite only the layers in the layer map: headline, summary, bullets, skills. Keep a similar length (frames are fixed size). Load each font before writing. Keep existing bold / colour ranges where they make sense.
3. Screenshot it and check nothing is cut off or overlapping. Re-score with the new text.

## 3. Cover letter in Figma

1. Clone the cover letter base frame. Name it `CoverLetter_<Name>_<lang> (<Company>) <DATE>`.
2. Rewrite only the mapped layers:
   - **Recipient**: the hiring manager's name if the posting gives it; otherwise "Dear Hiring Team," / the equivalent in the letter's language.
   - **Body**: why this product or company (specific, from the posting); one paragraph of proof with real numbers from the CV; what the user would bring, mapped to the posting; availability. 250 to 350 words. No clichés, no long dashes.
   - **Date**: today, in the letter's language.
   - Role title in the semibold weight of the base, if the base does that.
3. The only link is the portfolio URL from `profile.md`: as a text link, in the link colour from `settings.md`, underlined. Never attach or mention other files.
4. **Re-stack the paragraphs.** If the body paragraphs are not inside an auto layout frame, their positions are fixed, so shorter or longer text leaves gaps or overlaps. Measure the gap between paragraphs in the base frame and place each paragraph at `previous.y + previous.height + gap`. Check that the last one still ends above the sign-off.
5. Screenshot and check.

## 4. Group in a section

Create a Figma Section named `<Company> · <DATE>` with the CV on the left and the letter on the right (40 px gap, 60 px top padding), styled as in `settings.md` (default fill `#E1E1E1`, black 10% stroke). Place it to the right of the last section on the page.

## 5. Files

In `<applications folder>/*<Company>/` (create it; if `<Company>` exists without `*`, use it and say so):

- **Cover letter text**: `CoverLetter_<Name>_<lang> (<Company>) <DATE>.txt`, ready to paste into application forms (with the full portfolio URL).

## 5b. Export PDFs (after the user approves)

PDFs are the version that gets sent, so they are made **after** the user has reviewed the Figma section, unless `settings.md` says `Export PDFs: automatic`.

When the user says "export", "looks good", "approved" (or the setting is automatic):

1. Export both frames as PDF (`download_assets` with format `pdf`, or `exportAsync` if your client returns bytes). Save as `CV_<Name>_<lang> (<Company>) <DATE>.pdf` and `CoverLetter_<Name>_<lang> (<Company>) <DATE>.pdf`.
   - If your environment can't reach figma.com directly, download them through a browser tool (e.g. Claude in Chrome) (open `https://www.figma.com/robots.txt`, `fetch` each asset URL, save them with an `<a download>`; bundle several files in one zip to avoid the multiple-downloads block) and move them from Downloads into the folder. This needs the agent to have access to your **Downloads** folder as well as the applications folder (in the Claude desktop app: grant both folders when asked). Without it, the PDFs stay in Downloads and you move them yourself.
2. If the user edits Figma later, export again on request and overwrite.

## 5c. Text mode (no Figma)

If `settings.md` has `CV source: text`, skip sections 2 to 4 and 5b:

1. Read the base CV from `context/` (PDF, DOCX, Markdown or text).
2. Write the tailored CV and the letter as Markdown in the company folder: `CV_<Name>_<lang> (<Company>) <DATE>.md` and `CoverLetter_<Name>_<lang> (<Company>) <DATE>.md`. Same rules: reword and reorder only, same length, portfolio as the only link.
3. After the user approves, convert both to PDF with whatever is available (pandoc, or an HTML file printed to PDF) using a clean one-column layout, which is also ATS friendly.

## 5d. Document mode (Word, Pages, Google Docs)

If `settings.md` has `CV source: document`. Same idea as Figma: the base files stay untouched, each role gets a copy, and only the mapped text changes, so the user's own layout survives.

1. **Duplicate** the base CV and the base cover letter for the language (paths or links in `settings.md`) into `<applications folder>/*<Company>/`, named `CV_<Name>_<lang> (<Company>) <DATE>` and `CoverLetter_<Name>_<lang> (<Company>) <DATE>`, keeping the extension.
2. **Rewrite only the mapped parts** (the "Text map" in `settings.md`: headline, summary, bullets per job, skills, recipient, body, date). Replace text inside the existing paragraphs and runs so fonts, sizes, colours and spacing stay as they are; never rebuild the document. Keep a similar length so it doesn't spill onto another page. The letter follows the same rules as section 3 (250 to 350 words, portfolio as the only link).
   - **Word (.docx)**: edit the copy with a docx library (e.g. python-docx), changing the text of runs, not the styles. If the agent has a Word skill, use it.
   - **Google Docs**: copy the base Doc with the Google Drive MCP (or ask the user to make a copy and share the link), then edit the copy's text. Docs stay in Drive; the folder gets the PDFs.
   - **Pages**: agents can't edit `.pages` files reliably. On a Mac with a shell, script Pages (AppleScript / `osascript`) to duplicate, replace text and export. Otherwise ask the user to export the base once to Word (File → Export To → Word) and use the Word flow; the PDF looks the same.
3. **Check it**: export a PDF preview (or render the first page) and look for text cut off, a second page that wasn't there, or broken bold and links. Re-score with the new text.
4. **Export PDFs after approval** (same rule as 5b), next to the copies:
   - Word: LibreOffice (`soffice --headless --convert-to pdf`), or Word itself on the user's computer.
   - Google Docs: download the copy as PDF through Drive (export as `application/pdf`).
   - Pages: export from Pages (scripted or by the user).
   If nothing can convert the file, say so and ask the user to use File → Export / Save as PDF; the copy is already in the folder.

## 6. Wrap up

- ATS coverage before → after as % (e.g. `64% → 86%`), and a short list of what changed. Only real experience counts: if a requirement is still missing, it stays missing.
- Real gaps worth preparing for the interview.
- Link to the Figma section (or the document copies, or the Markdown files) and the folder path. Ask: "Review it and tell me when to export the PDFs."
- In Notion (`application-tracker`): Status "CV ready", Figma CV (or the link to the document copy), Folder and **ATS coverage** (the after %, as a number) filled, plus the covered / partial / missing list in the card body, Next action "Review CV + cover letter and send", Next action date today + 1. Do not mark as Applied.
