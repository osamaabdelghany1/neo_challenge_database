# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

NEO Challenge: a Streamlit app (fitness, language and general-knowledge challenges) on one SQLite file. It is **kid-simple** on purpose: code a curious 12-year-old could read top to bottom. Keep it that way (rules below). `README.md` explains the app and lists every trade-off under **Limits**.

## Commands

```bash
pip install -r requirements.txt
streamlit run app.py          # must run from the repo root
rm database/database.db       # reset: the app recreates and reseeds it on the next start
```

No build step, tests, or linter. `requirements.txt` pins `streamlit==1.64.0`; everything else is the standard library (`sqlite3`, `datetime`).

## How it fits together

- `app.py` runs on every rerun: `create_tables()` executes `database/schema.sql` (all `CREATE TABLE IF NOT EXISTS`), and if `challenges` is empty runs the `SEED_FILES` in order. Then it builds the `st.navigation` menu from `st.session_state`: logged out → Log in / Sign up; logged in → My challenges / Log out; `is_admin` → the Admin section. Pages not in the menu cannot be opened, so admin pages need no check of their own. `challenge_details.py` and `exercise_details.py` are always registered with `visibility="hidden"`. **A new page must be added to `app.py`.** Screens must stay in `app_pages/`, never a folder named `pages/`: Streamlit auto-lists a `pages/` folder, and the first request after a server start could then open any screen without going through `app.py`.
- `app_pages/` holds one plain script per screen. Each opens its own connection with the same three lines, then writes its SQL inline:

  ```python
  conn = sqlite3.connect(DATABASE_PATH)
  conn.execute("PRAGMA foreign_keys = ON")
  conn.row_factory = sqlite3.Row
  ```

  The `PRAGMA` line is required on every connection or SQLite ignores foreign keys and `ON DELETE CASCADE`. Rows are read by column name (`row["name"]`).
- Session keys: `user_id`, `username`, `is_admin` (set by `login.py`, cleared by `logout.py`), `selected_challenge_id`, `just_joined` (shows balloons once after joining), `selected_exercise_id`, `equipment_filter` (the key of the Exercises page's selectbox, preset by `workout.py`), `quiz_level`, `quiz_questions`, `quiz_number` (which question you are on), `quiz_answers` (the letters picked so far), `quiz_just_finished` (balloons once).
- `assets/config.py`: `DATABASE_PATH`, `CATEGORY_IMAGES`, `CHALLENGE_IMAGES`, `LEVEL_ICONS`. Colours live in `.streamlit/config.toml`; there is no custom CSS.
- Paths (`database/...`, `assets/...`, `videos/...`, also stored in `exercises.video_url`, `exercises.thumbnail_url` and `muscles.image_url`) are relative to the repo root.

## Database rules

- `database/schema.sql` is the only schema. `CHECK` rules fix the allowed values: difficulty/level `Easy|Medium|Hard`; challenge category `Sports|Language|General Knowledge`; exercise equipment `Machine|Bodyweight|Free Weights|Cable`; muscle group `Upper Body|Core|Lower Body`; nutrition category and goal.
- Child rows use `ON DELETE CASCADE`. `user_challenges` has `PRIMARY KEY (user_id, challenge_id)`; `user_nutrition_plans` has `user_id` as primary key (one plan per user).
- Counts (activities per challenge) are computed with SQL, never stored.
- Seed files link to parents **by name** with a subselect, e.g. `(select id from challenges where name = 'General Knowledge Challenge')`, never by a hard-coded id. `challenges.name` and `muscles.name` are `UNIQUE` for that reason.
- `database/database.db` is not in git; the app creates it.

## Kid-simple rules (keep them)

- Plain variables and functions with verb names; loops and `if`s instead of comprehensions, decorators, classes, type hints, or generators.
- One short comment in kid words above anything a reader would ask "why?" about.
- Constants at the top of a file in CAPITALS with a comment saying why the value is what it is.
- Repetition beats abstraction when it keeps a file readable on its own (the 3 connection lines are repeated on purpose).
- Standard library first; an extra library must do something plain code can't do in about 10 lines. Pin versions you tested.
- Validate with plain `if` checks where a user can go wrong (empty fields, taken email or name) and show a friendly message. No `try`/`except`.
- UI: sentence-case labels, icons on menu items, every button is `type="primary", width="stretch"` so all buttons look the same (filled teal), hide what the current user can't use.
- Every simplification that removes safety or capability goes in README's **Limits** section.

## Project process

- `ISSUES.md` is the local issue tracker; commits close issues with `closes #N`.
- `docs/neo_challenge_documentation.md` is the competition write-up; keep it in step with the app. Its screenshots are in `docs/screenshots/`.
- `.claude/skills/developing-with-streamlit` holds a project-local Streamlit skill.
