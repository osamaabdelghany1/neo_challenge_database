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
Status: open

## #6 [docs] Marketing and competition materials (English)
- Fill in `docs/afro_asian_software_template.md`, sections 1–9.
- Pitch slide deck (Artifact).
- Poster plus social posts (Artifact).
Depends on #1–#5 for screenshots.
Status: open
