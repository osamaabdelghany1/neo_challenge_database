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


CREATE TABLE muscles(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    latin_name VARCHAR(255),
    description TEXT NOT NULL,
    muscle_group VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL,
    function TEXT NOT NULL,
    origin TEXT,
    insertion TEXT,
    muscle_type VARCHAR(100),
    difficulty_to_train VARCHAR(50),
    image_url VARCHAR(500),
    video_url VARCHAR(500),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

select * from muscles;

CREATE TABLE exercises(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    muscle_id INTEGER NOT NULL,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    equipment_needed VARCHAR(255),
    difficulty VARCHAR(50),
    video_url VARCHAR(500),
    FOREIGN KEY (muscle_id) REFERENCES muscles(id)
);