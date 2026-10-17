-- Each activity finds its challenge by name, so the ids SQLite picks do not matter.
-- The language activities are the students' sentences: the name is in English, the description is the same sentence in the language you learn. Its mp3 in audio/ reads the description aloud.

-- English, Easy
INSERT INTO activities (name, description, difficulty, challenge_id, audio_url) VALUES
('I am someone who studies', 'I am a student', 'Easy', (select id from challenges where name = 'English for Beginners Challenge'), 'audio/english_easy_01.mp3'),
('People call me Adam', 'My name is Adam', 'Easy', (select id from challenges where name = 'English for Beginners Challenge'), 'audio/english_easy_02.mp3'),
('Egypt is the country where I live', 'I live in Egypt', 'Easy', (select id from challenges where name = 'English for Beginners Challenge'), 'audio/english_easy_03.mp3'),
('She enjoys eating apples', 'She likes apples', 'Easy', (select id from challenges where name = 'English for Beginners Challenge'), 'audio/english_easy_04.mp3'),
('He plays the sport of football', 'He plays football', 'Easy', (select id from challenges where name = 'English for Beginners Challenge'), 'audio/english_easy_05.mp3'),
('Our house is large', 'We have a big house', 'Easy', (select id from challenges where name = 'English for Beginners Challenge'), 'audio/english_easy_06.mp3'),
('They are people who are friends with me', 'They are my friends', 'Easy', (select id from challenges where name = 'English for Beginners Challenge'), 'audio/english_easy_07.mp3'),
('I attend school each day', 'I go to school every day', 'Easy', (select id from challenges where name = 'English for Beginners Challenge'), 'audio/english_easy_08.mp3'),
('My mother prepares the evening meal', 'My mother cooks dinner', 'Easy', (select id from challenges where name = 'English for Beginners Challenge'), 'audio/english_easy_09.mp3'),
('The weather is pleasant today', 'The weather is nice today', 'Easy', (select id from challenges where name = 'English for Beginners Challenge'), 'audio/english_easy_10.mp3');

-- English, Medium
INSERT INTO activities (name, description, difficulty, challenge_id, audio_url) VALUES
('I normally get up early because I need to attend school', 'I usually wake up early', 'Medium', (select id from challenges where name = 'English for Beginners Challenge'), 'audio/english_medium_01.mp3'),
('My sister is watching television at the same time that I am studying', 'My sister is watching TV', 'Medium', (select id from challenges where name = 'English for Beginners Challenge'), 'audio/english_medium_02.mp3'),
('Yesterday, we visited the supermarket and purchased fruit', 'We went to the supermarket', 'Medium', (select id from challenges where name = 'English for Beginners Challenge'), 'audio/english_medium_03.mp3'),
('I started living here five years ago and still live here', 'I have lived in this city', 'Medium', (select id from challenges where name = 'English for Beginners Challenge'), 'audio/english_medium_04.mp3'),
('She stayed home because she wasn''t feeling well', 'She didn''t come to school', 'Medium', (select id from challenges where name = 'English for Beginners Challenge'), 'audio/english_medium_05.mp3'),
('We will go to the beach if tomorrow''s weather is good', 'If the weather is good', 'Medium', (select id from challenges where name = 'English for Beginners Challenge'), 'audio/english_medium_06.mp3'),
('My father was at work at the time I called him', 'My father was working', 'Medium', (select id from challenges where name = 'English for Beginners Challenge'), 'audio/english_medium_07.mp3'),
('He wants to study German because he intends to visit Germany', 'He wants to learn German', 'Medium', (select id from challenges where name = 'English for Beginners Challenge'), 'audio/english_medium_08.mp3'),
('The test was hard, but I was able to answer most questions', 'Although the test was difficult', 'Medium', (select id from challenges where name = 'English for Beginners Challenge'), 'audio/english_medium_09.mp3'),
('I have not been to France before, but I want to visit it someday', 'I have never visited France', 'Medium', (select id from challenges where name = 'English for Beginners Challenge'), 'audio/english_medium_10.mp3');

-- English, Hard
INSERT INTO activities (name, description, difficulty, challenge_id, audio_url) VALUES
('I didn''t know about the problem earlier, so I didn''t try to help you', 'If I had known earlier', 'Hard', (select id from challenges where name = 'English for Beginners Challenge'), 'audio/english_hard_01.mp3'),
('She finished her homework first, and then her friends arrived', 'She had already finished', 'Hard', (select id from challenges where name = 'English for Beginners Challenge'), 'audio/english_hard_02.mp3'),
('He was very tired, but he continued working until midnight', 'Despite being extremely tired', 'Hard', (select id from challenges where name = 'English for Beginners Challenge'), 'audio/english_hard_03.mp3'),
('If I were you, I would carefully consider the decision', 'If I were in your position', 'Hard', (select id from challenges where name = 'English for Beginners Challenge'), 'audio/english_hard_04.mp3'),
('The teacher repeated the explanation because some students didn''t understand', 'The teacher explained again', 'Hard', (select id from challenges where name = 'English for Beginners Challenge'), 'audio/english_hard_05.mp3'),
('We arrived too late because the train had left before we got there', 'By the time we arrived', 'Hard', (select id from challenges where name = 'English for Beginners Challenge'), 'audio/english_hard_06.mp3'),
('She studied English for three years before moving to London', 'She had been studying English', 'Hard', (select id from challenges where name = 'English for Beginners Challenge'), 'audio/english_hard_07.mp3'),
('He had never traveled to another country, but he decided to study in Germany', 'Although he had never traveled', 'Hard', (select id from challenges where name = 'English for Beginners Challenge'), 'audio/english_hard_08.mp3'),
('They made many mistakes because they did not follow the instructions carefully', 'If they had followed instructions', 'Hard', (select id from challenges where name = 'English for Beginners Challenge'), 'audio/english_hard_09.mp3'),
('The book is old, but its ideas are still useful and important today', 'The book contains ideas', 'Hard', (select id from challenges where name = 'English for Beginners Challenge'), 'audio/english_hard_10.mp3');

-- French, Easy
INSERT INTO activities (name, description, difficulty, challenge_id, audio_url) VALUES
('I am a student', 'Je suis étudiant', 'Easy', (select id from challenges where name = 'French Conversation Challenge'), 'audio/french_easy_01.mp3'),
('My name is Adam', 'Je m''appelle Adam', 'Easy', (select id from challenges where name = 'French Conversation Challenge'), 'audio/french_easy_02.mp3'),
('I live in Egypt', 'J''habite en Égypte', 'Easy', (select id from challenges where name = 'French Conversation Challenge'), 'audio/french_easy_03.mp3'),
('She likes apples', 'Elle aime les pommes', 'Easy', (select id from challenges where name = 'French Conversation Challenge'), 'audio/french_easy_04.mp3'),
('He plays football', 'Il joue au football', 'Easy', (select id from challenges where name = 'French Conversation Challenge'), 'audio/french_easy_05.mp3'),
('We have a big house', 'Nous avons une grande maison', 'Easy', (select id from challenges where name = 'French Conversation Challenge'), 'audio/french_easy_06.mp3'),
('They are my friends', 'Ce sont mes amis', 'Easy', (select id from challenges where name = 'French Conversation Challenge'), 'audio/french_easy_07.mp3'),
('I go to school every day', 'Je vais à l''école tous les jours', 'Easy', (select id from challenges where name = 'French Conversation Challenge'), 'audio/french_easy_08.mp3'),
('My mother prepares dinner', 'Ma mère prépare le dîner', 'Easy', (select id from challenges where name = 'French Conversation Challenge'), 'audio/french_easy_09.mp3'),
('The weather is nice today', 'Il fait beau aujourd''hui', 'Easy', (select id from challenges where name = 'French Conversation Challenge'), 'audio/french_easy_10.mp3');

-- French, Medium
INSERT INTO activities (name, description, difficulty, challenge_id, audio_url) VALUES
('I usually wake up early because I have to go to school', 'Je me réveille tôt', 'Medium', (select id from challenges where name = 'French Conversation Challenge'), 'audio/french_medium_01.mp3'),
('My sister watches TV while I do my homework', 'Ma sœur regarde la télé', 'Medium', (select id from challenges where name = 'French Conversation Challenge'), 'audio/french_medium_02.mp3'),
('We went to the supermarket yesterday and bought fruit', 'Nous sommes allés au supermarché', 'Medium', (select id from challenges where name = 'French Conversation Challenge'), 'audio/french_medium_03.mp3'),
('I have lived in this city for five years', 'J''habite depuis cinq ans', 'Medium', (select id from challenges where name = 'French Conversation Challenge'), 'audio/french_medium_04.mp3'),
('She didn''t come to school because she wasn''t feeling well', 'Elle n''est pas venue à l''école', 'Medium', (select id from challenges where name = 'French Conversation Challenge'), 'audio/french_medium_05.mp3'),
('If the weather is nice tomorrow, we will go to the beach', 'S''il fait beau demain', 'Medium', (select id from challenges where name = 'French Conversation Challenge'), 'audio/french_medium_06.mp3'),
('My father was working when I called him', 'Mon père travaillait', 'Medium', (select id from challenges where name = 'French Conversation Challenge'), 'audio/french_medium_07.mp3'),
('He wants to learn German because he plans to travel to Germany', 'Il veut apprendre l''allemand', 'Medium', (select id from challenges where name = 'French Conversation Challenge'), 'audio/french_medium_08.mp3'),
('Although the exam was difficult, I managed to answer most of the questions', 'Bien que l''examen ait été difficile', 'Medium', (select id from challenges where name = 'French Conversation Challenge'), 'audio/french_medium_09.mp3'),
('I have never been to France, but I would like to go there one day', 'Je ne suis jamais allé en France', 'Medium', (select id from challenges where name = 'French Conversation Challenge'), 'audio/french_medium_10.mp3');

-- French, Hard
INSERT INTO activities (name, description, difficulty, challenge_id, audio_url) VALUES
('If I had known about the problem earlier, I would have tried to help you', 'Si j''avais été informé', 'Hard', (select id from challenges where name = 'French Conversation Challenge'), 'audio/french_hard_01.mp3'),
('She had already finished her homework before her friends arrived', 'Elle avait déjà terminé', 'Hard', (select id from challenges where name = 'French Conversation Challenge'), 'audio/french_hard_02.mp3'),
('Although he was extremely tired, he continued working until midnight', 'Bien qu''il soit fatigué', 'Hard', (select id from challenges where name = 'French Conversation Challenge'), 'audio/french_hard_03.mp3'),
('If I were in your position, I would think carefully before making such an important decision', 'Si j''étais à ta place', 'Hard', (select id from challenges where name = 'French Conversation Challenge'), 'audio/french_hard_04.mp3'),
('The teacher explained the lesson again because several students had not understood it', 'Le professeur a expliqué encore', 'Hard', (select id from challenges where name = 'French Conversation Challenge'), 'audio/french_hard_05.mp3'),
('When we arrived at the station, the train was already departed', 'Lorsque nous sommes arrivés', 'Hard', (select id from challenges where name = 'French Conversation Challenge'), 'audio/french_hard_06.mp3'),
('She said that she had been learning English for three years before moving to London', 'Elle apprenait l''anglais', 'Hard', (select id from challenges where name = 'French Conversation Challenge'), 'audio/french_hard_07.mp3'),
('Although he had never traveled abroad before, he decided to study in Germany for six months', 'Bien qu''il n''ait jamais voyagé', 'Hard', (select id from challenges where name = 'French Conversation Challenge'), 'audio/french_hard_08.mp3'),
('If they had followed the instructions carefully, they wouldn''t have made so many mistakes', 'S''ils avaient suivi les instructions', 'Hard', (select id from challenges where name = 'French Conversation Challenge'), 'audio/french_hard_09.mp3'),
('The book, which was written several decades ago, contains ideas that are still relevant today', 'Le livre contient des idées', 'Hard', (select id from challenges where name = 'French Conversation Challenge'), 'audio/french_hard_10.mp3');

-- German, Easy
INSERT INTO activities (name, description, difficulty, challenge_id, audio_url) VALUES
('I am a student', 'Ich bin Schüler', 'Easy', (select id from challenges where name = 'German For Beginner Challenge'), 'audio/german_easy_01.mp3'),
('My name is Adam', 'Ich heiße Adam', 'Easy', (select id from challenges where name = 'German For Beginner Challenge'), 'audio/german_easy_02.mp3'),
('I live in Egypt', 'Ich wohne in Ägypten', 'Easy', (select id from challenges where name = 'German For Beginner Challenge'), 'audio/german_easy_03.mp3'),
('She likes apples', 'Sie mag Äpfel', 'Easy', (select id from challenges where name = 'German For Beginner Challenge'), 'audio/german_easy_04.mp3'),
('He plays football', 'Er spielt Fußball', 'Easy', (select id from challenges where name = 'German For Beginner Challenge'), 'audio/german_easy_05.mp3'),
('We have a big house', 'Wir haben ein großes Haus', 'Easy', (select id from challenges where name = 'German For Beginner Challenge'), 'audio/german_easy_06.mp3'),
('They are my friends', 'Sie sind meine Freunde', 'Easy', (select id from challenges where name = 'German For Beginner Challenge'), 'audio/german_easy_07.mp3'),
('I go to school every day', 'Ich gehe jeden Tag zur Schule', 'Easy', (select id from challenges where name = 'German For Beginner Challenge'), 'audio/german_easy_08.mp3'),
('My mother cooks dinner', 'Meine Mutter kocht das Abendessen', 'Easy', (select id from challenges where name = 'German For Beginner Challenge'), 'audio/german_easy_09.mp3'),
('The weather is nice today', 'Das Wetter ist heute schön', 'Easy', (select id from challenges where name = 'German For Beginner Challenge'), 'audio/german_easy_10.mp3');

-- German, Medium
INSERT INTO activities (name, description, difficulty, challenge_id, audio_url) VALUES
('I usually wake up early because I have to go to school', 'Ich stehe früh auf', 'Medium', (select id from challenges where name = 'German For Beginner Challenge'), 'audio/german_medium_01.mp3'),
('My sister is watching TV while I do my homework', 'Meine Schwester sieht fern', 'Medium', (select id from challenges where name = 'German For Beginner Challenge'), 'audio/german_medium_02.mp3'),
('We went to the supermarket yesterday and bought fruit', 'Wir sind zum Supermarkt gegangen', 'Medium', (select id from challenges where name = 'German For Beginner Challenge'), 'audio/german_medium_03.mp3'),
('I have lived in this city for five years', 'Ich wohne seit fünf Jahren', 'Medium', (select id from challenges where name = 'German For Beginner Challenge'), 'audio/german_medium_04.mp3'),
('She didn''t come to school because she felt sick', 'Sie ist nicht zur Schule gekommen', 'Medium', (select id from challenges where name = 'German For Beginner Challenge'), 'audio/german_medium_05.mp3'),
('If the weather is good tomorrow, we will go to the beach', 'Wenn das Wetter morgen gut ist', 'Medium', (select id from challenges where name = 'German For Beginner Challenge'), 'audio/german_medium_06.mp3'),
('My father was working when I called him', 'Mein Vater hat gearbeitet', 'Medium', (select id from challenges where name = 'German For Beginner Challenge'), 'audio/german_medium_07.mp3'),
('He wants to learn German because he wants to travel to Germany', 'Er möchte Deutsch lernen', 'Medium', (select id from challenges where name = 'German For Beginner Challenge'), 'audio/german_medium_08.mp3'),
('Although the exam was difficult, I could answer most of the questions', 'Obwohl die Prüfung schwierig war', 'Medium', (select id from challenges where name = 'German For Beginner Challenge'), 'audio/german_medium_09.mp3'),
('I have never been to France, but I want to travel there one day', 'Ich war noch nie in Frankreich', 'Medium', (select id from challenges where name = 'German For Beginner Challenge'), 'audio/german_medium_10.mp3');

-- German, Hard
INSERT INTO activities (name, description, difficulty, challenge_id, audio_url) VALUES
('If I had known about the problem earlier, I would have tried to help you', 'Wenn ich früher gewusst hätte', 'Hard', (select id from challenges where name = 'German For Beginner Challenge'), 'audio/german_hard_01.mp3'),
('She had already done her homework before her friends arrived', 'Sie hatte bereits gemacht', 'Hard', (select id from challenges where name = 'German For Beginner Challenge'), 'audio/german_hard_02.mp3'),
('Although he was very tired, he continued working until midnight', 'Obwohl er sehr müde war', 'Hard', (select id from challenges where name = 'German For Beginner Challenge'), 'audio/german_hard_03.mp3'),
('If I were in your position, I would think carefully before making such an important decision', 'Wenn ich an deiner Stelle wäre', 'Hard', (select id from challenges where name = 'German For Beginner Challenge'), 'audio/german_hard_04.mp3'),
('The teacher explained the lesson again because several students had not understood it', 'Der Lehrer erklärte noch einmal', 'Hard', (select id from challenges where name = 'German For Beginner Challenge'), 'audio/german_hard_05.mp3'),
('When we arrived at the station, the train had already left', 'Als wir am Bahnhof ankamen', 'Hard', (select id from challenges where name = 'German For Beginner Challenge'), 'audio/german_hard_06.mp3'),
('She said that she had studied English for three years before she moved to London', 'Sie hatte Englisch gelernt', 'Hard', (select id from challenges where name = 'German For Beginner Challenge'), 'audio/german_hard_07.mp3'),
('Although he had never traveled abroad, he decided to study in Germany for six months', 'Obwohl er nie ins Ausland gereist war', 'Hard', (select id from challenges where name = 'German For Beginner Challenge'), 'audio/german_hard_08.mp3'),
('If they had followed the instructions carefully, they wouldn''t have made so many mistakes', 'Wenn sie die Anweisungen befolgt hätten', 'Hard', (select id from challenges where name = 'German For Beginner Challenge'), 'audio/german_hard_09.mp3'),
('The book, which was written several decades ago, contains ideas that are still relevant today', 'Das Buch enthält Ideen', 'Hard', (select id from challenges where name = 'German For Beginner Challenge'), 'audio/german_hard_10.mp3');

-- Sports activities. Most link to one of our video exercises by its name.
INSERT INTO activities (name, description, difficulty, challenge_id, exercise_id) VALUES
('Machine Chest Press', '3 sets of 12', 'Easy', (select id from challenges where name = 'Strength & Muscle Building Challenge'), (select id from exercises where name = 'Machine Chest Press')),
('Lat Pulldown', '3 sets of 12', 'Easy', (select id from challenges where name = 'Strength & Muscle Building Challenge'), (select id from exercises where name = 'Lat Pulldown')),
('Dumbbell Shoulder Press', '3 sets of 10', 'Medium', (select id from challenges where name = 'Strength & Muscle Building Challenge'), (select id from exercises where name = 'Dumbbell Shoulder Press')),
('Hack Squat', '3 sets of 10', 'Medium', (select id from challenges where name = 'Strength & Muscle Building Challenge'), (select id from exercises where name = 'Hack Squat')),
('Weighted Dips', '3 sets of 8', 'Hard', (select id from challenges where name = 'Strength & Muscle Building Challenge'), (select id from exercises where name = 'Weighted Dips')),
('T-Bar Row', '4 sets of 8', 'Hard', (select id from challenges where name = 'Strength & Muscle Building Challenge'), (select id from exercises where name = 'T-Bar Row')),
('Push-ups', '3 sets of 10', 'Easy', (select id from challenges where name = 'Home Workout Challenge'), (select id from exercises where name = 'Push-ups')),
('Bodyweight Squats', '3 sets of 15', 'Easy', (select id from challenges where name = 'Home Workout Challenge'), (select id from exercises where name = 'Bodyweight Squats')),
('Diamond Push-ups', '3 sets of 8', 'Medium', (select id from challenges where name = 'Home Workout Challenge'), (select id from exercises where name = 'Diamond Push-ups')),
('Inverted Rows', '3 sets of 10', 'Medium', (select id from challenges where name = 'Home Workout Challenge'), (select id from exercises where name = 'Inverted Rows')),
('Pull-ups', '3 sets of 5', 'Hard', (select id from challenges where name = 'Home Workout Challenge'), (select id from exercises where name = 'Pull-ups')),
('Wall Sit', '3 holds of 60 seconds', 'Hard', (select id from challenges where name = 'Home Workout Challenge'), (select id from exercises where name = 'Wall Sit')),
('Drink 8 glasses of water today', 'Spread them through the day, one with every meal.', 'Easy', (select id from challenges where name = 'Healthy Nutrition Plan Challenge'), NULL),
('Eat a piece of fruit with breakfast', 'An apple, a banana or a handful of dates all count.', 'Easy', (select id from challenges where name = 'Healthy Nutrition Plan Challenge'), NULL),
('Fill half your lunch plate with vegetables', 'Raw or cooked, any colour.', 'Medium', (select id from challenges where name = 'Healthy Nutrition Plan Challenge'), NULL),
('No sugary drinks for a whole day', 'Water, milk or tea without sugar instead.', 'Medium', (select id from challenges where name = 'Healthy Nutrition Plan Challenge'), NULL),
('Plan tomorrow''s three meals tonight', 'Write down breakfast, lunch and dinner.', 'Hard', (select id from challenges where name = 'Healthy Nutrition Plan Challenge'), NULL),
('Follow your chosen nutrition plan all day', 'Pick a plan on the Nutrition plans page first.', 'Hard', (select id from challenges where name = 'Healthy Nutrition Plan Challenge'), NULL);
