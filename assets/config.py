# Settings that several screens share.

# The database file. app.py creates it the first time the app starts.
DATABASE_PATH = "database/database.db"

# The picture for each kind of challenge.
CATEGORY_IMAGES = {
    "Sports": "assets/sport_challenge.png",
    "Language": "assets/language_challenge.png",
    "General Knowledge": "assets/General-Knowledge.jpg",
}

# Language challenges get their country's flag when the language is in the challenge name.
CHALLENGE_IMAGES = {
    "English": "assets/English.jpg",
    "French": "assets/French.png",
    "German": "assets/German.jpg",
}

# A coloured dot next to each level, so you can spot it quickly.
LEVEL_ICONS = {
    "Easy": "🟢",
    "Medium": "🟡",
    "Hard": "🔴",
}
