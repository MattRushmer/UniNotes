---
tags:
  - inbox
  - protocol
  - vault-admin
---

# Inbox Processing Protocol

> **The operating manual for sorting new files.** When the user drops files into `Inbox/` and says *"process the inbox"* (or anything similar), follow this protocol top to bottom. It exists so every AI session handles new material the same way: **sort -> link -> research -> validate**.

## Trigger
- User says "process the inbox", "sort my new files", "what's in the inbox?", or similar.
- The `Inbox/` folder lives at the **vault root** (the folder containing `.obsidian`, `Home.md`, and the 4 course folders).

---

## Step 0 — Read the lay of the land
1. List `Inbox/` contents.
2. Read this file (you're reading it).
3. Re-read the relevant course `Index.md` files so you know each course's subfolders and naming conventions.
4. Re-read `Home.md` for the vault conventions.

## Step 1 — Classify every file (NO moving yet)
For each file in `Inbox/`, determine:
- **Which course** it belongs to (see classification rules below).
- **Which subfolder** it belongs in (`Lectures/`, `Labs/`, `Tutorials/`, `Exam Prep/`, `Reference/`, `Techbooks/`, `Notes/`, `Case Studies/` — whatever that course actually uses).
- **Whether it's a source file** (slides, PDF, RIS) or **a user note** (markdown).

### Course classification rules (by filename/content)
| Pattern found in name or content | Course |
|---|---|
| `COMP504`, `Ch0x`, `Ch1x`, `Ethernet`, `VLSM`, `IPv4`, `Subnet`, `Backbone`, `LAN`, `WAN`, `TCP/IP`, `OSI`, `Network`, `Default Gateway` | **COMP504 Networks** |
| `COMP507`, `Project Management`, `PMBOK`, `WBS`, `Stakeholder`, `Risk`, `Scope`, `Quality`, `Cost`, `Schedule`, `Business Case`, `ROI`, `Northwest` | **COMP507 IT Project Management** |
| `COMP517`, `Data Analysis`, `EDA`, `Data Profiling`, `Python`, `pandas`, `Hypothesis`, `ANOVA`, `Regression`, `Correlation` | **COMP517 Data Analysis** |
| `MATH503`, `Math`, `Probability`, `Permutation`, `Combination`, `Binomial`, `Distribution`, `Statistics`, `Bayes`, `Mean`, `Median` | **MATH503 Mathematics** |

**If classification is ambiguous:** read the file's first ~20 lines of extractable text and match keywords. If it's *still* ambiguous, **ask the user** — never guess between courses.
**If it's clearly not course material** (admin, personal, general): flag it and ask the user where it should go.

### Subfolder rules
- Lecture slides (`.pptx`/`.ppt`) -> `Lectures/`
- Lab handouts/worksheets -> `Labs/` (COMP504/COMP517) or `Tutorials/` (COMP507)
- Exam/revision material -> `Exam Prep/` (if the course has one)
- Reference/extra reading -> `Reference/`
- Techbook/RIS/citation files -> `Techbooks/`
- Markdown the user wrote -> `Notes/`
- Business/industry case studies -> `Case Studies/` (COMP507)

## Step 2 — Show the plan, wait for approval (MANDATORY)
The user has explicitly chosen **show-plan-first**. Before moving anything, present a table:
`File -> Course -> Subfolder -> (Note to create/update)`
and **wait for the user to approve** (or adjust) before any `mv`/copy happens. No exceptions.

## Step 3 — Move the files
Only after approval:
- Move each file into `<Course>/<Subfolder>/` with the vault's naming convention:
  `Week NN - Topic.ext`, `ChNN - Topic.ext`, `Lab NN - Topic.ext`, or keep the user's name if it already fits.
- Never rename in a way that breaks existing `[[wikilinks]]` — check first.
- Never move `Inbox Processing Protocol.md` or anything outside `Inbox/` (that includes `Inbox/README.md` — it stays in place permanently).
- **Never delete the `Inbox/` folder itself.** After processing, leave it at the vault root with `README.md` inside so it's always visible and ready.

## Step 4 — Extract content (if it's a slide/PDF/RIS)
- **`.pptx`**: extract text with `python-pptx` (or unzip + grep `ppt/slides/slide*.xml`).
- **`.pdf`**: `pdftotext -layout` if available; if the PDF is a scanned image (no text layer), write a placeholder note and flag it for OCR — do not invent content.
- **`.ris`**: parse authors/title/year and file it under `Techbooks/`; update the course `Techbook Summary.txt` if one exists.
- Extract into a scratch file **outside the vault** (e.g. `/tmp`) if needed, then delete it after.

## Step 5 — Write/update the course note
For each new source file, create a note in `<Course>/Notes/` following the existing auto-extracted note format:
- Frontmatter: `tags:` with the course tag (`#comp504`/`#comp507`/`#comp517`/`#math503`) + topic tags already in use in that course + `lecture`/`lab` + `exam-topic` where relevant.
- Body: `# Title`, a source line `> Auto-extracted from [[<Course>/<Subfolder>/<file>|<filename>]]`, then structured bullets of the core concepts.
- **If a note for that file already exists**, update it in place — never duplicate.

## Step 6 — Link it (the "make connections" step)
1. Add `[[wikilinks]]` **at the concept mention**, not just once at the top — link to existing notes in the same course and across courses.
2. Run a **cross-course check**: does a concept in this file appear in another course's notes under a different name (e.g. binomial variance in COMP507 Quality vs MATH503 W06)? Link both ways.
3. Update the course `Index.md`: add the new file to its section and the note to the Notes section.
4. Update the course `Research.md` if the file resolves or raises an open question listed there.

## Step 7 — Research new topics (the "research" step)
For concepts in the new file that are **under-explored in the vault** (no note, or only a mention):
1. Check the vault first — if an existing note already covers it, just link it.
2. If genuinely new, do a **web search** for authoritative sources, and if it's substantial enough, propose a new note or a Research.md section update — **with the user's approval**, never silently.
3. External sources must be marked clearly (source name + URL, "external, not from vault").

## Step 8 — Validate
Run the standard link check from the vault root — every `[[wikilink]]` must resolve to a real file (allow `file.ext` variants and `#heading` anchors). Report:
- Files moved (from -> to)
- Notes created/updated
- Links added
- Tags used
- Research done / open questions flagged

---

## Known gotchas (learned the hard way)
- **Vault root vs shell folder:** the vault root is `..` relative to the workspace — ALWAYS `cd ..` before vault commands. The `Uni info/` shell folder at the workspace root is leftover and locked; don't write files there.
- **Long bash heredocs truncate.** Write long files with `write_file`, or split the heredoc into small chunks.
- **Non-ASCII characters mangle in heredocs** (superscript n, em dash, middot). Write them as `\uXXXX` escapes in Python, or keep content ASCII.
- **`write_file` may land in the wrong folder** (it writes relative to the workspace, not the vault). Always verify with `ls`/`find` after writing, and `mv` if needed.
- **Never assume a library is available** (`python-pptx`, `pdftotext`). Check with a quick command; fall back to `unzip` + grep for pptx.
- **Don't edit user markdown content** — only add links/tags (per the earlier "link-only" rule) unless the user asks for a rewrite.

## Never do
- Move files before showing the plan and getting approval.
- Delete the `Inbox/` folder or its `README.md` — they are permanent and must always exist at the vault root.
- Delete or overwrite user files.
- Invent content for unreadable (scanned) PDFs — flag them instead.
- Create new notes/hub notes without approval.
- Edit `graph.json` — Obsidian's graph updates automatically from the notes; the color groups in `.obsidian/graph.json` already cover every file inside the 4 course folders (path queries), and the `course-colors.css` snippet colors subfolders and note files automatically too. New course folders would need new color groups, but new *files* never do.
