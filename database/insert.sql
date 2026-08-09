INSERT INTO challenges
(name, number_of_levels, number_of_activities, category, duration, description)
VALUES
('30 Day Fitness Challenge',5,10,'Sports',30,'Improve your strength and endurance in 30 days.'),

('Morning Cardio',3,6,'Sports',14,'Daily cardio exercises for beginners.'),

('Strength Builder',4,8,'Sports',21,'Increase muscle strength with progressive workouts.'),

('English Vocabulary',5,10,'Languages',30,'Learn new English words every day.'),

('Basic Spanish',4,8,'Languages',21,'Practice common Spanish phrases and vocabulary.'),

('French Beginner',3,6,'Languages',14,'Start learning basic French.'),

('World Geography',5,10,'General Knowledge',30,'Test your knowledge of countries and capitals.'),

('Science Facts',4,8,'General Knowledge',21,'Learn interesting scientific facts.'),

('History Quiz',3,6,'General Knowledge',14,'Explore famous historical events.');





INSERT INTO activities
(name,description,category,difficulty,challenge_id)
VALUES

-- Sports Challenge 1
('Push Ups','Complete 20 push ups','Sports','Easy',1),
('Squats','Complete 25 squats','Sports','Easy',1),
('Plank','Hold plank for 60 seconds','Sports','Medium',1),
('Jump Rope','Jump rope for 5 minutes','Sports','Medium',1),
('Burpees','Complete 15 burpees','Sports','Hard',1),

-- Sports Challenge 2
('Walking','Walk 3 kilometers','Sports','Easy',2),
('Jogging','Jog for 20 minutes','Sports','Medium',2),
('Mountain Climbers','30 repetitions','Sports','Hard',2),

-- Sports Challenge 3
('Bench Press','3 sets of bench press','Sports','Hard',3),
('Deadlift','3 sets of deadlift','Sports','Hard',3),

-- Languages Challenge 4
('10 New Words','Learn 10 English words','Languages','Easy',4),
('Reading','Read a short English article','Languages','Medium',4),
('Listening','Listen to an English podcast','Languages','Medium',4),

-- Languages Challenge 5
('Spanish Greetings','Learn greetings','Languages','Easy',5),
('Spanish Numbers','Learn numbers 1-100','Languages','Easy',5),
('Spanish Conversation','Practice conversation','Languages','Medium',5),

-- Languages Challenge 6
('French Alphabet','Learn alphabet','Languages','Easy',6),
('French Greetings','Practice greetings','Languages','Easy',6),

-- General Knowledge Challenge 7
('Countries','Identify world countries','General Knowledge','Easy',7),
('Capitals','Match countries with capitals','General Knowledge','Medium',7),
('Flags','Recognize country flags','General Knowledge','Hard',7),

-- General Knowledge Challenge 8
('Solar System','Learn about planets','General Knowledge','Easy',8),
('Human Body','Study body organs','General Knowledge','Medium',8),

-- General Knowledge Challenge 9
('Ancient Egypt','Learn Ancient Egypt history','General Knowledge','Easy',9),
('World War II','Historical events quiz','General Knowledge','Hard',9);





INSERT INTO Nutrition_Plans
(bmi,category,goal,calories,breakfast,lunch,dinner,water_intake)
VALUES

(17.5,'Weight Gain','Gain 5 kg',3200,
'Oatmeal with milk and bananas',
'Chicken with rice',
'Steak with potatoes',
'3 Liters'),

(20.5,'Maintain Weight','Maintain current weight',2500,
'Eggs and toast',
'Grilled chicken salad',
'Fish with vegetables',
'2.5 Liters'),

(23.0,'Maintain Weight','Healthy lifestyle',2400,
'Greek yogurt and fruits',
'Turkey sandwich',
'Grilled salmon',
'2.5 Liters'),

(27.5,'Weight Loss','Lose 5 kg',1800,
'Oatmeal',
'Grilled chicken',
'Vegetable soup',
'3 Liters'),

(32.0,'Weight Loss','Lose 10 kg',1500,
'Boiled eggs',
'Tuna salad',
'Grilled vegetables',
'3.5 Liters');





INSERT INTO user
(username,email,password,DOB,height,weight,phone,ssn)
VALUES

('Ahmed','ahmed@gmail.com','123456','2000-05-10',175,72,'01011111111','111111111'),

('Sara','sara@gmail.com','123456','1999-08-22',165,58,'01022222222','222222222'),

('Mohamed','mohamed@gmail.com','123456','2001-02-15',180,85,'01033333333','333333333'),

('Mona','mona@gmail.com','123456','1998-11-09',162,60,'01044444444','444444444'),

('Omar','omar@gmail.com','123456','2002-03-19',178,77,'01055555555','555555555'),

('Nour','nour@gmail.com','123456','2000-12-01',168,63,'01066666666','666666666'),

('Youssef','youssef@gmail.com','123456','1997-06-18',182,90,'01077777777','777777777'),

('Laila','laila@gmail.com','123456','2001-09-30',160,55,'01088888888','888888888'),

('Khaled','khaled@gmail.com','123456','1996-04-25',176,80,'01099999999','999999999'),

('Mariam','mariam@gmail.com','123456','2003-01-14',167,59,'01111111111','101010101');






INSERT INTO user_nutrition_plans
(user_id,nutrition_plan_id)
VALUES

(1,2),
(2,3),
(3,1),
(4,3),
(5,2),
(6,3),
(7,1),
(8,4),
(9,2),
(10,5);