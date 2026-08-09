CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    DOB DATE NOT NULL,
    height DECIMAL(3, 2),
    weight DECIMAL(3, 2), 
    phone VARCHAR(20), 
    ssn VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


create table user_challenges (
    user_id INTEGER NOT NULL,
    challenge_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (challenge_id) REFERENCES challenges(id)
);




-- drop table if exists users;

create table challenges (
  name VARCHAR(255) NOT NULL,
    number_of_levels INTEGER NOT NULL,
    number_of_activities INTEGER NOT NULL,
    category VARCHAR(255) NOT NULL,
    duration INTEGER NOT NULL,
    description TEXT NOT NULL,   id INTEGER PRIMARY KEY AUTOINCREMENT,
   
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

create table activities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    category VARCHAR(255) NOT NULL,
    difficulty VARCHAR(255) NOT NULL,
    challenge_id int NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (challenge_id) REFERENCES challenges(id)
);




CREATE TABLE Nutrition_Plans (
    id INTeger PRIMARY KEY AUTOINCREMENT,
    bmi DECIMAL(4,2),
    category VARCHAR(30),
    goal VARCHAR(30),
    calories INT,
    breakfast TEXT,
    lunch TEXT,
    dinner TEXT,
    water_intake VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- drop table if exists nutrition_plans;

CREATE TABLE User_Nutrition_Plans (
    user_id INT NOT NULL,
    nutrition_plan_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (nutrition_plan_id) REFERENCES Nutrition_Plans(id)
);

INSERT INTO users (username, email, password, DOB, height, weight, phone, ssn) VALUES
('ahmed_hassan', 'ahmed.hassan@example.com', '$2b$10$examplehash0000000000001', '1998-03-12', 178.50, 75.20, '+201001234567', '000-00-0001'),
('sara_ali', 'sara.ali@example.com', '$2b$10$examplehash0000000000002', '2001-07-25', 165.00, 58.30, '+201009876543', '000-00-0002'),
('mohamed_yousef', 'mohamed.yousef@example.com', '$2b$10$examplehash0000000000003', '1995-11-02', 182.00, 82.10, '+201112223344', '000-00-0003'),
('layla_ibrahim', 'layla.ibrahim@example.com', '$2b$10$examplehash0000000000004', '1999-01-18', 160.00, 55.00, '+201223334455', '000-00-0004'),
('omar_khaled', 'omar.khaled@example.com', '$2b$10$examplehash0000000000005', '1993-09-09', 175.00, 79.60, '+201334445566', '000-00-0005'),
('nour_mostafa', 'nour.mostafa@example.com', '$2b$10$examplehash0000000000006', '2000-05-30', 168.00, 60.50, '+201445556677', '000-00-0006'),
('karim_fathy', 'karim.fathy@example.com', '$2b$10$examplehash0000000000007', '1997-12-14', 180.00, 85.00, '+201556667788', '000-00-0007'),
('mariam_saeed', 'mariam.saeed@example.com', '$2b$10$examplehash0000000000008', '2002-02-20', 162.50, 54.80, '+201667778899', '000-00-0008'),
('youssef_adel', 'youssef.adel@example.com', '$2b$10$examplehash0000000000009', '1996-06-06', 176.20, 73.40, '+201778889900', '000-00-0009'),
('hana_tarek', 'hana.tarek@example.com', '$2b$10$examplehash0000000000010', '1998-10-11', 170.00, 62.00, '+201889990011', '000-00-0010'),
('ali_mahmoud', 'ali.mahmoud@example.com', '$2b$10$examplehash0000000000011', '1994-04-04', 183.00, 88.30, '+201990001122', '000-00-0011'),
('rana_essam', 'rana.essam@example.com', '$2b$10$examplehash0000000000012', '2003-08-08', 158.00, 50.20, '+201001112233', '000-00-0012'),
('tamer_nabil', 'tamer.nabil@example.com', '$2b$10$examplehash0000000000013', '1992-01-01', 177.80, 80.00, '+201112223345', '000-00-0013'),
('dina_ashraf', 'dina.ashraf@example.com', '$2b$10$examplehash0000000000014', '2000-03-15', 163.00, 57.70, '+201223334456', '000-00-0014'),
('hossam_zaki', 'hossam.zaki@example.com', '$2b$10$examplehash0000000000015', '1999-07-07', 179.00, 76.50, '+201334445567', '000-00-0015');

INSERT INTO challenges (name, number_of_levels, number_of_activities, category, duration, description) VALUES
('Beginner Fitness Challenge', 3, 15, 'Sports', 14, 'A progressive program to build basic fitness through simple daily exercises, ideal for those who have never worked out before.'),
('Fat Burning Challenge', 4, 20, 'Sports', 30, 'A combined workout and nutrition plan over 30 days to burn fat and boost metabolism.'),
('Strength & Muscle Building Challenge', 5, 25, 'Sports', 30, 'Progressively harder resistance exercises with fitness metrics tracking to monitor muscle growth.'),
('Daily 10,000 Steps Challenge', 2, 10, 'Sports', 21, 'A simple daily habit to increase physical activity and improve overall health through regular walking.'),
('Home Workout Challenge', 3, 18, 'Sports', 21, 'No-equipment daily workouts designed to be done at home in under 30 minutes.'),
('Flexibility & Stretching Challenge', 2, 12, 'Sports', 14, 'Daily stretching routines to improve flexibility, posture, and reduce muscle tension.'),
('Yoga for Beginners Challenge', 3, 15, 'Sports', 21, 'Guided daily yoga sessions to build strength, balance, and mindfulness together.'),
('Healthy Nutrition Plan Challenge', 4, 20, 'Sports', 30, 'A daily meal-planning challenge with nutrition tips to build sustainable healthy eating habits.'),
('English for Beginners Challenge', 3, 18, 'Language', 21, 'Daily lessons and quizzes to build a strong foundation in English vocabulary and grammar.'),
('French Conversation Challenge', 4, 24, 'Language', 30, 'Progressive daily conversation exercises to improve fluency in French.'),
('Learn 500 Spanish Words Challenge', 5, 30, 'Language', 30, 'An intensive challenge to memorize and retain Spanish vocabulary using spaced repetition.'),
('German Grammar Challenge', 3, 15, 'Language', 14, 'Focused lessons on core German grammar with short daily quizzes.'),
('Business English Challenge', 4, 20, 'Language', 21, 'Daily lessons focused on professional vocabulary and workplace communication skills.'),
('Turkish for Travelers Challenge', 2, 12, 'Language', 14, 'Essential everyday phrases and vocabulary for traveling in Turkey.'),
('Italian Listening Practice Challenge', 3, 18, 'Language', 21, 'Daily audio lessons and comprehension quizzes to improve Italian listening skills.'),
('Advanced English Writing Challenge', 5, 25, 'Language', 30, 'Daily writing exercises and feedback to master advanced English composition skills.');

INSERT INTO activities (name, description, category, difficulty, challenge_id) VALUES
('Push Ups', 'Complete 20 push ups', 'Sports', 'Easy', 1),
('Squats', 'Complete 25 squats', 'Sports', 'Easy', 1),
('Plank', 'Hold plank for 60 seconds', 'Sports', 'Medium', 1),
('Jump Rope', 'Jump rope for 5 minutes', 'Sports', 'Medium', 1),
('Burpees', 'Complete 15 burpees', 'Sports', 'Hard', 1),
('Walking', 'Walk 3 kilometers', 'Sports', 'Easy', 2),
('Jogging', 'Jog for 20 minutes', 'Sports', 'Medium', 2),
('Mountain Climbers', '30 repetitions', 'Sports', 'Hard', 2),
('Bench Press', '3 sets of bench press', 'Sports', 'Hard', 3),
('Deadlift', '3 sets of deadlift', 'Sports', 'Hard', 3),
('10 New Words', 'Learn 10 English words', 'Languages', 'Easy', 4),
('Reading', 'Read a short English article', 'Languages', 'Medium', 4),
('Listening', 'Listen to an English podcast', 'Languages', 'Medium', 4),
('Spanish Greetings', 'Learn greetings', 'Languages', 'Easy', 5),
('Spanish Numbers', 'Learn numbers 1-100', 'Languages', 'Easy', 5),
('Spanish Conversation', 'Practice conversation', 'Languages', 'Medium', 5),
('French Alphabet', 'Learn alphabet', 'Languages', 'Easy', 6),
('French Greetings', 'Practice greetings', 'Languages', 'Easy', 6),
('Countries', 'Identify world countries', 'General Knowledge', 'Easy', 7),
('Capitals', 'Match countries with capitals', 'General Knowledge', 'Medium', 7),
('Flags', 'Recognize country flags', 'General Knowledge', 'Hard', 7),
('Solar System', 'Learn about planets', 'General Knowledge', 'Easy', 8),
('Human Body', 'Study body organs', 'General Knowledge', 'Medium', 8),
('Ancient Egypt', 'Learn Ancient Egypt history', 'General Knowledge', 'Easy', 9),
('World War II', 'Historical events quiz', 'General Knowledge', 'Hard', 9);

INSERT INTO Nutrition_Plans (bmi, category, goal, calories, breakfast, lunch, dinner, water_intake) VALUES
(16.50, 'Underweight', 'Gain Weight', 3000, 'Oatmeal with milk and nuts', 'Chicken with rice', 'Salmon with potatoes', '3.5 Liters'),
(17.20, 'Underweight', 'Gain Weight', 2900, 'Peanut butter toast', 'Beef with pasta', 'Chicken with sweet potato', '3 Liters'),
(18.10, 'Underweight', 'Gain Weight', 2800, 'Eggs and whole wheat bread', 'Turkey with rice', 'Fish with vegetables', '3 Liters'),
(19.50, 'Normal', 'Maintain Weight', 2400, 'Greek yogurt and fruit', 'Grilled chicken with quinoa', 'Steak with vegetables', '2.5 Liters'),
(21.00, 'Normal', 'Maintain Weight', 2300, 'Omelet with toast', 'Fish with brown rice', 'Chicken salad', '2.5 Liters'),
(22.80, 'Normal', 'Maintain Weight', 2200, 'Oats with banana', 'Turkey sandwich', 'Grilled salmon', '2.5 Liters'),
(24.50, 'Normal', 'Build Muscle', 2700, 'Protein pancakes', 'Chicken breast with rice', 'Lean beef with potatoes', '3 Liters'),
(23.20, 'Normal', 'Build Muscle', 2600, 'Eggs with oats', 'Beef and pasta', 'Chicken with vegetables', '3 Liters'),
(22.00, 'Normal', 'Build Muscle', 2500, 'Protein smoothie', 'Grilled fish with rice', 'Turkey with sweet potato', '3 Liters'),
(26.50, 'Overweight', 'Lose Weight', 1900, 'Boiled eggs', 'Grilled chicken salad', 'Vegetable soup', '3 Liters'),
(28.10, 'Overweight', 'Lose Weight', 1800, 'Greek yogurt', 'Tuna salad', 'Grilled fish with broccoli', '3 Liters'),
(29.70, 'Overweight', 'Lose Weight', 1700, 'Oatmeal', 'Turkey salad', 'Chicken with steamed vegetables', '3 Liters'),
(31.50, 'Obese', 'Lose Weight', 1600, 'Low-fat yogurt', 'Grilled chicken with vegetables', 'Vegetable soup with fish', '3.5 Liters'),
(34.20, 'Obese', 'Lose Weight', 1500, 'Boiled eggs and cucumber', 'Turkey breast salad', 'Grilled chicken', '3.5 Liters'),
(38.00, 'Obese', 'Lose Weight', 1400, 'Protein shake', 'Tuna with vegetables', 'Steamed fish with salad', '4 Liters');

INSERT INTO user_nutrition_plans (user_id, nutrition_plan_id) VALUES
(1, 2),
(2, 3),
(3, 1),
(4, 3),
(5, 2),
(6, 3),
(7, 1),
(8, 4),
(9, 2),
(10, 5);
