"""Minimal config for Fitness Challenge App"""

# Colors
PRIMARY_DARK = "#254B62"
PRIMARY_LIGHT = "#77ABB7"

DIFFICULTY_COLORS = {"Easy": "#77ABB7", "Medium": "#476D7C", "Hard": "#1D3E53"}
CATEGORY_COLORS = {"Sports": "#77ABB7", "Language": "#254B62", "General Knowledge": "#476D7C"}

# Challenge images (by keyword in challenge name)
CHALLENGE_IMAGES = {
    "English": "assets/English.jpg",
    "French": "assets/French.png",
    "German": "assets/German.jpg",
}

# Level icons with colors
LEVEL_ICONS = {
    "Easy": {"icon": "🟢", "color": "#77ABB7"},
    "Medium": {"icon": "🟡", "color": "#476D7C"},
    "Hard": {"icon": "🔴", "color": "#1D3E53"},
}

# Database
DATABASE_PATH = "database/database.db"