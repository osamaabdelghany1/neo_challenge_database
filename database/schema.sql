CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,                  -- plain text, see "Limits" in README.md
    birth_date TEXT NOT NULL,
    height REAL,                             -- centimetres
    weight REAL,                             -- kilograms
    phone TEXT,
    ssn TEXT,                                -- kept for later, no screen uses it
    is_admin INTEGER NOT NULL DEFAULT 0,     -- 1 means admin, 0 means normal user
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS challenges (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    category TEXT NOT NULL CHECK (category IN ('Sports', 'Language', 'General Knowledge')),
    duration INTEGER NOT NULL,               -- days
    description TEXT NOT NULL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS activities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    challenge_id INTEGER NOT NULL REFERENCES challenges(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    difficulty TEXT NOT NULL CHECK (difficulty IN ('Easy', 'Medium', 'Hard')),
    -- The video exercise this activity uses, if any. If that exercise is deleted, the link is cleared.
    exercise_id INTEGER REFERENCES exercises(id) ON DELETE SET NULL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    challenge_id INTEGER NOT NULL REFERENCES challenges(id) ON DELETE CASCADE,
    question TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    correct_answer TEXT NOT NULL CHECK (correct_answer IN ('A', 'B', 'C', 'D')),
    level TEXT NOT NULL CHECK (level IN ('Easy', 'Medium', 'Hard')),
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- Which user joined which challenge.
-- The PRIMARY KEY stops the same user joining the same challenge twice.
CREATE TABLE IF NOT EXISTS user_challenges (
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    challenge_id INTEGER NOT NULL REFERENCES challenges(id) ON DELETE CASCADE,
    PRIMARY KEY (user_id, challenge_id)
);

CREATE TABLE IF NOT EXISTS nutrition_plans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bmi REAL NOT NULL,
    category TEXT NOT NULL CHECK (category IN ('Underweight', 'Normal', 'Overweight', 'Obese')),
    goal TEXT NOT NULL CHECK (goal IN ('Lose Weight', 'Gain Weight', 'Maintain Weight', 'Build Muscle')),
    calories INTEGER NOT NULL,
    breakfast TEXT NOT NULL,
    lunch TEXT NOT NULL,
    dinner TEXT NOT NULL,
    water_intake TEXT NOT NULL,              -- for example "2.5 Liters"
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- The nutrition plan each user chose.
-- user_id is the PRIMARY KEY, so every user has at most one plan.
CREATE TABLE IF NOT EXISTS user_nutrition_plans (
    user_id INTEGER PRIMARY KEY REFERENCES users(id) ON DELETE CASCADE,
    nutrition_plan_id INTEGER NOT NULL REFERENCES nutrition_plans(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS muscles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    latin_name TEXT,
    description TEXT NOT NULL,
    muscle_group TEXT NOT NULL CHECK (muscle_group IN ('Upper Body', 'Core', 'Lower Body')),
    location TEXT NOT NULL,
    function TEXT NOT NULL,
    origin TEXT,
    insertion TEXT,
    muscle_type TEXT,
    difficulty_to_train TEXT CHECK (difficulty_to_train IN ('Easy', 'Medium', 'Hard')),
    image_url TEXT,                          -- a path like "assets/chest.jpg"
    video_url TEXT,                          -- kept for later, no screen uses it
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT DEFAULT CURRENT_TIMESTAMP -- kept for later, nothing updates it
);

CREATE TABLE IF NOT EXISTS exercises (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    muscle_id INTEGER NOT NULL REFERENCES muscles(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    description TEXT,
    equipment TEXT NOT NULL CHECK (equipment IN ('Machine', 'Bodyweight', 'Free Weights', 'Cable')),
    difficulty TEXT NOT NULL CHECK (difficulty IN ('Easy', 'Medium', 'Hard')),
    video_url TEXT,                          -- a path like "videos/pushups.mp4"
    thumbnail_url TEXT                       -- a still picture from the video, like "assets/thumbnails/pushups.jpg"
);

-- Progress: which activities each user has ticked Done.
CREATE TABLE IF NOT EXISTS user_activities (
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    activity_id INTEGER NOT NULL REFERENCES activities(id) ON DELETE CASCADE,
    done_at TEXT DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, activity_id)
);

-- Progress: the exercises each user did, at most once per exercise per day.
CREATE TABLE IF NOT EXISTS exercise_logs (
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    exercise_id INTEGER NOT NULL REFERENCES exercises(id) ON DELETE CASCADE,
    done_on TEXT NOT NULL,                   -- a date like "2026-10-07"
    PRIMARY KEY (user_id, exercise_id, done_on)
);

-- Progress: every quiz round a logged-in user finished.
CREATE TABLE IF NOT EXISTS quiz_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    level TEXT NOT NULL CHECK (level IN ('Easy', 'Medium', 'Hard')),
    score INTEGER NOT NULL,
    total INTEGER NOT NULL,
    played_at TEXT DEFAULT CURRENT_TIMESTAMP
);
