-- SQLite
CREATE TABLE survey_responses(
user_id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT DEFAULT 'Anonymous',
age INTEGER,
gender TEXT,
sleep_hours REAL,
screen_time REAL,
exercise_days INTEGER,
academic_stress INTEGER,
social_support INTEEGER,
cyberbullying INTEGER,
substance_use INTEGER,
mood_score INTEGER,
suicidal_thoughts INTEGER,
timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
