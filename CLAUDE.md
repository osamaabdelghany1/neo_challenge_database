# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A Streamlit multi-page app ("Daily Challenge") for fitness, language and general-knowledge challenges, backed by a local SQLite file. No build step, no tests, no linter, no `requirements.txt` — the only runtime deps are `streamlit` (developed against 1.64) and the stdlib `sqlite3`.

## Commands

```bash
streamlit run app.py                                   # run the app (must be launched from repo root)
sqlite3 database/database.db < database/tables.sql     # create schema on a fresh DB
sqlite3 database/database.db < database/insert_users.sql   # seed one table (repeat per insert_*.sql)
```

The app does **not** create or migrate the database itself; `database/database.db` is committed and already seeded. To change the schema, edit `database/tables.sql`, then rebuild the DB manually with the commands above. Note `tables.sql` contains stray `select` statements and commented `drop table` lines.

## Architecture

- **Entry point**: `app.py` is entirely commented out but must stay — Streamlit uses it as the main script and auto-discovers `pages/*.py` as sibling pages. The real landing page is `pages/home.py`.
- **Every page is self-contained**: each file calls `st.set_page_config()`, loads `assets/styles.css` via a path relative to `__file__`, defines its own tiny `header()` helper, and opens its own `sqlite3.connect(DATABASE_PATH)`. There is no shared DB/helper module — duplication across pages is the established style.
- **Relative paths assume CWD = repo root**: `DATABASE_PATH = "database/database.db"` and image paths like `"assets/x.jpg"` (in pages and in `muscles.image_url`) are resolved against the working directory, not the file.
- **Config** lives in `assets/config.py` (colors, `DIFFICULTY_COLORS`, `CATEGORY_COLORS`, `CHALLENGE_IMAGES`, `LEVEL_ICONS`, `DATABASE_PATH`), imported as `from assets.config import ...`.
- **List → detail navigation via session state**: a `view_*.py` page sets an id in `st.session_state` and calls `st.switch_page("pages/<detail>.py")`; the detail page reads that id and redirects back to the list page if it's missing. Keys in use: `selected_challenge_id`, `selected_activities_id`, `selected_nutrition_plans_id`, `selected_exercise_id`, `selected_muscle_id`, `selected_level`, `selected_difficulty`, `equipment_filter`, `fitness_level_filter`, `userId`.
- **Underscore-prefixed pages** (`_create_*.py`, `_*_details.py`) are detail/create pages reached via `switch_page`. Streamlit 1.64 does not hide them from the sidebar; the prefix is only a naming convention. `st.switch_page` paths must match the file name exactly, including the underscore and existing misspellings (`_activites_details.py`, `_create_nutration_plan.py`).
- **Rows are tuples**: queries use `select *` with no `row_factory`, and pages index columns positionally (e.g. `ex[2]` for exercise name). Changing column order in `tables.sql` silently breaks pages. Note `challenges` declares `id` after other columns.
- **Domain links**: `challenges` → `activities` / `questions` (by `challenge_id`, `questions.level` ∈ Easy/Medium/Hard); `muscles` → `exercises` (by `muscle_id`; `equipment_needed` drives the `workout.py` equipment filter); `users` ↔ `challenges` / `Nutrition_Plans` via `user_challenges` and `User_Nutrition_Plans` join tables.
- **Media**: images in `assets/`, exercise videos in `videos/` (the seeded `exercises.video_url` values are still `example.com` placeholders).

## Gotchas

- Passwords are stored and compared in plaintext (`login.py` / `sign_up.py`).
- `.claude/skills/developing-with-streamlit` holds a project-local Streamlit skill — use it for Streamlit/styling work.
