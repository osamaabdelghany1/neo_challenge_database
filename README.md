# NEO Challenge

One app, three daily habits: train your body, grow your languages, sharpen your mind.

NEO Challenge is a small web app for students aged 12–18. You can:

- browse **challenges** (Sports, Language, General Knowledge) and join the ones you like,
- learn **English, French or German** with activities from Easy to Hard,
- play a **general knowledge quiz**: 10 random questions, one at a time, with right or wrong straight away,
- find a **workout** for the equipment you have and watch a **video** for each of the 60 exercises,
- read about the **muscles** you train,
- pick a **nutrition plan** for your BMI category,
- tick off activities, log the exercises you did and keep your quiz scores, then see your progress on **My challenges**.

An admin can also see the users and add new challenges, activities, exercises, muscles and nutrition plans.

## How it works, in plain words

- The app is written in **Python** with **Streamlit**, which turns Python scripts into web pages.
- All the content lives in one **SQLite** database file, `database/database.db`.
- When the app starts, `app.py` creates the tables from `database/schema.sql`.
  If the database is empty, it fills it with our starting content from the `database/insert_*.sql` files.
- `app.py` also builds the menu. The menu only shows what you can open:
  log in / sign up when you are logged out, your pages when you are logged in, and the admin pages only for the admin.
- Every screen is one file in `app_pages/`. Each screen talks to the database itself with plain SQL.
- The very first person who signs up becomes the **admin**.

```
app.py                  creates the database, builds the menu
app_pages/              one file per screen
assets/config.py        settings shared by screens (database path, pictures, level icons)
assets/*.jpg, *.png     pictures
videos/                 60 exercise videos
database/schema.sql     the tables
database/insert_*.sql   the starting content
.streamlit/config.toml  the app's colours
```

## Run it

You need Python 3.

```bash
pip install -r requirements.txt
streamlit run app.py
```

Run it from this folder (the app finds its files with paths like `database/...` and `videos/...`).
Your browser opens the app. Sign up first: the first account becomes the admin.

To start over with a fresh database, stop the app, delete `database/database.db`, and start it again.

## Deploy it

1. Push this folder to GitHub.
2. On [Streamlit Community Cloud](https://share.streamlit.io), create an app from the repository with `app.py` as the main file.
3. Open the app and sign up straight away, so you become the admin.

The database file lives on the server, so it starts empty (with the starting content) every time the server restarts.

## Limits

We kept the app simple on purpose. These are the trade-offs we chose:

- **Passwords are stored as plain text.** Anyone who gets the database file can read every password. Do not reuse a real password here.
- **The first sign-up is the admin.** Whoever signs up first on a new database gets the admin pages, so sign up yourself right after deploying.
- **No error handling code.** The app checks the things a user can get wrong (empty fields, an email or name that is already used) and shows a friendly message. Anything else, such as a broken database file, shows Streamlit's own error.
- **The database resets on Streamlit Community Cloud** when the server restarts, so accounts and joins made there are not kept forever.
- **Some database columns are not used by any screen yet:** `users.ssn`, `muscles.video_url` and `muscles.updated_at`.
- **Admin forms take file paths as text.** To add an exercise video, its thumbnail picture or a muscle picture, put the file in `videos/` or `assets/` first, then type its path.
- **New database columns need a fresh database.** The app creates missing tables but never changes existing ones, so after a schema change delete `database/database.db` once (this resets accounts).
- **Progress is simple.** You can tick activities, log each exercise once a day and keep quiz scores, but there are no reminders or day-in-a-row streaks.
