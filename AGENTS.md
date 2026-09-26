# AGENTS.md — neo_challenge_database

## Project Overview
Streamlit-based fitness challenge management app with SQLite database. Multi-page app for challenges, activities, nutrition plans, users, exercises, muscles, language challenges, and general knowledge quizzes.

## Run Commands
```bash
streamlit run app.py
```
- Dependencies: streamlit, sqlite3
- Database: `database/database.db` (auto-created from `database/tables.sql`)
- Seed data: `database/insert_*.sql` files (run manually to populate)

## Project Structure
```
neo_challenge_database/
├── app.py                    # Entry point (commented out)
├── assets/
│   ├── config.py             # Minimal: PRIMARY_DARK, PRIMARY_LIGHT, DIFFICULTY_COLORS, CATEGORY_COLORS, DATABASE_PATH
│   ├── styles.css            # Custom CSS (loaded via simple relative path)
│   └── *.jpg/png/webp        # Static images
├── pages/                    # Streamlit pages (auto-discovered)
│   ├── home.py               # Landing page
│   ├── login.py / sign_up.py # Auth
│   ├── view_challenges.py / create_challenges.py
│   ├── view_activities.py / create_activities.py
│   ├── view_nutrition_plan.py / create_nutration_plan.py
│   ├── view_users.py
│   ├── view_exercise.py / create_exercise.py
│   ├── view_muscles.py / create_muscles.py
│   ├── challenge_details.py / nutrition_plan_details.py / activites_details.py
│   ├── language_challenge.py / english_challenge.py / american_english.py / British_english.py / french_challenge.py / german_challenge.py
│   ├── workout.py            # Equipment-based exercise browser
│   └── sport-challenge.py    # Fitness level calculator & challenge filter
└── database/
    ├── tables.sql            # Schema (users, challenges, activities, nutrition_plans, muscles, exercises, questions)
    ├── database.db           # SQLite file (populated)
    └── insert_*.sql          # Seed data
```

## Key Patterns (Ultra-Simple)
- **Page config**: `st.set_page_config()` at top
- **CSS**: `with open(css_path) as f: st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)` where `css_path = os.path.join(os.path.dirname(__file__), "..", "assets", "styles.css")`
- **Config**: `from assets.config import PRIMARY_DARK, ...` (no sys.path hack)
- **Database**: `sqlite3.connect(DATABASE_PATH)` in each page
- **Navigation**: `st.switch_page("pages/...")`
- **Session state**: `userId`, `selected_challenge_id`, `selected_activities_id`, `selected_nutrition_plans_id`, `equipment_filter`, `fitness_level_filter`, `selected_level`
- **Helpers per page**: Just `header(title, subtitle)` — 3 lines. Use `st.container(border=True)` for cards.

## Database Schema (Populated)
- `users` — 15 sample users
- `challenges` — 17 challenges (Sports: 8, Language: 9, General Knowledge: 1)
- `muscles` — 24 muscles with images
- `exercises` — 26 exercises with equipment/difficulty
- `nutrition_plans` — 15 plans (Underweight, Normal, Overweight, Obese)
- `questions` — 60 trivia questions (Easy/Medium/Hard) for General Knowledge challenge

## Common Tasks
- **Add a page**: Create `pages/new_page.py` with `st.set_page_config()`, CSS load, `header()`, then logic
- **Modify schema**: Edit `database/tables.sql`, delete `database/database.db`, rerun app
- **Seed data**: `sqlite3 database/database.db < database/insert_*.sql`
- **Theme changes**: Edit `assets/config.py` and `assets/styles.css`

## Gotchas
- `app.py` is commented out — entry point is `home.py`
- No test suite, no lint/typecheck, no requirements.txt
- Images: relative path from page files (e.g., `assets/image.jpg`)
- Detail pages `exercise_details.py` and `muscle_details.py` don't exist yet
- Passwords stored in plaintext