# Makes the mp3 that reads each language sentence aloud.
# The app never runs this. Run it yourself from the repo root, once after you add or change a sentence:
#
#     pip install gTTS==2.5.4      (only for this script, not for the app)
#     python3 tools/make_audio.py
#
# It needs internet, because gTTS asks Google to speak the sentence.
# It only makes the files that are missing, so delete an mp3 first if you changed its sentence.
import os
import sqlite3
import sys

from gtts import gTTS

# We run from the repo root, so tell Python to look there for the assets folder too.
sys.path.append(os.getcwd())
from assets.config import DATABASE_PATH, LANGUAGE_CODES

# The folder where all the clips live.
AUDIO_FOLDER = "audio"

conn = sqlite3.connect(DATABASE_PATH)
conn.execute("PRAGMA foreign_keys = ON")
conn.row_factory = sqlite3.Row
activities = conn.execute("""
    select activities.description, activities.audio_url, challenges.name as challenge_name
    from activities join challenges on challenges.id = activities.challenge_id
    where activities.audio_url is not null
""").fetchall()
conn.close()

if not os.path.exists(AUDIO_FOLDER):
    os.mkdir(AUDIO_FOLDER)

for activity in activities:
    path = activity["audio_url"]
    # An empty file is left behind when the internet drops halfway, so we make that one again.
    if os.path.exists(path) and os.path.getsize(path) > 0:
        print("skip", path)
        continue

    # Find the voice from the language in the challenge name, e.g. "French Conversation Challenge" -> "fr".
    code = None
    for language in LANGUAGE_CODES:
        if language in activity["challenge_name"]:
            code = LANGUAGE_CODES[language]
    if code is None:
        print("no language found for", activity["challenge_name"], "so skipping", path)
        continue

    gTTS(text=activity["description"], lang=code).save(path)
    print("made", path)
