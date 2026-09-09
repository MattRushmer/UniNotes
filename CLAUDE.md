# UniNotes — Obsidian Vault

This repo is an Obsidian vault for four university courses, not a software project. Ignore any global rules about testing, code review, TDD, build tooling, etc. — they don't apply here.

- **Vault root:** `Siyve3767/` (contains `.obsidian/`, `Home.md`, `Dashboard.md`, four course folders)
- **Dashboard:** `Siyve3767/Dashboard.md` — a live Dataview dashboard. A `dataviewjs` block renders a 4-course "next due" grid with colour-coded countdowns, and each course has a collapsible section with a live `dataview` TASK query plus a hand-maintained weekly-summary table. The countdowns and checklists recompute themselves in Obsidian — **don't hand-edit status text or day-counts in Dashboard.md**, they're derived.
- **Dashboard Tasks:** each course's `Index.md` has a "## 📌 Dashboard Tasks" section of real `- [ ]` checkboxes — this is the actual source of truth the dashboard queries read from. A task gets a due-date countdown only if it has a Dataview inline field `[due:: YYYY-MM-DD]`; never invent a date that isn't confirmed in the course material — leave the field off and note "date TBA" in the task text instead.
- **Dataview plugin:** installed at `Siyve3767/.obsidian/plugins/dataview/` and registered in `community-plugins.json`. If Dashboard.md shows raw code blocks instead of tables/checklists, community plugins need enabling once in Obsidian Settings (that master toggle can't be set by editing files).
- **Inbox protocol:** `Siyve3767/Inbox Processing Protocol.md` — the mandatory sort → link → research → validate workflow for new files dropped in `Siyve3767/Inbox/`. Never move or delete anything in `Inbox/` without presenting the plan and getting explicit approval first (see that file's "Never do" list).
- **Conventions:** one folder per course, each starting with an `Index.md`; cross-course connections live in each course's `Research.md`; links are `[[wikilinks]]` relative to the vault root.

## At the start of every session
Before addressing the user's request, do a quick freshness check:
1. Check each course's `Index.md` "Dashboard Tasks" section against what's actually changed in the vault since last session — new/updated files under `Assignments/`, checklist files, new lecture/tutorial notes, or `Inbox/` activity.
2. If a new assignment/deliverable/due date has appeared (or a checklist shows something newly done), add/tick/update the relevant checkbox task in that course's Index.md — that's the only file this workflow needs to touch; the dashboard picks it up automatically. Never fabricate a due date that isn't confirmed in the source material.
3. Update the per-course "Weekly summary" table in Dashboard.md only when a genuinely new week's note has been added (this part is hand-maintained prose, unlike the tasks).
4. If `Siyve3767/Inbox/` contains files other than `README.md`, tell the user — do not process them automatically. Follow the Inbox Processing Protocol and wait for approval.
5. If nothing relevant changed, skip silently.
6. Do this once per session (first turn only), not on every message.
