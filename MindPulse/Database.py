import sqlite3

#------------------------
# GET DATABASE CONNECTION
#------------------------
def get_connection():
    conn = sqlite3.connect("mindpulse.db", check_same_thread=False)
    return conn


#-------------
# CREATE TABLE
#-------------
def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS survey_responses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        gender TEXT,
        sleep_hours REAL,
        screen_time REAL,
        exercise_days INTEGER,
        academic_stress INTEGER,
        social_support INTEGER,
        cyberbullying INTEGER,
        substance_use INTEGER,
        mood_score INTEGER,
        suicidal_thoughts INTEGER
    )
    """)

    conn.commit()
    conn.close()


#-----------------------
# INSERT SURVEY RESPONSE
#-----------------------
def insert_response(name, age, gender, sleep_hours, screen_time,
                    exercise_days, academic_stress, social_support,
                    cyberbullying, substance_use, mood_score,
                    suicidal_thoughts):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO survey_responses (
        name, age, gender, sleep_hours, screen_time,
        exercise_days, academic_stress, social_support,
        cyberbullying, substance_use, mood_score,
        suicidal_thoughts
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        name, age, gender, sleep_hours, screen_time,
        exercise_days, academic_stress, social_support,
        cyberbullying, substance_use, mood_score,
        suicidal_thoughts
    ))

    conn.commit()
    conn.close()