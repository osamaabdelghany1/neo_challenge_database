# Issues

## #1 [bug] Links to deleted `pages/view_challenges.py` crash the app
Commit `c743132` deleted `pages/view_challenges.py`, but `home.py` (lines 30, 36), `sport-challenge.py` (line 62) and `challenge_details.py` (line 37) still `st.switch_page` to it.
Fix: restore the file from `c743132^` unchanged.
Status: closed

## #2 [bug] Exercise data is not linked to muscles, equipment filters or videos
- `exercises.muscle_id` is 1–15, but `muscles.id` is 25–39 after the muscles were re-inserted.
- `equipment_needed` values (`Barbell`, `None`, `Dumbbells`, …) don't match `workout.py` filters (`machine`, `bodyweight`, `free weights`, `cable`). As a result Bodyweight and Free Weights show nothing.
- Every `video_url` is an `https://example.com/...` placeholder, while `videos/` holds 60 real clips.
Fix: rewrite `database/insert_exercise.sql` with one exercise per file in `videos/`, resolve `muscle_id` by muscle name with a subselect, use the four filter values for equipment, and set `video_url` to `videos/<file>.mp4`. Then reseed `database/database.db`.
Status: closed

## #3 [feature] General Knowledge quiz
The `questions` table holds 60 questions (10 Easy / 20 Medium / 30 Hard) that no page reads.
Fix: add a quiz page where the user picks a level, answers the questions and sees a score. Link it from the home page's General Knowledge button and from `challenge_details.py` for General Knowledge challenges.
Status: closed

## #4 [feature] Joining a challenge saves to `user_challenges`
"Start Challenge" in `challenge_details.py` only shows balloons; `userId` (set in `login.py`) is never used.
Fix: if logged in, insert `(userId, challenge_id)` once and show "Joined"; if not, prompt the user to log in.
Status: closed

## #5 [refactor] Finishing cleanup
- `app.py` is fully commented out, so the app opens on a blank page. Make it open `pages/home.py`.
- Add `requirements.txt` (streamlit) for Streamlit Community Cloud.
- Remove the SSN field from `sign_up.py`. The column stays in the schema; insert NULL.
- Discard the blank-line-only diff in `pages/challenge_details.py`.
Status: closed

## #7 [refactor] Remove committed __pycache__ files
37 compiled `.pyc` files were tracked in git. They are deleted (staged) and `__pycache__/` is added to `.gitignore`.
Status: closed

## #8 [bug] Sports challenges have no activities; 30 activities are orphaned
Commit `ff4792a` deleted challenges 11 and 13-16, but their 30 activities (challenge_id 11, 13-16) remain. Sports challenges 1-8 have zero activities, so Sports challenge details show "No activities found" and the sport-challenge level filter finds nothing.
Status: closed (Sports challenges intentionally left without activities)

## #6 [docs] Marketing and competition materials (English)
- Fill in `docs/afro_asian_software_template.md`, sections 1–9.
- Pitch slide deck (Artifact).
- Poster plus social posts (Artifact).
Depends on #1–#5 for screenshots.
Status: closed (doc in docs/neo_challenge_documentation.md; pitch deck and poster/social posts published as Artifacts)

## #9 [ui] Sidebar lists every page file; exercise detail shows a muscle id
The sidebar lists `app`, the create pages and the detail pages. Fix: `app.py` becomes an `st.navigation` router with sections, and the detail pages are registered with `visibility="hidden"`. Also, `_exercise_details.py` shows "Muscle ID 30" instead of the muscle's name.
Status: closed

## #10 [docs] Home page "How It Works" promises features that don't exist
`pages/home.py` says "Three new challenges every day", "Track your progress" and "Challenges adapt as you grow stronger". None of these exist yet. Fix: reword the box to describe what the app actually does.
Status: closed

## #11 [refactor] Kid-simple rebuild and database redesign
Make the code readable top to bottom by a 12-year-old, and fix the database design.
- `app.py` creates the tables from `database/schema.sql` and seeds an empty database. It builds a menu that shows only what the current user can open, and the first sign-up becomes admin.
- New schema:
  - foreign keys enforced with `ON DELETE CASCADE`
  - `CHECK` rules on every fixed-choice column
  - live activity counts (`number_of_levels` and `number_of_activities` dropped)
  - `activities.category` dropped
  - `PRIMARY KEY` on `user_challenges`
  - snake_case names and `id` first in every table
  - seed files link to their parents by name
- Pages:
  - read rows by column name
  - no custom CSS (colours come from `.streamlit/config.toml`)
  - no `try`/`except`
  - Create forms use dropdowns
- Dropped: Sports by level and the fitness calculator, the Activities list, Activity details, Nutrition plan details, Muscle details, the fake balloon buttons and the seed users.
- Added: My challenges, Log out, and "Choose this plan" (saved to `user_nutrition_plans`).
- `database/database.db` is no longer in git.
- Trade-offs are listed under Limits in `README.md`.
Status: closed

## #12 [bug] First request after a server start could skip the menu
Screens lived in a folder named `pages/`, which Streamlit lists by itself. If the very first request after the server started was a direct link (for example `/view_users`), Streamlit ran that file without `app.py`. That skipped setting up the database and hiding the admin pages.
Fix: rename the folder to `app_pages/` and update every path. A direct link now always goes through `app.py`'s menu.
Status: closed

## #13 [refactor] Repo cleanup
- Remove the unused images `OIP.webp`, `American.png`, `Bretish.png` and `logo.svg`.
- Stop tracking the `.claude/` and `.agents/` skill symlinks; they point into a local Python install.
- The seed now has 7 challenges (3 Sports); the docs, the screenshot and the deck are updated to match.
Status: closed

## #14 [ui] Image and video sizes
Every picture and video was drawn at full width:
- The flag on a challenge page was stretched to about 980px and looked blurry.
- The exercise video filled the whole screen.
- The muscle pictures had 6 different shapes, so cards didn't line up.
- Workout was a long 2-column page.
Fix:
- Exercise page: video on the left and facts on the right, in two columns (3:2).
- Challenge picture: capped at 400px wide.
- Muscle pictures: cropped once to 4:3.
- Workout: all 4 cards in one row.
The videos turned out to be tall phone recordings, so the video gets the narrow column (1:2) and fits on one screen.
Also fixed: after "Start challenge", the button stayed on screen under the success message. The page now reloads after joining and shows the balloons once.
Status: closed

## #15 [ui] Better quiz and exercises pages; one button style
Buttons came in two looks (filled teal for the one main action, almost white for everything else), which read as random. The quiz was one long form. The exercises page was 60 text-only cards with one dropdown.
Fix:
- Buttons: every button is filled teal and full width.
- Quiz:
  - one question at a time, with level pills and a progress bar
  - 4 answer buttons, then instant ✅/❌ and Next
  - at the end: score, review and Play again
- Exercises:
  - square picture cards, 4 per row
  - pills for equipment and level, plus a muscle dropdown
  - new `exercises.thumbnail_url` column with 60 frames taken from the videos
Status: closed

## #16 [feature] Progress tracking and Sports activities
- **Activities:** on a challenge you joined, tick each activity Done. The page shows "X of N done" and balloons when all are done.
- **Exercises:** an "I did this today" button on the video page, once per day per exercise.
- **Quiz:** every finished round is saved for logged-in users.
- **My challenges:** becomes a dashboard with the challenge progress bars, workouts this week, the last 5 exercises, the best quiz score per level, the last 5 quiz rounds and your nutrition plan.
- **Sports activities:** 18 new activities for the 3 Sports challenges; the 12 workout ones link to a video exercise (new `activities.exercise_id` column).
- **New tables:** `user_activities`, `exercise_logs`, `quiz_results`.
Status: closed
